"""A small, Jev-compatible `/v1/systemone` HTTP service backed by Gemini."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Annotated, Any, Literal, Union

from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types
from pydantic import BaseModel, ConfigDict, Field, RootModel, model_validator


JsonValue = Union[dict[str, Any], list[Any], str, int, float, bool]


class ChoiceQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["choice"]
    instructions: JsonValue
    criteria: dict[str, JsonValue | None]

    @model_validator(mode="after")
    def validate_criteria(self) -> "ChoiceQuestion":
        if not self.criteria:
            raise ValueError("choice.criteria must contain at least one option")
        if len(self.criteria) > 255:
            raise ValueError("choice.criteria may contain at most 255 options")
        return self


class NoulCriteria(BaseModel):
    model_config = ConfigDict(extra="forbid")
    true: JsonValue | None = None
    false: JsonValue | None = None


class NoulQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["noul"]
    instructions: JsonValue
    criteria: NoulCriteria | None = None


Question = Annotated[Union[ChoiceQuestion, NoulQuestion], Field(discriminator="type")]


class Questions(RootModel[dict[str, Question]]):
    @model_validator(mode="after")
    def validate_questions(self) -> "Questions":
        if not self.root:
            raise ValueError("questions must contain at least one named question")
        return self


class SystemOneRequest(BaseModel):
    """The public request shape of TypeSafe's System One endpoint."""

    model_config = ConfigDict(extra="forbid")
    state: JsonValue
    model: str = Field(min_length=1)
    questions: Questions | None = None
    # Playground-style convenience alias: its value is still the named-question map.
    question: Questions | None = None

    @model_validator(mode="after")
    def normalize_question_field(self) -> "SystemOneRequest":
        if self.questions is not None and self.question is not None:
            raise ValueError("provide either questions or question, not both")
        if self.questions is None and self.question is None:
            raise ValueError("one of questions or question is required")
        if self.questions is None:
            self.questions = self.question
        return self


def _json_schema_for_answers(questions: dict[str, Question]) -> dict[str, Any]:
    """Create a strict Structured Outputs schema for one answer per question."""
    properties: dict[str, Any] = {}
    for question_id, question in questions.items():
        if isinstance(question, ChoiceQuestion):
            options = list(question.criteria)
            properties[question_id] = {
                "type": "object",
                "properties": {
                    "choice": {"type": "string", "enum": options},
                    "probabilities": {
                        "type": "object",
                        "properties": {option: {"type": "number", "minimum": 0, "maximum": 1} for option in options},
                        "required": options,
                        "additionalProperties": False,
                    },
                },
                "required": ["choice", "probabilities"],
                "additionalProperties": False,
            }
        else:
            properties[question_id] = {
                "type": "object",
                "properties": {"noul": {"type": "number", "minimum": 0, "maximum": 1}},
                "required": ["noul"],
                "additionalProperties": False,
            }
    return {
        "type": "object",
        "properties": properties,
        "required": list(questions),
        "additionalProperties": False,
    }


def _normalize_probabilities(raw: dict[str, Any], options: list[str]) -> dict[str, float]:
    values = {option: max(0.0, float(raw.get(option, 0.0))) for option in options}
    total = sum(values.values())
    if total <= 0:
        # Structured output should prevent this, but retain a useful result if a provider misbehaves.
        return {option: 1.0 / len(options) for option in options}
    return {option: value / total for option, value in values.items()}


def _confidence(probabilities: dict[str, float]) -> float:
    """A transparent proxy for Jev's undocumented calibrated confidence."""
    return round(max(probabilities.values()), 6)


class GeminiAnswerer:
    def __init__(self, client: Any | None = None) -> None:
        self.client = client or genai.Client(api_key=_gemini_api_key())
        self.model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

    def answer(self, request: SystemOneRequest) -> tuple[dict[str, Any], dict[str, int]]:
        questions = request.questions.root
        question_payload = {name: question.model_dump(mode="json") for name, question in questions.items()}
        instructions = (
            "You are an evaluation engine. Evaluate every named question independently against the supplied state. "
            "For a choice, choose the best criterion key and provide probabilities for every key that sum to 1. "
            "For a noul, return the probability (0=no, 1=yes) that its instruction is true. "
            "Use only the supplied state and question criteria."
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=json.dumps({"state": request.state, "questions": question_payload}, ensure_ascii=False),
            config=types.GenerateContentConfig(
                system_instruction=instructions,
                response_mime_type="application/json",
                response_json_schema=_json_schema_for_answers(questions),
            ),
        )
        try:
            raw_answers = json.loads(response.text)
        except (AttributeError, json.JSONDecodeError) as exc:
            raise RuntimeError("Gemini returned no valid structured output") from exc

        answers: dict[str, Any] = {}
        for question_id, question in questions.items():
            raw = raw_answers[question_id]
            if isinstance(question, ChoiceQuestion):
                probabilities = _normalize_probabilities(raw["probabilities"], list(question.criteria))
                choice = max(probabilities, key=probabilities.get)
                answers[question_id] = {
                    "type": "choice",
                    "choice": choice,
                    "probabilities": probabilities,
                    "confidence": _confidence(probabilities),
                }
            else:
                noul = min(1.0, max(0.0, float(raw["noul"])))
                answers[question_id] = {
                    "type": "noul",
                    "noul": noul,
                    # Extension: assignment asks for confidence for every question.
                    "confidence": round(abs(noul - 0.5) * 2, 6),
                }

        usage = getattr(response, "usage_metadata", None)
        return answers, {
            "input_tokens": int(getattr(usage, "prompt_token_count", 0) or 0),
            "output_tokens": int(getattr(usage, "candidates_token_count", 0) or 0),
        }


def _gemini_api_key() -> str:
    """Read the local-only Gemini key file, falling back to an environment variable."""
    key_file = Path(__file__).resolve().parent.parent / ".gemini_api_key"
    if key_file.is_file():
        key_lines = [
            line.strip()
            for line in key_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if len(key_lines) == 1:
            return key_lines[0]
        if len(key_lines) > 1:
            raise RuntimeError(
                ".gemini_api_key must contain exactly one non-comment, non-empty line"
            )

    environment_key = os.getenv("GEMINI_API_KEY")
    if environment_key:
        return environment_key

    raise RuntimeError(
        "Gemini API key is missing; add it to the local .gemini_api_key file or set GEMINI_API_KEY"
    )


app = FastAPI(title="Jev-compatible evaluation service", version="0.1.0")
answerer = GeminiAnswerer


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/systemone")
def system_one(request: SystemOneRequest) -> dict[str, Any]:
    try:
        answers, usage = answerer().answer(request)
    except UnicodeEncodeError as exc:
        raise HTTPException(
            status_code=500,
            detail="Gemini configuration contains non-ASCII characters; use a valid ASCII Gemini API key and restart the server",
        ) from exc
    except (KeyError, TypeError, ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=502, detail=f"Gemini returned an unusable answer: {exc}") from exc
    except Exception as exc:
        status_code = getattr(exc, "code", None)
        provider_message = str(exc).replace(_gemini_api_key(), "[redacted]")
        if status_code == 429:
            raise HTTPException(status_code=429, detail=f"Gemini rate limit reached: {provider_message}") from exc
        if status_code in (401, 403):
            raise HTTPException(
                status_code=502,
                detail=f"Gemini authentication failed; check .gemini_api_key: {provider_message}",
            ) from exc
        raise HTTPException(
            status_code=502,
            detail=f"Gemini provider request failed (status {status_code}): {provider_message}",
        ) from exc

    return {"model": f"gemini/{os.getenv('GEMINI_MODEL', 'gemini-3.8-flash')}", "answers": answers, "usage": usage}
