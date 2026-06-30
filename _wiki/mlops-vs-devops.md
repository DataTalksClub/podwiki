---
layout: wiki
title: "MLOps vs DevOps"
summary: "A podcast-backed comparison of DevOps and MLOps operating models."
related:
  - MLOps
  - Software Engineering
  - Platform Engineering
  - Production
  - Model Monitoring
  - Reproducibility
---

MLOps and DevOps are related operating models. The DataTalks.Club archive
treats [MLOps]({{ '/wiki/mlops/' | relative_url }}) as an extension of
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}).
It also extends [platform engineering]({{ '/wiki/platform-engineering/' | relative_url }})
and [production]({{ '/wiki/production/' | relative_url }}) practices into
systems that depend on data and model artifacts.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
defines MLOps through people, process, and technology around 4:42. Around
8:11-13:50, he ties the platform skill set to cloud infrastructure and software
engineering fundamentals. He also names Kubernetes and Terraform.

The two models control different objects. DevOps focuses on software services
and releases, while MLOps adds the model lifecycle around training data and
evaluation. It also adds registries, drift, retraining, and governance.

[Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }})
draws that boundary directly in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }})
around 7:28-13:04. He contrasts DevOps with model lifecycle and data drift.
The same discussion covers fairness, inference monitoring, and retraining
triggers.

## Link Map

This comparison links adjacent operating models:

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) for model training, artifacts, serving, monitoring, retraining, and governance.
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}) and [Production]({{ '/wiki/production/' | relative_url }}) for the engineering base that MLOps borrows from.
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}), [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}), and [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}) for self-service environments, deployment paths, and shared infrastructure.
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}), and [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) for the handoff from code and experiments to deployable artifacts.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), [Data Observability]({{ '/wiki/data-observability/' | relative_url }}), and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for the data and production signals that explain many model failures.
- [Software Engineer to Machine Learning]({{ '/wiki/software-engineer-to-machine-learning/' | relative_url }}) and [MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) for role transitions where DevOps, SRE, backend, and platform skills become ML-system skills.

These podcast routes support most of the comparison:

- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}) with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}).
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}) with [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}).
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}) with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}).
- [Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}) with [Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }}).
- [MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}) with [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}).
- [DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}) with [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}).

## Comparison Definition

DevOps runs reliable software delivery through version control, builds, and
deployment automation.
The archive usually reaches DevOps through software and data-production
conversations, rather than a standalone DevOps episode.
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
connects the data-side version to deployment culture, automation,
observability, and CI/CD in
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
around 13:27-15:52 and 30:55-42:39.

MLOps is the operating model for reliable machine learning delivery. It includes
the DevOps base, but the release candidate is no longer just code. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
places CI, repository structure, and testing in one operating system around
39:06-56:50. Raphaël also covers package registries, containers,
serving, and monitoring.

The overlap is large because production ML still needs deployable software.
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) argues in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
around 16:27-20:49 that teams should reuse existing infrastructure. Her list
includes Kubernetes, Git, registries, and monitoring.
That's why [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
and [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
should be read as additions to the engineering base, not replacements for it.

## Common Decision Rule

Use DevOps framing when the failure mode is mostly software delivery. The
service doesn't build, deploy, scale, or expose logs. That framing
fits the deployment automation, observability, CI/CD, and recovery practices
Bergh describes for data teams in
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
around 30:55-54:05.

Use MLOps framing when the failure mode depends on learned behavior. A model
can't be reproduced, or a training run can't be explained. A feature changed,
a prediction distribution drifted, or retraining has no owner. That framing matches
Stiebellehner's platform sequence from self-service compute to
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[model registries]({{ '/wiki/model-registry/' | relative_url }}), serving, and
orchestration. It also covers metadata, lineage, governance, and unified
prediction logging in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
around 28:20-54:15.

Most production ML systems need both. The practical rule from the MLOps guests
is simple: keep DevOps for the software delivery path. Add MLOps where data and
model artifacts create new lifecycle risk.

Vechtomova's central-team model around
12:42-18:41 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
and Hoogvliets's enabling-platform model around 23:01-27:56 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
both follow that rule.

## Operating Model Overlap

MLOps borrows the delivery mechanics of DevOps. Git, tests, CI/CD, and
monitoring appear as basic MLOps ingredients.
Vechtomova covers that stack around 16:27-20:49 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
and in Hoogvliets's core-practices discussion around 39:06-56:50 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

The shared organization model is enablement. A central platform or MLOps team
provides paved paths, templates, permissions, and monitoring support. Product
or ML teams keep domain ownership.
Vechtomova discusses centralized MLOps responsibilities, reusable CI/CD,
standard repositories, and DevOps buy-in around 12:42 and 29:55-38:01 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

Hoogvliets gives the scale version around 23:01-36:55 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
by framing the MLOps group as an enabling platform team. That team gathers pain
points, improves developer experience, and measures adoption.

The shared culture is production responsibility. Bergh's data-engineering
discussion around 13:27 and 23:56 in
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
contrasts fear-based deployment with staged production operations.
Papapanagiotou makes the same shift for ML around 16:37-20:08 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }})
by describing MLOps as a cross-functional practice. It spans developer,
operator, and product responsibilities rather than only a job title.

## MLOps Additions

MLOps adds artifact lineage because the deployed thing comes from code and
data. Hoogvliets links reproducibility to data versioning,
traceability, and experiment capture around
42:31-44:22 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Stiebellehner extends the same concern to metadata and lineage around
42:48-45:50 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

Model-specific monitoring matters because a healthy service can still serve bad
predictions. Papapanagiotou names drift and fairness around 11:17-14:44 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}).
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) connects
production model monitoring to upstream ETL and data pipelines around
25:04-31:50 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
That makes [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
and [data observability]({{ '/wiki/data-observability/' | relative_url }})
adjacent operating concerns.

MLOps also covers the handoff from exploration to production. Stiebellehner
starts with notebooks around 10:47 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He then moves through self-service compute and experiment tracking around
21:03-31:51 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Vechtomova makes the same handoff practical around 33:24 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
by moving notebook logic into packages and CI/CD. That connects this page to
[Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }}).

MLOps adds model governance when systems affect regulated or high-risk
decisions. In Stiebellehner's fintech examples around 39:54-45:50 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
he connects security, compliance, metadata, and lineage. He also covers GDPR
and dataset storage.
Those concerns sit beside [reproducibility]({{ '/wiki/reproducibility/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}), and
[governance]({{ '/wiki/governance/' | relative_url }}) rather than inside a
generic deployment checklist.

## Guest Differences

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) gives the
most pragmatic DevOps-overlap view. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she warns against tool overload around 14:45 and recommends existing
infrastructure around 16:27. She treats DevOps buy-in and standards as part of
MLOps implementation around 35:21-38:01.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
gives the platform-design view. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he emphasizes user-centric platform design, team composition, and build-vs-buy
decisions around 10:47-17:14. He then covers self-service compute, experiment
tracking, and serving modes around 28:20-54:15.

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) gives
the adoption and scale view. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
he stresses collaboration and enabling-team support around 14:05-16:58. He
then connects developer experience, deployment frequency, impact tracking,
and reproducibility around 23:01-1:01:58.

[Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }})
gives the systems-engineer view. In
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
he centers the difference on lifecycle automation and drift around 7:28-15:29.
His maturity section adds automated retraining and
Kubeflow pipelines around 27:01-46:58.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) gives the
monitoring and architecture view. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he starts from production model monitoring around 25:04. He then moves into ETL
root causes, data profiling, and platform-agnostic integrations around
27:35-39:10.

## Practical Boundary Questions

Check versioned objects by asking what must be recreated. If the answer is only
code and dependencies, the work is mostly DevOps. If the answer includes data
snapshots, training runs, and
model artifacts, the work needs MLOps practices such as
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and a
[model registry]({{ '/wiki/model-registry/' | relative_url }}). Hoogvliets
draws this expanded reproducibility boundary around 42:31 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
and Papapanagiotou links it to metadata and traceability around 46:58 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}).

Check monitored signals by asking what can fail silently. If uptime and logs
are enough, the monitoring problem is mostly DevOps. If the team also needs input
distributions, prediction distributions, and retraining triggers,
the monitoring problem is MLOps. Papapanagiotou discusses drift and retraining
around 11:17 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
while Leybzon connects model monitoring to upstream data-pipeline diagnosis
around 27:35 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).

Check response ownership by asking who can fix the incident. If a platform
team can fix it without model interpretation, the response path is mostly
DevOps. If the alert requires a product owner or ML engineer, the response
path needs MLOps ownership. This matches Vechtomova's centralized
MLOps guardrails around 27:06 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
and Hoogvliets's support model around 25:20 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

Check repeat work by counting repeated handoffs. A single model can often start
with lightweight DevOps and minimal MLOps pieces. Teams need shared MLOps
infrastructure when they repeat model deployment. Stiebellehner discusses
build-vs-buy and platform triggers around 16:52-20:04 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Vechtomova describes startup first steps around reproducibility around 24:01 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

## Practical Starting Point

Start with the DevOps base that the MLOps guests reuse. Use version control,
tests, CI/CD, and observability.
Vechtomova names those as pragmatic starting pieces around 16:27-20:49 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
Hoogvliets prioritizes CI/CD and tangible pain points around 48:41 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

Add ML lifecycle controls where the model creates operational risk. Start with
experiment tracking, artifact storage, and reproducible training. Then add
serving, prediction logging, model monitoring, and retraining decisions.
Stiebellehner's platform walkthrough around 29:41-42:48 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
and Papapanagiotou's maturity discussion around 27:01-33:27 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }})
provide the archive-backed sequence.

Keep the boundary explicit in team design. A central MLOps or platform team
can build paved paths. Product teams still need to understand the model.
Hoogvliets's enabling-platform discussion around
23:01-36:55 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
supports shared ownership. Vechtomova's guardrails around 27:06 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
support the same boundary.

## Related Pages

Continue through these connected wiki and article pages:

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }})
- [Software Engineer to Machine Learning]({{ '/wiki/software-engineer-to-machine-learning/' | relative_url }})
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
