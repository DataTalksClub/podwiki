---
title: "Git Worktrees"
summary: "Isolated working copies of one repository, letting multiple agents work in parallel without stepping on each other."
related_course:
  - Agent Skills and Subagents
  - CI/CD
  - Coding Agents
  - Loop and Graph Engineering
  - MCP
  - Transfer Learning
---

One repository, several agents, one checkout — that is a merge-conflict factory. Git worktrees give each agent its own directory with its own branch from the same repo, so tasks run in parallel in isolation: agent A's half-finished refactor never appears in agent B's working tree.

Module 5 pairs worktrees with the orchestration pattern: a coordinator assigns backlog tasks, each worker agent runs in its own worktree, and finished work comes back as branches to review and merge. The same discipline humans use for parallel development becomes the mechanism for safe parallel agents.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
## Related concepts

- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [MCP](/course-wiki/mcp/)
- [Coding Agents](/course-wiki/coding-agents/)
- [CI/CD](/course-wiki/ci-cd/)
