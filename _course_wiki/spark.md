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

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 6: Batch Processing](/course-wiki/dez-module-06/)
    - [6.1.2 Introduction to Spark](/course-wiki/dez-m06-6-1-2-introduction-to-spark/)
    - [6.3.1 First Look at Spark/PySpark](/course-wiki/dez-m06-6-3-1-first-look-at-spark-pyspark/)
    - [6.3.2 Spark Dataframes](/course-wiki/dez-m06-6-3-2-spark-dataframes/)
    - [6.3.4 SQL with Spark](/course-wiki/dez-m06-6-3-4-sql-with-spark/)
    - [6.4.1 Anatomy of a Spark Cluster](/course-wiki/dez-m06-6-4-1-anatomy-of-a-spark-cluster/)
    - [6.4.2 GroupBy in Spark](/course-wiki/dez-m06-6-4-2-groupby-in-spark/)
    - [6.4.3 Joins in Spark](/course-wiki/dez-m06-6-4-3-joins-in-spark/)
    - [6.5.1 Operations on Spark RDDs](/course-wiki/dez-m06-6-5-1-operations-on-spark-rdds/)
    - [6.5.2 Spark RDD mapPartition](/course-wiki/dez-m06-6-5-2-spark-rdd-mappartition/)
    - [6.6.2 Creating a Local Spark Cluster](/course-wiki/dez-m06-6-6-2-creating-a-local-spark-cluster/)
    - [6.6.4 Connecting Spark to Big Query](/course-wiki/dez-m06-6-6-4-connecting-spark-to-big-query/)
## Related concepts

- [Kafka](/course-wiki/kafka/)
- [Stream Processing](/course-wiki/stream-processing/)
- [BigQuery](/course-wiki/bigquery/)
- [Partitioning and Clustering](/course-wiki/partitioning-and-clustering/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
