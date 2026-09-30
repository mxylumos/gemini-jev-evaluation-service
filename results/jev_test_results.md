# Jev Playground test results

This file records manual Jev Playground runs for the current 26-case benchmark. The matching inputs are in [jev_requests.md](../data/jev_requests.md).

## Summary

| Metric | Value |
| --- | ---: |
| Requests completed | 26 |
| Correct | 23 |
| Incorrect | 3 |
| Failed | 0 |
| Accuracy | 88.46% |

## Per-case results

| # | ID | Task | Expected | Predicted | Result | Probabilities / noul | Confidence | Notes |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `ag-news-train-29994` | news topic | `world` | `world` | correct | world: 100%; sci_tech: 0%; business: 0%; sports not shown | 100% | Playground screenshot |
| 2 | `ag-news-train-29998` | news topic | `world` | `world` | correct | world: 100%; sci_tech: 0%; sports: 0%; business not shown | 100% | Playground screenshot |
| 3 | `ag-news-train-29992` | news topic | `sports` | `sports` | correct | sports: 100%; sci_tech: 0%; world: 0%; business not shown | 100% | Playground screenshot |
| 4 | `ag-news-train-29993` | news topic | `sports` | `sports` | correct | sports: 100%; sci_tech: 0%; world: 0%; business not shown | 100% | Playground screenshot |
| 5 | `ag-news-train-29997` | news topic | `business` | `business` | correct | business: 100%; sci_tech: 0%; sports: 0%; world not shown | 100% | Playground screenshot |
| 6 | `ag-news-train-29990` | news topic | `sci_tech` | `sci_tech` | correct | sci_tech: 98%; business: 2%; world: 0%; sports not shown | 98% | Playground screenshot |
| 7 | `ag-news-train-30003` | news topic | `sci_tech` | `sci_tech` | correct | sci_tech: 86%; business: 14%; sports: 0%; world not shown | 82% | Playground screenshot |
| 8 | `boolq-train-00000` | passage-grounded boolean | `true` | `true` | correct | noul / true: 74% | — | Playground screenshot |
| 9 | `boolq-train-00004` | passage-grounded boolean | `false` | `false` | correct | noul / true: 5% | — | Playground screenshot |
| 10 | `boolq-train-00009` | passage-grounded boolean | `true` | `true` | correct | noul / true: 98% | — | Playground screenshot |
| 11 | `boolq-train-00010` | passage-grounded boolean | `false` | `false` | correct | noul / true: 5% | — | Playground screenshot |
| 12 | `boolq-train-00013` | passage-grounded boolean | `true` | `true` | correct | noul / true: 93% | — | Playground screenshot |
| 13 | `boolq-train-00015` | passage-grounded boolean | `false` | `false` | correct | noul / true: 3% | — | Playground screenshot |
| 14 | `ag-news-train-00003` | news topic | `business` | `world` | incorrect | world: 94%; business: 6%; sci_tech: 0%; sports not shown | 92% | Playground screenshot |
| 15 | `ag-news-train-00030` | news topic | `business` | `world` | incorrect | world: 51%; business: 34%; sci_tech: 15%; sports not shown | 35% | Playground screenshot |
| 16 | `ag-news-train-00038` | news topic | `business` | `sci_tech` | incorrect | sci_tech: 98%; business: 2%; world: 0%; sports not shown | 98% | Playground screenshot |
| 17 | `ag-news-train-00078` | news topic | `sci_tech` | `sci_tech` | correct | sci_tech: 62%; sports: 23%; business: 15%; world not shown | 49% | Playground screenshot |
| 18 | `ag-news-train-00090` | news topic | `sci_tech` | `sci_tech` | correct | sci_tech: 59%; world: 41%; sports: 0%; business not shown | 45% | Playground screenshot |
| 19 | `boolq-train-00006` | passage-grounded boolean | `false` | `false` | correct | noul / true: 3% | — | Playground screenshot |
| 20 | `boolq-train-00012` | passage-grounded boolean | `false` | `false` | correct | noul / true: 6% | — | Playground screenshot |
| 21 | `boolq-train-00023` | passage-grounded boolean | `false` | `false` | correct | noul / true: 4% | — | Playground screenshot |
| 22 | `boolq-train-00031` | passage-grounded boolean | `true` | `true` | correct | noul / true: 86% | — | Playground screenshot |
| 23 | `boolq-train-00036` | passage-grounded boolean | `true` | `true` | correct | noul / true: 94% | — | Playground screenshot |
| 24 | `boolq-train-00037` | passage-grounded boolean | `false` | `false` | correct | noul / true: 5% | — | Playground screenshot |
| 25 | `ag-news-train-00073` | news topic | `business` | `business` | correct | business: 60%; sci_tech: 40%; sports: 0%; world not shown | 46% | Playground screenshot |
| 26 | `boolq-train-00029` | passage-grounded boolean | `false` | `false` | correct | noul / true: 15% | — | Playground screenshot |
