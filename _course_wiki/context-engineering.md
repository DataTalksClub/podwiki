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

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 1: AI-Native Developer Workflow

## Related concepts

- [Coding Agents](/course-wiki/coding-agents/)
- [Spec-Driven Development](/course-wiki/spec-driven-development/)
- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [Loop and Graph Engineering](/course-wiki/loop-and-graph-engineering/)
