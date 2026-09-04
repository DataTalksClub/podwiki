---
title: "Search Evaluation Metrics — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=TuirMy3Pdbk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Search Evaluation Metrics"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Search Evaluation Metrics

## Notes

---
video_url: "https://www.youtube.com/watch?v=TuirMy3Pdbk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Search Evaluation Metrics

In the previous lesson, we computed relevance lists for search results.
We can turn those lists into metrics.

## Hit Rate

Hit Rate (also called Recall@k) measures the fraction of queries where
the correct document appears anywhere in the results:

```python
example = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
]
```

Each line is one query. If a line contains `1`, search found the
correct document somewhere in the top 5 results. If the line contains
only zeros, search did not find the correct document.

In our setup, each query has one correct document, so Hit Rate and
Recall@k mean the same thing.

Let's calculate it:

```python
cnt = 0

for line in example:
    if 1 in line:
        cnt = cnt + 1

cnt
```

There are 14 hits. The example has 15 queries.

The Hit Rate is:

```python
cnt / len(example)
# 0.933
```

This means that search found the correct document for 93.3% of the
queries in this example.

Put the same logic into a function:

```python
def hit_rate(relevance):
    cnt = 0

    for line in relevance:
        if 1 in line:
            cnt = cnt + 1

    return cnt / len(relevance)
```

Check it on the same example:

```python
hit_rate(example)
# 0.933
```

## Mean Reciprocal Rank (MRR)

Hit Rate tells us if we found the right document, but not where it was.

MRR also considers the position.

For each query, the score is based on the rank of the first correct
document:

- position 1: score is 1.0
- position 2: score is 0.5
- position 3: score is 0.333
- not found: score is 0

In the example, most hits are at the first position. Some hits are
lower in the list.

Look at that line:

```python
example[1]
# [0, 1, 0, 0, 0]
```

For this line, the score is `1/2` because the correct document is at
position 2.

Let's calculate MRR:

```python
total_score = 0.0

for line in example:
    for rank in range(len(line)):
        if line[rank] == 1:
            total_score = total_score + 1 / (rank + 1)
            break

total_score
```

The total score is `12.333333333333334`. We use `rank + 1` because
Python counts positions from zero. The first position should score
`1/1`, and without the `+ 1` we'd divide by zero.

Divide it by the number of queries:

```python
total_score / len(example)
# 0.822
```

MRR is the average of these scores across all queries. It rewards
systems that put the correct document near the top.

Hit Rate is the upper bound for MRR. In practice, MRR is usually
smaller because some correct documents are found below the first
position.

Put the same logic into a function:

```python
def mrr(relevance):
    total_score = 0.0

    for line in relevance:
        for rank in range(len(line)):
            if line[rank] == 1:
                total_score = total_score + 1 / (rank + 1)
                break

    return total_score / len(relevance)
```

Check it on the same example:

```python
mrr(example)
# 0.822
```

## Putting it together

Wrap the metrics in a reusable evaluation function:

```python
def evaluate(ground_truth, search_function):
    relevance_total = compute_relevance_total(ground_truth, search_function)

    return {
        "hit_rate": hit_rate(relevance_total),
        "mrr": mrr(relevance_total),
    }
```

We can evaluate any search function:

```python
evaluate(
    ground_truth,
    text_search
)
```

You should see something like:

```python
{"hit_rate": 0.899, "mrr": 0.769}
```

Search metrics tell us whether retrieval works. Next, we'll use these
metrics to tune the search parameters.

## Interpreting the metrics

A few things to keep in mind when reading these numbers:

Our ground 

## Key concepts

- [Classification Metrics](/course-wiki/classification-metrics/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=TuirMy3Pdbk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/05-search-metrics.md)
