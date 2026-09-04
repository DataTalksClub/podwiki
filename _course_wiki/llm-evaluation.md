---
title: "LLM Evaluation"
summary: "Measuring retrieval quality and answer quality for RAG systems — before and after deployment."
related_course:
  - Agentic RAG
  - Classification Metrics
  - Function Calling
  - Hybrid Search
  - LLM Monitoring
  - LangChain
  - RAG
  - Reranking
  - Vector Search
---

Module 4 answers 'did my RAG change actually help?'. Evaluation splits in two: retrieval metrics (did the right documents make it into the context — hit rates, MRR over a golden test set of question-document pairs) and answer quality (is the generated answer correct, relevant, and grounded — judged by an LLM-as-a-judge against the retrieved documents).

The course builds a golden dataset from real user questions, then runs offline evaluation over candidate configurations (different retrieval methods, prompts, models) before anything ships. Online evaluation then continues the measurement in production from user feedback and monitored behavior — the handoff to the monitoring module.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 4: Evaluation

## Related concepts

- [LLM Monitoring](/course-wiki/llm-monitoring/)
- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Agentic RAG](/course-wiki/agentic-rag/)
