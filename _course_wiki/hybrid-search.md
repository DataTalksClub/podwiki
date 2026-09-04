---
title: "Hybrid Search"
summary: "Combining vector and keyword retrieval so semantic recall and exact-term precision reinforce each other."
related_course:
  - Embeddings
  - Keyword Search
  - LLM Evaluation
  - LangChain
  - Reranking
  - Vector Search
---

Hybrid search runs two retrievers over the same knowledge base — vector search for semantic similarity, keyword search for exact terms, codes, and names — and merges their results. Each covers the other's weakness: vectors miss rare exact tokens, keywords miss paraphrases.

The module shows the combination implemented with minsearch-style keyword scoring plus vector scores, blended into one ranking (typically via reciprocal rank fusion or weighted scores). The evaluation module's golden dataset is how the course proves the hybrid retriever actually beats either parent — measure first, then keep the winner.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 6: Best Practices

## Related concepts

- [Vector Search](/course-wiki/vector-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Reranking](/course-wiki/reranking/)
- [Embeddings](/course-wiki/embeddings/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
