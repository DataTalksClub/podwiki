---
title: "Analytics Engineering"
summary: "The practice layer between data engineering and analysis: production-grade data transformations."
related_course:
  - Agent Skills and Subagents
  - BigQuery
  - Bruin
  - Function Calling
  - Partitioning and Clustering
  - dbt
---

Analytics engineering applies software engineering practice to data transformation: version control, modularity, testing, documentation, and deployment pipelines. Where a data engineer builds the pipelines that load the warehouse, the analytics engineer shapes the data inside it into clean, tested, well-named models that analysts and BI tools can trust.

In the course, the dbt module is where this discipline is taught concretely: a layered project (staging, intermediate, marts) over the taxi dataset, with every model defined in SQL, wired into a DAG by refs, and gated by tests before it reaches a dashboard.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 4: Analytics Engineering

## Related concepts

- [dbt](/course-wiki/dbt/)
- [BigQuery](/course-wiki/bigquery/)
- [Bruin](/course-wiki/bruin/)
- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
