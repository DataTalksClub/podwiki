---
layout: wiki
title: "Modern Data Stack"
summary: "How DataTalks.Club guests describe the modern data stack across ELT, warehouses, dbt-style transformations, orchestration, activation, observability, and cost control."
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
business depends on it. DataTalks.Club guests usually describe this as
warehouse-centered [[ELT]]. The stack includes
ingestion and SQL transformations. It also includes
[[orchestration]], BI, and sometimes
reverse flows into business tools.

The clearest stack-level introduction covers ETL and ELT, and connects
warehouse-side transformation to analyst autonomy,
[[dbt]], and
[[analytics engineering]]
([[person:nataliekwong|Natalie Kwong]],
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The same episode places data marts and lakes next to warehouses, and adds
orchestration, Airbyte-style loading, CDC, and reverse ETL.

The same map reaches [[data-warehouse|data warehouses]],
[[data engineering tools]],
and [[DataOps]]. It also covers
[[reverse ETL]],
[[data activation]], and
[[data-quality-and-observability|data observability]].

## Stack Boundaries

Across the interviews, guests use a practical definition rather than a
brand-specific one. Teams identify source systems and move data into a
warehouse, lake, or lakehouse. They transform it into trusted models and
schedule the jobs. They expose the result to dashboards and analysts. The same
data may also serve product teams, models, or operational systems.

The typical modern analytics stack is best-of-breed tools rather than one
monolith
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
In the growth version, teams collect events, store them, analyze them, and
activate the results in business tools
([[person:arpitchoudhury|Arpit Choudhury]],
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

In the cost-aware engineering version, ELT, dbt, and BigQuery are parts of a
digital warehouse, with orchestration, monitoring, and tests in the same
operating picture
([[person:eddyzulkifly|Eddy Zulkifly]],
[[podcast:finops-for-data-engineers|FinOps for Data Engineers]]). Teams then
need
[[FinOps for Data Engineers]]
practices because tool choice also creates cloud usage, SaaS spend, and
ownership questions.

The modern data stack sits next to
[[data engineering platforms]].
A stack names the tools. A platform adds conventions, ownership, access paths,
and deployment habits. It also adds support paths so teams can use those tools
reliably.

## Tooling Choices and Constraints

Guests agree on the broad flow, but they focus on different constraints.

The move from ETL to ELT centers on faster iteration, warehouse-side
transformation, and analyst autonomy, while keeping governance in view through
data swamps and unused data ownership
([[person:nataliekwong|Natalie Kwong]],
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

From pipeline design, analytics and ML pipelines get compared, tooling choices
follow the use case rather than a fixed stack, and Upsolver, Snowflake,
Databricks, and build-vs-buy decisions weigh against persona-driven pipeline
design
([[person:santonatuli|Santona Tuli]],
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

A more skeptical take critiques vendor-packaged modern data stacks and argues
for requirements-led tool choice across Iceberg, catalogs, DuckDB,
orchestration, and streaming
([[person:adrianbrudaru|Adrian Brudaru]],
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
Those choices show why a team may need a warehouse stack, an open lakehouse
stack, or a smaller local-first stack.

## Ingestion

Ingestion moves data from product databases and SaaS tools into analytical
storage. It also moves events, files, and operational data. Airbyte is the
extract-load part of the flow, with raw ingestion layers placed next to dbt by
separating reliable loading from warehouse-side modeling
([[person:nataliekwong|Natalie Kwong]],
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

Teams also decide how much source detail to preserve during ingestion. Loading
first helps when teams need flexibility
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The same choice matters in the [[ETL vs ELT]]
tradeoff because loading first preserves flexibility when business logic
changes later. ETL can still fit large enterprises or complex staging needs.

The pipeline-engineering view compares Upsolver and dbt by separating
ingestion-focused pipeline authoring from transformation-focused modeling, and
adds practical ingestion concerns such as deduplication, ordering guarantees,
and PII masking
([[person:santonatuli|Santona Tuli]],
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).
Those concerns determine whether a simple connector is enough or whether the
team needs a stronger pipeline engine.

## Warehouses and Lakehouses

The warehouse is the default center of the stack in the older modern-stack
interviews. Warehouses, marts, and data lakes separate raw or broad storage from
modeled consumption layers
([[person:nataliekwong|Natalie Kwong]],
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The important design question is where teams transform data and how consumers
use it.

The growth-stack version keeps the warehouse at the center too, connecting
warehouses, dbt, and BI analysis, and naming Snowflake, BigQuery, Redshift, and
warehouse-first analytics
([[person:arpitchoudhury|Arpit Choudhury]],
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).
That flow supports
[[product analytics]] and
[[data activation]] because the
same modeled customer data can drive analysis and downstream tools.

Others broaden the storage discussion toward lakehouse designs. Staging and
lakehouse architecture come up on the pipeline side
([[person:santonatuli|Santona Tuli]],
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

Apache Iceberg is a table format over Parquet, and the catalog separates
storage, compute, and access, including metadata and lineage
([[person:adrianbrudaru|Adrian Brudaru]],
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
The storage tradeoff sits between [[Data Warehouse]] and
[[Data Warehouse vs Data Lakehouse]]
because teams choose between warehouse-first modeling, lakehouse table formats,
and mixed architectures.

## Transformations

Transformation turns loaded data into usable business entities, metrics,
features, and marts. In these modern-stack discussions, this is where dbt and
analytics engineering enter. Kwong connects transformations to type casting,
joins, and SQL modeling at 10:00, then links dbt to the emergence of the
analytics engineer at 12:39.

Tuli adds that transformation is also modeling work. At 39:23 in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]],
she discusses entities, foreign keys, and business mappings. At 43:05, she
connects marts and dashboards to the work of translating business questions
into metrics. That places transformations near
[[analytics engineering]]
rather than only low-level pipeline code.

Brudaru's 31:29 discussion in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]
shows where the category keeps changing. He treats dbt as influential because
it shaped the engineering workflow around SQL models, but he also discusses
alternatives such as SQLMesh. The durable idea isn't one tool. It's versioned
modeling with tests, dependencies, and maintainable business logic.

## Orchestration

Orchestration coordinates ingestion, transformations, checks, and refreshes.
It also coordinates backfills and downstream syncs, so teams can recover when
jobs fail. Kwong describes Airflow's role at 30:59 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
In that stack, the orchestrator schedules and runs jobs around tools such as
Airbyte and dbt.

Tuli brings deeper orchestration experience from Airflow and Astronomer. Her
career chapter at 7:08 in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]
sets up the distinction between authoring workflows and solving the full data
problem. At 26:43, she places orchestrators next to Spark and streaming tools
such as Kafka and Kinesis. She also mentions feature stores and vector
databases. The orchestrator is one control point in a broader system.

Brudaru's 35:37 discussion in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]
compares Airflow, Prefect, and Dagster. He also includes GitHub Actions.

Across these episodes, guests choose orchestration for workflows that need
dependency handling and retries. They also need visibility and clear ownership.
They keep simpler scheduling when the pipeline doesn't justify a full control
plane. The Airflow-specific details live in
[[Apache Airflow]].

## Reverse ETL and Activation

Modern data stack discussions often stop at dashboards, but several episodes
extend the stack into operational systems. Kwong introduces reverse data flows
at 35:42 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Teams can move modeled warehouse data back into tools where sales, marketing,
or support teams work.

Choudhury gives the clearest activation path. In
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]],
he moves from event tracking and tracking plans at 13:34 to the activation
flow at 22:50. That flow covers collection, storage, analysis, and activation.
At 30:03, he describes sending event data to support, sales, and engagement
tools. At 37:25, he names reverse
ETL and operational analytics tools such as Census, Hightouch, and Grouparoo.

This is where [[Reverse ETL]] and
[[Data Activation]] become part
of the stack rather than an afterthought. The same warehouse model that powers
a dashboard can also power lifecycle messaging, sales routing, onboarding, or
support context. That makes ownership and quality more important because a bad
sync can change a customer-facing workflow.

## Observability and Cost

Teams create risk when they move data quickly but can't tell whether it's
healthy. [[person:barrmoses|Barr Moses]]
defines data observability in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]
through freshness, volume, and distribution at 16:38. She also includes schema
and lineage.

At 21:57, Moses explains why a pipeline can run successfully and still produce
bad data. At 24:31, she separates monitoring from observability. Monitoring
says something changed, and observability helps the team diagnose why.

Teams need those signals across modern-stack tools. Ingestion jobs,
transformations, orchestration runs, and reverse ETL syncs all need checks that
match their consumers.
[[data-quality-and-observability|Data Observability]] and
[[Data Quality and Observability]]
cover the operating layer in more detail.

Cost is another operating constraint.
[[FinOps for Data Engineers]]
connects that constraint to cloud usage data, tagging, cost models, and
accountability.

In
[[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
Zulkifly frames cloud spend as part of data engineering, not only finance. At
31:40, he introduces FinOps for SaaS platforms. At 36:11-44:41, he covers cost
modeling, storage tiers, and reservations. He also covers tagging and
standardized reporting.

Warehouse-first stacks can shift complexity into compute, storage, and
managed-tool bills. Teams need ownership for cost just as much as they need
ownership for schemas and SLAs.
