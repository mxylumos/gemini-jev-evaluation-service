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

[data/evaluation_dataset.jsonl](data/evaluation_dataset.jsonl) holds 26 labeled source records, ordered as 13 choice-only then 13 bool-only requests. Their provenance, selection, and label mapping are documented in [data/README.md](data/README.md).

For manual testing in Jev Playground, copy one complete State/Question pair at a time from [data/jev_requests.md](data/jev_requests.md). For the local service's `/docs` page, copy one complete JSON line at a time from [data/local_service_requests.jsonl](data/local_service_requests.jsonl) into the request body. The expected answers in `jev_requests.md` are for manual checking only and are not part of the API request.

## Run the full local dataset

With the local service running, evaluate all 26 records and write a Markdown report:

```bash
python run_local_evaluation.py
```

The script retries temporary `429`, `502`, and `503` responses with exponential backoff. The checked-in local evaluation results are in [results/local_results.md](results/local_results.md). Each case records its choice-probability distribution or `noul` probability, its confidence, and the provider model for direct comparison with Jev.

## Evaluation conclusion

Both services were evaluated against exactly the same 26 source-labeled cases: 13 AG News four-way topic classifications and 13 BoolQ passage-grounded yes/no decisions. The local Gemini-backed service completed every request and answered 24 of 26 correctly (**92.31%**). Jev Playground also completed every request and answered 23 of 26 correctly (**88.46%**).

| Task | Local Gemini | Jev Playground | Interpretation |
| --- | ---: | ---: | --- |
| AG News `choice` | 11 / 13 (84.62%) | 10 / 13 (76.92%) | The only errors for either system occur here. |
| BoolQ `noul` | 13 / 13 (100%) | 13 / 13 (100%) | Both systems consistently follow the supplied passage for this sample. |
| Overall | 24 / 26 (92.31%) | 23 / 26 (88.46%) | Local Gemini is ahead by one case on this benchmark. |

The local errors are both deliberately selected AG News boundary cases whose source label is `business`: row 3 concerns Iraqi oil exports during conflict and was predicted as `world`; row 38 discusses IBM's email research and was predicted as `sci_tech`. Jev has the same two types of ambiguity, but on three cases: it predicted rows 3 and 30 as `world` and row 38 as `sci_tech`, where all three source labels are `business`. In other words, the disagreement is not random across the benchmark; it is concentrated where an article's subject matter overlaps business with international affairs, safety/politics, or technology.

These figures should be read as an evaluation of this fixed, deliberately small benchmark rather than a general ranking of the underlying models. The AG News labels are the source-dataset ground truth even when an alternative category can sound plausible, and the five chosen boundary cases make that limitation visible. Likewise, the returned probabilities and confidence values are useful diagnostic signals, but they are not directly comparable across providers: Gemini reports structured-output estimates normalized by this service, whereas Jev reports its own model-specific values. The per-case evidence, including every prediction, probability, confidence, and retry count, is available in [the local results](results/local_results.md) and [the Jev Playground results](results/jev_test_results.md).
