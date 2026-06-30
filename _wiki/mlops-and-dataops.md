---
layout: wiki
title: "MLOps and DataOps"
summary: "Navigation page separating MLOps and DataOps into distinct concepts and pointing to the comparison article."
related:
  - MLOps
  - DataOps
  - ML Platforms
  - Data Engineering Platforms
  - Data Quality and Observability
---

[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[DataOps]({{ '/wiki/dataops/' | relative_url }}) both borrow reliability
practice from software operations, but they operate different things. MLOps
operates machine learning systems after experimentation. DataOps operates data
delivery through pipelines and analytics workflows. It also covers tests,
observability, and recovery.

Use this bridge when an old link or a mixed production incident mentions both
terms. For the full boundary, read
[MLOps vs DataOps]({{ '/articles/mlops-vs-dataops/' | relative_url }}).

## MLOps

Use [MLOps]({{ '/wiki/mlops/' | relative_url }}) when the work centers on the
model lifecycle. That lifecycle covers experiments, artifacts, registries, and
serving. It also covers monitoring, retraining, governance, and ML platform
ownership. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
defines MLOps around people, operating practice, and technology. Around 5:11,
he ties MLOps to how teams develop, deploy, and serve models.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) lists
the practical MLOps toolbelt around 52:39. He includes version control, CI/CD,
containerization, and package registries. For the model side, he includes model
registries, experiment tracking, and monitoring. For runtime, he includes
compute and serving.

Those episodes make MLOps narrower than "anything reliable in production." The
model-specific handoffs are the useful boundary. A model leaves exploration,
another person needs to reproduce the run, an artifact enters a registry, and a
batch job or online endpoint serves predictions. After release, the team
monitors model behavior.

## DataOps

Use [DataOps]({{ '/wiki/dataops/' | relative_url }}) when the work centers on
data delivery. That includes data pipelines, platform workflows, analytics
releases, and orchestration. It also includes version control, tests, and
CI/CD. Observability and recovery belong in the same operating discipline.

In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) defines
DataOps around enablement, workflows, and continuous deployment around 11:57.
He also ties it to self-service data pipelines and aligned people. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) frames
DataOps around lowering production errors, shortening deployment cycle time, and
improving team productivity around 6:42.

That makes DataOps a delivery discipline for data systems, not a synonym for
MLOps.

In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
Bergh applies the same boundary around 31:45. He covers CI/CD pipelines,
regression tests, and realistic test data. He also covers infrastructure as
code. DataOps works on the data path from sources to transformations,
orchestrated jobs, datasets, and dashboards. Alerts and runbooks keep that path
dependable.

## Incident Boundary

MLOps and DataOps meet when a production model depends on upstream data. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) explains around
27:35 that a model problem often starts earlier in the data pipeline. Model
observability therefore needs visibility into upstream ETL and transformations.
Treat that as overlap in incident diagnosis, not a reason to merge the terms.

Use [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) when the
alert concerns prediction behavior, model versions, or serving health. It also
fits labels, feedback, and retraining. Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
or [Data Observability]({{ '/wiki/data-observability/' | relative_url }}) when
the root cause is freshness, volume, schema, or distribution. It also fits
lineage, ownership, and upstream pipeline failures.

## Related Paths

Continue from the page that matches the object you need to operate.

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) for model lifecycle ownership.
- [DataOps]({{ '/wiki/dataops/' | relative_url }}) for reliable data delivery.
- [MLOps vs DataOps]({{ '/articles/mlops-vs-dataops/' | relative_url }}) for the
  comparison and incident boundary.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
  [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  for the platform side of each discipline.
