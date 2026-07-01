---
layout: wiki
title: "CDC"
summary: "Change data capture in the DataTalks.Club archive: when to capture row-level database changes, how CDC compares with batch dumps and streaming, and what teams must operate around schema changes, deletes, and replay."
related:
  - Data Engineering
  - Data Pipelines
  - Modern Data Stack
  - Streaming
  - DataOps
  - Data Engineering Platforms
  - Data Engineering Portfolio Projects
---

CDC means change data capture. In a data engineering context, teams use it to
move database rows that changed since the last sync. Teams use it instead of
copying the whole source table again. It belongs near ingestion in
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}). Teams usually
choose it when a warehouse, lake, or
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}) needs
fresher source data without a full reload.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the
clearest definition in
[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
at 45:59-48:30. She explains CDC through Airbyte-style connectors: after an
initial sync, the connector captures changed records and updates the
destination with those changes. Her practical example is that if only 10% of
rows changed, CDC avoids reading and writing the other 90%. She also calls out
deleted rows as part of the value.

CDC isn't a replacement for [ETL]({{ '/wiki/etl/' | relative_url }}),
[ELT]({{ '/wiki/elt/' | relative_url }}), or [streaming]({{ '/wiki/streaming/' | relative_url }}).
It's an ingestion technique that can feed any of them. Use
[ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }}) for the transformation
boundary. Use [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
for the reliability and platform work around the feed.

## Captured Changes

Kwong frames CDC as row-level change movement. The source table may receive
inserts, updates, and deletes, and the CDC feed records those changed rows. The
destination then applies the changes rather than replacing the full table. In
the 47:26 chapter, the discussion turns to online marketplace listings. If
sellers update titles or prices, the data team wants the changed listing
records instead of another copy of all active listings.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) describes a
lower-level version in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
at 1:06:01-1:07:52. He places CDC next to full database dumps, application
change events, database change tables, and Kafka. In his wording, CDC can
translate the database transaction log into a Kafka stream so a data platform
can receive detailed change events.

Those two descriptions line up. Kwong focuses on the analytics connector
experience, where teams move less data and keep the destination current.
Albertsson focuses on the platform architecture, where teams preserve the
database changes that a full hourly or daily dump would miss.

## Fit Against Reloads, Batch, and Streaming

CDC fits when the source is mutable and the table is large enough that full
reloads are wasteful. It also fits when downstream consumers need changes
before the next large batch can reasonably finish. Kwong's 45:59 discussion
names speed and cloud cost as the immediate gains. A full reload may still be
simpler for small or low-value tables. It may also be simpler for one-off
backfills or sources that don't expose reliable change signals.

At 41:53-45:19, Albertsson compares batch and streaming. That discussion keeps
CDC from turning into a blanket "stream everything" recommendation. He argues
that many analytics and reporting cases can wait for batch, sometimes even short
micro-batches. Batch orchestration gives engineers explicit dependencies and
easier recovery. Streaming helps in the middle latency window, such as fraud
detection, but it costs more to operate.

That makes CDC a middle choice rather than a default. A team can capture
database changes continuously and still land them into batch-oriented tables or
warehouse models. The team still has to weigh source change volume and
acceptable latency. It also has to weigh recovery needs and how much streaming
infrastructure it can operate.

## Operating Requirements

CDC adds state to ingestion. A connector has to know where it left off and
which changes it already delivered. It also has to recover after a partial
failure.

That state may be a transaction-log position or a source cursor. It may also be
an offset in a stream or a destination-side checkpoint. Without it, retries can
duplicate rows or skip changes.

Albertsson's DataOps lesson is that mutable databases are hard to reason about
unless the platform preserves history. At 16:42-20:12, he argues for immutable
datasets and functional transformations because repeated runs against mutable
data can produce different results. CDC helps when it captures the changes
between dumps. The destination still needs an append-only history or careful
merge logic if analysts must reproduce past results.

Teams also need normal [dataops]({{ '/wiki/dataops/' | relative_url }})
controls around CDC feeds:

- monitoring for lag
- alerts for stopped connectors
- tests for expected row counts
- checks for deleted records
- runbooks for backfills

Albertsson's DataOps maturity chapter at 46:52 adds schema management
automation and data quality measurements to that operating model.

## Schema, Deletes, and Idempotency

CDC solves row movement, not every modeling problem. Kwong's schema-evolution
discussion at 48:58-49:32 explains that business systems keep adding fields as
teams collect new information. A Salesforce checkbox or picklist can become a
new warehouse column. CDC pipelines have to handle those source changes without
silently dropping fields or breaking downstream models.

Deletes need the same care, and Kwong specifically names deleted rows at 48:30.
A pipeline that only upserts changed records may keep stale rows forever unless
it sends delete markers into the destination. Analytical tables then need a
clear choice. They can keep a current-state table, a full history table, or
both.

Idempotency is the practical rule behind retries and replays. If a CDC job
runs the same event twice, the destination should end in the same state as if it
ran once. Teams usually get there with stable primary keys, event ordering, and
deduplication. Merge semantics and replayable raw change logs matter too. This
is where CDC connects to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) as an
operating discipline rather than a connector checkbox.

## Guest Tradeoffs

Kwong and Albertsson agree that CDC exists because mutable source systems make
full copies expensive and incomplete. Both treat CDC as a way to capture the
changes that matter instead of repeatedly moving a whole table.

They focus on different risks. Kwong, speaking from Airbyte and the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}), centers
connector coverage and cloud cost. She also centers sync speed, deletes, and
schema growth. Her view is useful when a team is building warehouse-centered
ELT ingestion.

Albertsson starts from DataOps and scalable data engineering platforms, putting
reproducibility and immutability at the center. He also focuses on dependency
management and the cost of operating streaming systems. His view is useful when
a team evaluates CDC as a log-backed platform capability. It also helps when
the team asks whether simple dumps and short batch jobs are enough.

## Project Signals

For [data engineering portfolio projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
CDC is useful only if the project shows the hard parts. A credible CDC project
should include an initial load and incremental changes. It should also include
deletes, schema changes, retries, and a backfill story. The writeup should
explain why CDC was a better fit than a full reload or a scheduled batch job
for that source.

The strongest portfolio version links CDC to the rest of the data platform. It
stores raw changes and models current-state tables. It adds quality checks, runs
through orchestration, and serves a small dashboard. It may also serve another
downstream consumer. That makes the project about reliable data movement, not
only about running a connector.
