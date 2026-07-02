---
layout: article
tags: ["comparison"]
title: "Batch vs Streaming"
keyword: "batch vs streaming"
secondary_keywords:
  - streaming vs batch
  - batch processing vs stream processing
  - batch vs stream processing
summary: "How DataTalks.Club podcast guests compare batch and streaming data processing through latency, operations, contracts, cost, ML serving, and product-decision tradeoffs."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Data Pipelines
  - Streaming
  - DataOps
  - Orchestration
  - Apache Airflow
  - Machine Learning System Design
  - Machine Learning Infrastructure
  - Data Quality and Observability
  - Data Engineering Portfolio Projects
---

Batch processing handles bounded chunks of data. In these episodes, that
includes scheduled warehouse jobs and backfills. It also includes training set
creation and batch inference.

Streaming processing handles events as they arrive from queues, brokers, or
production services. That makes batch vs streaming a pipeline design question,
not only a tool choice. It connects directly to
[[data pipelines]] and
[[streaming]]. It also sits near
[[data engineering platforms]],
[[DataOps]], and
[[machine learning system design]]
when the pipeline feeds a model-backed product.

[[person:andreaskretz|Andreas Kretz]] gives the cleanest
pipeline vocabulary in
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]].
Events land in systems such as Kafka or Kinesis. The team then decides whether
to react immediately or store the data first and transform it later.

That framing keeps batch vs streaming away from tool fashion. The useful
questions are latency, dependencies, and operating cost. They also include
replay, ownership, and the action that consumes the result.

## Choose by Latency and Dependencies

Batch is the default when the consumer can wait, and it fits teams that benefit
from explicit dependencies. [[person:larsalbertsson|Lars Albertsson]]
describes this workflow-oriented version in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].

Batch jobs can declare which upstream data is required. They can also declare
the time window and downstream dependencies. That makes batch natural for
[[Apache Airflow]] and warehouse
transformations in the
[[modern data stack]]. It also
fits backfills, training datasets, and scheduled scoring. Use
[[Orchestration]] for the broader
scheduling and dependency model behind those jobs.

Streaming fits cases where a delayed result changes the product outcome. Lars
separates slow reporting, the middle streaming window, and
sub-100-millisecond paths that belong inside the serving application in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]].
[[person:angelaramirez|Angela Ramirez]] shows the product
version in
[[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]].
Daily batch jobs prepare feature values, but the purchase flow still needs a
live fraud decision that can block a transaction. [[person:willempienaar|Willem Pienaar]]
shows the MLOps version in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]],
where offline stores support training and online stores serve low-latency
features.

The decision isn't "batch is old" or "streaming is modern." Name the downstream
action and the maximum useful latency. The team then chooses among scheduled
jobs, micro-batches, streaming jobs, and in-request logic.
[[person:adrianbrudaru|Adrian Brudaru]]
supports the SLA side of that decision in
[[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]].
In that episode, he warns that much so-called streaming is micro-batching unless
strict SLAs justify tools such as Kafka or Flink.

## Practitioner Boundaries

[[person:larsalbertsson|Lars Albertsson]] is the most
skeptical of streaming as a default. In
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]],
he argues that streaming has higher operational cost because dependency
management is less explicit than in workflow-orchestrated batch. He also argues
that batch latency can often be pushed into minute-level, and sometimes
second-level, windows before a team needs a full stream-processing architecture.

[[person:andreaskretz|Andreas Kretz]] treats the choice
as architecture-neutral. His
[[podcast:production-ml-pipelines-with-aws-and-kafka|production ML pipeline episode]]
maps ingestion, queues, and storage. It also maps processing frameworks such as
Spark and Flink, plus orchestration options. His contribution is vocabulary:
batch or streaming is one processing-mode decision inside a larger production
pipeline, not the whole architecture.

[[person:mehdiouazza|Mehdi OUAZZA]] focuses on the
organizational cost of streaming. In
[[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]],
Kafka creates onboarding work because teams need schemas and registry practice.
They also need allowed changes and change rules. His focus keeps streaming
close to [[data governance]] and
producer-consumer ownership, not only to brokers and compute engines. Use
[[Data Mesh]] and
[[data products]] for the broader
ownership model around those interfaces.

[[person:angelaramirez|Angela Ramirez]] and
[[person:willempienaar|Willem Pienaar]] make the case
for hybrid ML systems. Angela's
[[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|fraud engineering episode]]
combines daily feature computation with live transaction checks. Willem's
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|feature-store episode]]
separates source modes from storage modes. It also covers backfills, validation,
and low-latency feature retrieval.

[[person:simonstiebellehner|Simon Stiebellehner]]
adds a platform-maturity warning in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Teams should decide whether a model is consumed by a downstream service or only
by a batch job before investing in online serving infrastructure. That's the
same deployment boundary covered in
[[Machine Learning System Design]].

## Latency and Product Action

Batch fits reports and warehouse models. It also fits backfills, campaigns, and
model jobs where delayed results still support the decision. [[person:simonstiebellehner|Simon Stiebellehner]]
describes batch inference as a sequence of data loading and preprocessing. The
same sequence includes feature engineering, inference, and output writing in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
That structure is easy to reason about with
[[experiment tracking]],
[[model-registry|model registries]], and
[[data quality and observability]].

Streaming fits actions tied to event arrival. DataTalks.Club guests discuss
fraud checks, recommendations, risk scores, and pricing. They also discuss
ranking and request-time enrichment. Angela's
[[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|fraud workflow]]
must answer during a purchase.

Willem names fraud detection and recommendations as strong online tabular
feature-store use cases. He also names risk scores, pricing, and ranking in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]].

When the useful response time is tighter than the streaming window, Lars says
the logic belongs in the user-facing application path. It shouldn't be a
separate streaming pipeline
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).

## Operating Batch and Streaming Pipelines

Batch operations use schedules and dependency graphs. In batch pipelines,
retries, checks, and reruns are normal operating work. [[person:santonatuli|Santona Tuli]] explains in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]
that pipeline work is often about orchestration. Teams need to know dependencies
and start times. They also need to know when dependent steps can run.

Lars makes the same operating model central to
[[DataOps]] in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]].
Workflow orchestration gives teams a way to repair late data, transient
failures, and bugs.

Streaming operations center on brokers, consumers, schemas, and synchronized
event flows. Continuously running infrastructure adds more operating concerns.
[[person:mehdiouazza|Mehdi OUAZZA]] uses Kafka in
[[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]
to show why a few topics can become many topics. Missing schemas or
allowed-change rules create downstream problems for S3, transformations,
warehouses, and analytics.

Santona gives the pipeline-design version in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].
Combining Kafka queues means thinking about which downstream use cases depend on
which streaming upstreams and how to keep them in sync.

## Schemas, Ownership, and Replay

Batch pipelines can still break consumers through missing inputs, bad upstream
data, and dependency changes. Teams need tests, orchestration, and visibility
into whether expected data arrived. They also need to know whether the data is
fit for downstream use. Lars's
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps discussion]]
also treats CDC and database versioning as part of the same dependency and
change-management problem. Use
[[data quality and observability]]
and [[DataOps]] for the adjacent reliability
work.

Streaming moves those interface problems into event semantics. Mehdi's
[[podcast:scaling-data-engineering-teams-self-service-platforms|Kafka section]]
is explicit about ownership because software engineers may publish events for
service communication. Data teams consume the same topics for analytical
pipelines.

Without Avro or another schema practice, the stream becomes a
shifting interface. Registry lookup, allowed schema changes, and a change path for
changes make the interface usable. That's why the batch vs streaming decision
also touches
[[data governance]],
[[data products]], and
[[event tracking]].

## Cost and Platform Complexity

Batch is often cheaper to start and simpler to pause because scheduled compute
doesn't have to run continuously. Adrian describes cost-aware orchestration,
including cheaper serverless options, before his streaming discussion in
[[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]].
The same episode says streaming is often micro-batching unless strict SLAs
justify a more specialized stack.

Streaming earns its extra cost when the delayed result loses value. Lars says
stream processing is popular but brings higher operational cost in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]].
Mehdi adds that a team adopting Kafka may need people who understand cluster
operation and producer or consumer conventions. The same team also needs schema
practice and onboarding
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]).

For learning and portfolio work, Adrian's requirements-led tooling advice
supports the same lesson. Build a clear batch pipeline first. Add Kafka or
streaming only when the use case explains the cost
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]],
44:42 and 51:19). Use
[[Data Engineering Portfolio Projects]]
for project examples that show reviewers why the latency requirement exists.

## ML Features and Serving

ML systems often use both modes. Angela's
[[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|fraud episode]]
precomputes stable feature values daily, then combines them with real-time
payload information during a purchase. That's different from a pure dashboard
pipeline because the output can change the transaction while the user is still
waiting.

Feature stores make the hybrid design explicit. Willem describes Feast and
Tecton as systems that ingest precomputed features from batch or streams. They
materialize offline and online stores, build point-in-time-correct training
sets, and serve low-latency online features through a unified API in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]].

Pure batch scoring or campaign use cases may not need a feature store. SQL,
dbt, and validation may be enough. Those choices belong with
[[MLOps]],
[[Machine Learning System Design]], and
[[machine learning infrastructure]].

## Hybrid Designs

The strongest DataTalks.Club examples aren't pure batch or pure streaming.
Teams split the system by stability and latency. Historical features, backfills,
and training sets are computed in batch. Current context, event-triggered
actions, and low-latency retrieval live in streaming or online paths. Angela's
[[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|fraud prevention design]],
Willem's
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|feature-store design]],
and Simon's
[[podcast:building-production-ml-platform-and-mlops-team|ML platform discussion]]
all show that split.

In architecture review, ground the decision in four checks:

- name the action that consumes the result
- name the latest useful arrival time
- name the owner of the event or table interface
- define checks for bad data, lag, stale ML features, and downstream breakage

If the answer is "a person reads a dashboard tomorrow," batch is probably
enough. If the answer is a live purchase or ranking decision, streaming or
online serving may be justified. A hybrid feature path may also fit.

## Related Pages

Read these pages for the surrounding pipeline, operations, ML, and portfolio
context:

- [[Data Engineering]]
- [[Data Engineering Platforms]]
- [[Data Pipelines]]
- [[Streaming]]
- [[DataOps]]
- [[Orchestration]]
- [[Modern Data Stack]]
- [[Apache Airflow]]
- [[MLOps]]
- [[Machine Learning System Design]]
- [[Data Quality and Observability]]
- [[Data Engineering Portfolio Projects]]

