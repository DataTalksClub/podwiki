---
title: "dbt"
summary: "SQL-first analytics engineering: transformations as versioned, tested, documented models with a dependency graph."
related_course:
  - Analytics Engineering
  - Avro Schema Management
  - BigQuery
  - Bruin
  - Partitioning and Clustering
  - Workflow Orchestration
---

Module 4 is the analytics engineering module, and dbt is its tool: transformations from raw warehouse data to analytical models are SELECT statements in files, organized into a project with a dependency graph (refs between models), tests (uniqueness, not-null, accepted values), and generated documentation.

The module builds a dbt project over the NYC taxi data on two stacks — locally with DuckDB and dbt Core, or in the cloud with BigQuery and dbt Cloud — so learners see that the project structure is portable across warehouses. The outcome discipline: transformations that are version-controlled, tested, and documented instead of buried in a notebook.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 4: Analytics Engineering

## Related concepts

- [BigQuery](/course-wiki/bigquery/)
- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
- [Analytics Engineering](/course-wiki/analytics-engineering/)
- [Bruin](/course-wiki/bruin/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
