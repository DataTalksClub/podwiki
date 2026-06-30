---
layout: wiki
title: "ETL vs ELT"
summary: "A podcast-grounded comparison of transform-before-load and load-before-transform pipeline choices in modern data platforms."
related:
  - ETL
  - ELT
  - Modern Data Stack
  - Data Engineering
  - Data Engineering Platforms
  - Analytics Engineering
  - dbt
  - Reverse ETL
---

## Definition and Scope

ETL means extract, transform, load. The pipeline applies business logic before
the destination system receives the data. ELT means extract, load, transform.
The pipeline loads raw or lightly processed data first, then transforms it in
the warehouse or lakehouse.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) defines the split
in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
at 3:46-7:57. She uses source-specific extraction, business logic, and
destination-specific loading to explain older ETL workflows.

The podcast archive treats ETL vs ELT as a pipeline boundary decision, not a
tool ranking. The same source data can feed [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[data warehouses]({{ '/wiki/data-warehouse/' | relative_url }}), and downstream
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) workflows. The useful
question is where transformation belongs for the consumer, risk, and ownership
model in front of the team.

This comparison sits between [ETL]({{ '/wiki/etl/' | relative_url }})
and [ELT]({{ '/wiki/elt/' | relative_url }}) as standalone topic nodes,
then use [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
for the broader warehouse-centered stack. Use
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
for the storage-platform tradeoff.

## Link Map

Use these pages to place ETL vs ELT inside the archive.

- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) explains
  ingestion and warehouse-side transformation, plus orchestration,
  observability, and activation around ELT workflows.
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) covers the
  end-to-end movement from ingestion through processing and delivery.
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
  and [dbt]({{ '/wiki/dbt/' | relative_url }}) cover the warehouse-side modeling
  work that made ELT practical for analysts and analytics engineers.
- [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
  [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
  cover the code, tests, lineage, and reproducibility practices that keep either
  pipeline maintainable.
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }}),
  [Data Lake]({{ '/wiki/data-lake/' | relative_url }}), and
  [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
  cover where loaded data is written before or after transformation.
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  covers the checks needed when raw, staged, modeled, and activated data can all
  fail in different ways.
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}),
  [Data Activation]({{ '/wiki/data-activation/' | relative_url }}), and
  [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
  cover what happens after modeled warehouse data is sent back to operational
  tools.

These podcast discussions anchor the comparison.

- [ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
  with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) is the main
  comparison episode. It defines ETL at 3:46 and uses customer acquisition cost
  as a transform-before-load example at 6:37. It explains ELT flexibility at
  7:57, connects ELT to dbt and analyst autonomy at 12:39, and returns to ETL's
  continued relevance at 41:30.
- [Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
  with [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
  explains dbt as SQL transformations, version control, tests, and DAGs at
  6:49-10:04.
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})
  with [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
  frames analytics engineering as turning business reality into clean data at
  11:03 and bringing software engineering rigor to workflows at 46:34.
- [Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
  with [Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) distinguishes
  ingestion-focused pipeline authoring from dbt-style modeling at 10:48. It
  then covers staging, preprocessing, modeling, and marts at 32:57-43:05.
- [DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  with [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) adds
  the reproducibility focus. Mutable ETL results can change between runs unless
  the platform keeps immutable inputs and code-defined transformations
  (20:12-21:29 and 1:04:18).
- [Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})
  with [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) shows
  event collection and storage. It also shows warehouse transformation, BI, and
  reverse ETL for activation at 22:50-41:30.

## Common Definition

The archive's shared definition is simple. ETL puts the transform before the
destination, while ELT loads first and makes the warehouse or lakehouse the
place where business-facing models are built. Kwong's Airbyte example starts with the
extract-load layer. It then places dbt-style transformation after data reaches
the warehouse
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:19 and 31:31).

The common decision rule is to load first when future modeling flexibility is
more valuable than pre-load control. Transform first when pre-load control is
the main risk reducer. Kwong's ELT section says loading source detail first
helps when a new source field arrives or business logic changes. The team can
then write a new warehouse transform instead of re-extracting data
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-10:00). Her ETL section still preserves the older approach for cases where
the business logic must prepare the payload before it reaches the destination
(3:46-6:37).

The comparison also has an ownership rule. ETL often keeps more of the work in
data engineering or platform-owned jobs. ELT moves repeatable analytical logic
toward SQL models owned by analytics engineers, analysts, or mixed data teams.
Perez Mola's analytics engineering episode ties that ELT-side work to dbt and
tests. She also places it near DAGs, Snowflake, and Looker
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
4:05-10:04).

Perafan later describes the same discipline as converting messy
business reality into safer data systems
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
11:03-16:25).

## Guest Differences

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the
warehouse-centered ELT case. Her argument favors preserving source detail and
moving transformations closer to analysts. It also favors dbt-style SQL
workflows after ingestion
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-12:39).

She doesn't treat raw loading as a free-for-all. At 17:55-21:22 she separates
raw ingestion from governed marts and warns about data swamps.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) shifts the
discussion from order of operations to reproducibility. His DataOps episode
criticizes mutable warehouse-style ETL because results can differ when the same
process runs at different times. His preferred design uses immutable inputs and
functional transformations. Active datasets are defined in code
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
20:12-21:29 and 1:04:18). That view can support ELT-like raw retention, but the
important line for him is immutability and lineage rather than the acronym.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) focus
on the role boundary created by ELT. Perez Mola treats dbt and Snowflake as
daily analytics engineering tools. Looker, tests, and DAGs sit in the same
workflow
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
6:49-14:34). Perafan is less tool-specific, and his focus is modeling business
reality safely with software engineering rigor
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
11:03 and 46:34).

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) adds a pipeline
authoring view. Her episode contrasts Upsolver and dbt by where they sit.
Upsolver appears near ingestion and execution-engine concerns, while dbt appears
near transformation and analytics engineering
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
10:48 and 24:57). She also names deduplication, ordering guarantees, and PII
masking as pre-load concerns at 37:10. Those are reasons the transform step may
not wait until the warehouse.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) starts from
growth operations rather than pipeline theory. His data-led growth stack needs
event collection and warehouse storage. It also needs dbt/BI analysis plus
activation through operational tools
([Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
22:50-41:30). In that framing, ELT is useful only if the modeled warehouse layer
is trusted enough to drive support and sales. It also has to support engagement
and customer messaging.

## Practical Comparison

Compare the two choices by where meaning is created and who must operate it.

In ETL, business logic runs before or during the load into the destination.
Kwong's customer acquisition cost example joins CRM and ad-spend data before
consumption
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
6:37). In ELT, business logic usually runs after loading in a warehouse or
lakehouse. Kwong connects that work to type casting, joins, SQL modeling, and
dbt at 10:00-12:39.

ETL destinations receive curated payloads, modeled outputs, aggregates, or
destination-specific records. That fits systems that shouldn't receive broad raw
history. ELT destinations receive raw or lightly processed source data first.
Staging and modeled layers come later. Kwong separates raw ingestion from marts
and consumer layers at 15:30-18:47 in the same episode.

ETL ownership often sits with data engineering or platform teams when the
transform is part of ingestion, compliance, or operational delivery. ELT
ownership often moves toward analytics engineers or analysts when the transform
is SQL modeling, metrics, marts, and BI-ready data. Perez Mola describes that
analytics engineering workflow at 4:05-10:04 in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).

ETL's advantage is control before storage or delivery. It can reduce volume,
protect fields, normalize records, and meet destination constraints.
Tuli's ingestion section names deduplication, ordering guarantees, and PII
masking as pre-load concerns
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10).

ELT's advantage is flexibility after storage. It preserves source detail,
supports remodeling without re-extraction, and lets SQL users iterate on
business definitions. Kwong makes that case at 7:57-12:39.

The failure modes differ because ETL can hide transformation logic in jobs that
are hard to reproduce when inputs change between runs. Albertsson's DataOps
discussion makes that risk explicit at 20:12-21:29 in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
ELT can create untrusted raw zones if ownership and tests don't follow.
Documentation, cleanup, and governance have to follow too. Kwong warns about
data swamps at 21:22 and unused data ownership at 43:02.

## ETL Fit

Use ETL when the destination should only receive data that has already been
filtered or prepared. It also fits data that must be masked or joined first.
Kwong's ETL definition includes
source-specific extraction and organization-specific business logic before
destination-specific loading
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:46-6:37). That makes ETL a good fit when the target is an operational system
or a constrained data mart. It also fits legacy reporting workflows that expect
curated tables rather than broad raw source copies.

ETL also fits when preprocessing has pipeline-level semantics. Tuli's
discussion of ingestion preprocessing includes deduplication, ordering
guarantees, and PII masking
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10). Those aren't merely dashboard choices. They affect whether downstream
storage is allowed to contain sensitive fields, duplicates, or incorrectly
ordered events. In those cases, a transform-before-load step reduces risk before
more consumers see the data.

ETL remains relevant in large enterprises and complex staging environments.
Kwong says that older ETL workflows continue to appear when companies have
established workflows. Heavy staging needs also keep ETL relevant
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
41:30).

Albertsson's warning adds a condition. If those ETL jobs mutate shared
tables or depend on changing source state, the team needs reproducibility. It
also needs versioning and lineage controls
([DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
20:12-21:29 and 1:04:18).

## ELT Fit

Use ELT when changing analytical logic is the bottleneck. Source-detail
preservation lets teams write new transformations later when business logic or
source fields change
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-10:00). This matches [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
work because the transform becomes a maintained model rather than a one-off
pipeline script.

ELT fits warehouse-centered analytics stacks. Kwong places Airbyte-style loading
and dbt in the same modern stack. Warehouses and orchestration sit in that stack
too, along with reverse flows
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
31:31-35:42).

Choudhury's growth-stack episode shows the business version. Event collection
and storage come before warehouse dbt models support BI analysis. The same
warehouse layer supports segments and activation
([Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
22:50-37:25).

ELT isn't complete when raw data arrives. Perez Mola's dbt workflow adds version
control, tests, and a DAG to SQL transformations
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
6:49-10:04). Perafan's episode adds the reason those practices matter. The work
turns messy business reality into a safer data system. Later sections call for
software engineering rigor around data workflows
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
11:03 and 46:34).

## Ownership and Governance

The ETL vs ELT decision changes who can safely change business logic. In an ETL
flow, the transform may be tied to connector code, orchestration, or platform
jobs. In an ELT flow, the transform often becomes a SQL model in the warehouse.

Kwong connects that shift to analyst autonomy and dbt at 12:39. Perez Mola
connects the analytics engineer role to modeling and pipelines. She also
connects it to quality and Looker at 4:05
([modern stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[analytics engineering episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

The archive doesn't support "load everything and sort it out later" as a good
ELT rule. Kwong separates raw ingestion layers from marts and consumer-facing
tables at 15:30-18:47. She also warns about governance and data swamp risk at
21:22, then returns to ownership and cleanup at 43:02.

That connects ELT to
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[data observability]({{ '/wiki/data-observability/' | relative_url }}). It also
connects ELT to
[data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
not only faster modeling.

Albertsson's DataOps view adds a stricter operating rule. Keep active outputs
defined in code and make transformation history traceable
([DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:04:18). Whether the team says ETL or ELT, unclear lineage creates the same
failure mode. Consumers can't tell which transformation created a dataset. They
also can't tell why it changed or whether a rerun should reproduce the same
result.

## Downstream Activation

The comparison matters more when transformed data leaves analytics and changes
customer-facing work. Choudhury's data-led growth stack moves from collection
and storage to BI. It then moves to reverse ETL and operational analytics tools
such as Census, Hightouch, and Grouparoo
([Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
28:52-37:25). At that point, a metric or segment isn't only a dashboard
definition. It may drive support context, sales routing, engagement campaigns,
or onboarding.

Kwong also includes reverse data flows in the modern stack at 35:42
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
That makes ELT quality visible outside the warehouse. A warehouse transform that
is good enough for exploration may not be good enough for
[data activation]({{ '/wiki/data-activation/' | relative_url }}).

Before a team syncs modeled data into operational tools, the modeled layer needs
tests and ownership. It also needs documentation and a clear refresh path.

## Related Pages

Use these pages for the adjacent platform, modeling, and activation topics.

- [ETL]({{ '/wiki/etl/' | relative_url }})
- [ELT]({{ '/wiki/elt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
