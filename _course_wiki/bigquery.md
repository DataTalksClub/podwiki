---
title: "BigQuery"
summary: "Google Cloud's serverless data warehouse: SQL at scale with partitioning, clustering, and in-warehouse ML."
related_course:
  - Analytics Engineering
  - Avro Schema Management
  - Bruin
  - Docker
  - Kestra
  - Partitioning and Clustering
  - Spark
  - Terraform
  - Workflow Orchestration
  - dbt
  - dlt
---

Module 3 makes BigQuery the course warehouse. Data loaded from the pipeline lands in BigQuery tables, and all downstream analytics runs as SQL against them. Because it is serverless, there is no cluster to size — queries scale automatically and costs track data scanned, which is exactly why the module teaches controlling that scan volume.

Beyond basic SQL, the module covers best practices (select only needed columns, partition to prune scans), the internals of how queries execute, and BigQuery ML — training a model with a CREATE MODEL SQL statement on data that already lives in the warehouse.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Context Engineering](/course-wiki/llmz-m03-context-engineering/)
    - [AI Copilot](/course-wiki/llmz-m03-ai-copilot/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 2: Workflow Orchestration](/course-wiki/dez-module-02/)
    - [2.4.3 - Create an ETL Pipeline with GCS and BigQuery in Kestra](/course-wiki/dez-m02-2-4-3-create-an-etl-pipeline-with-gcs-and-bigque/)
  - [Module 3: Data Warehousing](/course-wiki/dez-module-03/)
    - [Internals of BigQuery](/course-wiki/dez-m03-internals-of-bigquery/)
    - [Machine Learning in Big Query](/course-wiki/dez-m03-machine-learning-in-big-query/)
    - [Deploying Machine Learning model from BigQuery](/course-wiki/dez-m03-deploying-machine-learning-model-from-bigquery/)
  - [Module 4: Analytics Engineering](/course-wiki/dez-module-04/)
    - [Analytics Engineering](/course-wiki/dez-m04-analytics-engineering/)
## Related concepts

- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
- [dbt](/course-wiki/dbt/)
- [Terraform](/course-wiki/terraform/)
- [Kestra](/course-wiki/kestra/)
- [Docker](/course-wiki/docker/)
