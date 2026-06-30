---
layout: "person"
title: "Barr Moses"
source_person: "../datatalksclub.github.io/_people/barrmoses.md"
person_id: "barrmoses"
summary: "Monte Carlo co-founder contributing the archive's data observability and data reliability reference for freshness, lineage, schema changes, and downtime prevention."
expertise: ["data observability", "MLOps", "data quality", "data reliability"]
podcast_episodes: ["data-quality-data-observability-data-reliability"]
source_url: "https://datatalks.club/people/barrmoses.html"
---
## Podcast Context

Barr Moses gives the archive its core early definition of data observability.
The relevant bio context is that she led customer data and analytics work before
co-founding Monte Carlo. In the episode, she uses that operating experience to
explain why data teams often learn about broken data from executives or
customers. The failure report often comes from business users instead of the
data team's own systems.

This profile is useful when a question needs the reliability model behind
freshness, volume, schema, and lineage. It also covers root-cause analysis,
SLAs, and false-positive reduction.

## Podcast Contributions

This episode defines the data reliability vocabulary used by later pages:

- [Data Observability Explained](https://datatalks.club/podcast.html) defines
  data downtime as a reliability problem for analytics, ML, and data products.
  Barr connects it to the moment when a dashboard, board report, model, or
  downstream workflow silently depends on bad data.
- She maps software observability ideas into the data world but explains why
  batch data differs from application monitoring. Data failures can be late,
  partial, skewed, or schema-breaking before a consumer notices.
- The episode introduces the five pillars of data observability: freshness,
  volume, distribution, schema, and lineage.
- Later sections cover RACI-style ownership, data SLAs, threshold automation,
  operational runbooks, and maturity stages. They also cover platform criteria,
  auto lineage, anomaly context, and false-positive reduction.

## Reusable Claims and Examples

These claims are reusable in future topic pages:

- Data teams are often the last to know about a data incident. Observability
  should detect data downtime before a stakeholder asks why a number looks
  wrong.
- Monitoring and observability are different. Monitoring detects a symptom.
  Observability helps diagnose root cause through context, correlation, logs,
  and lineage.
- Lineage turns an alert into impact analysis because teams can see which
  dashboards, ML jobs, and downstream consumers are affected.
- Good pipelines can still deliver bad data. Pipeline success isn't enough if
  volume, schema, or freshness changed in a way that breaks the
  use case.
- False positives are an adoption risk. Alerts need context, thresholds,
  ownership, and runbooks or teams will ignore them.

## Connected Concepts

Use these existing hubs for follow-up topic work:

- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  for freshness, schema, lineage, and data downtime.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  for platform ownership, pipeline contracts, lineage, and downstream impact.
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}) for
  production reliability when models depend on data freshness and quality.
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
  for the consumer-facing trust problem that makes data downtime a product
  issue.

## Source Links

Use these sources for verification:

- Canonical podcast index:
  [DataTalks.Club Podcast](https://datatalks.club/podcast.html)
- Person source: `../datatalksclub.github.io/_people/barrmoses.md`
- Podcast source:
  `../datatalksclub.github.io/_podcast/data-quality-data-observability-data-reliability.md`
- Useful incident timestamps include data downtime impact at 4:35, DevOps
  observability origins at 6:56, batch data challenges at 9:49, and silent
  failures at 13:40.
- Useful operations timestamps include five pillars at 16:38, a schema-change
  case study at 19:10, and monitoring versus observability at 24:31.
- Ownership timestamps include RACI at 29:00, data SLAs at 35:24, and false
  positives at 60:27.

## Podcast Discussions

- [Data Observability Explained: 5 Pillars to Prevent Downtime, Drift & False Positives]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}). Related topics: [MLOps]({{ '/wiki/mlops/' | relative_url }}), [data observability]({{ '/wiki/data-observability/' | relative_url }}).
