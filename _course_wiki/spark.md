---
title: "Spark"
summary: "Distributed batch processing: DataFrames, Spark SQL, and the internals of groupBy and joins."
related_course:
  - BigQuery
  - Decision Trees
  - Kafka
  - Partitioning and Clustering
  - Stream Processing
  - Workflow Orchestration
---

Module 6 moves from single-machine analytics to distributed batch processing with Apache Spark. Spark splits large datasets and the computation over them across a cluster; the module works with the DataFrame API and Spark SQL, which look like pandas and SQL but execute across many machines.

The distinctive part of the module is internals: how groupBy works (shuffling rows to group keys across the cluster) and how joins distribute and shuffle data — the knowledge that separates pipelines that run from pipelines that OOM or crawl. Batch itself is the processing model: data is collected first and processed in chunks, in contrast to the streaming module that follows.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 6: Batch Processing

## Related concepts

- [Kafka](/course-wiki/kafka/)
- [Stream Processing](/course-wiki/stream-processing/)
- [BigQuery](/course-wiki/bigquery/)
- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
