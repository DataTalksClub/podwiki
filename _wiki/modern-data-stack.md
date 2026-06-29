---
layout: wiki
title: "Modern Data Stack"
summary: "How the podcast archive describes the modern data stack across ELT, warehouses, dbt-style transformations, orchestration, activation, lakehouse patterns, and tool-selection cautions."
related:
  - Data Engineering Platforms
  - ELT
  - dbt
  - Analytics Engineering
  - Data Warehouse
  - Reverse ETL
---

## Definition and Scope

Teams use the modern data stack to move data from sources into analytical
storage. They transform it with SQL-oriented workflows and expose it through BI
or product analytics. Sometimes they send it back to operational tools. In the
archive, the core flow is ELT into a warehouse, dbt-style transformations, and
orchestration. Analytics engineering and reverse data flows complete the loop.

The archive also cautions against treating the term as a fixed architecture.
Natalie Kwong explains the classic stack with Airbyte, a warehouse, dbt, and
orchestration. BI and reverse ETL appear as downstream pieces. Santona Tuli
broadens the topic into pipeline design across ingestion, staging, warehouses,
and lakehouses. Adrian Brudaru later calls the modern data stack partly vendor
packaging and argues for requirements-led tool selection.


## Recurring Archive Themes

ELT and warehouse-side transformation are central. The archive explains why
teams load data first, preserve source detail, and transform later in the
warehouse or lakehouse. This supports analyst autonomy and faster changes to
business logic.

Analytics engineering emerged from this stack. dbt-style workflows brought SQL,
version control, tests, and documentation closer to analysts and analytics
engineers. Dependency graphs became part of the work too.

The archive treats the stack as more than ingestion and dashboards. Episodes add
data marts and orchestration, cover CDC and schema evolution, and discuss
staging areas and reverse data flows. Data quality and governance sit in the
same operating layer.

Modern stack choices depend on the use case. Analytics pipelines, ML pipelines,
streaming systems, and activation workflows need different constraints. Santona
Tuli's pipeline episode repeatedly moves the conversation from named tools to
the user problem.

The term can be marketing because Adrian Brudaru's trend episode warns that
vendors package interchangeable tools as a category. Teams still need to choose
based on cost, openness, governance, and data quality. Streaming needs and
operational skills matter too.

## Episode Evidence

These episodes give the strongest evidence:

- [Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html),
  3:46-15:03: defines ETL and ELT. It explains why ELT supports flexibility and
  analyst autonomy, then connects dbt to analytics engineering. Source:
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`.
- [Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html),
  15:30-33:45: covers data marts and ingestion layers. Natalie also discusses
  lakes, warehouses, and data swamps before moving to architecture decisions and
  orchestration. She then covers Airbyte's extract-load role.
- [Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html),
  33:45-39:06: lists common modern analytics stack components and adds
  operational reverse data flows.
- [Modern Data Pipelines](https://datatalks.club/podcast.html), 24:57-37:10:
  contrasts analytics and ML pipelines, describes dbt's role, and discusses
  Snowflake and Databricks choices. It also covers staging and lakehouse
  architecture.
  Source:
  `../datatalksclub.github.io/_podcast/modern-data-pipelines-orchestration-ingestion-modeling.md`.
- [Data-Led Growth Stack](https://datatalks.club/podcast.html), 41:30-44:24:
  gives the growth version of the modern data stack. It includes collection,
  product analytics, a warehouse, and activation through CDP or reverse ETL
  paths. Source:
  `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- [Modern Data Engineering Trends](https://datatalks.club/podcast.html),
  14:32-18:17 and 31:29-44:42: critiques the modern data stack label. Adrian
  adds Iceberg and catalogs while also covering DuckDB, dbt alternatives,
  orchestration choices, and vendor-caution guidance. Source:
  `../datatalksclub.github.io/_podcast/trends-in-modern-data-engineering.md`.

## Tradeoffs

The modern data stack speeds up analytics when teams have many SaaS sources and
cloud warehouse capacity. It also fits SQL-heavy transformations and BI or
product analytics consumers. It can create too many tools, unclear ownership,
duplicated metrics, and rising warehouse costs.

Warehouse-first ELT gives flexibility, but it pushes governance later in the
flow. Teams need model ownership, tests, documentation, and cleanup. They also
need orchestration and data quality checks so raw zones and staging layers don't
become permanent confusion.

Open-source and postmodern stacks can reduce lock-in, but they still need
operating discipline. The archive treats tool choice as secondary to pipeline
requirements, team skills, cost, and reliability.

## Related Pages

Useful adjacent pages:

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }})
- [ELT]({{ '/wiki/elt/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
