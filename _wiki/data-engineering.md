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

[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
gives the early DataTalks.Club boundary. Around 13:58 and 30:01, data engineers
prepare product data for analysts and data scientists without overloading
operational databases. Later interviews split that broad role across
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}). They also
separate [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
from [DataOps]({{ '/wiki/dataops/' | relative_url }}) and add AI-ready
infrastructure
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
11:54-17:29). [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
adds the AI-ready data thread at 16:40-23:41.
[Fundamentals of Data Engineering]({{ '/books/20220815-fundamentals-of-data-engineering/' | relative_url }})
by Joe Reis and Matthew Housley expands this same lifecycle and generation
model for data systems into a full reference.

## Role Boundaries

Companies draw the role differently as their teams and platforms grow. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
data engineers prepare datasets before analysts query them or data scientists
train on them. Around 24:55-30:01, the hosts separate that work from
[Data Science]({{ '/wiki/data-science/' | relative_url }}): data engineers
collect and prepare data, while data scientists model and evaluate it.
[CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}) shows why that handoff
matters, because data collection and preparation can decide whether modeling can
begin at 15:46-19:25.

[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) argues that
"data engineer" now covers several jobs. Platform data engineers own
infrastructure, orchestration, access, and shared conventions. Product data
engineers work closer to domain use cases, data products, and stakeholder needs
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
11:54-17:29). Data engineering overlaps with
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
when product-facing engineers help teams publish owned data products with clear
interfaces.

Warehouse transformation work creates another boundary with
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places dbt-style
transformation after ingestion in an ELT flow
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-15:30). The analytics engineering role episode treats metric modeling and
business-facing warehouse layers as a separate specialization
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
12:09-13:18 and 1:08:24-1:08:59).

## Pipelines and Stack Choices

Podcast discussions often start with pipeline mechanics. Kwong maps the modern
stack vocabulary by distinguishing ETL from ELT. She places ingestion before
dbt-style transformation and contrasts warehouses with lakes
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:46-12:39 and 30:59-49:32). Those choices connect directly to
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }}),
[CDC]({{ '/wiki/cdc/' | relative_url }}), and
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}).

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) expands the map
from tool categories into end-to-end design. She compares ML pipelines with
analytics pipelines, follows the work through orchestration and distributed
systems, and covers staging concerns such as deduplication and PII masking.
She also shows how ordering guarantees and entity modeling affect the marts
that consumers use
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
13:25-18:44 and 26:43-43:05).

Guests treat tools as choices, not badges. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
puts SQL, Python, and modeling before distributed systems for beginners
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
23:35-38:05). His job-prep episode names Python and SQL depth alongside Docker,
Airflow, and warehouses. He then adds code quality and interview practice as
proof points
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-11:24 and 32:22-35:09).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
makes the senior version of the same argument. Teams should choose platforms
and compute tools from actual requirements
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
14:32-18:17 and 35:37-44:42).

## Platforms and Self-Service

At team scale, data engineering becomes platform work.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) describes
storage and compute as shared foundations for data teams. He also includes
workflow engines and automation
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-35:57 and 50:13-57:46). Teams pursue
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
so analysts and data scientists don't have to rebuild the same foundation.
Software engineers and domain teams can use the supported path too.

[Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }}) adds the team
growth side by linking self-service to onboarding and playbooks, plus naming
conventions and sequencing rules. Senior engineers also turn repeated work into
shared capabilities
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26 and 50:17-54:31). Albertsson adds that domain teams need reliable
interfaces and ownership before data products become useful
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
57:46-1:04:18). [Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
shows the adoption problem after a platform has already produced tables or
models.

## Reliability and DataOps

Data engineering is reliability work because a scheduled job can succeed while
the data arrives late, changes schema, or stops representing the business event.
[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) names freshness,
schema, and lineage as observability signals. Ownership and SLAs turn those
signals into recovery inputs
([Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
16:38-29:00 and 35:24-43:00). Those signals belong with
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) turns
those signals into operating discipline. His DataOps episodes connect data
engineering to tests, CI/CD, realistic test data, and deployment automation.
They also connect observability to recovery behavior
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
15:52-18:46 and 30:55-54:05). [DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
separates that operating layer from the broader engineering role.
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
covers incidents where a model failure may start with upstream data delivery
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
18:46-26:13, and
[Production-Ready AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
18:38).

## Batch, Streaming, and Cost

Streaming helps when latency matters, but DataTalks.Club guests warn against
treating real-time systems as a maturity badge. Ouazza uses Kafka, schemas, and
event-driven work to show where streaming can support growth
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
23:26). Production ML examples also use Kafka and cloud queues when models
depend on live production paths
([Production ML Pipelines with AWS and Kafka]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
15:11). Use [Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
when the question is latency, ordering, replay, and operational cost.

Albertsson warns about the cost of real-time systems
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
41:53-45:11). Brudaru pushes teams back toward requirement-led architecture
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
51:19). Tulski argues that batch or managed systems may fit many businesses
better than a custom real-time stack
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
30:56-38:01).

Teams also choose tools under cost and governance constraints.
[Eddy Zulkifly]({{ '/people/eddyzulkifly/' | relative_url }}) frames data
platforms as digital warehouses that need tagging, capacity planning, and spend
accountability
([FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
21:57-24:34 and 31:40-48:01). [FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
covers that cloud-cost discipline in more detail. Brudaru adds an open-source
architecture lens: Iceberg and DuckDB can reduce lock-in, but metadata and
governance still matter
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-30:31 and 44:42-49:42).

## AI-Ready Data

Newer interviews connect data engineering to [AI]({{ '/wiki/ai/' | relative_url }})
and [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}).
They don't suggest that LLMs remove pipeline work. Brudaru describes AI
integration as a data engineering trend and predicts more convergence with AI
agents. He still centers metadata and quality
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
16:40-23:41 and 38:02-44:42).

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) ties
production AI to preprocessing and testing. AI systems also need retrieval
corpora and governance
([Production-Ready AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
18:38). The data engineering part of AI reliability is often upstream from the
model. A late table, schema change, weak lineage, or missing retrieval context
can look like a model problem from the outside.

## Career Skills

Katz treats data engineering as applied engineering, not a memorized tool list.
He recommends Python, SQL, and data modeling before advanced distributed
systems. He also presents dbt and Snowflake as early exposure to production
data work
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
23:35-45:14). The [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
and [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
turn that skill sequence into practice paths.

Katz's job-prep episode translates the same skills into hiring signals. He
emphasizes Python and SQL. He also names Docker and Airflow. Warehouse
experience and code quality matter too. Portfolio projects and technical
interview practice round out the signal
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-11:24 and 32:22-39:49).

Tulski adds the market-side distinction. Senior
candidates are valued for business judgment, cost awareness, and the ability to
avoid over-engineering. He also argues that AI automation makes strategic
builders more valuable than people who only operate one narrow tool
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
42:08-1:04:42).

Zulkifly's path from business analysis to data engineering shows why domain
understanding and stakeholder translation can become engineering advantages.
Those skills get stronger when paired with cloud, Python, and cost discipline
([FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
6:20-8:18 and 48:01-56:05). Many data engineering paths start near
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
or [Data Science]({{ '/wiki/data-science/' | relative_url }}). The role often
sits between business questions, analytical modeling, and production systems.

[José Figueiredo]({{ '/people/josemaria/' | relative_url }}) adds the
IoT and remote-work dimension. In
[Remote Data Engineering and IoT Platforms]({{ '/podcasts/remote-data-engineering-work-and-building-iot-platforms/' | relative_url }}),
he describes building an "operating system" for sensor data: a platform that
handles how data comes in, how it is stored, and how it flows out to internal
stakeholders. His ETL process starts with exploration — understanding what is
inside the data and why the pipeline exists — before writing code. He also shows
how a data engineering newsletter doubles as personal branding and
communication practice, and how remote work in Norway constrains the hiring
market to a few cities despite a remote-first setup.
