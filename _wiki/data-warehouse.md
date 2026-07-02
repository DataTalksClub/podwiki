---
layout: wiki
title: "Data Warehouse"
summary: "Podcast-backed notes on data warehouses as modeled analytical storage for ELT, dbt, BI, governance, cost control, and activation."
related:
  - Data Engineering Platforms
  - Modern Data Stack
  - Data Lake
  - Analytics Engineering
  - Business Intelligence
  - dbt
  - Data Quality and Observability
  - Data Governance
---

A data warehouse is modeled analytical storage. Teams load data from source
systems and model it into trusted tables. Analysts, BI tools, metrics layers,
and sometimes operational systems then consume those tables.

In DataTalks.Club episodes, the warehouse usually sits at the center of the
[[modern data stack]]. Ingestion
gets data in. [[ELT]] and
[[dbt]] model it.
[[Analytics engineering]]
turns repeated analysis into reusable definitions.
[[Business Intelligence]]
then exposes those definitions through dashboards, reports, and recurring
decision workflows.

A warehouse-centered view of the modern data stack contrasts ETL with ELT and
explains why teams may load raw data before transforming it, placing warehouses
beside marts and lakes with orchestration, CDC, and reverse flows on the same
map
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
Joyce Kay Avila's
[[book:20230123-snowflake-definitive-guide|Snowflake: The Definitive Guide]]
covers the same warehouse platform: virtual warehouses, cloud-native scaling,
data sharing, and the SQL modeling layer that dbt and analytics engineering
build on.

Apache Iceberg and catalogs update the warehouse boundary, alongside open table
formats and lakehouse tradeoffs
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

## Modeled Analytical Storage

A warehouse is defined by what teams do with it: it holds business-facing
analytical data, not just copied source tables. Raw records may arrive first.
Analysts and analytics engineers then model customer and order tables, along
with events, funnels, finance facts, and dimensions into tables that people can
reuse.

Loading first gives analysts more flexibility because they can add new warehouse
transformations without asking engineers to rebuild extraction code. Warehouses
and marts differ in scope: warehouses hold the broader analytical layer, while
data marts serve narrower consumption needs
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

Daily analytics engineering work ties data modeling, pipelines, and data quality
together, with Looker and Snowflake in the same tool stack. dbt supplies SQL
transformations, version control, tests, and a DAG
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]]).

The same idea appears in a dbt migration with Looker reporting on a stack of
Redshift, Airflow, Airbyte, and Snowplow
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]]).

## Warehouse and Lakehouse Boundaries

The warehouse can serve as an ELT workbench: once data arrives, SQL users can
cast types, join sources, and build models closer to the business question,
with governance kept in view through data swamps, unused-data ownership, and
cleanup
([[person:nataliekwong|Natalie Kwong]],
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

A contrasting view pushes toward lakehouse architecture, where Apache Iceberg
and Delta Lake are more than storage buzzwords: table formats sit on Parquet,
and catalogs are a separate layer, with metadata, access, and lineage in that
split ([[person:adrianbrudaru|Adrian Brudaru]]). Teams can combine open storage
with warehouse-like behavior and reduce lock-in
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Teams choosing between managed warehouse trust and an open table-format platform
can start with [Data Warehouse vs Data
Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}).

For storage engine internals that sit beneath both warehouses and lakehouses, Alex Petrov's [[book:20210315-database-internals|Database Internals]] Book of the Week covers transaction logs, B-trees, replication, and consensus protocols.

A separate emphasis focuses less on the storage product and more on the modeled
layer that users see. dbt and tests are role-defining tools for analytics
engineers, with documentation, Snowflake, and Looker in the same daily toolset
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]]).
The warehouse is also where product and marketing questions become durable
reporting tables, feeding A/B testing, retention analysis, and RFM analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]]).

A different test applies once the data is modeled: a warehouse hasn't succeeded
just because the tables exist. People still need to find it, trust it,
understand it, and connect it to a decision
([[person:caitlinmoorman|Caitlin Moorman]],
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]).
That turns the warehouse from a storage question into a
[[data product adoption]]
question.

## Warehouse, Lake, Lakehouse, and Marts

Warehouses serve modeled analytics, and marts narrow that modeled layer for a
team or subject area. Lakes and lakehouses keep a different storage boundary.
Warehouses sit near dbt and BI, with marts and reverse flows nearby
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

The same warehouse-centered model applies to product and growth data: teams
collect events, store them, transform them for BI, and send selected data back
to sales, support, or engagement tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]]).

[[data-lake|Data lakes]] preserve broader raw or
semi-structured storage, useful for files, logs, media, and less structured
data. Without governance, a lake turns into a swamp
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

Lakehouses try to add warehouse-like table guarantees to lake storage,
separating storage from table format and separating catalog, compute, and
lineage. Teams get open storage and multiple query engines but still need
reliable tables
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Data marts are narrower than warehouses: consumption layers for a team, subject
area, or use case. In practice, many marts are dbt models or BI-ready tables
inside the warehouse
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

## Warehouse Modeling with ELT, dbt, and BI

Teams using warehouse-centered ELT usually load source data and transform it
with SQL, then test it, document it, and expose it through BI or activation
tools. Those steps run through Airbyte-style extraction and loading into dbt
integration, with orchestration, CDC, and reverse data flows in the same stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

dbt matters because it puts software-engineering habits around SQL models
through transformations, version control, tests, and a DAG, linked to Looker and
Snowflake. Those modeled tables become usable reporting interfaces rather than
hidden SQL files
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]]).

Teams learn warehouse modeling through real migration work: a dbt migration,
wide-versus-narrow table tradeoffs, LookML, Redshift, and product analytics.
Domain knowledge becomes reusable structure, not just runnable queries
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]]).

## Warehouse Cost, Governance, and Reliability

Warehouses concentrate compute and storage, so teams need
[[finops-for-data-engineers|cost discipline]]. BigQuery and dbt are parts of a
digital warehouse, alongside orchestration, monitoring, and tests, and cloud
cost becomes engineering work: tagging, accountability, cost reporting, capacity
planning, vendor negotiation, and reservation choices
([[podcast:finops-for-data-engineers|FinOps for Data Engineers]]). FinOps
practices meet warehouse design in query patterns, partitioning choices,
ownership labels, and review habits.

Governance also keeps the warehouse useful. The data-swamp warning applies to
warehouses as well as lakes: unused tables, unclear ownership, and undocumented
transformations all make trusted analysis harder
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

[[Data Governance]] covers
warehouse ownership and policy decisions, including access and shared
definitions. [Data Quality and
Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
covers freshness and schema checks. It also covers lineage plus tests and
incident signals.

A career example adds implementation detail: data engineering work connecting
SQL reporting, Docker, Airflow, AWS, and data quality checks, plus a BI platform
rebuild that saved money and created a centralized source of truth
([[podcast:get-data-analytics-and-data-engineering-job|Gloria Quiceno's data engineering job episode]]).
This ties warehouse work to practical reliability, not only architecture
diagrams.

## Warehouse Skills in Data Careers

Warehouse literacy shows up in career episodes because many data roles depend
on analytical storage. Core skills for data engineering candidates include
Python, SQL, Docker, Airflow, and data warehouses, along with OLTP versus OLAP,
views and materialized views, and take-home projects
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]]).

SQL modeling is at the center for analytics engineers. Useful warehouse practice
means more than connecting a dashboard: build tables with a clear grain,
document metric definitions, add tests, and explain why a consumer should trust
the model.

Those warehouse habits belong in
[[analytics engineering portfolio projects]]
and the [[analytics engineering roadmap]]
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]];
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]]).

A final hiring signal: a good warehouse practitioner can connect tables to
decisions by asking who uses a model, what decision it supports, whether people
trust it, and how to measure adoption
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]).

## Warehouse Topic Map

Warehouse work in these episodes connects to [data engineering
platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[[modern data stack]], and
[[ETL vs ELT]] choices.
For storage boundaries, compare the warehouse with [data
lakes]({{ '/wiki/data-lake/' | relative_url }}) and [data warehouse vs data
lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}).

The modeled layer connects most directly to [analytics
engineering]({{ '/wiki/analytics-engineering/' | relative_url }}) and
[[dbt]]. [Business
intelligence]({{ '/wiki/business-intelligence/' | relative_url }}) consumes
those modeled warehouse tables. Operating the warehouse connects to [data
quality and
observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [[data governance]]. [FinOps
for data engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
covers the cost side.

After teams publish trusted tables, [data product
adoption]({{ '/wiki/data-product-adoption/' | relative_url }}) and [reverse
ETL]({{ '/wiki/reverse-etl/' | relative_url }}) describe how that data reaches
dashboards and business tools. Those business tools include sales and support
systems.
