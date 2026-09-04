---
title: "Reranking"
summary: "A second-pass model that reorders retrieved documents by true relevance to the query."
related_course:
  - Hybrid Search
  - Keyword Search
  - LLM Evaluation
  - LangChain
  - RAG
  - Vector Search
---

Reranking is precision work on top of fast retrieval: retrieve a generous candidate set (say 50 documents) with cheap vector or keyword search, then score each candidate against the query with a heavier cross-encoder model that actually reads query and document together, and keep only the top few for the prompt.

The course positions it as the last quality lever before generation: first-stage retrieval optimizes recall at speed, the reranker optimizes the ordering of what reaches the LLM. Better context ordering measurably improves answers — which the evaluation module's harness is there to verify.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Best Practices for RAG](/course-wiki/llmz-m06-best-practices-for-rag/)
    - [Document Reranking](/course-wiki/llmz-m06-document-reranking/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
## Related concepts

- [Hybrid Search](/course-wiki/hybrid-search/)
- [Vector Search](/course-wiki/vector-search/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
- [RAG](/course-wiki/rag/)
- [Keyword Search](/course-wiki/keyword-search/)
