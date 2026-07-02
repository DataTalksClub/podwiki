---
layout: wiki
title: "DuckDB"
summary: "How DataTalks.Club podcast guests place DuckDB in local OLAP, Parquet analytics, cost-aware pipelines, GitHub Actions workflows, headless table formats, and practical data engineering prototypes."
related:
  - Data Engineering Platforms
  - Apache Iceberg
  - Data Lake
  - Modern Data Stack
  - Data Engineering Portfolio Projects
  - Data Pipelines
---

DuckDB is an embeddable local OLAP engine. It can run close to files and Python
code without requiring a separate warehouse service, sitting next to open table
formats and connecting to catalogs and cheaper orchestration options
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

This places DuckDB inside the
[[data-engineering-platforms|data engineering platform]]
conversation, not only beside laptop analytics. It also belongs beside
[[Apache Iceberg]],
[[Data Lake]], and the
[[Data Warehouse vs Data Lakehouse]]
comparison, as a portable access layer over files, lakes, and table-format
experiments.

## Definition

DuckDB suits a team that wants analytical SQL before it stands up a large data
platform. As an embeddable engine, it works as a building block inside another
product or pipeline. In DLT, DuckDB queries data through one interface that
covers file systems, data lakes, and SQL databases
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

That definition is narrower than "replace the warehouse". DuckDB gives teams a
local OLAP engine and a portable way to query files. It doesn't provide the
full operating surface of a warehouse, lakehouse, catalog, or governed platform.
Teams still need ingestion and scheduling around it. They also need metadata,
ownership, tests, and access controls.

Use [[Data Pipelines]]
for that workflow layer. Use
[[Modern Data Stack]] for the
warehouse-centered stack DuckDB is often compared with.

## Key Episodes

The main DuckDB episode is
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]
with [[person:adrianbrudaru|Adrian Brudaru]]. It covers
[[Apache Iceberg]]
as a Parquet-backed table format, catalogs, metadata, and lineage, DuckDB as
embeddable local OLAP, and GitHub Actions as a low-cost workflow option.

[[podcast:from-academic-research-to-data-engineering-freelancing|From Academic Research to Lean Data Consulting]]
adds the practitioner version. Local analysis and CSV-first discovery come
before automated ingestion and processing, and DuckDB serves both prototyping
and actual pipelines because it integrates with Python.

Two older episodes explain why this local and file layer matters.
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]
covers Parquet on S3 and Docker jobs, and recommends simple proof-of-concept
work before heavier infrastructure. In
[[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]],
data engineers and data scientists collaborate through files; Parquet can serve
that boundary even when the teams use different languages or tools.

For a tool-category overview, the
[[Data Engineering Tools]]
article places DuckDB in the newer lakehouse and cost-aware tooling landscape.

## Cost-Aware Pipelines

DuckDB's strongest claim is economic, as teams challenge high vendor costs. Some
setups use DuckDB with GitHub Actions to run whole data stacks cheaply,
connecting portability to cheaper compute options
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

GitHub Actions doesn't become a universal orchestrator in this framing.
Orchestration depends on the team: Airflow remains common, while Prefect and
Dagster also appear. GitHub Actions can be enough for simple workflows because
it's serverless and cheaper than always-on orchestrators
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

DuckDB fits bounded batch workloads that are cheap to rerun. A small pipeline
can extract data and write Parquet. It can then query or transform the data with
DuckDB and publish a table or file without paying for an always-on warehouse. For
[[Data Engineering Portfolio Projects]],
DuckDB helps a project show ingestion and modeling. The project can also show
checks and cost judgment before adding Spark, Kafka, or Kubernetes.

## Parquet and Local Analytics

DuckDB ties to Parquet and file-based analytics. It sits alongside Iceberg, a
table format over Parquet storage, where catalogs map that data to compute
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
DuckDB then becomes one compute path over local or lake-backed data, rather than
the data owner.

An older collaboration model shows big data engineers often working with Avro,
Parquet, and ProtoBuf rather than only JSON or CSV, while data scientists
consume Parquet files from Python without entering the data engineering codebase
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).
DuckDB makes that file boundary easier to query with SQL, especially when the
work starts on one machine.

Cloud storage adds context through Parquet files on S3 and Docker jobs that read
from a data lake and write results elsewhere
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).
DuckDB can be part of that family of bounded processors when the data size,
latency, and reliability requirements fit.

## Fit With Warehouses and Lakehouses

DuckDB isn't a full substitute for a warehouse or lakehouse. It's a portable
query engine that can reduce the need to push every transformation into a
managed warehouse. That distinction matters because warehouses and lakehouses
still solve access, governance, sharing, and operational problems that DuckDB
doesn't solve alone.

Use a warehouse-centered [[Modern Data Stack]]
when the main work is governed SQL analytics. That side also fits dbt-style
modeling, BI, reverse flows, and analyst access. Use a lakehouse-oriented design
when the team needs open storage, table formats, catalogs, and multiple compute
engines. DuckDB can
serve as one compute engine for small transformations. It can also fit
validation, local exploration, and cost-sensitive batch jobs
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

DuckDB also connects to headless table formats, providing a local access layer
that's useful for data pipelines, alongside DLT work on headless Delta Lake and
Iceberg
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).
In that design, storage and table metadata stay open while compute can move
between local jobs, GitHub Actions, and larger engines.

## Lean Discovery Before Infrastructure

Consulting practice gives the clearest reason not to overbuild around DuckDB.
Client work starts by figuring out what data exists, how to access it, and what
problem the client wants solved. Pulling one day or one period of files onto a
computer for local analysis comes first; automated ingestion and scheduled
processing come only after
([[podcast:from-academic-research-to-data-engineering-freelancing|From Academic Research to Lean Data Consulting]]).

DuckDB fits that lean discovery phase because it's easy to try and needs no
server. A good approach starts with a get-started tutorial, then compares the
new tool against a problem already solved another way. DuckDB serves both
prototyping and actual pipelines, but tool choice stays secondary to solving the
client problem
([[podcast:from-academic-research-to-data-engineering-freelancing|From Academic Research to Lean Data Consulting]]).

This keeps DuckDB connected to [[Data Pipelines]]
rather than isolated as a tool preference. Start with the consumer, source
behavior, and output. Then decide whether local SQL over files is enough or
whether the work needs a warehouse, lakehouse, orchestrator, or streaming
system.

## Overuse Boundaries

DuckDB is a poor default when the real requirement is shared platform
operation. If many teams need governed access and lineage, the work belongs
closer to
[[Data Engineering Platforms]]
and [[Data Warehouse vs Data Lakehouse]].
The same is true when teams need catalog discovery, role-based permissions, and
BI integration.

Catalogs make that boundary explicit: they map data to compute and manage access
control, and some also handle metadata and lineage
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

DuckDB is also not a reason to skip pipeline discipline. Learners shouldn't start
with Kubernetes and Airflow on huge datasets, but production work still runs
through ingestion and processing, along with storage, visualization, scheduling,
and serving decisions
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).

DuckDB can simplify one processing layer. It doesn't remove the need to test
outputs, rerun jobs, and explain who consumes the result.

DuckDB is also not automatically the right answer for strict streaming or
large distributed workloads. It's a downstream processing option next to tools
such as Flink, and streaming is often micro-batching unless strict SLAs require a
stricter architecture
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]]).

Use DuckDB when local OLAP and file-backed SQL match the problem. It also fits
low-cost batch processing. Move to heavier systems when concurrency and latency
demand them. Governance, data size, and team operations can also demand heavier
systems.
