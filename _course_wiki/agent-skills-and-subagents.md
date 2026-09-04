---
title: "Agent Skills and Subagents"
summary: "Packaging repeated workflows as discoverable skills, and defining focused subagents that separate doing from reviewing."
related_course:
  - Analytics Engineering
  - Coding Agents
  - Context Engineering
  - Git Worktrees
  - Loop and Graph Engineering
  - MCP
---

Skills are reusable workflow packages: a SKILL.md file with instructions (and optional scripts) that an agent discovers and applies when a task matches — project-specific skills live in the repo, global ones in the agent's home directory. The course shows turning a repeated workflow (release checks, docs generation) into a skill so the process runs the same way every time.

Subagents are the role specialization: a QA subagent with its own prompt and context reviews what the implementing agent wrote; a PM subagent drafts specs. Because subagents start with fresh context and a focused charter, they verify independently instead of rubber-stamping — the module-level pattern from loop and graph engineering, made reusable.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 5: Coding Agent Capabilities

## Related concepts

- [MCP](/course-wiki/mcp/)
- [Loop and Graph Engineering](/course-wiki/loop-and-graph-engineering/)
- [Context Engineering](/course-wiki/context-engineering/)
- [Git Worktrees](/course-wiki/git-worktrees/)
- [Coding Agents](/course-wiki/coding-agents/)
