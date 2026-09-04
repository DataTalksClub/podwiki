---
layout: wiki
title: "AI Dev Tools Zoomcamp"
summary: "DataTalks.Club's free course on AI-native software engineering: coding agents, AGENTS.md context, full-stack builds, CI/CD, observability, MCP, and reusable agent skills."
related:
  - Zoomcamps
  - AI Coding Tools
  - AI Engineering
  - Agent Engineering
  - AI Engineering Roadmap
  - AI Engineering Portfolio Projects
  - Software Engineering
  - CI/CD
  - LLM Zoomcamp
---

AI Dev Tools Zoomcamp is DataTalks.Club's free, hands-on course on disciplined
AI-assisted software development. It is built around one workflow: give AI
tools the right context, use them for the right job, review what they
produce, test the result, and ship software with guardrails. The course
compares modern AI developer tools, builds and deploys a full-stack
application, operates it with observability and agent-assisted incident
response, and extends coding agents with MCP and reusable capabilities.

This is deliberately not a prompt-engineering course and not a model-training
or RAG course — the focus is day-to-day software development with AI coding
assistants, agents, tests, CI/CD, deployment, documentation, and review. For
the application layer, [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) covers building the LLM product
itself. All materials are open source in the
[course repository](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp),
with videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43)
and a [course FAQ](https://datatalks.club/faq/ai-dev-tools-zoomcamp.html). It
is part of the [Zoomcamps](/course-wiki/zoomcamps/) family.

## Curriculum

The [repository syllabus](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
maps the modules:

- **AI-native developer workflow** — turn a vague idea into a spec and a
  task backlog, give coding agents durable context through `AGENTS.md`, and
  run PM/engineer/QA roles with loop and graph engineering.
- **Build and ship an AI-assisted full-stack app** — frontend prototype, an
  OpenAPI contract, a FastAPI backend with auth and real-time collaboration,
  SQLite persistence, and tests.
- **Test, containerize, and deploy** — Docker Compose with Postgres,
  integration and end-to-end tests including Playwright, AWS deployment, and
  a GitHub Actions pipeline that deploys only after tests pass ([CI/CD](/wiki/ci-cd/)).
- **DevOps and observability for AI-built apps** — separate dev and prod
  environments with a promoted release pipeline, OpenTelemetry into
  Prometheus, Loki, Tempo, and Grafana, actionable alerts, and a bounded,
  read-only coding-agent responder that investigates incidents
  ([Production](/wiki/production/), [Agent Ops](/wiki/agent-ops/)).
- **Agent building blocks** — discoverable skills with `SKILL.md`, focused
  subagents that separate implementation from independent review, and
  parallel task orchestration with isolated Git worktrees
  ([Agent Engineering](/wiki/agent-engineering/), [Multi-Agent Systems](/wiki/multi-agent-systems/)).

The final project applies the workflow end to end: an app of the learner's
own with frontend, backend, an API contract, persistence, tests,
containerization, a public deployment, and documentation of exactly how AI
tools, prompts, and agent instructions were used.

## Who it is for

The course targets people who already write basic code — software engineers,
ML and MLOps engineers, data scientists, data engineers, and analysts who
code — and want to use AI coding tools professionally with a repeatable
workflow for planning, prompting, reviewing, testing, and shipping. No prior
AI tool experience, powerful machine, or GPU is required.

## What the podcast adds

AI-assisted development shows up in the podcast as the skill that let
learners ship faster without losing engineering discipline. An engineer
returning after a seven-year career break describes building prototypes with
AI dev tools — "vibe coding" with review — as part of rebuilding evidence and
interview readiness.
[How to Become an AI Engineer After a Career Break](https://datatalks.club/podcast/s23e04-how-to-become-ai-engineer-after-career-break.html)
Learners report moving from building models to designing AI-assisted systems
that ship faster and iterate more cleanly, with MCP servers and agent tools
as first-class parts of the workflow.

[AI Coding Tools](/wiki/ai-coding-tools/) covers the tool landscape — Cursor, Copilot, Claude Code,
and notebook-to-agent workflows — that the course teaches as a single
reviewed pipeline, and the [AI Engineering Roadmap](/wiki/ai-engineering-roadmap/) places AI-assisted
shipping inside the broader AI engineering skill stack. For portfolio use,
[AI Engineering Portfolios](/wiki/ai-engineering-portfolio-projects/) treats documented AI-assisted builds as
evidence of judgment, not just output.

## Related Pages

- [Zoomcamps](/course-wiki/zoomcamps/)
- [AI Coding Tools](/wiki/ai-coding-tools/)
- [AI Engineering](/wiki/ai-engineering/)
- [Agent Engineering](/wiki/agent-engineering/)
- [AI Engineering Roadmap](/wiki/ai-engineering-roadmap/)
- [AI Engineering Portfolios](/wiki/ai-engineering-portfolio-projects/)
- [CI/CD](/wiki/ci-cd/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
