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

[[person:nataliekwong=>Natalie Kwong]] gives the clearest
definition of why teams load first when business logic changes often. Source
detail stays available, and analysts can write new SQL transformations. Data
engineers don't need to re-extract a source every time a new field or question
appears
([[cite:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
The contrast with transform-before-load work is covered in [[ETL]] and the
[[etl-vs-elt=>ETL vs ELT comparison]].

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
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
ELT is still a [[data pipelines]]
topic because the pipeline has to move data, transform it, publish it, and keep
it reliable.

Guests don't treat ELT as "load everything and forget about it."
Kwong separates raw ingestion from data marts
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
[[person:16rahuljain=>Rahul Jain]] describes the same
move at platform scale. His team moved from tightly coupled ETL models to ELT.
They could then load data first, transform it later, and keep the model
resilient as use cases grew
([[cite:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).

## Warehouse Layers and Marts

ELT works when the warehouse has clear layers. Kwong describes an ingestion
database as the rawest form of data from a connector such as Airbyte. Teams may
then build a common layer that several groups can reuse, followed by data marts
for business consumers. Those marts may serve marketing, sales, finance, or
product teams. After transformation, business users can pull metrics from a
mart because the team has added guardrails and consistent definitions
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).

[[person:santonatuli=>Santona Tuli]] adds a more
pipeline-oriented version. She describes staging as a holding area between
source systems and the warehouse or lakehouse. Some tools hide that stage, but
the boundary still matters. Data may be staged and checked. The ingestion tool
may also deduplicate records, enforce ordering, and mask fields before
human-facing SQL work begins
([[cite:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

The modeled layer is where ELT becomes useful to the business. Tuli frames this
as mapping keys, entities, and business questions after data arrives in the
warehouse or lakehouse
([[cite:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

[[person:nikolamaksimovic=>Nikola Maksimovic]] shows the
analytics version in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]].
His team used dbt to model a domain and migrate transformation work. They also
made decisions about wide and narrow tables plus incremental strategies
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing-to-analytics episode]]).

[[person:16rahuljain=>Rahul Jain]] shows the same layer
question at platform scale. His team moved away from fixed target models that
became too tightly coupled as use cases grew. They kept traditional and flat
models alongside lineage, a data lake, and consumer-facing exposure paths
([[cite:data-engineering-leadership-and-modern-data-platforms|data engineering leadership episode]]).

## Tool Boundaries

In ELT, Airbyte, dbt, and Airflow do different jobs. Kwong places Airbyte at
the extract-load step and connects it with dbt after warehouse load
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
Airbyte is an ingestion tool in this page's vocabulary, while the warehouse
transformation layer belongs to SQL, dbt, or another modeling system.

[[person:victoriaperezmola=>Victoria Perez Mola]] explains
the transformation side. She describes dbt as the place where analytics
engineers write SQL models, documentation, and tests. dbt also tracks model
dependencies. Snowflake runs the queries in her example stack, while Looker
consumes the modeled result. Perez Mola gives the clearest link in these
episodes between ELT and [[analytics engineering]]
([[cite:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]]).

[[apache-airflow=>Airflow]] belongs at the scheduling
and dependency boundary. Kwong says Airflow is an orchestrator that can run
Airbyte jobs. It isn't the transformation layer
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).

Tuli makes the same boundary from the workflow-authoring side because Airflow,
Prefect, or another orchestrator may coordinate work. Ingestion engines,
warehouses, dbt, and modeling tools still own the work they run
([[cite:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode]]).

[[person:adrianbrudaru=>Adrian Brudaru]] widens the tool
choice by placing dbt next to newer workflow options and open table formats
([[cite:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
He also places it next to catalogs, metadata, and lineage.

His point for ELT is that
teams still need SQL and Python. They also need requirements work and tool
judgment even when the stack uses newer lakehouse or AI-assisted components
([[cite:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
ELT is a durable workflow structure, not a fixed vendor list.

## Schema, Quality, and Governance

ELT preserves source detail, but it also creates governance work. Kwong's
Salesforce example shows why teams load first. A new checkbox or picklist field
can be ingested and modeled later. The team doesn't need a full extraction
redesign
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
The same flexibility can create unused raw data, unclear ownership, and
inconsistent definitions when teams don't maintain the warehouse layers.

[[CDC]] is one ingestion technique that supports
ELT. Kwong describes change data capture as syncing only changed records after
an initial load. It includes changed or deleted rows instead of copying the
whole source table again
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
CDC helps keep the loaded layer fresh, but the team still has to decide how
those changes affect staged tables, modeled dimensions, and downstream marts.

Quality checks belong both before and after loading. Tuli says ingestion tools
may deduplicate, enforce ordering, and apply PII masking before data reaches
Snowflake or another destination
([[cite:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode]]).

She draws a boundary between ingestion hygiene and business transformation.
Deduplication and ordering guarantees can happen near ingestion. Masking can
happen there too. Business modeling happens later with warehouse entities and
use cases
([[cite:modern-data-pipelines-orchestration-ingestion-modeling|pipeline architecture episode]]).

Perez Mola then shows the warehouse-side checks. dbt tests can query for nulls,
range violations, and duplicate records before dependent models build. The same
test layer can catch bad source data
([[cite:analytics-engineer-skills-tools|analytics engineering episode]]).
Her later discussion also emphasizes bad data, schema changes, and raw-input
limits in analytics engineering work
([[cite:analytics-engineer-skills-tools|analytics engineering episode]]).

Jain's platform episode adds controls. His team tracked data quality metrics,
reconciled source counts against warehouse or lake targets, and used dynamic
data masking with role-based access. They also maintained lineage when raw and
modeled data changed
([[cite:data-engineering-leadership-and-modern-data-platforms|data engineering leadership episode]]).

These controls put ELT close to [[DataOps]]
because teams need versioned code, tests, lineage, and observability. They also
need repeatable runs, not only a load-first diagram.

## Operating the ELT Stack

ELT shifts some work from data engineers to analytics engineers and analysts,
but it doesn't remove engineering work. Kwong says ELT gives analytics teams
more autonomy. Many transformations can be written in SQL after data is already
in the warehouse
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).
Perez Mola's daily work requires data modeling, pipeline awareness, and data
quality. It also requires Looker work, dbt tests, and collaboration with
backend and data engineering teams
([[cite:analytics-engineer-skills-tools|analytics engineering episode]]).

Maksimovic's episode keeps the role from becoming tool worship. He says dbt
influenced analytics engineering, but the deeper skill is understanding data
model architecture, business domains, and KPIs. Table design and
incrementalization choices matter too
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing-to-analytics episode]]).
That's why an ELT stack can use dbt, a homegrown SQL runner, or another
warehouse modeling layer and still face the same modeling questions.

[[person:gloriaquiceno=>Gloria Quiceno]] brings in the
career and project side in
[[podcast:get-data-analytics-and-data-engineering-job=>her data engineering job story]].
Her discussion ties pipelines to Docker and Airflow. It also covers AWS runs,
warehouse-specific SQL, clean data, and quality checks. The episode is less
about the ELT acronym. It focuses on the operational skills that make a
pipeline reproducible and
useful to business analysts
([[cite:get-data-analytics-and-data-engineering-job|her data engineering job story]]).

Kwong's modern analytics argument is to load source detail and keep the
warehouse flexible. She argues that analytics teams can transform with SQL and
dbt. They still need governance, cleanup, and data mart boundaries
([[cite:data-engineering-tools-modern-data-stack|modern stack episode]]).

Perez Mola brings the same concern down to daily
[[analytics engineering]].
Models, tests, DAGs, and collaboration decide whether the load-first stack is
useful. The acronym alone doesn't make it useful.
