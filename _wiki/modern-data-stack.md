---
layout: wiki
title: "Modern Data Stack"
summary: "How podcast guests map the modern data stack across ELT, warehouses, dbt-style modeling, orchestration, activation, observability, and cost."
related:
  - Data Engineering Platforms
  - ELT
  - dbt
  - Analytics Engineering
  - Data Warehouse
  - Reverse ETL
  - Data Activation
  - Data Quality and Observability
---

Teams use the modern data stack to collect and load data into analytical
storage. They model it for consumers and keep the flow running after the
business depends on it. A warehouse-centered [[ELT]] stack usually includes
ingestion, SQL transformations, [[orchestration]], and BI. It may also send
modeled data back into business tools.[[cite:data-engineering-tools-modern-data-stack]]

That map reaches [[data-warehouse=>data warehouses]], [[data engineering tools]],
and [[DataOps]]. It also reaches [[reverse ETL]] and [[data activation]].
[[data-quality-and-observability=>Data observability]] covers the operating
layer. It connects
warehouse-side transformation to analyst autonomy and links [[dbt]] with
[[analytics engineering]]. It then adds data marts and lakes. It also adds
Airbyte-style loading, CDC, and reverse ETL.[[cite:data-engineering-tools-modern-data-stack]]

## Stack Boundaries

The practical definition isn't brand-specific. Teams identify source systems
and move data into a warehouse, lake, or lakehouse. They transform it into
trusted models, schedule the jobs, and expose the result to dashboards and
analysts. The same data may also serve product teams, models, or operational
systems.[[cite:data-engineering-tools-modern-data-stack]]

The typical modern analytics stack is best-of-breed tools rather than one
monolith.[[cite:data-engineering-tools-modern-data-stack]]

Tammy Liang's small-team version used Stitch for loading and GCP as the cloud
foundation. A [[dbt]] layer handled transformations. The team
used Google Data Studio for BI, and Notion held dashboard links and analysis
work.[[cite:building-and-scaling-data-team]]

That example treats delivery and documentation as part of the stack, not only
the ingestion and modeling tools.

The growth version collects and stores events. It analyzes them and activates
the results in business tools.[[cite:data-led-growth-event-tracking-and-reverse-etl]]

The cost-aware engineering version treats ELT and dbt as parts of a digital
warehouse. BigQuery anchors the warehouse, with orchestration, monitoring, and
tests in the same operating picture.[[cite:finops-for-data-engineers]]

Teams then need [[FinOps for Data Engineers]] practices because tool choice also
creates cloud usage, SaaS spend, and ownership questions.

The modern data stack sits next to [[data engineering platforms]]. A stack names
the tools. A platform adds conventions and ownership. It also defines access
paths, deployment habits, and support paths so teams can use those tools
reliably.

## Tooling Tradeoffs

Teams reuse the same broad flow, but constraints vary by team.

The move from ETL to ELT centers on faster iteration, warehouse-side
transformation, and analyst autonomy. It keeps governance in view through data
swamps and unused data ownership.[[cite:data-engineering-tools-modern-data-stack]]

Analytics and ML pipelines need different tooling choices because the use case
drives the stack. Upsolver, Snowflake, and Databricks fit different
persona-driven pipeline designs, and teams still face build-vs-buy decisions
inside that design.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

A more skeptical view critiques vendor-packaged modern data stacks and argues
for requirements-led tool choice. Iceberg and catalogs can belong in the
decision. DuckDB, orchestration, and streaming can too. A team may need a
warehouse stack, an open lakehouse stack, or a smaller local-first
stack.[[cite:trends-in-modern-data-engineering]]

## Ingestion

Ingestion moves data from product databases and SaaS tools into analytical
storage. It also moves events, files, and operational data. Airbyte handles the
extract-load part of the flow. Raw ingestion layers sit next to dbt by
separating reliable loading from warehouse-side modeling.[[cite:data-engineering-tools-modern-data-stack]]

During ingestion, teams choose how much source detail to preserve. Loading
first helps when teams need flexibility.[[cite:data-engineering-tools-modern-data-stack]]
The same choice matters in the [[ETL vs ELT]] tradeoff. Loading first preserves
flexibility when business logic changes later. ETL can still fit large
enterprises or complex staging needs.

The pipeline-engineering view compares Upsolver and dbt by separating
ingestion-focused pipeline authoring from transformation-focused modeling. It
also adds practical ingestion concerns. Deduplication, ordering guarantees, and
PII masking determine whether a simple connector is enough. Some teams need a
stronger pipeline engine.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

## Warehouses and Lakehouses

Older modern-stack interviews put the warehouse at the center. Warehouses and
marts hold modeled consumption layers, while data lakes handle raw or broad
storage.[[cite:data-engineering-tools-modern-data-stack]]

The important design question is where teams transform data and how consumers
use it.

The growth-stack version keeps the warehouse at the center too. It connects
warehouses, dbt, and BI analysis. It names Snowflake, BigQuery, and Redshift.
It also names warehouse-first analytics.[[cite:data-led-growth-event-tracking-and-reverse-etl]]
That flow supports
[[product analytics]] and
[[data activation]] because the
same modeled customer data can drive analysis and downstream tools.

Others broaden the storage discussion toward lakehouse designs. Staging and
lakehouse architecture come up on the pipeline side.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

Apache Iceberg uses Parquet tables. A catalog stores metadata and lineage, while
the table format separates storage, compute, and access.[[cite:trends-in-modern-data-engineering]]

The storage tradeoff sits between [[Data Warehouse]] and
[[Data Warehouse vs Data Lakehouse]]
because teams choose between warehouse-first modeling, lakehouse table formats,
and mixed architectures.

## Transformations

Transformation turns loaded data into usable business entities, metrics,
features, and marts. In these modern-stack discussions, this is where dbt and
analytics engineering enter. Transformation covers type casting, joins, SQL
modeling, and the analyst-to-analytics-engineer shift around
dbt.[[cite:data-engineering-tools-modern-data-stack]]

Transformation is also modeling work. Entities, foreign keys, and business
mappings connect marts and dashboards to metrics. That puts the stack near
[[analytics engineering]] rather than only low-level pipeline code.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

As the category changes, dbt shaped the engineering workflow around SQL models.
Alternatives such as SQLMesh keep the durable idea broader than one tool. The
durable practice is versioned modeling with tests, dependencies, and maintainable
business logic.[[cite:trends-in-modern-data-engineering]]

## Orchestration

Orchestration coordinates ingestion, transformations, checks, and refreshes.
It also coordinates backfills and downstream syncs, so teams can recover when
jobs fail. In the warehouse-centered stack, the orchestrator schedules and runs
jobs around tools such as Airbyte and dbt. Airbyte-style tools handle the
extract-load step, while dbt-style tools handle warehouse-side SQL
transformations. Orchestration keeps the pieces in the same operating
workflow.[[cite:data-engineering-tools-modern-data-stack]]

Workflow authoring isn't the whole data problem. Orchestrators sit next to
Spark, streaming tools such as Kafka and Kinesis, feature stores, and vector
databases in the same broader system.[[cite:modern-data-pipelines-orchestration-ingestion-modeling]]

Tools such as Airflow and Prefect cover different orchestration needs. Dagster
and GitHub Actions can also fit scheduling work.[[cite:trends-in-modern-data-engineering]]
Teams choose orchestration for workflows that need dependency handling and
retries. They also need visibility and clear ownership. They keep simpler
scheduling when the pipeline doesn't justify a full control plane. The
Airflow-specific details live in [[Apache Airflow]].

## Reverse ETL and Activation

Modern data stack discussions often stop at dashboards, but several episodes
extend the stack into operational systems. Reverse data flows move modeled
warehouse data back into tools where sales, marketing, or support teams
work.[[cite:data-engineering-tools-modern-data-stack]]

The activation path starts with event tracking and tracking plans. It then moves
through collection, storage, analysis, and activation. Event data can flow to
support, sales, and engagement tools. Reverse ETL and operational analytics
tools such as Census, Hightouch, and Grouparoo handle the sync.[[cite:data-led-growth-event-tracking-and-reverse-etl]]

This is where [[Reverse ETL]] and
[[Data Activation]] become part
of the stack rather than an afterthought. The same warehouse model that powers
a dashboard can also power lifecycle messaging, sales routing, onboarding, or
support context. That makes ownership and quality more important because a bad
sync can change a customer-facing workflow.

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
