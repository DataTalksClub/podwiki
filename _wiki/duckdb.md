---
layout: wiki
title: "DuckDB"
summary: "How DataTalks.Club podcast guests place DuckDB in local OLAP, Parquet analytics, cost-aware pipelines, GitHub Actions workflows, headless table formats, and practical data engineering prototypes."
related:
  - Data Engineering Platforms
  - Apache Iceberg
  - Data Lake
  - Data Warehouse vs Data Lakehouse
  - Modern Data Stack
  - Data Engineering Portfolio Projects
  - Data Pipelines
---

DuckDB appears in the DataTalks.Club archive as embeddable local OLAP. It can
run close to files and Python code without requiring a separate warehouse
service. The strongest archive discussion comes from
[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
In that episode, he places DuckDB next to open table formats. He also connects
it to catalogs and cheaper orchestration options.

This places DuckDB inside the
[data engineering platform]({{ '/wiki/data-engineering-platforms/' | relative_url }})
conversation, not only beside laptop analytics. It also belongs beside
[Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }}),
[Data Lake]({{ '/wiki/data-lake/' | relative_url }}), and the
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
comparison. The archive discusses it as a portable access layer over files,
lakes, and table-format experiments.

## Definition

DuckDB is useful in the archive when a team wants analytical SQL before it
stands up a large data platform. Brudaru describes it as embeddable. Engineers
can use it as a building block inside another product or pipeline. In DLT, his
team uses DuckDB to query data through one interface. That interface covers
file systems, data lakes, and SQL databases
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
25:58).

That definition is narrower than "replace the warehouse". DuckDB gives teams a
local OLAP engine and a portable way to query files. It doesn't provide the
full operating surface of a warehouse, lakehouse, catalog, or governed platform.
Teams still need ingestion and scheduling around it. They also need metadata,
ownership, tests, and access controls.

Use [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
for that workflow layer. Use
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) for the
warehouse-centered stack DuckDB is often compared with.

## Archive Anchors

The main DuckDB episode is
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}). The
relevant stretch starts with [Apache Iceberg]({{ '/wiki/apache-iceberg/' | relative_url }})
as a Parquet-backed table format at 18:17. Brudaru then covers catalogs,
metadata, and lineage at 21:27. DuckDB enters the discussion at 25:58 as
embeddable local OLAP, then GitHub Actions appears at 27:40 as a low-cost
workflow option.

[From Academic Research to Lean Data Consulting]({{ '/podcasts/from-academic-research-to-data-engineering-freelancing/' | relative_url }})
adds the practitioner version. [Orell Garten]({{ '/people/orellgarten/' | relative_url }})
uses local analysis and CSV-first discovery for client work before he automates
ingestion and processing. Later, he names DuckDB as a tool he uses for both
prototyping and actual pipelines because it integrates with Python
(42:16-42:58 and 58:37).

Two older episodes explain why this local and file layer matters.
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
has Andreas Kretz discussing Parquet on S3 and Docker jobs at 25:36-26:09.
Later, he recommends simple proof-of-concept work before heavier infrastructure
(57:33-58:56). In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) explains
how data engineers and data scientists can collaborate through files. Parquet
can serve that boundary even when the teams use different languages or tools
(10:29 and 16:26-17:04).

For a tool-category overview, the
[Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
article places DuckDB in the newer lakehouse and cost-aware tooling landscape.

## Cost-Aware Pipelines

Brudaru's strongest DuckDB claim is economic because teams are challenging high
vendor costs. He also references setups that use DuckDB with GitHub Actions to
run whole data stacks cheaply
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
27:40). He then connects portability to cheaper compute options such as GitHub
Actions at 28:44.

GitHub Actions doesn't become a universal orchestrator in this framing. Brudaru
later says orchestration depends on the team. Airflow remains common, while
Prefect and Dagster also appear. GitHub Actions can be enough for simple
workflows because it's serverless and cheaper than always-on orchestrators
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
35:37-37:08).

DuckDB fits bounded batch workloads that are cheap to rerun. A small pipeline
can extract data and write Parquet. It can then query or transform the data with
DuckDB and publish a table or file without paying for an always-on warehouse. For
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
DuckDB helps a project show ingestion and modeling. The project can also show
checks and cost judgment before adding Spark, Kafka, or Kubernetes.

## Parquet and Local Analytics

DuckDB's archive role depends on Parquet and file-based analytics. Brudaru
places DuckDB immediately after the Iceberg discussion, where Iceberg is a table
format over Parquet storage. Catalogs map that data to compute
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
18:17-23:41). DuckDB then becomes one compute path over local or lake-backed
data, rather than the data owner.

Roksolana Diachuk's episode gives the older collaboration model. Big data
engineers often work with Avro, Parquet, and ProtoBuf rather than only JSON or
CSV. Data scientists may consume Parquet files from Python without entering
the data engineering codebase
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
10:29 and 16:26-17:04). DuckDB makes that file boundary easier to query with
SQL, especially when the work starts on one machine.

Andreas Kretz adds cloud-storage context through Parquet files on S3 and Docker
jobs. Those jobs can read from a data lake and write results elsewhere
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
25:36-26:09). DuckDB can be part of that family of bounded processors when the
data size, latency, and reliability requirements fit.

## Fit With Warehouses and Lakehouses

The archive doesn't frame DuckDB as a full substitute for a warehouse or
lakehouse. It frames DuckDB as a portable query engine that can reduce the need
to push every transformation into a managed warehouse. That distinction matters
because warehouses and lakehouses still solve access, governance, sharing, and
operational problems that DuckDB doesn't solve alone.

Use a warehouse-centered [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
when the main work is governed SQL analytics. That side also fits dbt-style
modeling, BI, reverse flows, and analyst access. Use a lakehouse-oriented design
when the team needs open storage, table formats, catalogs, and multiple compute
engines. DuckDB can
serve as one compute engine for small transformations. It can also fit
validation, local exploration, and cost-sensitive batch jobs
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
25:58-30:31).

DuckDB also connects to headless table formats. Brudaru says DuckDB provides a
local access layer that's useful for data pipelines. He then discusses DLT work
on headless Delta Lake and Iceberg
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
29:33-30:31). In that design, storage and table metadata stay open while
compute can move between local jobs, GitHub Actions, and larger engines.

## Lean Discovery Before Infrastructure

Orell Garten's consulting episode gives the clearest reason not to overbuild
around DuckDB. He starts client work by figuring out what data exists. He then
checks how to access it and what problem the client wants solved. He may pull
one day or one period of files onto his computer and analyze them locally. Only
after that does he move toward automated ingestion and scheduled processing
([From Academic Research to Lean Data Consulting]({{ '/podcasts/from-academic-research-to-data-engineering-freelancing/' | relative_url }}),
42:16-42:58).

DuckDB fits that lean discovery phase because it's easy to try and needs no
server. Garten recommends starting with a get-started tutorial. Then he compares
the new tool against a problem he already solved with another approach. He uses
DuckDB for prototyping and actual pipelines. Still, he treats tool choice as
secondary to solving the client problem
([From Academic Research to Lean Data Consulting]({{ '/podcasts/from-academic-research-to-data-engineering-freelancing/' | relative_url }}),
50:33-53:03 and 58:37).

This keeps DuckDB connected to [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
rather than isolated as a tool preference. Start with the consumer, source
behavior, and output. Then decide whether local SQL over files is enough or
whether the work needs a warehouse, lakehouse, orchestrator, or streaming
system.

## Overuse Boundaries

DuckDB is a poor default when the real requirement is shared platform
operation. If many teams need governed access and lineage, the work belongs
closer to
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}).
The same is true when teams need catalog discovery, role-based permissions, and
BI integration.

Brudaru's catalog discussion makes that boundary explicit. Catalogs map data to
compute and manage access control, and some catalogs also handle metadata and
lineage
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
21:27).

DuckDB is also not a reason to skip pipeline discipline. Kretz warns learners
not to start with Kubernetes and Airflow on huge datasets. He still frames
production work through ingestion and processing. He also includes storage,
visualization and scheduling. Serving decisions remain part of the same work
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
13:25-26:09 and 57:33-58:56).

DuckDB can simplify one processing layer. It doesn't remove the need to test
outputs, rerun jobs, and explain who consumes the result.

DuckDB is also not automatically the right answer for strict streaming or
large distributed workloads. Brudaru mentions DuckDB as a downstream processing
option next to tools such as Flink. He also says streaming is often
micro-batching unless strict SLAs require a stricter architecture
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
51:19-52:31).

Use DuckDB when local OLAP and file-backed SQL match the problem. It also fits
low-cost batch processing. Move to heavier systems when concurrency and latency
demand them. Governance, data size, and team operations can also demand heavier
systems.
