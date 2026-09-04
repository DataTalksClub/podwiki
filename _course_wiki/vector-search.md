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

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 2: Vector Search

## Related concepts

- [Embeddings](/course-wiki/embeddings/)
- [RAG](/course-wiki/rag/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Agentic RAG](/course-wiki/agentic-rag/)
