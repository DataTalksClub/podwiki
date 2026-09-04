---
title: "Function Calling"
summary: "Giving an LLM typed tools it can invoke — the mechanism that turns a text generator into an agent."
related_course:
  - Agentic RAG
  - RAG
  - Keyword Search
  - LLM Evaluation
---

Function calling is the API mechanism for agents: you describe functions (name, purpose, parameters as JSON schema) to the model, and it responds not with text but with a request to call one of them with specific arguments. Your code executes the call and returns the result; the model continues from there.

LLM Zoomcamp uses it to expose search as a tool — the model decides when and what to search, iterating until it can answer. The course's point is that this one primitive generalizes: the same loop carries tools for database lookup, calculations, or actions, which is what makes an application agentic rather than a fixed pipeline.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 1: Agentic RAG

## Related concepts

- [Agentic RAG](/course-wiki/agentic-rag/)
- [RAG](/course-wiki/rag/)
- [Keyword Search](/course-wiki/keyword-search/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
