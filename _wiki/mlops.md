---
layout: wiki
title: "MLOps"
summary: "A bridge page for podcast evidence about operating machine learning systems: reproducibility, deployment, monitoring, retraining, governance, and team ownership."
related:
  - MLOps and DataOps
  - Data Quality and Observability
  - Machine Learning System Design
  - Production
---

## Definition and Scope

MLOps is the operating discipline for machine learning systems after they leave
experimentation. It covers the path from training to deployment. It also covers
serving, monitoring, retraining, incident response, governance, and ownership.

Use the larger [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
hub for the combined operating model across data and ML systems. Use this bridge
when the archive evidence is specifically about models and feature pipelines.
It also fits model registries, deployment paths, and ML platform teams.

## Recurring Archive Themes

The archive repeats a few MLOps ideas across platform, monitoring, and team
episodes:

- Platform guests don't treat MLOps as a tool category. They define it through
  infrastructure and repeatable process. Team enablement matters too.
- Teams reuse repository templates, CI/CD, model registries, and artifact
  storage. Shared deployment and monitoring conventions stop each project from
  inventing its own path.
- Guests discuss data versioning, traceability, experiment capture, and
  parameters. They also discuss dependencies, lineage, and exploratory notebook
  knowledge.
- Model failures often come from source data, feature pipelines, schema changes,
  distribution shift, or feedback loops.
- MLOps platform teams need quick wins and good developer experience. They also
  need feedback from product teams and clear support models.

## Episode Evidence

These episodes give the most direct evidence:

- [MLOps at Scale](https://datatalks.club/podcast.html): centralized MLOps as
  an enabling platform team. It covers adoption strategy, CI/CD, and repository
  structure. It also covers parameterization, monitoring, dependency management,
  and deployment-frequency KPIs.
- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  MLOps as people, processes, and technology. It covers experiment tracking,
  model registries, serving modes, and orchestration. It adds metadata, lineage,
  governance, API schemas, and on-call considerations.
- [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html):
  existing engineering primitives before new tools. The episode names Git,
  CI/CD, Kubernetes, registries, and standardized repositories.
- [MLOps Architect Guide](https://datatalks.club/podcast.html): model monitoring
  tied to ETL root causes and data observability. It also covers
  production-first monitoring, build-versus-buy choices, platform integration,
  and communication skills.
- [Human-Centered MLOps](https://datatalks.club/podcast.html): business cases,
  stakeholder buy-in, monitoring, and the human work behind trusted deployments.
- [MLOps in Finance](https://datatalks.club/podcast.html): regulated deployment
  concerns such as CI/CD, monitoring, governance, validation, and risk controls.
- [Lean MLOps for Startups](https://datatalks.club/podcast.html): lighter
  startup stacks and MVP constraints. It also covers SaaS adoption, vendor
  lock-in, and minimal operational discipline.

## Related Pages

Useful adjacent pages:

- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})

## Maintenance Notes

Future additions should stay model-specific:

- Add evidence here only when an episode discusses model-specific operations.
  Good examples include training deployment, inference deployment, model
  registries, and experiment tracking. Other good examples are retraining,
  model monitoring, feature pipelines, ML platform teams, and ML governance.
- Put pipeline-only reliability material on
  [DataOps]({{ '/wiki/dataops/' | relative_url }}) or
  [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
- Existing summaries to reuse:
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  and [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
