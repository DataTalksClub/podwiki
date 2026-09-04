---
title: "Document Reranking — LLM Zoomcamp Module 6"
summary: "When we retrieve documents, they're ranked by cosine similarity. But cosine similarity doesn't always reflect true relevance to the user's question. The most relevant document might be at position six, and we only return the top five."
related_course:
  - llmz-module-06
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 6: Best Practices](/course-wiki/llmz-module-06/) › Document Reranking

## Notes

# Document Reranking

When we retrieve documents, they're ranked by cosine similarity.
But cosine similarity doesn't always reflect true relevance to the
user's question. The most relevant document might be at position
six, and we only return the top five.

Reranking re-orders retrieved documents by a better relevance
score. It sits at the end of the search pipeline, after the
initial retrieval.

## Reciprocal Rank Fusion (RRF)

One popular reranking method is Reciprocal Rank Fusion (RRF). It
combines rankings from multiple search methods (vector, keyword,
etc.

) into a single score:

```text
RRF(d) = sum(1 / (k + rank(d))) for each ranking
```

where `k` is a constant (typically 60). Documents that appear
high in multiple rankings get a higher combined score.

## RRF in Elasticsearch

Elasticsearch 8.9+ supports RRF natively:

```python
def elastic_search_hybrid_rrf(field, query, vector, course):
    knn_query = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "boost": 0.5,
        "filter": {
            "term": {
                "course": course
            }
        }
    }

    keyword_query = {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields",
                    "boost": 0.5,
                }
            },
            "filter": {
                "term": {
                    "course": course
                }
            }
        }
    }
```

Then execute the search with RRF ranking:

```python
    response = es_client.search(
        index=index_name,
        query=keyword_query,
        knn=knn_query,
        size=5,
        rank={"rrf": {}}
    )

    return [hit["_source"] for hit in response["hits"]["hits"]]
```

Note: the built-in RRF requires a paid Elasticsearch subscription.
If you're using the free tier, you'll get an error.

## Implementing RRF ourselves

We can implement RRF manually.

The approach is to run vector and
keyword searches separately, compute RRF scores, and merge:

```python
def compute_rrf(rank, k=60):
    return 1 / (k + rank)

def elastic_search_hybrid_rrf(field, query, vector, course, k=60):
    knn_query = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "filter": {
            "term": {
                "course": course
            }
        }
    }
```

Define the keyword query and run both searches:

```python
    keyword_query = {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields",
                }
            },
            "filter": {
                "term": {
                    "course": course
                }
            }
        }
    }

    knn_response = es_client.search(
        index=index_name,
        knn=knn_query,
        size=5
    )

    keyword_response = es_client.search(
        index=index_name,
        query=keyword_query,
        size=5
    )
```

Now compute RRF scores from both result sets:

```python
    rrf_scores = {}

    for rank, hit in enumerate(knn_response["hits"]["hits"]):
        doc_id = hit["_source"]["id"]
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + compute_rrf(rank, k)

    for rank, hit in enumerate(keyword_response["hits"]["hits"]):
        doc_id = hit["_source"]["id"]
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + compute_rrf(rank, k)

    all_docs = {
        hit["_source"]["id"]: hit["_source"]
        for hit in knn_response["hits"]["hits"] + keyword_response["hits"]["hits"]
    }

    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

    return [all_docs[doc_id] for doc_id, _ in sorted_docs[:5]]
```

When the same document appear

## Key concepts

- [Reranking](/course-wiki/reranking/)
- [Elasticsearch](/course-wiki/elasticsearch/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
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
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/06-best-practices/03-reranking.md)
