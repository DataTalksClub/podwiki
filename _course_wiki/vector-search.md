---
title: "Vector Search"
summary: "Nearest-neighbor retrieval over embedding vectors — semantic search that matches meaning, not just words."
related_course:
  - Agentic RAG
  - Embeddings
  - Hybrid Search
  - Keyword Search
  - LLM Evaluation
  - LangChain
  - RAG
  - Reranking
---

Vector search retrieves documents by the closeness of their embedding vectors to the query's vector. Because the vectors encode meaning, a question about 'how do I reset my password' can retrieve a document that says 'change your credentials' without either sharing keywords. Module 2 implements it three ways in the course: minsearch (an in-memory approach), sqlitesearch, and PGVector for Postgres.

The module also teaches the operational layer: indexing the whole knowledge base, querying efficiently, and combining scores. It is the retrieval engine for the RAG pipeline — and, via the hybrid-search module, half of an even stronger combined retriever.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Environment](/course-wiki/llmz-m01-environment/)
    - [RAG](/course-wiki/llmz-m01-rag/)
    - [Search](/course-wiki/llmz-m01-search/)
    - [The LLM](/course-wiki/llmz-m01-the-llm/)
    - [RAG Helper](/course-wiki/llmz-m01-rag-helper/)
    - [Data Ingestion](/course-wiki/llmz-m01-data-ingestion/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
    - [Agents](/course-wiki/llmz-m01-agents/)
    - [Quick RAG Revision (Optional)](/course-wiki/llmz-m01-quick-rag-revision-optional/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [Embeddings](/course-wiki/llmz-m02-embeddings/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search-2/)
    - [Vector Search with minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
    - [Using ONNX Runtime instead of PyTorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
    - [Search Evaluation](/course-wiki/llmz-m04-search-evaluation/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Best Practices for RAG](/course-wiki/llmz-m06-best-practices-for-rag/)
    - [Hybrid Search](/course-wiki/llmz-m06-hybrid-search/)
    - [Hybrid Search with LangChain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
## Related concepts

- [Embeddings](/course-wiki/embeddings/)
- [RAG](/course-wiki/rag/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Agentic RAG](/course-wiki/agentic-rag/)
