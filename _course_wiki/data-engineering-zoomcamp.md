---
title: "Data Engineering Zoomcamp"
summary: "DataTalks.Club's free nine-week data engineering course: build an end-to-end pipeline with Docker, Terraform, Kestra, BigQuery, dbt, Spark, and Kafka."
related_course:
  - Zoomcamps
  - MLOps Zoomcamp
---

Data Engineering Zoomcamp is DataTalks.Club's free nine-week course on data
engineering fundamentals. Learners build an end-to-end data pipeline from
scratch — ingestion, warehousing, transformation, batch, and streaming —
using industry-standard tools. No prior data engineering experience is
required; basic coding and SQL familiarity are.

All materials are open source in the
[course repository](https://github.com/DataTalksClub/data-engineering-zoomcamp),
with videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
and a [course FAQ](https://datatalks.club/faq/data-engineering-zoomcamp.html).
The live cohort starts each January; everything is also available self-paced.

## Curriculum

- **Module 1: Containerization and Infrastructure as Code** — GCP basics,
  [Docker](/course-wiki/docker/) and Docker Compose, PostgreSQL in Docker, and
  [Terraform](/course-wiki/terraform/) for infrastructure setup.
- **Module 2: Workflow Orchestration** — data lakes and
  [workflow orchestration](/course-wiki/workflow-orchestration/) with
  [Kestra](/course-wiki/kestra/): scheduled and event-driven pipelines defined
  as YAML.
- **Workshop: Data Ingestion** — scalable API reading, normalization, and
  incremental loading with [dlt](/course-wiki/dlt/).
- **Module 3: Data Warehousing** — [BigQuery](/course-wiki/bigquery/),
  [partitioning and clustering](/course-wiki/partitioning-and-clustering/),
  query best practices, and machine learning in BigQuery.
- **Module 4: Analytics Engineering** — data modeling with
  [dbt](/course-wiki/dbt/) on DuckDB and BigQuery, plus testing, documentation,
  and deployment ([analytics engineering](/course-wiki/analytics-engineering/)).
- **Module 5: Data Platforms** — end-to-end pipelines with
  [Bruin](/course-wiki/bruin/): ingestion, transformation, orchestration,
  quality, and metadata in one platform.
- **Module 6: Batch Processing** — [Apache Spark](/course-wiki/spark/),
  DataFrames and Spark SQL, and the internals of groupBy and joins.
- **Module 7: Stream Processing** — [Kafka](/course-wiki/kafka/) concepts and
  a PyFlink workshop building a real-time pipeline with Redpanda, Flink, and
  PostgreSQL ([stream processing](/course-wiki/stream-processing/)).
- **Final project** — a real-world pipeline with peer review.

## Who it is for

The course targets developers, analysts, and data scientists moving into data
engineering. The prerequisite bar is deliberately low — basic coding
experience and familiarity with SQL, with Python helpful but optional.

## Projects and certificate

Certificates require the final project plus peer reviews during a live
cohort. The final project — problem statement, cloud infrastructure, ingested
dataset, warehouse or lake, transformations, dashboard, and tests — is a
complete portfolio artifact.
