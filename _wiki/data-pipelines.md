---
layout: wiki
title: "Data Pipelines"
summary: "Podcast-grounded guide to data pipelines as movement, transformation, publication, and operations across ingestion, orchestration, testing, recovery, batch, streaming, CDC, and ML handoffs."
related:
  - CDC
  - Orchestration
  - DataOps
  - Data Quality and Observability
  - Data Engineering Platforms
  - MLOps
---

Data pipelines move data from source systems into forms that people, products,
and models can use. DataTalks.Club guests treat that as more than a
scheduled job. A pipeline extracts or receives data and stores enough raw
history to recover. It also transforms data into modeled outputs and publishes
them. The team then needs a way to test, observe, and rerun the work.

[Natalie Kwong](https://datatalks.club/people/nataliekwong.html) gives the modern
analytics version in
[ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html).
She separates extraction and loading from warehouse-side transformation. She
then connects that approach to data marts and data lakes. Orchestration,
[CDC]({{ '/wiki/cdc/' | relative_url }}), and reverse data flows sit around
those storage choices.

[Santona Tuli](https://datatalks.club/people/santonatuli.html) expands the same map in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html):
ingestion and orchestration come before modeling. Transformation, analytics
outputs, and production ML handoffs belong in the same conversation.

This topic covers pipeline design. Use
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) for the transformation
boundary, while [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
and [Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}) cover
scheduling and dependencies. Use
[DataOps]({{ '/wiki/dataops/' | relative_url }}) for reliable delivery
practice, and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
for shared infrastructure around many pipelines.

## Definition

A useful data pipeline has three responsibilities.

- Movement: the pipeline gets data out of source systems, APIs, files, event
  streams, databases, or application logs and writes it to durable storage.
- Transformation: the pipeline cleans, joins, deduplicates, masks, aggregates,
  or models the data so downstream consumers can use it.
- Publication: the pipeline serves the result as a table, mart, dashboard,
  feature set, search index, model input, or API-facing output. It may also
  sync the result back into an operational system.

DataTalks.Club guests repeat the same warning: publication is part of the
pipeline. A table that loads successfully but breaks a dashboard, model, or
business workflow is still a pipeline failure. [Barr Moses](https://datatalks.club/people/barrmoses.html)
makes that reliability point in
[Data Observability Explained](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html):
at 21:57, the discussion separates a successful engineering job from useful
data. Teams use freshness, volume, and distribution to see whether the output
still works. They also use schema and lineage for downstream impact.

That definition also explains why pipeline work touches several roles.
Analytics engineers may own dbt models and marts. Data engineers may own
ingestion, storage, orchestration, and recovery. ML engineers may own feature
jobs, training data, and serving handoffs.

A pipeline usually separates raw, staged, modeled, and serving layers. Raw data
preserves source behavior for replay and backfills. The staging layer cleans
names, types, and obvious source-system issues.

The modeled layer represents business entities and facts, plus dimensions and
metrics. It also represents features. Serving outputs feed marts and dashboards.
They can also feed feature tables, indexes, APIs, or reverse ETL syncs.

[Jeff Katz](https://datatalks.club/people/jeffkatz.html) keeps the beginner
version grounded in Python and SQL in
[Data Engineering Job Prep and Interview Guide](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html)
around 1:20-2:22. He also names Docker, Airflow, and data warehouses. The
tools matter because a pipeline has to be readable, testable, and maintainable
by another engineer.

## Ingestion and Change Capture

Ingestion starts the pipeline, but it doesn't decide the whole architecture.
Kwong's Airbyte discussion places extraction and loading before warehouse-side
transformation. Teams can keep raw data close to the destination. They can move
business logic into SQL models when that fits the organization
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
3:46-18:47).

The same episode also shows why teams can't treat ingestion as an afterthought:
raw storage needs guardrails. Warehouses and lakes have different strengths,
and schema evolution changes downstream assumptions.

[CDC]({{ '/wiki/cdc/' | relative_url }}) is one ingestion technique, not a
separate pipeline type. At 45:59, Kwong defines it as capturing changed rows
instead of copying the whole source table again. The first load gives the
destination a baseline. Later syncs move inserts, updates, and deletes so the
destination stays current without rewriting everything
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
45:59-49:32).

Santona Tuli adds deduplication, ordering guarantees, and PII masking close to
ingestion. Those checks protect later
models and marts from source-system noise
([Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
37:10-39:23). This is where pipeline design crosses into governance. If the
source sends duplicate or out-of-order records, the transformation layer may
still run, but the output may no longer represent the business event correctly.

## Transformation and Modeling

Transformation turns stored data into outputs downstream consumers can
understand. In analytics pipelines, that often means SQL models and joins.
It can also mean type conversions, business metrics, and marts. Kwong uses
customer acquisition cost and warehouse transformations to explain why ELT can
give analysts more autonomy. That works when the raw data is already in the
warehouse
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
6:37-12:39).

Tuli frames modeling as the point where engineers translate entities,
relationships, foreign keys, and business questions into outputs. Her
discussion moves from ingestion into modeled marts and dashboards. It then
moves into ML-specific feature engineering, training, and serving
([Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
39:23-47:57). That progression matters because the same upstream data can feed
different publication paths.

A dashboard may need one freshness target. A feature store or model-training
job may need a different structure and auditability level.

For ML and AI systems, transformation includes feature engineering and
production handoffs. [Angela Ramirez](https://datatalks.club/people/angelaramirez.html)
shows the fraud-prevention version in
[Data Engineering for Fraud Prevention](https://datatalks.club/podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.html).
Daily jobs compute stable fraud features, while live transaction signals feed
real-time decisions at checkout. That hybrid design appears around 8:24 and
34:46. Use [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
for the latency decision and
[ML pipelines]({{ '/wiki/mlops-architecture/' | relative_url }}) for the
larger model lifecycle.

## Orchestration and Publication

Orchestration coordinates pipeline work after the steps are clear. Kwong places
Airflow at the scheduling layer beside Airbyte-style ingestion and dbt-style
transformation
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
30:59-33:45). Airflow can run a connector sync and trigger transformations. It
can also sequence checks, but it shouldn't hide the business logic inside a
tangle of tasks. The pipeline remains easier to review when ingestion,
transformation, checks, and publication each have an explicit role.

For a local Airflow project, the
[Airflow Docker Compose local stack]({{ '/wiki/airflow-docker-compose/' | relative_url }})
keeps the scheduler, UI, and metadata database visible. It also keeps the DAG
folder and logs visible.

[Andreas Kretz](https://datatalks.club/people/andreaskretz.html) gives a
production pipeline anatomy in
[From Notebooks to Production](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html)
at 13:25. His sequence starts with ingestion and buffering. It then moves to
transforms, storage, and visualization. He also discusses SQL or dataframe
transforms, Airflow or simpler schedulers, and model-serving options. His
practical advice around 41:06 is to start simple and add Airflow, Kubernetes,
or heavier infrastructure when the dependencies justify it.

Publication closes the pipeline, whether the output is a warehouse table, mart,
or dashboard. It can also be a model artifact, feature set, prediction API, or
reverse data flow back into an operational system.
Kwong's reverse data flow discussion around 35:42 shows that the pipeline may
not end inside the warehouse. It may send modeled data back to business tools
when sales, marketing, or operations teams need it.

## Testing, Recovery, and Observability

DataTalks.Club guests treat reliable pipelines as operated systems, not as
scripts that happen to run on a schedule.
[Christopher Bergh](https://datatalks.club/people/christopherbergh.html)
anchors that operating model in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
and
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html).
He connects pipeline quality to version control, tests, CI/CD, and
observability. He also adds automated runbooks, realistic test data, and
deployment confidence. The
discussion reaches practical steps at 33:47 in the earlier episode and
regression tests at 30:55 in the later one.

Data tests need to cover both code and data behavior. Bergh mentions dbt,
Great Expectations, SQL tests, and test strategies around 48:25 in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html).
Ramirez gives the applied data-engineering version for PySpark jobs, cloud
monitoring, and schema changes. She also covers job failures, runbooks, and
error documentation
([Data Engineering for Fraud Prevention](https://datatalks.club/podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.html),
40:50-48:21).

Observability catches failures that task status alone misses. Barr Moses names
freshness, volume, and distribution at 16:38 in
[Data Observability Explained](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html).
She also names schema and lineage. At 24:31, she separates detection from
diagnosis. That distinction matters for pipelines because the team needs to
find the cause of a late table.

The cause may sit in an upstream source or ingestion connector. It may also be
a transformation bug, a schema change, or publication. Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
for those reliability signals.

Teams should design recovery into the pipeline. Useful pipelines keep enough
raw or intermediate state to backfill, replay, or compare outputs after a
change. CDC feeds need checkpoints and delete handling. Batch jobs need
rerunnable windows, and streaming jobs need lag and replay monitoring. ML
feature pipelines need a way to connect training data, online features, and
production outcomes.

## Batch, Streaming, and CDC

[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) is a
latency and operating decision. Kretz introduces events and queues around 15:11
in
[From Notebooks to Production](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html),
then contrasts streaming and batch around 16:51. Streaming helps when a system
must react to events as they arrive. Batch helps when a bounded run is easier
to reason about, cheaper to operate, and fresh enough for the consumer.

In Ramirez's fraud-detection system, daily batch jobs prepare stable network
and member features. The checkout path still needs
instant inference for a transaction
([Data Engineering for Fraud Prevention](https://datatalks.club/podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.html),
8:24 and 33:34-34:46). That's stronger than "stream everything"
because it names which part of the decision needs low latency.

[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) adds the team-scale
cost of streaming in
[Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html).
At 23:26, he connects Kafka to schemas and schema registries. He also discusses
explicit producer-consumer agreements.
Those conventions keep consumers from breaking when producers change events.
Streaming pipelines therefore need platform standards, not only a broker.

CDC sits between full reloads and event streaming. It can keep a warehouse or
lake current with row-level changes without forcing every downstream consumer
to operate as a streaming application. It still needs checkpoints, schema
handling, deduplication, and recovery. Treat CDC as an ingestion strategy that
feeds a pipeline. Then decide separately whether the downstream work is
batch, micro-batch, streaming, or request-time serving.

## Platform Conventions

One pipeline can live as a small repo, but many pipelines need a platform. The
platform supplies shared storage, orchestration, secrets, and deployment paths.
It also supplies lineage, monitoring, access control, and reusable conventions.
That's why this topic sits next to
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

Mehdi OUAZZA gives the scale-up version. At 12:30 in
[Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
the data platform enables self-service and onboarding. It also supports
scalability.

At 17:22, he names Airflow and shared conventions as part of that platform. He
also includes playbooks and best practices. Later, around 52:55, he describes a
split between platform work and use-case pipelines. That split helps teams avoid rewriting the same
orchestration, access, and recovery rules for every project.

[Paul Iusztin](https://datatalks.club/people/pauliusztin.html) and [Mariano
Semelman](https://datatalks.club/people/marianosemelman.html) extend the platform
discussion into AI systems. Paul frames the AI engineer as a full-stack role
that has to ship products, not only prototypes
([AI Engineering Skill Stack](https://datatalks.club/podcast/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.html),
22:29-42:28). Mariano focuses on end-to-end ownership and business
requirements. He also discusses feedback and the declining role of notebooks in
production
([From Notebook to Production](https://datatalks.club/podcast/s24e03-from-notebook-to-production-building-end-to-end-ai-systems.html),
17:27-55:28). For data pipelines, their shared implication is that product
systems need a repeatable path from data and prompts or features into
production behavior.

## Design Tradeoffs

DataTalks.Club discussions converge on the same pipeline lifecycle, but design
pressure changes by use case. Kwong's
[modern stack discussion](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html)
puts the extraction and loading boundary first. That makes
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) a pipeline
decision rather than only a tooling label.

Tuli's
[architecture walkthrough](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html)
starts with ingestion choices before ordering, deduplication, and PII masking.
Modeling and marts come later, followed by dashboards and ML handoffs.
Together, those episodes show how storage choices and early data
handling decide who can change the pipeline safely.

Reliability changes the tradeoff from job status to output usefulness. Bergh's
[DataOps]({{ '/wiki/dataops/' | relative_url }})
interviews on
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
and [DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html)
frame reliable pipeline delivery around version control and tests as team
practice. They also rely on CI/CD, observability, and recovery runbooks in
production.

Moses's
[data observability discussion](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html)
adds the downstream view because a green run can still publish stale, partial,
shifted, or schema-breaking data. Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
for freshness, volume, or distribution signals. Schema plus lineage helps show
which consumers may break and where the cause sits.

Production pipelines also differ by latency and ownership. Kretz's
[notebook-to-production episode](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html)
starts with ingestion plus buffering before transforms and storage.
Visualization and serving come next, and his practical line is to keep the
first production version simple enough to operate. Ramirez's
[fraud-prevention pipeline](https://datatalks.club/podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.html)
uses daily feature jobs beside live checkout decisions, so
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
depends on the decision that consumes the data.

Mehdi OUAZZA's
[team-scaling discussion](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html)
adds self-service onboarding and Airflow standards. He also covers Kafka
schemas and producer-consumer agreements, which link individual pipelines to
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

Katz's
[job-prep discussion](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html)
keeps the foundation concrete by making Python and SQL the base. Docker and
Airflow support day-to-day work beside warehouses and tests, while small
functions plus classes make pipeline code easier for another engineer to
maintain.

[Fundamentals of Data Engineering](https://datatalks.club/books/20220815-fundamentals-of-data-engineering.html)
by Joe Reis and Matthew Housley frames this same pipeline lifecycle —
ingestion, transformation, serving — across data system generations.

## Adjacent Topics

Use [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) when the question is
where transformations should run. Use [CDC]({{ '/wiki/cdc/' | relative_url }})
when the source data changes incrementally and full reloads are wasteful. Use
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}) and
[Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}) when the
problem is scheduling, dependencies, retries, or backfills.

Use [DataOps]({{ '/wiki/dataops/' | relative_url }}) when the concern is
version control and tests. It also covers CI/CD and observability. Recovery
belongs there too. Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
when the concern is freshness, volume, or distribution. It also covers schema,
lineage, SLAs, and runbooks.

Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
when the same conventions have to support many teams and many pipelines.

Use [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) when
latency and replay drive the design. It also covers cost and operations. Use
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[ML pipelines]({{ '/wiki/mlops-architecture/' | relative_url }}) when the
pipeline publishes features, training data, or model artifacts. They also
apply when the pipeline publishes online predictions or feedback data.
