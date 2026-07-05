---
layout: wiki
title: "Data Lake"
summary: "Data lakes as flexible raw storage, plus the governance and DataOps work that keeps them useful."
related:
  - Data Engineering Platforms
  - Data Warehouse
  - Data Warehouse vs Data Lakehouse
  - Delta Lake
  - Delta Lake vs Apache Iceberg
  - Modern Data Stack
  - DataOps
  - Data Governance
---

Data lakes are broad analytical storage for raw or lightly staged data. They can
hold structured tables and click events. They can also hold logs and files.
Media, IoT payloads, and long-lived history fit too. Teams use that flexibility
to preserve source detail before they know every downstream question
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

For architecture tradeoffs, see [[Data Warehouse vs Data Lakehouse]]. For
table-format choice, see [[Delta Lake vs Apache Iceberg]] after the storage
decision has become a lakehouse design question. [[Delta Lake]] is one concrete
versioned table layer that can sit above lake storage. The data lake discussion
stays on storage, governance, and recovery.

## Flexible Raw Storage

Natalie Kwong contrasts data lakes with the warehouse-centered
[[modern-data-stack=>modern data stack]]. A warehouse is built for structured
analytical tables and SQL access. A lake is more open to different file types
and structures. Her KeepTruckin example uses IoT images and video. That example
shows why a team may need storage that a warehouse doesn't naturally handle
[[cite:data-engineering-tools-modern-data-stack@19:50=>ETL vs ELT and the Modern Data Stack]].

Lars Albertsson gives the platform version. He treats the lake as object
storage for raw dumps, often with systems such as S3 behind it. That raw layer
sits beside compute and a workflow engine. Teams turn stored data into usable
outputs with transformations, self-service access, and governance
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Together, the examples define a data lake as a storage boundary, not a full
analytics product. The lake can support analysts and data engineers. It can
also support application teams and ML teams. That only works when the
surrounding platform runs ingestion, transformation, access, and trust
mechanisms.

## Lake, Warehouse, and Lakehouse

Data lakes aren't a simple warehouse replacement. Warehouses and data lakes
serve different consumers, even as lakehouse systems bring the categories
closer. Analytics teams often work mainly inside the warehouse, where BI-facing
outputs, SQL models, and data marts live
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

Engineering and ML teams may rely on lake storage when files or events need a
more flexible store. Application data, media, and long history can push the same
way. That makes [[ETL vs ELT]] part of the same decision. ELT loads source data
first, then transforms it in an analytical destination. A warehouse can be that
destination, while a lake can be the durable landing zone
[[cite:data-engineering-tools-modern-data-stack@24:24=>ETL vs ELT and the Modern Data Stack]].

Teams enter the [[Data Warehouse vs Data Lakehouse]] comparison when they want
warehouse-like use on lake storage. Albertsson describes a lakehouse as a data
lake with interactive exploration and warehouse-style use
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Keep [[Apache Iceberg]] and [[Delta Lake]] in their own table-format pages unless
the storage question has already become a lakehouse design question.

The practical split is:

- Use a warehouse when the main work is governed SQL analytics, marts,
  dashboards, and activation.
- Use a lake when the team needs to preserve raw files, event streams, logs,
  media, or application history before every use case is known.
- Use a lakehouse when the team wants warehouse-like behavior on lake storage.
- Use both when raw history and modeled analytics serve different teams.

## Data Swamp Risk

Kwong names the failure mode directly: a data lake can become a data swamp. The
swamp is unused, low-quality, poorly understood data that people can't
confidently use. She ties the fix to [[Data Governance]] through data origin,
ownership, current usefulness, and cleanup rules
[[cite:data-engineering-tools-modern-data-stack@21:22=>ETL vs ELT and the Modern Data Stack]].

Albertsson makes the same point from the platform side. Dumping every dataset
into S3 and calling it a lake is easy. Getting value from the lake requires
control and governance. He also distinguishes retained raw data from the
curated datasets people actually consume
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Christopher Bergh adds a delivery warning in [[DataOps]]. Data lake and cloud
projects fail when teams postpone the question of who gets value. Teams should
optimize the whole value stream. That includes data engineers, governance staff,
analysts, and downstream consumers
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

## Raw Storage and Immutability

Albertsson argues for immutable data platforms because immutable datasets can be
shared, rerun, and reasoned about. Teams keep raw inputs and apply code-defined
transformations instead of changing rows in place
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

This is where a lake differs from a loose staging area. A useful lake keeps raw
events and source files stable enough for rebuilds and model reruns. Teams can
also audit changes and debug transformations from the same raw layer. Kwong's
clickstream example makes the same point. Raw clicks can remain in the lake
while analysts create derived outputs elsewhere
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

Bergh's DataOps view adds version control, tests, CI/CD, and observability. It
also adds automated runbooks and end-to-end versioning of code, models,
governance, and catalogs
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Those practices make the lake a recoverable system instead of shared storage
with a better name.

## Governance and Ownership

Kwong ties lake quality to ownership and cleanup. Teams need to know which data
is stale and which data has an owner. They also need to know which data should
be removed or ignored
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

Business analysts know which use cases still need a dataset. Analytics
engineers can trace those needs back to ingestion. Governance owners can remove
or quarantine data with no current or expected use case
[[cite:data-engineering-tools-modern-data-stack@43:02=>ETL vs ELT and the Modern Data Stack]].

Albertsson ties governance to architecture because object storage sits beside
ingress, egress, and self-service SQL. Lineage and versioning are part of the
same platform responsibility
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
That makes [[data-engineering-platforms=>data engineering platforms]] and
[[Data Governance]] part of the lake conversation from the start.

## Table Formats Sit Above Storage

Table formats sit above the lake rather than inside the storage definition.
Open table formats can add table metadata over files. The lake still needs owners, access
rules, quality signals, and repeatable jobs
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]].
Local query engines such as [[DuckDB]] can then query Parquet-backed lake data
for experiments without making the lake the compute platform
[[cite:trends-in-modern-data-engineering@25:58=>Modern Data Engineering Trends]].

The data-lake decision is whether flexible raw storage is needed. The format
choice comes later, when teams need shared table semantics over that storage.

## Related Pages

Use [[Data Warehouse]] for the warehouse side of the storage vocabulary. Use
[[Data Warehouse vs Data Lakehouse]] for the architecture tradeoff. Use
[[Delta Lake vs Apache Iceberg]] only after the team needs table semantics over
lake storage.

Use [[Modern Data Stack]] and [[ETL vs ELT]] for ingestion and transformation
boundaries. Use [[Data Engineering Platforms]], [[DataOps]], and
[[Data Governance]] for the operating practices that keep a lake from becoming
unused storage.
