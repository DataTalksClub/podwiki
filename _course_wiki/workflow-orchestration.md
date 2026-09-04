---
title: "Workflow Orchestration"
summary: "Coordinating multi-step data and ML workflows: schedules, dependencies, retries, and observability."
related_course:
  - Kestra
  - Model Deployment
  - dlt
  - MLflow
  - BigQuery
---

Workflow orchestration is the conductor role for pipelines: multiple tools and steps need to run in order, on a schedule or in reaction to events, with errors monitored and handled. Data Engineering Zoomcamp introduces the concept with Kestra; MLOps Zoomcamp applies it to ML — turning a training notebook into a Python script, then wrapping the script in an orchestrator such as Prefect, Airflow, Dagster, Kestra, or Mage to make it a production pipeline.

The shared lesson across the three courses: anything that must run repeatedly and reliably belongs to an orchestrator, which handles scheduling, dependency ordering, retries, and run history so the pipeline code does not have to.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 2: Workflow Orchestration
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 3: Orchestration and ML Pipelines
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Module 3: AI Orchestration

## Related concepts

- [Kestra](/course-wiki/kestra/)
- [Model Deployment](/course-wiki/model-deployment/)
- [dlt](/course-wiki/dlt/)
- [MLflow](/course-wiki/mlflow/)
- [BigQuery](/course-wiki/bigquery/)
