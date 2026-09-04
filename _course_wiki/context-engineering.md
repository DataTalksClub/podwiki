---
title: "Context Engineering"
summary: "Feeding coding agents durable project knowledge through AGENTS.md so they stop re-learning the codebase every session."
related_course:
  - Agent Skills and Subagents
  - Coding Agents
  - Evidently
  - Loop and Graph Engineering
  - MCP
  - Spec-Driven Development
---

An agent that starts every session knowing nothing about your project will fight it. Context engineering is the module's practice of writing the durable knowledge down: AGENTS.md at the repo root carries the project's structure, conventions, commands, and constraints; task-level context rides in the backlog items; the agent reads both before touching code.

The course treats the instruction file as living documentation — updated as the project evolves, kept short enough to stay in the agent's working set. The payoff compounds across modules: subagents, skills, and CI all assume the shared context file is accurate.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
    - [Context Engineering](/course-wiki/llmz-m03-context-engineering/)
    - [Next Steps](/course-wiki/llmz-m03-next-steps/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 1: AI-Native Developer Workflow](/course-wiki/aidt-module-01/)
    - [AI-Native Developer Workflow](/course-wiki/aidt-m01-ai-native-developer-workflow/)
  - [Module 2: Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-module-02/)
    - [Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-m02-build-and-ship-an-ai-assisted-full-stack-app/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 2: Workflow Orchestration](/course-wiki/dez-module-02/)
    - [2.5.2 - Context Engineering with ChatGPT](/course-wiki/dez-m02-2-5-2-context-engineering-with-chatgpt/)
## Related concepts

- [Coding Agents](/course-wiki/coding-agents/)
- [Spec-Driven Development](/course-wiki/spec-driven-development/)
- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [Loop and Graph Engineering](/course-wiki/loop-and-graph-engineering/)
