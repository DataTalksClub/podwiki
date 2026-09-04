---
title: "Kestra"
summary: "The open-source, event-driven orchestrator Data Engineering and LLM Zoomcamps use to define pipelines as YAML."
related_course:
  - BigQuery
  - Docker
  - Prometheus and Grafana
  - Terraform
  - Workflow Orchestration
  - dlt
---

Kestra is the orchestration tool taught in both Data Engineering Zoomcamp and LLM Zoomcamp. Workflows are declared in YAML as tasks with dependencies: extraction tasks feed transformation tasks, everything runs on schedules or on event triggers, and retries, error handling, and logging are part of the definition rather than custom scripts.

Data Engineering Zoomcamp builds ETL and ELT pipelines against GCP with it; LLM Zoomcamp uses the same engine to orchestrate LLM application workflows. The transferable idea: a pipeline is configuration, reproducible and versionable, not a pile of cron scripts.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
    - [Context Engineering](/course-wiki/llmz-m03-context-engineering/)
    - [Setting up Kestra](/course-wiki/llmz-m03-setting-up-kestra/)
    - [AI Copilot](/course-wiki/llmz-m03-ai-copilot/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
    - [Multi-Agent Systems](/course-wiki/llmz-m03-multi-agent-systems/)
    - [Best Practices](/course-wiki/llmz-m03-best-practices/)
    - [Next Steps](/course-wiki/llmz-m03-next-steps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Using an Orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 2: Workflow Orchestration](/course-wiki/dez-module-02/)
    - [2.1.2 - What is Kestra?](/course-wiki/dez-m02-2-1-2-what-is-kestra/)
    - [2.2.1 - Installing Kestra](/course-wiki/dez-m02-2-2-1-installing-kestra/)
    - [2.2.2 - Kestra Concepts](/course-wiki/dez-m02-2-2-2-kestra-concepts/)
    - [2.4.3 - Create an ETL Pipeline with GCS and BigQuery in Kestra](/course-wiki/dez-m02-2-4-3-create-an-etl-pipeline-with-gcs-and-bigque/)
    - [2.5.3 - AI Copilot in Kestra](/course-wiki/dez-m02-2-5-3-ai-copilot-in-kestra/)
## Related concepts

- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [dlt](/course-wiki/dlt/)
- [Terraform](/course-wiki/terraform/)
- [BigQuery](/course-wiki/bigquery/)
- [Docker](/course-wiki/docker/)
