---
layout: wiki
title: "Streaming"
summary: "How the DataTalks.Club archive discusses event streaming with Kafka, real-time pipelines, schemas, feature stores, fraud systems, and search."
related:
  - Batch vs Streaming
  - Data Pipelines
  - Data Engineering Platforms
  - CDC
  - DataOps
  - Data Quality and Observability
  - MLOps
  - Machine Learning System Design
  - Search
---

Streaming data systems process events close to the moment they're produced. In
the DataTalks.Club archive, streaming usually means a producer writes events to
a broker such as Kafka or Kinesis. SQS and RabbitMQ appear in the same queueing
family. Consumers then transform those events for storage, dashboards, alerts,
and online features. The same stream can support fraud decisions or search
ranking.

That makes streaming a design choice inside
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), not a default
architecture. The archive repeatedly ties streaming to
[batch vs streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), schema ownership, and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). A team chooses streaming when the
result loses value if it waits for a scheduled batch job.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the
clearest pipeline-level explanation in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 15:11, he uses website click events flowing into Kafka or Kinesis as the
ingestion example. Around 16:51, he contrasts stream processing with batch
processing: streaming reacts from the queue, while batch stores data first and
processes it later.

## Common Definition

Across the archive, a streaming system has four practical parts:

- producers that emit events
- a broker or queue that buffers events
- processors that transform, join, validate, or enrich events
- outputs such as storage, online stores, alerts, applications, search indexes,
  or dashboards

Kretz maps those pieces in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
around 13:25-17:33. He names ingestion and queues. He also names processing
frameworks, storage, and visualization. Around 12:03, he warns that too many
tools create extra operations work.

That matters because streaming adds
always-on brokers and consumer jobs. It also adds schema checks, lag
monitoring, and replay paths.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
archive's most useful latency boundary in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Around 42:29, he separates slow reporting, streaming's middle latency window,
and sub-100-millisecond interactions that need data already in the serving
application. Streaming can react in seconds or minutes, but it still crosses
multiple services and often contains internal batching.

That definition keeps streaming connected to
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
A broker endpoint isn't enough because teams also need topic naming, ownership,
schemas, and compatibility rules. They need observability and conventions for
replaying or backfilling data when consumers break.

## Guest Differences

Albertsson is the strongest skeptic of streaming as a default. In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
around 41:53-45:19, he argues that teams can often push batch latency down to
minutes or seconds. They can do that while keeping explicit dependencies and
easier reruns. His view favors workflow-oriented batch when the product can
tolerate the delay.

Kretz treats streaming as one processing mode inside a larger production
pipeline. In
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
around 18:14-24:44, he says the team should understand the schema, processing
steps, and desired output before choosing an implementation. The options he
names include Spark and Flink. He also mentions Lambda, Glue, and Docker jobs.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) adds a modern
data-stack warning in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
Around 51:19, he says many so-called streaming systems are micro-batches unless
strict service-level agreements justify Kafka, Flink, or similar
infrastructure.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) focuses on the
organizational cost. In
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
he warns around 20:20 that teams shouldn't expect engineers with no Kafka
experience to design a cluster under scale pressure. Around 23:26, he explains
why topics and schemas become platform concerns. Registry practice and
allowed-change rules matter more as the number of producers and consumers
grows.

## Kafka, Queues, and Event Ingestion

Kafka appears in the archive as the concrete symbol for event streaming, but
guests don't treat Kafka as the whole system. Kretz uses Kafka and Kinesis for
click-event ingestion in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
around 15:11. Brudaru names Kafka and SQS as common buffers in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
around 52:31.

The broker gives producers and consumers a shared event path. A product service
can publish one event, then consumers can use it for analytics and alerts. The
same event can also feed ML features or search freshness. That separation is
valuable only when each consumer can understand the event and recover from late,
duplicated, malformed, or replayed events.

OUAZZA's Kafka discussion in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
shows the failure mode. Software engineers may publish Kafka events for
service-to-service communication while data teams consume the same topics into
S3, Spark, or a warehouse. Without typed schemas and change rules, each
producer change can become a downstream parsing failure, data-quality incident,
or compute-cost problem.

## Batch, Micro-Batch, and Event Time

The archive doesn't frame streaming as the opposite of batch in every case. It
treats them as latency and recovery choices. Albertsson argues in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
that batch windows make dependencies explicit: a job knows which upstream data
and time interval it depends on. Streaming can hide dependencies in event
arrival order, joins across streams, and synchronization between consumers.

Micro-batching can reduce latency while keeping bounded windows that engineers
can test and rerun. Brudaru's
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
discussion makes the same point. At 51:19, strict SLAs may justify true
streaming. Many teams can use short batches or micro-batches instead.

This is why the streaming decision should start with the action that consumes
the result. Fraud blocking and operational alerts can justify low latency.
Online features, search freshness, and traffic response can justify it too.

Reports, backfills, training-set construction, and many warehouse models often
fit batch. The
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) page
covers that broader tradeoff.


## Schemas, Contracts, and Ownership

Streaming moves producer mistakes quickly. OUAZZA's
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
episode is the archive's strongest warning about Kafka schemas. Around 23:26,
he describes teams growing from a few topics to hundreds. Once many consumers
depend on those topics, informal payload changes become expensive to unwind.

His controls are concrete because teams need typed schemas and a schema
registry. They also need allowed-change rules and a documented schema-change
process. Those controls make an event stream closer to a shared data product.
They connect streaming to
[data products]({{ '/wiki/data-products/' | relative_url }}),
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

[CDC]({{ '/wiki/cdc/' | relative_url }}) sits next to this problem. Database
change capture can feed batch jobs, streaming consumers, warehouses, or
event-driven services. The same ownership question remains. Consumers need to
know what changed and whether the change is compatible. They also need to know
how to replay or backfill when the source system changes.

## Stream Processing and Systems Research

Stream processing is a systems problem, not only a product integration problem.
Kretz lists Spark and Flink as processing options in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
around 18:14-24:44. Brudaru also places Flink beside Kafka, SQS, and
micro-batching in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
around 51:19-52:31.

[Eleni Tzirita-Zacharatou]({{ '/people/elenitziritazacharatou/' | relative_url }})
shows why hard streaming problems remain active research. In
[Big Data Analytics and Postdoc Research]({{ '/podcasts/big-data-analytics-and-postdoc-research/' | relative_url }}),
she describes Nebula Stream around 23:08-24:15 as a general-purpose data
management system for IoT. She also frames it as a research successor line
after Apache Flink.
IoT streams force systems to handle distributed data, resource limits, and
application-specific algorithms at the same time.

Those research concerns surface in production too. Teams have to reason about
event time, late arrivals, stateful joins, and processing guarantees. They also
have to account for backpressure and the cost of keeping processing
infrastructure running continuously.

## Fraud, Feature Stores, and Online ML

The archive's strongest applied examples combine streaming and batch.
[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) explains this
split in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
Around 8:24, daily batch jobs compute fraud features, while the live
purchase flow calls a fraud system to decide whether to block a transaction.
Around 34:46, she returns to the same split: known calculations can be prepared
ahead of time, while transaction-payload information must be handled almost
immediately.

[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) gives the
feature-store version in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).
He places feature stores between source systems and the production ML
environment. Those sources can include raw streams and warehouses. They can
also include lakes.
Around 45:00, he separates streaming ingestion,
batch transforms, and training-set construction.

He also separates serving-time behavior. That separation helps teams avoid
training-serving skew while still serving low-latency online features.

For [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
the useful question isn't whether all data should stream. It's which features
can be precomputed and which request-time signals must be handled live. The
team also has to validate both paths. That connects streaming to
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

## Search, Freshness, and Ranking Signals

Search systems consume streaming ideas when relevance depends on fresh events
or recent inventory. Current user behavior and changing ranking signals can
create the same need.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) frames search
as a production decision problem in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Around 34:00, he discusses combining vector similarity with filters and
recency. Around 39:53-45:11, he adds constraints and time encoding. He also
adds normalization and query-time weights.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) connects modern
search to personalization and learning-to-rank in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
around 23:00-30:38. She also connects search to vector databases and RAG.
Those systems may not require a streaming framework for every update, but they
often need reliable ingestion, freshness guarantees, and reindexing processes.

This is where [search]({{ '/wiki/search/' | relative_url }}) overlaps with
streaming. A search index, vector store, or recommendation candidate store is a
consumer of product events. The design has to define how fresh results need to
be and what happens when an event arrives late. It also has to define how
embeddings or ranking features are recomputed, then how teams evaluate
relevance after changes.

## Operations and Reliability

Streaming systems fail differently from scheduled jobs. A batch job can be
late, missing, or wrong for a fixed window. A stream can lag, duplicate
messages, process events out of order, or keep running while silently changing
a metric. Albertsson's
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
discussion is useful because it names the recovery advantage of explicit batch
windows.

The streaming version of [DataOps]({{ '/wiki/dataops/' | relative_url }}) needs
lag monitoring and replay strategy. It also needs schema compatibility checks,
consumer error alerts, and runbooks.

OUAZZA supplies the schema side in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Ramirez adds the production ML side in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
Around 40:50-48:21, she discusses monitoring and runbooks. She also covers
schema changes and upstream data problems. Pienaar adds feature
validation and monitoring in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
around 47:30.

The more consumers depend on a stream, the more the stream needs production
ownership. That means freshness checks, schema checks, and volume checks. It
also means replay procedures and a way to tell downstream teams when the event
rules change.

## Project and Architecture Signals

A credible streaming design names the latency requirement before naming the
tool. Kretz's pipeline anatomy gives the basic structure. Name the producer and
broker first. Then name the processor, storage, and output
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
13:25-17:33). Albertsson's comparison then asks whether streaming is truly
needed or whether a short batch window would be easier to rerun
([DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
41:53-45:19).

The strongest designs explain:

- the action that needs low latency, such as fraud blocking, alerting, online
  feature retrieval, search freshness, or real-time traffic response
- the event schema, versioning rules, and owner
- handling for late events, duplicate events, malformed payloads, and replay
- checks for lag, freshness, volume, errors, and downstream quality
- why batch, micro-batch, or CDC alone wouldn't meet the requirement

Those signals keep streaming grounded in the same tradeoffs the podcast guests
discuss. The design has to explain speed, correctness, recoverability,
and ownership. It also has to explain product value.

## Related Pages

Use these pages for adjacent latency and platform details, plus data quality,
ML, and search.

- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [CDC]({{ '/wiki/cdc/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
