---
title: "dlt"
summary: "The library-first data ingestion tool taught in the Data Engineering and LLM Zoomcamp ingestion workshops."
related_course:
  - BigQuery
  - Bruin
  - Kafka
  - Kestra
  - LLM Monitoring
  - Stream Processing
  - Workflow Orchestration
---

dlt (data load tool) is a Python library for building ingestion pipelines: declare a source (REST API, filesystem, database), and dlt handles API pagination, normalization of nested JSON into tables, incremental loading with tracked cursors, and schema inference as it loads into a destination such as DuckDB or BigQuery.

Data Engineering Zoomcamp's workshop scales API reading and teaches incremental loading with it. LLM Zoomcamp's workshop uses the same library to ingest LLM application traces — filesystem and REST API sources into DuckDB — and then analyzes them in marimo notebooks. One library, the same declarative pipeline shape, two problem domains.

## Taught in

- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — Workshop: Data Ingestion
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — Workshop: Data Ingestion

## Related concepts

- [Kestra](/course-wiki/kestra/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [BigQuery](/course-wiki/bigquery/)
- [Stream Processing](/course-wiki/stream-processing/)
- [LLM Monitoring](/course-wiki/llm-monitoring/)
