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

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 5: Coding Agent Capabilities

## Related concepts

- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [Coding Agents](/course-wiki/coding-agents/)
- [Context Engineering](/course-wiki/context-engineering/)
- [Git Worktrees](/course-wiki/git-worktrees/)
