---
title: "OpenAPI Contract"
summary: "A machine-readable API specification that lets frontend, backend, and agents build against the same interface."
related_course:
  - FastAPI
  - Spec-Driven Development
  - Playwright
  - Coding Agents
  - CI/CD
---

Module 2 builds the full-stack app contract-first: before backend implementation, the API is written as an OpenAPI document — endpoints, request and response schemas, status codes. The contract is the single source of truth the FastAPI backend implements, the frontend codes against, and mock servers can satisfy during early development.

For agent-driven work the contract matters even more: an agent implementing the backend does not need to guess what the frontend expects, and an agent writing the frontend consumes the same document. The course's app connects a real-time collaborative frontend to its FastAPI backend through this contract, then swaps mock storage for SQLite with tests.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 2: Build and Ship an AI-Assisted Full-Stack App

## Related concepts

- [FastAPI](/course-wiki/fastapi/)
- [Spec-Driven Development](/course-wiki/spec-driven-development/)
- [Playwright](/course-wiki/playwright/)
- [Coding Agents](/course-wiki/coding-agents/)
- [CI/CD](/course-wiki/ci-cd/)
