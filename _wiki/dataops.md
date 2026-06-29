---
layout: wiki
title: "DataOps"
summary: "Podcast-grounded reference page for DataOps as the operating discipline for reliable data pipelines, analytics workflows, and data platforms."
related:
  - Data Engineering Platforms
  - Data Quality and Observability
  - Data Observability
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
---

DataOps is the operating discipline for data pipelines, analytics workflows,
and data platforms. It covers version control, tests, CI/CD, orchestration,
observability, reproducibility, deployment confidence, and recovery for data
work. Use [MLOps]({{ '/wiki/mlops/' | relative_url }}) for the separate
discipline around production machine learning systems. Use
[MLOps vs DataOps]({{ '/articles/mlops-vs-dataops/' | relative_url }}) for the
comparison.

## Link Map

Related wiki pages:
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}),
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}), and
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}).

Core podcast interviews:
[DataOps 101](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
[DataOps and GitOps for Data Teams](https://datatalks.club/podcast/dataops-and-gitops-best-practices-for-data-teams.html),
[Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
and
[Data Quality, Data Observability, and Data Reliability](https://datatalks.club/podcast/data-quality-observability-reliability.html).

## Common Definition

Across the archive, DataOps means making data delivery reliable and repeatable.
In [Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
Christopher Bergh frames DataOps around error reduction, deployment cycle time,
productivity, observability, automated runbooks, version control, tests, and
CI/CD. In
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
the same operating model is tied to automation, regression tests, realistic
test data, observability, deployment confidence, on-call readiness, and
production monitoring.

The common thread is that data systems keep changing. Sources change, schemas
change, files arrive late, transformations break, and downstream consumers may
notice bad data before the producing team does. DataOps adds the operating
habits that help teams prevent, detect, explain, and recover from those
failures.

## Where Guests Differ

Guests differ on whether DataOps starts from platform design or team delivery
practice. In
[DataOps 101](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
Lars Albertsson emphasizes scalable platforms, immutable pipelines,
reproducibility, self-service, batch versus streaming tradeoffs, quality
automation, and Data Mesh risks. In
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
Christopher Bergh emphasizes the day-to-day delivery loop: version control,
tests, CI/CD, observability, runbooks, and automation.

Those views are compatible, but they imply different first steps. A platform
team may start with self-service infrastructure and shared conventions. A
smaller analytics or data engineering team may start with Git, tests, a
scheduler, basic observability, and a recovery runbook.

## Pipeline Delivery

DataOps applies to pipelines, transformations, datasets, dashboards, data
products, and analytics workflows. In
[Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
the operating pressure appears across ELT, ingestion, dbt-style
transformations, orchestration, CDC, schema evolution, and warehouse analytics
workflows.

This is where [Orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
connect to DataOps. The goal is not a tool label. The goal is a data delivery
path another person can review, test, rerun, observe, and fix.

## Observability and Recovery

DataOps depends on observability, but it is broader than observability. In
[Data Quality, Data Observability, and Data Reliability](https://datatalks.club/podcast/data-quality-observability-reliability.html),
the observability layer includes freshness, volume, distribution, schema,
lineage, ownership, SLAs, and runbooks. DataOps uses those signals inside the
larger delivery system: alerts, recovery steps, deployment paths, and ownership.

Use [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}) for
that monitoring layer. Use this DataOps page for the operating model around the
monitoring layer.

## Relation to MLOps

DataOps and MLOps overlap because production ML depends on production data.
DataOps owns the reliability of upstream pipelines, datasets, features,
metadata, and quality checks. [MLOps]({{ '/wiki/mlops/' | relative_url }})
adds model artifacts, training jobs, inference paths, model registries,
retraining decisions, and model behavior.

The overlap matters in incidents. A model alert may come from model drift, but
it may also come from a late table, a changed schema, a broken feature pipeline,
or a missing label. That is why
[MLOps Architect Guide](https://datatalks.club/podcast/mlops-model-monitoring-data-observability.html)
connects model monitoring to ETL root causes and data observability.

## Related Pages

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
