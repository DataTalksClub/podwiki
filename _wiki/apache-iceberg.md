---
layout: wiki
title: "Apache Iceberg"
summary: "How DataTalks.Club podcast guests place Apache Iceberg inside lakehouse architecture, open table formats, catalogs, Parquet storage, Delta Lake and Hudi comparisons, DLT support, and data engineering platform design."
related:
  - Data Warehouse vs Data Lakehouse
  - Data Engineering Platforms
  - Data Lake
  - Delta Lake
  - Modern Data Stack
  - DataOps
  - ETL vs ELT
  - DuckDB
  - Data Governance
---

Apache Iceberg appears in the DataTalks.Club archive as a table-format answer
to a specific [data engineering platform]({{ '/wiki/data-engineering-platforms/' | relative_url }})
problem. Teams want lake-style storage without giving up table behavior,
metadata, or catalogs. They also want multiple compute paths. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
explains Iceberg as a table format over Parquet storage. He then separates
storage and compute from access, metadata, and lineage in the same discussion
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41).

Apache Iceberg belongs in the
[data warehouse vs data lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
conversation. Use [Data Lake]({{ '/wiki/data-lake/' | relative_url }}) for the
broader storage concept. Use [Delta Lake]({{ '/wiki/delta-lake/' | relative_url }})
for the adjacent table format and
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) for the
warehouse-centered ELT stack that Iceberg is often compared against.

## Starting Points

Related wiki pages:

- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
  places Iceberg in the open-storage lakehouse tradeoff.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  covers storage and compute choices, plus workflow, access, and support
  responsibilities.
- [Data Lake]({{ '/wiki/data-lake/' | relative_url }}) and
  [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }}) provide the
  older storage vocabulary.
- [Delta Lake]({{ '/wiki/delta-lake/' | relative_url }}) is the closest named
  comparison point in the podcast archive.
- [DuckDB]({{ '/wiki/duckdb/' | relative_url }}) connects to portable query
  engines and small, cost-aware table-format experiments.
- [DataOps]({{ '/wiki/dataops/' | relative_url }}),
  [Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
  [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  cover the operating practices that keep lakehouse tables trustworthy.
- [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) and
  [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) cover
  the ingestion and transformation choices around the storage layer.

Core podcast discussions:

- [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
  with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) is the
  main Iceberg episode. It covers 2025 Iceberg adoption at 16:40, Iceberg as a
  table format over Parquet at 18:17, and catalogs and metadata at
  21:27-23:41. It also covers headless table formats and DLT support at 30:31,
  plus the Delta/Hudi/Iceberg comparison at 49:42.
- [ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
  with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the
  warehouse, lake, and governance context. She covers data lakes at 19:50 and
  data swamps at 21:22. She also covers when teams keep a lake, warehouse, or
  both at 27:39.
- [DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  with [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives
  the platform context. He covers object storage, governance, and self-service
  SQL at 21:29-30:34. He then covers storage and compute components, lineage,
  versioning, and lakehouse architecture from 30:34 through 1:07:52.

## Common Definition

In the archive, Iceberg isn't presented as a warehouse replacement.
It's a table format that sits above files and below query engines. Brudaru
anchors the explanation in Parquet storage. He then moves into the layers that
make the table usable.

Teams still need storage and compute decisions, plus access and metadata.
Lineage and catalogs matter too
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41).

This connects Iceberg to the
[lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
idea rather than to a single vendor product. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
describes the lakehouse as warehouse features layered onto a data lake after
he has already separated raw storage, aggregates, and object storage. He also
covers ingress, egress, and self-service SQL
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
21:29-30:34 and 1:07:52). Iceberg fits that architecture when the table layer must
serve more than one compute engine or platform surface.

Across these episodes, Iceberg helps teams put table semantics and metadata on
open lake storage. It matters only when the team also owns the catalog and
access model. Lineage, quality, and workflow choices belong with those tables
too.

Brudaru makes those layers explicit in the catalog chapters, while Albertsson
ties lakehouse usefulness to reproducibility and versioning. Platform
operation is part of the same discussion
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
21:27-23:41 and
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:04:18-1:07:52).

## Guest Differences

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) treats Iceberg
as part of a 2025 shift toward open, decomposed data platforms. He criticizes
vendor-packaged modern stacks at 14:32. He names Iceberg adoption as a trend
at 16:40 and returns to requirements-led tool selection at 44:42
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

His version starts from the table format and quickly expands into catalogs and
cost. DLT support, DuckDB, orchestration, and lock-in come next.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives an earlier
modern-stack view. Her episode doesn't center Iceberg, but it explains the
storage problem Iceberg tries to improve. She distinguishes warehouses, marts,
and lakes. She then warns that unmanaged lakes become data swamps without
governance and ownership
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
15:30-27:39). That makes Iceberg a possible table-format choice, not a
substitute for governance.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) starts from
DataOps and platform design. He emphasizes immutable pipelines,
reproducibility, and object storage, while workflow engines and compute
options matter too.

He also covers lineage and versioning before he discusses lakehouse architecture
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-35:57 and 1:04:18-1:07:52). His framing keeps Iceberg-like decisions
inside the broader operating model. If a team can't reproduce and serve the
data, a table format alone won't create a platform.

## Storage, Metadata, and Catalogs

Brudaru's Iceberg explanation separates the lakehouse into layers. Files sit
in storage, and Parquet is the columnar file format. Iceberg supplies the table
format above those files. Compute engines read and write through that
table layer rather than owning the data outright
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-21:27).

The catalog is the next boundary. Brudaru's catalog chapter names metadata and
lineage as part of the same layer. It includes AWS Glue and peer tools as
examples
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
21:27-23:41). That connects Iceberg to
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
because the table format doesn't answer who may access a table. It also
doesn't answer whether a table is fresh or how downstream consumers discover
lineage.

Albertsson's DataOps episode explains why this metadata work matters. His
platform chapters place object storage beside governance, ingress, and egress.
He also includes self-service SQL, workflow engines, and compute choices
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
23:29-35:57). Iceberg is useful in that architecture when the team makes the
table layer part of a governed platform rather than a pile of files.

## Comparison With Delta Lake and Hudi

Brudaru gives the archive's direct Delta/Hudi/Iceberg comparison. His 49:42
chapter compares table formats after earlier chapters on Iceberg and catalogs.
He also discusses headless table formats
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-30:31 and 49:42).

Teams choose more than a file layout because the table format affects engines,
catalogs, vendors and operating practices.

Iceberg enters the discussion as the more open-storage and lock-in-sensitive
option. Brudaru connects Iceberg to vendor lock-in reduction at 18:17, then
returns to headless table formats at 30:31
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).
Use [Delta Lake]({{ '/wiki/delta-lake/' | relative_url }}) for the adjacent
topic node, but keep the comparison tied to the requirement. Ask which table
format best supports the engines, catalog, governance, and cost model the team
actually needs. For the dedicated comparison, use
[Delta Lake vs Apache Iceberg]({{ '/comparisons/delta-lake-vs-apache-iceberg/' | relative_url }}).

## DLT, DuckDB, and Headless Tables

Brudaru links Iceberg to smaller and more portable pipeline designs. At 27:40,
he discusses cost-efficient pipelines with DuckDB and GitHub Actions. He also
connects that setup to headless table formats. At 30:31, he says DLT supports
Delta Lake and Iceberg
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).
That makes Iceberg relevant outside large cloud lakehouse migrations.

The [DuckDB]({{ '/wiki/duckdb/' | relative_url }}) link matters because
Brudaru treats DuckDB's embeddable OLAP as part of the same cost-aware
table-format discussion. Portable query paths sit there too
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
25:58-30:31). A team can test the open-table-format idea on a small pipeline
before it commits to a larger lakehouse platform.

Iceberg still needs orchestration and DataOps, and Brudaru compares Airflow
with peer orchestration tools at 35:37. Albertsson treats workflow engines as
core platform components
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
35:37 and
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
30:34-35:57). Iceberg can keep tables open. The team still needs a reliable
path for loading, transforming and testing them.

## Use Cases and Triggers

Iceberg matters when open storage is an actual constraint because Brudaru
names vendor lock-in reduction in the Iceberg chapter. Later in the episode, his
tool-selection guidance asks teams to choose from requirements rather than
trend labels
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17 and 44:42). If one warehouse already handles the workload, Iceberg may
add more platform work than value.

Iceberg also matters when multiple engines need to share data. Brudaru
separates storage, compute, access, and metadata at 21:27. He then
discusses DuckDB and headless table formats at 25:58-30:31
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).
This fits teams that need SQL engines, batch jobs, local analysis, and other
compute paths to operate over the same tables.

Iceberg matters less when the main problem is analyst-facing modeling. Kwong's
modern-stack episode shows why a warehouse-centered ELT path can be enough.
Teams can load data, then transform it with SQL and dbt-style workflows. They
can expose marts and BI, then orchestrate the stack
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-18:47 and 30:59-35:42). In that case, improve
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[dbt]({{ '/wiki/dbt/' | relative_url }}), and
[orchestration]({{ '/wiki/orchestration/' | relative_url }}) before changing
the table format.

Teams take more risk with Iceberg when governance is weak. Kwong's data-lake
chapter warns about data swamps at 19:50-21:22 in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Albertsson puts governance and lineage inside the platform design at
23:29-30:34 and 1:04:18-1:07:52 in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Teams should solve ownership and trust at the same time as the table-format
decision.

## Fit in Data Engineering Platforms

Iceberg belongs in the platform layer, not only in the storage layer.
Albertsson breaks a scalable data platform into storage, compute, and workflow
engine components. He then adds Spark, Flink, containers and managed services
as compute choices
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
30:34-35:57). Brudaru adds the 2025 table-format and catalog version of that
same split
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41).

That puts Iceberg beside [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}).
It also belongs beside [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) rather
than above them.

Teams still need ingestion and transformations. They also
need scheduling, quality checks, cost controls and consumer-facing
documentation. Iceberg
changes where table metadata lives and how engines can share data. It doesn't
remove the platform work around the table.

## See Also

Continue with these adjacent archive topics:

- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Lake]({{ '/wiki/data-lake/' | relative_url }})
- [Delta Lake]({{ '/wiki/delta-lake/' | relative_url }})
- [Delta Lake vs Apache Iceberg]({{ '/comparisons/delta-lake-vs-apache-iceberg/' | relative_url }})
- [DuckDB]({{ '/wiki/duckdb/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
