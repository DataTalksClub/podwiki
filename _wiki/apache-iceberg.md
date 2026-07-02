---
layout: wiki
title: "Apache Iceberg"
summary: "How DataTalks.Club podcast guests place Apache Iceberg inside lakehouse architecture, open table formats, catalogs, Parquet storage, Delta Lake and Hudi comparisons, DLT support, and data engineering platform design."
related:
  - Data Engineering Platforms
  - Data Lake
  - Delta Lake
  - Modern Data Stack
  - DataOps
  - DuckDB
  - Data Governance
---

Apache Iceberg is a table-format answer to a specific
[[data-engineering-platforms|data engineering platform]]
problem: teams want lake-style storage without giving up table behavior,
metadata, or catalogs, and they want multiple compute paths. Iceberg is a table
format over Parquet storage, which separates storage and compute from access,
metadata, and lineage
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Apache Iceberg belongs in the
[[data warehouse vs data lakehouse]]
conversation. Use [[Data Lake]] for the
broader storage concept, [[Delta Lake]]
for the adjacent table format, and
[[Modern Data Stack]] for the
warehouse-centered ELT stack Iceberg is often compared against.

## Table Format for Lakehouse Storage

Iceberg isn't a warehouse replacement. It's a table format that sits above files
and below query engines, anchored in Parquet storage, with layers that make the
table usable: storage and compute decisions, access, metadata, lineage, and
catalogs
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Iceberg fits the
[[data-warehouse-vs-data-lakehouse|lakehouse]]
idea when teams need table behavior on lake storage instead of a single
vendor-owned surface. The lakehouse is warehouse features layered onto a data
lake, on top of separated raw storage, aggregates, and object storage, with
ingress, egress, and self-service SQL
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Iceberg fits that architecture when the table layer must serve more than one
compute engine or platform surface.

Iceberg helps teams put table semantics and metadata on open lake storage, but
only matters when the team also owns the catalog and access model; lineage,
quality, and workflow choices belong with those tables too. Those layers are
explicit in the catalog discussion, and lakehouse usefulness ties to
reproducibility, versioning, and platform operation
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

## Table Format, Governance, and Platform Views

Iceberg is part of a 2025 shift toward open, decomposed data platforms:
vendor-packaged modern stacks draw criticism, Iceberg adoption is named as a
trend, and tool selection stays requirements-led
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
That view starts from the table format and expands into catalogs and cost, then
DLT support, DuckDB, orchestration, and lock-in.

An earlier modern-stack view doesn't center Iceberg but explains the storage
problem it tries to improve: warehouses, marts, and lakes are distinguished, and
unmanaged lakes become data swamps without governance and ownership
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
That makes Iceberg a possible table-format choice, not a substitute for
governance.

A DataOps and platform-design view emphasizes immutable pipelines,
reproducibility, and object storage, with workflow engines, compute options,
lineage, and versioning coming before lakehouse architecture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
That keeps Iceberg-like decisions inside the broader operating model: if a team
can't reproduce and serve the data, a table format alone won't create a
platform.

## Storage, Metadata, and Catalogs

The lakehouse separates into layers. Files sit in storage, Parquet is the
columnar file format, and Iceberg supplies the table format above those files;
compute engines read and write through that table layer rather than owning the
data outright
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

The catalog is the next boundary, holding metadata and lineage in the same
layer, with AWS Glue and peer tools as examples
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Those catalog responsibilities put Iceberg beside
[[Data Governance]] and
[[Data Quality and Observability]].
The table format doesn't answer who may access a table, whether the table is
fresh, or how downstream consumers discover lineage.

The DataOps view explains why this metadata work matters: object storage sits
beside governance, ingress, egress, self-service SQL, workflow engines, and
compute choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Iceberg is useful in that architecture when the team makes the table layer part
of a governed platform rather than a pile of files.

## Comparison With Delta Lake and Hudi

A direct Delta/Hudi/Iceberg comparison follows the earlier chapters on Iceberg
and catalogs, and also covers headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Teams choose more than a file layout, because the table format affects engines,
catalogs, vendors, and operating practices.

Iceberg enters as the more open-storage and lock-in-sensitive option, tied to
vendor lock-in reduction and headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Use [[Delta Lake]] for the adjacent
topic node, but keep the comparison tied to the requirement: which table format
best supports the engines, catalog, governance, and cost model the team actually
needs. For the dedicated comparison, use
[[Delta Lake vs Apache Iceberg]].

## DLT, DuckDB, and Headless Tables

Iceberg links to smaller and more portable pipeline designs: cost-efficient
pipelines with DuckDB and GitHub Actions, headless table formats, and DLT
support for both Delta Lake and Iceberg
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
That makes Iceberg relevant outside large cloud lakehouse migrations.

The [[DuckDB]] link matters because
DuckDB's embeddable OLAP and portable query paths belong to the same cost-aware
table-format discussion
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
A team can test the open-table-format idea on a small pipeline before it commits
to a larger lakehouse platform.

Iceberg still needs orchestration and DataOps: Airflow compares with peer
orchestration tools, and workflow engines are core platform components
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Iceberg can keep tables open, but the team still needs a reliable path for
loading, transforming, and testing them.

## Use Cases and Triggers

Iceberg matters when open storage is an actual constraint: vendor lock-in
reduction is central to the Iceberg chapter, and tool-selection guidance asks
teams to choose from requirements rather than trend labels
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
If one warehouse already handles the workload, Iceberg may add more platform
work than value.

Iceberg also matters when multiple engines need to share data: storage, compute,
access, and metadata are separated, alongside DuckDB and headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
This fits teams that need SQL engines, batch jobs, local analysis, and other
compute paths to operate over the same tables.

Iceberg matters less when the main problem is analyst-facing modeling. A
warehouse-centered ELT path can be enough: load data, transform with SQL and
dbt-style workflows, expose marts and BI, then orchestrate the stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
In that case, improve
[[analytics engineering]],
[[dbt]], and
[[orchestration]] before changing
the table format.

Teams take more risk with Iceberg when governance is weak: unmanaged lakes
become data swamps
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]),
and governance and lineage belong inside the platform design
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Teams should solve ownership and trust at the same time as the table-format
decision.

## Fit in Data Engineering Platforms

Iceberg belongs in the platform layer, not only the storage layer. A scalable
data platform breaks into storage, compute, and workflow engine components, with
Spark, Flink, containers, and managed services as compute choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]),
and the 2025 table-format and catalog version is the same split
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

That puts Iceberg beside [[ETL vs ELT]],
[[DataOps]], and
[[Modern Data Stack]] rather than
above them.

Teams still need ingestion, transformations, scheduling, quality checks, cost
controls, and consumer-facing documentation. Iceberg changes where table
metadata lives and how engines can share data; it doesn't remove the platform
work around the table.

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
</content>
