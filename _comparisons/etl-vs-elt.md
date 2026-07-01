---
layout: article
title: "ETL vs ELT"
keyword: "etl vs elt"
secondary_keywords:
  - elt vs etl
  - etl and elt
summary: "A decision guide for choosing transform-before-load or load-before-transform pipelines in modern data stacks."
related_wiki:
  - ETL
  - ELT
  - Modern Data Stack
  - Data Pipelines
  - Analytics Engineering
  - dbt
  - DataOps
  - Reverse ETL
---

ETL and ELT answer one pipeline decision: the team has to choose where
transformation happens. In [ETL]({{ '/wiki/etl/' | relative_url }}), the team
extracts data, transforms it, and loads the prepared result. In
[ELT]({{ '/wiki/elt/' | relative_url }}), the team loads data first. The
transform then happens inside a
[data warehouse]({{ '/wiki/data-warehouse/' | relative_url }}),
[data lake]({{ '/wiki/data-lake/' | relative_url }}), or
[lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }}).

The practical choice is about ownership, risk, and future modeling flexibility.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) defines ETL and
ELT in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}):
ETL organizes source data before loading it at 3:46-6:37. ELT preserves source
detail and moves transformation into warehouse-side SQL and
[dbt]({{ '/wiki/dbt/' | relative_url }}) workflows at 7:57-12:39. That choice
also affects [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and downstream
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}).

## Short Comparison

Use ETL when the destination should receive curated data only. This fits
operational systems and constrained marts. It also fits compliance-heavy
targets where masking, deduplication, or joins must happen before broad
storage.

Use ELT when future modeling flexibility matters more than pre-load control.
This fits warehouse-centered analytics stacks where teams preserve source
detail and write new SQL models later.

The difference changes who can safely change business logic:

- ETL often keeps transformation logic in data engineering, ingestion, or
  platform jobs.
- ELT often moves transformation logic into SQL models owned by analytics
  engineers, analysts, or mixed data teams.
- Both need [DataOps]({{ '/wiki/dataops/' | relative_url }}) practices because
  either path can fail without versioned code, tests, lineage, and ownership.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) makes the
reproducibility risk explicit in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
At 20:12-21:29, he warns that mutable ETL results can differ across runs when
inputs change. At 1:04:18, he ties active datasets to code and versioning, with
lineage as the audit path.

## ETL Fit

Choose ETL when the target shouldn't receive broad raw data. Kwong's customer
acquisition cost example joins CRM data with ad-spend data. The reporting layer
then consumes the prepared result
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
6:37). That's a good fit when the target expects a prepared metric or mart
rather than source-level detail.

ETL also fits when preprocessing reduces risk before storage.
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) describes
ingestion-stage deduplication, ordering guarantees, and PII masking in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10. Those steps change what downstream tables can expose. They may belong
before data reaches a human-facing warehouse or lakehouse layer.

ETL remains useful in large enterprises and complex staging environments.
Kwong says established enterprise workflows and heavy staging needs can keep ETL
relevant
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
41:30).
The right question is whether the transform protects the target or only hides
useful source detail from future modeling work.

## ELT Fit

Choose ELT when questions or source fields change often. Kwong says ELT keeps
source detail available for later transformation work. Analysts and analytics
engineers can add new models when the business question changes
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-12:39). That's why ELT sits close to
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}) and
[dbt]({{ '/wiki/dbt/' | relative_url }}).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) shows
the operating side of ELT in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
At 4:05-10:04, she puts dbt and SQL models inside the analytics engineering
workflow. The same operating context includes tests and DAGs alongside Snowflake
and Looker. ELT works only when the team maintains the warehouse-side transform
like production code.

ELT also fits activation and growth stacks. [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
describes a growth stack that starts with event collection and warehouse
storage. It then adds BI and
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) in his
[Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})
discussion at 22:50-41:30.
In that setup, the modeled warehouse layer has to be trusted because it may
drive support context and sales routing. It may also drive customer messaging or
onboarding.

ELT isn't complete when raw data arrives because Kwong separates raw ingestion
from consumer-facing data marts. She says raw forms usually need cleaning
before business users should rely on them
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
15:30-18:47). ELT still needs governed models, tests, and quality checks. It
also needs documentation and ownership.

## Transformation Boundary

Focus on the transform boundary. ETL makes business meaning durable before or
during the destination load. Kwong's customer acquisition cost example is a
curated result. It combines CRM and advertising data before the business
consumes it
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
6:37).

ELT writes raw or lightly processed records first, and SQL models create
business meaning later. Those models handle joins and type casting. They also
build marts and other warehouse-side modeling work
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
10:00-12:39). Tuli uses a similar split between ingestion or staging and later
modeling. Teams prepare entities and mappings, then prepare marts and
use-case-specific tables in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
32:57-43:05.

That boundary is why ETL often fits curated operational payloads, while ELT
often fits broad analytical reuse. If the transformation defines what the
target is allowed to store or expose, push it earlier. If the transformation is
mostly analytical interpretation, load source detail and model it under review.

## Tool Boundaries

Don't map ETL vs ELT directly to one vendor, because Kwong separates
orchestration from loading and transformation. Airflow schedules jobs, while
Airbyte handles extract-load work and dbt handles warehouse transformations
after data arrives
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-33:45).

Tuli gives the same boundary from a pipeline-authoring view. At 10:48 in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
she contrasts ingestion-focused pipeline authoring with dbt-style modeling.
At 39:23-43:05, she moves from transformation and data modeling into marts and
dashboards. Metrics sit in that same business-facing layer. That split is often
the real ETL-versus-ELT boundary.

The orchestrator doesn't decide the acronym. A pipeline can use Airflow,
Prefect, Dagster, or another scheduler and still be ETL or ELT. The team still
has to decide where business meaning becomes durable and who owns the change
path.

## Ownership And Governance

ETL often keeps transformation close to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}), ingestion,
or platform jobs. ELT often moves repeatable analytical logic into SQL models
owned by analytics engineers, analysts, or mixed data teams. Kwong connects that
shift to analyst autonomy and dbt in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
12:39.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes dbt as SQL transformations with version control and tests. She also
describes scheduled runs and dependency graphs in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
6:49-10:04. [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
adds the organizational reason in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
11:03 and 46:34. He frames analytics engineering as the work of turning messy
business reality into cleaner data systems with software engineering rigor.

ELT shouldn't mean "load everything and sort it out later." Kwong warns that
unmanaged raw zones can become data swamps. She later returns to ownership when
teams collect unused data
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22 and 43:02). That ties ELT to
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data observability]({{ '/wiki/data-observability/' | relative_url }}), and
[GitOps for data teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}),
not only faster modeling.

Albertsson's DataOps rule applies to both designs. Keep active outputs defined
in code and make transformation history traceable
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:04:18). Whether a team says ETL or ELT, unclear lineage creates the same
failure mode. Consumers can't tell which transformation created a dataset, why
it changed, or whether a rerun should reproduce the same result.

## Downstream Activation

The comparison matters more when transformed data leaves analytics and changes
customer-facing work. Choudhury's growth stack moves from collection and
storage to BI. It then moves to reverse ETL and operational analytics tools
such as Census and Hightouch. Grouparoo appears in the same tool category in
[Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
28:52-37:25.

A metric or segment is no longer only a dashboard definition at that point. It
can drive support context, sales routing, engagement campaigns, or onboarding.
Kwong also includes reverse data flows in the modern stack
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
35:42). That makes ELT quality visible outside the warehouse. A warehouse model
that's good enough for exploration may still fail when used for
[data activation]({{ '/wiki/data-activation/' | relative_url }}).

## Decision Checklist

Start from the target and the failure mode.

- Use ETL if the target must receive masked, joined, filtered, or ready-to-use
  data.
- Use ETL if pre-load validation protects compliance, data volume, ordering, or
  operational constraints.
- Use ELT if future business questions require raw source detail and flexible
  SQL modeling.
- Use ELT if analytics engineers or analysts own the transformation layer and
  can maintain tests, docs, and dependencies.
- Use either pipeline choice only with clear ownership, lineage, and quality
  checks.

The interviews give a practical rule: transform early when the target needs
protection. Load first when the team needs future modeling flexibility.
Don't use ELT as a reason to ignore governance. Don't use ETL as a reason to
hide source detail that future teams will need.

## Related Pages

These pages cover the deeper topic nodes behind the decision:

- [ETL]({{ '/wiki/etl/' | relative_url }})
- [ELT]({{ '/wiki/elt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
