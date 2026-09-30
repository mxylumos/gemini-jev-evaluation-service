#!/usr/bin/env python3
"""Run every labeled dataset record against the local Jev-compatible service."""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_DATASET = ROOT / "data" / "evaluation_dataset.jsonl"
DEFAULT_URL = "http://127.0.0.1:8000/v1/systemone"
DEFAULT_OUTPUT = ROOT / "results" / "local_evaluation_report.md"

TOPIC_CRITERIA = {
    "world": "International affairs, politics, diplomacy, conflict, or major world events.",
    "sports": "Sports competitions, athletes, teams, or sporting organizations.",
    "business": "Companies, markets, finance, jobs, trade, or the economy.",
    "sci_tech": "Technology, science, software, devices, research, or space.",
}


@dataclass
class CaseResult:
    id: str
    task: str
    expected: str | bool
    predicted: str | bool | None
    correct: bool | None
    attempts: int
    model: str | None = None
    weight: str | None = None
    confidence: float | None = None
    error: str | None = None


class RequestError(RuntimeError):
    def __init__(self, status: int | None, message: str) -> None:
        self.status = status
        super().__init__(message)


def load_dataset(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def to_request(record: dict[str, Any]) -> tuple[dict[str, Any], str, str | bool]:
    question_id, question = next(iter(record["questions"].items()))
    expected = record["expected"][question_id]["answer"]
    if question["type"] == "classification":
        api_question: dict[str, Any] = {
            "type": "choice",
            "instructions": question["prompt"],
            "criteria": {label: TOPIC_CRITERIA[label] for label in question["labels"]},
        }
    elif question["type"] == "boolean":
        api_question = {
            "type": "noul",
            "instructions": question["prompt"],
            "criteria": {
                "true": "The answer to the supplied question is yes, based only on the supplied passage.",
                "false": "The answer is no, based only on the supplied passage.",
            },
        }
    else:
        raise ValueError(f"Unsupported dataset question type: {question['type']}")
    # The local service accepts this Playground-style alias in addition to Jev's
    # official top-level `questions` field. Keep the named key (`topic`/`answer`).
    return {"state": record["state"], "model": "jev-latest", "question": {question_id: api_question}}, question_id, expected


def post_json(url: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RequestError(exc.code, f"HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RequestError(None, f"Network error: {exc.reason}") from exc


def evaluate_record(record: dict[str, Any], url: str, retries: int, retry_delay: float, timeout: int) -> CaseResult:
    payload, question_id, expected = to_request(record)
    attempts = 0
    for attempt in range(retries + 1):
        attempts += 1
        try:
            response = post_json(url, payload, timeout)
            answer = response["answers"][question_id]
            if answer["type"] == "choice":
                predicted: str | bool = answer["choice"]
                weight = json.dumps(answer["probabilities"], separators=(",", ":"))
            elif answer["type"] == "noul":
                noul = float(answer["noul"])
                predicted = noul >= 0.5
                weight = str(noul)
            else:
                raise ValueError(f"Unsupported returned answer type: {answer['type']}")
            confidence = answer.get("confidence")
            return CaseResult(
                record["id"], record["task"], expected, predicted, predicted == expected, attempts,
                response.get("model"), weight, float(confidence) if confidence is not None else None,
            )
        except (KeyError, TypeError, ValueError, RequestError) as exc:
            status = exc.status if isinstance(exc, RequestError) else None
            retryable = status in {429, 502, 503}
            if retryable and attempt < retries:
                time.sleep(retry_delay * (2**attempt))
                continue
            return CaseResult(record["id"], record["task"], expected, None, None, attempts, str(exc))
    raise AssertionError("unreachable")


def display(value: str | bool | None) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return str(value).lower()
    return value


def report(results: list[CaseResult], dataset: Path, url: str) -> str:
    completed = [result for result in results if result.correct is not None]
    correct = sum(result.correct for result in completed)
    accuracy = "N/A" if not completed else f"{correct / len(completed):.2%}"
    lines = [
        "# Local evaluation results",
        "",
        f"Run at: `{datetime.now(UTC).isoformat()}`",
        f"Dataset: `{dataset}`",
        f"Endpoint: `{url}`",
        "",
        "| Completed | Correct | Failed | Accuracy |",
        "| ---: | ---: | ---: | ---: |",
        f"| {len(completed)} | {correct} | {len(results) - len(completed)} | {accuracy} |",
        "",
        "## Per-case results",
        "",
        "| # | ID | Task | Expected | Predicted | Result | Weights (probabilities / noul) | Confidence | Model | Attempts |",
        "| ---: | --- | --- | --- | --- | --- | --- | ---: | --- | ---: |",
    ]
    for index, result in enumerate(results, 1):
        outcome = "correct" if result.correct else "incorrect" if result.correct is False else "failed"
        lines.append(
            f"| {index} | `{result.id}` | {result.task} | `{display(result.expected)}` | "
            f"`{display(result.predicted)}` | {outcome} | `{display(result.weight)}` | "
            f"{display(result.confidence)} | `{display(result.model)}` | {result.attempts} |"
        )
    failures = [result for result in results if result.error]
    if failures:
        lines.extend(["", "## Failed requests", ""])
        for result in failures:
            lines.extend([f"### `{result.id}`", "", "```text", result.error or "", "```", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--retries", type=int, default=4, help="Retries after the first attempt for 429/502/503 responses.")
    parser.add_argument("--retry-delay", type=float, default=2.0, help="Initial retry delay in seconds; it doubles after each retry.")
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()
    if args.retries < 0 or args.retry_delay < 0 or args.timeout <= 0:
        parser.error("retries and retry-delay must be non-negative; timeout must be positive")

    results = [evaluate_record(record, args.url, args.retries, args.retry_delay, args.timeout) for record in load_dataset(args.dataset)]
    output = report(results, args.dataset, args.url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(output)
    print(f"\nReport written to: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
