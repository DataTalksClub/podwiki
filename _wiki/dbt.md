---
layout: wiki
title: "dbt"
summary: "How DataTalks.Club guests describe dbt as warehouse-side SQL transformation plus an engineering workflow for analytics models, tests, documentation, DAGs, and reviewed changes."
related:
  - Analytics Engineering
  - Modern Data Stack
  - ELT
  - Data Warehouse
  - Data Quality and Observability
  - DataOps
---

DataTalks.Club guests use dbt as the clearest example of
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
in practice. Teams write SQL models, run them in a
[data warehouse]({{ '/wiki/data-warehouse/' | relative_url }}), and treat the
transformation layer as reviewed code with tests. The shift isn't only from
ETL to [ELT]({{ '/wiki/elt/' | relative_url }}). Analysts and analytics
engineers move from isolated SQL queries to a maintained project.

That project
tracks dependencies and version control. It also keeps tests, documentation,
and macros with the SQL models.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
gives the most direct explanation in
[Analytics Engineer Skills and Tools at 6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She describes dbt as the tool her team uses for modeling data after it arrives
in Snowflake, alongside Looker and ingestion tooling. dbt keeps SQL files in a
code workflow and manages model dependencies. It builds a DAG, runs tests, and
exposes documentation. DataTalks.Club therefore treats dbt as a practical
bridge between analytics work and software engineering habits.
Rui Machado and Helder Russa's
[Analytics Engineering with SQL and DBT]({{ '/books/20231106-analytics-engineering-with-sql-and-dbt/' | relative_url }})
covers the same warehouse-side SQL modeling, testing, and DAG-based project
workflow that Victoria describes here.

## Warehouse-Side Transformation

dbt belongs most naturally to warehouse-side transformation in the
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) discussion.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains that
move in
[ETL vs ELT and the Modern Data Stack at 7:57-12:39]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
She contrasts transforming before load with loading first and transforming in
analytical storage. ELT gives analysts and analytics engineers more room to
adjust business logic after raw data is available.

dbt fits that ELT flow because it doesn't replace the warehouse. It compiles
and runs transformation logic against warehouses such as Snowflake and BigQuery.
Redshift fits the same warehouse-backed model. Kwong places dbt next to ingestion tools and
data marts. She also places it near orchestration, CDC, and reverse data flows
([Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})).

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) draws the same
boundary from the pipeline side in
[Modern Data Pipeline Architecture at 10:48 and 24:57]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Her Upsolver comparison separates ingestion-focused pipeline authoring from
dbt-style SQL modeling. dbt can author transformations, but another system
still loads data, handles streaming or ordering guarantees, and may provide the
execution engine.

## Analytics Engineering Workflow

Perez Mola centers dbt on workflow because SQL models live in files. Teams can
review changes in Git and see how a model changed over time. dbt resolves
dependencies between models and renders the DAG. Teams can see what a change
will affect before it reaches dashboards or downstream tables
([Analytics Engineer Skills and Tools at 6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows the
implementation side in
[From Marketing to Analytics Engineering at 18:34-22:08]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
His transition from marketing into BI and analytics engineering included a dbt
migration and data modeling. It also included Looker work, product analytics,
and A/B testing support.

The dbt project wasn't a side tool. It was where reusable business logic moved
out of scattered reports and into modeled transformation layers. His later
discussion of wide and narrow tables at 30:28 keeps the focus on model design,
not tool adoption alone.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
pushes the same point in
[Foundations of the Analytics Engineer Role at 11:03 and 49:50-55:42]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
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
source data shouldn't silently flow into the modeled layer
([Analytics Engineer Skills and Tools at 38:53]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Those tests put dbt close to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
dbt can catch assumptions about required fields and duplicate identifiers. It
can also check accepted ranges, valid city names, and relationships. It can't
prove that every business number is correct.

Perez Mola is explicit that data quality remains ongoing work. Teams add tests
after they learn from mismatches.

Perafan broadens the testing conversation. He contrasts manual dashboard
checking with automated tests for SQL logic and data assumptions.

He describes generic tests and singular SQL tests as ways to make analytics
work safer. Unit-test style checks belong in the same testing conversation
([Foundations of the Analytics Engineer Role at 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
His argument lines up with
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) and
[DataOps]({{ '/wiki/dataops/' | relative_url }}): tests should run before bad
changes reach consumers, not only after a stakeholder reports a broken metric.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) puts the
same testing habit inside a broader DataOps operating model in
[Mastering DataOps at 33:47 and 48:25]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
He names version control and automated tests among the ways data teams reduce
fragile releases. CI/CD, SQL tests, and dbt belong in that same toolkit.

## Documentation and Lineage

dbt documentation is part of the workflow, not an afterthought. Perez Mola
describes schema YAML files where teams document models and fields. Teams can
also record tags and custom metadata.

dbt docs can show model code, generated documentation, and dependencies. Before
changing a table, an analytics engineer can look at what depends on it
([Analytics Engineer Skills and Tools at 50:46]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Perez Mola also marks a limit by distinguishing documentation from data
profiling. dbt can document models and expose lineage, but it isn't the main
tool for deep profiling or full observability. She mentions profiling and
observability tools such as Datafold and Monte Carlo as adjacent options. dbt
therefore sits inside the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}) rather
than above it.

## Macros and Reuse

Macros let teams reuse transformation logic instead of copying SQL across
models. Perez Mola compares dbt macros to user-defined functions in SQL
systems. Her example is practical: standardizing city names or similar repeated
cleanup logic across tables
([Analytics Engineer Skills and Tools at 36:44]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Macros remove repeated transformation code, but they don't eliminate the need
for clear modeling. Maksimovic's dbt migration story keeps the focus on table
design and transformation layers. dbt can package reusable logic, but the team
still has to decide the model grain. It also has to define business entities
and metrics
([Metrics]({{ '/wiki/metrics/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

## Orchestration Boundary

dbt builds a model DAG, but that doesn't make it the whole orchestrator for a
data platform. Perez Mola notes that dbt Cloud can schedule runs. Kwong places
Airflow around the broader flow of ingestion and transformation at
30:59-31:31 in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).

Tuli brings the same boundary from her Airflow and pipeline background. Modern
data pipelines still need orchestration, ingestion, and staging. They also need
ordering guarantees and recovery outside the transformation project
([Modern Data Pipeline Architecture at 7:08-13:25 and 37:10]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

Use [Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}) for the
orchestration-specific tool discussion. In a typical warehouse stack, Airflow
or another orchestrator coordinates extract-load jobs and dbt runs. It also
coordinates checks and downstream syncs. dbt owns the transformation graph and
model tests. The orchestrator owns when jobs run, how retries happen, and how
the end-to-end [data pipeline]({{ '/wiki/data-pipelines/' | relative_url }})
recovers.

## Tool Identity and Alternatives

Guests agree that dbt made SQL transformation more engineerable, but they don't
treat it as the whole discipline.

Perez Mola links dbt closely to the rise of analytics engineering at 30:06 in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She presents it as the everyday tool for modeling, tests, DAGs, and docs.
Maksimovic shows how learning dbt can anchor a career move from business or
marketing work into analytics engineering. That path still requires SQL, BI,
product context, and modeling practice.

See
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
for that transition path. Analysts using dbt as the bridge into model ownership
can also use the
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }}).

Perafan is more careful about tool identity. At 49:50-55:42 in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
he says dbt helps teams practice analytics engineering. dbt alone doesn't make
someone an analytics engineer. Tuli separates dbt from ingestion and
execution-engine concerns. Kwong situates it inside ELT and the modern stack.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) adds the 2025
tooling perspective in
[Modern Data Engineering Trends at 31:29 and 44:42]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
He credits dbt with changing how people think about data engineering by
reducing boilerplate and improving project quality. He also names SQLMesh as
an alternative and argues for requirements-led tool selection.

dbt is influential, but teams still choose storage layers and catalogs around
it. They also choose orchestration and observability tools. Use
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
for the warehouse and lakehouse boundary.

## dbt Fit

Use dbt when the main problem is maintaining warehouse-side SQL models with
clear dependencies and repeatable runs. It's a strong fit for analytics
engineering teams that need reviews, tests, and documentation. Those teams
also need trusted marts, shared metrics, and BI-ready tables. dbt helps
transformation logic survive beyond one analyst's query.

Don't expect dbt to solve every data-platform problem. Teams still need
separate design choices for ingestion, orchestration, and deep profiling. They
also need observability, streaming, source ownership, and warehouse cost
control.

Perez Mola's workflow walkthrough and Kwong's ELT map show the same boundary.
So do Tuli's pipeline boundary, Perafan's role definition, Bergh's DataOps
discussion, and Brudaru's tool-selection advice. dbt improves the
transformation layer. Reliable analytics still depends on the surrounding data
platform and team practices.
