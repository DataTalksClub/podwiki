---
title: "Avro Schema Management"
summary: "Declaring event schemas and evolving them compatibly so streaming consumers do not break."
related_course:
  - Kafka
  - Stream Processing
  - dbt
  - BigQuery
---

Events in a streaming pipeline are contracts: producers write records in a schema, consumers read them expecting one. The module teaches Avro as the schema format and a schema registry as its keeper — every message carries a schema id, the registry stores the schemas, and compatibility checks run when a producer tries to evolve one.

The practical rule the module lands on: schemas may evolve backward-compatibly (add optional fields, don't delete or rename required ones). With that discipline, consumers keep reading old and new events through the same code while the data model grows.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Module 7: Stream Processing (Schema management)

## Related concepts

- [Kafka](/course-wiki/kafka/)
- [Stream Processing](/course-wiki/stream-processing/)
- [dbt](/course-wiki/dbt/)
- [BigQuery](/course-wiki/bigquery/)
