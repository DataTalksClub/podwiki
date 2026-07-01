---
layout: article
title: "Data Engineer Roadmap: From Fundamentals to Job-Ready Projects"
keyword: "data engineer roadmap"
summary: "A practical, podcast-backed data engineer roadmap from SQL and Python fundamentals to pipelines, orchestration, DataOps, portfolio projects, and interviews."
search_intent: "People searching for a data engineer roadmap want a practical sequence of skills, projects, tools, and interview preparation that can turn study into job-ready proof."
related_wiki:
  - Data Engineer Role
  - Data Engineering Roadmap
  - Data Engineering Portfolio Projects
  - Data Engineering
  - Data Pipelines
  - Data Quality and Observability
  - DataOps
  - Modern Data Stack
  - Job Search
---

A useful data engineer roadmap starts with the work a data engineer owns. Data
engineers move data from source systems into trusted datasets that other people
can use. That means SQL and Python first. After that, learn ingestion and
storage.

The next layer is modeling and orchestration. The final layer is quality
checks, documentation, cloud basics, and interview-ready projects.

The DataTalks.Club podcast archive is consistent on this point. In
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) names the junior core at
23:35: Python and SQL, plus cloud fundamentals and orchestration. At 38:05 and
56:46, he explains why a beginner path can focus on Python and SQL while
postponing Spark, Kafka, and Kubernetes. In
[Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) gives the same
modern version at 41:06. Learn SQL and Python, capture business requirements,
and build a portfolio before chasing a vendor checklist.

Use this article as the keyword-focused path, and use
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
for the archive-level reference.
For the role scope, start with
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}) and
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}).

## Start With The Role

Before choosing tools, decide which slice of data engineering you're trying to
prove.

A junior roadmap should show four abilities:

- ingest data and preserve raw records
- transform and model data with SQL
- run the workflow repeatedly
- explain how consumers can trust the output

That role boundary matters because "data engineer" can mean different things.
In
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) separates
platform data engineering from product-facing data work around 11:54. Later, at
42:08, he describes a tougher market for junior roles and recommends reusing
existing domain experience rather than applying blindly to every data title.

That role split gives the roadmap a practical target.

Match the path to your starting point:

- If you're closer to analytics, build toward modeled tables, marts, data
  quality, and stakeholder trust.
- If you're closer to software or DevOps, build toward ingestion,
  orchestration, testing, cloud deployment, and platform operations.

Use
[Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
and [Job Search]({{ '/wiki/job-search/' | relative_url }}) to connect the
roadmap to your background.

## Stage 1: SQL, Python, And Modeling

Start with SQL, Python, and basic data modeling. These skills make you useful
before you own a warehouse, lakehouse, streaming system, or platform.

For SQL, practice:

- joins and aggregations
- common table expressions
- window functions
- table grain and primary keys
- slowly changing attributes
- validation queries

Jeff Katz makes this concrete in
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}):
at 44:21 he recommends SQL depth beyond joins and aggregates, including window
functions. At 45:14, he highlights data modeling practice such as OLTP versus
OLAP.

For Python, practice:

- reading files and calling APIs
- handling pagination and configuration
- retrying failed requests
- isolating bad records
- writing data into storage

Code readability matters in
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}).
Jeff warns at 1:49 that many projects list tools while showing too little
Python and SQL. At 2:22, he asks for small functions and useful names. He also
asks for targeted classes and tests.

The modeling layer turns data movement into data engineering. Name the grain of
each table, separate raw and modeled layers, and write a data dictionary for
final tables. For deeper context, use
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }}), and
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

## Stage 2: Build One End-To-End Batch Pipeline

After the fundamentals, build one small pipeline that moves data from a source
to a trusted output. This is the center of the data engineer roadmap because it
turns study into evidence.

The first pipeline should include:

- a source such as an API, file drop, database export, public dataset, event log,
  or simulated change-data feed
- raw storage that keeps source records before transformation
- staging tables that clean types, rename fields, deduplicate records, and keep
  load metadata
- modeled tables with joins, grain, business rules, aggregations, and windows
- a serving output for a named consumer such as an analyst, dashboard, ML
  training job, product workflow, or operational alert
- a command, script, scheduler, or simple orchestrator so the pipeline doesn't
  depend on notebook clicks
- documentation for setup, tables, quality checks, failure modes, and recovery

This project should show substantial SQL and Python, not only a stack diagram.
In
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
Jeff connects portfolio work to Python and SQL at 1:20. He also covers Docker,
Airflow, and warehouse fundamentals there. At 2:46, he says personal projects
and open-source contributions help create credible proof. Use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
as the review standard, and use
[End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
for a single-project blueprint.

## Stage 3: Choose Storage, ETL, And ELT Deliberately

Once the first pipeline runs, learn where data should land and why. Start with
storage and transformation patterns before memorizing product names.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the clearest
archive introduction in
[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
At 3:46 she explains ETL, at 7:57 she covers ELT's flexibility, and at 10:00
she discusses transformations from type casting to SQL joins. At 15:30 and
17:55, she distinguishes data marts, warehouses, and raw ingestion layers. At
27:39, she frames lake versus warehouse choices as architecture decisions.

Your project doesn't need a full platform, but it should explain its storage
choice:

- what stays raw and what gets transformed
- whether the final output lives in a warehouse, lake, lakehouse, local
  analytical database, or object store
- who queries the final data
- how you rerun or backfill if the source changes
- what would become expensive, slow, or hard to maintain at larger scale

For deeper reading, connect this stage to
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) and
[ELT]({{ '/wiki/elt/' | relative_url }}). Then add
[Data Lake]({{ '/wiki/data-lake/' | relative_url }}),
[Data Warehouse vs Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}),
and [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}).

## Stage 4: Add Orchestration, Quality, And DataOps

A data engineer roadmap is incomplete without repeatable operations. A pipeline
has to run in the right order, rerun safely, and tell you when the data is
wrong.

For orchestration, learn:

- schedules and dependencies
- retries and failure states
- backfills and reruns
- logs and alerts
- idempotent writes
- parameters and configuration

Natalie Kwong describes Airflow's orchestration role at 30:59 in
[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) goes deeper
in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}):
at 30:34 he breaks a data platform into storage, compute, and workflow engine.
At 46:52, he discusses data quality measurements and schema automation as part
of DataOps maturity.
Use the
[Airflow Docker Compose how-to]({{ '/how-tos/airflow-docker-compose/' | relative_url }})
when you need a local Airflow project that a reviewer can start, break, look
at, and rerun.

For quality checks, protect the consumer:

- freshness: the latest batch arrived when expected
- volume: row counts stay within a reasonable range
- schema: required columns and types are present
- uniqueness: keys don't duplicate unexpectedly
- nulls: required fields are populated
- accepted values: categorical fields stay within expected values
- referential integrity: facts join to dimensions as expected
- distribution: important measures don't shift without explanation

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) adds the
operational standard in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
At 6:42, he ties DataOps to error reduction, deployment cycle time, and team
productivity.

At 33:47 and 48:25, he uses practical reliability tools:

- version control
- automated tests
- CI/CD
- dbt tests
- Great Expectations
- SQL tests

Use [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}) for the
deeper version.

## Stage 5: Make The Portfolio Interview-Ready

By this point, you should have one complete pipeline and one smaller project
that proves a specific skill. The next step isn't adding another tool. It's
making the work reviewable.

An interview-ready data engineering portfolio should include:

- a README that explains the consumer, source, architecture, setup, and
  tradeoffs
- a command or documented path to run the pipeline
- visible SQL and Python depth
- tests for code and data
- logs, run metadata, or screenshots from successful runs
- table descriptions and table grain
- one documented failure scenario
- one backfill or rerun story
- a short explanation of what you would simplify or change next

This matches the hiring advice across the archive. Jeff Katz's
[job-prep episode]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
asks for readable code and tests at 2:22. Slawomir Tulski's
[2026 career episode]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
pushes portfolio framing at 57:35 and suggests a small end-to-end platform at
1:04:42, even if the implementation is simple. In
[Scale Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) recommends writing
and open-source work at 46:44. Blogs and videos can also create feedback and
make work visible.

Build projects in this order:

1. Reliable analytical model: raw data, cleaned staging tables, modeled marts,
   and tests.
2. Scheduled ingestion pipeline: API or file ingestion, raw storage,
   transformations, checks, and a runbook.
3. Backfill exercise: replay older data and document what downstream users see.
4. Schema-change exercise: handle a renamed, missing, or newly added field.
5. Capstone pipeline: ingestion, transformation, orchestration, quality,
   documentation, and a named consumer.

Keep one project small enough to finish and one project deep enough to defend.
For project review, use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
[Documentation]({{ '/wiki/documentation/' | relative_url }}), and
[CV Screening]({{ '/wiki/cv-screening/' | relative_url }}).

## Stage 6: Prepare For Interviews While You Build

Interview preparation should follow the same roadmap. Don't study interviews
as a separate universe from your projects. Your projects should give you
examples for most interview questions.

Prepare for these areas:

- SQL screens: joins, windows, aggregations, deduplication, ranking, date logic,
  and validation queries
- Python screens: file parsing, API calls, data structures, small functions,
  error handling, and tests
- pipeline design: source, raw storage, transformation, orchestration, quality,
  serving, and recovery
- data modeling: table grain, fact and dimension thinking, slowly changing
  attributes, marts, and warehouse concepts
- failure scenarios: late data, duplicate records, schema changes, partial
  loads, broken dependencies, and bad joins
- cloud and tooling: storage, permissions, schedulers, Docker, warehouses, and
  cost awareness
- project walkthroughs: tradeoffs, bugs, rejected designs, and future
  improvements

In
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
Jeff says technical interviews include SQL, Python, and take-home work at 7:46.
In
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
he also discusses SQL tests and on-site expectations at 48:00. That means the
roadmap should end with practice under constraints. Explain your pipeline out
loud, redesign one part on a whiteboard, and solve SQL without searching for
every syntax detail. Then write a small extractor or validation function from
scratch.

## Stage 7: Add Advanced Tools Only When They Solve A Constraint

Add advanced tools when the project or target role needs them.

Add advanced tools only when the constraint is real:

- Add Spark for distributed processing, large-data transformations, or
  Spark-specific job experience.
- Add Kafka when delayed answers lose value and event ordering, replay, or late
  events become central.
- Add Kubernetes when deployment and platform ownership are part of the role.
- Add Iceberg, Delta Lake, or a catalog when lakehouse metadata and schema
  evolution become the problem.
- Add catalog and lineage tooling when discovery, ownership, and governance
  become the problem.

The archive repeatedly warns against tool-first roadmaps. Adrian Brudaru's
[Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
covers Iceberg at 18:17 and DuckDB at 25:58. He covers orchestration choices at
35:37 and streaming patterns at 51:19. He still returns to requirements and
portfolio work at 41:06. At 44:42, he returns to vendor caution.

Slawomir Tulski makes the same point in
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).
At 30:56, he warns about over-engineered platforms. At 38:01, he says Kafka
belongs where real-time needs justify it.

The practical sequence is:

1. Build the batch version.
2. Add tests and documentation.
3. Identify the bottleneck or requirement.
4. Add the advanced tool that addresses it.
5. Explain what became easier and what became harder.

This keeps the roadmap connected to
[Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}).

## A Practical 12-Week Roadmap

Use this as a pacing guide, not a promise. Move faster if you already know SQL,
Python, or backend engineering, and move slower if you're learning programming
from scratch. The sequence follows the podcast evidence above. Fundamentals
come before tool breadth, one finished pipeline comes before specialization,
and portfolio proof comes before certificate collecting.

Weeks 1-2 cover SQL and modeling through joins, windows, aggregations, and
CTEs. Then add table grain, OLTP versus OLAP, and validation queries. Jeff
Katz's SQL and modeling advice in
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
is the benchmark for this stage.

Weeks 3-4 cover Python ingestion through scripts that call an API or read files.
Handle bad records, configuration, retries, and raw data preservation. Use
Jeff's code-quality guidance from
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
as the review bar.

Weeks 5-6 cover storage in a warehouse, lake, or local analytical database.
Create raw, staging, modeled, and serving layers. Add a data dictionary and
document table grain. Natalie Kwong's
[ETL vs ELT episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
is the stack vocabulary for this stage.

Weeks 7-8 cover orchestration through a command or scheduler with dependencies,
retries, logs, and rerun behavior. Connect the work to
[Apache Airflow: Workflow Orchestration for Data Pipelines]({{ '/wiki/orchestration/' | relative_url }})
and Lars Albertsson's DataOps discussion of workflow engines in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

Weeks 9-10 cover quality and failures through freshness, volume, schema, and
null checks. They should also cover uniqueness, accepted values, and business
rules. Then break the pipeline on purpose and write recovery notes.
Christopher Bergh's
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
is the reliability model for this stage.

Weeks 11-12 cover portfolio and interviews. Clean the README, document setup,
and add a project walkthrough. Practice SQL, Python, and take-home scenarios.
Link your project story to the
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}) you're
targeting, then use [Job Search]({{ '/wiki/job-search/' | relative_url }}) to
turn the project into applications.

After that, choose one specialization based on your target role:

- analytics-heavy modeling
- platform engineering
- streaming
- lakehouse formats
- data governance
- product data engineering
- AI-ready data pipelines

## Roadmap Checklist

You're ready to apply for junior data engineering roles when you can do most
of this without following a tutorial step by step:

- write SQL for joins, windows, aggregations, and validation checks
- write Python that extracts, validates, and loads data
- explain raw, staging, modeled, and serving layers
- design a table with a clear grain
- run a pipeline without manual notebook steps
- add basic orchestration, logs, and rerun behavior
- test freshness, volume, schema, nulls, uniqueness, and business rules
- document setup, data dictionaries, tradeoffs, and recovery steps
- explain warehouse, lake, and lakehouse tradeoffs at a practical level
- discuss one cloud storage or warehouse path
- walk through a portfolio project under interview questioning
- know when not to use Spark or streaming systems

For the full topic map, continue with
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
and [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}). Then use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}).
