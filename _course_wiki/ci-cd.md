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

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 6: Best Practices
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 3: Test, Containerize, and Deploy

## Related concepts

- [Docker](/course-wiki/docker/)
- [Terraform](/course-wiki/terraform/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Playwright](/course-wiki/playwright/)
- [OpenTelemetry](/course-wiki/opentelemetry/)
