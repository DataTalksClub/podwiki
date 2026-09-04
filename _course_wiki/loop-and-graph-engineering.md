---
title: "Loop and Graph Engineering"
summary: "Structuring agent work as verification loops, and as graphs of specialized roles that check each other."
related_course:
  - Agent Skills and Subagents
  - Coding Agents
  - Context Engineering
  - Git Worktrees
  - Kubernetes
  - Spec-Driven Development
---

Loop engineering closes the implementation circle: the agent writes code, runs the tests, reads the failures, and iterates until green — the loop, not the first draft, is where agent quality comes from. Graph engineering goes further: instead of one agent doing everything, the work flows through a graph of roles — a product-manager agent writes the spec, engineer agents implement tasks, and a QA agent independently verifies the result against the spec.

The course's rule underneath both patterns: implementation and verification must not be the same context. The QA agent gets the spec and the code, not the implementer's reasoning, so its review stays independent.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 1: AI-Native Developer Workflow](/course-wiki/aidt-module-01/)
    - [AI-Native Developer Workflow](/course-wiki/aidt-m01-ai-native-developer-workflow/)
## Related concepts

- [Coding Agents](/course-wiki/coding-agents/)
- [Spec-Driven Development](/course-wiki/spec-driven-development/)
- [Context Engineering](/course-wiki/context-engineering/)
- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
