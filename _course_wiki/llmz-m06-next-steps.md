---
title: "Next Steps — LLM Zoomcamp Module 6"
summary: "In this module, we covered hybrid search and document reranking,
two of the most impactful techniques for improving RAG quality."
related_course:
  - llmz-module-06
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 6: Best Practices](/course-wiki/llmz-module-06/) › Next Steps

## Notes

# Next Steps

In this module, we covered hybrid search and document reranking,
two of the most impactful techniques for improving RAG quality.

The key takeaways:

- Hybrid search combines vector and keyword search for better
  retrieval. It works because vector search captures semantic
  meaning while keyword search catches exact term matches.
- Reranking re-orders results with a better relevance score. Even
  a simple RRF implementation can improve metrics.
- LangChain wraps Elasticsearch functionality in a cleaner
  interface, but the underlying queries are the same.

## Other techniques to explore

We only covered two of the five techniques from the intro lesson.

Here are pointers for the rest:

- Small-to-big chunk retrieval: use small chunks for embedding
  but retrieve surrounding context for the LLM. Look at
  LangChain's ParentDocumentRetriever.
- Document metadata: add titles, topics, dates as filterable
  fields in your search index. Use them to narrow results before
  ranking.
- Query rewriting: ask an LLM to reformulate the user's question
  into a clearer search query before hitting the database.

## To learn more

Check out these resources:

- [Advanced RAG techniques overview](https://arxiv.org/abs/2312.10997)
- [LangChain retrieval docs](https://python.langchain.com/docs/concepts/retrievers/)

## Key concepts

- [Hybrid Search](/course-wiki/hybrid-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/06-best-practices/05-next-steps.md)
