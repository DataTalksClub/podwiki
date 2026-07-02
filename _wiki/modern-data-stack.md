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

[[person:nataliekwong|Natalie Kwong]] gives the
clearest stack-level introduction in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
She explains ETL and ELT at 3:46-7:57. At 10:00-12:39, she connects
warehouse-side transformation to analyst autonomy,
[[dbt]], and
[[analytics engineering]].
Later in the same episode, she places data marts and lakes next to
warehouses. She also adds orchestration, Airbyte-style loading, CDC, and
reverse ETL.

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

Kwong's 33:45 discussion names the typical modern analytics stack as
best-of-breed tools rather than one monolith. [[person:arpitchoudhury|Arpit Choudhury]]
describes the growth version in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]].
Teams collect events, store them, and analyze them. They also activate the
results in business tools (22:50-41:30).

[[person:eddyzulkifly|Eddy Zulkifly]] adds the
cost-aware engineering version in
[[podcast:finops-for-data-engineers|FinOps for Data Engineers]].
At 21:57-24:34, he frames ELT, dbt, and BigQuery as parts of a digital
warehouse. He places orchestration, monitoring, and tests in the same operating
picture. Teams then need
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

Kwong starts with the move from ETL to ELT. Her version centers on faster
iteration, warehouse-side transformation, and analyst autonomy. She still keeps
governance in view. At 21:22, she discusses data swamps. At 43:02, she discusses
unused data ownership in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].

[[person:santonatuli|Santona Tuli]] starts from
pipeline design in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].
She compares analytics and ML pipelines at 13:25, then treats tooling choices
as a result of the use case rather than a fixed stack. Her 29:16 chapter
compares Upsolver, Snowflake, Databricks, and build-vs-buy decisions. At 52:54,
she returns to persona-driven pipeline design.

[[person:adrianbrudaru|Adrian Brudaru]] is more
skeptical of the label. In
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
he critiques vendor-packaged modern data stacks at 14:32 and argues for
requirements-led tool choice at 44:42. His discussion covers Iceberg,
catalogs, DuckDB, and orchestration. He also covers streaming. Those choices
show why a team may need a warehouse stack, an open lakehouse stack, or a
smaller local-first stack.

## Ingestion

Ingestion moves data from product databases and SaaS tools into analytical
storage. It also moves events, files, and operational data. In the
modern-stack episode,
Kwong frames Airbyte as the extract-load part of the flow at 3:19. She returns
to raw ingestion layers at 17:55. At 31:31, she places Airbyte next to dbt by
separating reliable loading from warehouse-side modeling.

Teams also decide how much source detail to preserve during ingestion. Kwong's
ELT discussion argues for loading first when teams need flexibility (7:57-10:00 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The same choice matters in the [[ETL vs ELT]]
tradeoff because loading first preserves flexibility when business logic
changes later. ETL can still fit large enterprises or complex staging needs,
which Kwong covers at 41:30.

Tuli adds the pipeline-engineering view. At 10:48 in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]],
she compares Upsolver and dbt by separating ingestion-focused pipeline
authoring from transformation-focused modeling. At 37:10, she adds practical
ingestion concerns such as deduplication, ordering guarantees, and PII masking.
Those concerns determine whether a simple connector is enough or whether the
team needs a stronger pipeline engine.

## Warehouses and Lakehouses

The warehouse is the default center of the stack in the older modern-stack
interviews. Kwong describes warehouses, marts, and data lakes at 15:30-27:39 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Her version separates raw or broad storage from modeled consumption layers.
The important design question is where teams transform data and how consumers
use it.

Choudhury's growth-stack episode keeps the warehouse at the center too. At
28:52-35:27, he connects warehouses, dbt, and BI analysis. He also names
Snowflake, BigQuery, Redshift, and warehouse-first analytics. That flow supports
[[product analytics]] and
[[data activation]] because the
same modeled customer data can drive analysis and downstream tools.

Tuli and Brudaru broaden the storage discussion toward lakehouse designs.
Tuli discusses staging and lakehouse architecture at 32:57 in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].

Brudaru explains Apache Iceberg as a table format over Parquet at 18:17 in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]].
At 21:27, he separates storage, compute, and access through the catalog
discussion. He also includes metadata and lineage. The storage tradeoff sits
between [[Data Warehouse]] and
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
