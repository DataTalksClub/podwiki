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
  - Docker
  - Hybrid Search
  - Streamlit
---

RAG is the architecture LLM Zoomcamp is built around. A user question is answered in three steps: retrieve relevant documents from a knowledge base (search over your own data), assemble them into a prompt with the question, and have the LLM generate an answer grounded in that context. The model explains your documents instead of guessing from its training data.

Module 1 builds the pipeline in its simplest form — keyword search over a FAQ dataset, a prompt template, an OpenAI API call — then spends the course hardening each stage: better retrieval with vectors, answer quality measurement in the evaluation module, and feedback loops in monitoring.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Introduction](/course-wiki/llmz-m01-introduction/)
    - [RAG](/course-wiki/llmz-m01-rag/)
    - [The Course FAQ Dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
    - [Search](/course-wiki/llmz-m01-search/)
    - [The LLM](/course-wiki/llmz-m01-the-llm/)
    - [RAG Helper](/course-wiki/llmz-m01-rag-helper/)
    - [Data Ingestion](/course-wiki/llmz-m01-data-ingestion/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
    - [Agents](/course-wiki/llmz-m01-agents/)
    - [Quick RAG Revision (Optional)](/course-wiki/llmz-m01-quick-rag-revision-optional/)
    - [Function Calling](/course-wiki/llmz-m01-function-calling/)
    - [Other Frameworks](/course-wiki/llmz-m01-other-frameworks/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [Vector Search with minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
    - [Next Steps](/course-wiki/llmz-m02-next-steps/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
    - [Best Practices](/course-wiki/llmz-m03-best-practices/)
    - [Next Steps](/course-wiki/llmz-m03-next-steps/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
    - [Search Evaluation](/course-wiki/llmz-m04-search-evaluation/)
    - [Search Parameter Tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
    - [RAG and Agent Evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
    - [Generating RAG Answers](/course-wiki/llmz-m04-generating-rag-answers/)
    - [LLM as a Judge](/course-wiki/llmz-m04-llm-as-a-judge/)
    - [Agent Evaluation](/course-wiki/llmz-m04-agent-evaluation/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [Assistant](/course-wiki/llmz-m05-assistant/)
    - [Chat App](/course-wiki/llmz-m05-chat-app/)
    - [Capturing Metrics](/course-wiki/llmz-m05-capturing-metrics/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [User Feedback](/course-wiki/llmz-m05-user-feedback/)
    - [Built-in Judge](/course-wiki/llmz-m05-built-in-judge/)
    - [Docker Compose](/course-wiki/llmz-m05-docker-compose/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Best Practices for RAG](/course-wiki/llmz-m06-best-practices-for-rag/)
    - [Next Steps](/course-wiki/llmz-m06-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Evaluating Retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
    - [Evaluating RAG](/course-wiki/llmz-m07-evaluating-rag/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
    - [Chunking for Longer Texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
    - [Content Processing Cases and Steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
## Related concepts

- [Agentic RAG](/course-wiki/agentic-rag/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Embeddings](/course-wiki/embeddings/)
- [Vector Search](/course-wiki/vector-search/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
