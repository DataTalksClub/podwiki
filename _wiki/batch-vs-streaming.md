---
layout: wiki
title: "Batch vs Streaming"
summary: "How the podcast archive frames batch and streaming as latency, cost, reliability, and product-decision tradeoffs."
related:
  - Data Engineering
  - Data Engineering Platforms
  - Streaming
  - DataOps
  - Machine Learning System Design
---

## Definition and Scope

Batch systems process data on a schedule or after data has arrived in storage.
Streaming systems process events as they arrive. The archive discusses Kafka,
Kinesis, SQS, Flink, Spark Streaming, and message queues in that context.

The podcast archive doesn't treat streaming as the mature default. Guests use
streaming when a product, model, or operational workflow needs immediate
reaction. They use batch when daily, hourly, or triggered processing gives the
business enough freshness with less operational load.


## Archive-Level Takeaways

**Latency should come from the decision, not the tool.**

The archive keeps returning to one question: when does someone use the result?
Retail fraud prevention needs instant scoring because a cashier or security
workflow must act during the transaction. Many analytics jobs, training runs,
dashboards, and backfills don't need that latency.

Lars Albertsson's DataOps episode and Adrian Brudaru's modern data engineering
episode both warn against treating streaming as a badge of platform maturity.
When strict SLAs are absent, micro-batches or scheduled jobs may produce the
same business value with easier debugging and lower cost.

**Streaming moves complexity earlier.**

Streaming makes event order, schema contracts, replay, consumer lag, stateful
processing, and incident response part of the first design. Mehdi OUAZZA's
scale-up episode is useful because it shows the organizational cost. Kafka only
helps when teams also define schemas, registry practices, guidelines, and
downstream data contracts.

**Batch remains central for ML and analytics.**

Several ML and data engineering episodes keep batch in the architecture even
when real-time inference exists. Fraud detection combines daily feature
computation with instant inference. Production ML platform discussions include
batch scoring alongside online serving. Warehouse and lakehouse episodes still
use scheduled ingestion, transformation, and orchestration as core platform
work.

**Hybrid architectures are common.**

The archive rarely makes batch and streaming mutually exclusive. A system may
stream events into durable storage, run batch feature jobs, and serve a low
latency prediction from precomputed or partially updated data. The architecture
choice is usually about where freshness matters, where replay matters, and
which part of the system can fail without blocking the user.

## Comparison Structure

Compare the two modes by the constraints they put on the team.

- **Best fit:** Batch fits reporting, training, backfills, periodic sync, and
  cost-aware transforms. Streaming fits fraud checks, alerts, product events,
  operational triggers, and live features.
- **Freshness:** Batch usually means minutes, hours, or days. Streaming usually
  means seconds or near-real time.
- **Failure mode:** Batch fails through late or missing job output. Streaming
  adds lag, malformed events, state errors, and duplicate processing.
- **Operational burden:** Batch needs scheduling, retries, partitions,
  backfills, and data quality checks. Streaming adds brokers, ordering, schemas,
  state, replay, and consumer ownership.
- **Cost shape:** Batch can run on cheaper scheduled compute. Streaming often
  needs always-on infrastructure and specialized operators.
- **Governance need:** Batch needs dataset ownership, freshness, lineage, and
  contracts. Streaming needs event contracts, schema registry practices,
  consumer ownership, and replay policy.

## Decision Points

**Use batch when freshness doesn't change the action.**

Batch is a strong default when the downstream action waits for a daily report,
a training run, a customer segment sync, a billing cycle, or an analyst review.
The archive's modern-stack episodes keep warehouse-centered ELT and dbt
workflows in the picture. Analysts and analytics engineers get a clear place to
look at, test, and document transformations.

**Use streaming when a late answer loses value.**

Streaming earns its complexity when the window for action is short. Fraud
detection is the clearest archive example: the system needs to score a
transaction while the customer is still at the register. Product telemetry,
recommendations, operational alerts, and IoT events can fit the same design
when delayed processing would make the answer irrelevant.

**Choose micro-batching when the SLA allows it.**

Micro-batching often gives teams enough freshness without making every
transformation a true streaming job. Adrian Brudaru's modern data engineering
episode explicitly notes that much "streaming" is micro-batching unless a team
has strict SLAs. This is a useful vocabulary correction for architecture
reviews: name the actual latency target before naming the tool.

**Treat event contracts as part of streaming architecture.**

Streaming without contracts pushes pain downstream. The scale-up episode shows
why Kafka topics, schemas, and registry practices matter. Software engineers
may publish events for service communication while data teams depend on those
same events for S3 writes, transformations, warehouse models, and analytics.
Without guidelines, the data platform inherits breakage that producers may not
notice.

## Episode Evidence

These episodes provide the most direct comparison evidence.

- [DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast.html):
  At 41:53, compares batch and streaming by latency and use case. At 45:11,
  discusses micro-batching, dependency management, and predictability. Source:
  `../datatalksclub.github.io/_podcast/dataops-principles-and-scalable-data-platforms.md`.
- [From Notebooks to Production](https://datatalks.club/podcast.html): At
  13:25, lays out data pipeline anatomy. At 15:11, covers events and Kafka or
  Kinesis. At 16:51, compares streaming with batch. Streaming reacts
  immediately, while batch stores first and processes later. Source:
  `../datatalksclub.github.io/_podcast/production-ml-pipelines-with-aws-and-kafka.md`.
- [Scaling Data Engineering Teams](https://datatalks.club/podcast.html): At
  23:26, covers Kafka, schemas, schema registry, and data contracts as the
  practices that keep event streaming usable at scale. Source:
  `../datatalksclub.github.io/_podcast/scaling-data-engineering-teams-self-service-platforms.md`.
- [Data Engineering for Fraud Prevention](https://datatalks.club/podcast.html):
  At 8:24, combines daily feature batches with real-time scoring. At 33:34 and
  34:46, shows why fraud workflows need instant decisioning while still using
  batch computation. Source:
  `../datatalksclub.github.io/_podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.md`.
- [Modern Data Engineering](https://datatalks.club/podcast.html): At 51:19,
  compares micro-batching, Kafka, SQS, and Flink. Adrian warns that streaming
  often means micro-batching unless the SLA is strict. Summary:
  [Modern Data Engineering]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
- [Machine Learning System Design](https://datatalks.club/podcast.html): Uses
  batch, online, streaming, and hybrid serving as system-design choices driven
  by product latency, fallbacks, and monitoring needs. Source:
  `../datatalksclub.github.io/_podcast/building-scalable-and-reliable-machine-learning-systems.md`.

## Related Pages

Use these pages for adjacent data engineering and system design context.

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
