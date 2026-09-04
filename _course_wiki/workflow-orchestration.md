---
title: "Workflow Orchestration"
summary: "Coordinating multi-step data and ML workflows: schedules, dependencies, retries, and observability."
related_course:
  - BigQuery
  - Bruin
  - Deployment Automation
  - Experiment Tracking
  - Kafka
  - Kestra
  - MLOps Maturity Model
  - MLflow
  - Model Deployment
  - Spark
  - Terraform
  - dbt
  - dlt
---

Workflow orchestration is the conductor role for pipelines: multiple tools and steps need to run in order, on a schedule or in reaction to events, with errors monitored and handled. Data Engineering Zoomcamp introduces the concept with Kestra; MLOps Zoomcamp applies it to ML — turning a training notebook into a Python script, then wrapping the script in an orchestrator such as Prefect, Airflow, Dagster, Kestra, or Mage to make it a production pipeline.

The shared lesson across the three courses: anything that must run repeatedly and reliably belongs to an orchestrator, which handles scheduling, dependency ordering, retries, and run history so the pipeline code does not have to.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Other Frameworks](/course-wiki/llmz-m01-other-frameworks/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 5: Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](/course-wiki/aidt-module-05/)
    - [Module 5 — Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](/course-wiki/aidt-m05-module-5-coding-agent-capabilities-mcp-skills-pl/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Using an Orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
    - [Homework](/course-wiki/mlops-m03-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 2: Workflow Orchestration](/course-wiki/dez-module-02/)
    - [2.1.1 - What is Workflow Orchestration?](/course-wiki/dez-m02-2-1-1-what-is-workflow-orchestration/)
  - [Module 5: Data Platforms](/course-wiki/dez-module-05/)
    - [Introduction to Bruin](/course-wiki/dez-m05-introduction-to-bruin/)
## Related concepts

- [Kestra](/course-wiki/kestra/)
- [Model Deployment](/course-wiki/model-deployment/)
- [dlt](/course-wiki/dlt/)
- [MLflow](/course-wiki/mlflow/)
- [BigQuery](/course-wiki/bigquery/)
