---
title: "Embeddings"
summary: "Representing text as vectors so similarity in meaning becomes closeness in space."
related_course:
  - Vector Search
  - RAG
  - Keyword Search
  - Hybrid Search
---

An embedding model maps text to a fixed-length vector such that texts with similar meanings land close together. LLM Zoomcamp's module 2 embeds the FAQ documents and the user's question into the same vector space, and retrieval becomes nearest-neighbor search: the documents whose vectors are closest to the question vector are the relevant ones.

The course covers the operational realities alongside the math: choosing an embedding model, computing and storing vectors (with sqlitesearch, minsearch, and PGVector as the course's storage options), and the cost model of calling an embedding API over a whole knowledge base.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 2: Vector Search

## Related concepts

- [Vector Search](/course-wiki/vector-search/)
- [RAG](/course-wiki/rag/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Hybrid Search](/course-wiki/hybrid-search/)
