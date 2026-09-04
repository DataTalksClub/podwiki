---
title: "Kafka"
summary: "The distributed event log behind streaming pipelines: topics, producers, consumers, and schemas."
related_course:
  - Avro Schema Management
  - OpenTelemetry
  - Spark
  - Stream Processing
  - Workflow Orchestration
  - dlt
---

Kafka is a distributed log built for streaming: producers append events to topics, consumers read them at their own pace, and the broker keeps the events durable and ordered per partition. The module's theory track teaches the concepts — topics, partitions, consumer groups, delivery semantics — with Java code examples.

Schema management with Avro rounds out the theory: producers declare message schemas, and the schema registry validates compatibility as data evolves, so consumers do not break when a field changes. The workshop track then builds a real-time pipeline with PyFlink and Redpanda (a Kafka-compatible broker) writing into PostgreSQL.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 7: Stream Processing (Kafka theory)

## Related concepts

- [Stream Processing](/course-wiki/stream-processing/)
- [Spark](/course-wiki/spark/)
- [dlt](/course-wiki/dlt/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
