---
layout: wiki
title: "CDC"
summary: "Change data capture in podcast discussions: when to capture row-level database changes, how CDC compares with batch dumps and streaming, and what teams must operate around schema changes, deletes, and replay."
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

[[person:nataliekwong|Natalie Kwong]] gives the
connector-centered definition in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering at 45:59-48:30]].
After an initial sync, an Airbyte-style connector captures changed records and
updates the destination with those changes. Her marketplace example is
practical. If only 10% of rows changed, CDC avoids reading and writing the other
90%. It also includes deleted rows that an append-only sync might miss.

CDC isn't a replacement for [[ETL]],
[[ELT]], or
[[streaming]]. It's an ingestion method
that can feed any of them. [[ETL vs ELT]]
covers the transformation boundary. [[DataOps]]
and [[Data Engineering Platforms]]
cover the reliability work around the feed.

## Captured Rows

Kwong frames CDC as row-level movement that captures changed rows from inserts
and updates as well as deletions. In
the [[podcast:data-engineering-tools-modern-data-stack|47:26 marketplace-listing chapter]],
sellers change titles or prices. The data team wants those changed listing
records rather than another copy of all active listings. The destination can
apply the changes to current-state tables or store history.

[[person:larsalbertsson|Lars Albertsson]] describes a
lower-level version in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms at 1:06:01-1:07:52]].
He places CDC next to full database dumps, application change events, database
change tables, and Kafka. In that platform view, CDC translates a database
transaction log into a Kafka stream so downstream systems receive detailed
change events instead of periodic snapshots.

The two views converge on the same boundary, but their emphasis differs. Kwong
emphasizes analytics connectors in the
[[modern data stack]], with CDC
centered on cloud cost and sync speed. She also covers deletes and schema
growth.
Albertsson emphasizes [[DataOps]],
immutability, dependency management, and the platform cost of streaming. CDC is
valuable in both settings because mutable source systems make repeated full
copies expensive and can hide changes between dumps.

## Fit Against Reloads, Batch, and Streaming

CDC fits when the source is mutable and the table is large enough that full
reloads are wasteful. It also fits when downstream consumers need changes
before the next large batch can reasonably finish. Kwong's
[[podcast:data-engineering-tools-modern-data-stack|45:59 CDC discussion]]
names speed and cloud cost as the immediate gains. A full reload may still be
simpler for small or low-value tables, one-off backfills, or sources that don't
expose reliable change signals.

Albertsson's
[[podcast:dataops-principles-and-scalable-data-platforms|41:53-45:19 batch-versus-streaming discussion]]
keeps CDC from becoming a blanket "stream everything" recommendation. He argues
that many analytics and reporting cases can wait for batch, including short
micro-batches. Batch orchestration gives engineers explicit dependencies and
easier recovery. Streaming helps in the middle latency window, such as fraud
detection, but it costs more to operate.

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

Albertsson's [[DataOps]] lesson is that
mutable databases are hard to reason about unless the platform preserves
history. In
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 at 16:42-20:12]],
he argues for immutable datasets and functional transformations because repeated
runs against mutable data can produce different results. CDC helps when it
captures the changes between dumps. The destination still needs an append-only
history or careful merge logic if analysts must reproduce past results.

CDC feeds need the same platform controls that Albertsson puts under DataOps.
The first controls are lag monitoring and alerts for stopped connectors.
Row-count tests and deleted-record checks cover data quality. Backfill runbooks
cover recovery.

His
[[podcast:dataops-principles-and-scalable-data-platforms|46:52 maturity discussion]]
adds schema management automation and data quality measurements. Those checks
matter when CDC is the feed that keeps warehouse tables current.

## Schema, Deletes, and Idempotency

CDC solves row movement, not every modeling problem. Kwong's
[[podcast:data-engineering-tools-modern-data-stack|48:58-49:32 schema-evolution discussion]]
explains that business systems keep adding fields as teams collect new
information. A Salesforce checkbox or picklist can become a new warehouse
column. CDC pipelines have to handle those source changes without silently
dropping fields or breaking downstream models.

Kwong calls out delete handling at
[[podcast:data-engineering-tools-modern-data-stack|48:30 in the CDC example]].
A pipeline that only upserts changed records can leave stale rows in the
destination unless it sends delete markers. Downstream models can apply those
markers to current tables or retain them in historical logs for replay and
audit.

Idempotency is the practical rule behind retries and replays. If a CDC job
runs the same event twice, the destination should end in the same state as if it
ran once. Teams usually get there with stable primary keys, event ordering, and
deduplication. Merge semantics and replayable raw change logs matter too. This
puts CDC inside [[data engineering]]
as reliability work rather than a connector checkbox.

## Project Signals

For [[data engineering portfolio projects]],
CDC is useful only if the project shows the hard parts that Kwong and
Albertsson describe. A credible project includes an initial load and incremental
changes. It also includes deletes, schema changes, retries, and a backfill
story. The writeup should explain why CDC was a better fit than a full reload or
scheduled batch job for that source.

The strongest portfolio version links CDC to the rest of the data platform. It
stores raw changes and models current-state tables. It adds quality checks, runs
through orchestration, and serves a small dashboard or downstream consumer. That
makes the project about reliable data movement, not only about running a
connector.
