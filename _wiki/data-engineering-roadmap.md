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
---

A data engineering roadmap starts with querying and modeling data. The
DataTalks.Club archive later expands it into reliable data products and
platforms. Start with SQL plus Python. Then add modeling and requirements
before pipeline operations
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-38:05 and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-30:56).

The archive doesn't treat the roadmap as a tool checklist. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
puts core database work before distributed systems
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-38:05 and 56:46). [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
makes the same point from the modern stack side. He tells beginners to learn
the fundamentals first. They should gather requirements and build projects
before surveying every orchestrator or table format
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
41:06-44:42).

Use [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) for the
discipline and [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
for job scope. Use [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
for proof of skill and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for
operating practice.

## Link Map

Core roadmap pages:

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})

Podcast discussions to read first:

- [Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}) with [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
- [Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}) with [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
- [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
- [Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}) with [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
- [DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}) with [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
- [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}) with [Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }})
- [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}) with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
- [Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}) with [Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }})

## Common Definition

The archive treats a data engineering roadmap as a path toward useful data.
It also emphasizes recoverability.

At the entry point write SQL and Python, then learn OLTP and OLAP. Build
tables that answer real business questions.
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-26:40 and 44:21-45:14 and
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-2:22 and 9:41).

After fundamentals, build a working pipeline. [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
places ingestion and transformation in the same modern stack discussion as
warehouses, marts, and orchestration. She also covers CDC and schema evolution
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
3:46-17:55 and 30:59-49:32). [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
adds the end-to-end pipeline structure. Her discussion moves from ingestion
and orchestration into modeled marts, dashboards, and production ML handoffs
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
10:48-18:44 and 24:57-44:57).

At the senior end use judgment about system burden instead of adding tools by
default. Decide when a simple batch pipeline is enough. Then decide which
constraint should guide the architecture
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
12:30-23:26 and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-38:01).

## Guest Differences

Guests agree on SQL, Python, and reliable pipelines. They differ on how
quickly the roadmap should move into platform work.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) keeps the beginner
curriculum narrow and emphasizes interviewable fundamentals. His later
job-prep episode adds warehouse work plus Docker and Airflow. He explains
why a junior curriculum can skip distributed platform tools.
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-40:42 and
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-7:46).

[Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }}) starts from a
scale-up constraint where the roadmap needs platform conventions. It also
needs senior hiring and Kafka data contracts. A fast-growing company can't
have every team reinvent data plumbing
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
5:41-23:26 and 50:17-54:31). That belongs later in a learner roadmap unless
the learner already works in a team with those scale problems.

[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) separates
platform data engineering from product data engineering. Platform engineers
own infrastructure and shared systems. Product-facing data engineers sit closer
to domain models, data products, and stakeholders
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
11:54-17:29).

That split matters for specialization. For a platform role, go deeper into
cloud, orchestration, cost and reliability. For product data engineering,
focus on modeling, requirements and data product ownership.

## Stage 1: Query and Model Useful Data

Start with analytical SQL, Python, and database concepts. Katz's curriculum
puts Python, SQL and cloud fundamentals at the center. He
also uses OLTP versus OLAP and sample databases for data modeling
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-26:40 and 44:21-45:14). His job-prep episode adds code quality, tests,
and common interview formats
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-2:22 and 7:46-11:24).

Practice by turning raw product data or public data into tables with documented
grain. Join source data and handle nulls. Explain why a dashboard number
changes when the grain changes.
This connects the roadmap to
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
because useful data engineering often ends in trustworthy marts and BI-facing
tables.
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
12:39-15:30 and
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
39:23-43:05).

## Stage 2: Build an End-to-End Batch Pipeline

Build one batch pipeline before adding streaming or distributed processing.
A good first pipeline extracts from an API or file source and stores raw data.
It then transforms the data into modeled tables and runs on a schedule. Publish
documentation for the consumer too.

Kwong's modern stack episode covers ETL and ELT. It connects raw ingestion to
transformation, marts, orchestration and schema evolution
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
3:46-17:55 and 30:59-49:32).

Keep the first stack small enough to finish. Use Python extraction, local
storage, one query engine and one scheduler.
Brudaru's trends episode supports simple, requirement-led tool choice. It also
shows where DuckDB, Iceberg and open table formats fit when the project grows
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
18:17-35:37 and 41:06-44:42).

## Stage 3: Operate the Pipeline Like a Product

Add tests, CI/CD, observability and runbooks as soon as the pipeline
has a consumer. [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
connects DataOps to automation and CI/CD. He also ties it to regression tests,
realistic test data and production monitoring
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
15:52-18:46 and 30:55-54:05 and
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
33:47-51:21).

Break the pipeline on purpose. Change a schema, delay an input, duplicate
records, and backfill old data. Then document how you detect the issue and who
gets notified. Also document what gets rolled back and how downstream tables
recover. This is the bridge from [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
to [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}).

## Stage 4: Choose Platform Patterns Deliberately

Learn storage with processing as tradeoffs, and treat orchestration with
streaming the same way. Don't treat managed services as badges. Kwong's episode
shows how teams choose
between lakes, warehouses and marts. She also covers reverse flows
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
19:50-35:42). Brudaru's episode adds table formats, DuckDB, metadata,
lineage and orchestration options
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
3. Failure and backfill exercise: simulate late data, a schema change and a
   rerun, then add tests, alerts and a runbook.
   Bergh's DataOps discussions make this operational work part of the roadmap,
   not an optional polish step
   ([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
   30:55-54:05 and
   [Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
   33:47-44:12).
4. Platform comparison: run the same workload in a simple local stack and in a
   cloud-style stack, then compare cost, latency and handoff
   complexity. Tulski and Brudaru both argue for cost-aware, requirements-led
   tool decisions
   ([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
   25:33-30:56 and
   [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
   27:40-30:31 and 44:42-49:42).
5. Capstone data platform: combine ingestion, transformation and quality checks
   for a consumer, then frame it as self-service or product-facing data.
   Ouazza and Tulski give the strongest evidence
   for this final structure
   ([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
   12:30-23:26 and 52:55-54:31 and
   [Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
   57:35-1:04:42).

## Role Milestones

Entry-level readiness means you can write SQL and Python. You can explain table
grain, model basic entities and run one orchestrated job with tests. Katz's
two episodes map this level to coding, orchestration and
interviews.
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
23:35-40:42 and
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
1:20-11:24).

Mid-level readiness means you can own a production pipeline. You can talk with
downstream users about freshness and quality. You can handle backfills and
review transformation code.

Kwong covers stack tradeoffs, Tuli covers pipeline architecture and Bergh
covers DataOps ownership.
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
30:59-49:32 and
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
37:10-44:57 and
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
23:56-34:13).

Senior readiness means you can set platform conventions. You can define
ownership boundaries and decide whether governance or self-service work is
worth the operational burden.
Tulski's 2026 career discussion links senior value to cost-aware engineering
and strategic portfolio framing. Ouazza shows the team-scale version through
self-service. He also discusses cross-team impact
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
25:33-38:01 and 51:04-1:04:42 and
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
20:13-23:26 and 50:17-54:31).

## Study-Build Boundary

Stop studying and build when you can already write SQL joins plus window
functions. You should also be able to write Python that reads inputs and writes
outputs. Explain raw-to-mart layers and run one scheduler locally.

Use Git with a basic test because Katz explicitly keeps fundamentals ahead of
tool collection. Brudaru's beginner roadmap says to combine fundamentals,
requirements gathering and building
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
