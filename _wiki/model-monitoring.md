---
layout: wiki
title: "Model Monitoring"
summary: "How teams watch deployed models, diagnose drift, and assign ownership for production ML behavior."
related:
  - MLOps
  - Data Quality and Observability
  - ML Platforms
  - Model Registry
  - Machine Learning Infrastructure
  - Production
  - A/B Testing
---

Model monitoring is the practice of watching a deployed model and the
production system around it. Teams track input data, predictions, service
health, and response paths. Those signals show whether the model still behaves
well after deployment and whether the right team knows when to investigate.

Model monitoring is part of [[MLOps]], not a
dashboard bolted onto the end of a project. Production monitoring connects to
upstream [[data pipelines]]
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).
That matters because a model can degrade when the model artifact is unchanged
but the data, features, labels, or serving path changed.

## Production Signals

Model monitoring starts with production signals that tell a team whether a
model still works for its intended use. Teams usually track input distributions
and prediction distributions. They also track service errors, latency, and
business outcomes. They may track user or stakeholder feedback too. The
monitoring system needs to help the team diagnose a problem after an alert
fires.

In the data-science version, Thom Ives separates data drift from concept drift
([[person:thomives|Thom Ives]],
[[podcast:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]).
The training data may stop matching the current world. The relationship between
features and outcomes may change too.

In the human-centered version, live test sets and small A/B tests detect model
issues. Teams watch input distributions, unit changes, and feature drift.
Logging, feature stores, and reproducibility support the work
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]).
Monitoring is useful only when teams can debug and respond.

## Monitoring Priorities

Production models need monitoring, but guests prioritize different operating
problems. Danny Leybzon focuses on production pain. Teams that already have
production models are distinct from teams still before deployment. The market
conversation shifts from why monitoring matters to how teams should monitor
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).

Lina Weichbrodt focuses on people and incident response, so service levels and
impact assessment happen with stakeholders. ML incidents connect to post-mortems
and recovery steps
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]).
That monitoring system needs a human response path, not only metrics.

Maria Vechtomova treats monitoring as part of the minimum MLOps stack and a
roadmap priority. It may need to fit existing observability tools rather than
forcing a separate ML-only stack
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]).

Raphaël Hoogvliets focuses on adoption. The core challenge is keeping deployed
models monitored and maintained. Solving tangible pain points comes first.
Monitoring sits alongside experiment tracking, registries, and serving in the
MLOps toolset
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

For startup validation, Evidently began with customer discovery around
post-production model failures. Models can break without anyone noticing.
Monitoring can disappear after data scientists leave
[[cite:building-mlops-startup|MLOps Startup|43:59]].
Evidently treated monitoring as both an [[MLOps]] operating practice and a
product pain for an MLOps startup.

## Data Drift

Data drift covers changes in the input data a model receives after deployment.
The model may still run, but the feature values no longer look like the
training data
([[person:thomives|Thom Ives]],
[[podcast:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]).
The same episode links monitoring to feature work and ETL reliability, and
connects monitoring to
[[data governance]].

In the production-operations version, observability connects to ETL and data
pipelines, and to upstream root causes
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).

That link is why model monitoring and
[[data-quality-and-observability=>data observability]] overlap.
The model team needs model-specific signals, but many failures start in
upstream freshness or schema changes. Volume and distribution changes can
break the model too.

Deployment population is part of the monitored distribution. In healthcare, a
model developed on European patients may not generalize to African clinical
settings. Disease prevalence, available measurements, collection practices, and
infrastructure can differ. European data can still inform reasoning, but it
shouldn't automatically justify an algorithm for a low-resource setting
[[cite:building-healthcare-machine-learning-systems|Healthcare ML Systems|35:45]].
That makes population coverage a [[Machine Learning System Design]] constraint
as well as a [[data-quality-and-observability=>data observability]] signal.

Barr Moses covers silent data incidents and model drift. She also covers
freshness, volume, and distribution as data reliability signals. Schema and
lineage matter too
([[person:barrmoses|Barr Moses]],
[[podcast:data-quality-data-observability-data-reliability=>Data Observability Explained]]).
For model monitoring, those signals help explain whether drift came from the
data system or from model behavior.

## Model Performance

Model performance monitoring tracks whether predictions still match the task.
For some systems, teams can compare predictions with labels after a delay. For
others, teams watch proxy metrics and human review. Customer complaints,
business KPIs, or small experiments may provide earlier signals.

Tying monitoring to real response paths covers live test sets and small
[[a-b-testing=>A/B tests]]. It also covers user feedback channels, internal bug
reports, and widespread user complaints
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]).
Those signals matter when labels are late or incomplete.

Ives covers model selection, accuracy, variance, and generalizability. He also
covers the move from selecting a model to maintaining it
([[person:thomives|Thom Ives]],
[[podcast:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]).
A model can be good at release and still become the wrong model later.

## Observability

Monitoring detects that something may be wrong, and observability helps a team
explain why. Danny Leybzon makes the distinction concrete through profiles,
pipelines, and integrations. His example uses data profiling architecture with
WhyLogs and a backend for storing profiles. It also uses platform-agnostic
integrations because production models run through many serving tools
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).

Observability connects to platform design through API design and unified
prediction schemas for logging requests, predictions, and responses
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
That schema gives teams material for later monitoring and analysis.

This is where [[machine learning infrastructure]]
and [[ML platforms]] matter. A model
service needs to log the right inputs and outputs before a team can diagnose
drift alerts, latency spikes, or bad prediction clusters.

## Alerts

Alerts make monitoring operational because they name a team, a severity, and a
next action. From the data side, teams need contextual alerts and fewer false
positives, and alerts connect to runbooks and remediation
([[person:barrmoses|Barr Moses]],
[[podcast:data-quality-data-observability-data-reliability=>Data Observability Explained]]).

Sabina Firtala's domestic-risk assessment episode adds the high-stakes version
of the same rule. After a risk-scoring tool enters frontline workflows,
monitoring has to watch for drift and trigger maintenance alerts. The response
path still needs human review because the served population may change after
release. Source data and operational workflows can change too
[[cite:building-domestic-risk-assessment-tool|Building a Domestic Risk Assessment Tool]].

Model alerts have the same problem. If every distribution shift pages a team,
people stop trusting the monitoring system. The incident-response view adds the
human test: post-mortem evidence and investigation steps become action items and
workflow changes
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]).

Teams should alert on signals that someone can act on. For model teams, those
signals usually include input quality and prediction distribution. They also
include service health and label-backed performance. They may include business
impact or a stakeholder complaint path too.

## Ownership

Model monitoring fails when no one owns the response. The owning team may be a
product team, an ML engineering team, a central MLOps team, or a data platform
team. The right owner depends on the failure mode.

A central MLOps team provides infrastructure, reusable CI/CD, and monitoring
support
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]).
But the product or feature team still needs to understand the model and its
users.

Hoogvliets describes the MLOps team as an enabling platform team. That team
supports product teams and ML engineers
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]). Monitoring
belongs in that shared ownership boundary: the platform can provide the tools,
but the model owner must interpret the business impact.

Stakeholder ownership turns stakeholder concerns into mitigations and metrics.
Teams use service levels and impact assessment to decide what kind of incident
response a model needs
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]).

## MLOps and Platforms

Model monitoring is one layer of the larger MLOps system. A team needs
[[experiment tracking]] and a
[[model registry]] to know which
model version is running. A team needs
[[reproducibility]] when it has to
recreate training conditions. Alerts also need
[[production]] practices for
deployment, rollback, and incident response.

Stiebellehner's platform sequence starts with experiment tracking and model
registries. It then runs through batch inference and online serving.
Orchestration, metadata, and lineage come next
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Monitoring uses those pieces after release.

Vechtomova places version control, CI/CD, and registries in the same stack.
Model registry, deployment, and monitoring belong there too
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]).
Standardizing monitoring can come after teams have already solved earlier
deployment and reproducibility problems.

## Related Pages

Use these pages for adjacent MLOps, platform, and observability concepts.

- [[MLOps]]
- [[MLOps Tools]]
- [[MLOps Roadmap]]
- [[ML Platforms]]
- [[Machine Learning Infrastructure]]
- [[Model Registry]]
- [[Experiment Tracking]]
- [[Reproducibility]]
- [[data-quality-and-observability=>Data Observability]]
- [[Data Quality and Observability]]
- [[Machine Learning System Design]]
- [[Production]]
