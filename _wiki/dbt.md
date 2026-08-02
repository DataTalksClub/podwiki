---
layout: wiki
title: "dbt"
summary: "dbt as warehouse-side SQL transformation for analytics engineering: models, tests, docs, DAGs, and reviewed changes."
related:
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Modern Data Stack
  - ELT
  - Data Warehouse
  - Data Quality and Observability
  - DataOps
---

dbt is the clearest practical example of
[[analytics engineering]]
in this set of episodes. Teams write SQL models, run them in a
[[data warehouse]], and treat the
transformation layer as reviewed code with tests. The shift isn't only from
ETL to [[ELT]]. Analysts and analytics
engineers move from isolated SQL queries to a maintained project.
[[cite:analytics-engineer-skills-tools@30:06=>Analytics Engineer Skills and Tools]]

That project
tracks dependencies and version control. It also keeps tests, documentation,
and macros with the SQL models.

[[person:victoriaperezmola=>Victoria Perez Mola]]
gives the most direct explanation in.
[[cite:analytics-engineer-skills-tools@06:49=>Analytics Engineer Skills and Tools]]
She describes dbt as the tool her team uses for modeling data after it arrives
in Snowflake, alongside Looker and ingestion tooling. dbt keeps SQL files in a
code workflow and manages model dependencies. It builds a DAG and exposes
documentation. Teams also use it for tests.

DataTalks.Club therefore treats dbt as a practical bridge between analytics
work and software engineering habits.
Rui Machado and Helder Russa's
[[book:20231106-analytics-engineering-with-sql-and-dbt=>Analytics Engineering with SQL and DBT]]
covers the same warehouse-side SQL modeling workflow. It also reinforces the
testing and DAG-based project practices that Victoria describes here.

## Warehouse-Side Transformation

dbt belongs most naturally to warehouse-side transformation in the
[[ETL vs ELT]] discussion.
[[person:nataliekwong=>Natalie Kwong]] explains that
move in.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
She contrasts transforming before load with loading first and transforming in
analytical storage. ELT gives analysts and analytics engineers more room to
adjust business logic after raw data is available.

dbt fits that ELT flow because it doesn't replace the warehouse. It compiles
and runs transformation logic against warehouses such as Snowflake and BigQuery.
Redshift fits the same warehouse-backed model. Kwong places dbt next to ingestion tools and
data marts. She also places it near orchestration, CDC, and reverse data flows
([[Modern Data Stack]],
[[Reverse ETL]]).

[[person:santonatuli=>Santona Tuli]] draws the same
boundary from the pipeline side in.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]
Her Upsolver comparison separates ingestion-focused pipeline authoring from
dbt-style SQL modeling. dbt can author transformations, but another system
still loads data, handles streaming or ordering guarantees, and may provide the
execution engine.

## Analytics Engineering Workflow

Perez Mola centers dbt on workflow because SQL models live in files. Teams can
review changes in Git and see how a model changed over time. dbt resolves
dependencies between models and renders the DAG. Teams can see what a change
will affect before it reaches dashboards or downstream tables.
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

[[person:nikolamaksimovic=>Nikola Maksimovic]] shows the
implementation side in.
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]
His transition from marketing into BI and analytics engineering included a dbt
migration and data modeling. It also included Looker work, product analytics,
and A/B testing support.

The dbt project wasn't a side tool. It was where reusable business logic moved
out of scattered reports and into modeled transformation layers. His later
discussion of wide and narrow tables keeps the focus on model design, not tool
adoption alone.
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]

[[person:juanmanuelperafan=>Juan Manuel Perafan]]
pushes the same point in.
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]
He treats dbt as one way to put analytics engineering into practice, not as the
definition of the job. The craft is still translating business reality into
clean data systems. dbt helps when the team needs those systems to be tested,
reviewed, and repeatable.

## Tests and Quality

dbt tests turn data quality checks into project code. Perez Mola describes
standard checks such as non-null and uniqueness tests. She also covers custom
SQL tests.

A dbt test is a query: if the query returns failing rows, dbt can
warn or error. Her team checks sources before building dependent models. Bad
source data shouldn't silently flow into the modeled layer.
[[cite:analytics-engineer-skills-tools@38:53=>Analytics Engineer Skills and Tools]]

Those tests put dbt close to
[[data quality and observability]].
dbt can catch assumptions about required fields and duplicate identifiers. It
can also check accepted ranges, valid city names, and relationships. It can't
prove that every business number is correct.

Perez Mola is explicit that data quality remains ongoing work. Teams add tests
after they learn from mismatches.

Perafan broadens the testing conversation. He contrasts manual dashboard
checking with automated tests for SQL logic and data assumptions.

He describes generic tests and singular SQL tests as ways to make analytics
work safer. Unit-test style checks belong in the same testing conversation.
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]
His argument lines up with
[[ci-cd=>CI/CD]] and
[[DataOps]]: tests should run before bad
changes reach consumers, not only after a stakeholder reports a broken metric.

[[person:christopherbergh=>Christopher Bergh]] puts the
same testing habit inside a broader DataOps operating model in.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
He names version control and automated tests among the ways data teams reduce
fragile releases. CI/CD, SQL tests, and dbt belong in that same toolkit. Use
[[dataops-checks-for-data-pipelines=>DataOps checks for data pipelines]] when
dbt checks need to sit beside freshness, schema, volume, and recovery checks.

## Documentation and Lineage

dbt documentation is part of the workflow, not an afterthought. Perez Mola
describes schema YAML files where teams document models and fields. Teams can
also record tags and custom metadata.

dbt docs can show model code, generated documentation, and dependencies. Before
changing a table, an analytics engineer can look at what depends on it.
[[cite:analytics-engineer-skills-tools@50:46=>Analytics Engineer Skills and Tools]]

Perez Mola also marks a limit by distinguishing documentation from data
profiling. dbt can document models and expose lineage, but it isn't the main
tool for deep profiling or full observability. She mentions profiling and
observability tools such as Datafold and Monte Carlo as adjacent options. dbt
therefore sits inside the
[[modern data stack]] rather
than above it.
[[cite:analytics-engineer-skills-tools@50:46=>Analytics Engineer Skills and Tools]]

## Macros and Reuse

Macros let teams reuse transformation logic instead of copying SQL across
models. Perez Mola compares dbt macros to user-defined functions in SQL
systems. Her example is practical: standardizing city names or similar repeated
cleanup logic across tables.
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

Macros remove repeated transformation code, but they don't eliminate the need
for clear modeling. Maksimovic's dbt migration story keeps the focus on table
design and transformation layers. dbt can package reusable logic, but the team
still has to decide the model grain. It also has to define business entities
and metrics
([[Metrics]],
[[Product Analytics]]).

## Orchestration Boundary

dbt builds a model DAG, but that doesn't make it the whole orchestrator for a
data platform. Perez Mola notes that dbt Cloud can schedule runs. Kwong places
Airflow around the broader flow of ingestion and transformation.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

Tuli brings the same boundary from her Airflow and pipeline background. Modern
data pipelines still need orchestration, ingestion, and staging. They also need
ordering guarantees and recovery outside the transformation project.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

Use [[Apache Airflow]] for the
orchestration-specific tool discussion. In a typical warehouse stack, Airflow
or another orchestrator coordinates extract-load jobs and dbt runs. It also
coordinates checks and downstream syncs. dbt owns the transformation graph and
model tests. The orchestrator owns when jobs run, how retries happen, and how
the end-to-end [[data-pipelines=>data pipeline]]
recovers.

## Tool Identity and Alternatives

Guests agree that dbt made SQL transformation more engineerable, but they don't
treat it as the whole discipline.

Perez Mola links dbt closely to the rise of analytics engineering.
[[cite:analytics-engineer-skills-tools@30:06=>Analytics Engineer Skills and Tools]]
She presents it as the everyday tool for modeling, tests, DAGs, and docs.
Maksimovic shows how learning dbt can anchor a career move from business or
marketing work into analytics engineering. That path still requires SQL, BI,
product context, and modeling practice.

See
[[Marketing to Analytics Engineering]]
for that transition path. Analysts using dbt as the bridge into model ownership
can also use the
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]].

Perafan is more careful about tool identity.
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]
dbt helps teams practice analytics engineering. dbt alone doesn't make
someone an analytics engineer. Tuli separates dbt from ingestion and
execution-engine concerns. Kwong situates it inside ELT and the modern stack.

[[person:adrianbrudaru=>Adrian Brudaru]] adds the 2025
tooling perspective in.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
He credits dbt with changing how people think about data engineering by
reducing boilerplate and improving project quality. He also names SQLMesh as
an alternative and argues for requirements-led tool selection.

SQLMesh belongs in the comparison because it competes around the same
engineering surface as dbt. That surface includes SQL transformation projects,
quality, and model workflow. The evidence doesn't make SQLMesh a universal
replacement for dbt. It marks a healthy alternative when a team wants to revisit
how its transformation project is planned and executed.
[[cite:trends-in-modern-data-engineering@31:29=>Modern Data Engineering Trends]]

dbt is influential, but teams still choose storage layers and catalogs around
it. They also choose orchestration and observability tools. Use
[[Data Warehouse vs Data Lakehouse]]
for the warehouse and lakehouse boundary.

## dbt Fit

Use dbt when the main problem is maintaining warehouse-side SQL models with
clear dependencies and repeatable runs. It's a strong fit for analytics
engineering teams that need reviews, tests, and documentation. Those teams
also need trusted marts, shared metrics, and BI-ready tables. dbt helps
transformation logic survive beyond one analyst's query.
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]][[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]

Don't expect dbt to solve every data-platform problem. Teams still need
separate design choices for ingestion, orchestration, and deep profiling. They
also need observability, streaming, source ownership, and warehouse cost
control.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]][[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

Perez Mola's workflow walkthrough and Kwong's ELT map show the same boundary.
So do Tuli's pipeline boundary, Perafan's role definition, Bergh's DataOps
discussion, and Brudaru's tool-selection advice. dbt improves the
transformation layer. Reliable analytics still depends on the surrounding data
platform and team practices.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]][[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]
