---
layout: wiki
title: "Modern Data Engineering Trends"
summary: "How DataTalks.Club podcast guests describe modern data engineering trends: specialization, governance, quality, DataOps, AI convergence, open lakehouse formats, streaming pragmatism, and FinOps pressure."
related:
  - Data Engineering
  - Modern Data Stack
  - Streaming
  - Data Quality and Observability
  - Data Engineering Platforms
  - DataOps
  - FinOps for Data Engineers
  - Apache Iceberg
  - Open Source
---

Modern data engineering is moving from one broad pipeline-building role toward
more specialized platform and operating disciplines. The important lanes are
governance and reliability. AI systems, cost control, and platform work are
also data engineering concerns.
In [Modern Data Engineering Trends](https://datatalks.club/podcast/trends-in-modern-data-engineering.html),
[Adrian Brudaru](https://datatalks.club/people/adrianbrudaru.html) describes the
shift away from "anyone who can do basic integration." He frames the newer
specializations around governance, data quality, and streaming
([11:03](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

The same trend sits inside the broader
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) topic.
Modern teams still need SQL and Python. They also need ingestion, modeling, and
orchestration.

Consumer-facing datasets still matter, but the operating standard changes.
Teams are expected to make those systems governed and observable.
They also need to make them cost-aware and useful for AI products rather than
only scheduled dashboards.

## Specialization Replaces the Generic Data Engineer

Brudaru's 2025 view is that the field has split into deeper lanes. Governance
work handles sensitive data, policy, metadata, and access. Data quality work
turns broken or ambiguous datasets into testable systems. Streaming work
appears when the business has latency or event-processing requirements
([11:03](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
That makes modern data engineering closer to
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
than to a single tool list.

The career implication isn't that junior engineers must learn every
specialization at the same time. Brudaru still recommends focusing on one area
first when someone is tempted to pursue data engineering, data science, and AI
engineering together
([37:38](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
The trend is specialization by business pressure, not specialization as a
resume taxonomy.

## Governance, Quality, and DataOps Move Upstream

Governance and quality are no longer cleanup steps after pipelines exist.
Brudaru ties modern platform choices to metadata and catalogs. He also includes
lineage and access layers
([21:27-23:41](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
Those concerns belong with
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) because
modern data systems need visible storage and compute choices. Metadata and
access choices need the same visibility.

[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) gives
the operating discipline behind that shift in
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html).
He argues that modern teams need automation, testing, monitoring, and
observability. Those practices reduce production errors and cycle time
([15:52-16:10](https://datatalks.club/podcast/dataops-for-data-engineering.html)).

Later, he makes CI/CD and realistic test data part of the same data delivery
practice. Infrastructure as code, deployment automation, and production
monitoring belong there too
([30:55-50:29](https://datatalks.club/podcast/dataops-for-data-engineering.html)).
That places [DataOps]({{ '/wiki/dataops/' | relative_url }}) at the center of
modern data engineering rather than as a separate afterthought.

## The Modern Data Stack Gets Unbundled

Brudaru is skeptical of the phrase
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) when it
means a vendor package rather than a requirements-led architecture. He
describes the label as marketing around tools such as Fivetran, Snowflake, and
Looker. He then describes open-source "postmodern" alternatives that aim for
similar capability with better efficiency and lower cost
([14:32-16:04](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

That critique doesn't reject stack thinking, but it changes the evaluation unit.
Instead of asking whether a team bought the right branded stack, Brudaru asks
whether storage, compute, and transformation choices match the use case.
Orchestration, metadata, and cost choices need the same test.

His later tool-selection discussion warns teams to be cautious with vendors and
to choose tools from actual requirements
([44:42](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
The durable trend is composability with judgment, not tool maximalism.

## Open Formats and Local-First Tools Reduce Lock-In

Table formats are central here because Brudaru spends a substantial part of
the episode on [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }})
and Delta Lake. Hudi, catalogs, and DuckDB are part of the same discussion. He
explains Iceberg as a table format over files such as Parquet. It can support
updates without rewriting whole files and can reduce database or warehouse lock-in
([18:17-19:11](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

He then separates storage and compute through the catalog discussion. Access,
metadata, and lineage are separate concerns too
([21:27-23:41](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

The open-source trend is practical rather than ideological. Brudaru describes
DuckDB as an embeddable query engine that teams can use as a building block
across file systems, data lakes, and SQL databases
([25:58](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

He also describes cost-efficient setups that use DuckDB and GitHub Actions for
small data stacks. Headless Delta Lake and Iceberg support in DLT fit the same
direction
([27:40-30:31](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
That puts [Open Source]({{ '/wiki/open-source/' | relative_url }}) beside
lakehouse architecture and cost control rather than only community licensing.

## Streaming Is Requirement-Led

Modern data engineering includes [Streaming]({{ '/wiki/streaming/' | relative_url }}),
but the podcast discussion treats it as an SLA decision. Brudaru says streaming
is often micro-batching unless the system has strict latency requirements
([51:19](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
He names Kafka and SQS as common buffers. Flink and DuckDB are downstream
processing options
([52:31](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

The trend isn't "everything real time." It's a more careful split between
batch, micro-batch, and true event processing. Teams should pay the operational
cost of streaming only when freshness or user experience requires it. Control
systems and service-level commitments can justify the same cost.

## AI Engineering Pulls Data Engineers Closer to Product Systems

AI doesn't remove data engineering work in these episodes, but it changes where
data engineers apply it. Brudaru names AI integration as a 2025 trend and says
data engineers are building AI agents
([16:40](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).
At 38:38, he argues that AI systems need data and algorithms. They also need
semantics, so data engineers will play an important role in agent systems
([38:02-38:38](https://datatalks.club/podcast/trends-in-modern-data-engineering.html)).

Bergh adds the reliability boundary. In his DataOps discussion, he warns that
new labels around MLOps and LLMs can obscure the core systems-thinking work.
Data Mesh and Data Observability labels can create the same problem. Teams
still need quality checks and monitoring.

They also need safe deployments across day-one build, day-two operations, and
day-three change
([18:46-24:24](https://datatalks.club/podcast/dataops-for-data-engineering.html)).
AI engineering convergence therefore increases the need for
[DataOps]({{ '/wiki/dataops/' | relative_url }}), not just prompt or model
skills.

## Cost Pressure Becomes an Engineering Constraint

Cost pressure is now part of modern data engineering design. In
[FinOps for Data Engineers](https://datatalks.club/podcast/finops-for-data-engineers.html),
[Eddy Zulkifly](https://datatalks.club/people/eddyzulkifly.html) frames the data
platform as a digital warehouse. Data arrives and is stored in BigQuery.
The platform uses orchestrated SQL for transformation, and BI tools consume the
outputs
([21:57-22:36](https://datatalks.club/podcast/finops-for-data-engineers.html)).
He adds that cloud systems change quickly, so monitoring and tests are needed
to keep the warehouse reliable
([24:34](https://datatalks.club/podcast/finops-for-data-engineers.html)).

Zulkifly's FinOps discussion makes cost visible through usage data and metric
trees. Tagging and accountability turn that data into operating practice. He
describes cloud-cost factors such as servers, regional storage, backups, and
security requirements.

Capacity commitments, VM sizing, storage tiers, and licensing affect the same
cost model. Multi-cloud comparisons affect it too
([31:40-40:18](https://datatalks.club/podcast/finops-for-data-engineers.html)).

He also ties FinOps processes back to DataOps-style CI/CD and dataset
validation. Downstream dashboard impact matters too
([46:17-48:01](https://datatalks.club/podcast/finops-for-data-engineers.html)).

For modern data engineering, [FinOps for Data Engineers]({{ '/wiki/finops-for-data-engineers/' | relative_url }})
is the cost side of the same platform discipline. Reliable systems must also be
explainable in terms of spend, ownership, and business value.
