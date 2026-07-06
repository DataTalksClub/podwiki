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

Apache Iceberg is an open table format for lakehouse-style storage. It matters
when teams need shared table metadata, catalog decisions, governance
boundaries, and access from more than one engine. It sits above Parquet files
and below query engines, so table metadata stays separate from raw
[[data-lake=>data lake]] storage and compute
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]].

[[Data Lake]] covers the storage layer. [[Data Warehouse vs Data Lakehouse]]
covers the warehouse-lakehouse architecture choice, and
[[Delta Lake vs Apache Iceberg]] owns the direct format comparison with
[[Delta Lake]].

## Table Metadata Over Lake Files

Iceberg gives lake files table behavior by pairing Parquet storage with table
metadata. The table layer can allow updates without rewriting whole files. The
files can stay in open storage while engines use shared metadata to read and
write the data
[[cite:trends-in-modern-data-engineering@19:11=>Modern Data Engineering Trends]].

That makes Iceberg a [[data-engineering-platforms=>platform]] topic, not only a
file-format topic. Teams still have to name which engines write tables, which
engines read them, and how jobs create repeatable table changes. That operating
work connects Iceberg to [[DataOps]], [[orchestration]], and
[[Data Quality and Observability]]
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

## Catalog Ownership and Lock-In

Catalogs sit next to Iceberg because access, metadata, and lineage live outside
raw storage and compute. A catalog maps data to compute, manages access, and may
also include metadata such as lineage. AWS Glue is one example of this catalog
layer
[[cite:trends-in-modern-data-engineering@21:27=>Modern Data Engineering Trends]]
[[cite:trends-in-modern-data-engineering@23:41=>Modern Data Engineering Trends]].

An open table format doesn't remove vendor dependency. Vendors can still capture
value through catalogs, so the dependency boundary moves from files and engines
toward metadata, access, and discovery
[[cite:trends-in-modern-data-engineering@19:11=>Modern Data Engineering Trends]].
That's the governance question Iceberg doesn't answer.

Catalog ownership should be explicit before Iceberg becomes a lock-in reduction
strategy. Useful catalog entries need technical metadata, lineage, and business
meaning. Enforcement may sit in a catalog interface or in the storage control
plane. That ties Iceberg decisions to [[Data Governance]] as much as to storage
[[cite:cloud-data-governance@45:04=>Cloud Data Governance]]
[[cite:cloud-data-governance@54:37=>Cloud Data Governance]].

## Multi-Engine and Headless Pipelines

Iceberg matters when more than one engine needs shared lake tables. The
lakehouse platform separates storage and compute from access, metadata, and
lineage. Iceberg can act as a table-metadata layer between open files and
several compute surfaces
[[cite:trends-in-modern-data-engineering@18:17=>Modern Data Engineering Trends]].

The same direction appears in smaller cost-aware designs. [[DuckDB]] provides a
local access layer for data pipelines, and headless table formats can pair with
cheap compute such as GitHub Actions. Headless table-format work was already
serving Delta Lake and moving toward similar Iceberg support
[[cite:trends-in-modern-data-engineering@30:31=>Modern Data Engineering Trends]].
That puts Iceberg inside [[modern-data-engineering-trends=>modern data engineering trends]]
in two settings: governed lakehouses and portable pipelines that still need
open table semantics.

## Iceberg Scope

Use Iceberg for table metadata, not for the whole lakehouse decision. A
lakehouse still needs object storage and compute. Teams also need ingress,
egress, self-service SQL, and workflow engines
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Those platform choices belong in [[Data Warehouse vs Data Lakehouse]] and
[[Data Engineering Platforms]].

Keep metadata, catalogs, interoperability, and lock-in details here while
[[Delta Lake vs Apache Iceberg]] covers the table-format choice.

## Related Pages

Key neighboring pages:

- [[Delta Lake vs Apache Iceberg]]
- [[Delta Lake]]
- [[Data Lake]]
- [[Data Warehouse vs Data Lakehouse]]
- [[Data Engineering Platforms]]
- [[DataOps]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[DuckDB]]
