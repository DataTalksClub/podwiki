---
title: "Terraform"
summary: "Infrastructure as code for cloud environments: declarative resource definitions that can be planned, applied, and reproduced."
related_course:
  - Docker
  - BigQuery
  - Kestra
  - CI/CD
  - Workflow Orchestration
---

Module 1 pairs Docker with Terraform: after containerizing the runtime components, the cloud infrastructure itself — GCP storage buckets and BigQuery datasets for the course's pipeline — is declared in Terraform configuration files instead of clicked into existence in a console.

The workflow is plan, apply, destroy. Plan shows what changes Terraform will make; apply creates the resources; destroy tears the environment down. For data engineers the payoff is reproducible environments: the same configuration recreates the same infrastructure for the next project or cohort.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 1: Containerization and Infrastructure as Code

## Related concepts

- [Docker](/course-wiki/docker/)
- [BigQuery](/course-wiki/bigquery/)
- [Kestra](/course-wiki/kestra/)
- [CI/CD](/course-wiki/ci-cd/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
