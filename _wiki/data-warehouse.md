---
layout: wiki
title: "Data Warehouse"
summary: "Data warehouses as modeled analytical storage for ELT, dbt, BI, governance, cost control, and activation."
related:
  - Data Engineer Roadmap
  - Data Engineering Platforms
  - Modern Data Stack
  - Data Lake
  - Data Warehouse vs Data Lakehouse
  - Analytics Engineering
  - Business Intelligence
  - dbt
  - Data Quality and Observability
  - Data Governance
---

A data warehouse is modeled analytical storage. Teams load data from source
systems and model it into trusted tables. Analysts, BI tools, metrics layers,
and sometimes operational systems then consume those tables.

The warehouse usually sits at the center of the
[[modern data stack]]. Ingestion
gets data in. [[ELT]] and
[[dbt]] model it.
[[Analytics engineering]]
turns repeated analysis into reusable definitions.
[[Business Intelligence]]
then exposes those definitions through dashboards, reports, and recurring
decision workflows.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

A warehouse-centered view of the modern data stack contrasts ETL with ELT.
Teams may load raw data before transforming it. The same map places warehouses
beside marts and lakes. Reverse flows sit nearby.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
Joyce Kay Avila's
[[book:20230123-snowflake-definitive-guide=>Snowflake: The Definitive Guide]]
covers the same warehouse platform. The book explains virtual warehouses,
cloud-native scaling, data sharing, and the SQL modeling layer that dbt and
analytics engineering build on.

[[apache-iceberg=>Apache Iceberg]] and catalogs update the warehouse boundary,
alongside open table formats and lakehouse
tradeoffs.[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]

## Modeled Warehouse Layer

A warehouse is defined by what teams do with it. It holds business-facing
analytical data, not just copied source tables. Raw records may arrive first.
Analysts and analytics engineers then model customer and order tables. They also
model events, funnels, finance facts, and dimensions into tables that people can
reuse.

The [[data-architect-role=>data architect]] role adds discovery before the
modeling step. Stakeholders may ask for margin by region. The architect
identifies the metrics, then designs dimension and fact tables. Departments can
then share one model on top of the same underlying data.[[cite:from-iot-data-engineering-to-leading-data-architect=>From IoT Data Engineering to Leading Data Architect]]

That makes dimensional modeling a stakeholder-discovery practice, not only a
schema style. A request such as regional margin hides a metric, a geography
dimension, a time dimension, and a grain decision. The warehouse model becomes
more valuable when those choices support several departments instead of one
dashboard.[[cite:from-iot-data-engineering-to-leading-data-architect@32:58=>From IoT Data Engineering to Leading Data Architect]]

Loading first gives analysts more flexibility. They can add new warehouse
transformations without asking engineers to rebuild extraction code. Warehouses
and marts differ in scope. Warehouses hold the broader analytical layer, while
data marts serve narrower consumption needs.[[cite:data-engineering-tools-modern-data-stack@15:30=>ETL vs ELT and the Modern Data Stack]]

Tammy Liang's e-commerce team needed a warehouse for demand forecasting.
Historical sales had to be stored before the team could build and deliver
models. Forecasting still required business teams to
provide product details, promotions, and plans. Here the team joined warehouse
history with [[machine-learning-for-business=>forecasting models]] and business
inputs.[[cite:building-and-scaling-data-team@12:10=>Building and Scaling a Data Team]]
[[cite:building-and-scaling-data-team@17:11=>Building and Scaling a Data Team]]

Kwong describes this as layers inside or around the warehouse. A raw ingestion
database receives source data. A shared layer can feed several teams. Marts
serve marketing, sales, finance, or product consumers. Teams use the mart as
the trusted consumption table, not the raw landing zone
[[cite:data-engineering-tools-modern-data-stack@15:30=>ETL vs ELT and the Modern Data Stack]].

Daily analytics engineering work ties data modeling, pipelines, and data quality
together. Looker and Snowflake sit in the same tool stack. dbt supplies SQL
transformations, version control, tests, and a DAG.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

The same idea appears in a dbt migration with Looker reporting on a stack of
Redshift, Airflow, Airbyte, and Snowplow.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

## Warehouse Boundary Tradeoffs

The warehouse can serve as an ELT workbench. Once data arrives, SQL users can
cast types, join sources, and build models closer to the business question.
Governance still matters because unused data, unclear ownership, and weak
cleanup habits can turn storage into a swamp.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

Some teams push toward lakehouse architecture. [[apache-iceberg=>Apache
Iceberg]] and [[delta-lake=>Delta Lake]] are more than storage buzzwords. Table formats sit on
Parquet. Catalogs handle metadata, access, and lineage in that split.

Teams can combine open storage with warehouse-like behavior and reduce
lock-in.[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
For the architecture boundary, start with [[Data Warehouse vs Data Lakehouse]].
For the table-format choice, use
[[delta-lake-vs-apache-iceberg=>Delta Lake vs Apache Iceberg]]. For the broader
shift toward open formats and catalogs, use
[[modern-data-engineering-trends=>modern data engineering trends]]. Use the same
trend frame for multiple engines and cost-aware platform choices.

Storage engine internals sit beneath both warehouses and lakehouses. Alex
Petrov's [[book:20210315-database-internals=>Database Internals]] Book of the Week
covers transaction logs, B-trees, replication, and consensus protocols.

Other discussions focus on the modeled layer that users see. dbt and tests are
role-defining tools for analytics engineers. Snowflake and Looker are daily
tools.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]
The warehouse is also where product and marketing questions become durable
reporting tables. Those tables feed A/B testing, retention analysis, and RFM
analysis.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

After teams model data, the warehouse still has to prove its value. People need
to find the warehouse, trust it, and understand it. They also need to connect it
to a decision.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]
That turns the warehouse from a storage question into a
[[data product adoption]]
question.

## Warehouse, Lake, Lakehouse, and Marts

Warehouses serve modeled analytics, and marts narrow that modeled layer for a
team or subject area. Lakes and lakehouses keep a different storage boundary.
Warehouses sit near dbt and BI, with marts and reverse flows nearby.[[cite:data-engineering-tools-modern-data-stack@15:30=>ETL vs ELT and the Modern Data Stack]]

The same warehouse-centered model applies to product and growth data. Teams
collect events and store them. They transform the events for BI and send
selected data back to sales, support, or engagement tools.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]]

[[data-lake=>Data lakes]] preserve broader raw or
semi-structured storage for files, logs, media, and less structured data.
Without governance, a lake turns into a swamp.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

Warehouse and lake categories can converge, but the consumer still matters.
Analytics teams often live in the warehouse. Engineering teams may need a lake
for application data and flexible files
[[cite:data-engineering-tools-modern-data-stack@24:24=>ETL vs ELT and the Modern Data Stack]].

Lakehouses try to add warehouse-like table guarantees to lake storage. They
separate storage from table format. They also separate the catalog from compute
and lineage. Teams get open storage and multiple query engines but still need
reliable tables.[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]

Data marts are narrower than warehouses and serve as consumption layers for a
team, subject area, or use case. In practice, many marts are dbt models or
BI-ready tables inside the warehouse.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
That distinction matters for trust. Business users shouldn't have to pull
metrics directly from raw ingestion tables because each user may clean or join
the data differently. The mart layer gives them a shared definition with enough
guardrails to use the metric consistently
[[cite:data-engineering-tools-modern-data-stack@17:55=>ETL vs ELT and the Modern Data Stack]].

## Warehouse Modeling with ELT, dbt, and BI

Teams using warehouse-centered ELT usually load source data and transform it
with SQL. Then they test it, document it, and expose it through BI or activation
tools. The stack connects Airbyte-style extraction and loading to dbt
integration. It also includes orchestration, CDC, and reverse data flows.[[cite:data-engineering-tools-modern-data-stack@30:59=>ETL vs ELT and the Modern Data Stack]]
[[cite:data-engineering-tools-modern-data-stack@33:45=>ETL vs ELT and the Modern Data Stack]]

dbt matters because it puts software-engineering habits around SQL models
through transformations, version control, tests, and a DAG. Looker and Snowflake
connect to that modeled layer. Those modeled tables become usable reporting
interfaces rather than hidden SQL files.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

Teams learn warehouse modeling through real migration work. The episode covers a
dbt migration and wide-versus-narrow table tradeoffs. It also covers LookML,
Redshift, and product analytics. Domain knowledge becomes reusable structure,
not just runnable queries.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

## Warehouse Cost, Governance, and Reliability

Warehouses concentrate compute and storage, so teams need
[[finops-for-data-engineers=>cost discipline]]. BigQuery and dbt are parts of a
digital warehouse, alongside orchestration, monitoring, and tests. Cloud cost
becomes engineering work. Teams tag spend and assign accountability. They also
report costs, plan capacity, negotiate with vendors, and choose reservations.[[cite:finops-for-data-engineers=>FinOps for Data Engineers]]

FinOps practices meet warehouse design in query patterns, partitioning choices,
ownership labels, and review habits.

Governance also keeps the warehouse useful. The data-swamp warning applies to
warehouses as well as lakes. Teams make trusted analysis harder when they leave
tables unused, ownership unclear, and transformations undocumented.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

[[Data Governance]] covers
warehouse ownership and policy decisions, including access and shared
definitions. [[Data Quality and Observability]]
covers freshness and schema checks. It also covers lineage plus tests and
incident signals.

Career episodes connect SQL reporting and Docker to data engineering practice.
They also include Airflow, AWS, and data quality checks. A BI platform rebuild
saved money. It also created a centralized source of truth.[[cite:get-data-analytics-and-data-engineering-job=>Gloria Quiceno's data engineering job]]
This ties warehouse work to practical reliability, not only architecture
diagrams.

## Warehouse Skills in Data Careers

Warehouse literacy shows up in career episodes because many data roles depend
on analytical storage. Data engineering candidates need Python and SQL. They
also need Docker, Airflow, and data warehouse practice. Warehouse concepts
include OLTP versus OLAP, views, and materialized views. Take-home projects can
test those concepts.[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]

Jeff Katz names OLTP versus OLAP modeling as fair game for data engineering
interviews. He pairs that with medium SQL practice. That makes warehouse
modeling part of the [[data-engineer-roadmap=>data engineer roadmap]], not only
a BI topic
[[cite:data-engineering-career-path-and-skills@45:14=>Build a Data Engineering Career]].

SQL modeling is at the center for analytics engineers, and useful warehouse
practice means more than connecting a dashboard. Teams build tables with a clear
grain, document metric definitions, add tests, and explain why a consumer should
trust the model.

Those warehouse habits belong in
[[analytics engineering portfolio projects]] and the
[[analytics engineering roadmap]]. The same work combines SQL modeling, BI
usage, and domain knowledge. Analytics engineering roles use the warehouse as
the place where those skills meet.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]][[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

A final hiring signal is whether a good warehouse practitioner can connect
tables to decisions. They ask who uses a model, what decision it supports,
whether people trust it, and how to measure adoption.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

## Related Pages

Warehouse work connects to these adjacent Podwiki pages:

- [[Data Engineering Platforms]],
  [[modern data stack]], and [[ETL vs ELT]] cover the platform choices around a
  warehouse.
- [[Data Lake]] and [[Data Warehouse vs Data Lakehouse]]
  cover the storage-boundary tradeoffs.
- [[Analytics Engineering]],
  [[dbt]], and [[Business Intelligence]]
  cover the modeled layer that people query.
- [[Data Quality and Observability]],
  [[data governance]], and [[FinOps for Data Engineers]]
  cover operations, trust, and cost control.
- [[Data Product Adoption]]
  and [[Reverse ETL]] cover how
  warehouse data reaches dashboards and business tools.
