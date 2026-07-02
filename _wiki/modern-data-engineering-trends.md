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
In [[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
[[person:adrianbrudaru|Adrian Brudaru]] describes the
shift away from "anyone who can do basic integration." He frames the newer
specializations around governance, data quality, and streaming
([[podcast:trends-in-modern-data-engineering|11:03]]).

The same trend sits inside the broader
[[Data Engineering]] topic.
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
([[podcast:trends-in-modern-data-engineering|11:03]]).
That makes modern data engineering closer to
[[Data Engineering Platforms]]
than to a single tool list.

The career implication isn't that junior engineers must learn every
specialization at the same time. Brudaru still recommends focusing on one area
first when someone is tempted to pursue data engineering, data science, and AI
engineering together
([[podcast:trends-in-modern-data-engineering|37:38]]).
The trend is specialization by business pressure, not specialization as a
resume taxonomy.

## Governance, Quality, and DataOps Move Upstream

Governance and quality are no longer cleanup steps after pipelines exist.
Brudaru ties modern platform choices to metadata and catalogs. He also includes
lineage and access layers
([[podcast:trends-in-modern-data-engineering|21:27-23:41]]).
Those concerns belong with
[[Data Quality and Observability]]
and [[Data Governance]] because
modern data systems need visible storage and compute choices. Metadata and
access choices need the same visibility.

[[person:christopherbergh|Christopher Bergh]] gives
the operating discipline behind that shift in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
He argues that modern teams need automation, testing, monitoring, and
observability. Those practices reduce production errors and cycle time
([[podcast:dataops-for-data-engineering|15:52-16:10]]).

Later, he makes CI/CD and realistic test data part of the same data delivery
practice. Infrastructure as code, deployment automation, and production
monitoring belong there too
([[podcast:dataops-for-data-engineering|30:55-50:29]]).
That places [[DataOps]] at the center of
modern data engineering rather than as a separate afterthought.

## The Modern Data Stack Gets Unbundled

Brudaru is skeptical of the phrase
[[Modern Data Stack]] when it
means a vendor package rather than a requirements-led architecture. He
describes the label as marketing around tools such as Fivetran, Snowflake, and
Looker. He then describes open-source "postmodern" alternatives that aim for
similar capability with better efficiency and lower cost
([[podcast:trends-in-modern-data-engineering|14:32-16:04]]).

That critique doesn't reject stack thinking, but it changes the evaluation unit.
Instead of asking whether a team bought the right branded stack, Brudaru asks
whether storage, compute, and transformation choices match the use case.
Orchestration, metadata, and cost choices need the same test.

His later tool-selection discussion warns teams to be cautious with vendors and
to choose tools from actual requirements
([[podcast:trends-in-modern-data-engineering|44:42]]).
The durable trend is composability with judgment, not tool maximalism.

## Open Formats and Local-First Tools Reduce Lock-In

Table formats are central here because Brudaru spends a substantial part of
the episode on [[Apache Iceberg]]
and Delta Lake. Hudi, catalogs, and DuckDB are part of the same discussion. He
explains Iceberg as a table format over files such as Parquet. It can support
updates without rewriting whole files and can reduce database or warehouse lock-in
([[podcast:trends-in-modern-data-engineering|18:17-19:11]]).

He then separates storage and compute through the catalog discussion. Access,
metadata, and lineage are separate concerns too
([[podcast:trends-in-modern-data-engineering|21:27-23:41]]).

The open-source trend is practical rather than ideological. Brudaru describes
DuckDB as an embeddable query engine that teams can use as a building block
across file systems, data lakes, and SQL databases
([[podcast:trends-in-modern-data-engineering|25:58]]).

He also describes cost-efficient setups that use DuckDB and GitHub Actions for
small data stacks. Headless Delta Lake and Iceberg support in DLT fit the same
direction
([[podcast:trends-in-modern-data-engineering|27:40-30:31]]).
That puts [[Open Source]] beside
lakehouse architecture and cost control rather than only community licensing.

## Streaming Is Requirement-Led

Modern data engineering includes [[Streaming]],
but the podcast discussion treats it as an SLA decision. Brudaru says streaming
is often micro-batching unless the system has strict latency requirements
([[podcast:trends-in-modern-data-engineering|51:19]]).
He names Kafka and SQS as common buffers. Flink and DuckDB are downstream
processing options
([[podcast:trends-in-modern-data-engineering|52:31]]).

The trend isn't "everything real time." It's a more careful split between
batch, micro-batch, and true event processing. Teams should pay the operational
cost of streaming only when freshness or user experience requires it. Control
systems and service-level commitments can justify the same cost.

## AI Engineering Pulls Data Engineers Closer to Product Systems

AI doesn't remove data engineering work in these episodes, but it changes where
data engineers apply it. Brudaru names AI integration as a 2025 trend and says
data engineers are building AI agents
([[podcast:trends-in-modern-data-engineering|16:40]]).
At 38:38, he argues that AI systems need data and algorithms. They also need
semantics, so data engineers will play an important role in agent systems
([[podcast:trends-in-modern-data-engineering|38:02-38:38]]).

Bergh adds the reliability boundary. In his DataOps discussion, he warns that
new labels around MLOps and LLMs can obscure the core systems-thinking work.
Data Mesh and Data Observability labels can create the same problem. Teams
still need quality checks and monitoring.

They also need safe deployments across day-one build, day-two operations, and
day-three change
([[podcast:dataops-for-data-engineering|18:46-24:24]]).
AI engineering convergence therefore increases the need for
[[DataOps]], not just prompt or model
skills.

## Cost Pressure Becomes an Engineering Constraint

Cost pressure is now part of modern data engineering design. In
[[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
[[person:eddyzulkifly|Eddy Zulkifly]] frames the data
platform as a digital warehouse. Data arrives and is stored in BigQuery.
The platform uses orchestrated SQL for transformation, and BI tools consume the
outputs
([[podcast:finops-for-data-engineers|21:57-22:36]]).
He adds that cloud systems change quickly, so monitoring and tests are needed
to keep the warehouse reliable
([[podcast:finops-for-data-engineers|24:34]]).

Zulkifly's FinOps discussion makes cost visible through usage data and metric
trees. Tagging and accountability turn that data into operating practice. He
describes cloud-cost factors such as servers, regional storage, backups, and
security requirements.

Capacity commitments, VM sizing, storage tiers, and licensing affect the same
cost model. Multi-cloud comparisons affect it too
([[podcast:finops-for-data-engineers|31:40-40:18]]).

He also ties FinOps processes back to DataOps-style CI/CD and dataset
validation. Downstream dashboard impact matters too
([[podcast:finops-for-data-engineers|46:17-48:01]]).

For modern data engineering, [[FinOps for Data Engineers]]
is the cost side of the same platform discipline. Reliable systems must also be
explainable in terms of spend, ownership, and business value.
