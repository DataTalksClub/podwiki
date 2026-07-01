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

In the DataTalks.Club archive, the warehouse usually sits at the center of the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). Ingestion
gets data in. [ELT]({{ '/wiki/elt/' | relative_url }}) and
[dbt]({{ '/wiki/dbt/' | relative_url }}) model it.
[Analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
turns repeated analysis into reusable definitions.
[Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
then exposes those definitions through dashboards, reports, and recurring
decision workflows.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the
clearest warehouse-centered explanation in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
She contrasts ETL with ELT. She explains why teams may load raw data before
transforming it. She also places warehouses beside marts and lakes.
Orchestration, CDC, and reverse flows stay in the same map.

[Adrian
Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
updates the boundary in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
through Apache Iceberg and catalogs. He also covers open table formats and
lakehouse tradeoffs.

## Starting Points

Use these archive paths to place the warehouse in context:

- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) for the
  stack around warehouse analytics.
- [ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }}) for the load-first
  versus transform-first tradeoff.
- [Data Lake]({{ '/wiki/data-lake/' | relative_url }}) and
  [Data Warehouse vs Data Lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }})
  for storage boundaries.
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
  and [dbt]({{ '/wiki/dbt/' | relative_url }}) for warehouse-side modeling,
  tests, documentation, and BI-facing tables.
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  and [Data Observability for Data Engineering]({{ '/guides/data-observability-for-data-engineering/' | relative_url }})
  for freshness, schema, lineage, and trust.
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) for
  ownership, access, and policy.
- [FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
  for warehouse cost ownership, tagging, reservations, and spend reporting.
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
  and [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) for what happens
  after modeled warehouse data reaches dashboards or business tools.

Core podcast discussions:

- [ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
  with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
- [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
  with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
- [Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
  with [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})
  with [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
- [Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
  with [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
- [Gloria Quiceno's data engineering job episode]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }})
  with [Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }})
- [FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }})
  with [Eddy Zulkifly]({{ '/people/eddyzulkifly/' | relative_url }})
- [Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
  with [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})

## Common Definition

Guests usually describe a warehouse by what teams do with it. A warehouse holds
business-facing analytical data, not just copied source tables. Raw records may
arrive first. Analysts and analytics engineers then model customer and order
tables. They also model events, funnels, finance facts, and dimensions into
tables that people can reuse.

Kwong's ELT discussion makes this practical. At 7:57-12:39, she explains that
loading first gives analysts more flexibility because they can add new
warehouse transformations without asking engineers to rebuild extraction code.
At 15:30-18:47, she separates warehouses from marts. Warehouses hold the
broader analytical layer, while data marts serve narrower consumption needs
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

The analytics engineering episodes add the modeling layer. [Victoria Perez
Mola]({{ '/people/victoriaperezmola/' | relative_url }}) ties daily analytics
engineering work to data modeling, pipelines, and data quality. Looker and
Snowflake sit in the same toolstack. She also explains dbt through SQL
transformations, version control, and tests. She describes the DAG too
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
4:05-10:04).

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
shows the same idea through a dbt migration and Looker reporting. His stack uses
Redshift and Airflow. It also uses Airbyte and Snowplow
([From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
18:34-30:28).

## Guest Differences

Kwong favors the warehouse as an ELT workbench. Her strongest argument is
autonomy because after data arrives, SQL users can cast types and join sources.
They can also build models closer to the business question. She still keeps
governance in view through data swamps, unused data ownership, and cleanup
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22 and 43:02).

Brudaru pushes the conversation toward lakehouse architecture. In his 2025
trends discussion, Apache Iceberg and Delta Lake aren't just storage buzzwords.
He describes table formats on Parquet and catalogs as separate layers. Metadata,
access, and lineage sit in that split too.

Teams can combine open storage with
warehouse-like behavior and reduce lock-in
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41 and 49:42). Use
[Data Warehouse vs Data Lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }})
when the question is whether trust should live in a managed warehouse or in an
open table-format platform.

Perez Mola and Maksimovic focus less on the storage product and more on the
modeled layer that users see. Perez Mola treats dbt and tests as role-defining
tools for analytics engineers. Documentation and Snowflake sit in the same
daily toolset, along with Looker
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
26:10-44:52). Maksimovic treats the warehouse as the place where product and
marketing questions become durable reporting tables. He also connects warehouse
models to A/B testing, retention analysis, and RFM analysis
([From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
14:14-39:36).

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) adds a
different test: a warehouse hasn't succeeded just because the data is modeled.
People still need to find it and trust it. They also need to understand it and
connect it to a decision
([Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}),
8:48-26:36). That turns the warehouse from a storage question into a
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
question.

## Warehouse, Lake, Lakehouse, and Marts

Warehouses serve modeled analytics, and marts narrow that modeled layer for a
team or subject area. Lakes and lakehouses keep a different storage boundary.
Kwong places warehouses near dbt and BI. She places marts nearby. Reverse flows
sit nearby too.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
uses the same warehouse-centered model for product and growth data. Teams
collect events and store them. They transform them for BI and send selected
data back to sales, support, or engagement tools
([Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
22:50-41:30).

[Data lakes]({{ '/wiki/data-lake/' | relative_url }}) preserve broader raw or
semi-structured storage. Kwong describes lakes as useful for files, logs, and
media. They also hold less structured data. She warns that teams need governance
or the lake turns into a swamp
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
19:50-27:39).

Lakehouses try to add warehouse-like table guarantees to lake storage. Brudaru's
Iceberg discussion separates storage from table format. It also separates
catalog, compute, and lineage. Teams get open storage and multiple query
engines, but still need reliable tables
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-30:31).

Data marts are narrower than warehouses. Kwong describes marts as consumption
layers for a team, subject area, or use case. In practice, many marts are dbt
models or BI-ready tables inside the warehouse
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
15:30-18:47).

## ELT, dbt, and BI

Teams using warehouse-centered ELT usually load source data and transform it
with SQL. They test it, document it, and expose it through BI or activation
tools. Kwong maps those steps through Airbyte-style extraction and loading. She
also connects them to dbt integration. Orchestration, CDC, and reverse data
flows fit into the same stack
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-45:59).

dbt matters because it puts software-engineering habits around SQL models. Perez
Mola explains dbt through transformations, version control, tests, and a DAG.
She also links the work to Looker and Snowflake. Those modeled tables become usable
reporting interfaces rather than hidden SQL files
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
6:49-10:04 and 36:44-50:46).

Maksimovic shows how teams learn warehouse modeling through real migration work.
His episode covers a dbt migration and wide-versus-narrow table tradeoffs. It
also covers LookML, Redshift, and product analytics. Teams turn domain knowledge
into reusable structure, not just runnable queries
([From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
18:34-33:46 and 38:27-41:50).

## Cost, Governance, and Reliability

Warehouses concentrate compute and storage, so teams need
[cost discipline]({{ '/wiki/finops-for-data-engineers/' | relative_url }}).
[Eddy Zulkifly]({{ '/people/eddyzulkifly/' | relative_url }}) frames BigQuery
and dbt as parts of a digital warehouse. Orchestration, monitoring, and tests
belong there too. He then turns cloud cost into engineering work.

Teams need tagging, accountability, and cost reporting. They also need capacity
planning, vendor negotiation, and reservation choices
([FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
21:57-46:17). FinOps practices should meet warehouse design in query patterns
and partitioning choices. Ownership labels and review habits matter too.

Teams also need governance to keep the warehouse useful. Kwong's data-swamp
warning applies to warehouses as well as lakes. Teams make trusted analysis
harder when they keep unused tables. Unclear ownership creates the same
problem. Teams create the same problem when transformations are undocumented
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22 and 43:02).

Use
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) for ownership,
access, definitions, and policy. Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
for freshness, schema, and lineage. Use the same page for tests and incident
signals.

[Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }}) gives a career
example with implementation detail. Her episode connects data engineering work
to SQL reporting plus Docker. Airflow appears with AWS, and data quality checks
appear there too.

It also includes a BI platform rebuild. That rebuild saved money and created a
centralized source of truth
([Gloria Quiceno's data engineering job episode]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}),
7:46-21:25 plus 36:20-45:29 and 50:15-53:34). Her story ties warehouse work to
practical reliability, not only architecture diagrams.

## Learning and Hiring Signals

Warehouse literacy shows up in career episodes because many data roles depend
on analytical storage. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
names Python plus SQL among the core skills for data engineering candidates. He
names Docker too. Airflow and data warehouses also matter.

He also brings up OLTP versus OLAP, while views and materialized views appear
too. The same interview covers take-home projects
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-11:24 and 19:57-23:13).

Perez Mola and Maksimovic put SQL modeling at the center for analytics
engineers. Useful warehouse practice means more than connecting a dashboard.
Build tables with a clear grain. Document metric definitions. Add tests and
explain why a consumer should trust the model.

These habits link warehouse skills to
[analytics engineering portfolio projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
and to the [analytics engineering roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).
Perez Mola covers this at 42:05-50:46 in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
Maksimovic covers it at 41:50-45:09 in
[From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).

Moorman's last-mile discussion adds the final hiring signal. A good warehouse
practitioner can connect tables to decisions by asking who uses a model and what
decision it supports. They can also ask whether people trust it and how to
measure adoption
([Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}),
34:00-49:25).
