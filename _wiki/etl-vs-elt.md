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

ETL means extract, transform, load. The pipeline extracts data from a source,
applies transformation logic, and then loads the prepared result into a
destination. ELT means extract, load, transform. The pipeline loads raw or
lightly processed data first, then transforms it in a
[data warehouse]({{ '/wiki/data-warehouse/' | relative_url }}),
[data lake]({{ '/wiki/data-lake/' | relative_url }}), or
[lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }})
layer.

The DataTalks.Club archive treats ETL vs ELT as a boundary decision inside
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), not as a
simple ranking of tools. In
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) defines ETL at
3:46-6:37. She then explains ELT at 7:57-12:39 as a way to preserve source
detail and move transformation into warehouse-side SQL and dbt workflows. The
same choice affects the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}).
It also affects [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and downstream
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}).

Use the standalone [ETL]({{ '/wiki/etl/' | relative_url }}) and
[ELT]({{ '/wiki/elt/' | relative_url }}) pages for narrower definitions. Use
the shorter [ETL vs ELT decision guide]({{ '/comparisons/etl-vs-elt/' | relative_url }})
when the task is a practical selection checklist rather than an archive-wide
wiki comparison.

## Common Definition

Across the archive, the comparison turns on the transformation step. ETL
transforms before the destination receives the data. ELT loads first. The
warehouse, lakehouse, or downstream modeling layer then becomes the place where
business-facing tables are built.

Kwong's Airbyte explanation places Airbyte in
the extract-load layer. dbt sits in the transform layer after data arrives in
the warehouse
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:19 and 31:31).

Load first when later modeling flexibility matters more than pre-load control.
Kwong says ELT helps when a source field
arrives later or business logic changes. The team can write a new warehouse
transform instead. That avoids re-extracting data
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-10:00).

Transform first when the destination should receive only prepared data. That
includes filtered or joined data. Kwong's example is customer acquisition cost.
It joins CRM and ad spend before consumption in a traditional ETL-style mart
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
6:37).

The archive also gives ETL vs ELT an ownership meaning. ETL often keeps
transformation close to [data engineering]({{ '/wiki/data-engineering/' | relative_url }})
or platform-owned ingestion jobs. ELT moves repeatable analytical logic toward
SQL models owned by analytics engineers, analysts, or mixed data teams.
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes dbt as SQL transformations with version control and tests. She also
describes the DAG that dbt builds in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
at 6:49-10:04.

## Guest Differences

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) makes the
warehouse-centered ELT case. She favors preserving source detail and moving
business logic closer to analysts. She also favors dbt-style SQL after ingestion
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-12:39).

She doesn't present raw loading as enough on its own. The same episode
separates raw ingestion from governed marts at 15:30-18:47. It also warns about
data swamps at 21:22.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) shifts the
discussion from acronym order to reproducibility. In
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he criticizes mutable ETL-style warehouse workflows because results can change
when the same process runs at different times. His preferred design is
immutable inputs, functional transformations, and active datasets defined in
code (20:12-21:29 and 1:04:18). That view can support ELT-like raw retention,
but the deeper requirement is traceable lineage rather than the label.

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) draws the boundary
around pipeline authoring and ingestion guarantees. In
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
she contrasts Upsolver and dbt by where they sit. Upsolver focuses on
ingestion, execution, and lake flow. dbt delegates execution to the warehouse
and fits the modeling layer (10:48 and 24:57).

She also names deduplication, ordering guarantees, and PII masking as
ingestion-stage concerns at 37:10. Those are reasons some transformations can't
wait until the warehouse.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
focuses on the role boundary ELT creates. She treats dbt and Snowflake as daily
analytics engineering tools. Looker and tests sit in the same workflow, as do
DAGs
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
4:05-14:34).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
is less tool-specific. His
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})
episode frames analytics engineering as turning business reality into clean
data. It also brings software engineering rigor to data workflows (11:03 and
46:34).

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) starts from
growth operations rather than pipeline architecture. In
[Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
event collection plus warehouse storage support dbt and BI analysis. Reverse ETL
then sends modeled segments into operational systems (22:50-41:30). In that
view, ELT matters only if the modeled warehouse layer is trusted enough to drive
support and sales. It also has to support engagement and customer messaging.

## Transformation Boundary

Meaning is the practical ETL vs ELT question. For ETL, business logic runs
before load or during the destination load. Kwong uses customer acquisition cost
as the example. It combines CRM and advertising data into a curated result
before the business consumes it
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
6:37).

In ELT, the raw or lightly processed records land first. SQL models
create business meaning later in the warehouse. Joins, type casting, and marts
are part of that work
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
10:00-12:39).

That boundary is why ETL often fits curated operational payloads. ELT often
fits broad analytical reuse. Tuli's pipeline
episode uses a similar split between ingestion or staging and the later
transformation or modeling phase. In that later phase, teams prepare entities
and mappings. They also prepare marts and use-case-specific tables
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
32:57-43:05).

## Raw, Staged, And Modeled Layers

ELT doesn't mean business users should query raw dumps. Kwong describes the
raw Airbyte-style ingestion layer as separate from data marts and consumer
tables. She says raw forms usually require cleaning before business users should
use them
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
15:30-18:47). This connects ELT to [dbt]({{ '/wiki/dbt/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
and [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
The loaded data still needs governed models, tests, documentation, and clear
ownership.

ETL pushes more of that preparation before the main destination. That's useful
when the pipeline must reduce volume or normalize records. It's also useful
when sensitive fields need protection before more systems can see the data.
Tuli's ingestion discussion names deduplication and ordering guarantees as
staging concerns. PII masking can also happen at the ingestion stage rather than
later in a BI mart
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10).

## Ownership, Governance, And Reproducibility

The ETL vs ELT decision changes who can safely change business logic. In ETL,
the transform may be tied to connector code or orchestration. It may also sit in
platform jobs or a destination-specific integration. In ELT, the transform often
becomes a reviewed SQL model in the warehouse. Kwong links that shift to analyst
autonomy and dbt
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
12:39).

Perez Mola describes analytics engineers working with modeling and pipelines.
She also places data quality and Looker in that role
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
4:05).

The archive doesn't support "load everything and sort it out later" as a good
ELT rule. Kwong warns that unmanaged raw zones can become data swamps. She later
returns to ownership and cleanup when data teams collect unused data
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
21:22 and 43:02). That connects ELT to
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data observability]({{ '/wiki/data-observability/' | relative_url }}), and
[GitOps for data teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}),
not only faster modeling.

Albertsson's DataOps episode adds a stricter operating rule for both designs.
Keep active outputs defined in code and make transformation history traceable
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:04:18). Whether a team says ETL or ELT, unclear lineage creates the same
failure mode. Consumers can't tell which transformation created a dataset, why
it changed, or whether a rerun should reproduce the same result.

## ETL Fit

ETL fits when the destination should receive only data that has already been
filtered, joined, masked, or conformed to a target schema. Kwong's ETL
definition includes source-specific extraction, organization-specific business
logic, and destination-specific loading
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:46-6:37). That makes ETL suitable for operational systems, constrained marts,
and legacy reporting workflows that expect curated tables rather than broad raw
source copies.

ETL also fits when preprocessing has pipeline-level semantics. Deduplication,
ordering guarantees, and PII masking affect downstream storage because they
define what storage is allowed to contain. They aren't just dashboard metric
choices
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10). Kwong also says ETL remains relevant in large enterprises with
established workflows and complex staging needs
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
41:30).

## ELT Fit

ELT fits when changing analytical logic is the bottleneck. Loading source detail
lets teams write new transformations later when business logic or source fields
change
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-10:00). That matches analytics engineering work because the transform
becomes a maintained model instead of a one-off pipeline script.

ELT also fits warehouse-centered modern stacks. Kwong places Airbyte-style
loading and dbt in the same stack. Warehouses, orchestration, and reverse flows
sit around them
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
31:31-35:42).

In Choudhury's growth-stack episode, event collection and storage precede
warehouse transformations. BI analysis and activation through reverse ETL follow
([Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
22:50-37:25).

ELT isn't complete when raw data arrives. Perez Mola's dbt workflow adds
version control and tests to SQL transformations. It also adds dependency graphs
and scheduled runs
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
6:49-10:04). Perafan's analytics engineering episode adds the organizational
reason. The work translates messy business reality into safer, engineered data
systems
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
11:03 and 46:34).

## Downstream Activation

The comparison becomes more consequential when transformed data leaves
analytics and changes customer-facing work. Choudhury's data-led growth stack
moves from collection and storage to BI. It then moves to reverse ETL and
operational analytics tools. Census and Hightouch are examples. Grouparoo is
another
([Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
28:52-37:25).

A metric or segment is no longer only a dashboard definition at that point. It
can drive support context, sales routing, and engagement campaigns or
onboarding.

Kwong also includes reverse data flows in the modern stack
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
35:42). That makes ELT quality visible outside the warehouse. A warehouse model
that's good enough for exploration may still fail when used for
[data activation]({{ '/wiki/data-activation/' | relative_url }}). It needs
tests, ownership, documentation, and a clear refresh path.

## Related Pages

These pages cover adjacent pipeline and modeling topics, plus storage, quality,
and activation.

- [ETL]({{ '/wiki/etl/' | relative_url }})
- [ELT]({{ '/wiki/elt/' | relative_url }})
- [ETL vs ELT decision guide]({{ '/comparisons/etl-vs-elt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
- [Data Warehouse vs Data Lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
