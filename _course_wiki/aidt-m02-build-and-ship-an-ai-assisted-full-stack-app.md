---
title: "Build and Ship an AI-Assisted Full-Stack App — AI Dev Tools Zoomcamp Module 2"
summary: "# Build and Ship an AI-Assisted Full-Stack App"
related_course:
  - aidt-module-02
---

[AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) › [Module 2: Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-module-02/) › Build and Ship an AI-Assisted Full-Stack App

## Notes

# Build and Ship an AI-Assisted Full-Stack App

## Overview

In this module, you build a working end-to-end application with AI assistance. The default project remains a small Snake Arena app because it is visual, interactive, and still requires the main parts of a real system:

- product spec
- frontend
- OpenAPI contract
- backend
- database
- tests

The goal is not to let an AI tool build everything unchecked. The goal is to practice a controlled workflow where AI helps you move faster and you verify each step.

The module ends with an app that runs on your machine: a frontend and a backend that talk to each other over a defined contract, with data persisted in SQLite. Everything needed to put it in front of other people — integration tests, containers, CI, deployment, and CI/CD — is [Module 3](../03-deployment/lesson.md).

You will:

- Write a small product spec with user stories, acceptance criteria, and non-goals before generating any code
- Draft a frontend prototype with an AI tool (Lovable, Bolt, Cursor, Claude Code, Codex, ...), then pull it into a normal repo workflow and make it maintainable
- Define an OpenAPI contract as the source of truth between frontend and backend
- Implement a FastAPI backend against the contract, starting with a mock database and tests for the key endpoints
- Swap the mock store for SQLite, keeping the app database-agnostic so Postgres can replace it later without a rewrite
- Add unit and frontend tests that cover the behavior described in the spec and the contract

Reference app:

- https://github.com/alexeygrigorev/interview-canvas-share

[Recording: Build and Ship an AI-Assisted Full-Stack App](https://www.youtube.com/watch?v=x9dq5nBpDg8)

Module summary: The companion article builds a collaborative system-design interview app from
scratch. It moves from a frontend prototype with mocked calls to an OpenAPI
contract, a FastAPI backend, WebSocket collaboration, and SQLite persistence,
while testing each stage before moving on.

[Read the article: Build and Ship a Full-Stack App with AI Coding Assistants](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with)

## Module Deliverables

At the end of Module 2, your repo should include:

```text
product-spec.md
AGENTS.md or equivalent
frontend/
backend/
openapi.yaml
tests/
docs/ai-usage-report.md
```

The app should run locally from the README, persist data in SQLite, and pass its own tests.

## Homework

- [Homework](homework.md)

## Previous Cohort Materials

The previous version of this module is archived here:

- [2025 archived Module 2](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/cohorts/2025/02-end-to-end)

## Community Notes

Did you take notes? You can share them here.

- Add a link to your notes above this line

## Key concepts

- [Context Engineering](/course-wiki/context-engineering/)
- [OpenAPI Contract](/course-wiki/openapi-contract/)
- [CI/CD](/course-wiki/ci-cd/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [aidt-m01-ai-native-developer-workflow](/course-wiki/aidt-m01-ai-native-developer-workflow/)
- [aidt-m03-test-containerize-and-deploy-an-ai-assisted-app](/course-wiki/aidt-m03-test-containerize-and-deploy-an-ai-assisted-app/)
- [aidt-m04-devops-and-observability-for-ai-built-apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
- [aidt-m05-configuration](/course-wiki/aidt-m05-configuration/)
- [aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)

## Sources

- [Video](https://www.youtube.com/watch?v=x9dq5nBpDg8)
- [Lesson file](https://github.com/ai-dev-tools-zoomcamp/blob/main/ai-dev-tools-zoomcamp/cohorts/2026/02-development/lesson.md)
