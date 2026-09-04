---
title: "Elasticsearch"
summary: "The production full-text search engine LLM Zoomcamp references for keyword retrieval at scale."
related_course:
  - Keyword Search
  - Hybrid Search
  - Vector Search
  - RAG
  - Reranking
---

Elasticsearch appears in LLM Zoomcamp as the industry-standard keyword retrieval engine: an inverted index over document fields, query-time boosting, and scoring — the production-grade version of the minsearch approach the course starts with. The course's search-evaluation lessons compare candidate retrieval methods, with Elasticsearch as the serious option when a FAQ corpus outgrows in-memory search.

The concepts transfer directly: the course's keyword-search baseline, hybrid search combinations, and reranking all plug into an Elasticsearch-backed pipeline the same way they plug into minsearch.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [RAG](/course-wiki/llmz-m01-rag/)
    - [Search](/course-wiki/llmz-m01-search/)
    - [Data Ingestion](/course-wiki/llmz-m01-data-ingestion/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Document Reranking](/course-wiki/llmz-m06-document-reranking/)
    - [Hybrid Search with LangChain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
## Related concepts

- [Keyword Search](/course-wiki/keyword-search/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Vector Search](/course-wiki/vector-search/)
- [RAG](/course-wiki/rag/)
- [Reranking](/course-wiki/reranking/)
