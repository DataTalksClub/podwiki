---
layout: wiki
title: "CDC"
summary: "CDC moves changed database rows into analytics systems without full reloads, with tradeoffs around deletes, schema changes, replay, and streaming operations."
related:
  - Data Engineering
  - Data Pipelines
  - Modern Data Stack
  - Streaming
  - DataOps
  - Data Engineering Platforms
  - Data Engineering Portfolio Projects
---

CDC means change data capture: moving database rows that changed since the last
sync instead of copying the whole source table again. In
[[data pipelines]], CDC sits near
ingestion. Teams choose it when a warehouse, lake, or
[[modern data stack]] needs
fresher source data without paying the cost of a full reload.

One connector-centered definition starts after an initial sync. An Airbyte-style
connector captures changed records and updates the destination with those
changes [[cite:data-engineering-tools-modern-data-stack@45:59=>ETL vs ELT and Modern Data Engineering]].
In a marketplace example, only 10% of rows may change. CDC avoids reading and
writing the other 90%. It also captures deleted rows that an append-only sync
might miss.

CDC isn't a replacement for [[ETL]],
[[ELT]], or
[[streaming]]. It's an ingestion method
that can feed any of them. [[ETL vs ELT]]
covers the transformation boundary. [[DataOps]]
and [[Data Engineering Platforms]]
cover the reliability work around the feed.

Santona Tuli puts CDC in the same complex-ingestion bucket as Kafka and Kinesis.
Once a team moves beyond scheduled Airflow batches, it has to handle ordering
and mixed batch-stream inputs. It also has to handle nested records and large
files
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@11:57=>Modern Data Pipelines]].
That makes CDC part of [[data engineering]]
and [[orchestration]] design, not only a connector setting.

## Captured Rows

CDC is row-level movement that captures inserts, updates, and deletions. Sellers
may change marketplace listing titles or prices. The data team wants those
changed listing records instead of another copy of all active listings
[[cite:data-engineering-tools-modern-data-stack@45:59=>ETL vs ELT and Modern Data Engineering]].
The destination can apply the changes to current-state tables or store history.

A lower-level version places CDC next to full database dumps, application change
events, database change tables, and Kafka. In that platform view, CDC translates
a database transaction log into a Kafka stream. Downstream systems then receive
detailed change events instead of periodic snapshots
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

When CDC emits events into shared streams, the event interface becomes part of
the product. Mehdi Ouazza's Kafka example shows why teams need typed schemas,
schema registries, and allowed-change rules. They need written guidelines before
one or two topics turn into hundreds
[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Scale Data Engineering Teams]].

The same discipline applies to CDC topics because consumers need stable keys,
delete semantics, and schema-change rules. That lets downstream
[[data pipelines]] evolve without guessing what changed.

The two views converge on the same boundary, but their emphasis differs.
[[person:nataliekwong=>Kwong]] emphasizes analytics connectors in the
[[modern data stack]], with CDC centered on cloud cost and sync speed, deletes,
and schema growth. [[person:larsalbertsson=>Albertsson]] emphasizes
[[DataOps]], immutability, dependency management, and the platform cost of
streaming. CDC is valuable in both settings because mutable source systems make
repeated full copies expensive and can hide changes between dumps.

## Fit Against Reloads, Batch, and Streaming

CDC fits when the source is mutable and full reloads are wasteful. It can help
when downstream consumers need changes before the next large batch can finish.
The immediate gains are speed and cloud cost
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
A full reload may still be simpler for small or low-value tables, one-off
backfills, or sources that don't expose reliable change signals.

CDC isn't a blanket "stream everything" recommendation. Many analytics and
reporting cases can wait for batch, including short micro-batches. Batch
orchestration gives engineers explicit dependencies and easier recovery.
Streaming helps in middle-latency cases such as fraud detection. It costs more
to operate [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Slawomir Chodnicki makes the same caution from a modern data-engineering
career lens. Kafka is useful when a product genuinely needs real time, but many
analytics teams should prove the low-latency need first
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for@37:38=>Data Engineer Career in 2026]].
For CDC, that means separating freshness from immediacy. A warehouse may need
incremental changes every few minutes. Fraud checks, dynamic pricing, or online
recommendations may justify a full [[streaming]]
or [[batch-vs-streaming=>batch vs streaming]] design.

CDC is a middle choice rather than a default. A team can capture database
changes continuously and still land them into batch-oriented tables or warehouse
models. The decision should weigh source change volume and acceptable latency.
It should also weigh recovery needs and whether the team can operate the
streaming infrastructure that a log-backed CDC design may require.

## Reliability and Reproducibility

CDC adds state to ingestion. A connector has to know where it left off and
which changes it already delivered. It also has to recover after a partial
failure.

That state may be a transaction-log position or a source cursor. It may also be
an offset in a stream or a destination-side checkpoint. Without it, retries can
duplicate rows or skip changes.

Mutable databases are hard to reason about unless the platform preserves
history. Immutable datasets and functional transformations matter because
repeated runs against mutable data can produce different results
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
CDC helps when it captures the changes between dumps. The destination still needs
an append-only history or careful merge logic if analysts must reproduce past
results.

CDC feeds need the same platform controls that fall under [[DataOps]].
The first controls are lag monitoring and alerts for stopped connectors.
Row-count tests and deleted-record checks cover data quality. Backfill runbooks
cover recovery.

The practical checks start with source freshness and complete windows. They add
delete reconciliation, schema compatibility, and replay behavior. These checks
connect CDC to [[dataops-checks-for-data-pipelines=>DataOps pipeline checks]]
and [[data-quality-and-observability=>data quality and observability]].
The team needs to know whether the feed stopped or delivered duplicate changes.
It also needs to catch missed deletes and tables that no longer match the source.

Platform maturity adds schema management automation and data quality
measurements [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
CDC needs those checks when it keeps warehouse tables current.

## Schema, Deletes, and Idempotency

CDC solves row movement, not every modeling problem. Business systems keep
adding fields as teams collect new information. A Salesforce checkbox can become
a new warehouse column
[[cite:data-engineering-tools-modern-data-stack@48:58=>ETL vs ELT and Modern Data Engineering]].
CDC pipelines have to handle those source changes without silently dropping
fields or breaking downstream models.

Schema evolution is separate from capturing changed rows. CDC tracks changed
rows, while schema evolution tracks new or changed fields. A source can update
existing records and add a new dimension at the same time. A useful CDC
pipeline handles both paths
[[cite:data-engineering-tools-modern-data-stack@45:59=>ETL vs ELT and Modern Data Engineering]]
[[cite:data-engineering-tools-modern-data-stack@48:58=>ETL vs ELT and Modern Data Engineering]].

Delete handling also matters because a pipeline that only upserts changed records
can leave stale rows in the destination. It needs delete markers
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
Downstream models can apply those markers to current tables or retain them in
historical logs for replay and audit.

Idempotency is the practical rule behind retries and replays. If a CDC job
runs the same event twice, the destination should end in the same state as if it
ran once. Teams usually get there with stable primary keys, event ordering, and
deduplication. Merge semantics and replayable raw change logs matter too. This
puts CDC inside [[data engineering]]
as reliability work rather than a connector checkbox.

## CDC Portfolio Evidence

For [[data engineering portfolio projects]],
CDC is useful only if the project shows the hard parts described here. A credible
project includes an initial load and incremental
changes. It also includes deletes, schema changes, retries, and a backfill
story. The writeup should explain why CDC was a better fit than a full reload or
scheduled batch job for that source.

The strongest portfolio version links CDC to the rest of the data platform. It
stores raw changes and models current-state tables. It adds quality checks, runs
through orchestration, and serves a small dashboard or downstream consumer. That
makes the project about reliable data movement, not only about running a
connector
[[cite:data-engineering-tools-modern-data-stack@45:59=>ETL vs ELT and Modern Data Engineering]]
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@11:57=>Modern Data Pipelines]].
