---
schema_type: Course
title: "AI Dev Tools Zoomcamp"
summary: "DataTalks.Club's free course on AI-native software engineering: coding agents, context engineering, full-stack builds, CI/CD, observability, MCP, and reusable agent skills."
related_course:
  - Zoomcamps
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
assistants, agents, tests, CI/CD, deployment, documentation, and review. All
materials are open source in the
[course repository](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp),
with videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43)
and a [course FAQ](https://datatalks.club/faq/ai-dev-tools-zoomcamp.html). The
2026 cohort starts August 31; materials are also usable self-paced.

## Curriculum

All modules, each with its lesson-level notes:

- [Module 1: AI-Native Developer Workflow](/course-wiki/aidt-module-01/)
- [Module 2: Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-module-02/)
- [Module 3: Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-module-03/)
- [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
- [Module 5: Coding Agent Capabilities](/course-wiki/aidt-module-05/)

- [**Module 1: AI-Native Developer Workflow**](/course-wiki/aidt-module-01/) — turn a vague idea into a spec
  and a task backlog ([spec-driven development](/course-wiki/spec-driven-development/)),
  give coding agents durable context through AGENTS.md
  ([context engineering](/course-wiki/context-engineering/)), and run
  PM/engineer/QA roles with [loop and graph engineering](/course-wiki/loop-and-graph-engineering/)
  ([coding agents](/course-wiki/coding-agents/)).
- [**Module 2: Build and Ship an AI-Assisted Full-Stack App**](/course-wiki/aidt-module-02/) — frontend
  prototype, an [OpenAPI contract](/course-wiki/openapi-contract/), a
  [FastAPI](/course-wiki/fastapi/) backend with auth and real-time
  collaboration, SQLite persistence, and tests.
- **Module 3: Test, Containerize, and Deploy** —
  [Docker](/course-wiki/docker/) Compose with Postgres, integration and
  end-to-end tests including [Playwright](/course-wiki/playwright/), AWS
  deployment, and a [CI/CD](/course-wiki/ci-cd/) pipeline that deploys only
  after tests pass.
- [**Module 4: DevOps and Observability for AI-Built Apps**](/course-wiki/aidt-module-04/) — separate dev and
  prod environments with a promoted release pipeline,
  [OpenTelemetry](/course-wiki/opentelemetry/) into Prometheus, Loki, Tempo,
  and Grafana, actionable alerts, and a bounded, read-only coding-agent
  responder that investigates incidents.
- [**Module 5: Coding Agent Capabilities**](/course-wiki/aidt-module-05/) —
  [MCP](/course-wiki/mcp/) servers, discoverable
  [agent skills](/course-wiki/agent-skills-and-subagents/) with SKILL.md,
  focused subagents that separate implementation from independent review, and
  parallel task orchestration with isolated
  [Git worktrees](/course-wiki/git-worktrees/).

The final project applies the workflow end to end: an app of the learner's
own with frontend, backend, an API contract, persistence, tests,
containerization, a public deployment, and documentation of exactly how AI
tools, prompts, and agent instructions were used.

## Who it is for

The course targets people who already write basic code — software engineers,
ML and MLOps engineers, data scientists, data engineers, and analysts who
code — and want to use AI coding tools professionally with a repeatable
workflow for planning, prompting, reviewing, testing, and shipping. No prior
AI tool experience, powerful machine, or GPU is required. Certificates
require the final project plus the required peer reviews during a live
cohort.
