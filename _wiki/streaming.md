---
layout: wiki
title: "Streaming"
summary: "How DataTalks.Club guests discuss event streaming with Kafka, real-time pipelines, schemas, feature stores, fraud systems, and search."
related:
  - Data Pipelines
  - Data Engineering Platforms
  - CDC
  - DataOps
  - Data Quality and Observability
  - MLOps
  - Machine Learning System Design
  - Search
---

Streaming data systems handle events close to the moment they're produced. In
DataTalks.Club episodes, streaming usually means a producer writes events to a
broker such as Kafka or Kinesis. SQS and RabbitMQ appear in the same queueing
family. Consumers then transform those events for storage and dashboards. Other
consumers use the same events for alerts, online features, fraud decisions, or
search ranking.

The episodes treat streaming as a design choice inside
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), not as the
default architecture. Streaming sits beside
[batch vs streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). It also sits beside
schema ownership, [MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[search]({{ '/wiki/search/' | relative_url }}) when a delayed result loses
product value.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the
clearest pipeline-level explanation in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 15:11, he uses website click events flowing into Kafka or Kinesis as the
ingestion example. Around 16:51, he contrasts stream handling with batch work:
streaming reacts from the queue, while batch stores data first and handles it
later.

## Pipeline Anatomy

A streaming system in these discussions has four practical parts:

- producers that emit events
- a broker or queue that buffers events
- jobs that transform or enrich events
- outputs such as storage, online stores, alerts, applications, search indexes,
  or dashboards

Kretz maps those pieces around 13:25-17:33 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Ingestion and queues belong to the same pipeline anatomy. So do compute
frameworks, storage, and visualization.

Kretz also warns around 12:03 that too many tools create extra operating work.
That warning matters because streaming adds always-on brokers and consumer
jobs. It also adds schema checks, lag monitoring, and replay paths. A
[data engineering platform]({{ '/wiki/data-engineering-platforms/' | relative_url }})
therefore needs topic naming and ownership. It also needs compatibility rules,
observability, and conventions for replaying or backfilling data when consumers
break.

## Latency Boundaries

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
clearest latency boundary in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Around 42:29, he separates slow reporting, streaming's middle latency window,
and sub-100-millisecond interactions that need data already inside the serving
application. Streaming can react in seconds or minutes, but it still crosses
multiple services and often includes internal batching.

Albertsson is also the strongest skeptic of streaming as a default. Around
41:53-45:19 in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he argues that teams can often push batch latency down to minutes or seconds.
They can still keep explicit dependencies and easier reruns. His view favors
workflow-oriented batch when the product can tolerate the delay. It keeps
streaming tied to recoverability rather than tool fashion.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) adds the modern
data-stack warning in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
Around 51:19, he says many systems described as streaming are micro-batches
unless strict service-level agreements justify Kafka, Flink, or
similar infrastructure. Short batches or micro-batches can reduce latency while
keeping bounded windows that engineers can test and rerun.

## Kafka and Event Interfaces

Kafka appears as the concrete symbol for event streaming, but the guests don't
treat Kafka as the whole system. Kretz uses Kafka and Kinesis for click-event
ingestion around 15:11 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Brudaru names Kafka and SQS as common buffers around 52:31 in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).

The broker gives producers and consumers a shared event path. A product service
can publish one event, then consumers can use it for analytics and alerts.
Other consumers can use the same event for ML features and search freshness.
That separation only works when each consumer can understand the event and
recover from late, duplicated, malformed, or replayed events.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) shows the failure
mode in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Around 20:20, he warns that teams shouldn't expect engineers with no Kafka
experience to design a cluster under scale pressure. Around 23:26, he explains
why topics and schemas become platform concerns. Software engineers may publish
Kafka events for service-to-service communication. Data teams may consume the
same topics into S3, Spark, or a warehouse.

Teams use typed schemas, a schema registry, allowed-change rules, and a
documented schema-change path to turn an event stream into a shared data
interface. Without those controls, each producer change can become a downstream
parsing failure, data-quality incident, or compute-cost problem. The same
ownership model links streaming to
[data products]({{ '/wiki/data-products/' | relative_url }}),
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

[CDC]({{ '/wiki/cdc/' | relative_url }}) sits next to this interface problem.
Database change capture can feed batch jobs, streaming consumers, warehouses,
or event-driven services. Consumers still need to know what changed, whether
the change is compatible, and how to replay or backfill when the source system
changes.

## Batch, Micro-Batch, and Event Time

The podcast discussions frame streaming and batch as latency or recovery
choices. Albertsson argues in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
that batch windows make dependencies explicit: a job knows which upstream data
and time interval it depends on. Streaming can hide dependencies in event
arrival order, joins across streams, and synchronization between consumers.

The streaming decision starts with the action that consumes the result. Fraud
blocking and operational alerts can justify low latency. Online features, search
freshness, and traffic response can justify it too. Reports, backfills,
training-set construction, and many warehouse models often fit batch. The
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
page covers that broader tradeoff.

## Stream Engines and IoT Research

Kretz lists Spark and Flink as compute options around 18:14-24:44 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
He also mentions Lambda and Glue jobs after saying the team should understand
the schema, transformation steps, and desired output before choosing an
implementation. Docker jobs appear in the same implementation discussion.
Brudaru places Flink beside Kafka and SQS around
51:19-52:31 in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
He discusses micro-batching in the same section.

[Eleni Tzirita-Zacharatou]({{ '/people/elenitziritazacharatou/' | relative_url }})
shows why hard streaming problems remain active research. In
[Big Data Analytics and Postdoc Research]({{ '/podcasts/big-data-analytics-and-postdoc-research/' | relative_url }}),
she describes Nebula Stream around 23:08-24:15 as a general-purpose data
management system for IoT. She also frames it as a research successor line
after Apache Flink. IoT streams force systems to handle distributed data,
resource limits, and application-specific algorithms at the same time.

Those research concerns surface in production systems too. Teams have to reason
about event time, late arrivals, stateful joins, and delivery guarantees. They
also have to account for backpressure and the cost of keeping stream
infrastructure running continuously.

## Fraud, Feature Stores, and Online ML

The strongest applied examples combine streaming and batch.
[Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }}) explains this
split in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
Around 8:24, daily batch jobs compute fraud features, while the live purchase
flow calls a fraud system to decide whether to block a transaction. Around
34:46, she returns to the same split: known calculations can be prepared ahead
of time, while transaction-payload information must be handled almost
immediately.

[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) gives the
feature-store version in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).
He places feature stores between source systems and the production ML
environment. Those sources can include raw streams, warehouses, and lakes.
Around 45:00, he separates streaming ingestion, batch transforms, and
training-set construction.

Pienaar also separates serving-time behavior. That split helps teams avoid
training-serving skew while still serving low-latency online features. For
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
the useful question isn't whether all data should stream. It's which features
can be precomputed and which request-time signals must be handled live. Teams
then validate both paths through [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

## Search Freshness and Ranking Signals

Search systems use streaming ideas when relevance depends on fresh events and
recent inventory. Current user behavior or changing ranking signals can create
the same need.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) frames search
as a production decision problem in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Around 34:00, he discusses combining vector similarity with filters and
recency. Around 39:53-45:11, he adds constraints and time encoding. He also
adds normalization and query-time weights.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) connects modern
search to personalization and learning-to-rank in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
around 23:00-30:38. She also connects search to vector databases and RAG. Those
systems may not need a streaming framework for every update, but they often
need reliable ingestion, freshness guarantees, and reindexing paths.

A search index, vector store, or recommendation candidate store is a consumer
of product events. The design has to define how fresh results need to be and
what happens when an event arrives late. It also has to define how embeddings or
ranking features are recomputed, then how teams evaluate relevance after
changes. Use
[search]({{ '/wiki/search/' | relative_url }}) for the retrieval-specific
side of that design.

## Reliability and Operations

Streaming systems fail differently from scheduled jobs. A batch job can be
late, missing, or wrong for a fixed window. A stream can lag, duplicate
messages, handle events out of order, or keep running while silently changing a
metric. Albertsson's
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
discussion is useful because it names the recovery advantage of explicit batch
windows.

The streaming version of [DataOps]({{ '/wiki/dataops/' | relative_url }}) needs
lag monitoring and replay strategy. It also needs schema compatibility checks,
consumer error alerts, and runbooks. OUAZZA supplies the schema side in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).

Ramirez adds the production ML side in
[Data Engineering for Fraud Prevention]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}).
Around 40:50-48:21, she discusses monitoring and runbooks. She also covers
schema changes and upstream data problems. Pienaar adds feature validation and
monitoring around 47:30 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

The more consumers depend on a stream, the more the stream needs production
ownership. Freshness checks, schema checks, and volume checks become part of
the platform rules. Replay procedures and communication about event-rule
changes do too.

## Design Signals

A credible streaming design names the latency requirement before naming the
tool. Kretz's pipeline anatomy gives the basic structure. Name the producer and
broker first. Then name the transformation job, storage, and output
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

Those signals keep streaming grounded in speed and correctness. They also keep
it grounded in recoverability, ownership, and product value.
