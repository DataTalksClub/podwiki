---
title: "Partitioning and Clustering"
summary: "BigQuery's two mechanisms for pruning scanned data: splitting tables by a column and sorting data within splits."
related_course:
  - BigQuery
  - dbt
  - Spark
  - Analytics Engineering
---

Partitioning splits a table into pieces along a column — typically a date, so a query filtering on one day scans only that day's partition instead of the full table. Clustering sorts the rows inside each partition by additional columns, so filters on those columns skip blocks of data as well.

The module frames both as cost and performance tools: on a serverless warehouse that bills by bytes scanned, a well-partitioned taxi dataset turns a full-table query into a targeted one. The best-practices lesson follows directly — always query with the partition filter.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 3: Data Warehousing

## Related concepts

- [BigQuery](/course-wiki/bigquery/)
- [dbt](/course-wiki/dbt/)
- [Spark](/course-wiki/spark/)
- [Analytics Engineering](/course-wiki/analytics-engineering/)
