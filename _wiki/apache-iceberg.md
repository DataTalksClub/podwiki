---
layout: wiki
title: "Apache Iceberg"
summary: "How Apache Iceberg fits lakehouse design, open table formats, catalogs, governance, and platform operations."
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

Apache Iceberg is an open table format for lakehouse-style storage. Iceberg sits
above Parquet files and below query engines. That puts table metadata between
raw lake storage and the systems that read or write the data.
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

Use [[Data Warehouse vs Data Lakehouse]] for the warehouse-versus-lakehouse
architecture choice and [[Data Lake]] for the raw-storage model. Iceberg stays a
requirement-led table-format choice. It matters when teams need open table
metadata on lake storage across more than one compute engine
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]].

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

Teams should decide catalog ownership up front because Iceberg can keep the
table layer open. The team still chooses who runs the catalog and how access
rules attach to it. The team also has to judge how much vendor control that
catalog creates
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]].

Iceberg has to sit inside a governed platform because data lakes still need
ownership and cleanup
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

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
