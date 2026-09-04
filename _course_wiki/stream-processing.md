---
title: "Stream Processing"
summary: "Processing events as they arrive instead of in collected batches, built with Kafka, PyFlink, and Postgres."
related_course:
  - Kafka
  - Spark
  - dlt
  - Model Monitoring
---

Stream processing is the complement to the batch module: instead of collecting data and processing it in chunks, events are processed continuously as they arrive. The module's workshop builds a real-time pipeline step by step — Redpanda as the Kafka-compatible event broker, PyFlink for the processing logic, PostgreSQL as the destination.

The concepts transfer directly to any streaming stack: events flow through a broker, a stream processor transforms or aggregates them in motion, and results land in a store that serves them. Batch answers 'what happened yesterday?'; streaming answers 'what is happening now?'.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 7: Stream Processing

## Related concepts

- [Kafka](/course-wiki/kafka/)
- [Spark](/course-wiki/spark/)
- [dlt](/course-wiki/dlt/)
- [Model Monitoring](/course-wiki/model-monitoring/)
