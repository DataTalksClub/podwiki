---
layout: wiki
title: "Data Pipelines"
summary: "Guide to data pipelines: ingestion, transformation, publication, orchestration, testing, recovery, CDC, and ML handoffs."
related:
  - ETL
  - ELT
  - ETL vs ELT
  - CDC
  - Orchestration
  - DataOps
  - Data Quality and Observability
  - Data Engineering Platforms
  - MLOps
---

Data pipelines move data from source systems into forms that people, products,
and models can use. A pipeline is more than a scheduled job. It extracts or
receives data and stores enough raw history to recover. It transforms data into
modeled outputs and publishes them. It also gives the team a way to test,
observe, and rerun the work.

The modern analytics version separates extraction and loading from warehouse-side
transformation, then connects that approach to data marts and data lakes.
Orchestration, [[CDC]], and reverse data flows
sit around those storage choices
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).

The same map extends further because ingestion and orchestration come before
modeling. Transformation, analytics outputs, and production ML handoffs belong in
the same conversation
([[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).

This topic covers pipeline design. Use
[[ETL vs ELT]] for the transformation
boundary between [[ETL]] and [[ELT]],
while [[Orchestration]]
and [[Apache Airflow]] cover
scheduling and dependencies. Use
[[DataOps]] for reliable delivery
practice, and
[[Data Engineering Platforms]]
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

Publication is part of the pipeline. A table that loads successfully but breaks
a dashboard, model, or business workflow is still a pipeline failure. A
successful engineering job isn't the same as useful data. Teams use freshness,
volume, and distribution to see whether the output still works. Schema and
lineage show downstream impact
([[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]).

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

The beginner version stays grounded in Python and SQL, plus Docker, Airflow, and
data warehouses
([[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]).
The tools matter because a pipeline has to be readable, testable, and
maintainable by another engineer.

## Ingestion and Change Capture

Ingestion starts the pipeline, but it doesn't decide the whole architecture.
Extraction and loading can come before warehouse-side transformation. Teams keep
raw data close to the destination and put business logic in SQL models when that
fits the organization
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).

IoT work shows the full pipeline boundary in a compact form. Sensor data flows
from installed devices and loggers into an ETL step, then into a database and
reporting layer. In that setting, the same person may configure data collection
and load the records. They also make the result usable for structural-health
monitoring
([[cite:from-iot-data-engineering-to-leading-data-architect@09:21=>From IoT Data Engineering to Data Architecture]]).

For ML-facing pipelines, ingestion can begin before connector work. CRISP-DM
treats data collection as part of data understanding rather than as its own
named step. Pipeline design then has to ask whether important data is missing.
If it's missing, the team may need new collection work. It may also need
infrastructure, labeling, or [[Data Quality and Observability]] before
modeling [[cite:crisp-dm@19:25=>CRISP-DM Methodology]].

The same episode also shows why teams can't treat ingestion as an afterthought:
raw storage needs guardrails. Warehouses and lakes have different strengths,
and schema evolution changes downstream assumptions.

[[CDC]] is one ingestion technique, not a
separate pipeline type. It captures changed rows instead of copying the whole
source table again. The first load gives the destination a baseline. Later syncs
move inserts, updates, and deletes so the destination stays current without
rewriting everything
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).

Deduplication, ordering guarantees, and PII masking sit close to ingestion.
Those checks protect later models and marts from source-system noise
([[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).
This is where pipeline design crosses into governance. If the
source sends duplicate or out-of-order records, the transformation layer may
still run, but the output may no longer represent the business event correctly.

## Transformation and Modeling

Transformation turns stored data into outputs downstream consumers can
understand. In analytics pipelines, that often means SQL models and joins. It
can also mean type conversions, business metrics, and marts.

ELT can give analysts more autonomy once raw data is in the warehouse
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).

Modeling is the point where engineers translate entities, relationships, foreign
keys, and business questions into outputs. The work moves from ingestion into
modeled marts and dashboards, then into ML-specific feature engineering,
training, and serving
([[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).
That progression matters because the same upstream data can feed different
publication paths.

A dashboard may need one freshness target. A feature store or model-training
job may need a different structure and auditability level.

For ML and AI systems, transformation includes feature engineering and
production handoffs. In a fraud-prevention pipeline, daily jobs compute stable
fraud features while live transaction signals feed real-time decisions at
checkout
([[cite:building-and-scaling-data-engineering-systems-for-fraud-detection=>Data Engineering for Fraud Prevention]]).
Use [[Batch vs Streaming]]
for the latency decision and
[[mlops-architecture=>ML pipelines]] for the
larger model lifecycle.

## Orchestration and Publication

Orchestration coordinates pipeline work after the steps are clear. Airflow sits
at the scheduling layer beside Airbyte-style ingestion and dbt-style
transformation
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).
Airflow can run a connector sync and trigger transformations. It
can also sequence checks, but it shouldn't hide the business logic inside a
tangle of tasks. The pipeline remains easier to review when ingestion,
transformation, checks, and publication each have an explicit role.

For a local Airflow project, DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
keeps the scheduler, UI, and metadata database visible. It also keeps the DAG
folder and logs visible.

A production pipeline anatomy starts with ingestion and buffering, then moves to
transforms, storage, and visualization. SQL or dataframe transforms fit into that
anatomy. Airflow or simpler schedulers and model-serving options do too
([[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]).
The practical advice is to start simple and add Airflow, Kubernetes, or heavier
infrastructure when the dependencies justify it.

Publication closes the pipeline with a warehouse table, mart, or dashboard. It
can also be a model artifact, feature set, prediction API, or reverse data flow
back into an operational system.
Reverse data flows show that the pipeline may not end inside the warehouse. It
may send modeled data back to business tools when sales, marketing, or
operations teams need it
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]).

## Testing, Recovery, and Observability

DataTalks.Club guests treat reliable pipelines as operated systems, not as
scripts that happen to run on a schedule.
[[person:christopherbergh=>Christopher Bergh]]
anchors that operating model in
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
and
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].
He connects pipeline quality to version control, tests, CI/CD, and
observability. He also adds automated runbooks, realistic test data, and
deployment confidence.

Data tests need to cover both code and data behavior. Bergh mentions dbt,
Great Expectations, SQL tests, and test strategies in
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Ramirez gives the applied data-engineering version for PySpark jobs, cloud
monitoring, and schema changes. She also covers job failures, runbooks, and
error documentation
([[cite:building-and-scaling-data-engineering-systems-for-fraud-detection=>Data Engineering for Fraud Prevention]]).

Observability catches failures that task status alone misses. Barr Moses names
freshness, volume, and distribution in
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
She also adds schema and lineage, then separates detection from diagnosis. That
distinction matters for pipelines because the team needs to find the cause of a
late table.

The cause may sit in an upstream source or ingestion connector. It may also be
a transformation bug, a schema change, or publication. Use
[[Data Quality and Observability]]
for those reliability signals.

Teams should design recovery into the pipeline. Useful pipelines keep enough
raw or intermediate state to backfill, replay, or compare outputs after a
change. CDC feeds need checkpoints and delete handling. Batch jobs need
rerunnable windows, and streaming jobs need lag and replay monitoring. ML
feature pipelines need a way to connect training data, online features, and
production outcomes.

## Batch, Streaming, and CDC

[[Batch vs Streaming]] is a
latency and operating decision. Kretz introduces events and queues in
[[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]],
then contrasts streaming and batch. Streaming helps when a system
must react to events as they arrive. Batch helps when a bounded run is easier
to reason about, cheaper to operate, and fresh enough for the consumer.

In Ramirez's fraud-detection system, daily batch jobs prepare stable network
and member features. The checkout path still needs
instant inference for a transaction
([[cite:building-and-scaling-data-engineering-systems-for-fraud-detection=>Data Engineering for Fraud Prevention]]).
That's stronger than "stream everything"
because it names which part of the decision needs low latency.

[[person:mehdiouazza=>Mehdi OUAZZA]] adds the team-scale
cost of streaming in
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].
He connects Kafka to schemas and schema registries. He also discusses explicit
producer-consumer agreements.
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
[[Data Engineering Platforms]].

Mehdi OUAZZA gives the scale-up version. In
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]],
the data platform enables self-service, onboarding, and scalability.

Airflow and shared conventions are part of that platform, and playbooks and best
practices belong there too. A split between platform work and use-case pipelines
helps teams avoid rewriting the same orchestration, access, and recovery rules
for every project.

Reusable ingestion, transformation, and datamart templates put platform
discipline inside individual pipelines. They work best when they reuse
production-proven pieces such as API ingestion into bronze, merges into silver,
or shared geography dimensions. They still need room for project-specific logic
([[cite:from-iot-data-engineering-to-leading-data-architect@57:12=>From IoT Data Engineering to Data Architecture]]).

Cloud-native storage conventions matter when the pipeline works over dense
imagery instead of ordinary tables. Daynan Crull's asteroid-mining discussion
contrasts cloud-native access with local downloads that make analysts manage
massive image files.

He names Cloud Optimized GeoTIFFs, or COGs, from Earth observation. He also
names STAC-style asset catalogs as a better storage and query approach. The
data stays close to cloud compute. Analysts query only the relevant tiles, so
the pipeline avoids downloading or cutting whole files before analysis
[[cite:machine-learning-for-asteroid-mining-and-water-detection@42:23=>Asteroid Mining and Water Detection]].
That convention links pipeline design to [[Data Engineering Platforms]],
storage layout, analyst-facing query access, and
[[astroinformatics-scientific-data-pipelines=>astroinformatics pipelines]].

[[person:pauliusztin=>Paul Iusztin]] and
[[person:marianosemelman=>Mariano Semelman]] extend the platform
discussion into AI systems. Paul frames the AI engineer as a full-stack role
that has to ship products, not only prototypes
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
Mariano focuses on end-to-end ownership and business
requirements. He also discusses feedback and the declining role of notebooks in
production
([[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]).
For data pipelines, their shared implication is that product
systems need a repeatable path from data and prompts or features into
production behavior.

## Design Tradeoffs

DataTalks.Club discussions converge on the same pipeline lifecycle, even though
each use case applies different design pressure. Kwong's
[[cite:data-engineering-tools-modern-data-stack=>modern stack discussion]]
puts the extraction and loading boundary first. That makes
[[ETL vs ELT]] a pipeline
decision rather than only a tooling label. After teams choose that
transformation boundary, the wider lifecycle still runs from ingestion through
publication plus recovery and reliability.

Tuli's
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>architecture walkthrough]]
starts with ingestion choices before ordering, deduplication, and PII masking.
Modeling and marts come later, followed by dashboards and ML handoffs.
Together, those episodes show how storage choices and early data
handling decide who can change the pipeline safely.

Reliability changes the tradeoff from job status to output usefulness. Bergh's
[[DataOps]]
interviews on
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
and [[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]
frame reliable pipeline delivery around version control and tests as team
practice. They also rely on CI/CD, observability, and recovery runbooks in
production.

Moses's
[[cite:data-quality-data-observability-data-reliability=>data observability discussion]]
adds the downstream view because a green run can still publish stale, partial,
shifted, or schema-breaking data. Use
[[Data Quality and Observability]]
for freshness, volume, or distribution signals. Schema plus lineage helps show
which consumers may break and where the cause sits.

Production pipelines also differ by latency and ownership. Kretz's
[[cite:production-ml-pipelines-with-aws-and-kafka=>notebook-to-production episode]]
puts ingestion plus buffering before later work. Transforms, storage,
visualization, and serving follow.[[cite:production-ml-pipelines-with-aws-and-kafka@13:25=>notebook-to-production episode]]
His practical line is to keep the first production version simple enough to
operate. Ramirez's
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection=>fraud-prevention pipeline]]
uses daily feature jobs beside live checkout decisions, so
[[Batch vs Streaming]]
depends on the decision that consumes the data.

Mehdi OUAZZA's
[[cite:scaling-data-engineering-teams-self-service-platforms=>team-scaling discussion]]
adds self-service onboarding and Airflow standards. He also covers Kafka
schemas and producer-consumer agreements, which link individual pipelines to
[[Data Engineering Platforms]].

Katz's
[[cite:get-data-engineering-job-prep-and-interview=>job-prep discussion]]
keeps the foundation concrete by making Python and SQL the base. Docker and
Airflow support day-to-day work beside warehouses and tests, while small
functions plus classes make pipeline code easier for another engineer to
maintain.

[[book:20220815-fundamentals-of-data-engineering=>Fundamentals of Data Engineering]]
by Joe Reis and Matthew Housley frames this same pipeline lifecycle across
ingestion, transformation, and serving layers.

## Adjacent Topics

Use [[ETL vs ELT]] when the question is
where transformations should run. Use [[ETL]] or [[ELT]] when the question is
one lifecycle rather than the comparison. Use [[CDC]]
when the source data changes incrementally and full reloads are wasteful. Use
[[Orchestration]] and
[[Apache Airflow]] when the
problem is scheduling, dependencies, retries, or backfills.

Use [[DataOps]] when the concern is
version control and tests. It also covers CI/CD and observability. Recovery
belongs there too. Use
[[Data Quality and Observability]]
when the concern is freshness, volume, or distribution. It also covers schema,
lineage, SLAs, and runbooks.

Use
[[Data Engineering Platforms]]
when the same conventions have to support many teams and many pipelines.

Use [[Batch vs Streaming]] when
latency and replay drive the design. It also covers cost and operations. Use
[[MLOps]] and
[[mlops-architecture=>ML pipelines]] when the
pipeline publishes features, training data, or model artifacts. They also
apply when the pipeline publishes online predictions or feedback data.
