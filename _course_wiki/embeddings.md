---
title: "Embeddings"
summary: "Representing text as vectors so similarity in meaning becomes closeness in space."
related_course:
  - FastAPI
  - Hybrid Search
  - Keyword Search
  - RAG
  - Risk Management
  - Vector Search
---

An embedding model maps text to a fixed-length vector such that texts with similar meanings land close together. LLM Zoomcamp's module 2 embeds the FAQ documents and the user's question into the same vector space, and retrieval becomes nearest-neighbor search: the documents whose vectors are closest to the question vector are the relevant ones.

The course covers the operational realities alongside the math: choosing an embedding model, computing and storing vectors (with sqlitesearch, minsearch, and PGVector as the course's storage options), and the cost model of calling an embedding API over a whole knowledge base.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [Embeddings](/course-wiki/llmz-m02-embeddings/)
    - [Embedding Our Dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search-2/)
    - [Vector Search with minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
    - [Using ONNX Runtime instead of PyTorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Hybrid Search with LangChain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [Chunking for Longer Texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
## Related concepts

- [Vector Search](/course-wiki/vector-search/)
- [RAG](/course-wiki/rag/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Hybrid Search](/course-wiki/hybrid-search/)
