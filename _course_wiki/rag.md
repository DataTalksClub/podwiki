---
title: "RAG"
summary: "Retrieval-augmented generation: ground an LLM's answers in retrieved documents instead of relying on what it memorized."
related_course:
  - Agentic RAG
  - Embeddings
  - Function Calling
  - Keyword Search
  - LLM Evaluation
  - LLM Monitoring
  - LangChain
  - Reranking
  - Vector Search
---

RAG is the architecture LLM Zoomcamp is built around. A user question is answered in three steps: retrieve relevant documents from a knowledge base (search over your own data), assemble them into a prompt with the question, and have the LLM generate an answer grounded in that context. The model explains your documents instead of guessing from its training data.

Module 1 builds the pipeline in its simplest form — keyword search over a FAQ dataset, a prompt template, an OpenAI API call — then spends the course hardening each stage: better retrieval with vectors, answer quality measurement in the evaluation module, and feedback loops in monitoring.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 1: Agentic RAG

## Related concepts

- [Agentic RAG](/course-wiki/agentic-rag/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Embeddings](/course-wiki/embeddings/)
- [Vector Search](/course-wiki/vector-search/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
