---
title: "Vector Search — LLM Zoomcamp Module 2"
summary: "--- video_url: 'https://www.youtube.com/watch?v=h-_tdBc24qc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Vector Search"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Vector Search

## Notes

---
video_url: "https://www.youtube.com/watch?v=h-_tdBc24qc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Vector Search

In the previous lesson we embedded our FAQ dataset into a matrix `X`
with 1208 document vectors. Here we see how vector search works under
the hood.

## Scoring documents

We have a matrix `X` with all document embeddings. We take a query,
compare it against every document, and keep the most similar ones.

When a query comes in, we embed it:

```python
query = "Can I still join the course after the start date?"
v_query = model.encode(query)
```

Next, we compute the dot product against all documents:

```python
scores = X.dot(v_query)
```

This is matrix-vector multiplication. Each element `i` of `scores` is
the cosine similarity between document `i` (row `i` of `X`) and
`v_query`.

We could compute the same thing with a for loop:

```python
scores = [v_query.dot(X[i]) for i in range(len(X))]
```

But `X.dot(v_query)` is much faster. Numpy runs optimized C code instead
of looping in Python, so the matrix version is hard to beat. The outcome
is the same either way: one score per document.

## Best match

The highest score is the most similar document:

```python
idx = np.argmax(scores)
idx, scores[idx]
```

This returns document 553 with score 0.76.

The index and score may differ for you. Our FAQ is a living document, so
we add and remove entries over time.

Let's see which document it is:

```python
documents[idx]
```

We see:

```python
{"id": "3f1424af17",
 "course": "data-engineering-zoomcamp",
 "section": "General Course-Related Questions",
 "question": "Course: Can I still join the course after the start date?",
 "answer": "Yes, even if you don't register, you're still eligible..."}
```

## Top 5 results

Usually we want more than the single best match, so let's pull the top
5.

`np.argsort` sorts from lowest to highest, so the last 5 are the top
ones:

```python
top5 = np.argsort(scores)[-5:]
```

They come out smallest-first, so we reverse them to get the highest
first:

```python
top5 = top5[::-1]
top5
```

Now we can read off the top 5 scores:

```python
scores[top5]
```

There's a shorter trick I usually reach for. We negate the scores
first, so the largest becomes the smallest. Then `argsort` puts the best
matches at the front.

Here it is in one line:

```python
top5 = np.argsort(-scores)[:5]
```

It looks cryptic the first time you see it. But it's a common way to
turn a min-sort into a max-sort.

Let's read off the actual documents:

```python
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

This is vector search in its simplest form. We embed the query, compute
dot products against all documents, and return the highest-scoring ones.

We return 5 and not the single best for a reason. The answer to a
question can be spread across several documents. One holds part of it,
another fills in the rest. Sometimes the top result isn't the right one
but the second is. We send all 5 to the LLM and let it combine them.

The number 5 is a starting point, picked on gut feeling. Later, when we
evaluate search quality, we can test whether 3 or 10 works better for
our data.

Doing this by hand with numpy is fine for a small dataset. A larger one
needs a library that also handles filtering and ranking. That's what we
turn to next.

## Key concepts

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
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=h-_tdBc24qc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/04-vector-search.md)
