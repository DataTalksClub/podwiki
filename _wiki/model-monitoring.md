---
layout: wiki
title: "Model Monitoring"
summary: "A bridge page for podcast evidence about watching deployed models and retraining signals."
related:
  - MLOps
  - Data Quality and Observability
  - Data Observability
  - Model Registry
---

## Definition and Scope

Model monitoring is the practice of watching a deployed model and its
surrounding data system after release. In the archive, teams monitor input
quality and feature distributions, plus prediction distributions, latency and
errors. They also watch drift, feedback, business outcomes and root cause
signals. Alerting ties those signals to response.

Use this page when the evidence is model-specific. Use
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}) when
the evidence focuses on freshness, schema, volume, or lineage. Pipeline
incidents without a model-specific focus also belong there.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive connects model monitoring to data and operations:

- Production models fail for upstream reasons. Danny Leybzon ties model
  monitoring to ETL, data pipelines, and observability because model behavior
  often changes when inputs or transformations change.
- Monitoring becomes easier to sell after a team feels pain. Teams with models
  already in production understand drift, broken models, or model outages more
  quickly than teams still in development.
- Data drift and concept drift are separate concerns. Thom Ives describes why
  teams need ongoing human oversight. New data, new features, and changed
  business workflows can make the old model less useful.
- Prediction logging needs shared schemas. The platform episode discusses
  request and response logging so teams can analyze model behavior
  later.
- Monitoring is part of adoption. Raphaël Hoogvliets suggests starting with
  monitoring when teams don't know what production models are doing.

## Episode Evidence

These episodes give the strongest monitoring evidence:

- [MLOps Architect Guide](https://datatalks.club/podcast.html): At
  25:04-31:50, the episode covers production-first monitoring, upstream ETL root
  causes, and data profiling. It also covers anomaly detection,
  alerts, and the shift from "why monitor" to "how to monitor". At 36:47-39:29,
  it discusses platform-agnostic integrations and heterogeneous tooling.
- [Feature Engineering, Model Monitoring, and Data Governance](https://datatalks.club/podcast.html):
  At 47:30-49:28, the episode discusses production monitoring, data drift, and
  concept drift. It also covers ongoing maintenance and whether the model
  remains the best model for production. Earlier sections tie this to ETL
  reliability, feature quality, and governance.
- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 54:15-55:29, the episode discusses API and logging design for storing
  requests, predictions, and responses in a shared schema. Teams can then
  monitor and analyze model behavior. Reuse the [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 48:41, Raphaël
  says monitoring is the right starting point when teams have models in
  production but don't know what they're doing. At 60:54-61:36, he defines
  MLOps as keeping models running because data changes. Reuse the
  [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [Data Quality and Observability](https://datatalks.club/podcast.html): Data
  observability episodes supply upstream failure modes that matter for model
  monitoring. They include freshness, schema and volume, plus lineage, alerting
  and recovery. See [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

## Related Pages

Use these pages for adjacent reliability topics.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/mlops-model-monitoring-data-observability.md`
- `../datatalksclub.github.io/_podcast/feature-engineering-model-monitoring-and-data-governance.md`
- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/human-centered-mlops-and-model-monitoring.md`

Add future evidence when a source names what's monitored, who receives alerts,
how teams diagnose root cause, or what triggers retraining. Keep generic data
quality evidence on the observability pages unless the model impact is explicit.
