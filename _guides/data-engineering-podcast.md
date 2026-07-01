---
layout: article
title: "Data Engineering Podcast: DataTalks.Club Episodes to Start With"
keyword: "data engineering podcast"
canonical_url: "https://datatalks.club/podcast.html"
summary: "A podcast-backed listening guide to DataTalks.Club episodes on data engineering fundamentals, tools, platforms, DataOps, careers, freelance work, streaming, Data Mesh, and governance."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Data Engineering Roadmap
  - Modern Data Stack
  - DataOps
  - Data Quality and Observability
  - Batch vs Streaming
  - Data Mesh
  - Data Governance
  - Freelance
---

If you're looking for a data engineering podcast, use this guided path through
DataTalks.Club episodes. It starts with pipelines, warehouses, orchestration,
and DataOps. It also covers platforms, streaming, governance, and careers.
Freelance work has its own section. Start with role definitions, then move into
tooling and operating problems, then into career and consulting episodes.

Use [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) for
the reference layer behind the listening path. Pair it with
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }}),
and [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}).

## Listening Map

Use these sections to choose the next cluster to listen to.

- [Fundamentals](#fundamentals)
- [Tools and Modern Stack](#tools-and-modern-stack)
- [DataOps and Quality](#dataops-and-quality)
- [Platforms and Team Scale](#platforms-and-team-scale)
- [Careers and Learning Paths](#careers-and-learning-paths)
- [Freelance and Consulting](#freelance-and-consulting)
- [Batch and Streaming](#batch-and-streaming)
- [Data Mesh and Governance](#data-mesh-and-governance)
- [Build a Listening Path](#build-a-listening-path)

## Fundamentals

Start here if you want the base vocabulary because these episodes explain what
data engineers do. They show where engineers hand work to analysts and data
scientists, and why a pipeline needs ownership beyond a scheduled script.

Start with [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the archive's first role map. Around 13:58, data engineers make necessary data
available in usable form. Around 30:01, the episode separates data preparation
from machine learning work.

Use [Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})
for older big-data vocabulary. [Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }})
starts from ETL pipelines, HDFS/S3, Impala, and Spark performance work. She
then compares data engineering with data science, ML deployment, and
analyst-facing interfaces.

[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
is the foundation episode for modern-stack vocabulary.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) walks through
ETL, ELT, ingestion, and transformations. She also covers data marts,
warehouses, and lakes. Later sections cover orchestration, reverse data flows,
CDC, and schema evolution.

For written companions, use
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) and
[Fundamentals of Data Engineering]({{ '/guides/fundamentals-of-data-engineering/' | relative_url }}).

## Tools and Modern Stack

The tool episodes are useful because guests keep tying products back to data
flow. They discuss ingestion, storage, transformation, and orchestration.
Activation and cost come up as operating concerns too.

[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
is the cleanest starting point:

- 3:46 for ETL.
- 7:57 for ELT.
- 12:39 for analytics engineering and dbt.
- 19:50 for data lakes.
- 30:59 for Airflow.
- 35:42 for reverse data flows.
- 45:59 for CDC.

[Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
updates that map for lakehouse and AI-era work.
[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) covers Apache
Iceberg, Delta Lake, and Hudi. He also discusses DuckDB, metadata catalogs,
orchestration, and streaming. He also discusses AI-assisted pipeline work.
Around 44:42, he warns against vendor-led tool choices.

Around 41:06, he brings the learning path back to SQL and Python, plus
requirements and portfolio evidence.

In [Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) shows the
product and growth side of the stack. He connects tracking plans to warehouse
work, then moves into transformations and reverse ETL. Customer data platforms
and operational analytics come next. Use this episode when you want to
understand why a warehouse table isn't the end of the data flow.

For deeper tool comparisons, use these pages:

- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Apache Airflow]({{ '/wiki/orchestration/' | relative_url }})

## DataOps and Quality

Data engineering work breaks in ordinary ways because files arrive late,
schemas change, and joins duplicate records. Dashboards go stale, and
downstream models can train on broken inputs. The reliability episodes treat
these failures as operating problems, not as one-off bugs.

[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
connects pipeline work to automation, observability, CI/CD, and regression
tests. It also covers realistic test data, deployment confidence, and recovery.
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) makes
the case that data teams need operating practices, not only orchestration.

In [Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) anchors the quality
layer. Around 16:38, she defines the five pillars as freshness and volume,
distribution and schema, and lineage. Later sections cover schema-change
incidents and SLAs. They also cover runbooks, alerting, and ownership. Use the
episode for the difference between detecting a failure and finding the cause.

[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
shows data quality under time pressure. [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }})
discusses feature pipelines, daily batches, real-time scoring, and Great
Expectations. She also covers schema changes, logs, runbooks, and debugging.
It's the most concrete episode here for seeing how bad data can affect a live
operational decision.

For the written synthesis, use these pages:

- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})

## Platforms and Team Scale

Data engineering becomes platform work when many teams need reliable data
without waiting for one central engineer to handle every request. The archive
keeps a useful tension here. Self-service helps teams move faster, but only
when shared conventions, ownership, and monitoring exist.

[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
is the core platform episode. [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }})
describes scale-up data work, self-service platforms, and onboarding. He also
covers Airflow conventions, playbooks, and Kafka. Schema registries and data
contracts are part of the same platform discussion.

Around 17:22, he explains the platform anatomy. Around 23:26, he connects
Kafka to schemas and contracts rather than treating it as a standalone
streaming tool.

[Data Engineering Leadership and Modern Data Platforms]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})
adds the management view. [Rahul Jain]({{ '/people/16rahuljain/' | relative_url }})
uses his ETL-to-platform-management path to discuss stakeholder management,
team prioritization, and data reconciliation. He also discusses GDPR controls,
lineage, and the shift from ETL to ELT.

[FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }})
adds the cost dimension. [Eddy Zulkifly]({{ '/people/eddyzulkifly/' | relative_url }})
ties cloud cost work to BigQuery, storage tiers, reservations, and tagging. He
also covers accountability, forecasting, and managed-versus-custom tradeoffs.

For the reference layer, use these pages:

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})

## Careers and Learning Paths

The archive's career advice is consistent: SQL and Python matter before broad
tool collecting. Data modeling, tests, and requirements gathering matter too.
You need finished projects more than shallow exposure to Spark, Kafka,
Kubernetes, or a lakehouse stack.

[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
is the main beginner-curriculum episode. Around 23:35,
[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) names Python, SQL, and
cloud fundamentals as core skills. Around 38:05, he explains why a
junior-focused path may skip Spark, Kafka, and Kubernetes until the basics are
solid.

[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
is useful for role definition. [Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }})
separates platform data engineering from product-facing data engineering,
questions overbuilt stacks, and treats cost-aware judgment as a senior signal.
Use the portfolio sections around 57:35 and 1:04:42 when deciding what kind of
project proves readiness.

[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
and
[Data Engineering Job Search Story]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }})
are useful when you want hiring and interview context. Jeff Katz covers Python,
SQL, Docker, and Airflow. He also covers portfolio work, interviews, and
application strategy.

[Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }}) gives a
job-search case study from neuroscience research into analytics and data
engineering. The episode covers Docker, Airflow, and AWS. It also covers
application tracking and a custom portfolio project.

For written guides, use these pages:

- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})

## Freelance and Consulting

The archive has a strong independent-work thread because several data
engineering episodes involve freelancers, consultants, and founders who turned
repeated client problems into reusable tools.

[Freelance Data Engineering Playbook]({{ '/podcasts/freelance-data-engineering-pricing-and-clients/' | relative_url }})
is the main episode. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
covers pricing, occupancy, agencies versus direct clients, and repeat business.
He also covers scoping, discovery spikes, written scope documents, and volatile
schemas. Remote work, reusable assets, and client expectations come up too.

Use 11:36 for early projects that involved legacy cleanup and Airflow. Use
31:43 for scoping through spikes and written scope documents. Use 46:17 for
reusable portfolio assets.

[Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
also helps here because Adrian connects freelance experience to tool building
and reusable ingestion patterns. Listen to the early career section around 3:10
and the DLT discussion around 4:03 if you want the bridge from consulting pain
to product work.

[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
adds a senior consulting perspective. It helps clarify when clients need a
platform specialist, product data engineer, or consultant who can diagnose the
operating constraint before choosing a tool.

For written follow-up, use these pages:

- [Freelance]({{ '/wiki/freelance/' | relative_url }})

## Batch and Streaming

The podcast archive doesn't treat streaming as a maturity badge. Guests use
streaming when the decision needs low latency. They use batch, scheduled jobs,
or micro-batches when the business can wait and the simpler system is easier to
operate.

[Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
gives the most recent vocabulary. Around 51:19, Adrian Brudaru compares
micro-batching and Kafka, then discusses SQS and Flink. Name the SLA before
naming the tool.

[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
explains the organizational side of streaming. Mehdi OUAZZA treats Kafka as
part of a platform with schemas, registries, contracts, and guidelines. Consumer
ownership matters too.

[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
is the clearest applied example. Angela Ramirez combines daily feature batches
with real-time scoring because fraud systems need to support decisions during a
transaction.

[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
and
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
also compare batch and streaming. [Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }})
covers queues, event pipelines, and model-serving tradeoffs.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) covers
micro-batching, streaming, dependency management, and reproducibility from a
DataOps platform focus.

For written comparison, see
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) and
[Streaming]({{ '/wiki/streaming/' | relative_url }}).

## Data Mesh and Governance

Data engineering work becomes governance work when teams need shared meaning,
access control, and ownership. Quality signals, retention, and policy
automation belong in that work too.

[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})
is the core Data Mesh episode. [Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }})
explains domain ownership and data products, then moves into contracts, quality
guarantees, and SLAs. Self-serve platforms and federated governance come next.

Use 13:20 for contracts and domain ownership, 31:05 for metadata and
interoperability, and 41:58 for self-serve platforms and federated governance.

[How to Build Data Governance in the Cloud]({{ '/podcasts/cloud-data-governance/' | relative_url }})
is the practical governance episode. [Jessi Ashdown]({{ '/people/jessiashdown/' | relative_url }})
and [Uri Gilad]({{ '/people/urigilad/' | relative_url }}) define governance
beyond security and PII. They cover classification, catalogs, policies, and
data stewards. They also cover data quality signals, retention, and freshness.

They discuss purpose-based access, automation, access workflows, and ROI later.

[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
adds a useful caution: decentralization creates ownership and governance risk
if teams don't have mature operating practices. Pair it with the Data Mesh
episode if you want the tradeoff between domain autonomy and shared standards.

For written synthesis, use these pages:

- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Mesh vs Centralized Data Platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})

## Build a Listening Path

Choose the path based on the question you're trying to answer.

- New to data engineering: listen to
  [Data Team Roles]({{ '/podcasts/data-team-roles/' | relative_url }}),
  [Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
  and
  [Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
- Choosing tools: listen to
  [Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
  [Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
  [Apache Airflow]({{ '/wiki/orchestration/' | relative_url }}), and
  [Data-Led Growth]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
- Operating pipelines: listen to
  [DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
  [Data Observability]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}), and
  [Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
- Designing platforms: listen to
  [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
  [Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
  [Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}), and
  [Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
- Moving into consulting: listen to
  [Freelance Data Engineering Playbook]({{ '/podcasts/freelance-data-engineering-pricing-and-clients/' | relative_url }}),
  [Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}), and
  [Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).
- Comparing batch and streaming: listen to
  [Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
  [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
  [Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}), and
  [From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).

The best way to listen is to pair one concept episode with one applied episode.
For example, listen to
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
then listen to
[Data-Led Growth]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
That pairing shows how warehouse data moves back into customer-facing work. Or
listen to the batch-versus-streaming material, then listen to the
fraud-prevention episode to see why latency changes the architecture.

## Related Pages

Use these pages after you choose an episode cluster.

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Freelance]({{ '/wiki/freelance/' | relative_url }})
