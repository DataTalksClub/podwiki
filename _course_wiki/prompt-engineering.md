---
title: "Prompt Engineering"
summary: "Designing the instructions and context an LLM responds to: prompt structure, examples, and iteration against real outputs."
related_course:
  - RAG
  - Function Calling
  - LLM Evaluation
  - OpenAI API
  - RAG
---

LLM Zoomcamp treats the prompt as the core programmable surface of an LLM application: a template that combines instructions, the retrieved context, and the user question. Module 1 builds the RAG prompt step by step — role and instructions, context section, question section — and shows how each part affects answer quality.

The course's evaluation module closes the loop: prompt variants are A/B-compared on a golden question set instead of judged by vibes, which is the discipline that separates prompt engineering from guessing. Token limits and API costs shape how much context a prompt can carry.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 8: Neural Networks and Deep Learning](/course-wiki/mlz-module-08/)
    - [Installation of tensorflow](/course-wiki/mlz-m08-installation-of-tensorflow/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Introduction](/course-wiki/llmz-m01-introduction/)
    - [RAG](/course-wiki/llmz-m01-rag/)
    - [Building the Prompt](/course-wiki/llmz-m01-building-the-prompt/)
    - [The LLM](/course-wiki/llmz-m01-the-llm/)
    - [RAG Helper](/course-wiki/llmz-m01-rag-helper/)
    - [Data Ingestion](/course-wiki/llmz-m01-data-ingestion/)
    - [Wrap-up of Part 1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
    - [Agents](/course-wiki/llmz-m01-agents/)
    - [Quick RAG Revision (Optional)](/course-wiki/llmz-m01-quick-rag-revision-optional/)
    - [Function Calling](/course-wiki/llmz-m01-function-calling/)
    - [The Agentic Loop](/course-wiki/llmz-m01-the-agentic-loop/)
    - [ToyAIKit](/course-wiki/llmz-m01-toyaikit/)
    - [Other Frameworks](/course-wiki/llmz-m01-other-frameworks/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [RAG with Vector Search](/course-wiki/llmz-m02-rag-with-vector-search/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Context Engineering](/course-wiki/llmz-m03-context-engineering/)
    - [AI Copilot](/course-wiki/llmz-m03-ai-copilot/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
    - [Multi-Agent Systems](/course-wiki/llmz-m03-multi-agent-systems/)
    - [Best Practices](/course-wiki/llmz-m03-best-practices/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
    - [Search Parameter Tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
    - [RAG and Agent Evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
    - [Generating RAG Answers](/course-wiki/llmz-m04-generating-rag-answers/)
    - [LLM as a Judge](/course-wiki/llmz-m04-llm-as-a-judge/)
    - [Agent Evaluation](/course-wiki/llmz-m04-agent-evaluation/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [Assistant](/course-wiki/llmz-m05-assistant/)
    - [Capturing Metrics](/course-wiki/llmz-m05-capturing-metrics/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [Querying Data](/course-wiki/llmz-m05-querying-data/)
    - [Streamlit Dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
    - [User Feedback](/course-wiki/llmz-m05-user-feedback/)
    - [Built-in Judge](/course-wiki/llmz-m05-built-in-judge/)
    - [Synthetic Data Generation](/course-wiki/llmz-m05-synthetic-data-generation/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Evaluating Retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
    - [Evaluating RAG](/course-wiki/llmz-m07-evaluating-rag/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
## Related concepts

- [RAG](/course-wiki/rag/)
- [Function Calling](/course-wiki/function-calling/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
- [OpenAI API](/course-wiki/openai-api/)
- [RAG](/course-wiki/rag/)
