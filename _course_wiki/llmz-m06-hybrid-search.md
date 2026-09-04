---
title: "Hybrid Search — LLM Zoomcamp Module 6"
summary: "Vector search finds documents by semantic meaning, while keyword search finds documents by exact word matches. Hybrid search combines both."
related_course:
  - llmz-module-06
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 6: Best Practices](/course-wiki/llmz-module-06/) › Hybrid Search

## Notes

# Hybrid Search

Vector search finds documents by semantic meaning, while keyword search
finds documents by exact word matches. Hybrid search combines both.

Each search produces a ranked list with scores.

We combine them with a weighted sum:

```text
score = alpha * vector_score + (1 - alpha) * keyword_score
```

When `alpha = 1`, it's pure vector search. When `alpha = 0`, it's pure
keyword search, and values in between give a mix.

## Reciprocal Rank Fusion

Another approach is fusion: merge the ranked lists from each search
method and compute a combined score based on rankings.

Reciprocal Rank Fusion (RRF) is a simple fusion method. The score
for each document is the sum of `1 / (k + rank + 1)` across all
lists where it appears.

Here is how it works with an example.

- text search: `[A, B, C, D, E]`
- vector search: `[C, B, F, G, A]`
- they have 3 documents in common (A, B, C)

With `k = 1`:

```text
Vector ranks:  C=0, B=1, F=2, G=3, A=4

RRF scores:
  A = 1/(1+0+1) + 1/(1+4+1) = 0.500 + 0.167 = 0.667
  B = 1/(1+1+1) + 1/(1+1+1) = 0.333 + 0.333 = 0.667
  C = 1/(1+2+1) + 1/(1+0+1) = 0.250 + 0.500 = 0.750
  D = 1/(1+3+1)              = 0.200
  E = 1/(1+4+1)              = 0.167
  F =              1/(1+2+1) = 0.250
  G =              1/(1+3+1) = 0.200

Final ranking: C, A/B (tie), F, D/G (tie), E
```

C wins because it ranks high in both lists. Documents that only
appear in one list get lower scores.

The parameter `k` smooths the
differences between ranks - higher `k` means rank position matters
less.

This algorithm works with any number of ranked lists, not just two.
So in our implementation we can generalize to an arbitrary number
of ranked results.

Let's implement it:

```python
def rrf(search_results, k=1, num_results=10):
    scores = {}
    doc_map = {}

    for results in search_results:
        for rank, doc in enumerate(results):
            key = doc["question"]
            if key not in scores:
                scores[key] = 0
                doc_map[key] = doc
            scores[key] += 1 / (k + rank + 1)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_map[key] for key, _ in ranked[:num_results]]
```

Let's put everything together:

```python
def hybrid_search(query, course="data-engineering-zoomcamp", num_results=10):
    keyword_results = keyword_search(query, course=course, num_results=num_results)
    vector_results = vector_search(query, course=course, num_results=num_results)
    return rrf([keyword_results, vector_results], num_results=num_results)
```

## Key concepts

- [Hybrid Search](/course-wiki/hybrid-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/06-best-practices/02-hybrid-search.md)
