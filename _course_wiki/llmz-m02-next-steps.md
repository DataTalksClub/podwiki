---
title: "Next Steps — LLM Zoomcamp Module 2"
summary: "--- video_url: 'https://www.youtube.com/watch?v=vhNfnNUz3A0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Next Steps"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Next Steps

## Notes

---
video_url: "https://www.youtube.com/watch?v=vhNfnNUz3A0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Next Steps

In this module, we:

- Learned what embeddings are and how they turn text into vectors
- Generated embeddings for our FAQ dataset using sentence-transformers
- Built vector search with numpy, minsearch, sqlitesearch, and PGVector
- Integrated vector search into our RAG pipeline with the `RAGVector`
  class

The code is available in the
code directory.

## Using vector search

Text search is simple and fast, and for many applications it's all you
need. Start there.

Vector search adds real overhead:

- You need an embedding model
- You need to compute and store embeddings
- At query time you encode the query before you can search

Even with the smallest model that overhead is considerable, and that's
before counting the extra dependencies. Don't take it on without a
reason.

Most RAG tutorials assume you need vector search from the start. Quite a
few of them come from companies that sell vector databases. So of course
they push it. You don't need it on day one.

A reasonable progression:

1. v1: Start with text search. Get your RAG pipeline working end to end.
   For our FAQ dataset, text search already handles most questions well.
   We saw that in module 1.
2. v2: Add vector search when you can measure that text search misses
   relevant results. This happens when users ask questions in different
   words than what is in your documents.
3. v3: Combine both with hybrid search (text + vector), which typically
   outperforms either one alone.

The right time to move from one version to the next is when evaluation
shows it's justified. A later module covers how to evaluate search
quality and compare methods. With numbers in hand, you can tell a
marginal gain from a real one. A marginal gain isn't worth the overhead.
A real one is.

## Hybrid search and reranking

Once you have both text search and vector search, you can combine them.
Hybrid search runs both methods and merges the results using techniques
like Reciprocal Rank Fusion (RRF).

Reranking takes it further. After retrieving candidate documents, a
separate model re-scores them for relevance.

Both techniques can improve retrieval quality. We cover them in the
Hybrid Search lesson in the Best Practices module.

## Moving forward

Try these next steps:

- Compare text search and vector search on your own data
- Experiment with different embedding models
- Try PGVector with a larger dataset
- Try a different vector database - Elasticsearch, Qdrant,
  Weaviate, Chroma, or any other. The concepts are the same:
  embed documents, store vectors, search by similarity
- Evaluate your search results (covered in a later module)

## Key concepts

- [RAG](/course-wiki/rag/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Reranking](/course-wiki/reranking/)
- [Vector Search](/course-wiki/vector-search/)
- [Embeddings](/course-wiki/embeddings/)
- [Elasticsearch](/course-wiki/elasticsearch/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
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
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
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

- [Video](https://www.youtube.com/watch?v=vhNfnNUz3A0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/10-next-steps.md)
