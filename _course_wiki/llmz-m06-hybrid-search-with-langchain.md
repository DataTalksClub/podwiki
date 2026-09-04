---
title: "Hybrid Search with LangChain — LLM Zoomcamp Module 6"
summary: "So far we've been working with Elasticsearch directly. LangChain provides wrappers that simplify the code. In this lesson, we'll rewrite our hybrid search using LangChain's ElasticsearchRetriever."
related_course:
  - llmz-module-06
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 6: Best Practices](/course-wiki/llmz-module-06/) › Hybrid Search with LangChain

## Notes

# Hybrid Search with LangChain

So far we've been working with Elasticsearch directly. LangChain
provides wrappers that simplify the code. In this lesson, we'll
rewrite our hybrid search using LangChain's ElasticsearchRetriever.

The indexing stage stays the same - we still use the same
Elasticsearch index from the previous lesson. Only the retrieval
code changes.

## Installing LangChain

Install the LangChain packages:

```bash
uv add langchain langchain-elasticsearch langchain-huggingface
```

## Setting up the retriever

LangChain provides `ElasticsearchRetriever`, a wrapper around the
Elasticsearch client.

We configure it with a hybrid query function:

```python
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Dict
from langchain_elasticsearch import ElasticsearchRetriever

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
)

es_url = "http://localhost:9200"
```

Define a hybrid query function that combines keyword and vector search:

```python
def hybrid_query(search_query: str) -> Dict:
    vector = embedding.embed_query(search_query)
    return {
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": search_query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields",
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        },
        "knn": {
            "field": "question_text_vector",
            "query_vector": vector,
            "k": 5,
            "num_candidates": 10000,
        },
        "size": 5
    }
```

Create the retriever from the query function:

```python
hybrid_retriever = ElasticsearchRetriever.from_es_params(
    url=es_url,
    index_name="course-questions",
    body_func=hybrid_query,
    content_field="text"
)
```

Now we can search:

```python
query = "I just discovered the course. Can I still join it?"
results = hybrid_retriever.invoke(query)

for result in results:
    print(result.metadata["_source"]["question"])
    print(result.metadata["_score"])
```

## Evaluating with LangChain

To evaluate, we wrap the retriever in a function that works with
our ground truth data:

```python
def elastic_search_hybrid(field, query, course):
    def hybrid_query(search_query: str) -> Dict:
        vector = embedding.embed_query(search_query)
        return {
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": search_query,
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
            },
            "knn": {
                "field": field,
                "query_vector": vector,
                "k": 5,
                "num_candidates": 10000,
            },
            "size": 5
        }

    retriever = ElasticsearchRetriever.from_es_params(
        url=es_url,
        index_name="course-questions",
        body_func=hybrid_query,
        content_field="text"
    )
```

Run the retriever and format the results:

```python
    results = retriever.invoke(query)
    return [
        {
            "id": r.metadata["_source"]["id"],
            "question": r.metadata["_source"]["question"],
            "text": r.metadata["_source"]["text"],
        }
        for r in results
    ]

def question_text_hybrid(q):
    return elastic_search_hybrid("question_text_vector", q["question"], q["course"])

evaluate(ground_truth, question_text_

## Key concepts

- [Hybrid Search](/course-wiki/hybrid-search/)
- [Vector Search](/course-wiki/vector-search/)
- [LangChain](/course-wiki/langchain/)
- [Embeddings](/course-wiki/embeddings/)
- [Elasticsearch](/course-wiki/elasticsearch/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
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
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/06-best-practices/04-langchain.md)
