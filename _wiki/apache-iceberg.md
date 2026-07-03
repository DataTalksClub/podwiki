---
layout: wiki
title: "Apache Iceberg"
summary: "How podcast guests place Apache Iceberg in lakehouse design, open table formats, catalogs, governance, and Delta Lake comparisons."
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
[[data-engineering-platforms=>data engineering platform]]
problem. Teams want lake-style storage without giving up table behavior,
metadata, or catalogs. They also want multiple compute paths. Iceberg is a table
format over Parquet storage. That separates storage and compute from access,
metadata, and lineage
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Apache Iceberg belongs in the
[[data warehouse vs data lakehouse]]
conversation. Use [[Data Lake]] for the
broader storage concept. Use [[Delta Lake]]
for the adjacent table format and
[[Modern Data Stack]] for the
warehouse-centered ELT stack Iceberg is often compared against.

## Table Format for Lakehouse Storage

Iceberg isn't a warehouse replacement because it sits above files and below
query engines. Parquet anchors the storage layer, while Iceberg adds catalogs
and access controls. It also tracks metadata and lineage
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Iceberg fits the
[[data-warehouse-vs-data-lakehouse=>lakehouse]]
idea when teams need table behavior on lake storage instead of a single
vendor-owned surface. The lakehouse is warehouse features layered onto a data
lake. The DataOps discussion separates raw storage, aggregates, and object
storage. It also covers ingress, egress, and self-service SQL
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Iceberg fits that architecture when the table layer must serve more than one
compute engine or platform surface.

Iceberg helps teams put table semantics and metadata on open lake storage, but
only matters when the team also owns the catalog and access model. Lineage,
quality, and workflow choices belong with those tables too. Those layers are
explicit in the catalog discussion. The DataOps discussion ties lakehouse
usefulness to reproducibility, versioning, and platform operation
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
[[podcast:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]]).

## Table Format, Governance, and Platform Views

Iceberg is part of a 2025 shift toward open, decomposed data platforms.
The episode criticizes vendor-packaged modern stacks. It names Iceberg adoption
as a trend, and tool selection stays requirements-led
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
That view starts from the table format and expands into catalogs, cost, and DLT
support. It also covers DuckDB, orchestration, and lock-in.

An earlier modern-stack view doesn't center Iceberg, but it explains the storage
problem Iceberg tries to improve. Warehouses, marts, and lakes are distinct, and
unmanaged lakes become data swamps without governance and ownership
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
That makes Iceberg a possible table-format choice, not a substitute for
governance.

A DataOps and platform-design view emphasizes immutable pipelines,
reproducibility, and object storage. Workflow engines, compute options, lineage,
and versioning come before lakehouse architecture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
That keeps Iceberg-like decisions inside the broader operating model. If a team
can't reproduce and serve the data, a table format alone won't create a
platform.

## Storage, Metadata, and Catalogs

The lakehouse separates into layers. Files sit in storage, and Parquet is the
columnar file format. Iceberg supplies the table format above those files.
Compute engines read and write through that table layer rather than owning the
data
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

The catalog is the next boundary, holding metadata and lineage in the same
layer. AWS Glue and peer tools are examples
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Those catalog responsibilities put Iceberg beside
[[Data Governance]] and
[[Data Quality and Observability]].
The table format doesn't answer who may access a table, whether the table is
fresh, or how downstream consumers discover lineage.

The DataOps view explains why this metadata work matters because object storage
sits beside governance, ingress, and egress. The same platform view includes
self-service SQL, workflow engines, and compute choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Iceberg is useful in that architecture when the team makes the table layer part
of a governed platform rather than a pile of files.

## Comparison With Delta Lake and Hudi

A direct Delta/Hudi/Iceberg comparison follows the earlier chapters on Iceberg
and catalogs. It also covers headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Teams choose more than a file layout. The table format affects engines and
catalogs. It also affects vendors and operating practices.

Iceberg enters as the open-storage and lock-in-sensitive option. It's tied to
vendor lock-in reduction and headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Use [[Delta Lake]] for the adjacent
topic node, but keep the comparison tied to the requirement. The practical
question is which table format best supports the engines, catalog, governance,
and cost model the team actually needs. For the dedicated comparison, use
[[Delta Lake vs Apache Iceberg]].

## DLT, DuckDB, and Headless Tables

Iceberg links to smaller and more portable pipeline designs. The trends episode
covers cost-efficient pipelines with DuckDB and GitHub Actions. It also covers
headless table formats and DLT support for both Delta Lake and Iceberg
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
That makes Iceberg relevant outside large cloud lakehouse migrations.

The [[DuckDB]] link matters because
DuckDB's embeddable OLAP and portable query paths belong to the same cost-aware
table-format discussion
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
A team can test the open-table-format idea on a small pipeline before it commits
to a larger lakehouse platform.

Iceberg still needs orchestration and DataOps. Airflow compares with peer
orchestration tools, and workflow engines are core platform components
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
[[podcast:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]]).
Iceberg can keep tables open, but the team still needs a reliable path for
loading, transforming, and testing them.

## Use Cases and Triggers

Iceberg matters when open storage is an actual constraint because vendor lock-in
reduction is central to the Iceberg chapter. Tool-selection guidance asks teams
to choose from requirements rather than trend labels
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
If one warehouse already handles the workload, Iceberg may add more platform
work than value.

Iceberg also matters when multiple engines need to share data. The same
discussion separates storage, compute, access, and metadata while covering DuckDB
and headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
This fits teams that need SQL engines, batch jobs, local analysis, and other
compute paths over the same tables.

Iceberg matters less when the main problem is analyst-facing modeling. A
warehouse-centered ELT path can be enough. Teams can load data and transform it
with SQL and dbt-style workflows. Then they can expose marts and BI before
orchestrating the stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
In that case, improve
[[analytics engineering]],
[[dbt]], and
[[orchestration]] before changing
the table format.

Teams take more risk with Iceberg when governance is weak. The modern-stack
episode warns that unmanaged lakes become data swamps
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The DataOps episode puts governance and lineage inside the platform design
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Teams should solve ownership and trust at the same time as the table-format
decision.

## Fit in Data Engineering Platforms

Iceberg belongs in the platform layer, not only the storage layer. A scalable
data platform breaks into storage, compute, and workflow engine components. The
DataOps episode names Spark, Flink, containers, and managed services as compute
choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
The 2025 table-format and catalog discussion follows the same split
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

That puts Iceberg beside [[ETL vs ELT]],
[[DataOps]], and
[[Modern Data Stack]] rather than
above them.

Teams still need ingestion, transformations, and scheduling. They also need
quality checks, cost controls, and consumer-facing documentation. Iceberg
changes where table metadata lives and how engines can share data. It doesn't
remove the platform
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
