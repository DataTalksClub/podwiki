---
layout: wiki
title: "Apache Iceberg"
summary: "How podcast guests place Apache Iceberg in lakehouse design, open table formats, catalogs, governance, and platform operations."
related:
  - Data Engineering Platforms
  - Data Lake
  - Delta Lake
  - Delta Lake vs Apache Iceberg
  - Data Warehouse vs Data Lakehouse
  - Modern Data Stack
  - DataOps
  - DuckDB
  - Data Governance
---

Apache Iceberg is an open table format for lakehouse-style storage. In the
podcast discussions, Iceberg sits above Parquet files and below query engines.
That puts table metadata between raw lake storage and the systems that read or
write the data.
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]]
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]]

Iceberg belongs in [[data-engineering-platforms=>data engineering platform]]
design because catalogs, access rules, metadata, and lineage sit around the
table format. Use [[Data Lake]] for the storage model and
[[Data Warehouse vs Data Lakehouse]] for the architecture tradeoff. When the
question is whether Iceberg or [[Delta Lake]] fits a platform requirement
better, use [[Delta Lake vs Apache Iceberg]].

## Table Format Role

Iceberg gives lake storage table behavior by pairing Parquet files with table
metadata. More than one engine can read and write through the shared table
layer.
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]]

Catalogs belong next to the table format. Access, metadata, and lineage sit
outside raw storage and compute, so an Iceberg platform still needs a catalog
path and a governance model.
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]]
Those responsibilities connect Iceberg to [[Data Governance]] and
[[Data Quality and Observability]].

Iceberg fits the [[data-warehouse-vs-data-lakehouse=>lakehouse]] idea when a
team wants warehouse-like table behavior on data-lake storage. A lakehouse puts
warehouse features on a data lake, but the surrounding platform still matters.
It still includes object storage and compute. It also includes ingress, egress,
self-service SQL, and workflow engines.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]]

## Platform Boundaries

Iceberg isn't a universal replacement for warehouses or the modern data stack.
A warehouse-centered ELT path can still be enough. Teams can load data,
transform it with SQL and dbt-style workflows, then expose marts or BI before
they need a separate lakehouse table-format layer.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
That keeps Iceberg as a requirement-led table-format choice, especially when
one warehouse already serves the workload.

A table format doesn't replace reproducible pipelines or workflow engines.
Teams still need versioning plus lineage and governance.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]]
Teams need a reliable path to load and transform the data before Iceberg adds
much value. They also need to test and serve it.

## Storage, Metadata, and Catalogs

Iceberg is useful when the team needs open lake storage with a table layer that
multiple compute engines can use. Storage and compute are separate from access,
metadata, and lineage. Catalog tools such as AWS Glue sit in that boundary.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
In Adrian Brudaru's framing, the underlying files can stay Parquet while
Iceberg supplies table metadata above them. That's why the format is discussed
as a lock-in reduction tool, not just as a faster file layout
[[cite:trends-in-modern-data-engineering@19:11=>Modern Data Engineering Trends]].

That lock-in reduction has a second edge. Vendors can still capture value
through catalogs, because catalogs map data to compute and manage access,
metadata, and lineage. Iceberg opens the table layer, but the platform still
has to choose and operate the catalog boundary
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]].

The catalog boundary matters because Iceberg doesn't decide who may access a
table, whether the table is fresh, or how downstream users discover lineage.
Those questions belong with [[Data Governance]], [[DataOps]], and
[[Data Engineering Platforms]].

Data lakes can become data swamps when ownership and governance are weak.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
Iceberg can make files behave like tables. The team still has to own quality,
access, and discoverability around those tables.

## DLT, DuckDB, and Headless Tables

Iceberg also appears in smaller, cost-aware pipeline designs. [[DuckDB]], GitHub
Actions, headless table formats, and DLT support for Delta Lake and Iceberg all
belong to that thread.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
That makes Iceberg relevant beyond large cloud lakehouse migrations when a team
still needs open table semantics.

Iceberg appears beside [[Delta Lake]] and Hudi in Adrian Brudaru's
table-format discussion.
[[cite:trends-in-modern-data-engineering@49:42=>Modern Data Engineering Trends]]
For side-by-side selection, use [[Delta Lake vs Apache Iceberg]].

Orchestration stays close to the table-format choice because portable tables
need repeatable jobs. The options include Airflow, Prefect, Dagster, and GitHub
Actions. Workflow engines also belong inside scalable platform architecture.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]][[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Iceberg can keep tables open, but [[orchestration]] still has to cover loading
and transformation plus testing and recovery.

## Operating Fit

Iceberg works best when the team can operate the platform around it. Weak
governance raises the risk because data lakes still need ownership and cleanup.
Scalable platforms need storage and compute plus workflow engines with lineage
and versioning.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]][[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Teams should plan those operating choices with the table format instead of
treating Iceberg as a storage-only change.

Iceberg belongs beside [[DataOps]] and [[Modern Data Stack]], and it also belongs
beside [[Data Engineering Platforms]]. It changes where table metadata lives and
how engines can share data. Teams still need to handle ingestion and
transformation. They also need scheduling, quality, cost, and documentation.

## Related Pages

Continue with these adjacent topics:

- [[Data Warehouse vs Data Lakehouse]]
- [[Data Engineering Platforms]]
- [[Data Lake]]
- [[Delta Lake]]
- [[Delta Lake vs Apache Iceberg]]
- [[DuckDB]]
- [[Modern Data Stack]]
- [[ETL vs ELT]]
- [[DataOps]]
- [[Data Governance]]
- [[Data Quality and Observability]]
