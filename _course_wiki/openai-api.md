---
title: "OpenAI API"
summary: "The hosted LLM API the courses call for generation and embeddings — models, chat completions, and token costs."
related_course:
  - Prompt Engineering
  - RAG
  - Function Calling
  - Embeddings
  - LLM Evaluation
---

The OpenAI API is the default LLM backend of LLM Zoomcamp: chat completions for generated answers, the embeddings endpoint for vector search, and function-calling parameters for the agentic modules. The course's dollar-a-few-credits budget teaches cost awareness — every prompt includes retrieved context, and context is billed in tokens.

The course keeps the provider at arm's length: base URLs and model names are configuration, so the same pipeline runs against other providers, including local models via Ollama. AI Dev Tools Zoomcamp's agents consume the same APIs indirectly through coding-agent tools.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Environment](/course-wiki/llmz-m01-environment/)
    - [RAG](/course-wiki/llmz-m01-rag/)
    - [The LLM](/course-wiki/llmz-m01-the-llm/)
    - [RAG Helper](/course-wiki/llmz-m01-rag-helper/)
    - [Data Ingestion](/course-wiki/llmz-m01-data-ingestion/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
    - [Quick RAG Revision (Optional)](/course-wiki/llmz-m01-quick-rag-revision-optional/)
    - [Function Calling](/course-wiki/llmz-m01-function-calling/)
    - [The Agentic Loop](/course-wiki/llmz-m01-the-agentic-loop/)
    - [ToyAIKit](/course-wiki/llmz-m01-toyaikit/)
    - [Other Frameworks](/course-wiki/llmz-m01-other-frameworks/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
    - [Context Engineering](/course-wiki/llmz-m03-context-engineering/)
    - [Setting up Kestra](/course-wiki/llmz-m03-setting-up-kestra/)
    - [AI Copilot](/course-wiki/llmz-m03-ai-copilot/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Generating Ground Truth Data](/course-wiki/llmz-m04-generating-ground-truth-data/)
    - [Generating Ground Truth for All Documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
    - [Generating RAG Answers](/course-wiki/llmz-m04-generating-rag-answers/)
    - [LLM as a Judge](/course-wiki/llmz-m04-llm-as-a-judge/)
    - [Agent Evaluation](/course-wiki/llmz-m04-agent-evaluation/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Assistant](/course-wiki/llmz-m05-assistant/)
    - [Capturing Metrics](/course-wiki/llmz-m05-capturing-metrics/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [Streamlit Dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
    - [User Feedback](/course-wiki/llmz-m05-user-feedback/)
    - [Built-in Judge](/course-wiki/llmz-m05-built-in-judge/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Evaluating Retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
    - [Content Processing Cases and Steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Configuration](/course-wiki/aidt-m05-configuration/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Using an Orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 2: Workflow Orchestration](/course-wiki/dez-module-02/)
    - [2.5.2 - Context Engineering with ChatGPT](/course-wiki/dez-m02-2-5-2-context-engineering-with-chatgpt/)
## Related concepts

- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [RAG](/course-wiki/rag/)
- [Function Calling](/course-wiki/function-calling/)
- [Embeddings](/course-wiki/embeddings/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
