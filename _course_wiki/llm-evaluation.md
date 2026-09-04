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

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [CRISP-DM](/course-wiki/mlz-m01-crisp-dm/)
    - [Summary](/course-wiki/mlz-m01-summary/)
  - [Module 4: Evaluation Metrics for Classification](/course-wiki/mlz-module-04/)
    - [Evaluation metrics: session overview](/course-wiki/mlz-m04-evaluation-metrics-session-overview/)
    - [Cross-Validation](/course-wiki/mlz-m04-cross-validation/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Building the Prompt](/course-wiki/llmz-m01-building-the-prompt/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Embeddings](/course-wiki/llmz-m02-embeddings/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
    - [Generating Ground Truth Data](/course-wiki/llmz-m04-generating-ground-truth-data/)
    - [Generating Ground Truth for All Documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
    - [Search Evaluation](/course-wiki/llmz-m04-search-evaluation/)
    - [Search Evaluation Metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
    - [Search Parameter Tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
    - [RAG and Agent Evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
    - [Generating RAG Answers](/course-wiki/llmz-m04-generating-rag-answers/)
    - [LLM as a Judge](/course-wiki/llmz-m04-llm-as-a-judge/)
    - [Agent Evaluation](/course-wiki/llmz-m04-agent-evaluation/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [Capturing Metrics](/course-wiki/llmz-m05-capturing-metrics/)
    - [User Feedback](/course-wiki/llmz-m05-user-feedback/)
    - [Built-in Judge](/course-wiki/llmz-m05-built-in-judge/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Best Practices for RAG](/course-wiki/llmz-m06-best-practices-for-rag/)
    - [Document Reranking](/course-wiki/llmz-m06-document-reranking/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Evaluating Retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
    - [Evaluating RAG](/course-wiki/llmz-m07-evaluating-rag/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
    - [Chunking for Longer Texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
    - [Content Processing Cases and Steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
  - [Module 3: Analytical Modeling](/course-wiki/sma-module-03/)
    - [Analytical Modeling](/course-wiki/sma-m03-analytical-modeling/)
## Related concepts

- [LLM Monitoring](/course-wiki/llm-monitoring/)
- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Agentic RAG](/course-wiki/agentic-rag/)
