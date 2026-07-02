---
layout: wiki
title: "Delta Lake"
summary: "How DataTalks.Club podcast discussions place Delta Lake in lakehouse table-format choices, especially beside Apache Iceberg, Hudi, DuckDB, DataOps, data lakes, and governance."
related:
  - Apache Iceberg
  - Data Lake
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - DuckDB
  - Data Governance
---

Delta Lake appears in DataTalks.Club podcast discussions as an open lakehouse
table format, not as a complete architecture. It sits above files in a
[[data lake]] and gives teams table
behavior on open storage. The surrounding
[[data-engineering-platforms|data engineering platform]]
still owns compute and catalogs. It also owns access, lineage, orchestration,
and cost.

[[person:adrianbrudaru|Adrian Brudaru]] gives the
clearest table-format framing in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]].
He first explains [[Apache Iceberg]]
as a table format over Parquet storage. He then separates storage and compute
from access, metadata, and lineage
([[podcast:trends-in-modern-data-engineering|18:17-23:41]]).
At 30:31 he says DLT is already serving headless Delta Lake and working on
similar Iceberg support. At 49:42 he compares Delta Lake, Hudi, and Iceberg as
related table-format options.

For architecture decisions, use
[[Data Warehouse vs Data Lakehouse]]
beside this page. For the direct format comparison, use
[[Delta Lake vs Apache Iceberg]].

## Lakehouse Table Layer

The lakehouse stack is covered end to end in
[[book:20220314-data-engineering-with-apache-spark-delta-lake-and-lakehouse|Data Engineering with Apache Spark, Delta Lake, and Lakehouse]]
by Manoj Kukreja, which treats Delta Lake as the table format above Spark and
open storage.

Delta Lake belongs to the table layer of a lakehouse. In Brudaru's layer model,
files and compute aren't enough. Catalogs and metadata sit around the table
format too, alongside access and lineage
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
21:27-23:41). That placement keeps Delta Lake close to
[[Data Governance]], because the
format can support table semantics but doesn't assign dataset ownership,
permissions, or trust.

[[person:larsalbertsson|Lars Albertsson]] gives the
older platform version of the same idea in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
He discusses raw lake storage and object storage. He also covers ingress,
egress, and self-service SQL. Workflow engines and lakehouse architecture appear
with lineage and versioning
([[podcast:dataops-principles-and-scalable-data-platforms|16:42-35:57 and 1:04:18-1:07:52]]).

Delta Lake fits that platform story only when the team can operate the
ingestion and transformation paths around the tables. It also needs testing,
access, and recovery paths.

## Delta Lake, Hudi, and Iceberg

Brudaru doesn't present Delta Lake as a default choice. In the same episode, he
criticizes buying a packaged
[[modern data stack]] without
decomposing its layers. He then argues for requirements-led tool selection
([[podcast:trends-in-modern-data-engineering|14:32 and 44:42]]).

The Delta/Hudi/Iceberg comparison at 49:42 follows that logic. Choose the table
format after the team names its storage and compute constraints. Catalog,
governance, and cost constraints belong in the same decision.

The DataTalks.Club material gives deeper coverage to
[[Apache Iceberg]] than to Delta
Lake. Brudaru names Iceberg adoption as a 2025 trend, describes it over
Parquet, and ties it to reduced vendor lock-in
([[podcast:trends-in-modern-data-engineering|16:40-18:17]]).
Delta Lake appears beside Iceberg through DLT support at 30:31 and the
Delta/Hudi/Iceberg comparison at 49:42. He also describes Delta as the most
mature of those three options in that comparison chapter.

That distinction matters for reuse across the wiki. Claims about open storage,
catalogs, metadata, and lock-in should usually point readers to the
[[apache-iceberg|Iceberg page]]. Claims about
Delta Lake should stay tied to tool support, Spark-oriented versioning, and
existing Delta-oriented lakehouse environments.

## Spark Versioning and Historical Reruns

[[person:roksolanadiachuk|Roksolana Diachuk]] provides
the clearest Delta-specific operating example in
[[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]].
She describes deduplication, month-old data mistakes, risky production
rewrites, and resource-heavy historical reruns. Then she names Delta Lake with
Spark as a way to track data versions and travel back to earlier data states
([[podcast:big-data-engineer-vs-data-scientist|58:05-1:00:25]]).

Her example places Delta Lake near
[[data quality and observability]],
[[data engineering tools]],
and [[data engineering platforms]].
The practical requirement isn't the name of the format. It's the ability to
recover from bad data, audit changes, rerun historical batches, and keep table
state understandable to engineers who operate Spark-based jobs.

## Portable and Smaller Lakehouse Work

Delta Lake also appears in Brudaru's discussion of leaner data pipelines. He
connects cost-efficient pipelines with
[[DuckDB]], GitHub Actions, and headless
table formats before naming DLT support for Delta Lake and Iceberg
([[podcast:trends-in-modern-data-engineering|25:58-30:31]]).
That sequence puts Delta Lake beside large lakehouse platforms and smaller
portable experiments where teams still want table semantics on files.

The same episode links table formats to
[[orchestration]]. Brudaru compares
Airflow, Prefect, Dagster, and GitHub Actions at 35:37. Albertsson places
workflow engines inside scalable platform architecture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
30:34-35:57). A Delta table is easier to justify when the surrounding jobs,
tests, catalogs, and access paths can support repeated reads and writes.

## Format Misfit

[[person:nataliekwong|Natalie Kwong]] explains why
storage flexibility alone isn't enough in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
She contrasts warehouses, marts, and lakes, then warns that unmanaged lakes
become data swamps without governance and ownership
([[podcast:data-engineering-tools-modern-data-stack|15:30-24:24]]).
Her episode doesn't center Delta Lake, but it explains the failure mode that
lakehouse table formats are often asked to address.

For analyst-facing work, a warehouse-centered ELT system may be enough. Kwong's
modern-data-stack discussion covers ingestion and dbt-style transformation. It
also covers orchestration, documentation, and reverse data flows
([[podcast:data-engineering-tools-modern-data-stack|7:57-18:47 and 30:59-35:42]]).

Before changing a lake table format, teams should ask where the bottleneck
sits:

- ingestion reliability
- [[dbt]] modeling
- [[analytics engineering]]
- documentation
- consumer access

For Delta Lake specifically, the grounded checks are concrete:

- Name the engines that need to read and write the same tables.
- Choose the catalog that will hold metadata and lineage.
- Confirm whether ingestion or platform tooling already expects Delta tables.
- Compare the requirement with Iceberg's open-storage and lock-in story.
- Assign ownership for governance, tests, documentation, and table operation.

Those checks keep Delta Lake inside the lakehouse platform discussion instead
of turning it into a generic data architecture label.
