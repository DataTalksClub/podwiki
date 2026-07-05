---
layout: article
tags: ["how-to"]
title: "How to Build Data Pipelines"
keyword: "build data pipelines"
summary: "Build data pipelines from consumer needs through ingestion, modeling, orchestration, testing, observability, and activation."
secondary_keywords:
  - "data pipeline training"
related_wiki:
  - Data Engineering Platforms
  - Data Pipelines
  - Apache Airflow
  - Orchestration
  - DataOps
  - Data Quality and Observability
  - Data Activation
  - End-to-End Data Pipeline Project
---

To build data pipelines that people trust, start with the decision, model, or
workflow the pipeline must support. Then work backward into source ownership and
event definitions. Add ingestion and storage. Then add transformation and
orchestration. Finish with quality checks, observability, and last-mile
delivery.

Pipeline implementation starts from the broader [[Data Pipelines]] system
definition. [[Orchestration]] adds schedules and run state. [[Apache Airflow]]
adds the tool-specific boundary when the implementation uses Airflow.

Pipeline design starts with raw arrival, then moves to cleaned ingestion and
modeled business entities. The pipeline finally produces answers for dashboards
or ML systems.[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

ELT keeps raw data separate from business-facing marts. That way teams don't
invent inconsistent transformations downstream.[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]]
For related background, see
[[Data Engineering Platforms]]
and [[Data Pipelines]].

For data pipeline training, the build sequence should become one small project.
Santona Tuli points learners to Fundamentals of Data Engineering and Airflow
guides. She also recommends engineering blogs, but the project still has to
prove source-to-output thinking
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@56:49=>Modern Data Pipeline Architecture]].
Build a pipeline that another person can run, look at, break, and repair. Show
ingestion and modeling first, then show that orchestration, checks, and delivery
fit together.

## Start With The Consumer

A pipeline should answer a real question or power a real workflow. After data
arrives, engineers still need to identify mapping keys, foreign keys, and
business entities. They also name the question the business wants answered. Data and
analytics engineers should talk to end users before deciding which tables and
transformations matter.[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]

For product and growth data, that consumer-first work begins even earlier. A
[[tracking-plans=>tracking plan]] comes before instrumentation. Teams define
events, properties, data types, and ownership.
Product and growth teams then know what each event
means before downstream tools use it.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

If teams use vague event names in
[[product analytics]], they
create operational risk. Teams create more risk when they use the same events
for funnels, experiments, or reverse ETL.

Start with this brief before you pick tools:

1. Who uses the output?
2. What decision, model, dashboard, or operational action depends on it?
3. Which source system owns the data?
4. What freshness and quality expectations does the consumer need?
5. What if data is late or missing? What if it's duplicated or structurally changed?

Turn the brief into implementation criteria before implementation starts, and
link consumer expectations to the [[DataOps]] work that follows. That means
version-controlled changes, tests, monitoring, and recovery paths. Without those
criteria, a pipeline can be technically complete while still failing the
workflow it was meant to support.

## Design The Ingestion Layer

Ingestion isn't the same as final modeling. The ingestion layer stays separate
from data marts because raw data isn't ready for most business users. If every
analyst transforms raw tables differently, the organization gets conflicting
answers. ELT keeps the raw form available while moving shared
business logic into a controlled transformation layer
[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]].

Ingestion can still perform limited quality work because the early stage handles
deduplication and ordering guarantees. It can also mask or hash PII before the
data appears in Snowflake or another human-facing destination
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
Treat those steps as guardrails, not as the place where every business metric
is defined.

The operating sequence is raw arrival, controlled ingestion, modeled entities,
and final outputs. Santona Tuli separates raw, ingested, and modeled layers. She
treats ingestion preprocessing as deduplication, ordering, and PII strategy
rather than business-metric definition
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@32:57=>Modern Data Pipeline Architecture]]
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@37:10=>Modern Data Pipeline Architecture]].

Pick storage from the data structure and each team's needs. Warehouses are a
strong fit for structured analytics teams. Lakes help when engineering or data
science teams need unstructured files, logs, video, and other raw formats.

Lakes and warehouses become swamps when teams keep data people can't trust.
[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]]
For that comparison, use
[[Data Warehouse vs Data Lakehouse]].

## Model Data Into Useful Outputs

After ingestion, model data around entities, relationships, and business
questions. This means finding the keys and relationships across multiple
sources, then building the modeled layer that can answer real business
questions. Keep ingested data and modeled data separate from answers. Marts or
dashboard-specific transformations sit after the core business entities
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

This is where
[[analytics engineering]]
and [[data engineering]] overlap.
ELT connects analysts using dbt and SQL inside the warehouse, with data marts as
the business-facing layer. Those marts should be easier to use than raw ingestion
tables.[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]]

The practical output isn't "a pipeline" in the abstract. It may be a modeled
table or mart, or it may be a feature set, dashboard input, or activation
segment that a consumer understands.

For ML pipelines, the modeling mindset shifts for machine outputs. You still
deduplicate and handle nulls, and you still transform features for model
training rather than a human-readable business entity
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
That boundary is why pipeline work often touches
[[MLOps vs DataOps]].

## Orchestrate The Work, Not The Buzzwords

Orchestration coordinates jobs after each pipeline step is clear. Airflow is an
orchestrator that schedules work and runs ingestion jobs. Tools such as Airbyte
focus on the extract-load part, and dbt handles warehouse transformations
[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]].

At this step, decide where orchestration belongs in the build sequence. Don't
turn every pipeline into an Airflow project. That split keeps the DAG thin.
Extraction, modeling, tests, and publication should stay in real code or
tool-owned commands that reviewers can read outside the scheduler. Use
[[Apache Airflow]] for DAG design and [[Orchestration]] for the broader tool
choice.

Use the orchestrator to make the operating sequence visible. It should show
how data moves through extraction/loading and transformation. It should also
show where tests run, what gets published, and how reruns work.

Natalie Kwong describes Airflow as an orchestrator. It runs Airbyte jobs while
Airbyte handles extraction/loading and dbt handles transformations
[[cite:data-engineering-tools-modern-data-stack@30:59=>Modern Stack]]
[[cite:data-engineering-tools-modern-data-stack@31:31=>Modern Stack]].
That separation keeps the training project close to production practice because
each step has a clear owner and failure mode.

For production ML pipelines, use Lambda functions and queues first. Move to
Airflow or Kubernetes when the simple chain becomes hard to operate
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>Production ML Pipelines with AWS and Kafka]].

For stakeholder proof, Kretz starts even smaller with a zero-cost proof of
concept. Quantify possible ROI before deciding which pipeline pieces deserve
automation
[[cite:production-ml-pipelines-with-aws-and-kafka@58:56=>Production ML Pipelines with AWS and Kafka]].

Modern data engineering discussions make the same simple-first point from a
cost perspective. Teams can run small workflows cheaply with [[DuckDB]] plus
GitHub Actions. GitHub Actions can be enough when the team doesn't need
always-on orchestration
[[cite:trends-in-modern-data-engineering@27:40=>Modern Data Engineering Trends]]
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]].

For a local learning or portfolio setup, follow DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
to run the scheduler, UI, and metadata database. Use that setup when the local
environment helps someone look at the dependency graph, task logs, rerun path,
and data checks. It's not a substitute for source, staging, modeled, and serving
layers. It's the place where those steps become visible together.

Make dependencies visible and repeatable, and don't rename
the whole pipeline after the scheduler.
For a portfolio implementation, link the run command and failing check from the
README. Also link the logs and rerun path so the project connects to
[[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]] instead
of becoming an Airflow demo.

At team scale, teams need orchestration conventions because a platform is more
than an Airflow cluster. Those conventions include naming standards and sequence
practices. They also include playbooks, support channels, and onboarding. Other
data users can then build without turning the platform team into a bottleneck.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]

See
[[self-service-data-platforms=>Self-Service Data Platforms]]
for that operating model.

Streaming adds stricter schema agreements. Teams can grow from a few Kafka
topics to hundreds quickly. Define typed schemas and schema registry usage before
downstream teams depend on the stream. Also define allowed changes and a
schema-change process
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].
[[Batch vs Streaming]]
covers the latency decision.

## Add Tests, Observability, And Recovery

A pipeline can finish successfully and still deliver bad data. The core
observability signals are freshness and volume. Teams also track distribution,
schema, and lineage.
[[cite:data-quality-data-observability-data-reliability=>Data Observability]]
Teams use those signals to see whether data is up to date and complete, whether
values look plausible, and whether schemas stay stable. Lineage connects the
right upstream and downstream assets.

Freshness expectations should become explicit SLAs when downstream work depends
on them. A dataset that must arrive within five minutes after a user action is
one example. The SLA helps the data team prioritize which freshness incidents
matter first instead of treating every late table as equal
[[cite:data-quality-data-observability-data-reliability=>Data Observability]].
Link those expectations to
[[Data Quality and Observability]].

[[DataOps]] turns the same reliability problem into delivery practice. Teams use
automation and tests to reduce errors, while monitoring and observability show
what broke, and version control and CI/CD make deployments safer. Teams also
need realistic test data and infrastructure as code, with end-to-end checks
running before changes reach production.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

DataOps reliability work also includes runbooks and automated playbooks. Bergh's
pipeline advice moves from production tests to development tests, automated
deployment, version control, and playbooks for known recovery actions
[[cite:dataops-automation-and-reliable-data-pipelines@33:47=>DataOps Automation]].
Teams also version code, models, visualizations, and governance end to end
[[cite:dataops-automation-and-reliable-data-pipelines@51:21=>DataOps Automation]].
Use [[DataOps Platforms]] when these checks become a shared path across many
pipelines.

## Deliver Data Where People Act

A table may not be enough when the business action happens outside the
warehouse. A data-led growth stack starts with collection and storage, then
teams analyze and activate the data
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]].

Product events can power support context and sales prioritization. They can also
power engagement campaigns and personalized onboarding when teams define the
events and properties clearly enough.

Reverse ETL is one concrete last-mile mechanism. In reverse ETL, modeled
warehouse outputs move back into operational systems such as Salesforce.
Salespeople or marketers act on lead scores and other modeled outputs
[[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]].
The same operational-analytics path connects to tools such as Census, Hightouch,
and Grouparoo
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]].
[[Data Activation]]
and [[Reverse ETL]] cover the delivery
side of the pipeline.

## Build Sequence

This sequence gives a practical starting point for training, portfolio work, or
team implementation:

1. Define the consumer, decision, and freshness need, linking pipeline design to
   the business question and the entities that answer it
   [[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
2. Document product events or source agreements before collection: event names,
   properties, types, and ownership before instrumentation
   [[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]].
3. Write raw data to a warehouse, lake, or lakehouse that fits the data
   structure, keeping raw ingestion separate from marts and matching warehouse
   and lake use cases
   [[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]].
4. Apply ingestion guardrails such as deduplication, ordering, masking, and
   basic validation before human-facing destinations
   [[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
5. Model entities, relationships, metrics, marts, or features around the
   consumer's question, placing modeled business entities between raw ingestion
   and final answers
   [[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
6. Orchestrate extraction, loading, transformation, tests, and delivery with
   visible dependencies, separating Airflow, Airbyte, and dbt by job
   responsibility
   [[cite:data-engineering-tools-modern-data-stack=>Data Engineering Tools and the Modern Data Stack]].
7. Publish schemas, ownership, and change rules, so Kafka schemas define types
   and change processes before streams become shared dependencies
   [[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].
8. Add production checks, development checks, CI/CD, observability signals,
   SLAs, and runbooks, turning observability signals into explicit checks and
   recovery paths
   [[cite:data-quality-data-observability-data-reliability=>Data Observability]].
9. Run the full pipeline against realistic test data before production, because
   integration tests and end-to-end checks reveal breakage that unit tests miss
   [[cite:dataops-automation-and-reliable-data-pipelines@43:06=>DataOps Automation]].
10. Deliver modeled outputs to dashboards, ML systems, support tools, sales
   tools, or product experiences, following the collection-to-activation flow
   [[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]].
11. Review usage, incidents, and stale data so the pipeline keeps matching the
    workflow it supports, making ongoing review part of trust rather than
    cleanup after the fact
    [[cite:data-quality-data-observability-data-reliability=>Data Observability]].

That sequence isn't a universal stack prescription. Teams start by building the
smallest pipeline that satisfies the use case. They add
platform conventions, automation, and observability as more people and systems
depend on it.
