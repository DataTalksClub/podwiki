---
title: "Keyword Search"
summary: "The baseline retrieval method: matching query terms against document text with full-text search techniques."
related_course:
  - Embeddings
  - Function Calling
  - Hybrid Search
  - RAG
  - Reranking
  - Vector Search
---

LLM Zoomcamp starts retrieval with keyword search — no embeddings, no vector database. Documents are indexed with an inverted index (the approach behind minsearch and classic full-text engines like Elasticsearch), queries match on term overlap with optional boosting of important fields, and scoring ranks the matches.

The course's point is practical: keyword search is cheap, explainable, and surprisingly strong on FAQ-style data. Later modules reintroduce it in hybrid search, where combining keyword and vector retrieval outperforms either alone — so the baseline is not a stepping stone to discard but a component to keep.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Search](/course-wiki/llmz-m01-search/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Hybrid Search](/course-wiki/llmz-m06-hybrid-search/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
## Related concepts

- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Embeddings](/course-wiki/embeddings/)
