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

## Definition and Scope

Batch processing handles bounded chunks of data. In the archive, batch shows up
as scheduled warehouse work and backfills. It also appears in feature jobs,
training datasets, and batch inference. Streaming handles events as they arrive
from queues or brokers.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) draws that
boundary in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}):
at 15:11 he places events in Kafka or Kinesis. At 16:51 he contrasts immediate
reaction with storing data first and processing it later.

The useful comparison isn't "old versus modern." The archive treats batch and
streaming as a decision about latency and operations. It also covers replay,
cost, and ownership.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) is explicit in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

Around 41:53-45:11, he says streaming covers the middle latency window. He also
says batch can often be pushed down to minutes or seconds when workflow
dependencies are explicit.

That connects the comparison to
[DataOps]({{ '/wiki/dataops/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

## Link Map

Use this map to move from the comparison to the adjacent archive pages.

- Pipeline design: use [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
  when the work is about ingestion, processing, orchestration, and delivery.
- Product latency: use
  [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
  when a live prediction, fallback, monitoring path, or user-facing decision is
  part of the system.
- Kafka and events: use
  [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  and [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}) when the hard part is
  ownership, contracts, schemas, or self-service.
- Online features: use
  [Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
  and [MLOps]({{ '/wiki/mlops/' | relative_url }}) when feature values must work
  for both offline training and online serving.
- Scheduled work: use
  [Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}) and
  [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) when the
  main question is orchestration, warehouses, or dbt-style transformation.
- Reliability: use
  [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  and [DataOps]({{ '/wiki/dataops/' | relative_url }}) when the concern is bad
  data, schema drift, lag, or missing checks.

## Common Decision Rule

Start with the downstream action. If a late answer changes nothing, prefer batch
or micro-batch. If a late answer loses the product opportunity, consider
streaming. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
uses this latency framing in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
He separates slow reporting, the streaming middle window, and
sub-100-millisecond paths that must live inside the user-serving application.

Fraud prevention is the clearest archive example, and it isn't pure streaming.
In
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}),
[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) explains at
8:24 that daily batch jobs compute feature-engineering values. The live purchase
flow then calls the fraud system and may block a transaction. At 33:34-34:46,
she returns to the same design: prepare stable values in batch, then calculate
request-specific values from the transaction payload.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) gives the
modern-stack version in
[Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
At 51:19, he warns that much "streaming" is micro-batching unless strict SLAs
justify tools such as Kafka or Flink. The review should name the latency target.
It should also name the person or system that acts on the result.

## Comparison

Compare the two modes by the constraint they impose on the team.

## Decision Fit

Batch fits reports and warehouse models. It also fits backfills, training sets,
campaigns, and batch inference. [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
discusses batch inference at 31:15-31:51 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

Streaming fits event-triggered actions such as fraud checks and live risk
scores. It also fits alerts and request-time features. [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }})
shows the fraud version in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
and [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) shows the
feature-store version in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

## Freshness

Batch is often enough when minutes or hours still support the action. It can
support days too when the downstream workflow waits for review or reporting.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) says batch can
be pushed to low latency when dependencies are explicit in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

Streaming helps when seconds or event-time reaction matter. It isn't a
substitute for in-request serving when the product needs sub-100-millisecond
response.

## Operations

Batch uses schedulers and retries, plus dependency graphs, backfills, and
checks.
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) places batch work
inside Airflow-style orchestration in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})
around 10:48-13:25.

Streaming adds brokers and consumers. It also adds lag, replay, event-time
joins, and schema evolution. [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }})
shows that through Kafka topics, schemas, registry practice, and contracts at
23:26 in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).

## Failure Mode

A batch job can be late or missing. It can also be partly backfilled or based on
bad upstream data. [DataOps]({{ '/wiki/dataops/' | relative_url }}) connects
those failures to tests, orchestration, and observability.

A stream can be late, duplicated, or malformed. It can also be out of order or
consumed by teams that don't own the producer. [Mehdi's Kafka section]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
describes downstream S3, transformation, and analytics breakage when schemas are
informal.

## Cost

Teams can stop scheduled compute more easily. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
discusses cheaper serverless orchestration options before the streaming section
in
[Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).

Always-on streaming systems can be justified by product value, but
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) says they bring
more operating cost in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

## Guest Differences

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) is the most
skeptical of streaming as a default. His
[DataOps]({{ '/wiki/dataops/' | relative_url }}) argument is that explicit batch
dependencies are easier to reason about. Micro-batching can cover many latency
needs before teams adopt a full stream-processing stack
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
41:53-45:11).

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) is more
architecture-neutral. In
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
he maps the production pipeline from events and queues to processing frameworks
and orchestration. His contribution is a vocabulary for where the batch or
streaming choice sits in a pipeline.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) focuses on the
organizational cost of streaming. In
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
Kafka creates a need for conventions and onboarding. It also needs schema
registry practice, allowed changes, and downstream contracts. That connects
streaming to
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[data products]({{ '/wiki/data-products/' | relative_url }}), not only to
infrastructure.

[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) and
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) give the ML
product version. Angela's fraud episode shows daily batch feature jobs plus live
transaction decisions. Willem's feature-store episode separates batch and stream
sources, offline and online stores, and low-latency serving. Together, they
support the hybrid approach used in [MLOps]({{ '/wiki/mlops/' | relative_url }}).

Stable history is computed in batch. Current decisions are served online, and
both paths need monitoring.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) keeps
the comparison tied to platform maturity. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he says teams should decide whether a model is consumed by a downstream service
or only by a batch job. Teams should make that call before building serving
infrastructure. That's the ML platform version of the same decision rule.

## Practical Batch Defaults

Batch is a strong default when the consumer can wait and the team benefits from
explicit dependencies. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
uses workflow orchestration as the reason in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

Batches can declare the complete time window and the upstream outputs required
for the run. That makes batch useful for warehouse models and reporting. It
also fits training datasets, backfills, and batch inference. It aligns with
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}) when the
problem is dependency management rather than event-time reaction.

Batch also fits systems where reruns are part of the operating model.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
describes batch inference as data loading and preprocessing. He also includes
feature engineering, inference, and output writing in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
That structure is easier to audit through
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[model registries]({{ '/wiki/model-registry/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
than a continuously changing event flow.

Batch is usually the safer first answer for learning and portfolio work unless
the use case has a low-latency requirement. The archive's data engineering
career pages warn against overbuilding with Kafka, Spark, or Kubernetes before
the pipeline problem needs them. See
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
and [DevOps to Data Engineering]({{ '/wiki/devops-to-data-engineering/' | relative_url }}).

## Practical Streaming Triggers

Streaming earns its cost when a delayed result changes the product outcome.
Fraud blocking in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
is the strongest example because the system must answer during a purchase.
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) names similar
online tabular cases in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).
The examples include fraud detection and recommendations. They also include risk
scores, pricing, and ranking.

Streaming also fits when upstream events are already the product interface and
downstream consumers need consistent event semantics. [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }})
explains the failure mode in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Software teams may publish Kafka events for service communication. Data teams
may depend on the same topics for S3, transformation, warehouse, and analytics
workflows. Without schemas and change rules, streaming shifts ambiguity
downstream.

Use streaming cautiously when the requirement is only fresh dashboards or
near-real-time analytics. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
calls out micro-batching at 51:19 in
[Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) argues that
the true streaming window can be narrower than teams assume in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Those episodes support a practical review: verify the latency target before
adding an always-on pipeline.

## Hybrid Designs

The archive's most realistic design is hybrid. [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }})
combines daily feature computation with live fraud requests in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) describes feature
stores as a layer that can ingest from batch and stream sources. The same layer
can materialize offline and online stores, and serve models through an API in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) adds the pipeline
engineering version in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Around 38:20-40:45, she discusses keeping streaming upstream use cases in sync,
including combined Kafka queues. She notes that batch worlds avoid some
event-time coordination because the batch boundary is explicit. Hybrid designs
therefore need clear boundaries for live events, staged data, precomputed
features, and serving latency.

## Review Prompts

Use these prompts during architecture review.

- Name the action triggered by the result and the consequence of lateness. This
  comes from [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})'s
  [latency discussion]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  and [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }})'s
  [fraud workflow]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
- State whether "real-time" means seconds, minutes, or sub-100 milliseconds.
  [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) separates
  those windows in
  [DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
- Test micro-batching before adopting a full streaming stack when the SLA
  allows it, as [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
  raises this in
  [Trends in Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
- Assign ownership for event schemas and allowed changes. Replay policy and
  downstream consumers need owners too. [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }})
  makes this the core Kafka operating question in
  [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
- Separate offline training parity, online feature retrieval, and batch scoring.
  [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) and
  [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
  cover those angles in
  [Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
  and [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- Define detection for bad data, schema drift, lag, and silent downstream
  breakage through
  [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  and [DataOps]({{ '/wiki/dataops/' | relative_url }}).

## Related Pages

These pages provide adjacent context for platform, ML, and reliability choices.

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }})
- [Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
