---
layout: wiki
title: "Model Monitoring"
summary: "Podcast-grounded reference page for watching deployed models, diagnosing drift, and assigning ownership for production ML behavior."
related:
  - MLOps
  - Data Observability
  - ML Platforms
  - Model Registry
  - Machine Learning Infrastructure
  - Production
---

Model monitoring is the practice of watching a deployed model and the
production system around it. Teams watch the input data, predictions, service
health, and response path. They ask whether the model still behaves well after
deployment and whether the right team knows when to investigate.

The DataTalks.Club interviews treat model monitoring as part of
[MLOps]({{ '/wiki/mlops/' | relative_url }}), not as a dashboard bolted onto
the end of a project. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) starts with
production monitoring around 25:04 and connects it to upstream
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) around 27:35.
That framing matters because a model can degrade when the model artifact is
unchanged but the data, features, labels, or serving path changed.

## Common Definition

Across the podcast discussions, model monitoring means tracking production
signals that tell a team whether a model still works for its intended use.
Teams usually track input distributions and prediction distributions. They
also track service errors, latency, and business outcomes. They may track user
or stakeholder feedback too. The common definition also includes the ability to
diagnose a problem after an alert fires.

[Thom Ives]({{ '/people/thomives/' | relative_url }}) gives the data-science
version in
[Feature Engineering and Model Monitoring]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}).
Around 47:30, he separates data drift from concept drift and ties both to
ongoing maintenance. His point is practical: the training data may stop
matching the current world, or the relationship between features and outcomes
may change.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) gives the
human-centered version in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Around 29:23, she discusses live test sets and small A/B tests for detecting
model issues. Around 46:28, she focuses on input distributions, unit changes,
and feature drift. Around 49:28, she adds logging, feature stores, and
reproducibility. Her version makes monitoring useful only when teams can debug
and respond.

## Guest Differences

Guests agree that production models need monitoring, but they start from
different problems. Danny Leybzon starts from production pain. Around
28:59 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he distinguishes teams that already have production models from teams still
before deployment. Around 30:39, he says the market conversation shifts from
why monitoring matters to how teams should monitor.

Lina Weichbrodt starts from people and incident response. Around 24:34 in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
she discusses service levels and impact assessment with stakeholders. Around
27:14, she connects ML incidents to post-mortems and recovery steps. Her
monitoring system needs a human response path, not only metrics.

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) starts
from standardization. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she names monitoring as part of the minimum MLOps stack around 18:41. Around
42:53, she discusses monitoring standardization as a roadmap priority. She
also warns that monitoring may need to fit existing observability tools rather
than forcing a separate ML-only stack.

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) starts
from adoption. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
he frames the core challenge around 1:01:58 as keeping models deployed,
monitored, and maintained. Around 48:41, he recommends solving tangible pain
points first. Around 51:21, he places monitoring alongside experiment tracking,
registries, and serving in the MLOps toolset.

## Data Drift

Data drift covers changes in the input data a model receives after deployment.
The model may still run, but the feature values no longer look like the
training data. Thom Ives discusses this directly around 47:30 in
[Feature Engineering and Model Monitoring]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}).
The same episode links monitoring to feature work and ETL reliability. It also
connects monitoring to
[data governance]({{ '/wiki/data-governance/' | relative_url }}).

Danny Leybzon gives the production operations version. Around 27:35 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he connects observability to ETL and data pipelines. He also connects it to
upstream root causes.

That link is why model monitoring and
[data observability]({{ '/wiki/data-observability/' | relative_url }}) overlap.
The model team needs model-specific signals, but many failures start in
upstream freshness or schema changes. Volume and distribution changes can
break the model too.

[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) gives the broader data
observability view in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
Around 13:40, she discusses silent data incidents and model drift. Around
16:38, she describes freshness, volume, and distribution. She also includes
schema and lineage. For model monitoring, those signals help explain whether
drift came from the data system or from model behavior.

## Model Performance

Model performance monitoring tracks whether predictions still match the task.
For some systems, teams can compare predictions with labels after a delay. For
others, teams watch proxy metrics and human review. Customer complaints,
business KPIs, or small experiments may provide earlier signals.

Lina Weichbrodt's discussion is useful here because she ties monitoring to
real response paths. Around 29:23 in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
she covers live test sets and small A/B tests. Around 36:41, she adds user
feedback channels and internal bug reports. Around 38:20, she discusses
prioritizing widespread user complaints. Those signals matter when labels are
late or incomplete.

Thom Ives adds the maintenance view. Around 45:53 in
[Feature Engineering and Model Monitoring]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}),
he discusses model selection and accuracy. He also covers variance and
generalizability. Around 47:30, he moves from selecting a model to maintaining
it. A model can be good at release and still become the wrong model later.

## Observability

Monitoring detects that something may be wrong, and observability helps a team
explain why. Danny Leybzon makes this distinction concrete through profiles,
pipelines, and integrations. Around 31:50 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he discusses data profiling architecture with WhyLogs and a backend for storing
profiles. Around 36:47, he discusses platform-agnostic integrations because
production models run through many serving tools.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
connects observability to platform design in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Around 54:15, he discusses API design and unified prediction schemas for
logging requests, predictions, and responses. That schema gives teams material
for later monitoring and analysis.

This is where [machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
and [ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}) matter. A model
service needs to log the right inputs and outputs before a team can diagnose
drift alerts, latency spikes, or bad prediction clusters.

## Alerts

Alerts make monitoring operational because they name a team, a severity, and a
next action. Barr Moses discusses this from the data side around 1:00:27 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}):
teams need contextual alerts and fewer false positives. Around 41:03, she
connects alerts to runbooks and remediation.

Model alerts have the same problem. If every distribution shift pages a team,
people stop trusting the monitoring system. Lina Weichbrodt's incident-response
chapters add the human test. Around 39:26 in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
she discusses post-mortem evidence and investigation steps. Around 42:03, she
turns post-mortems into action items and process changes.

The practical rule from the interviews is to alert on signals that someone can
act on. For model teams, those signals usually include input quality and
prediction distribution. They also include service health and label-backed
performance. They may include business impact or a stakeholder complaint path
too.

## Ownership

Model monitoring fails when no one owns the response. The owning team may be a
product team, an ML engineering team, a central MLOps team, or a data platform
team. The right owner depends on the failure mode.

Maria Vechtomova describes a central MLOps team around 12:42 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
That team provides infrastructure, reusable CI/CD, and monitoring support. But
the product or feature team still needs to understand the model and its users.

Raphaël Hoogvliets gives a similar adoption model around 23:01 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
The MLOps team acts as an enabling platform team. Around 25:20, he describes
supporting product teams and ML engineers. Monitoring belongs in that shared
ownership boundary: the platform can provide the tools, but the model owner
must interpret the business impact.

Lina Weichbrodt adds stakeholder ownership. Around 18:29 in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
she turns stakeholder concerns into mitigations and metrics. Around 24:34, she
uses service levels and impact assessment to decide what kind of incident
response a model needs.

## MLOps and Platforms

Model monitoring is one layer of the larger MLOps system. A team needs
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and a
[model registry]({{ '/wiki/model-registry/' | relative_url }}) to know which
model version is running. A team needs
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) when it has to
recreate training conditions. Alerts also need
[production]({{ '/wiki/production/' | relative_url }}) practices for
deployment, rollback, and incident response.

Simon Stiebellehner covers that platform sequence in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Around 29:41, he discusses experiment tracking. Around 30:32, he discusses
model registries. Around 31:15 and 31:51, he covers batch inference, online
serving, and orchestration.

Around 42:48, he adds metadata and lineage, and monitoring uses those pieces
after release.

Maria Vechtomova makes the stack boundary explicit around 18:41 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
She places version control, CI/CD, and registries in one stack. Model registry,
deployment, and monitoring belong in that same stack. Her roadmap discussion
around 42:53 also shows why standardizing monitoring can come after teams have
already solved earlier deployment and reproducibility problems.

## Related Pages

Use these pages for adjacent MLOps, platform, and observability concepts.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
