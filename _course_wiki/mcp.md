---
title: "MCP"
summary: "The Model Context Protocol: a standard way to connect agents to external tools and data sources."
related_course:
  - Agent Skills and Subagents
  - Coding Agents
  - Context Engineering
  - Git Worktrees
  - Neural Networks
  - Partitioning and Clustering
---

MCP is the protocol layer for agent extensions: instead of hand-wiring each tool into each agent, a tool exposes itself as an MCP server (documentation lookup, database queries, issue trackers — the course uses a Context7-style documentation server as the example), and any MCP-capable agent discovers and calls it through the standard interface.

Module 5 teaches the capability, not one product: servers define tools, resources, and prompts; clients (coding agents) enumerate them and invoke them mid-task. The protocol also carries the security discussion — an MCP server is code the agent will execute, so trust, scoping, and audit matter — which is the module's pairing of capability with constraint.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [Model Selection Process](/course-wiki/mlz-m01-model-selection-process/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
    - [Configuration](/course-wiki/aidt-m05-configuration/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 5: Data Platforms](/course-wiki/dez-module-05/)
    - [Getting Started with Bruin](/course-wiki/dez-m05-getting-started-with-bruin/)
    - [Using Bruin MCP with AI Agents](/course-wiki/dez-m05-using-bruin-mcp-with-ai-agents/)
## Related concepts

- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [Coding Agents](/course-wiki/coding-agents/)
- [Context Engineering](/course-wiki/context-engineering/)
- [Git Worktrees](/course-wiki/git-worktrees/)
