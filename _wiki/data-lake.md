---
layout: wiki
title: "Data Lake"
summary: "How DataTalks.Club podcast guests use data lake as raw, flexible storage for files, events, logs, and long-lived history, plus the governance, table-format, and DataOps work needed to keep it useful."
related:
  - Data Engineering Platforms
  - Data Warehouse
  - Apache Iceberg
  - Delta Lake
  - Modern Data Stack
  - DataOps
  - Data Governance
---

DataTalks.Club guests use data lake to mean broad analytical storage for raw
or lightly staged data. It can hold structured tables and click events. It
can also hold logs and files, images and video, IoT payloads, and long-lived
history. Teams use that flexibility to keep source detail before they know
every downstream question.

That flexibility creates the main risk. The team needs ownership, catalogs,
quality checks, access rules and reproducible transformations. Without those
controls, a lake becomes a place where people dump data and stop trusting it.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
uses the data lake versus [data warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
comparison to explain that risk in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
19:50-27:39. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
then gives the platform version in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-30:34. He argues that raw storage works when the platform keeps data
immutable, governed, and reproducible.

## Definition and Scope

Kwong contrasts data lakes with the warehouse-centered
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). A
warehouse is built for structured analytical tables and SQL access. A lake is
more open to different file types and structures. Her KeepTruckin example uses
IoT images and video. It shows why a team may need storage that a warehouse
doesn't naturally handle
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
19:50).

Albertsson gives the platform definition. He treats the lake as object storage
for raw dumps, usually with systems such as S3 behind it. That raw layer sits
beside compute and a workflow engine. The platform turns stored data into
usable outputs through functional transformations, self-service access, and
governance
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
23:29-30:34).

Together, those episodes treat a data lake as a storage boundary, not a full
analytics product. A lake can support analysts and data engineers. It can also
support application and ML teams.

That only works when the team also operates ingestion and transformation. It
must also operate access and trust mechanisms around the lake. So this topic
belongs near [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). It also belongs near
[data governance]({{ '/wiki/data-governance/' | relative_url }}), not only near
storage.

## Lake, Warehouse, and Lakehouse

Kwong and Albertsson don't frame data lakes as a simple warehouse replacement.
Kwong argues that data warehouses and data lakes serve different consumers. An
analytics team often works mainly inside the warehouse. The warehouse contains
BI-facing outputs, SQL models and data marts.

Engineering teams may rely on a lake when files need a more flexible store.
Events and application data may need that too
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
24:24-27:39).

That makes [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) part of the
same decision. ELT loads source data first. The team then transforms it in an
analytical destination.

Kwong's episode explains why that gives analysts more flexibility when fields
or business questions change. A warehouse can be the destination. A lake or
lakehouse can also be the first durable landing zone
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-18:47).

Teams enter the [data warehouse vs data lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
comparison when they want warehouse-like behavior on lake storage. Albertsson
describes a lakehouse as something that technically looks like a data lake. It
adds interactive exploration and warehouse-style use
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:07:52).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
updates that vocabulary through open table formats. In
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
he explains [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }}) as a
table format over Parquet storage. He then separates storage and compute. He
also separates access, metadata, and lineage (18:17-23:41).

The practical split is:

- Use a warehouse when the main work is governed SQL analytics, marts,
  dashboards, and activation.
- Use a lake when the team needs to preserve raw files, event streams, logs,
  media, or application history before every use case is known.
- Use a lakehouse when the team wants open lake storage with table semantics,
  catalogs, metadata, and multiple compute engines.
- Use both when raw history and modeled analytics serve different teams.

## Data Swamp Risk

Kwong names the failure mode directly when she says a data lake can become a
data swamp. In her explanation, the swamp isn't just "too much data". It's
unused, low-quality, poorly understood data that people can't confidently use.
She ties the fix to [data governance]({{ '/wiki/data-governance/' | relative_url }}).

Teams need to know where data came from and who owns it. They also need to know
what it means and whether it's still useful
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22-24:24).

Albertsson makes the same point from the platform side. Dumping every dataset
into S3 and calling it a lake is easy. Getting value from the lake requires
control and governance. He also distinguishes retained raw data from the
curated datasets people actually consume
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
23:29-28:22).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) adds a
delivery warning in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
At 31:23, he criticizes data lake and cloud projects that postpone the question
of who gets value. In his DataOps framing, teams should optimize the whole
value stream. That stream includes data engineers and warehouse or lake teams.
It also includes governance staff, analysts and downstream consumers
(28:14-33:47).

A lake project that stops at storage hasn't delivered a reliable data product.

## Raw Storage and Immutability

Albertsson's strongest contribution is the immutability principle. He argues
that data platforms should make data immutable as much as possible. Immutable
datasets can be shared, rerun, and reasoned about. Instead of changing rows in
place and hoping old reports can be reproduced, teams keep raw inputs. They
apply code-defined transformations
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-21:29).

This is where a lake differs from a loose staging area. A useful lake keeps raw
events and source files stable enough for rebuilds and model reruns. Teams can
also audit changes and debug transformations from the same raw layer.

Kwong's clickstream example makes the same point in simpler terms. Raw clicks
can remain in the lake. Analysts can write queries and derived outputs
elsewhere
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
27:39-30:59).

Immutability also explains why [DataOps]({{ '/wiki/dataops/' | relative_url }})
belongs close to the lake. Bergh's version of DataOps includes version control,
tests and CI/CD. It also includes observability and automated runbooks. He also
includes end-to-end versioning of code, models, governance and catalogs
([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
33:47-51:21). Those practices make the lake a recoverable system instead of a
shared folder with more storage.

## Table Formats and Catalogs

Table formats sit between raw object storage and analytical use. Brudaru
explains Iceberg as a table format over files. It gives teams database-like
table behavior without hiding lake storage. He ties that design to Parquet
storage and reduced vendor lock-in.

He then discusses catalogs as the layer that maps data to compute and manages
access. Some catalogs also hold metadata and lineage
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41).

This is why [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }}) and
[Delta Lake]({{ '/wiki/delta-lake/' | relative_url }}) appear in lake
discussions. They don't remove the need for governance or DataOps. They add a
table layer that can make lake data easier to query and version. That layer
can also help teams share data across engines.

Brudaru compares Delta, Hudi and Iceberg later in the same episode. He also
discusses headless table formats and DLT support for Delta Lake and Iceberg
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
30:31 and 49:42).

Start with the requirement, then choose the table and catalog layer. If one
warehouse already serves the consumers, adding a lakehouse table format may add
platform work without enough benefit. Table formats become more important when
multiple engines need shared open storage. They also matter when the team wants
to keep storage independent from a single compute vendor.

## Governance and Ownership

Kwong ties lake quality to ownership and cleanup, so governance makes a lake
usable. Teams need to know which data is stale. They also need to know which
data has an owner. They need to know which data should be removed or ignored
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22-24:24 and 43:02).

Albertsson ties governance to architecture. He places object storage beside
ingress, egress, and self-service SQL. Later, he discusses lineage and
versioning as part of the same platform responsibility
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
23:29-35:57 and 1:04:18-1:07:52).

Bergh turns governance into an operational dependency. When code, data models,
visualizations and governance rules change separately, teams create
handoff risk. His DataOps answer is to automate and version the whole change,
not only the pipeline code
([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
51:21).

These views align with the broader [data governance]({{ '/wiki/data-governance/' | relative_url }})
page because a useful lake needs inventory and classification. It also needs
access controls, lineage, owners and quality signals. The lake stores data,
while governance tells people what the data is, whether they may use it, and
who can fix it.

## Team Boundaries and Tool Selection

A lake's team boundary matters as much as its storage layer. Albertsson is
cautious about decentralizing ownership before teams have a strong sharing
culture and governance model. In his framing, a lake sits inside a platform with
ingestion and workflow engines. It also needs self-service SQL, lineage and
versioning
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-35:57 and 57:46-1:03:02). The same boundary makes
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}) and
[data mesh vs centralized data platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }})
lake questions when ownership moves closer to domain teams.

Brudaru's table-format discussion adds the tool-selection boundary. A team
should name catalog needs and cost before choosing Iceberg, Delta Lake, or
another table layer. It should also name lock-in and interoperability
requirements. His split separates storage and compute from access, metadata and
lineage. That keeps the choice grounded in architecture rather than in the
lakehouse label
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
14:32-23:41 and 44:42-49:42).

Bergh adds the delivery boundary. A lake initiative needs a named consumer and
recovery plan. Storage migration isn't enough. It also needs tests and
observability.

His [DataOps]({{ '/wiki/dataops/' | relative_url }}) view places the lake inside
a larger value stream. Engineers, governance staff, analysts and business users
all participate
([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
28:14-37:13 and 51:21).

## Related Pages

Use [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }}) for the
warehouse side of the storage vocabulary. Use
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
for the architecture tradeoff. Use
[Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }}) and
[Delta Lake]({{ '/wiki/delta-lake/' | relative_url }}) for table-format
choices over lake storage.

Use [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) and
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) for ingestion and
transformation boundaries. Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) for the
operating practices that keep a lake from becoming unused storage.
