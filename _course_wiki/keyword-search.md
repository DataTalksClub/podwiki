---
title: "Keyword Search"
summary: "The baseline retrieval method: matching query terms against document text with full-text search techniques."
related_course:
  - RAG
  - Vector Search
  - Hybrid Search
  - Embeddings
---

LLM Zoomcamp starts retrieval with keyword search — no embeddings, no vector database. Documents are indexed with an inverted index (the approach behind minsearch and classic full-text engines like Elasticsearch), queries match on term overlap with optional boosting of important fields, and scoring ranks the matches.

The course's point is practical: keyword search is cheap, explainable, and surprisingly strong on FAQ-style data. Later modules reintroduce it in hybrid search, where combining keyword and vector retrieval outperforms either alone — so the baseline is not a stepping stone to discard but a component to keep.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 1: Agentic RAG
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 6: Best Practices (Hybrid Search)

## Related concepts

- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)
- [Hybrid Search](/course-wiki/hybrid-search/)
- [Embeddings](/course-wiki/embeddings/)
