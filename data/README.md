# Evaluation dataset

`evaluation_dataset.jsonl` contains 26 independently labeled evaluation cases:

| Task | Count | Expected-answer type | Source |
| --- | ---: | --- | --- |
| News-topic classification | 13 | `"world"`, `"sports"`, `"business"`, or `"sci_tech"` | [AG News on Hugging Face](https://huggingface.co/datasets/fancyzhx/ag_news) |
| Passage-grounded yes/no evaluation | 13 | JSON boolean (`true` or `false`) | [BoolQ on Hugging Face](https://huggingface.co/datasets/google/boolq) |

## Provenance and selection

The examples were retrieved on 2026-09-25 from each dataset's `train` split via the Hugging Face dataset viewer. Every record stores the original dataset row in `source.row_index`, its split, and its dataset URL, making the selection reproducible.

- **AG News:** Seven representative rows (29994, 29998, 29992, 29993, 29997, 29990, 30003) are combined with six harder boundary rows (3, 30, 38, 73, 78, 90). The added row 73 concerns Apple and music downloads but has the source label `business`, making it a technology/business boundary. AG News documents the integer-label mapping as `0 -> World`, `1 -> Sports`, `2 -> Business`, and `3 -> Sci/Tech`; labels were normalized to the lowercase API keys above.
- **BoolQ:** Six representative rows (0, 4, 9, 10, 13, 15) are combined with seven harder rows (6, 12, 23, 29, 31, 36, 37). The added row 29 distinguishes saline solution (a mixture) from sodium chloride, a fine-grained semantic distinction. The original `passage`, `question`, and boolean `answer` are preserved.

The expected answers are source-dataset labels only; Jev was not run to generate or alter them.

## Record schema

Each JSON Lines record is one test case:

- `state` is the shared input a Jev-compatible request will provide.
- `questions` holds named typed questions; this dataset uses service-neutral `classification` and `boolean` labels.
- `expected` holds the source label keyed by the same question name.
- `source` records provenance for auditing and replaying the selection.

## Jev mapping

The HTTP service implements Jev's actual `choice` and `noul` primitives. For evaluation, translate each record without changing its state or expected label:

- `classification` -> a `choice` question. Its `labels` become `criteria` keys and its expected string remains the expected `choice` answer.
- `boolean` -> a `noul` question. Its expected JSON boolean becomes `true` when the returned `noul` probability is at least `0.5`, otherwise `false`.

This keeps the source data format concise while using Jev's wire-level question types at the service boundary.
