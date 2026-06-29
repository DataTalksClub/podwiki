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

Batch systems process data on a schedule or after data has landed in storage.
Streaming systems process events as they arrive, often through Kafka, Kinesis,
SQS, Flink, Spark Streaming, or similar infrastructure.

The podcast archive does not treat streaming as the mature default. Guests use
streaming when a product, model, or operational workflow needs immediate
reaction. They use batch when daily, hourly, or triggered processing gives the
business enough freshness with less operational load.

## Contents

- [Archive-Level Takeaways](#archive-level-takeaways)
- [Comparison Structure](#comparison-structure)
- [Decision Points](#decision-points)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Archive-Level Takeaways

### Latency should come from the decision, not the tool

The strongest archive pattern is simple: ask when the result is used. Retail
fraud prevention needs instant scoring because a cashier or security workflow
must act during the transaction. Many analytics, training, dashboard, and
backfill jobs do not need that latency.

Lars Albertsson's DataOps episode and Adrian Brudaru's modern data engineering
episode both warn against treating streaming as a badge of platform maturity.
When strict SLAs are absent, micro-batches or scheduled jobs may produce the
same business value with easier debugging and lower cost.

### Streaming moves complexity earlier

Streaming makes event order, schema contracts, replay, consumer lag, stateful
processing, and incident response part of the first design. Mehdi OUAZZA's
scale-up episode is useful because it makes the organizational cost visible:
Kafka only helps when teams also define schemas, registry practices,
guidelines, and downstream data contracts.

### Batch remains central for ML and analytics

Several ML and data engineering episodes keep batch in the architecture even
when real-time inference exists. Fraud detection combines daily feature
computation with instant inference. Production ML platform discussions include
batch scoring alongside online serving. Warehouse and lakehouse episodes still
use scheduled ingestion, transformation, and orchestration as core platform
work.

### Hybrid architectures are common

The archive rarely makes batch and streaming mutually exclusive. A system may
stream events into durable storage, run batch feature jobs, and serve a low
latency prediction from precomputed or partially updated data. The architecture
choice is usually about where freshness matters, where replay matters, and
which part of the system can fail without blocking the user.

## Comparison Structure

| Dimension | Batch | Streaming |
| --- | --- | --- |
| Best fit | Reporting, training, backfills, periodic sync, cost-aware transforms | Fraud checks, alerts, product events, operational triggers, live features |
| Freshness | Minutes, hours, or days | Seconds or near-real time |
| Failure mode | Late or missing job output | Lag, dropped or malformed events, state errors, duplicate processing |
| Operational burden | Scheduling, retries, partitions, backfills, data quality checks | All batch concerns plus brokers, ordering, schemas, state, replay, and consumers |
| Cost shape | Easier to run on cheaper scheduled compute | Often needs always-on infrastructure and specialized operators |
| Governance need | Dataset ownership, freshness, lineage, contracts | Event contracts, schema registry, consumer ownership, replay policy |

## Decision Points

### Use batch when freshness does not change the action

Batch is a strong default when the downstream action waits for a daily report,
a training run, a customer segment sync, a billing cycle, or an analyst review.
The archive's modern-stack episodes show that warehouse-centered ELT and dbt
workflows remain useful because they give analysts and analytics engineers a
clear place to inspect, test, and document transformations.

### Use streaming when a late answer loses value

Streaming earns its complexity when the window for action is short. Fraud
detection is the clearest archive example: the system needs to score a
transaction while the customer is still at the register. Product telemetry,
recommendations, operational alerts, and IoT events can fit the same pattern
when delayed processing would make the answer irrelevant.

### Choose micro-batching when the SLA allows it

Micro-batching often gives teams enough freshness without making every
transformation a true streaming job. Adrian Brudaru's modern data engineering
episode explicitly notes that much "streaming" is micro-batching unless a team
has strict SLAs. This is a useful vocabulary correction for architecture
reviews: name the actual latency target before naming the tool.

### Treat event contracts as part of streaming architecture

Streaming without contracts pushes pain downstream. The scale-up episode shows
why Kafka topics, schemas, and registry practices matter: software engineers
may publish events for service communication while data teams depend on those
same events for S3 landing, transformations, warehouse models, and analytics.
Without guidelines, the data platform inherits breakage that producers may not
notice.

## Episode Evidence

| Episode | Evidence | Source pointer |
| --- | --- | --- |
| [DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast.html) | At 41:53, compares batch and streaming by latency and use case. At 45:11, discusses micro-batching, dependency management, and predictability. | `../datatalksclub.github.io/_podcast/dataops-principles-and-scalable-data-platforms.md` |
| [From Notebooks to Production](https://datatalks.club/podcast.html) | At 13:25, lays out data pipeline anatomy. At 15:11, covers events and Kafka or Kinesis. At 16:51, compares streaming, which reacts immediately, with batch, which stores first and processes later. | `../datatalksclub.github.io/_podcast/production-ml-pipelines-with-aws-and-kafka.md` |
| [Scaling Data Engineering Teams](https://datatalks.club/podcast.html) | At 23:26, covers Kafka, schemas, schema registry, and data contracts as the practices that keep event streaming usable at scale. | `../datatalksclub.github.io/_podcast/scaling-data-engineering-teams-self-service-platforms.md` |
| [Data Engineering for Fraud Prevention](https://datatalks.club/podcast.html) | At 8:24, combines daily feature batches with real-time scoring. At 33:34 and 34:46, shows why fraud workflows need instant decisioning while still using batch computation. | `../datatalksclub.github.io/_podcast/building-and-scaling-data-engineering-systems-for-fraud-detection.md` |
| [Modern Data Engineering](https://datatalks.club/podcast.html) | At 51:19, compares micro-batching, Kafka, SQS, and Flink, and warns that streaming often means micro-batching unless the SLA is strict. | [summary]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}) |
| [Machine Learning System Design](https://datatalks.club/podcast.html) | Uses batch, online, streaming, and hybrid serving as system-design choices driven by product latency, fallbacks, and monitoring needs. | `../datatalksclub.github.io/_podcast/building-scalable-and-reliable-machine-learning-systems.md` |

## Related Pages

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

## Maintenance Notes

- Keep this page focused on architecture vocabulary and decision criteria. Tool
  tutorials for Kafka, Flink, Airflow, or Spark belong on tool-specific pages.
- Add future evidence when guests name the business action that forces
  real-time processing.
- When expanding the page, distinguish true streaming, micro-batching, online
  inference, batch scoring, and event ingestion. The archive uses all five
  patterns.
