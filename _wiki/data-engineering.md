---
layout: wiki
title: "Data Engineering"
summary: "How the DataTalks.Club podcast archive frames data engineering: pipelines, platforms, data quality, role boundaries, business enablement, and the shift toward AI-ready data systems."
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

Data engineering makes data usable and reliable for downstream work. That
includes analysis, machine learning, product systems, and business decisions. In
the DataTalks.Club archive, data engineers build the paths between source
systems and consumers. Those paths cover ingestion, transformation, monitoring,
and recovery.

The podcast archive doesn't treat data engineering as a single fixed job. In
the early role taxonomy, data engineers prepare product data for analysts and
data scientists. They do that without burdening operational systems
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})).
Later interviews split the work across platform engineering, product-facing
data engineering, analytics engineering, and DataOps. Recent episodes also add
AI-ready infrastructure
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

Use this page as the foundation hub for the broader discipline. For deeper
platform work, use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
For pipeline operating practices, use
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }}).
Use [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
when the incident boundary is between model lifecycle and data delivery. For
warehouse-side modeling and metric layers, use
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

## Listening Path

Use the local podcast pages as the listening layer for this topic. Start with
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
for role boundaries, then use
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
for ETL and ELT. It also covers warehouses, orchestration, and reverse data flows. Add
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
when the question is end-to-end pipeline design.

For operations, pair
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
with
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
For platforms and team scale, use
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
and
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
For careers, use
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).

## Core Archive Threads

The central archive thread starts with role boundaries. In the role-taxonomy
episode, data engineering means building systems that move and protect data.
Those systems prepare data for analysts and data scientists
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})).

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) then turns that role
into a skill path. That path starts with SQL and Python. It also includes data
modeling and warehousing, plus orchestration and interview preparation
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})).

The tooling thread runs through the
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) and
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains ETL,
ELT, ingestion, and orchestration as the working vocabulary of modern data
engineering
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) extends that
thread into end-to-end pipeline design. She connects ingestion and staging to
orchestration, transformation, analytics marts, and ML pipeline handoffs
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

The operating thread links data engineering to platform work, quality, and
cost. [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
frames DataOps as tests, CI/CD, observability, and recovery for data teams
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
Use
[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
for that operating boundary.
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) adds the
2026 career split between platform data engineers, product data engineers, and
AI-aware specialists
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

## Common Definition

Across the archive, data engineering converges on one practical definition.
Data engineers make data dependable enough for other people and systems to use.
They collect data from operational systems and preserve raw context. They also
transform data into useful structures, schedule repeatable work, expose
interfaces, and monitor whether the work still behaves as expected.

The earliest DataTalks.Club role episode makes the dependency explicit. Data
engineers prepare data before analysts query it or data scientists train on it.
In that episode, the data engineer also protects the product database from
analytical workloads. The same role helps production features receive
predictions or prepared datasets when needed
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
about 13:58 and 30:01).

Later episodes add the modern stack vocabulary.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) connects ETL
and ELT vocabulary to ingestion and orchestration
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:46-15:30 and 30:59-49:32).
[Jeff Katz's]({{ '/people/jeffkatz/' | relative_url }}) career episode keeps
the foundation more basic. SQL, Python, and data modeling come before Spark
for junior engineers
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
23:35-38:05).

## Disagreements and Boundaries

Guests differ on where the title begins and ends.
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) argues that
"data engineer" still hides several jobs. Platform data engineering owns
infrastructure, orchestration, access, and shared conventions. Product data
engineering sits closer to domain use cases, data products, and stakeholder
needs
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
11:54-17:29).

That split explains many archive boundaries. Data engineering overlaps with
[Data Science]({{ '/wiki/data-science/' | relative_url }}) around training
data, feature pipelines, and production handoff. The role
taxonomy episode gives the simple boundary. Data engineers prepare data, while
data scientists model and evaluate it. CRISP-DM shows that data collection and
preparation can determine whether modeling can even begin
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
24:55-30:01 and
[CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}), 15:46-19:25).

This role boundary is porous because warehouse transformation work often
overlaps with [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
Kwong places dbt-style transformation after ingestion in the ELT workflow
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-15:30). The analytics engineering role episode treats metric modeling and
business-facing warehouse layers as a distinct specialization
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also disagree by architecture pressure. Some scale-up stories need
Kafka, schemas, and self-service conventions, but
[Tulski's]({{ '/people/slawomirtulski/' | relative_url }}) 2026 career
discussion warns against treating real-time tools as a maturity badge. Batch
or managed systems may fit the business better
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26 and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
30:56-38:01).

## Pipelines and the Modern Data Stack

Data engineering episodes usually begin with pipeline mechanics because
engineers extract source data and transform it for consumers.
[Kwong's]({{ '/people/nataliekwong/' | relative_url }}) episode maps this
vocabulary. It distinguishes ETL from ELT and places ingestion before
dbt-style transformation. It also contrasts lakes with warehouses
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
3:46-12:39 and 30:59-49:32 and
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

[Tuli's]({{ '/people/santonatuli/' | relative_url }}) pipeline architecture
episode shows the same discipline through workflow design. She compares ML
pipelines with analytics pipelines. She then follows pipelines through
orchestration tools and distributed systems. The episode covers staging
concerns such as deduplication and PII masking. It also connects ordering
guarantees and entity modeling to marts
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
13:25-18:44 and 26:43-43:05).

The archive treats those tools as implementation choices.
[Katz]({{ '/people/jeffkatz/' | relative_url }}) puts SQL, Python, and
modeling before distributed systems for beginners
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
23:35-38:05). His job-prep episode gives the same hiring signal. He names
Python and SQL depth alongside Docker, Airflow, and warehouses. He also
emphasizes code quality and interview practice as early proof points
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-11:24 and 32:22-35:09).

[Adrian Brudaru's]({{ '/people/adrianbrudaru/' | relative_url }}) trends
episode makes the same point from the senior side. Teams should choose
platforms and processing tools from actual requirements
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
14:32-18:17 and 35:37-44:42).

## Platform Engineering and Self-Service

At team scale, data engineering becomes platform work.
[Lars Albertsson's]({{ '/people/larsalbertsson/' | relative_url }}) DataOps
platform episode covers storage, compute, and workflow engines. The platform
lets other teams use data without reinventing the same foundation
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
16:42-35:57 and 50:13-57:46).

[Mehdi Ouazza's]({{ '/people/mehdiouazza/' | relative_url }}) scale-up
episode adds the human side by showing that
self-service needs onboarding and playbooks. Fast-growing teams may need
seniors who turn repeated work into shared capabilities
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26 and 50:17-54:31 and
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})).

This is the main overlap with
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}).
The platform isn't successful merely because tables exist. It succeeds when
domain teams can safely produce and consume reliable data products. Those
products need clear interfaces and ownership
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
57:46-1:04:18 and
[Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

## Quality, Observability, and DataOps

The archive repeatedly frames data engineering as reliability work. Pipelines
can complete successfully while still delivering late or wrong data.
[Barr Moses's]({{ '/people/barrmoses/' | relative_url }}) observability
episode names the key signals. Teams monitor freshness and schema. Lineage and
ownership matter too
([Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
16:38-29:00 and 35:24-43:00 and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

[Christopher Bergh's]({{ '/people/christopherbergh/' | relative_url }})
DataOps episodes turn those signals into operating practice. Data engineering
teams need tests, CI/CD, observability, and recovery behavior.
[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
separates that operating layer from the broader engineering discipline
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
15:52-18:46 and 30:55-54:05 and
[DataOps]({{ '/wiki/dataops/' | relative_url }})).

Quality work also connects data engineering to ML and AI incidents. A model or
agent may look broken because an upstream table arrived late. It may also fail
because a schema changed or a retrieval corpus lost context. Use
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}) when the
incident boundary is between model lifecycle and data delivery
([DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
18:46-26:13 and
[Production-Ready AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
18:38).

## Batch, Streaming, and Real-Time Tradeoffs

Streaming helps when latency matters, but it isn't a universal maturity mark.
[Ouazza's]({{ '/people/mehdiouazza/' | relative_url }}) scale-up episode uses
Kafka, schemas, and event-driven work to show where streaming can support
growth
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
23:26). Production ML examples also use Kafka and cloud queues when models
depend on live production paths
([Production ML Pipelines with AWS and Kafka]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
15:11).

Other guests push against treating streaming as a badge of maturity because it
adds operational complexity or distracts from requirements.
[Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) warns about the
operational cost of real-time systems
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
41:53-45:11).
[Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) pushes teams back
toward requirement-led architecture
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
51:19).
[Tulski]({{ '/people/slawomirtulski/' | relative_url }}) argues that batch or
managed systems may fit many businesses better
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
38:01).

## Cost, Governance, and Tool Choice

Modern data engineering includes cost and governance. Cloud warehouses and
lakehouse stacks can become expensive shared infrastructure. Use
[FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
for cloud-cost visibility, tagging, capacity planning, and accountability.
[Eddy Zulkifly's]({{ '/people/eddyzulkifly/' | relative_url }}) FinOps
episode frames data platforms as digital warehouses. Teams need cost tagging,
capacity planning, and spend accountability
([FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
21:57-24:34 and 31:40-48:01).

[Brudaru's]({{ '/people/adrianbrudaru/' | relative_url }}) modern trends
episode adds an open-source architecture lens. Iceberg and DuckDB can reduce
lock-in, but they still require metadata and governance. The archive's
synthesis is requirements-led tool selection. Choose the smallest system that
meets latency and cost constraints
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-30:31 and 44:42-49:42 and
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
25:33-30:56).

## AI-Ready Data Engineering

The newer archive links data engineering to AI engineering, but it doesn't
claim that LLMs remove pipeline work.
[Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) describes AI
integration as a trend in data engineering and predicts more convergence with
AI agents. The same episode keeps the focus on metadata and quality
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
16:40-23:41 and 38:02-44:42).

Production AI discussions show the same dependency because
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) connects
production AI to preprocessing and testing. AI systems still need retrieval
corpora and governance
([Production-Ready AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
18:38 and
[AI]({{ '/wiki/ai/' | relative_url }}),
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})).

## Career and Skill Development

The career episodes treat data engineering as an applied engineering path, not
a memorized list of tools. [Katz]({{ '/people/jeffkatz/' | relative_url }})
recommends Python, SQL, and data modeling before advanced distributed systems.
He also presents dbt and Snowflake as early exposure to production data work
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
23:35-45:14 and
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})).

[Katz's]({{ '/people/jeffkatz/' | relative_url }}) job-prep episode
translates those skills into hiring signals. He names Python and SQL depth
alongside Docker, Airflow, and warehouses. He also emphasizes code quality,
portfolio projects, and technical interview practice
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-11:24 and 32:22-39:49).

[Tulski]({{ '/people/slawomirtulski/' | relative_url }}) adds the market-side
distinction. Senior candidates are valued for business judgment, cost
awareness, and the ability to avoid over-engineering. He also argues that AI
automation makes strategic builders more valuable than people who only operate
one narrow tool
([Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
42:08-1:04:42).
[Zulkifly's]({{ '/people/eddyzulkifly/' | relative_url }}) path from business
analysis to data engineering shows why domain understanding and stakeholder
translation can become an engineering advantage. That background becomes
stronger when paired with cloud, Python, and cost discipline
([FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
6:20-8:18 and 48:01-56:05).

## Related Pages

Use these pages for adjacent topics and deeper implementation detail.

- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
