---
layout: wiki
title: "Streaming"
summary: "How the DataTalks.Club archive discusses event streaming with Kafka and Flink, feature stores for real-time ML, and low-latency operations."
related:
  - Batch vs Streaming
  - Data Pipelines
  - Data Engineering Platforms
  - CDC
  - DataOps
  - Data Quality and Observability
  - MLOps
  - Machine Learning System Design
---

Streaming data means handling events as they arrive rather than waiting for a
bounded file or scheduled table refresh. In the DataTalks.Club archive, guests
mostly use streaming for click events and Kafka topics. They also use it for
Kinesis queues and fraud decisions. Feature stores, IoT systems, and real-time
analytics appear in the same discussion.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the
clearest pipeline-level definition in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
At 15:11, he describes a website sending click events into a queue such as
Kafka or Kinesis. At 16:51, he contrasts streaming with batch. Streaming takes
data from the queue, processes it immediately, and pushes the result forward.
Batch stores the data first and processes it later.

That doesn't make streaming the default. Streaming is a latency and operations
choice inside [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}).
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) covers
the latency judgment.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
argues in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
that streaming fits the middle latency window. It's faster than ordinary
batch, but not fast enough for every in-request user interaction.

## Link Map

Streaming applies when the question is about event streams, brokers, or stream
processors. It also fits low-latency features and the cost of keeping a
streaming system running.

- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) covers
  the broader latency decision and the batch alternative.
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) covers
  ingestion, processing, storage, and publication around both batch and
  streaming systems.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  covers the shared platform conventions around Kafka, schemas, ownership, and
  self-service.
- [CDC]({{ '/wiki/cdc/' | relative_url }}) covers row-level database change
  capture, which can feed streaming or batch-oriented pipelines.
- [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
  [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
  cover online inference, feature stores, and model serving.
- [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
  [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  cover lag, schema changes, tests, and recovery.

Core podcast discussions:

- [From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
  with [Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) explains
  event ingestion, message queues, processing frameworks, and the batch versus
  streaming boundary.
- [DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  with [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) frames
  streaming as a latency, dependency, and recovery tradeoff.
- [Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
  with [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) shows how
  Kafka topics need schemas, schema registries, change rules, and experienced
  ownership.
- [Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
  with [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) connects
  streams and batch transforms to online stores and low-latency feature
  retrieval.
- [Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
  with [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) gives the
  applied fraud case: daily feature jobs plus live transaction decisions.
- [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
  with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) keeps
  streaming tied to strict SLAs and places Kafka, SQS, and Flink beside
  micro-batching.

## Common Definition

Across the archive, streaming has three parts:

- A producer emits events.
- A buffer or broker such as Kafka, Kinesis, SQS, or RabbitMQ holds events long
  enough for consumers to read them.
- A processor consumes the events and writes a result to a store, feature
  system, dashboard, alert, or application.

Kretz describes that structure at 13:25-17:33 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
He names ingestion, buffers, and processing frameworks. He also names storage
and visualization. At 12:03, he warns that too many tools create operations
work.

That warning matters for streaming because brokers, processors, and schemas all
need someone to operate them. So do storage and serving paths.

The archive also separates streaming from instant application serving.
Albertsson says around 42:29 in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
that sub-100-millisecond interactions usually need data already in memory inside
the serving application. Streaming handles the window between slow reporting and
that direct interaction. It can react in seconds, but it still crosses multiple
machines and often does internal batching.

## Guest Differences

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) is the most
skeptical of streaming as a default. At 41:53-45:19 in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he argues that teams can often push batch latency down to minutes or even
seconds. He prefers explicit batch dependencies when they give engineers
predictable reruns and recovery.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) treats streaming
as one pipeline mode beside batch. His advice at 18:14-24:44 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
is to understand the schema, processing steps, and final output before choosing
a framework. He lists Spark and Flink as options. He also names Lambda, Glue,
and Docker jobs.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) brings the
newer modern-data-stack warning. In
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
at 51:19, he says streaming is often micro-batching unless strict service-level
agreements justify it. He names Kafka and SQS as common buffers, with Flink or
DuckDB downstream depending on the processing need.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) focuses on scale-up
ownership. In
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
he warns at 20:20 that teams shouldn't expect engineers with no Kafka
experience to design a cluster under scale pressure. At 23:26, he explains
that topics multiply, producers change payloads, and downstream data teams pay
the cost when schemas are informal.

## Event Ingestion and Brokers

The broker isn't the whole streaming system, but it's where many streaming
designs become concrete. Kretz uses Kafka and Kinesis for website click events
at 15:11 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Brudaru later names Kafka and SQS as common buffers in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
at 52:31.

Producers shouldn't write straight into every consumer. Instead, they write
events once so consumers can process them for storage and analytics or for
alerts and ML features.

That separation only helps when the team knows what each event means. OUAZZA's
Kafka section in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
shows the failure mode. Software engineers may use Kafka as pub/sub between
services. The data team may consume the same topics into S3, Spark, or a
warehouse. Without typed schemas and allowed change rules, each producer change
can become a downstream parsing or compute-cost problem.

## Processing Semantics and Time

Streaming isn't defined only by the tool. Albertsson draws the practical
boundary at 45:19 in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}):
batch work makes time windows and dependencies explicit. Streaming hides some
dependencies in the arrival order and synchronization of streams. If a click
stream arrives late, a click-through-rate calculation can change.

That's why micro-batching keeps coming up. Albertsson treats micro-batching as
a way to keep short latency while preserving explicit dependency management.

Brudaru makes a similar point in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
at 51:19. He says many streaming systems are micro-batches unless strict SLAs
force true streaming. The design question isn't "Kafka or no Kafka." Ask
whether the consumer can tolerate a bounded window, a late event, a replay, and
a predictable rerun.

Research discussions show the same hard problems. [Eleni
Tzirita-Zacharatou]({{ '/people/elenitziritazacharatou/' | relative_url }})
describes Nebula Stream in
[Big Data Analytics and Postdoc Research]({{ '/podcasts/big-data-analytics-and-postdoc-research/' | relative_url }})
at 23:08-24:15 as a general-purpose data management system for IoT. She also
describes it as a successor research line after Apache Flink. That episode
isn't a product adoption guide, but it shows why stream processing remains a
systems topic. IoT streams force teams to reason about distributed data and
resources, and they also have to connect algorithms to application needs.

## Schemas and Ownership

Streaming moves producer mistakes quickly. That's the strongest organizational
lesson in OUAZZA's
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
discussion. At 23:26, he explains that teams may start with one or two Kafka
topics and end up with hundreds. The cost of late discipline rises because
existing consumers already depend on the old payloads.

He recommends concrete controls:

- typed schemas
- schema registry
- documented allowed changes
- schema-change steps

Those controls turn an event stream into a data product that other teams can
trust. They also connect streaming to
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[data products]({{ '/wiki/data-products/' | relative_url }}), and
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}). A stream that feeds many
teams needs ownership and compatibility rules, not only a broker endpoint.

## Real-Time ML and Online Features

The archive's strongest product examples use streaming and batch together.
[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) explains in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }})
at 8:24 that daily batch jobs compute fraud feature values. The live purchase
flow then calls a fraud system, makes a decision for that transaction, and may
block the purchase.

At 34:46, she returns to the same design. Batch jobs prepare known
calculations, and the live system uses transaction-payload information almost
instantly.

[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) gives the
feature-store version in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).
He places feature stores between raw streams, warehouses, or lakes and the
production ML environment. At 45:00, he says teams should treat streaming and
batch separately. Teams should validate streaming ingestion, batch transforms,
training set builds, and serving-time behavior.

He also contrasts Flink and Spark for real-time feature engineering. Feast used
Spark for ecosystem and connector support.

Those episodes connect streaming to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
For online inference, the useful question isn't whether all data is streamed.
Ask which features can be precomputed. Then ask which request-time signals must
be handled live and how the team keeps training and serving semantics aligned.

## Operations and Reliability

Streaming systems fail differently from scheduled jobs. A batch job can be late
or missing, and it can also be wrong for a fixed window. A stream can lag,
duplicate messages, process events out of order, or keep running while silently
changing a metric. Albertsson's dependency discussion in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
is useful because it names the recovery advantage of explicit batch windows.

The streaming version of [DataOps]({{ '/wiki/dataops/' | relative_url }}) needs
lag monitoring and replay strategy. It also needs schema compatibility checks,
consumer error alerts, and runbooks. OUAZZA's Kafka guidance supplies the
schema side.

Ramirez adds the ML production side in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}):
she discusses monitoring and runbooks. She also discusses schema changes and
upstream data problems around 40:50-48:21. Pienaar adds feature validation and
monitoring in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
around 47:30.

Across these episodes, streaming is valuable when late information would change
an action. The team still has to operate the event path as a production system.
The more consumers depend on the stream, the more it needs schema agreements
and observability. It also needs replay and ownership.

## Project Signals

A credible streaming project should make the latency requirement explicit.
Kretz's pipeline anatomy gives a simple structure. Name the producer and
broker. Then name the processor, storage, and output
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
13:25-17:33). Albertsson's comparison then asks whether streaming is truly
needed or whether a short batch window would be easier to rerun
([DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
41:53-45:19).

For a portfolio or internal design review, use these signals:

- The project names the action that needs low latency, such as fraud blocking,
  alerting, online feature retrieval, or real-time traffic response.
- The event schema is typed and versioned, with schema-change steps.
- The design covers late events, duplicate events, malformed payloads, and
  replay behavior.
- The output is observable through lag and freshness, plus volume, error, and
  downstream-quality checks.
- The writeup explains why batch, micro-batch, or CDC alone wouldn't be enough.

Those signals keep a streaming project grounded in the same tradeoffs the
podcast guests discuss. The project should explain speed, correctness,
recoverability, and ownership. It should also explain product value.

## Related Pages

Continue with these adjacent pages:

- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [CDC]({{ '/wiki/cdc/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
