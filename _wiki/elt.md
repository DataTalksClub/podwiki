---
layout: wiki
title: "ELT"
summary: "ELT as a load-first data pipeline setup for warehouses, dbt transformations, analytics engineering, orchestration, CDC, quality checks, and governed data marts."
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
and loads it into analytical storage. It then transforms the data inside a
[[data warehouse]], lakehouse, or
adjacent SQL engine.

In DataTalks.Club discussions, ELT usually sits inside the
[[modern data stack]]. In that
stack, an ingestion tool writes raw source data to storage.
[[dbt]] or plain SQL builds models. BI tools
consume governed tables.

[[person:nataliekwong|Natalie Kwong]] gives the clearest
definition in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
At 7:57-14:54, she explains why teams load first when business logic changes
often. Source detail stays available, and analysts can write new SQL
transformations. Data engineers don't need to re-extract a source every time a
new field or question appears. The contrast with transform-before-load work is
covered in [[ETL]] and the
[[etl-vs-elt|ETL vs ELT comparison]].

## Load-First Model

ELT changes where business meaning gets created. In ETL, the pipeline applies
business logic before it writes to the destination. In ELT, the destination
receives raw or lightly prepared data first. The team then builds typed,
joined, cleaned, and documented tables from that stored data. Aggregations come
from the same stored layer.

Kwong describes this as splitting the `E-L` work from the `T` work. Airbyte
handles extraction and loading, while transformations happen after data arrives
in the warehouse. Her examples range from simple type casting to joining
AdWords and Salesforce data into a final business model
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 10:00-12:39]]).
ELT is still a [[data pipelines]]
topic because the pipeline has to move data, transform it, publish it, and keep
it reliable.

Guests don't treat ELT as "load everything and forget about it."
Kwong separates raw ingestion from data marts at 15:30-18:47.
[[person:16rahuljain|Rahul Jain]] describes the same
move at platform scale in
[[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]].
His team moved from tightly coupled ETL models to ELT. They could then load
data first, transform it later, and keep the model resilient as use cases grew
(30:50-33:15).

## Warehouse Layers and Marts

ELT works when the warehouse has clear layers. Kwong describes an ingestion
database as the rawest form of data from a connector such as Airbyte. Teams may
then build a common layer that several groups can reuse, followed by data marts
for business consumers. Those marts may serve marketing, sales, finance, or
product teams. After transformation, business users can pull metrics from a
mart because the team has added guardrails and consistent definitions
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 15:30-18:47]]).

[[person:santonatuli|Santona Tuli]] adds a more
pipeline-oriented version in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].
At 32:57-39:23, she describes staging as a holding area between source systems
and the warehouse or lakehouse. Some tools hide that stage, but the boundary
still matters. Data may be staged and checked. The ingestion tool may also
deduplicate records, enforce ordering, and mask fields before human-facing SQL
work begins.

The modeled layer is where ELT becomes useful to the business. Tuli frames this
as mapping keys, entities, and business questions after data arrives in the
warehouse or lakehouse (39:23-43:05).

[[person:nikolamaksimovic|Nikola Maksimovic]] shows the
analytics version in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]].
His team used dbt to model a domain and migrate transformation work. They also
made decisions about wide and narrow tables plus incremental strategies
(18:34-33:46).

[[person:16rahuljain|Rahul Jain]] shows the same layer
question at platform scale. His team moved away from fixed target models that
became too tightly coupled as use cases grew. They kept traditional and flat
models alongside lineage, a data lake, and consumer-facing exposure paths
([[podcast:data-engineering-leadership-and-modern-data-platforms|data engineering leadership episode at 30:50-33:15 and 57:29-57:56]]).

## Tool Boundaries

In ELT, Airbyte, dbt, and Airflow do different jobs. Kwong places Airbyte at
the extract-load step and connects it with dbt after warehouse load
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 31:31-33:45]]).
Airbyte is an ingestion tool in this page's vocabulary, while the warehouse
transformation layer belongs to SQL, dbt, or another modeling system.

[[person:victoriaperezmola|Victoria Perez Mola]] explains
the transformation side in
[[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]].
At 4:05-10:04, she describes dbt as the place where analytics engineers write
SQL models, documentation, and tests. dbt also tracks model dependencies.
Snowflake runs the queries in her example stack, while Looker consumes the
modeled result. Perez Mola gives the clearest link in these episodes between
ELT and [[analytics engineering]].

[[apache-airflow|Airflow]] belongs at the scheduling
and dependency boundary. Kwong says Airflow is an orchestrator that can run
Airbyte jobs. It isn't the transformation layer
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 30:59-31:31]]).

Tuli makes the same boundary from the workflow-authoring side because Airflow,
Prefect, or another orchestrator may coordinate work. Ingestion engines,
warehouses, dbt, and modeling tools still own the work they run
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode at 7:08-10:48 and 26:43-29:16]]).

[[person:adrianbrudaru|Adrian Brudaru]] widens the tool
choice in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]].
He places dbt next to newer workflow options and open table formats. He also
places it next to catalogs, metadata, and lineage.

His point for ELT is that
teams still need SQL and Python. They also need requirements work and tool
judgment even when the stack uses newer lakehouse or AI-assisted components
(21:27-35:37 and 41:06-44:42).
ELT is a durable workflow structure, not a fixed vendor list.

## Schema, Quality, and Governance

ELT preserves source detail, but it also creates governance work. Kwong's
Salesforce example shows why teams load first. A new checkbox or picklist field
can be ingested and modeled later. The team doesn't need a full extraction
redesign
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 7:57-12:39 and 48:58-49:32]]).
The same flexibility can create unused raw data, unclear ownership, and
inconsistent definitions when teams don't maintain the warehouse layers.

[[CDC]] is one ingestion technique that supports
ELT. Kwong describes change data capture as syncing only changed records after
an initial load. It includes changed or deleted rows instead of copying the
whole source table again
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 45:59-48:26]]).
CDC helps keep the loaded layer fresh, but the team still has to decide how
those changes affect staged tables, modeled dimensions, and downstream marts.

Quality checks belong both before and after loading. Tuli says ingestion tools
may deduplicate, enforce ordering, and apply PII masking before data reaches
Snowflake or another destination
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode at 37:10-39:23]]).

She draws a boundary between ingestion hygiene and business transformation.
Deduplication and ordering guarantees can happen near ingestion. Masking can
happen there too. Business modeling happens later with warehouse entities and
use cases
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode at 37:10-43:05]]).

Perez Mola then shows the warehouse-side checks. dbt tests can query for nulls,
range violations, and duplicate records before dependent models build. The same
test layer can catch bad source data
([[podcast:analytics-engineer-skills-tools|analytics engineering episode at 36:44-40:42]]).
Her later discussion also emphasizes bad data, schema changes, and raw-input
limits in analytics engineering work
([[podcast:analytics-engineer-skills-tools|analytics engineering episode at 36:44-48:36]]).

Jain's platform episode adds controls. His team tracked data quality metrics,
reconciled source counts against warehouse or lake targets, and used dynamic
data masking with role-based access. They also maintained lineage when raw and
modeled data changed
([[podcast:data-engineering-leadership-and-modern-data-platforms|data engineering leadership episode at 25:04-33:15]]).

These controls put ELT close to [[DataOps]]
because teams need versioned code, tests, lineage, and observability. They also
need repeatable runs, not only a load-first diagram.

## Operating the ELT Stack

ELT shifts some work from data engineers to analytics engineers and analysts,
but it doesn't remove engineering work. Kwong says ELT gives analytics teams
more autonomy. Many transformations can be written in SQL after data is already
in the warehouse
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 12:39-14:54]]).
Perez Mola's daily work requires data modeling, pipeline awareness, and data
quality. It also requires Looker work, dbt tests, and collaboration with
backend and data engineering teams
([[podcast:analytics-engineer-skills-tools|analytics engineering episode at 4:05-14:34 and 33:02-40:42]]).

Maksimovic's episode keeps the role from becoming tool worship. He says dbt
influenced analytics engineering, but the deeper skill is understanding data
model architecture, business domains, and KPIs. Table design and
incrementalization choices matter too
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing-to-analytics episode at 28:40-33:46]]).
That's why an ELT stack can use dbt, a homegrown SQL runner, or another
warehouse modeling layer and still face the same modeling questions.

[[person:gloriaquiceno|Gloria Quiceno]] brings in the
career and project side in
[[podcast:get-data-analytics-and-data-engineering-job|her data engineering job story]].
Her discussion ties pipelines to Docker and Airflow. It also covers AWS runs,
warehouse-specific SQL, clean data, and quality checks. The episode is less
about the ELT acronym. It focuses on the operational skills that make a
pipeline reproducible and
useful to business analysts (21:25-36:20 and 50:15-53:34).

Kwong's modern analytics argument is to load source detail and keep the
warehouse flexible. She argues that analytics teams can transform with SQL and
dbt. They still need governance, cleanup, and data mart boundaries
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 7:57-18:47 and 43:02-45:59]]).

Perez Mola brings the same concern down to daily
[[analytics engineering]].
Models, tests, DAGs, and collaboration decide whether the load-first stack is
useful. The acronym alone doesn't make it useful.
