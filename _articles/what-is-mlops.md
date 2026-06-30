---
layout: article
title: "What Is MLOps? A Practical Definition from Production ML Work"
keyword: "what is mlops"
secondary_keywords:
  - mlops
summary: "MLOps is the practice of turning machine learning models into reproducible, monitored, governed production systems."
related_wiki:
  - MLOps
  - MLOps Roadmap
  - Model Monitoring
  - Machine Learning System Design
  - Reproducibility
  - DataOps
---

MLOps is the operating discipline for machine learning after a model leaves the
notebook. It gives teams a repeatable path from experiment to production. That
path includes training-run tracking, model packaging, and deployment. It also
includes monitoring, incident response, retraining, and rollback.

That definition comes up across DataTalks.Club production ML interviews. In
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
[Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }})
defines MLOps around culture, operating habits, and technology. He then
separates it from plain DevOps through model lifecycle and data drift. He also
covers fairness monitoring and retraining triggers.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
uses the same people-process-technology framing and turns it into platform
building blocks. His platform blocks include experiment tracking, model
registries, batch serving, and online serving. He also covers orchestration,
metadata, and lineage. Governance and prediction logging appear there too.

For the full archive-backed reference page, see
[MLOps]({{ '/wiki/mlops/' | relative_url }}). If machine learning builds the
model, MLOps keeps it reproducible and deployable. It also keeps it observable
and owned.

## Core Scope

MLOps starts with reproducibility because one useful training metric isn't
enough for production. A team needs to recover the code and environment behind
that run. The same record needs parameters and a data reference, plus metrics
and the artifact.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
connects CI, repository structure, and testing to the practical work of keeping
models deployed. He also covers data versioning, traceability, and experiment
capture. Those concerns map directly to
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}),
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}), and
[model registries]({{ '/wiki/model-registry/' | relative_url }}).

MLOps also covers deployment paths. A model may run as a batch scoring job, an
online API, a feature pipeline, or a managed endpoint. It may also run as an
embedded component in a larger product.

Simon Stiebellehner separates batch inference from online
serving around the middle of
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
and then ties both to orchestration and platform design.

In
[Machine Learning System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }})
adds the design side. Fraud detection, recommendation, and ranking systems need
metrics and baselines. They also need A/B tests, monitoring, fallbacks, and
serving assumptions. Teams need those choices before they can choose a model
architecture. That's where
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and MLOps meet.

Monitoring is the part most people notice after deployment. In
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
Theofilos discusses drift and fairness alongside inference monitoring and
retraining triggers.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) goes deeper in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}):
model monitoring has to include upstream ETL and data pipelines. A model can
fail when features or schemas change. Labels and source systems can change too.
That's why [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
often overlaps with
[data observability]({{ '/wiki/data-observability/' | relative_url }}) and
[data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

After deployment, MLOps assigns ownership through response paths. In
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) connects
model operations to stakeholder trust, service levels, and post-mortems. She
also covers user feedback and recovery steps. A dashboard isn't enough if no team knows which
alert matters, who investigates it, and what action follows.

## Purpose

Traditional software delivery already has version control, tests, and CI/CD. It
also has deployment automation, logs, and incident response. MLOps keeps those
practices and adds the parts that are specific to learned systems. Those parts include
training data, features, labels, and metrics. They also include model artifacts,
drift, and retraining decisions.

Theofilos Papapanagiotou makes the DevOps boundary visible in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}).
A normal service can be healthy while the model inside it quietly becomes less
useful because the world changed. That's why an MLOps release candidate isn't
only code. It includes data assumptions and a trained artifact. It also
includes validation evidence, a deployment target, and a monitoring plan.

MLOps also isn't only a tool category. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) warns
against chasing the whole tool landscape.

Her practical stack starts with existing engineering primitives such as Git and
CI/CD. Registries, reusable repositories, and code quality belong in that base.
So do testing, documentation, and monitoring.

Kubernetes fits when the organization already uses it. The mature move is to
standardize the path to production, not to buy every product labeled MLOps. For
tool selection, see
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}).

## Adoption Signals

A team needs MLOps when model work starts affecting a real product or business
decision.

The early signs are concrete:

- another person can't reproduce the training run.
- the model artifact has no clear owner or approval history.
- deployment depends on manual notebook steps.
- no one knows which model version is serving predictions.
- input data, prediction distributions, or labels can change without alerting
  the team.
- retraining, rollback, and incident response are informal.

The archive shows several versions of this threshold. In
[CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}), teams start with
business understanding and end with deployment, evaluation, and feedback.
That conversation isn't a modern MLOps tooling guide. It still explains the
same boundary: a useful model has to support a measured business objective
after release.

In
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
the shift from dashboards and ad hoc analysis to ML systems with APIs,
predictions, and SLAs. He also covers experiments, A/B testing, and
shadow-mode evaluation. That
shift is usually when informal data science work needs a production operating
model.

## Healthy Practice

Good MLOps gives data scientists and ML engineers a repeatable path without
removing judgment. Maria Vechtomova's episode is especially useful here because
she describes central MLOps teams as enablement teams. They provide
infrastructure, reusable CI/CD, and repository templates. They also provide
permissions and monitoring support. Product teams keep domain ownership.

Raphaël Hoogvliets gives the scale version in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
His MLOps team collects pain points and improves developer experience. It also
measures deployment frequency and impact. The team prioritizes quick wins
before adding more platform weight.

That sequence matches the
[MLOps roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}): start with
reproducible experiments and a simple deployment path, then add registries and
monitoring when repeated work justifies them. Governance and platform pieces
come later.

The amount of operating discipline depends on the risk. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
ties ML engineering in finance to CI/CD and dev/test/prod separation. He also
covers approvals and legacy systems. Monitoring, model governance, and interim
registries matter there too.

The same person argues for a lighter approach in startup contexts elsewhere in
the archive. MLOps should match the model's failure cost and regulatory
pressure. It should also match the team size.

## MLOps vs DataOps

MLOps and DataOps overlap, but they shouldn't be merged into one vague topic.
[DataOps]({{ '/wiki/dataops/' | relative_url }}) focuses on reliable data
delivery. It covers pipelines, orchestration, and data quality. It also covers
observability, deployment automation, and collaboration around analytical data
products.

MLOps focuses on machine learning systems through experiment tracking, trained
artifacts, and model registries. It also covers serving, monitoring,
retraining, and governance.

They meet because production models depend on production data. Danny Leybzon's
monitoring discussion in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
is the clearest example. An apparent model problem may start in ETL, schemas,
freshness, or feature generation.

The practical split is simple: use DataOps to make data pipelines trustworthy.
Use MLOps to make model behavior reproducible, deployed, monitored, and owned.

## Learning Path

Start by building one small model all the way through production-style
operations. Track the experiment and save the artifact. Package inference code,
create a repeatable deploy step, and log predictions. Then monitor inputs and
outputs, and write down what would trigger rollback or retraining. You learn
more from this project than from a disconnected tour of tools because it forces
the same handoffs that the podcast guests discuss.

Then add complexity deliberately with the
[MLOps roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) when you need a
learning sequence. Use
[MLOps vs DevOps]({{ '/wiki/mlops-vs-devops/' | relative_url }}) when you're
coming from software or platform engineering. Use
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
when you need to connect model operations to requirements and metrics. It also
helps with serving, fallbacks, and product validation.
