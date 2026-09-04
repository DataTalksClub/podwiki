---
title: "Kestra"
summary: "The open-source, event-driven orchestrator Data Engineering and LLM Zoomcamps use to define pipelines as YAML."
related_course:
  - Workflow Orchestration
  - dlt
  - Terraform
  - BigQuery
  - Docker
---

Kestra is the orchestration tool taught in both Data Engineering Zoomcamp and LLM Zoomcamp. Workflows are declared in YAML as tasks with dependencies: extraction tasks feed transformation tasks, everything runs on schedules or on event triggers, and retries, error handling, and logging are part of the definition rather than custom scripts.

Data Engineering Zoomcamp builds ETL and ELT pipelines against GCP with it; LLM Zoomcamp uses the same engine to orchestrate LLM application workflows. The transferable idea: a pipeline is configuration, reproducible and versionable, not a pile of cron scripts.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 2: Workflow Orchestration
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 3: AI Orchestration

## Related concepts

- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [dlt](/course-wiki/dlt/)
- [Terraform](/course-wiki/terraform/)
- [BigQuery](/course-wiki/bigquery/)
- [Docker](/course-wiki/docker/)
