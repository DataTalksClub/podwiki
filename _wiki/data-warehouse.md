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

[[person:nataliekwong|Natalie Kwong]] gives the
clearest warehouse-centered explanation in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
She contrasts ETL with ELT. She explains why teams may load raw data before
transforming it. She also places warehouses beside marts and lakes.
Orchestration, CDC, and reverse flows stay in the same map.
Joyce Kay Avila's
[[book:20230123-snowflake-definitive-guide|Snowflake: The Definitive Guide]]
covers the same warehouse platform Kwong references: virtual warehouses,
cloud-native scaling, data sharing, and the SQL modeling layer that dbt and
analytics engineering build on.

[[person:adrianbrudaru|Adrian Brudaru]]
updates the boundary in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]
through Apache Iceberg and catalogs. He also covers open table formats and
lakehouse tradeoffs.

## Modeled Analytical Storage

Guests usually describe a warehouse by what teams do with it. A warehouse holds
business-facing analytical data, not just copied source tables. Raw records may
arrive first. Analysts and analytics engineers then model customer and order
tables. They also model events, funnels, finance facts, and dimensions into
tables that people can reuse.

Kwong makes this practical in her ELT discussion. At 7:57-12:39, she explains
that loading first gives analysts more flexibility because they can add new
warehouse transformations without asking engineers to rebuild extraction code.
At 15:30-18:47, she separates warehouses from marts. Warehouses hold the
broader analytical layer, while data marts serve narrower consumption needs
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

[[person:victoriaperezmola|Victoria Perez Mola]] adds
the modeling layer by tying daily analytics engineering work to data modeling,
pipelines, and data quality. Looker and Snowflake sit in the same tool stack.
She also explains dbt through SQL transformations, version control, and tests.
She describes the DAG too
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]],
4:05-10:04).

[[person:nikolamaksimovic|Nikola Maksimovic]]
shows the same idea through a dbt migration and Looker reporting. His stack uses
Redshift and Airflow. It also uses Airbyte and Snowplow
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]],
18:34-30:28).

## Warehouse and Lakehouse Boundaries

Kwong favors the warehouse as an ELT workbench. Her strongest argument is
autonomy because after data arrives, SQL users can cast types and join sources.
They can also build models closer to the business question. She still keeps
governance in view through data swamps, unused data ownership, and cleanup
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
21:22 and 43:02).

Brudaru pushes the conversation toward lakehouse architecture. In his 2025
trends discussion, Apache Iceberg and Delta Lake aren't just storage buzzwords.
He describes table formats on Parquet and catalogs as separate layers. Metadata,
access, and lineage sit in that split too.

Teams can combine open storage with
warehouse-like behavior and reduce lock-in
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-23:41 and 49:42). Teams choosing between managed warehouse trust and an
open table-format platform can start with [Data Warehouse vs Data
Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}).

For storage engine internals that sit beneath both warehouses and lakehouses, Alex Petrov's [[book:20210315-database-internals|Database Internals]] Book of the Week covers transaction logs, B-trees, replication, and consensus protocols.

Perez Mola and Maksimovic focus less on the storage product and more on the
modeled layer that users see. Perez Mola treats dbt and tests as role-defining
tools for analytics engineers. Documentation and Snowflake sit in the same
daily toolset, along with Looker
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]],
26:10-44:52). Maksimovic treats the warehouse as the place where product and
marketing questions become durable reporting tables. He also connects warehouse
models to A/B testing, retention analysis, and RFM analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]],
14:14-39:36).

[[person:caitlinmoorman|Caitlin Moorman]] adds a
different test: a warehouse hasn't succeeded just because the data is modeled.
People still need to find it and trust it. They also need to understand it and
connect it to a decision
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]],
8:48-26:36). That turns the warehouse from a storage question into a
[[data product adoption]]
question.

## Warehouse, Lake, Lakehouse, and Marts

Warehouses serve modeled analytics, and marts narrow that modeled layer for a
team or subject area. Lakes and lakehouses keep a different storage boundary.
Kwong places warehouses near dbt and BI. She places marts nearby. Reverse flows
sit nearby too.

[[person:arpitchoudhury|Arpit Choudhury]]
uses the same warehouse-centered model for product and growth data. Teams
collect events and store them. They transform them for BI and send selected
data back to sales, support, or engagement tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]],
22:50-41:30).

[[data-lake|Data lakes]] preserve broader raw or
semi-structured storage. Kwong describes lakes as useful for files, logs, and
media. They also hold less structured data. She warns that teams need governance
or the lake turns into a swamp
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
19:50-27:39).

Lakehouses try to add warehouse-like table guarantees to lake storage. Brudaru's
Iceberg discussion separates storage from table format. It also separates
catalog, compute, and lineage. Teams get open storage and multiple query
engines, but still need reliable tables
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-30:31).

Data marts are narrower than warehouses. Kwong describes marts as consumption
layers for a team, subject area, or use case. In practice, many marts are dbt
models or BI-ready tables inside the warehouse
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
15:30-18:47).

## Warehouse Modeling with ELT, dbt, and BI

Teams using warehouse-centered ELT usually load source data and transform it
with SQL. They test it, document it, and expose it through BI or activation
tools. Kwong maps those steps through Airbyte-style extraction and loading. She
also connects them to dbt integration. Orchestration, CDC, and reverse data
flows fit into the same stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
30:59-45:59).

dbt matters because it puts software-engineering habits around SQL models. Perez
Mola explains dbt through transformations, version control, tests, and a DAG.
She also links the work to Looker and Snowflake. Those modeled tables become
usable reporting interfaces rather than hidden SQL files
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]],
6:49-10:04 and 36:44-50:46).

Maksimovic shows how teams learn warehouse modeling through real migration work.
His episode covers a dbt migration and wide-versus-narrow table tradeoffs. It
also covers LookML, Redshift, and product analytics. Teams turn domain knowledge
into reusable structure, not just runnable queries
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]],
18:34-33:46 and 38:27-41:50).

## Warehouse Cost, Governance, and Reliability

Warehouses concentrate compute and storage, so teams need
[[finops-for-data-engineers|cost discipline]].
[[person:eddyzulkifly|Eddy Zulkifly]] frames BigQuery
and dbt as parts of a digital warehouse. Orchestration, monitoring, and tests
belong there too. He then turns cloud cost into engineering work.

Teams need tagging, accountability, and cost reporting. They also need capacity
planning, vendor negotiation, and reservation choices
([[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
21:57-46:17). FinOps practices should meet warehouse design in query patterns
and partitioning choices. Ownership labels and review habits matter too.

Teams also need governance to keep the warehouse useful. Kwong's data-swamp
warning applies to warehouses as well as lakes. Teams make trusted analysis
harder when they keep unused tables. Unclear ownership creates the same
problem. Teams create the same problem when transformations are undocumented
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]],
21:22 and 43:02).

[[Data Governance]] covers
warehouse ownership and policy decisions, including access and shared
definitions. [Data Quality and
Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
covers freshness and schema checks. It also covers lineage plus tests and
incident signals.

[[person:gloriaquiceno|Gloria Quiceno]] gives a career
example with implementation detail. Her episode connects data engineering work
to SQL reporting plus Docker. Airflow appears with AWS, and data quality checks
appear there too.

It also includes a BI platform rebuild. That rebuild saved money and created a
centralized source of truth
([[podcast:get-data-analytics-and-data-engineering-job|Gloria Quiceno's data engineering job episode]],
7:46-21:25 plus 36:20-45:29 and 50:15-53:34). Quiceno ties warehouse work to
practical reliability, not only architecture diagrams.

## Warehouse Skills in Data Careers

Warehouse literacy shows up in career episodes because many data roles depend
on analytical storage. [[person:jeffkatz|Jeff Katz]]
names Python plus SQL among the core skills for data engineering candidates. He
names Docker too. Airflow and data warehouses also matter.

He also brings up OLTP versus OLAP, while views and materialized views appear
too. He also covers take-home projects
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]],
1:20-11:24 and 19:57-23:13).

Perez Mola and Maksimovic put SQL modeling at the center for analytics
engineers. Useful warehouse practice means more than connecting a dashboard.
Build tables with a clear grain. Document metric definitions. Add tests and
explain why a consumer should trust the model.

Those warehouse habits belong in
[[analytics engineering portfolio projects]]
and the [[analytics engineering roadmap]].
Perez Mola covers this at 42:05-50:46 in
[[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]].
Maksimovic covers it at 41:50-45:09 in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]].

Moorman adds the final hiring signal in her last-mile discussion. A good
warehouse practitioner can connect tables to decisions by asking who uses a
model and what decision it supports. They can also ask whether people trust it
and how to measure adoption
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]],
34:00-49:25).

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
