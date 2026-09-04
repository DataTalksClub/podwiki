---
title: "Agentic RAG"
summary: "Letting the model control its own retrieval: deciding when to search, what to search for, and whether the answer is good enough."
related_course:
  - Function Calling
  - LLM Evaluation
  - Partitioning and Clustering
  - RAG
  - Regularization
  - Vector Search
---

Agentic RAG hands the retrieval step to the model. Instead of a fixed pipeline that always searches once and answers, the LLM is given search as a tool it can call: it reformulates the question, decides whether results are relevant, searches again with different terms, and answers when it has enough context — all through function calling.

The course frames this as the bridge from a fixed RAG pipeline to an agent: the retrieval logic moves from your code into the model's loop. The same search tools, prompts, and knowledge base serve the agentic version, which is why the module comes first.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Introduction](/course-wiki/llmz-m01-introduction/)
    - [Agents](/course-wiki/llmz-m01-agents/)
    - [Function Calling](/course-wiki/llmz-m01-function-calling/)
    - [The Agentic Loop](/course-wiki/llmz-m01-the-agentic-loop/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
## Related concepts

- [RAG](/course-wiki/rag/)
- [Function Calling](/course-wiki/function-calling/)
- [Vector Search](/course-wiki/vector-search/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
