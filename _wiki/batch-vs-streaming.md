---
layout: wiki
title: "Batch vs Streaming"
summary: "A podcast-backed comparison of batch and streaming data processing through latency, operations, contracts, cost, ML serving, and product-decision tradeoffs."
related:
  - Data Engineering
  - Data Engineering Platforms
  - Streaming
  - DataOps
  - Machine Learning System Design
---

Batch processing handles bounded chunks of data. In the archive, that includes
scheduled warehouse jobs and backfills. It also includes training set creation
and batch inference.

Streaming processing handles events as they arrive from queues, brokers, or
production services. In the DataTalks.Club archive, the comparison connects to
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). It also connects to
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the cleanest
pipeline vocabulary in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Events land in systems such as Kafka or Kinesis. The team then decides whether
to react immediately or store the data first and process it later.

That framing keeps batch vs streaming away from tool fashion. The useful
questions are latency, dependencies, and operating cost. They also include
replay, ownership, and the action that consumes the result.

## Common Definition

Across the archive, batch is the default when the consumer can wait. It also
fits teams that benefit from explicit dependencies. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
describes the workflow-oriented version in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

Batch jobs can declare which upstream data is required. They can also declare
the time window and downstream dependencies. That makes batch natural for
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}) and warehouse
transformations in the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). It also
fits backfills, training datasets, and scheduled scoring.

Streaming is the archive's answer when a delayed result changes the product
outcome. Lars separates slow reporting, the middle streaming window, and
sub-100-millisecond paths that belong inside the serving application in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) shows the product
version in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
Daily batch jobs prepare feature values, but the purchase flow still needs a
live fraud decision that can block a transaction. [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }})
shows the MLOps version in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
where offline stores support training and online stores serve low-latency
features.

The common decision rule is therefore not "batch is old" or "streaming is
modern." It's to name the downstream action and the maximum useful latency. The
team then chooses among scheduled jobs, micro-batches, streaming jobs, and
in-request logic. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
makes the same point in
[Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
In that episode, he warns that much so-called streaming is micro-batching unless
strict SLAs justify tools such as Kafka or Flink.

## Guest Differences

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) is the most
skeptical of streaming as a default. In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he argues that streaming has higher operational cost because dependency
management is less explicit than in workflow-orchestrated batch. He also argues
that batch latency can often be pushed into minute-level, and sometimes
second-level, windows before a team needs a full stream-processing architecture.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) is more
architecture-neutral. His
[production ML pipeline episode]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
maps ingestion, queues, and storage. It also maps processing frameworks such as
Spark and Flink, plus orchestration options. His contribution is vocabulary:
batch or streaming is one processing-mode decision inside a larger production
pipeline, not the whole architecture.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) focuses on the
organizational cost of streaming. In
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
Kafka creates onboarding work because teams need schemas and registry practice.
They also need allowed changes and change rules. His focus links streaming to
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data products]({{ '/wiki/data-products/' | relative_url }}), and
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}), not only to brokers and
compute engines.

[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) and
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) make the case
for hybrid ML systems. Angela's
[fraud engineering episode]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
combines daily feature computation with live transaction checks. Willem's
[feature-store episode]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
separates source modes from storage modes. It also covers backfills, validation,
and low-latency feature retrieval.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
adds a platform-maturity warning in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Teams should decide whether a model is consumed by a downstream service or only
by a batch job before investing in online serving infrastructure.

## Latency and Product Action

Batch fits reports and warehouse models. It also fits backfills, campaigns, and
model jobs where delayed results still support the decision. [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
describes batch inference as a sequence of data loading and preprocessing. The
same sequence includes feature engineering, inference, and output writing in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
That structure is easy to reason about with
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[model registries]({{ '/wiki/model-registry/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

Streaming fits actions tied to event arrival. The archive examples include
fraud checks, recommendations, risk scores, and pricing. They also include
ranking, alerts, and request-time enrichment. Angela's
[fraud workflow]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
must answer during a purchase.

Willem names fraud detection and recommendations as strong online tabular
feature-store use cases. He also names risk scores, pricing, and ranking in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

When the useful response time is tighter than the streaming window, Lars says
the logic belongs in the user-facing application path. It shouldn't be a
separate streaming pipeline
([DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

## Operational Model

Batch operations use schedules and dependency graphs. In batch pipelines,
retries, checks, and reruns are normal operating work. [Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) explains in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
that pipeline work is often about orchestration. Teams need to know dependencies
and start times. They also need to know when dependent steps can run.

Lars makes the same operating model central to
[DataOps]({{ '/wiki/dataops/' | relative_url }}) in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Workflow orchestration gives teams a way to repair late data, transient
failures, and bugs.

Streaming operations center on brokers and consumers, with lag, replay, and
event-time joins. Schema evolution and continuously running
infrastructure add more operating concerns. [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) uses Kafka in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
to show why a few topics can become many topics. Missing schemas or
allowed-change rules create downstream problems for S3, transformations,
warehouses, and analytics.

Santona gives the pipeline-design version in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Combining Kafka queues means thinking about which downstream use cases depend on
which streaming upstreams and how to keep them in sync.

## Schemas, Ownership, and Replay

Batch pipelines can still break consumers through late files and bad upstream
data. Partial backfills and silent transformation changes can do the same. The
archive ties those
failure modes to [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}).

Teams need tests,
orchestration, and visibility into whether expected data arrived. They also need
to know whether the data is fit for downstream use. Lars's
[DataOps discussion]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
also treats CDC and database versioning as part of the same dependency and
change-management problem.

Streaming moves those interface problems into event semantics. Mehdi's
[Kafka section]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
is explicit about ownership because software engineers may publish events for
service communication. Data teams consume the same topics for analytical
pipelines.

Without Avro or another schema practice, the stream becomes a
shifting interface. Registry lookup, allowed schema changes, and a process for
changes make the interface usable. That's why the batch vs streaming decision
also touches
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data products]({{ '/wiki/data-products/' | relative_url }}), and
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}).

## Cost and Platform Complexity

Batch is often cheaper to start and simpler to pause because scheduled compute
doesn't have to run continuously. Adrian describes cost-aware orchestration,
including cheaper serverless options, before his streaming discussion in
[Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
The same episode says streaming is often micro-batching unless strict SLAs
justify a more specialized stack.

Streaming earns its extra cost when the delayed result loses value. Lars says
stream processing is popular but brings higher operational cost in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Mehdi adds that a team adopting Kafka may need people who understand cluster
operation and producer or consumer conventions. The same team also needs schema
practice and onboarding
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

For learning and portfolio work, the archive's
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
page applies the same lesson. Build a clear batch pipeline first, then add Kafka
or streaming when the use case explains the cost.

## ML Features and Serving

ML systems often use both modes. Angela's
[fraud episode]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
precomputes stable feature values daily, then combines them with real-time
payload information during a purchase. That's different from a pure dashboard
pipeline because the output can change the transaction while the user is still
waiting.

Feature stores make the hybrid design explicit. Willem describes Feast and
Tecton as systems that ingest precomputed features from batch or streams. They
materialize offline and online stores, build point-in-time-correct training
sets, and serve low-latency online features through a unified API in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

Pure batch scoring or campaign use cases may not need a feature store. SQL,
dbt, and validation may be enough. That connects batch vs streaming to
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}), and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

## Hybrid Designs

The strongest archive examples aren't pure batch or pure streaming. They split
the system by stability and latency. Historical features, backfills, and
training sets are computed in batch. Current context, event-triggered actions,
and low-latency retrieval live in streaming or online paths. Angela's
[fraud prevention design]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}),
Willem's
[feature-store design]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
and Simon's
[ML platform discussion]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
all show that split.

In architecture review, ground the decision in four checks:

- name the action that consumes the result
- name the latest useful arrival time
- name the owner of the event or table interface
- define checks for bad data, lag, drift, and silent downstream breakage

If the answer is "a person reads a dashboard tomorrow," batch is probably
enough. If the answer is a live purchase or ranking decision, streaming or
online serving may be justified. A hybrid feature path may also fit.

## Related Pages

These pages connect the comparison to adjacent archive topics.

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
