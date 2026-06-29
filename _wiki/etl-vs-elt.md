---
layout: wiki
title: "ETL vs ELT"
summary: "A podcast-backed comparison of transform-before-load and load-before-transform patterns in modern data engineering."
related:
  - ELT
  - Data Engineering
  - Data Engineering Platforms
  - Analytics Engineering
---

## Definition and Scope

ETL means extract, transform, load: data is pulled from source systems,
transformed before or during movement, then loaded into the destination where it
will be consumed. ELT means extract, load, transform: raw or lightly processed
data is loaded first, usually into a warehouse or lakehouse, and transformed
afterward.

The podcast archive treats this as an architecture and ownership choice, not a
religious split. ELT became attractive as cloud warehouses, cheap storage, dbt,
and analytics engineering made warehouse-side SQL transformations practical.
ETL still matters when staging, compliance, performance, source constraints, or
complex preprocessing require transformation before loading.

## Contents

- [Comparison](#comparison)
- [Boundary Principles](#boundary-principles)
- [When ETL Matters](#when-etl-matters)
- [When ELT Matters](#when-elt-matters)
- [Podcast Evidence](#podcast-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Comparison

| Question | ETL | ELT |
| --- | --- | --- |
| Order | Extract, transform, then load. | Extract, load, then transform. |
| Usual destination | Curated warehouse tables, marts, operational targets, or specialized stores. | Raw or staging layer in a warehouse, lake, or lakehouse before modeled layers. |
| Transformation owner | Often data engineering or platform teams. | Often analytics engineering or analytics teams using SQL/dbt-style workflows. |
| Main advantage | Control before data lands: reduce volume, enforce shape, protect sensitive fields, handle complex staging. | Flexibility after landing: preserve source detail, iterate business logic, empower SQL users, reduce re-extraction. |
| Main risk | Business logic changes can require pipeline changes or full re-extraction. | Raw zones can become messy without ownership, tests, documentation, and cleanup. |

## Boundary Principles

### ETL encodes business logic before the destination

Natalie Kwong's modern data stack episode describes ETL as source-specific
extraction, organization-specific business logic, and destination-specific load
routines. The customer acquisition cost example shows why transformation may be
needed to join CRM revenue and ad spend into a useful data mart.

### ELT preserves optionality

The same episode gives the strongest archive explanation for ELT: when business
logic changes or a new source field appears, loading more source detail first
lets teams write a new transformation instead of re-extracting the source. ELT
also lowers the dependency on engineering teams when analysts or analytics
engineers can work in the warehouse with SQL.

### ELT depends on governance

Loading first does not mean business users should query raw data directly. The
archive describes ingestion layers as raw zones that should feed modeled layers,
marts, and BI-facing tables. Without ownership and guardrails, ELT can produce
inconsistent metric definitions and a data swamp.

### The modern stack moved transformation closer to analysts

ELT and dbt-style workflows are a key reason analytics engineering appears in
the archive. Data engineers still own ingestion, orchestration, infrastructure,
and platform reliability. Analytics engineers often own the warehouse-side
business transformations and tests that turn raw data into trusted analytical
models.

## When ETL Matters

Use ETL when transformation before loading reduces risk or complexity:

- source data is too large, expensive, or sensitive to land raw
- privacy rules require masking, filtering, or aggregation before storage
- the destination cannot support the needed transformation efficiently
- operational systems need curated payloads, not broad analytical history
- legacy enterprise systems already depend on staged ETL jobs
- complex preprocessing is easier outside the warehouse

## When ELT Matters

Use ELT when flexibility and warehouse-side modeling are more important:

- analysts and analytics engineers need fast iteration on business logic
- source schemas change and teams need to preserve new fields
- storage is cheaper than repeated extraction
- dbt-style tests, documentation, lineage, and dependency graphs are available
- the data warehouse or lakehouse can compute transformations efficiently
- multiple marts can reuse the same raw or staging layer

## Podcast Evidence

| Episode | Evidence |
| --- | --- |
| [ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast.html) | At 3:46-6:37, ETL is defined through extract, transform, load and source/business/destination routines. The CAC example joins CRM and ad-spend sources. |
| [ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast.html) | At 7:57-12:37, ELT is presented as more flexible because data lands before business logic, which reduces re-extraction when fields or needs change. |
| [ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast.html) | At 12:39-15:03, ELT is connected to analyst autonomy, SQL, dbt, and faster warehouse-side transformations. |
| [ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast.html) | At 15:30-18:47, the episode distinguishes raw ingestion layers from production-ready data marts with guardrails. |
| [ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast.html) | At 41:30-43:02, ETL's continued relevance is tied to large enterprises and complex staging contexts. |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | At 5:47-10:04, dbt is described as warehouse-side transformation with SQL, version control, documentation, tests, and dependency graphs. |
| [Data-Led Growth, Event Tracking, and Reverse ETL](https://datatalks.club/podcast.html) | Adds the downstream side: modeled warehouse data may later be activated back into operational tools through reverse ETL. |

## Related Pages

- [ELT]({{ '/wiki/elt/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`,
  `../datatalksclub.github.io/_podcast/analytics-engineer-skills-tools.md`,
  and `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- Keep this page as a decision boundary. Put broader platform architecture on
  [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  and role implications on [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
- Future improvement: add more evidence from CDC, schema evolution, and data
  lakehouse episodes to refine when raw landing zones are appropriate.
