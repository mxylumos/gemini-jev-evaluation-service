# Local evaluation results

Run at: `2026-09-30T17:08:44.213071+00:00`
Dataset: `/Users/yue/找工/TabbyML/Assignment/data/evaluation_dataset.jsonl`
Endpoint: `http://127.0.0.1:8000/v1/systemone`

| Completed | Correct | Failed | Accuracy |
| ---: | ---: | ---: | ---: |
| 26 | 24 | 0 | 92.31% |

## Per-case results

| # | ID | Task | Expected | Predicted | Result | Weights (probabilities / noul) | Confidence | Model | Attempts |
| ---: | --- | --- | --- | --- | --- | --- | ---: | --- | ---: |
| 1 | `ag-news-train-29994` | news_topic_classification | `world` | `world` | correct | `{"world":0.99,"sports":0.0,"business":0.005,"sci_tech":0.005}` | 0.99 | `gemini/gemini-3.8-flash` | 1 |
| 2 | `ag-news-train-29998` | news_topic_classification | `world` | `world` | correct | `{"world":0.98,"sports":0.0,"business":0.01,"sci_tech":0.01}` | 0.98 | `gemini/gemini-3.8-flash` | 1 |
| 3 | `ag-news-train-29992` | news_topic_classification | `sports` | `sports` | correct | `{"world":0.0,"sports":1.0,"business":0.0,"sci_tech":0.0}` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 4 | `ag-news-train-29993` | news_topic_classification | `sports` | `sports` | correct | `{"world":0.0,"sports":1.0,"business":0.0,"sci_tech":0.0}` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 5 | `ag-news-train-29997` | news_topic_classification | `business` | `business` | correct | `{"world":0.01,"sports":0.0,"business":0.98,"sci_tech":0.01}` | 0.98 | `gemini/gemini-3.8-flash` | 1 |
| 6 | `ag-news-train-29990` | news_topic_classification | `sci_tech` | `sci_tech` | correct | `{"world":0.05,"sports":0.0,"business":0.1,"sci_tech":0.85}` | 0.85 | `gemini/gemini-3.8-flash` | 1 |
| 7 | `ag-news-train-30003` | news_topic_classification | `sci_tech` | `sci_tech` | correct | `{"world":0.01,"sports":0.01,"business":0.28,"sci_tech":0.7}` | 0.7 | `gemini/gemini-3.8-flash` | 1 |
| 8 | `ag-news-train-00003` | news_topic_classification | `business` | `world` | incorrect | `{"world":0.75,"sports":0.0,"business":0.24,"sci_tech":0.01}` | 0.75 | `gemini/gemini-3.8-flash` | 1 |
| 9 | `ag-news-train-00030` | news_topic_classification | `business` | `business` | correct | `{"world":0.2,"sports":0.0,"business":0.7,"sci_tech":0.1}` | 0.7 | `gemini/gemini-3.8-flash` | 1 |
| 10 | `ag-news-train-00038` | news_topic_classification | `business` | `sci_tech` | incorrect | `{"world":0.01,"sports":0.0,"business":0.09,"sci_tech":0.9}` | 0.9 | `gemini/gemini-3.8-flash` | 1 |
| 11 | `ag-news-train-00078` | news_topic_classification | `sci_tech` | `sci_tech` | correct | `{"world":0.01,"sports":0.15,"business":0.09,"sci_tech":0.75}` | 0.75 | `gemini/gemini-3.8-flash` | 1 |
| 12 | `ag-news-train-00090` | news_topic_classification | `sci_tech` | `sci_tech` | correct | `{"world":0.32,"sports":0.01,"business":0.02,"sci_tech":0.65}` | 0.65 | `gemini/gemini-3.8-flash` | 1 |
| 13 | `ag-news-train-00073` | news_topic_classification | `business` | `business` | correct | `{"world":0.02,"sports":0.01,"business":0.62,"sci_tech":0.35}` | 0.62 | `gemini/gemini-3.8-flash` | 1 |
| 14 | `boolq-train-00000` | passage_grounded_boolean_qa | `true` | `true` | correct | `1.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 15 | `boolq-train-00004` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 16 | `boolq-train-00009` | passage_grounded_boolean_qa | `true` | `true` | correct | `1.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 17 | `boolq-train-00010` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 18 | `boolq-train-00013` | passage_grounded_boolean_qa | `true` | `true` | correct | `1.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 19 | `boolq-train-00015` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 20 | `boolq-train-00006` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 21 | `boolq-train-00012` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 22 | `boolq-train-00023` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 23 | `boolq-train-00031` | passage_grounded_boolean_qa | `true` | `true` | correct | `1.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 24 | `boolq-train-00036` | passage_grounded_boolean_qa | `true` | `true` | correct | `1.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 25 | `boolq-train-00037` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |
| 26 | `boolq-train-00029` | passage_grounded_boolean_qa | `false` | `false` | correct | `0.0` | 1.0 | `gemini/gemini-3.8-flash` | 1 |