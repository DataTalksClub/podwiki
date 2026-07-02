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

DataTalks.Club guests discuss Apache Iceberg as a table-format answer to a
specific [[data-engineering-platforms|data engineering platform]]
problem. Teams want lake-style storage without giving up table behavior,
metadata, or catalogs. They also want multiple compute paths. [[person:adrianbrudaru|Adrian Brudaru]]
explains Iceberg as a table format over Parquet storage. He then separates
storage and compute from access, metadata, and lineage in the same discussion
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-23:41).

Apache Iceberg belongs in the
[[data warehouse vs data lakehouse]]
conversation. Use [[Data Lake]] for the
broader storage concept. Use [[Delta Lake]]
for the adjacent table format and
[[Modern Data Stack]] for the
warehouse-centered ELT stack that Iceberg is often compared against.

## Table Format for Lakehouse Storage

In these episodes, Iceberg isn't presented as a warehouse replacement.
It's a table format that sits above files and below query engines. Brudaru
anchors the explanation in Parquet storage. He then moves into the layers that
make the table usable.

Teams still need storage and compute decisions, plus access and metadata.
Lineage and catalogs matter too
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-23:41).

Iceberg fits the
[[data-warehouse-vs-data-lakehouse|lakehouse]]
idea when teams need table behavior on lake storage instead of a single
vendor-owned surface. [[person:larsalbertsson|Lars Albertsson]]
describes the lakehouse as warehouse features layered onto a data lake after
he has already separated raw storage, aggregates, and object storage. He also
covers ingress, egress, and self-service SQL
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
21:29-30:34 and 1:07:52). Iceberg fits that architecture when the table layer must
serve more than one compute engine or platform surface.

Across these episodes, Iceberg helps teams put table semantics and metadata on
open lake storage. It matters only when the team also owns the catalog and
access model. Lineage, quality, and workflow choices belong with those tables
too.

Brudaru makes those layers explicit in the catalog chapters, while Albertsson
ties lakehouse usefulness to reproducibility and versioning. Platform
operation is part of the same discussion
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
21:27-23:41 and
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
1:04:18-1:07:52).

## Table Format, Governance, and Platform Views

[[person:adrianbrudaru|Adrian Brudaru]] treats Iceberg
as part of a 2025 shift toward open, decomposed data platforms. He criticizes
vendor-packaged modern stacks at 14:32. He names Iceberg adoption as a trend
at 16:40 and returns to requirements-led tool selection at 44:42
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

His version starts from the table format and quickly expands into catalogs and
cost. DLT support, DuckDB, orchestration, and lock-in come next.

[[person:nataliekwong|Natalie Kwong]] gives an earlier
modern-stack view. Her episode doesn't center Iceberg, but it explains the
storage problem Iceberg tries to improve. She distinguishes warehouses, marts,
and lakes. She then warns that unmanaged lakes become data swamps without
governance and ownership
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
15:30-27:39). That makes Iceberg a possible table-format choice, not a
substitute for governance.

[[person:larsalbertsson|Lars Albertsson]] starts from
DataOps and platform design. He emphasizes immutable pipelines,
reproducibility, and object storage, while workflow engines and compute
options matter too.

He also covers lineage and versioning before he discusses lakehouse architecture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
16:42-35:57 and 1:04:18-1:07:52). His framing keeps Iceberg-like decisions
inside the broader operating model. If a team can't reproduce and serve the
data, a table format alone won't create a platform.

## Storage, Metadata, and Catalogs

Brudaru's Iceberg explanation separates the lakehouse into layers. Files sit
in storage, and Parquet is the columnar file format. Iceberg supplies the table
format above those files. Compute engines read and write through that
table layer rather than owning the data outright
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-21:27).

The catalog is the next boundary. Brudaru's catalog chapter names metadata and
lineage as part of the same layer. It includes AWS Glue and peer tools as
examples
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
21:27-23:41).

Those catalog responsibilities put Iceberg beside
[[Data Governance]] and
[[Data Quality and Observability]].
The table format doesn't answer who may access a table. It also doesn't show
whether the table is fresh or how downstream consumers discover lineage.

Albertsson's DataOps episode explains why this metadata work matters. His
platform chapters place object storage beside governance, ingress, and egress.
He also includes self-service SQL, workflow engines, and compute choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
23:29-35:57). Iceberg is useful in that architecture when the team makes the
table layer part of a governed platform rather than a pile of files.

## Comparison With Delta Lake and Hudi

Brudaru gives the direct Delta/Hudi/Iceberg comparison. His 49:42 chapter
compares table formats after earlier chapters on Iceberg and catalogs.
He also discusses headless table formats
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-30:31 and 49:42).

Teams choose more than a file layout because the table format affects engines,
catalogs, vendors and operating practices.

Iceberg enters the discussion as the more open-storage and lock-in-sensitive
option. Brudaru connects Iceberg to vendor lock-in reduction at 18:17, then
returns to headless table formats at 30:31
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Use [[Delta Lake]] for the adjacent
topic node, but keep the comparison tied to the requirement. Ask which table
format best supports the engines, catalog, governance, and cost model the team
actually needs. For the dedicated comparison, use
[[Delta Lake vs Apache Iceberg]].

## DLT, DuckDB, and Headless Tables

Brudaru links Iceberg to smaller and more portable pipeline designs. At 27:40,
he discusses cost-efficient pipelines with DuckDB and GitHub Actions. He also
connects that setup to headless table formats. At 30:31, he says DLT supports
Delta Lake and Iceberg
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
That makes Iceberg relevant outside large cloud lakehouse migrations.

The [[DuckDB]] link matters because
Brudaru treats DuckDB's embeddable OLAP as part of the same cost-aware
table-format discussion. Portable query paths sit there too
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
25:58-30:31). A team can test the open-table-format idea on a small pipeline
before it commits to a larger lakehouse platform.

Iceberg still needs orchestration and DataOps, and Brudaru compares Airflow
with peer orchestration tools at 35:37. Albertsson treats workflow engines as
core platform components
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
35:37 and
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
30:34-35:57). Iceberg can keep tables open. The team still needs a reliable
path for loading, transforming and testing them.

## Use Cases and Triggers

Iceberg matters when open storage is an actual constraint because Brudaru
names vendor lock-in reduction in the Iceberg chapter. Later in the episode, his
tool-selection guidance asks teams to choose from requirements rather than
trend labels
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17 and 44:42). If one warehouse already handles the workload, Iceberg may
add more platform work than value.

Iceberg also matters when multiple engines need to share data. Brudaru
separates storage, compute, access, and metadata at 21:27. He then
discusses DuckDB and headless table formats at 25:58-30:31
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
This fits teams that need SQL engines, batch jobs, local analysis, and other
compute paths to operate over the same tables.

Iceberg matters less when the main problem is analyst-facing modeling. Kwong's
modern-stack episode shows why a warehouse-centered ELT path can be enough.
Teams can load data, then transform it with SQL and dbt-style workflows. They
can expose marts and BI, then orchestrate the stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
7:57-18:47 and 30:59-35:42). In that case, improve
[[analytics engineering]],
[[dbt]], and
[[orchestration]] before changing
the table format.

Teams take more risk with Iceberg when governance is weak. Kwong's data-lake
chapter warns about data swamps at 19:50-21:22 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Albertsson puts governance and lineage inside the platform design at
23:29-30:34 and 1:04:18-1:07:52 in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
Teams should solve ownership and trust at the same time as the table-format
decision.

## Fit in Data Engineering Platforms

Iceberg belongs in the platform layer, not only in the storage layer.
Albertsson breaks a scalable data platform into storage, compute, and workflow
engine components. He then adds Spark, Flink, containers and managed services
as compute choices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
30:34-35:57). Brudaru adds the 2025 table-format and catalog version of that
same split
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-23:41).

That puts Iceberg beside [[ETL vs ELT]].
It also belongs beside [[DataOps]] and
[[Modern Data Stack]] rather
than above them.

Teams still need ingestion and transformations. They also
need scheduling, quality checks, cost controls and consumer-facing
documentation. Iceberg
changes where table metadata lives and how engines can share data. It doesn't
remove the platform work around the table.

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
