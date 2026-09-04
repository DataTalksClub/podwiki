---
title: "Playwright"
summary: "Browser-level end-to-end testing that verifies the whole application, not just its parts."
related_course:
  - CI/CD
  - Coding Agents
  - Docker
  - OpenAPI Contract
  - OpenTelemetry
  - Technical Indicators
---

Module 3 adds the outermost testing ring: Playwright drives a real browser against the deployed app — loading the page, clicking through the collaborative workflow, asserting what the user should see. Unit and integration tests verify components in isolation; Playwright verifies the assembled system, frontend and backend together, in an environment that matches production.

The tests slot into the CI/CD pipeline as the deployment gate: the GitHub Actions workflow builds the containerized app, runs the test suite including the browser tests, and deploys to AWS only when everything passes. It is the course's guardrail for AI-generated changes — if the user-visible flow breaks, the pipeline blocks the release.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 3: Test, Containerize, and Deploy

## Related concepts

- [CI/CD](/course-wiki/ci-cd/)
- [OpenAPI Contract](/course-wiki/openapi-contract/)
- [Docker](/course-wiki/docker/)
- [Coding Agents](/course-wiki/coding-agents/)
- [OpenTelemetry](/course-wiki/opentelemetry/)
