---
title: "Terraform"
summary: "Infrastructure as code for cloud environments: declarative resource definitions that can be planned, applied, and reproduced."
related_course:
  - BigQuery
  - CI/CD
  - Docker
  - Kestra
  - LLM Monitoring
  - Workflow Orchestration
---

Module 1 pairs Docker with Terraform: after containerizing the runtime components, the cloud infrastructure itself — GCP storage buckets and BigQuery datasets for the course's pipeline — is declared in Terraform configuration files instead of clicked into existence in a console.

The workflow is plan, apply, destroy. Plan shows what changes Terraform will make; apply creates the resources; destroy tears the environment down. For data engineers the payoff is reproducible environments: the same configuration recreates the same infrastructure for the next project or cohort.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 1: Introduction](/course-wiki/mlops-module-01/)
    - [Homework](/course-wiki/mlops-m01-homework/)
  - [Module 6: Best Practices](/course-wiki/mlops-module-06/)
    - [Homework](/course-wiki/mlops-m06-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 1: Containerization and Infrastructure as Code](/course-wiki/dez-module-01/)
    - [Introduction to GCP (Google Cloud Platform)](/course-wiki/dez-m01-introduction-to-gcp-google-cloud-platform/)
    - [Introduction Terraform: Concepts and Overview, a primer](/course-wiki/dez-m01-introduction-terraform-concepts-and-overview-a-p/)
    - [Terraform Basics: Simple one file Terraform Deployment](/course-wiki/dez-m01-terraform-basics-simple-one-file-terraform-deplo/)
## Related concepts

- [Docker](/course-wiki/docker/)
- [BigQuery](/course-wiki/bigquery/)
- [Kestra](/course-wiki/kestra/)
- [CI/CD](/course-wiki/ci-cd/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
