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

Batch processing handles bounded chunks of data: scheduled warehouse jobs,
backfills, training set creation, and batch inference.

Streaming processing handles events as they arrive from queues, brokers, or
production services. That makes batch vs streaming a pipeline design question,
not only a tool choice. It connects directly to
[[data pipelines]] and
[[streaming]], and sits near
[[data engineering platforms]],
[[DataOps]], and
[[machine learning system design]]
when the pipeline feeds a model-backed product.

The cleanest pipeline vocabulary: events land in systems such as Kafka or
Kinesis, and the team then decides whether to react immediately or store the
data first and transform it later
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).
That framing keeps batch vs streaming away from tool fashion. The useful
questions are latency, dependencies, operating cost, replay, ownership, and the
action that consumes the result.

## Choose by Latency and Dependencies

Batch is the default when the consumer can wait, and it fits teams that benefit
from explicit dependencies. Batch jobs can declare which upstream data is
required, the time window, and downstream dependencies
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
That makes batch natural for
[[Apache Airflow]] and warehouse
transformations in the
[[modern data stack]], and it fits
backfills, training datasets, and scheduled scoring. Use
[[Orchestration]] for the broader
scheduling and dependency model behind those jobs.

Streaming fits cases where a delayed result changes the product outcome. Slow
reporting, the middle streaming window, and sub-100-millisecond paths that belong
inside the serving application are distinct tiers
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
In fraud prevention, daily batch jobs prepare feature values, but the purchase
flow still needs a live fraud decision that can block a transaction
([[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]]).
In MLOps, offline stores support training while online stores serve low-latency
features
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

The decision isn't "batch is old" or "streaming is modern." Name the downstream
action and the maximum useful latency, then choose among scheduled jobs,
micro-batches, streaming jobs, and in-request logic. On the SLA side, much
so-called streaming is micro-batching unless strict SLAs justify tools such as
Kafka or Flink
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]]).

## Practitioner Boundaries

Approaches differ. One view is skeptical of streaming as a default: streaming
has higher operational cost because dependency management is less explicit than
in workflow-orchestrated batch, and batch latency can often be pushed into
minute-level, and sometimes second-level, windows before a team needs a full
stream-processing architecture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

Another view treats the choice as architecture-neutral, mapping ingestion,
queues, storage, processing frameworks such as Spark and Flink, and
orchestration options; batch or streaming is one processing-mode decision inside
a larger production pipeline, not the whole architecture
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).

A third view focuses on the organizational cost of streaming: Kafka creates
onboarding work because teams need schemas, registry practice, allowed changes,
and change rules
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]).
That keeps streaming close to [[data governance]]
and producer-consumer ownership, not only brokers and compute engines. Use
[[Data Mesh]] and
[[data products]] for the broader
ownership model around those interfaces.

Hybrid ML systems combine daily feature computation with live transaction checks
([[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]]),
and separate source modes from storage modes with backfills, validation, and
low-latency feature retrieval
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

A platform-maturity warning: decide whether a model is consumed by a downstream
service or only by a batch job before investing in online serving infrastructure
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
That's the same deployment boundary covered in
[[Machine Learning System Design]].

## Latency and Product Action

Batch fits reports, warehouse models, backfills, campaigns, and model jobs where
delayed results still support the decision. Batch inference is a sequence of data
loading, preprocessing, feature engineering, inference, and output writing
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
That structure is easy to reason about with
[[experiment tracking]],
[[model-registry|model registries]], and
[[data quality and observability]].

Streaming fits actions tied to event arrival: fraud checks, recommendations,
risk scores, pricing, ranking, and request-time enrichment. A fraud workflow
must answer during a purchase
([[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]]).
Fraud detection, recommendations, risk scores, pricing, and ranking are strong
online tabular feature-store use cases
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

When the useful response time is tighter than the streaming window, the logic
belongs in the user-facing application path, not a separate streaming pipeline
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

## Operating Batch and Streaming Pipelines

Batch operations use schedules and dependency graphs, where retries, checks, and
reruns are normal operating work. Pipeline work is often about orchestration:
knowing dependencies, start times, and when dependent steps can run
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).
That operating model is central to
[[DataOps]], where workflow
orchestration gives teams a way to repair late data, transient failures, and
bugs
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

Streaming operations center on brokers, consumers, schemas, and synchronized
event flows, and continuously running infrastructure adds more operating
concerns. A few Kafka topics can become many topics, and missing schemas or
allowed-change rules create downstream problems for S3, transformations,
warehouses, and analytics
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]).
Combining Kafka queues means thinking about which downstream use cases depend on
which streaming upstreams and how to keep them in sync
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

## Schemas, Ownership, and Replay

Batch pipelines can still break consumers through missing inputs, bad upstream
data, and dependency changes. Teams need tests, orchestration, and visibility
into whether expected data arrived and whether it is fit for downstream use. CDC
and database versioning are part of the same dependency and change-management
problem
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).
Use [[data quality and observability]]
and [[DataOps]] for the adjacent reliability
work.

Streaming moves those interface problems into event semantics. Ownership is
explicit: software engineers may publish events for service communication while
data teams consume the same topics for analytical pipelines
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]).
Without Avro or another schema practice, the stream becomes a shifting
interface; registry lookup, allowed schema changes, and a change path make the
interface usable. That's why the batch vs streaming decision also touches
[[data governance]],
[[data products]], and
[[event tracking]].

## Cost and Platform Complexity

Batch is often cheaper to start and simpler to pause because scheduled compute
doesn't have to run continuously. Cost-aware orchestration, including cheaper
serverless options, comes before the streaming discussion, and streaming is
often micro-batching unless strict SLAs justify a more specialized stack
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]]).

Streaming earns its extra cost when the delayed result loses value. Stream
processing is popular but brings higher operational cost
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]),
and a team adopting Kafka may need people who understand cluster operation,
producer or consumer conventions, schema practice, and onboarding
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]]).

For learning and portfolio work, requirements-led tooling advice supports the
same lesson: build a clear batch pipeline first, and add Kafka or streaming only
when the use case explains the cost
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]]).
Use [[Data Engineering Portfolio Projects]]
for project examples that show reviewers why the latency requirement exists.

## ML Features and Serving

ML systems often use both modes. A fraud system precomputes stable feature
values daily, then combines them with real-time payload information during a
purchase
([[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]]).
That's different from a pure dashboard pipeline because the output can change the
transaction while the user is still waiting.

Feature stores make the hybrid design explicit. Feast and Tecton ingest
precomputed features from batch or streams, materialize offline and online
stores, build point-in-time-correct training sets, and serve low-latency online
features through a unified API
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Pure batch scoring or campaign use cases may not need a feature store; SQL, dbt,
and validation may be enough. Those choices belong with
[[MLOps]],
[[Machine Learning System Design]], and
[[machine learning infrastructure]].

## Hybrid Designs

The strongest examples aren't pure batch or pure streaming. Teams split the
system by stability and latency: historical features, backfills, and training
sets are computed in batch, while current context, event-triggered actions, and
low-latency retrieval live in streaming or online paths. That split appears in
fraud prevention design
([[podcast:building-and-scaling-data-engineering-systems-for-fraud-detection|Data Engineering for Fraud Prevention]]),
feature-store design
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]),
and ML platform design
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

In architecture review, ground the decision in four checks:

- name the action that consumes the result
- name the latest useful arrival time
- name the owner of the event or table interface
- define checks for bad data, lag, stale ML features, and downstream breakage

If the answer is "a person reads a dashboard tomorrow," batch is probably
enough. If the answer is a live purchase or ranking decision, streaming or
online serving may be justified, and a hybrid feature path may also fit.

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
</content>
