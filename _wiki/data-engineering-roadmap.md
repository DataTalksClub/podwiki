---
layout: wiki
title: "Data Engineering Roadmap"
summary: "A podcast-backed roadmap for becoming useful as a data engineer: fundamentals, project sequence, platform judgment, role milestones, and when to stop studying and build."
related:
  - Data Engineering
  - Data Engineer Role
  - Data Engineering Portfolio Projects
  - Data Engineering Platforms
  - Data Pipelines
  - Modern Data Stack
  - DataOps
  - Data Quality and Observability
  - Analytics Engineering
  - Data Engineering Certification
---

A data engineering roadmap is a sequence for becoming useful with data before
becoming broad with tools. In the DataTalks.Club archive, you learn SQL and
Python first. Then you add data modeling, pipeline construction, and operating
habits. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) puts Python, SQL,
database concepts, and cloud basics before distributed systems in
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-40:42 and 56:46.

Use this roadmap as the practical path through
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}), not as a
catalog of [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }}).
For role scope, use [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}).
For proof of skill, use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}).

If you already work in analytics, use the
[Data Analyst to Data Engineer Roadmap]({{ '/roadmaps/data-analyst-to-data-engineer/' | relative_url }}).
If you already work in data science, use the
[Data Scientist to Data Engineer Roadmap]({{ '/roadmaps/data-scientist-to-data-engineer/' | relative_url }}).
Both pages translate existing skills into the data engineering path.

For operating practice, use [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) makes the same
roadmap point from the modern-stack side. Beginners should learn fundamentals
and gather requirements. They should build projects before surveying every
orchestrator or table format
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
41:06-44:42).

[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) adds the
senior constraint. Data engineers need cost-aware tool judgment instead of
defaulting to real-time or cloud-heavy systems
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-38:01). Use
[FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
when the roadmap moves from learning tools to operating shared cloud spend.

## Common Definition

Across the archive, guests converge on one definition. You should become able
to turn raw inputs into trusted, recoverable data products. Katz starts that
path with SQL and Python. He then adds database concepts such as OLTP versus
OLAP and modeling practice
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-26:40 and 44:21-45:14). His job-prep discussion repeats the same hiring
signal.

Candidates need Python, SQL, and warehouse familiarity. They should also
practice Docker, Airflow, and interviews before they chase a larger platform
stack
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-11:24).

After fundamentals you move into [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
and the [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) covers
ingestion in one modern-stack discussion. She connects that work to warehouses
and marts. She compares ETL with ELT. She also covers orchestration, CDC, and
schema evolution in
[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
3:46-17:55 and 30:59-49:32.

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
describes an end-to-end pipeline that moves from ingestion and orchestration
into modeled marts and dashboards. She also covers production ML handoffs
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
10:48-18:44 and 24:57-44:57).

At senior level, you stop adding tools by default and start practicing
architecture judgment. You learn when a simple batch pipeline is enough and
when streaming is worth the burden. You also learn when platform conventions
help multiple teams move faster.

[Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }}) discusses that
team-scale platform problem in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
12:30-23:26. Tulski ties the same decision to business value and cost. He also
stresses operational burden in
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-38:01.

## Guest Differences

Guests agree on SQL, Python, and reliable pipelines. They differ on how
quickly the roadmap should move into platform work.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) keeps the beginner
curriculum narrow and emphasizes interviewable fundamentals. He starts with
Python, SQL, and cloud basics. He then uses OLTP versus OLAP and modeling to
explain why a junior curriculum can skip distributed platform tools.
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-40:42 and
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-7:46).

[Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }}) starts from a
scale-up constraint where the roadmap needs [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
senior hiring, and Kafka data contracts. A fast-growing company can't have
every team reinvent data plumbing
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
5:41-23:26 and 50:17-54:31). That belongs later in a learner roadmap unless
the learner already works in a team with those scale problems.

[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) separates
platform data engineering from product data engineering. Platform engineers
own infrastructure and shared systems. Product-facing data engineers sit closer
to domain models, data products, and stakeholders
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
11:54-17:29).

That split changes the roadmap. For a platform role, go deeper into cloud and
orchestration. Add
[cost]({{ '/wiki/finops-for-data-engineers/' | relative_url }}) and
reliability. For product data engineering, focus on modeling and requirements.
Pair that work with
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
and data product ownership.

## Courses, Bootcamps, and Training

Courses, bootcamps, and company training are roadmap inputs. They help when
they create deadlines, feedback, reviewable labs, and a project that another
engineer can run. They're weak when they replace the roadmap with a tool list
or certificate signaling.

Katz gives the curriculum test in
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}):
Python and SQL come first. Cloud fundamentals and orchestration come next. He
later describes the beginner balance as mostly Python and SQL, with tools and
cloud basics added around that core (23:35-40:42 and 56:46).

Use structured learning to move through the same stages as this roadmap. A
useful course starts with SQL, Python, and data modeling. It then makes the
learner ingest data and keep raw data. It also makes the learner transform
data into modeled tables, schedule the work, test it, and document a consumer.

The first useful project should include a real failure mode. Ingest data from
an API, database dump, or file source. Event logs and CDC simulations work too.

Store raw data before transforming it, then create staged and modeled tables
with a clear grain. Add tests for freshness, schema, row counts, and nulls.
Uniqueness and business-rule checks belong there too.

Schedule the work and add a runbook for late data and failed jobs. Name the
consumer who can trust the output.

Kwong's modern-stack episode grounds that sequence through ETL, ELT, marts,
and orchestration. She also adds CDC and schema evolution
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
3:46-17:55 and 30:59-49:32). Tuli's pipeline episode adds the same
source-to-dashboard and source-to-ML handoff
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
10:48-18:44 and 32:57-44:57).

Bootcamps and cohorts are most useful for career changers when they add
pressure, feedback, interview practice, and customization. [Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }})
shows the learner side in
[Gloria's data engineering job episode]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}).
Her path included a bootcamp, a four-month search, volunteer practice, and
tracked applications.

She connects Python and Docker to job readiness, with Airflow, AWS, and
networking helping too. Her Twitter data pipeline capstone used Docker
containers and a Slack bot. Custom projects stand out more than repeated course
projects (16:14-18:21, 36:20-37:25, and 50:15-53:34).

That makes the project the main output of any training path. Katz's job-prep
episode warns that many portfolio projects list tools while showing too little
Python and SQL. He asks for cleaner code with small functions and descriptive
names. He also asks for useful classes and tests
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:49-2:46).

A course project should therefore become a
[Data Engineering Portfolio Project]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}).
The project needs one realistic source, raw storage, modeled tables, and
orchestration.
It also needs data quality checks, setup instructions, a runbook, and at least
one handled failure mode.

The same rule applies to course catalogs such as
[Data Engineering Zoomcamp](https://datatalks.club/blog/data-engineering-zoomcamp.html).
The DataTalks.Club course discussion frames the Zoomcamp portfolio as free
project-based learning
([Inside Scaling DataTalks.Club]({{ '/podcasts/datatalksclub-scaling-and-free-courses/' | relative_url }})
5:07-9:22 and 12:04-16:27). A learner should still finish with a pipeline they
can explain instead of only a completed syllabus.

Brudaru gives the modern-stack version of that boundary. Beginners should
combine SQL, Python, requirements gathering, and portfolio work. They should
do that before chasing every orchestrator, table format, or vendor trend
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
41:06-44:42).

## Stage 1: Query and Model Useful Data

Start with analytical SQL, Python, and database concepts. Katz's curriculum
puts Python, SQL, and cloud fundamentals at the center. He also uses OLTP
versus OLAP and sample databases for data modeling
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-26:40 and 44:21-45:14). His job-prep episode adds code quality, tests,
and common interview formats
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-2:22 and 7:46-11:24).

Practice by turning raw product data or public data into tables with documented
grain. Join source data, handle nulls, and explain why a dashboard number
changes when the grain changes. This connects the roadmap to
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
because both guests place marts and BI-facing tables after ingestion and
transformation.
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
12:39-15:30 and
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
39:23-43:05).

## Stage 2: Build an End-to-End Batch Pipeline

Build one batch pipeline before adding streaming or distributed processing. A
good first pipeline extracts from an API or file source and stores raw data. It
then transforms the data into modeled tables, runs on a schedule, and documents
the table for its consumer.

Kwong's modern stack episode connects ETL and ELT to raw ingestion,
transformation, and marts. It also covers orchestration and schema evolution
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
3:46-17:55 and 30:59-49:32). Tuli's pipeline architecture episode adds
ingestion and declarative transformations. It also covers marts, dashboards, and
production ML handoffs
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
10:48-18:44 and 32:57-44:57).

Keep the first stack small enough to finish. Use Python extraction, local
storage, one query engine, and one scheduler. Brudaru's trends episode supports
simple, requirement-led tool choice. It also shows where DuckDB, Iceberg, and
open table formats fit when the project grows
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
18:17-35:37 and 41:06-44:42).

## Stage 3: Operate the Pipeline Like a Product

Add tests, CI/CD, observability, and runbooks as soon as the pipeline
has a consumer. [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
connects DataOps to automation and CI/CD. He also ties it to regression tests,
realistic test data, and production monitoring
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
15:52-18:46 and 30:55-54:05 and
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
33:47-51:21).

Break the pipeline on purpose. Change a schema, delay an input, duplicate
records, and backfill old data. Then document how you detect the issue and who
gets notified. Document what gets rolled back and how downstream tables recover.
That work connects [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
to [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}).

## Stage 4: Choose Platform Patterns Deliberately

Learn storage and processing as tradeoffs, and treat orchestration and
streaming the same way. Don't treat managed services as badges.

Kwong's episode compares lakes, warehouses, and marts. She also covers reverse
flows
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
19:50-35:42). Brudaru's episode adds table formats, DuckDB, and metadata. It
also covers lineage and orchestration options
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
18:17-35:37 and 49:42-51:19).

Treat streaming as a constraint-driven choice. Ouazza discusses Kafka schemas
and data contracts in scale-up platform work
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
23:26). Tulski warns against real-time systems as default architecture and
ties tool choice to business value, cost, and operational burden
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
30:56-38:01).

## Stage 5: Specialize by Constraint

Choose a constraint after you can build and operate a basic pipeline:

- Platform data engineering uses shared infrastructure and self-service
  conventions, so pair [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  with [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).
  Tulski and Ouazza provide the episode evidence
  ([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
  11:54-17:29 and
  [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
  12:30-17:22).
- Product data engineering covers domain models and stakeholder requirements.
  Pair [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
  with Tuli's modeling and marts discussion
  ([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
  39:23-43:05).
- Reliability work centers on tests and recovery playbooks. Read
  Bergh's DataOps episodes with [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  ([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
  15:52-18:46 and 30:55-54:05).
- Streaming and event systems go deep on latency and contracts. Use Ouazza for
  Kafka practices and Brudaru for stream processing tradeoffs
  ([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
  23:26 and
  [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
  51:19).
- AI-ready data engineering centers on metadata and semantic layers. Brudaru
  frames AI integration as a modern data engineering trend, but still anchors
  the roadmap in requirements and quality
  ([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
  16:40 and 38:02-44:42).

## Project Sequence

Build projects in this order so each one adds a new responsibility instead of a
new tool list:

1. Reliable analytical model: ingest a small raw dataset and define entities,
   then produce staging and mart tables with SQL tests. Katz's SQL and data
   modeling sections ground this project
   ([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
   44:21-45:14 and
   [Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
   9:41).
2. Scheduled ingestion pipeline: pull from an API or file source and preserve
   raw data, then transform it on a schedule and document the consumer table.
   Kwong and Tuli cover the ingestion-to-mart path
   ([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
   17:55-31:31 and
   [Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
   32:57-43:05).
3. Failure and backfill exercise: simulate late data, a schema change, and a
   rerun, then add tests, alerts, and a runbook.
   Bergh's DataOps discussions make this operational work part of the roadmap,
   not an optional polish step
   ([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
   30:55-54:05 and
   [Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
   33:47-44:12).
4. Platform comparison: run the same workload in a simple local stack and in a
   cloud-style stack, then compare cost, latency, and handoff
   complexity. Tulski and Brudaru both argue for cost-aware, requirements-led
   tool decisions
   ([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
   25:33-30:56 and
   [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
   27:40-30:31 and 44:42-49:42).
5. Capstone data platform: combine ingestion, transformation, and quality checks
   for a consumer, then frame it as self-service or product-facing data.
   Ouazza and Tulski give the strongest evidence
   for this final structure
   ([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
   12:30-23:26 and 52:55-54:31 and
   [Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
   57:35-1:04:42).

## Role Milestones

Entry-level readiness means you can write SQL and Python. You can explain table
grain, model basic entities, and run one orchestrated job with tests. Katz's
two episodes map this level to coding, orchestration, and interviews.
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-40:42 and
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-11:24).

Mid-level readiness means you can own a production pipeline. You can talk with
downstream users about freshness and quality, handle backfills, and review
transformation code. Kwong covers stack tradeoffs, Tuli covers pipeline
architecture, and Bergh covers DataOps ownership.
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
30:59-49:32 and
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
37:10-44:57 and
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
23:56-34:13).

Senior readiness means you can set platform conventions and define ownership
boundaries. You can also decide whether governance or self-service work is
worth the operational burden. Tulski's 2026 career discussion links
senior value to cost-aware engineering and portfolio framing
([Tulski 2026 career discussion]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-38:01 and 51:04-1:04:42).
Ouazza shows the team-scale version through self-service and cross-team impact
([Ouazza on scaling teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
20:13-23:26 and 50:17-54:31).

## Study-Build Boundary

Stop studying and build when you can already write SQL joins plus window
functions. You should also be able to write Python that reads inputs and writes
outputs. Explain raw-to-mart layers and run one scheduler locally.

Use Git with a basic test because Katz keeps fundamentals ahead of tool
collection. Brudaru's beginner roadmap says to combine fundamentals,
requirements gathering, and building
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
56:46 and
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
41:06).

Learn the next tool when your project exposes the constraint that tool solves.
Use orchestration when manual reruns become unclear. Add observability when
consumers need freshness signals. Consider Kafka only when latency justifies
the operational cost. Event contracts can justify it too
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
50:29-54:05 and
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
23:26 and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
30:56-38:01).

## Related Pages

Use these adjacent pages for deeper roadmap work:

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Engineering Certification]({{ '/wiki/data-engineering-certification/' | relative_url }})
