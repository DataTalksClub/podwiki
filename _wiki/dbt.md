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

dbt is the archive's clearest example of
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
in practice. Teams write SQL models, run them in a
[data warehouse]({{ '/wiki/data-warehouse/' | relative_url }}), and treat the
transformation layer as reviewed, tested code. The important shift isn't only
from ETL to [ELT]({{ '/wiki/elt/' | relative_url }}). It's from isolated SQL
queries to a maintained project with dependencies and version control. The
same project includes tests, documentation, and macros.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
gives the most direct explanation in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She describes dbt as the tool her team uses for modeling data after it arrives
in Snowflake, alongside Looker and ingestion tooling. In her walkthrough, dbt
keeps SQL files in a code workflow and manages model dependencies. It also
builds a DAG, runs tests, and exposes documentation. That makes it a practical
bridge between analytics work and software engineering habits.

## Warehouse-Side Transformation

dbt belongs most naturally to warehouse-side transformation in the
[ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }}) discussion.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains that
move in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
She contrasts transforming before load with loading first and transforming in
analytical storage. That approach gives analysts and analytics engineers more
room to adjust business logic after raw data is available.

dbt fits that ELT flow because it doesn't replace the warehouse. It compiles
and runs transformation logic against systems such as Snowflake, BigQuery, or
Redshift. Kwong places dbt next to ingestion tools and data marts. She also
places it next to warehouses, orchestration, and CDC.

Reverse data flows belong to the same stack. The same boundary appears in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
where [Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) separates dbt
from ingestion-focused pipeline engines. In her Upsolver comparison, dbt can
author SQL transformations. Another system still loads data, handles streaming
or ordering concerns, and may provide the execution engine.

## Engineering Workflow

Perez Mola centers dbt on workflow because SQL models live in files. Teams can
review changes in Git and see how a model changed over time. dbt also resolves
dependencies between models. It renders the DAG so teams can see what a change
will affect before it reaches dashboards or downstream tables.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows the
implementation side in
[From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
His transition from marketing into BI and analytics engineering included a dbt
migration, data modeling, Looker work, and product analytics. It also included
A/B testing support. The dbt project wasn't a side tool. It was where reusable business
logic moved out of scattered reports and into modeled transformation layers.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
pushes the same point in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
He treats dbt as one way to put analytics engineering into practice, not as the
definition of the job. The craft is still translating business reality into
clean data systems. dbt helps when the team needs those systems to be tested,
reviewed, and repeatable.

## Tests and Quality

dbt tests turn data quality checks into project code. Perez Mola describes
standard checks such as non-null and uniqueness tests, plus custom SQL tests.
She also explains that a dbt test is a query: if the query returns failing
rows, dbt can warn or error. Her team checks sources before building dependent
models so bad source data doesn't silently flow into the modeled layer.

This is where dbt connects to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
dbt can catch assumptions about required fields and duplicate identifiers. It
can also check accepted ranges, valid city names, and relationships. It can't
prove that every business number is correct. Perez Mola is explicit that data
quality is ongoing work and that teams add tests after they learn from
mismatches.

Perafan broadens the testing conversation. He contrasts manual dashboard
checking with automated tests for SQL logic and data assumptions. He describes
generic tests, singular SQL tests, and unit-test style checks as ways to make
analytics work safer. His argument lines up with
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) and
[DataOps]({{ '/wiki/dataops/' | relative_url }}): tests should run before bad
changes reach consumers, not only after a stakeholder reports a broken metric.

## Documentation and Lineage

dbt documentation is part of the workflow, not an afterthought. Perez Mola
describes schema YAML files where teams document models, fields, tags, and
custom metadata. dbt docs can show model code and generated documentation.
They also show dependencies, so an analytics engineer can look at what depends
on a table before changing it.

Perez Mola also marks a limit by distinguishing documentation from data
profiling. dbt can document models and expose lineage, but it isn't the main
tool for deep profiling or full observability. She mentions profiling and
observability tools such as Datafold and Monte Carlo as adjacent options. That
places dbt inside the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}) rather
than above it.

## Macros and Reuse

Macros let teams reuse transformation logic instead of copying SQL across
models. Perez Mola compares dbt macros to user-defined functions in SQL
systems. Her example is practical: standardizing city names or similar repeated
cleanup logic across tables.

Macros remove repeated transformation code, but they don't eliminate the need
for clear modeling. Maksimovic's dbt migration story keeps
the focus on table design and transformation layers. He also discusses the
choice between wide and narrow models. In other words, dbt can package reusable
logic, but the team still has to decide the model grain. It also has to decide
business entities and metrics.

## Orchestration Boundary

dbt builds a model DAG, but that doesn't make it the whole orchestrator for a
data platform. Perez Mola notes that dbt Cloud can schedule runs. Kwong places
Airflow around the broader flow of ingestion and transformation.

Tuli brings the same boundary from her Airflow and pipeline background. Modern
data pipelines still need orchestration, ingestion, and staging. They also need
ordering guarantees and recovery outside the transformation project.

Use [Apache Airflow]({{ '/wiki/orchestration/' | relative_url }}) for the
orchestration-specific tool discussion. In a typical warehouse stack, Airflow
or another orchestrator coordinates extract-load jobs and dbt runs. It also
coordinates checks and downstream syncs. dbt owns the transformation graph and
model tests.

The orchestrator owns when jobs run and how retries happen. It also owns how
the end-to-end
[data pipeline]({{ '/wiki/data-pipelines/' | relative_url }}) recovers.

## Guest Differences

Guests agree that dbt made SQL transformation more engineerable, but they don't
treat it as the whole discipline. Perez Mola links dbt closely to the rise of
analytics engineering. She presents it as the everyday tool for modeling,
tests, DAGs, and docs.

Maksimovic shows how learning dbt can anchor a career move from business or
marketing work into analytics engineering. That path also needs SQL, BI,
product context, and modeling practice. See
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
for that transition path. Analysts using dbt as the bridge into model ownership
can also use the
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }}).

Perafan is more careful about tool identity. dbt helps teams practice
analytics engineering, but dbt alone doesn't make someone an analytics
engineer. Tuli separates dbt from ingestion and execution-engine concerns.
Kwong situates it inside ELT and the modern stack.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
connects dbt tests to a broader [DataOps]({{ '/wiki/dataops/' | relative_url }})
operating model in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}):
tests should be automated and version-controlled. They should also stay close
to the data and run during development.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) adds the 2025
tooling perspective in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
He credits dbt with changing how people think about data engineering by
reducing boilerplate and improving project quality, while also noting
alternatives such as SQLMesh. His broader advice is requirements-led tool
selection.

dbt is influential, but teams still choose storage layers and catalog tools
around it. Use
[Data Warehouse vs Data Lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }})
for the warehouse and lakehouse boundary.

## Practical Takeaways

Use dbt when the main problem is maintaining warehouse-side SQL models with
clear dependencies and repeatable runs. It's a strong fit for analytics
engineering teams that need reviews, tests, and documentation. Those teams
also need trusted marts, shared metrics, and BI-ready tables. dbt helps
transformation logic survive beyond one analyst's query.

Don't expect dbt to solve every data-platform problem. Teams still need
separate design choices for ingestion, orchestration, and deep profiling. They
also need observability, streaming, source ownership, and warehouse cost
control. The archive's strongest dbt episodes all make the same distinction:
dbt improves the transformation layer. Reliable analytics still depends on the
surrounding data platform and team practices.
