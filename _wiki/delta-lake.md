---
layout: wiki
title: "Delta Lake"
summary: "How DataTalks.Club podcast discussions place Delta Lake in lakehouse table-format choices, especially beside Apache Iceberg, Hudi, DuckDB, DataOps, data lakes, and governance."
related:
  - Apache Iceberg
  - Data Lake
  - Data Warehouse vs Data Lakehouse
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - DuckDB
  - Data Governance
---

Delta Lake appears in the DataTalks.Club archive as an open lakehouse table
format rather than as a standalone architecture. The strongest discussion comes
from [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
He first explains [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }})
as a table format over Parquet storage. Later, he compares Delta Lake, Hudi,
and Iceberg as table-format choices (18:17 and 49:42).

That matters because the archive usually talks about Delta Lake through
comparison. This topic covers the Delta Lake side of the lakehouse discussion.
Treat the Iceberg page as the deeper archive-backed explanation of open table
formats, catalogs, metadata, and vendor lock-in. Use
[Data Lake]({{ '/wiki/data-lake/' | relative_url }}) for the storage layer and
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
for the architecture tradeoff.

For the dedicated side-by-side decision page, use
[Delta Lake vs Apache Iceberg]({{ '/comparisons/delta-lake-vs-apache-iceberg/' | relative_url }}).

## Archive Definition

In the archive context, Delta Lake is a table format for lakehouse storage. It
sits above files in a [data lake]({{ '/wiki/data-lake/' | relative_url }}) and
helps teams add table behavior to open storage. That table layer belongs
beside compute engines, catalogs, metadata, and lineage. It also belongs beside
access controls.

Brudaru's episode gives the clearest layer model. He separates storage and
compute from access, metadata, and lineage. He does this while explaining
Iceberg and catalogs. At 30:31, he says DLT supports Delta Lake and Iceberg in the same
headless-table-format discussion
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-30:31). Delta Lake therefore enters the archive as one table-format
choice inside a broader [data engineering platform]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) supplies the
older platform framing. In
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he describes raw lake storage, object storage, and governance. He also covers
ingress, egress, and self-service SQL
(21:29-30:34 and 1:07:52).

That context keeps Delta Lake from becoming a magic label. A table format helps
only when the team also operates the platform around the table.

## Delta, Hudi, and Iceberg

Brudaru's 49:42 chapter compares Delta Lake with Hudi and Iceberg in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
Earlier in the same episode, he criticizes buying a packaged modern data stack
without decomposing the layers. Later, he argues for requirements-led tool
selection (14:32 and 44:42).

That sequence is important: the archive doesn't say "choose Delta Lake" in
general. It says teams should pick the table format after they name storage,
compute, and catalog constraints. Cost and governance matter too.

Delta Lake also appears beside Iceberg in the DLT chapter. Brudaru connects
cost-efficient pipelines with
[DuckDB]({{ '/wiki/duckdb/' | relative_url }}) and GitHub Actions. He then
moves to headless table formats before naming DLT support for Delta Lake and
Iceberg
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
25:58-30:31). That makes Delta Lake relevant to smaller, portable pipeline
experiments as well as larger lakehouse platforms.

The archive gives less detail about Hudi on this page's source path. Hudi is
useful as the third named comparison point, but the reusable archive synthesis
is about the decision boundary. Table formats differ in engine support,
catalog integration, operational maturity, and lock-in risk.

## Contrast With Iceberg

[Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }}) has stronger
coverage in the archive. Brudaru names Iceberg adoption as a 2025 trend, then
uses it to explain Parquet-backed table formats and reduced vendor lock-in
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
16:40-18:17). He also spends time on catalogs, metadata, and lineage. DuckDB
and headless formats come before the later Delta/Hudi/Iceberg comparison.

So the safest archive-backed distinction isn't a feature-by-feature verdict:
Iceberg is the format the podcast explains most fully. Delta Lake is the
adjacent format the same episode places in the comparison set and in DLT
support. For open storage, multi-engine access, and vendor-lock-in reduction,
the archive points readers to the Iceberg discussion first. Some teams already
use Delta Lake tooling.

Some pipeline tools may need Delta Lake support. The archive treats those cases
as part of the same lakehouse table-format family.

That distinction keeps the page honest. Delta Lake can be a legitimate
lakehouse format, but the DataTalks.Club evidence is thinner than the Iceberg
evidence. Claims about Delta Lake should stay tied to the comparison chapter,
DLT support, and the wider lakehouse platform discussion.

## Table-Format Triggers

Delta Lake matters when a team needs table semantics on lake storage.

At least one concrete requirement is usually present:

- Multiple engines need to read and write shared tables.
- The team wants to keep data in open storage.
- The platform needs versioned table metadata rather than loose files.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains why the
storage boundary matters in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
She contrasts warehouses, marts, and data lakes. She then warns that unmanaged
lakes become data swamps without governance and ownership (15:30-24:24). Her
episode doesn't center Delta Lake, but it explains the problem that lakehouse
formats try to solve. Flexible storage still needs structure, trust, and
consumer-facing access.

Albertsson adds the [DataOps]({{ '/wiki/dataops/' | relative_url }}) version.
He argues for immutable, reproducible platform design before he discusses raw
lake storage and object storage. He also covers compute engines and workflow
engines. Lineage, versioning, and lakehouse architecture come later
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-35:57 and 1:04:18-1:07:52).

Delta Lake fits this kind of platform only when the team also runs the
ingestion and transformation paths around it. It also needs testing and access
paths.

Table formats matter less when the main bottleneck is analyst-facing modeling.
Kwong's [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
discussion shows why a warehouse-centered ELT flow can be enough for many
teams. They may get more value from ingestion reliability and dbt-style
transformation before they change the lake table format. Orchestration,
documentation, and reverse data flows may matter more too
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-18:47 and 30:59-35:42).

## Platform and Governance Work

Delta Lake belongs in the platform layer. A team still needs catalog choices,
metadata, and lineage around the table format. Permissions and cost controls
belong there too.

Brudaru names access, metadata, and lineage while explaining the database
layers behind lakehouse systems
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
21:27-23:41). That connects Delta Lake directly to
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), because the
format doesn't decide dataset ownership. It also doesn't decide access rights
or downstream trust.

This is also why the warehouse-versus-lakehouse decision should start from the
consumer and operating model. A [data warehouse vs data lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
choice isn't mainly a brand choice. It's a choice about where storage,
compute, trust, and access should live. Brudaru's requirements-led guidance
and Albertsson's platform chapters both support that reading
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
44:42).
Albertsson supports it in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
30:34-35:57.

For Delta Lake specifically, the practical archive-backed checks are:

- Name the engines that need to read and write the same lakehouse tables.
- Choose the catalog that will hold metadata, lineage, and access information.
- Confirm whether the team's ingestion or platform tooling already supports
  Delta Lake.
- Compare the requirement with Iceberg's archive-supported open-storage and
  lock-in story.
- Assign ownership for governance, tests, documentation, and table operation.

Those questions keep Delta Lake tied to the archive's main lesson. Table
formats matter when they serve a real lakehouse requirement. They don't replace
the platform, governance, and DataOps work that makes lake data useful.

## Related Pages

Continue with these adjacent archive topics:

- [Delta Lake vs Apache Iceberg]({{ '/comparisons/delta-lake-vs-apache-iceberg/' | relative_url }})
- [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }})
- [Data Lake]({{ '/wiki/data-lake/' | relative_url }})
- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [DuckDB]({{ '/wiki/duckdb/' | relative_url }})
