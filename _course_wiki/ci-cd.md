---
title: "CI/CD"
summary: "Automated pipelines that test, build, and deploy ML code — GitHub Actions from MLOps and AI Dev Tools Zoomcamps."
related_course:
  - Docker
  - Git Worktrees
  - MLOps Maturity Model
  - Model Deployment
  - OpenAPI Contract
  - OpenTelemetry
  - Playwright
  - Prometheus and Grafana
  - Terraform
---

CI/CD closes the best-practices module: every push to GitHub triggers a GitHub Actions workflow that lints and formats the code, runs unit tests, builds the Docker image, and — for releases — deploys it. The pipeline is defined as code in the repository, so the process is reviewable and reproducible.

AI Dev Tools Zoomcamp extends the same practice to full-stack apps: a workflow that runs backend and frontend tests (including Playwright end-to-end tests) and deploys to AWS only when everything passes. In both courses the principle is identical — no manual deployment steps between a tested commit and production.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 2: Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-module-02/)
    - [Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-m02-build-and-ship-an-ai-assisted-full-stack-app/)
  - [Module 3: Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-module-03/)
    - [Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-m03-test-containerize-and-deploy-an-ai-assisted-app/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 6: Best Practices](/course-wiki/mlops-module-06/)
    - [Homework](/course-wiki/mlops-m06-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [Docker](/course-wiki/docker/)
- [Terraform](/course-wiki/terraform/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Playwright](/course-wiki/playwright/)
- [OpenTelemetry](/course-wiki/opentelemetry/)
