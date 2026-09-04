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

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 3: Data Warehousing

## Related concepts

- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
- [dbt](/course-wiki/dbt/)
- [Terraform](/course-wiki/terraform/)
- [Kestra](/course-wiki/kestra/)
- [Docker](/course-wiki/docker/)
