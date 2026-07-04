---
layout: wiki
title: "ELT"
summary: "ELT as a load-first pipeline setup for warehouses, dbt transformations, analytics engineering, CDC, quality checks, and governed marts."
related:
  - ETL
  - Modern Data Stack
  - Data Warehouse
  - Data Pipelines
  - dbt
  - Analytics Engineering
  - CDC
  - DataOps
---

ELT means extract, load, transform. A team extracts data from source systems
and loads it into analytical storage. Transformation then runs inside a
[[data warehouse]], lakehouse, or
adjacent SQL engine.

ELT usually sits inside the [[modern data stack]]. In that stack, an ingestion
tool writes raw source data to storage. [[dbt]] or plain SQL builds models. BI
tools consume governed tables.

Teams load first when business logic changes often because source detail stays
available and analysts can write new SQL transformations. Data engineers don't
need to re-extract a source every time a new field or question appears.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

Start here for load-first ELT. Use [[ETL]] for transform-before-load work and
the [[etl-vs-elt=>ETL vs ELT comparison]] when choosing between ETL and ELT.
For the full data flow and operating lifecycle, use [[Data Pipelines]].

## Load-First Model

ELT changes where business meaning gets created. In ETL, the pipeline applies
business logic before it writes to the destination. In ELT, the destination
receives raw or lightly prepared data first. The team then builds typed,
joined, cleaned, and documented tables from that stored data. Aggregations come
from the same stored layer.

Use [[ETL vs ELT]] for the tradeoff with transform-before-load. This hub follows
the load-first model after that choice is made.

The modern stack splits `E-L` from `T`, with Airbyte handling extraction and
loading. Transformations happen after data arrives in the warehouse. They range
from simple type casting to final business models that join AdWords and
Salesforce data.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]
ELT is still a [[data pipelines]]
topic because the pipeline has to move and transform data. It also has to
publish data and keep runs reliable.

ELT isn't "load everything and forget about it." Raw ingestion and data marts
are separate layers.[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]
At platform scale, teams can move from tightly coupled ETL models to ELT. They
can load data first, transform it later, and keep the model resilient as use
cases grow.[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]

## Warehouse Layers and Marts

ELT works when the warehouse has clear layers. An ingestion database keeps the
rawest form of data from a connector such as Airbyte. Teams may then build a
common layer that several groups can reuse, followed by data marts for business
consumers. Those marts may serve marketing, sales, finance, or product teams.
After transformation, business users can pull metrics from a mart because the
team has added guardrails and consistent definitions.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]

Staging gives the pipeline a holding area between source systems and the
warehouse or lakehouse. Some tools hide that stage, but the boundary still
matters. Data may be staged and checked. The ingestion tool may also
deduplicate records, enforce ordering, and mask fields before human-facing SQL
work begins.[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

ELT becomes useful to the business when teams map keys, entities, and business
questions after data arrives in the warehouse or lakehouse.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

Analytics teams use dbt to model a domain and migrate transformation work. The
same modeling work also includes decisions about wide and narrow tables plus
incremental strategies.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

At platform scale, fixed target models can become too tightly coupled as use
cases grow. Teams may keep traditional and flat models alongside lineage, a
data lake, and consumer-facing exposure paths.
[[cite:data-engineering-leadership-and-modern-data-platforms=>data engineering leadership episode]]

## Tool Boundaries

In ELT, Airbyte, dbt, and Airflow do different jobs. Airbyte sits at the
extract-load step and connects with dbt after warehouse load.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]
Airbyte is an ingestion tool in this page's vocabulary, while the warehouse
transformation layer belongs to SQL, dbt, or another modeling system.

On the transformation side, analytics engineers write SQL models,
documentation, and tests in dbt. dbt also tracks model dependencies. Snowflake
runs the queries in one example stack, while Looker consumes the modeled
result. This connects ELT directly to [[analytics engineering]].
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

[[apache-airflow=>Airflow]] belongs at the scheduling and dependency boundary.
Airflow can run Airbyte jobs, but it isn't the transformation layer.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]

Airflow, Prefect, or another orchestrator may coordinate the work. Ingestion
engines, warehouses, dbt, and modeling tools still own the work they run.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>pipeline architecture episode]]

The tool boundary widens when dbt sits next to newer workflow options and open
table formats. It also sits next to catalogs, metadata, and lineage.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]

Teams still need SQL and Python. They also need requirements work and tool
judgment even when the stack uses newer lakehouse or AI-assisted components.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
ELT is a durable workflow structure, not a fixed vendor list.

## Schema, Quality, and Governance

ELT preserves source detail, but it also creates governance work. A Salesforce
checkbox or picklist field can be ingested and modeled later without a full
extraction redesign.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]
The same flexibility can create unused raw data, unclear ownership, and
inconsistent definitions when teams don't maintain the warehouse layers.

[[CDC]] is one ingestion technique that supports
ELT. Change data capture syncs only changed records after an initial load.
Those records include changed or deleted rows instead of a fresh copy of the
whole source table.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]

CDC keeps the loaded layer fresh. The team still has to decide how changes
affect staged tables. It also has to decide how they affect modeled dimensions
and downstream marts.

Quality checks belong both before and after loading. Ingestion tools may
deduplicate, enforce ordering, and apply PII masking before data reaches
Snowflake or another destination.[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>pipeline architecture episode]]

Teams separate ingestion hygiene from business transformation. Deduplication
and ordering guarantees can happen near ingestion, and masking can happen there
too. Business modeling happens later with warehouse entities and use cases.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>pipeline architecture episode]]

Warehouse-side dbt tests can query for nulls and duplicate records. They can
also check ranges before dependent models build. The same test layer can catch
bad source data.
[[cite:analytics-engineer-skills-tools=>analytics engineering episode]]
Analytics engineering work also has to handle bad data, schema changes, and
raw-input limits.[[cite:analytics-engineer-skills-tools=>analytics engineering episode]]

Platform teams may track data quality metrics, reconcile source counts against
warehouse or lake targets, and use dynamic data masking with role-based access.
They also maintain lineage when raw and modeled data changes.
[[cite:data-engineering-leadership-and-modern-data-platforms=>data engineering leadership episode]]

These controls put ELT close to [[DataOps]]
because teams need versioned code, tests, lineage, and observability. They also
need repeatable runs, not only a load-first diagram.

## Operating the ELT Stack

ELT shifts some work from data engineers to analytics engineers and analysts.
It doesn't remove engineering work. Analytics teams gain autonomy because many
transformations can be written in SQL after data is already in the warehouse.
[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]

Daily analytics engineering work still requires data modeling and pipeline
awareness. It also requires data quality work and Looker modeling. dbt tests
and collaboration with backend and data engineering teams matter too.
[[cite:analytics-engineer-skills-tools=>analytics engineering episode]]

dbt influenced analytics engineering, but the role extends beyond tool work.
Analytics engineers also need to understand data model architecture and
business domains. They need to connect the models to KPIs. Table design and
incrementalization choices matter too.
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>marketing-to-analytics episode]]

Whether teams use dbt or a homegrown SQL runner, the same modeling questions
still apply. Another warehouse modeling layer faces those questions too.

Career projects expose the same operating skills because pipelines may need
Docker, Airflow, and AWS runs. They may also need warehouse-specific SQL, clean
data, and quality checks.
Reproducible work matters more than the ELT acronym when a pipeline has to be
useful to business analysts.[[cite:get-data-analytics-and-data-engineering-job=>data engineering job story]]

Modern analytics teams load source detail and keep the warehouse flexible.
They can transform with SQL and dbt, but they still need governance, cleanup,
and data mart boundaries.[[cite:data-engineering-tools-modern-data-stack=>modern stack episode]]

Teams make a load-first stack useful through daily [[analytics engineering]]
work. They maintain models and tests, and they coordinate DAGs and
collaboration. The acronym alone doesn't make it useful.
[[cite:analytics-engineer-skills-tools=>analytics engineering episode]]
