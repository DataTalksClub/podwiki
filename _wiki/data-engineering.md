---
layout: wiki
title: "Data Engineering"
summary: "Data engineering across pipelines, platforms, data quality, role boundaries, business enablement, and the shift toward AI-ready data systems."
related:
  - Data Engineering Platforms
  - Data Pipelines
  - Modern Data Stack
  - MLOps
  - DataOps
  - Data Quality and Observability
  - Analytics Engineering
  - Data Science
  - AI
---

Data engineering makes data dependable enough for analysts and data scientists
to use. Product teams, machine learning systems, and AI systems rely on the
same work. Data engineers move data out of source systems and preserve
recoverable history. They transform that data into modeled outputs, schedule the
work, expose interfaces, and monitor whether the outputs still behave as
expected.

[[podcast:data-team-roles|Data Team Roles Explained]]
gives the early DataTalks.Club boundary. Around 13:58 and 30:01, data engineers
prepare product data for analysts and data scientists without overloading
operational databases. Later interviews split that broad role across
[[Data Engineering Platforms]]
and [[Data Pipelines]]. They also
separate [[Analytics Engineering]]
from [[DataOps]] and add AI-ready
infrastructure
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
11:54-17:29). [[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]
adds the AI-ready data thread at 16:40-23:41.
[[book:20220815-fundamentals-of-data-engineering|Fundamentals of Data Engineering]]
by Joe Reis and Matthew Housley expands this same lifecycle and generation
model for data systems into a full reference.

## Role Boundaries

Companies draw the role differently as their teams and platforms grow. In
[[podcast:data-team-roles|Data Team Roles Explained]],
data engineers prepare datasets before analysts query them or data scientists
train on them. Around 24:55-30:01, the hosts separate that work from
[[Data Science]]: data engineers
collect and prepare data, while data scientists model and evaluate it.
[[podcast:crisp-dm|CRISP-DM]] shows why that handoff
matters, because data collection and preparation can decide whether modeling can
begin at 15:46-19:25.

[[person:slawomirtulski|Slawomir Tulski]] argues that
"data engineer" now covers several jobs. Platform data engineers own
infrastructure, orchestration, access, and shared conventions. Product data
engineers work closer to domain use cases, data products, and stakeholder needs
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
11:54-17:29). Data engineering overlaps with
[[Data Product Management]]
when product-facing engineers help teams publish owned data products with clear
interfaces.

Warehouse transformation work creates another boundary with
[[Analytics Engineering]].
[[person:nataliekwong|Natalie Kwong]] places dbt-style
transformation after ingestion in an ELT flow
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
7:57-15:30). The analytics engineering role episode treats metric modeling and
business-facing warehouse layers as a separate specialization
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]],
12:09-13:18 and 1:08:24-1:08:59).

## Pipelines and Stack Choices

Podcast discussions often start with pipeline mechanics. Kwong maps the modern
stack vocabulary by distinguishing ETL from ELT. She places ingestion before
dbt-style transformation and contrasts warehouses with lakes
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
3:46-12:39 and 30:59-49:32). Those choices connect directly to
[[Modern Data Stack]],
[[ETL vs ELT]],
[[CDC]], and
[[Orchestration]].

[[person:santonatuli|Santona Tuli]] expands the map
from tool categories into end-to-end design. She compares ML pipelines with
analytics pipelines, follows the work through orchestration and distributed
systems, and covers staging concerns such as deduplication and PII masking.
She also shows how ordering guarantees and entity modeling affect the marts
that consumers use
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]],
13:25-18:44 and 26:43-43:05).

Guests treat tools as choices, not badges. [[person:jeffkatz|Jeff Katz]]
puts SQL, Python, and modeling before distributed systems for beginners
([[podcast:data-engineering-career-path-and-skills|Data Engineering Career Path and Skills]],
23:35-38:05). His job-prep episode names Python and SQL depth alongside Docker,
Airflow, and warehouses. He then adds code quality and interview practice as
proof points
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]],
1:20-11:24 and 32:22-35:09).

[[person:adrianbrudaru|Adrian Brudaru]]
makes the senior version of the same argument. Teams should choose platforms
and compute tools from actual requirements
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
14:32-18:17 and 35:37-44:42).

## Platforms and Self-Service

At team scale, data engineering becomes platform work.
[[person:larsalbertsson|Lars Albertsson]] describes
storage and compute as shared foundations for data teams. He also includes
workflow engines and automation
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
16:42-35:57 and 50:13-57:46). Teams pursue
[[self-service-data-platforms|Self-Service Data Platforms]]
so analysts and data scientists don't have to rebuild the same foundation.
Software engineers and domain teams can use the supported path too.

[[person:mehdiouazza|Mehdi Ouazza]] adds the team
growth side by linking self-service to onboarding and playbooks, plus naming
conventions and sequencing rules. Senior engineers also turn repeated work into
shared capabilities
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]],
12:30-23:26 and 50:17-54:31). Albertsson adds that domain teams need reliable
interfaces and ownership before data products become useful
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
57:46-1:04:18). [[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]
shows the adoption problem after a platform has already produced tables or
models.

## Reliability and DataOps

Data engineering is reliability work because a scheduled job can succeed while
the data arrives late, changes schema, or stops representing the business event.
[[person:barrmoses|Barr Moses]] names freshness,
schema, and lineage as observability signals. Ownership and SLAs turn those
signals into recovery inputs
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
16:38-29:00 and 35:24-43:00). Those signals belong with
[[Data Quality and Observability]]
and [[data-quality-and-observability|Data Observability]].

[[person:christopherbergh|Christopher Bergh]] turns
those signals into operating discipline. His DataOps episodes connect data
engineering to tests, CI/CD, realistic test data, and deployment automation.
They also connect observability to recovery behavior
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
15:52-18:46 and 30:55-54:05). [[DataOps vs Data Engineering]]
separates that operating layer from the broader engineering role.
[[MLOps vs DataOps]]
covers incidents where a model failure may start with upstream data delivery
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
18:46-26:13, and
[[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]],
18:38).

## Batch, Streaming, and Cost

Streaming helps when latency matters, but DataTalks.Club guests warn against
treating real-time systems as a maturity badge. Ouazza uses Kafka, schemas, and
event-driven work to show where streaming can support growth
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]],
23:26). Production ML examples also use Kafka and cloud queues when models
depend on live production paths
([[podcast:production-ml-pipelines-with-aws-and-kafka|Production ML Pipelines with AWS and Kafka]],
15:11). Use [[Batch vs Streaming]]
when the question is latency, ordering, replay, and operational cost.

Albertsson warns about the cost of real-time systems
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
41:53-45:11). Brudaru pushes teams back toward requirement-led architecture
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
51:19). Tulski argues that batch or managed systems may fit many businesses
better than a custom real-time stack
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
30:56-38:01).

Teams also choose tools under cost and governance constraints.
[[person:eddyzulkifly|Eddy Zulkifly]] frames data
platforms as digital warehouses that need tagging, capacity planning, and spend
accountability
([[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
21:57-24:34 and 31:40-48:01). [[FinOps for Data Engineers]]
covers that cloud-cost discipline in more detail. Brudaru adds an open-source
architecture lens: Iceberg and DuckDB can reduce lock-in, but metadata and
governance still matter
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-30:31 and 44:42-49:42).

## AI-Ready Data

Newer interviews connect data engineering to [[AI]]
and [[AI Infrastructure]].
They don't suggest that LLMs remove pipeline work. Brudaru describes AI
integration as a data engineering trend and predicts more convergence with AI
agents. He still centers metadata and quality
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
16:40-23:41 and 38:02-44:42).

[[person:bartoszmikulski|Bartosz Mikulski]] ties
production AI to preprocessing and testing. AI systems also need retrieval
corpora and governance
([[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]],
18:38). The data engineering part of AI reliability is often upstream from the
model. A late table, schema change, weak lineage, or missing retrieval context
can look like a model problem from the outside.

## Career Skills

Katz treats data engineering as applied engineering, not a memorized tool list.
He recommends Python, SQL, and data modeling before advanced distributed
systems. He also presents dbt and Snowflake as early exposure to production
data work
([[podcast:data-engineering-career-path-and-skills|Data Engineering Career Path and Skills]],
23:35-45:14). The [[data-engineer-roadmap|Data Engineering Roadmap]]
and [[Data Engineering Portfolio Projects]]
turn that skill sequence into practice paths.

Katz's job-prep episode translates the same skills into hiring signals. He
emphasizes Python and SQL. He also names Docker and Airflow. Warehouse
experience and code quality matter too. Portfolio projects and technical
interview practice round out the signal
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]],
1:20-11:24 and 32:22-39:49).

Tulski adds the market-side distinction. Senior
candidates are valued for business judgment, cost awareness, and the ability to
avoid over-engineering. He also argues that AI automation makes strategic
builders more valuable than people who only operate one narrow tool
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
42:08-1:04:42).

Zulkifly's path from business analysis to data engineering shows why domain
understanding and stakeholder translation can become engineering advantages.
Those skills get stronger when paired with cloud, Python, and cost discipline
([[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
6:20-8:18 and 48:01-56:05). Many data engineering paths start near
[[Data Analyst Careers]]
or [[Data Science]]. The role often
sits between business questions, analytical modeling, and production systems.

[[person:josemaria|José Figueiredo]] adds the
IoT and remote-work dimension. In
[[podcast:remote-data-engineering-work-and-building-iot-platforms|Remote Data Engineering and IoT Platforms]],
he describes building an "operating system" for sensor data: a platform that
handles how data comes in, how it is stored, and how it flows out to internal
stakeholders. His ETL process starts with exploration — understanding what is
inside the data and why the pipeline exists — before writing code. He also shows
how a data engineering newsletter doubles as personal branding and
communication practice, and how remote work in Norway constrains the hiring
market to a few cities despite a remote-first setup.
