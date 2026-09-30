# Jev-compatible service

This repository contains the first two parts of the assignment:

- a 26-case labeled dataset based on AG News and BoolQ, including deliberately ambiguous boundary cases; and
- an HTTP service that mirrors the relevant parts of TypeSafe AI's Jev `systemone` endpoint using Gemini.

## Run it

Requires Python 3.11+ and a Gemini API key. The service reads a local `.gemini_api_key` file by default; that file is Git-ignored. Create a key in [Google AI Studio](https://aistudio.google.com/apikey).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .gemini_api_key.example .gemini_api_key
# Open .gemini_api_key and paste one newly created Gemini API key on its own line.
uvicorn app.main:app --reload
```

The service listens at `http://127.0.0.1:8000`. `GET /health` needs no API key. API documentation is available at `/docs` while the service is running.

## Endpoint

`POST /v1/systemone` accepts the same top-level `state`, `model`, and named `questions` shape as [Jev's System One API](https://docs.typesafe.ai/api). This implementation supports the two Jev primitives required by the dataset:

- `choice` for AG News's four topic labels;
- `noul` for BoolQ's passage-grounded yes/no decision.

```json
{
  "state": {"text": "Vodafone introduces a new BlackBerry device."},
  "model": "jev-latest",
  "questions": {
    "topic": {
      "type": "choice",
      "instructions": "Which news topic best classifies this article?",
      "criteria": {
        "world": "International affairs, politics, diplomacy, conflict, or major world events.",
        "sports": "Sports competitions, athletes, teams, or sporting organizations.",
        "business": "Companies, markets, finance, jobs, trade, or the economy.",
        "sci_tech": "Technology, science, software, devices, research, or space."
      }
    },
    "is_technology_or_science": {
      "type": "noul",
      "instructions": "Is this article primarily about technology or science?"
    }
  }
}
```

Responses preserve question ids and return typed answers, probabilities, and token usage. Invalid request bodies receive FastAPI/Pydantic `422` responses with field-level details. Gemini authentication/provider errors become actionable `502` responses; rate limits return `429`. The default provider model is `gemini-3.8-flash`.

Jev Playground may show State and Question in separate editors. To mirror that workflow, this local service also accepts `question` as an alias for `questions`; its value must remain the named-question map, for example `{"question": {"topic": {"type": "choice", "instructions": "...", "criteria": {"world": "..."}}}}`. Send either `questions` or `question`, never both.

## Intentional differences from Jev

- The `model` request field is accepted for wire compatibility but inference always uses `GEMINI_MODEL`; the response identifies it as `gemini/<model>`.
- Jev supports `choice`, `score`, and `noul`; this assignment service implements only `choice` and `noul`, the dataset's needs.
- Jev's calibrated confidence is model-specific. For `choice`, this service reports the largest normalized Gemini probability. Jev returns no separate `noul` confidence, but this service adds `confidence = |noul - 0.5| * 2` because the assignment asks for confidence on every answer.
- Gemini is prompted to produce probability estimates through [Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output); these are not Jev-calibrated probabilities.

## Dataset and manual requests

[data/evaluation_dataset.jsonl](data/evaluation_dataset.jsonl) holds the 26 labeled source records. Their provenance, selection, and label mapping are documented in [data/README.md](data/README.md).

For manual testing in Jev Playground, copy one complete State/Question pair at a time from [data/requests.md](data/requests.md). For the local service's `/docs` page, copy one complete JSON line at a time from [data/local_service_requests.jsonl](data/local_service_requests.jsonl) into the request body. The expected answers in `requests.md` are for manual checking only and are not part of the API request.

## Run the full local dataset

With the local service running, evaluate all 26 records and write a Markdown report:

```bash
python run_local_evaluation.py
```

The script retries temporary `429`, `502`, and `503` responses with exponential backoff. The checked-in local evaluation results are in [results/local_results.md](results/local_results.md). Each case records its choice-probability distribution or `noul` probability, its confidence, and the provider model for direct comparison with Jev.

## Evaluation conclusion

Both services were evaluated against the same 26 source-labeled cases (13 AG News topic classifications and 13 BoolQ passage-grounded yes/no decisions). The local Gemini-backed service answered 24 of 26 cases correctly (**92.31%**); Jev Playground answered 23 of 26 correctly (**88.46%**). The detailed runs are available in [the local results](results/local_results.md) and [the Jev Playground results](results/jev_test_results.md).

The Boolean cases were correct for both services. The remaining errors were intentionally included topic-boundary cases: local Gemini classified AG News rows 38 and 73 as `sci_tech` rather than the source `business` label, while Jev classified rows 3 and 30 as `world` and row 38 as `sci_tech` rather than `business`. These results show that both implementations handle the two task types reliably, while the residual disagreement is concentrated in the known ambiguous business/technology/world boundaries of AG News.
