---
layout: wiki
title: "Modern Data Stack"
summary: "The modern data stack as an ELT-centered architecture for loading, modeling, serving, operating, and activating data."
related:
  - Modern Data Engineering Trends
  - Data Engineering Platforms
  - ETL vs ELT
  - ETL
  - ELT
  - dbt
  - Analytics Engineering
  - Data Warehouse
  - Reverse ETL
  - Data Activation
  - Data Quality and Observability
---

Teams use the modern data stack as an architecture for collecting data and
loading it into analytical storage. They model it for consumers and keep the
flow running after the business depends on it. A warehouse-centered [[ELT]]
stack usually composes ingestion and SQL transformations. It also needs
[[orchestration]] and BI. It may send modeled data back into business tools
too.[[cite:data-engineering-tools-modern-data-stack]]

Stack composition asks which layers exist and how data moves between them. It
also asks where warehouse-centered analytics changes the operating model.

[[Data Engineering Tools]] covers category-by-category tool selection, while
[[ETL vs ELT]] covers the transform-before-load versus load-first decision.
[[ETL]] and [[ELT]] cover the underlying concepts, while
[[Data Pipelines]] covers movement and publication. It also covers recovery and
reliability.

This architecture reaches [[data-warehouse=>data warehouses]], [[Data Engineering Tools]],
and [[DataOps]]. It also reaches [[reverse ETL]] and [[data activation]].
[[data-quality-and-observability=>Data observability]] covers the operating
layer. It connects
warehouse-side transformation to analyst autonomy and links [[dbt]] with
[[analytics engineering]]. It then adds data marts and lakes. It also adds
Airbyte-style loading, CDC, and reverse ETL.[[cite:data-engineering-tools-modern-data-stack]]

## Stack Boundaries

The practical definition isn't brand-specific. Teams identify source systems
and choose where analytical data lives. They transform it into trusted models,
schedule the work, and expose the result to dashboards or operational
systems.[[cite:data-engineering-tools-modern-data-stack]]

The typical modern analytics stack is best-of-breed tools rather than one
monolith.[[cite:data-engineering-tools-modern-data-stack]]
Kwong names the split through concrete tools. Airbyte handles extract-load into
the warehouse. dbt handles SQL transformations after data arrives. Airflow
schedules work around those pieces, and reverse ETL sends selected warehouse
outputs back into operational tools.
[[cite:data-engineering-tools-modern-data-stack@30:59=>ETL vs ELT and the Modern Data Stack]]
[[cite:data-engineering-tools-modern-data-stack@31:31=>ETL vs ELT and the Modern Data Stack]]
[[cite:data-engineering-tools-modern-data-stack@35:42=>ETL vs ELT and the Modern Data Stack]].

Tammy Liang's small-team version used Stitch for loading and GCP as the cloud
foundation. A [[dbt]] layer handled transformations. The team
used Google Data Studio for BI, and Notion held dashboard links and analysis
work.[[cite:building-and-scaling-data-team]]

That example treats delivery and documentation as part of stack composition,
not only the ingestion and modeling layers.

In the analytics-engineering version, the stack loads data into Snowflake,
models it in dbt, and exposes modeled data through Looker
[[cite:analytics-engineer-skills-tools@10:04=>Analytics Engineer Skills and Tools]].

The growth version collects and stores events, analyzes them, and activates the
results in business tools.[[cite:data-led-growth-event-tracking-and-reverse-etl]]

The cost-aware engineering version treats ELT and dbt as parts of a digital
warehouse. BigQuery anchors the warehouse, with orchestration, monitoring, and
tests in the same operating picture.[[cite:finops-for-data-engineers]]

Teams then need [[FinOps for Data Engineers]] practices because tool choice also
creates cloud usage, SaaS spend, and ownership questions.

The modern data stack sits next to [[data engineering platforms]]. A stack
names how the layers fit together. A platform adds conventions and ownership.
It also defines access paths, deployment habits, and support paths so teams can
use those layers reliably.

## Composition Tradeoffs

Teams reuse the same broad flow, but constraints vary by team.

The move from ETL to ELT centers on faster iteration, warehouse-side
transformation, and analyst autonomy. It keeps governance in view through data
swamps and unused data ownership.[[cite:data-engineering-tools-modern-data-stack]]

Analytics and ML pipelines need different compositions because the use case
drives the stack. Upsolver, Snowflake, and Databricks fit different
persona-driven pipeline designs. Teams still face build-vs-buy decisions inside
that design.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

Adrian Brudaru critiques vendor-packaged modern data stacks and argues for
requirements-led composition. A team may need a warehouse-first stack or an
open lakehouse stack. Another team may need a streaming-heavy stack or a smaller
local-first stack.
Teams can use [[DuckDB]] with GitHub Actions in the local-first case when
file-backed SQL is enough for a small workflow.

[[Modern Data Engineering Trends]] covers the current version of that critique.
For selection risks, compare licensing and lock-in in [[Data Engineering Tools]].
Connector coverage belongs in that comparison too
[[cite:trends-in-modern-data-engineering@14:32=>Modern Data Engineering Trends]]
[[cite:trends-in-modern-data-engineering@27:40=>Modern Data Engineering Trends]]
[[cite:data-engineering-tools-modern-data-stack@43:45=>Modern Data Stack]]
[[cite:data-engineering-tools-modern-data-stack@48:26=>Modern Data Stack]].

The same caution applies to enterprise-grade platforms. Teams should move to
Snowflake or Databricks only when the use case justifies it. Scale and analyst
count are the first checks. Data-science needs and business value are the next
checks. Teams should use the same standard for a large self-built platform
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for@30:56=>Data Engineer Career in 2026]].

Smaller teams can start with a database plus dbt. Simple orchestration and BI
may fit better than a lakehouse plus real-time platform when the business only
needs daily analytics.

## Load, Model, Serve

The core architecture loads source data into analytical storage. It models that
data into business entities and serves the modeled layer to consumers. Those
consumers include dashboards, analysts, and product teams. They also include ML
systems and operational tools.
[[cite:data-engineering-tools-modern-data-stack]]

Loading first matters because it preserves flexibility when business logic
changes later. That's the central [[ETL vs ELT]] tradeoff. ETL can still fit
large enterprises or complex staging needs, but modern-stack conversations
often put raw loading and warehouse-side modeling next to each other
[[cite:data-engineering-tools-modern-data-stack]].
When central storage contains repeated customer, supplier, or product records,
teams have another warehouse-side modeling problem: [[Entity Resolution]]
[[cite:building-open-source-data-product-for-identity-resolution=>Building an Open-Source Identity Resolution Tool]].

The pipeline-engineering view draws the same boundary by separating
ingestion-focused pipeline authoring from transformation-focused modeling.
Deduplication, ordering guarantees, and PII masking may move a team away from a
simple connector toward a stronger pipeline engine. The architectural question
stays the same. Teams decide what enters the analytical store, what gets
modeled there, and what leaves it for consumers.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

## Storage Center of Gravity

Older modern-stack interviews put the warehouse at the center. In that design,
warehouses and marts hold modeled consumption layers. Data lakes handle raw or
broad storage.[[cite:data-engineering-tools-modern-data-stack]]
The important design question is where teams transform data and how consumers
use it.

The growth-stack version keeps the warehouse at the center too. It connects a
warehouse, dbt models, BI analysis, and activation. That flow supports
[[product analytics]] and [[data activation]] because the same modeled customer
data can drive analysis and downstream tools.[[cite:data-led-growth-event-tracking-and-reverse-etl]]

Others broaden the storage discussion toward lakehouse designs. Staging and
lakehouse architecture come up on the pipeline side. Apache Iceberg separates
storage and compute. It manages access through Parquet tables, catalog
metadata, and lineage.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]
[[cite:trends-in-modern-data-engineering]].
The storage tradeoff sits between [[Data Warehouse]] and
[[Data Warehouse vs Data Lakehouse]] because teams choose between
warehouse-first modeling, lakehouse table formats, and mixed architectures.

## Operating The Stack

Orchestration coordinates ingestion and transformations when modern stack
layers operate together. It runs checks, refreshes, backfills, and downstream
syncs for recovery. In warehouse-centered stacks, orchestrators schedule jobs
around loading and modeling layers. They don't replace those layers
[[cite:data-engineering-tools-modern-data-stack@30:59=>Modern Data Stack]]
[[cite:data-engineering-tools-modern-data-stack@33:45=>Modern Data Stack]].

Workflow authoring isn't the whole data problem. Modern stacks may also include
Spark and streaming systems such as Kafka and Kinesis. Some designs add feature
stores or vector databases. Teams still have to define checks and ownership
across the layers the use case requires. They also need recovery paths.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

The specific orchestrator selection details belong on [[Data Engineering Tools]]
and [[Apache Airflow]]. The architectural boundary stays here.

## Reverse ETL and Activation

Modern data stack discussions often stop at dashboards, but several episodes
extend the stack into operational systems. Reverse data flows move modeled
warehouse data back into tools where sales, marketing, or support teams
work.[[cite:data-engineering-tools-modern-data-stack]]

The activation path starts with event tracking and tracking plans. It then moves
through collection, storage, analysis, and activation. Event data can flow to
support, sales, and engagement tools. Reverse ETL and operational analytics
tools such as Census, Hightouch, and Grouparoo handle the sync.[[cite:data-led-growth-event-tracking-and-reverse-etl]]

This is where [[Reverse ETL]] and [[Data Activation]] become part of the stack
rather than an afterthought. The same warehouse model that powers a dashboard
can also power lifecycle messaging, sales routing, onboarding, or support
context. [[Data Engineering Tools]] covers the product-selection side of that
decision. A bad sync can change a customer-facing workflow, so activation
belongs in the stack design.

## Observability and Cost

Teams create risk when they move data quickly but can't tell whether it's
healthy. Data observability covers freshness, volume, and distribution. It also
covers schema and lineage.[[cite:data-quality-data-observability-data-reliability]]
A pipeline can run successfully and still produce bad data. Monitoring says
something changed, and observability helps the team diagnose why.[[cite:data-quality-data-observability-data-reliability]]

Teams need those signals across modern-stack tools. Ingestion jobs,
transformations, orchestration runs, and reverse ETL syncs all need checks that
match their consumers.
[[data-quality-and-observability=>Data Observability]] and
[[Data Quality and Observability]]
cover the operating layer in more detail.

Cost is another operating constraint.
[[FinOps for Data Engineers]]
connects that constraint to cloud usage data, tagging, cost models, and
accountability.

Cloud spend belongs in data engineering, not only finance. The operating work
includes SaaS platform spend, cost modeling, and storage tiers. It also covers
reservations, tagging, and standardized reporting.[[cite:finops-for-data-engineers]]

Warehouse-first stacks can shift complexity into compute, storage, and
managed-tool bills. Teams need ownership for cost just as much as they need
ownership for schemas and SLAs.
