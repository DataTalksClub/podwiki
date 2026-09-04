---
title: "AI Orchestration — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # AI Orchestration"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › AI Orchestration

## Notes

---
video_url: "https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# AI Orchestration

This module introduces AI-powered workflow orchestration using Kestra. You'll learn how AI can accelerate workflow development and enable autonomous task automation through three techniques: AI Copilot for generating flows, RAG for grounding responses in real data, and AI Agents for autonomous task execution.

## Learning Objectives

By the end of this module, you will:

- Understand the importance of context engineering in AI applications
- Use AI Copilot to build Kestra flows faster and more accurately
- Implement Retrieval Augmented Generation (RAG) to ground AI responses in real data
- Build autonomous AI agents that can make decisions and use tools dynamically
- Design multi-agent systems where specialized agents collaborate to solve complex tasks
- Apply best practices for using AI in production data workflows

## Prerequisites

- Kestra running locally (see Setting up Kestra)
- Google Cloud account with access to Gemini API
- Basic understanding of YAML and workflow concepts

> Note: The flows in this module use Gemini, but Kestra's AI plugins support any major provider — OpenAI, Gemini, Anthropic, and more. See the [full list of supported providers](https://kestra.io/plugins/plugin-ai/provider). You can swap the provider in your flows without changing anything else.

## Why AI for Workflows?

When building LLM applications and workflows, we often spend significant time writing boilerplate code, searching documentation, and structuring pipelines. AI tools can help us:

- Generate workflows faster: describe what you want in natural language instead of writing YAML from scratch
- Avoid errors: get syntax-correct, up-to-date code that follows best practices
- Automate complex decisions: let AI agents dynamically orchestrate tasks based on changing conditions
- Ground responses in data: use RAG to ensure AI provides accurate, contextual information

However, AI is only as good as the context we provide. This module teaches you how to engineer that context for reliable, production-ready workflows.

## What Makes This Different from AI Assistants?

Traditional AI assistants (like ChatGPT or Gemini in a browser) don't have context about your codebase and workflow patterns, real-time data from your systems, or the latest documentation and best practices.

By integrating AI directly into Kestra and using techniques like RAG and specialized agents, we can provide this context and get much better results.

## Key concepts

- [RAG](/course-wiki/rag/)
- [Context Engineering](/course-wiki/context-engineering/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Deployment Automation](/course-wiki/deployment-automation/)
- [Kestra](/course-wiki/kestra/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/01-intro.md)
