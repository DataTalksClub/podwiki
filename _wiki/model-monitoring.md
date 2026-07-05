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
  - Sensor ML Personal Baselines
---

Model monitoring is the practice of watching a deployed model and the
production system around it. Teams track input data, predictions, service
health, and response paths. Those signals show whether the model still behaves
well after deployment and whether the right team knows when to investigate.

Model monitoring is part of [[MLOps]], not a dashboard bolted onto the
end of a project. Production monitoring connects to upstream
[[data pipelines]] because a model can degrade even when the model artifact
is unchanged. The data or serving path may have changed instead. Feature values
and labels may have changed too.[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]
For the boundary with pipeline reliability, see
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]].

## Production Signals

Model monitoring starts with production signals that tell a team whether a
model still works for its intended use. Teams usually track input distributions
and prediction distributions. They also track service errors, latency, and
business outcomes. They may track user or stakeholder feedback too. The
monitoring system needs to help the team diagnose a problem after an alert
fires.

Data drift and concept drift describe different production failures. The
training data may stop matching the current world while feature-outcome
relationships change.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]

Live test sets and small A/B tests can detect model issues. Teams watch input
distributions, unit changes, and feature drift. Logging, feature stores, and
reproducibility support the response path.[[cite:human-centered-mlops-and-model-monitoring@29:23=>Human-Centered MLOps and Model Monitoring]][[cite:human-centered-mlops-and-model-monitoring@46:28=>Human-Centered MLOps and Model Monitoring]].
Monitoring is useful only when teams can debug and respond.

In [[manufacturing-predictive-maintenance-yield-analytics=>fab maintenance and yield analytics]],
the monitored production signal is tied to tool state, wafer exposure, and qual
timing rather than only prediction drift. The useful alert tells engineers
whether to run a check earlier or keep watching the tool
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

## Monitoring Priorities

Production models need monitoring, but the operating problem changes by team
stage. Teams that already have production models face a different problem from
teams still before deployment. The question shifts from why monitoring matters
to how teams should monitor.[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]

Service levels and impact assessment belong with stakeholders because model
incidents affect people outside the model team. ML incidents connect to
post-mortems, Five Whys, and recovery steps.[[cite:human-centered-mlops-and-model-monitoring@24:34=>Human-Centered MLOps and Model Monitoring]][[cite:human-centered-mlops-and-model-monitoring@27:14=>Human-Centered MLOps and Model Monitoring]].
Monitoring needs a human response path, not only metrics.

The post-mortem is also a debugging format. Weichbrodt uses Five Whys to move
from a bad recommendation or credit-scoring surprise toward input features,
business rules, and action items. The response path should create tickets or
process changes after the diagnosis, not stop at the incident note
[[cite:human-centered-mlops-and-model-monitoring@32:11=>Human-Centered MLOps]]
[[cite:human-centered-mlops-and-model-monitoring@39:26=>Human-Centered MLOps]].

Monitoring can be part of the minimum MLOps stack and a roadmap priority. It
may need to fit existing observability tools rather than force a separate
ML-only stack.[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

Adoption work starts with tangible pain points. Keeping deployed models
monitored and maintained sits alongside experiment tracking, registries, and
serving in the MLOps toolset.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

For startup validation, Evidently began with customer discovery around
post-production model failures. Elena Samuylova heard the same complaints from
teams in traditional companies. Models break without anyone noticing,
monitoring is annoying to own, and monitoring may disappear when data
scientists leave a project
[[cite:building-mlops-startup@43:59=>MLOps Startup]].
Evidently treated monitoring as both an [[MLOps]] operating practice and a
product pain for an MLOps startup.

## Data Drift

Data drift changes the inputs a model receives after deployment. A model can
still run on drifted feature values.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]
The same monitoring problem links feature work, ETL reliability, and
[[data governance]].

In production operations, observability connects model symptoms to ETL,
[[data pipelines]], and upstream root causes.[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]

Monitoring is also a retraining input. Drift signals can trigger retraining
decisions, and fairness, anomaly, and robustness signals can too.

Theofilos Papapanagiotou separates this from ordinary service monitoring
because latency and request counts are only part of the picture. An
[[MLOps Roadmap]] has to treat monitoring as runtime observability and pipeline
control. The same stack watches model quality signals that may kick off
retraining
[[cite:mlops-kubeflow-model-monitoring@11:17=>Kubeflow Model Monitoring]].
The monitoring output can become new training data when the team has a
production feedback path
[[cite:mlops-kubeflow-model-monitoring@33:27=>Kubeflow Model Monitoring]].

Fairness-aware monitoring adds subgroup behavior to that drift view. Supreet
Kaur connects post-launch bias checks to demographic composition, feedback
loops, overfitting, and basic statistics. KS-style drift tests can belong in the
same review. A model can look stable in aggregate while a population slice
changes or a feedback channel starts collecting biased examples
[[cite:responsible-explainable-ai-bias-detection@37:31=>Responsible and Explainable AI]].

Accuracy-only monitoring can hide that problem. In the event-recommendation
example, a model could become more accurate for the people it keeps serving
while excluding people who would also benefit. The monitoring plan therefore
needs population checks and sample-size checks. It also needs a human review
path for distribution alarms, not only precision, recall, or service metrics
[[cite:responsible-explainable-ai-bias-detection@37:31=>Responsible and Explainable AI]].

That connection puts model monitoring close to
[[data-quality-and-observability=>data observability]].
The model team needs model-specific signals, but many failures start in
upstream freshness or schema changes. Volume and distribution changes can
break the model too.

Deployment population is part of the monitored distribution. A healthcare model
developed on European patients may not generalize to African clinical settings.
Disease prevalence, available measurements, collection practices, and
infrastructure can differ. Eleni Stamatelou treats European data as potentially
useful for reasoning, but not enough to justify an algorithm for a low-resource
setting
[[cite:building-healthcare-machine-learning-systems@35:45=>Healthcare ML Systems]].

That makes population coverage a [[Machine Learning System Design]] constraint
as well as a [[data-quality-and-observability=>data observability]] signal.
For [[healthcare-ml-validation-and-adoption=>healthcare ML validation]], the
monitoring plan needs population slices and clinical-site context rather than a
single aggregate drift alert. In low-resource clinical deployment, the same
monitoring question includes missing metrics and local collection limits. A
stable distribution from the original site doesn't prove the system is safe for
a hospital with a different disease mix, connectivity, or measurement setup.

Silent data incidents and model drift can share the same root cause. Freshness,
volume, and distribution help track data reliability.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]
Schema and lineage add context for root-cause analysis. For model monitoring,
those signals help explain whether drift came from the data system or from
model behavior.

Context matters because an anomaly isn't always bad data. A useful monitoring
system reduces false positives by learning which deviations are expected and
which ones need investigation
[[cite:data-quality-data-observability-data-reliability@1:00:27=>Data Observability Explained]].
For baseline-heavy sensor products, the same rule applies inside the model.
[[Sensor ML Personal Baselines]] shows why an alert can be wrong when a system
ignores routine changes, device placement, aging, or missing sensor history.

## Model Performance

Model performance monitoring tracks whether predictions still match the task.
For some systems, teams can compare predictions with labels after a delay. For
others, teams watch proxy metrics and human review. Customer complaints,
business KPIs, or small experiments may provide earlier signals.

Real response paths include live test sets and small [[a-b-testing=>A/B tests]].
They also include user feedback channels and internal bug reports. Widespread
user complaints can serve as signals too.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]]
Those signals matter when labels are late or incomplete.
When labels come from people or model-assisted review,
[[annotation-quality-workflows=>annotation quality workflows]] determines
whether the performance signal is trustworthy enough to trigger action.

A live test set works only if the team can later reconstruct what the model saw.
Locking and logging the arrived features connects monitoring to
[[feature-stores=>feature stores]] and [[Reproducibility]]
[[cite:human-centered-mlops-and-model-monitoring@29:23=>Human-Centered MLOps]].

Before release, teams still care about model selection and accuracy. Variance
and generalizability matter too. After release teams maintain the
model.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Model Monitoring]]
A model can be good at release and still become the wrong model later.

## Observability

Monitoring detects that something may be wrong, and observability helps a team
explain why. Barr Moses makes the same split for data systems: monitoring can
show a freshness problem, while observability traces the root cause. It also
shows downstream impact and recovery priority
[[cite:data-quality-data-observability-data-reliability@24:31=>Data Observability Explained]].
For that boundary, use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
to separate model-specific drift signals from upstream data freshness and
lineage work.

The profiling side of [[MLOps Tools]] can use WhyLogs and a backend for storing
profiles. Platform-agnostic integrations matter because production models run
through many serving tools.[[cite:mlops-model-monitoring-data-observability@31:50=>MLOps Architect Guide]]
Teams can split open-source profiling from managed observability at the tool
boundary.
WhyLogs creates portable profiles for open-source profiling. WhyLabs adds hosted
monitoring, visualization, alerting, and longer-term operations
[[cite:mlops-model-monitoring-data-observability@55:50=>MLOps Architect Guide]].

Observability connects to platform design through API design and unified
prediction schemas. Teams use those schemas to log requests, predictions, and
responses
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
The schema gives teams material for later monitoring and analysis before a
dashboard exists. It should preserve request context and prediction output. It
should also preserve response data, model version, and owner context for later
investigations.

The platform doesn't have to own every product API structure. It may need a
shared logging schema when teams want monitoring and analytics across many
models.

Churn prediction and lead scoring services become easier to compare when their
request, response, and prediction logs follow the same structure
[[cite:building-production-ml-platform-and-mlops-team@54:15=>Building Production ML Platforms]].

Without that consistent structure, fairness reviews, product analytics, and
incident response have to reconstruct what the serving path failed to record
[[cite:building-production-ml-platform-and-mlops-team@54:15=>Building Production ML Platforms]].

Teams also have to use the schema to say what not to log. In regulated settings,
platform teams need request and prediction data for debugging. They also need
response data, model version, and owner context. They still need to avoid
copying governed source data into every log stream or run artifact.

Simon Stiebellehner describes fintech platform work where GDPR and compliance
constraints shaped metadata and lineage. The team used the same constraints for
logging and artifact storage
[[cite:building-production-ml-platform-and-mlops-team@39:54=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@45:50=>Building Production ML Platforms]].

This is where [[machine learning infrastructure]]
and [[ML platforms]] matter. A model
service needs to log the right inputs and outputs before a team can diagnose
drift alerts, latency spikes, or bad prediction clusters.

## Alerts

Alerts make monitoring operational because they name a team, a severity, and a
next action. From the data side, teams need contextual alerts and fewer false
positives, and alerts connect to runbooks and remediation
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Sabina Firtala's domestic-risk assessment episode adds the high-stakes version
of the same rule. After a risk-scoring tool enters frontline workflows,
monitoring has to watch for drift and trigger maintenance alerts. The response
path still needs human review because the served population may change after
release. Source data and operational workflows can change too
[[cite:building-domestic-risk-assessment-tool@42:20=>Building a Domestic Risk Assessment Tool]].
That review path needs the same label discipline as
[[annotation-quality-workflows=>annotation quality workflows]] when monitoring
findings become future evaluation data.

Model alerts have the same problem. If every distribution shift pages a team,
people stop trusting the monitoring system. The incident-response view adds a
human test. Post-mortem evidence and investigation steps become action items and
workflow changes
[[cite:human-centered-mlops-and-model-monitoring@32:11=>Human-Centered MLOps and Model Monitoring]][[cite:human-centered-mlops-and-model-monitoring@39:26=>Human-Centered MLOps and Model Monitoring]].

Teams should alert on signals that someone can act on. For model teams, those
signals usually include input quality and prediction distribution. They also
include service health and label-backed performance. They may include business
impact or a stakeholder complaint path too.

## Ownership

Model monitoring fails when no one owns the response. The owning team may be a
product team, an ML engineering team, a central MLOps team, or a data platform
team. The right owner depends on the failure mode.

A central MLOps team can provide monitoring
support.[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]
It may also provide infrastructure and reusable CI/CD.
But the product or feature team still needs to understand the model and its
users.

An MLOps team can support product teams and ML
engineers.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
It can act as an enabling platform team.
Monitoring belongs in that shared ownership boundary: the platform can provide
the tools, but the model owner must interpret the business impact.

Stakeholder ownership turns stakeholder concerns into mitigations and metrics.
Teams use service levels and impact assessment to decide what kind of incident
response a model needs
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps and Model Monitoring]].

## MLOps and Platforms

Model monitoring is one layer of the larger MLOps system. A team needs
[[experiment tracking]] and a
[[model registry]] to know which
model version is running. A team needs
[[reproducibility]] when it has to
recreate training conditions. Alerts also need
[[production]] practices for
deployment, rollback, and incident response.

Platform work can start with experiment tracking and model registries, then
move through batch inference and online serving. Orchestration, metadata, and
lineage come next.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Monitoring uses those pieces after release.

Teams can't design monitoring last. The registry supplies model identity, and
serving supplies request and prediction logs. The platform schema determines
whether later dashboards can join those records reliably
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

The same MLOps stack can cover version control and CI/CD. It can also cover
registries, deployment, and monitoring.[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]
Standardizing monitoring can come after teams have already solved earlier
deployment and reproducibility problems.

## Related Pages

These pages connect monitoring to the surrounding MLOps system.

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
