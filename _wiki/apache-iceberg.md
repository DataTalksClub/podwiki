---
layout: wiki
title: "Apache Iceberg"
summary: "Apache Iceberg as an open table format for lake storage, catalogs, governance, interoperability, and lock-in reduction."
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

Apache Iceberg is an open table format for lakehouse-style storage. It sits
above Parquet files and below query engines. The shared table metadata is
separate from raw [[data-lake=>data lake]] storage and compute
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]].

Iceberg's topic is its table-format, catalog, governance, and interoperability
role. [[Data Lake]] covers the storage layer. [[Data Warehouse vs Data Lakehouse]]
covers the warehouse-lakehouse architecture choice. [[Delta Lake vs Apache
Iceberg]] covers the direct format comparison with [[Delta Lake]].

## Open Table Metadata

Iceberg gives lake files table behavior by pairing Parquet storage with table
metadata. Adrian Brudaru ties that separation to lock-in reduction. Files can
stay in open storage while the table layer gives engines a consistent way to
read and write the data
[[cite:trends-in-modern-data-engineering@19:11=>Modern Data Engineering Trends]].

That makes Iceberg a [[data-engineering-platforms=>platform]] topic, not only a
file-format topic. The team still has to name which engines write tables, which
engines read them, and how jobs create repeatable table changes. That operating
work connects Iceberg to [[DataOps]], [[orchestration]], and
[[Data Quality and Observability]]
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

## Catalogs, Governance, and Lock-In

Catalogs sit next to Iceberg because access, metadata, and lineage live outside
raw storage and compute. Brudaru names AWS Glue as one example. He also warns
that vendors can still capture value through catalogs even when the table format
is open
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]].

That's the governance question Iceberg doesn't answer. The format can keep
table metadata open, but teams still need owners for access rules and
freshness. They also need owners for discovery and lineage. Those
responsibilities belong with [[Data Governance]], [[DataOps]], and the surrounding
[[data-engineering-platforms=>data engineering platform]]
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

Teams should decide catalog ownership before treating Iceberg as a lock-in
reduction strategy. If the catalog controls discovery, permissions, and engine
access, the catalog can become the new platform dependency
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]].

## Interop Beyond One Engine

Iceberg matters when more than one engine needs shared lake tables. Brudaru's
discussion separates storage and compute from access, metadata, and lineage.
The table format becomes the shared metadata layer between open files and
several compute surfaces
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]].

The same episode links open table formats to smaller cost-aware designs. Those
designs include [[DuckDB]], GitHub Actions, headless tables, and DLT support for
both Iceberg and Delta Lake
[[cite:trends-in-modern-data-engineering@30:31=>Modern Data Engineering Trends]].
That puts Iceberg in two settings. Teams can use it in large governed
lakehouses and in portable pipelines that still need open table semantics.

## Iceberg's Boundary

Iceberg doesn't replace lakehouse architecture, [[Data Governance]], or workflow
design. A lakehouse still needs object storage and compute. It also needs
ingress, egress, self-service SQL, and workflow engines
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Iceberg owns the table metadata layer inside that architecture.

Choose Iceberg when open table metadata, shared engine access, and catalog
strategy are the real requirements.

- For raw file retention, start with [[Data Lake]].
- For warehouse-style analytics versus lakehouse architecture, start with
  [[Data Warehouse vs Data Lakehouse]].
- For Delta or Iceberg, use [[Delta Lake vs Apache Iceberg]].

## Related Pages

Continue with these adjacent topics:

- [[Delta Lake vs Apache Iceberg]]
- [[Delta Lake]]
- [[Data Lake]]
- [[Data Warehouse vs Data Lakehouse]]
- [[Data Engineering Platforms]]
- [[DataOps]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[DuckDB]]
