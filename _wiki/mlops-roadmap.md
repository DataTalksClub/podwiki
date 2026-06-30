---
layout: wiki
title: "MLOps Roadmap"
summary: "A podcast-backed roadmap for MLOps: reproducible experiments, deployment paths, model registries, monitoring, platform adoption, and role milestones."
related:
  - MLOps
  - ML Platforms
  - Machine Learning Infrastructure
  - Model Registry
  - Experiment Tracking
  - Model Monitoring
  - Reproducibility
  - Production
  - DataOps
---

An MLOps roadmap starts when a practitioner can train a model. It ends when a
team can reproduce and operate that model in production. In the DataTalks.Club
archive, that path isn't a vendor-stack checklist. It's an operating discipline
that combines people, process, and technology, as
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
defines around 4:42 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

Use this page for the learning and project sequence. Use
[MLOps]({{ '/wiki/mlops/' | relative_url }}) for the reference concept,
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) for shared internal
platforms, and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for the separate
discipline around reliable data pipelines. This roadmap keeps those boundaries
separate. It also shows where production ML depends on data quality, lineage,
and observability.

## Link Map

These wiki pages cover the core roadmap concepts:

- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})

These podcast interviews anchor the roadmap:

- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  with [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
  with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
- [MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
  with [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})
- [Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
  with [Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})
- [MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
  with [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
- [Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }})
  with [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})

## Common Definition

Across the archive, MLOps readiness means a model can move through a repeatable
lifecycle. That lifecycle includes experiment capture and artifact handoff. It
then covers deployment, monitoring, feedback, and retraining or rollback
decisions.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
lays out that lifecycle in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
At 29:41, he covers experiment tracking. Around 30:32, he moves to model
registries. Batch and online serving appear around 31:15-31:51. Metadata,
lineage, and prediction logging appear between 42:48 and 54:15.

The archive also treats adoption as part of the roadmap. [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes a central MLOps team as an enabling platform team around 23:01 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

The same episode connects CI, repository structure, parameterization, and
testing between 39:06 and 44:22. It also covers reproducibility. Later it adds
registries, serving, monitoring, and dependency management. It closes that tool
discussion with Docker, Kubernetes, and Databricks tradeoffs between 51:21 and
56:50.

The roadmap is therefore both technical and organizational: a learner builds
the path, and a senior practitioner makes teams use it.

## Guest Tradeoffs

Guests differ most on when to add platform weight. [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
argues for pragmatic standardization in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

She recommends existing infrastructure such as Kubernetes, Git, CI/CD,
and registries before adding more tools. She also includes shared repositories.
Her 18:41 and 22:23 chapters put version control, CI/CD, registries, and model
registry into the essential maturity base. They also include documentation,
reproducibility, code quality, and testing.

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) draws a
different boundary for startups in
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
Around 7:54, he frames lean MLOps as a shoestring strategy. Around 11:54-21:35,
he discusses SaaS-first choices and cloud credits. He also covers migration
friction, lock-in, low-code tradeoffs, and rapid MVP stacks.

In a regulated finance setting, the same guest emphasizes release governance
and approvals. He adds dev/test/prod separation, monitoring, and simple interim
registries around 22:25-35:57 in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).

Monitoring specialists also shift the center of gravity. [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})
starts from production and model monitoring around 25:04 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
then links observability to ETL and upstream data pipelines around 27:35.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) starts from
stakeholder trust and incident response. She covers live test sets,
post-mortems, and data drift in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
between 24:34 and 49:28. She also covers logging and reproducibility. Together
they make monitoring a response system, not just a dashboard.

## Stage 1: Reproducible Experiments

Start by proving that another person can rerun or look at a training result.
Use Git, dependency management, and repeatable environments. Add a data
reference and experiment tracking. Add parameters, metrics, and saved
artifacts. This stage maps directly to
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
frames experiment tracking as an early reproducibility and collaboration win
around 29:41 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) adds
the operating version around 39:06-44:22 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Repository structure, parameterization, and testing keep ML knowledge from
staying on one laptop. Data versioning, traceability, and experiment capture
do the same for run history.

Don't turn this into tool collecting. [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
warns about MLOps landscape overload around 14:45 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
This stage is complete when you can recover the code, environment, and data
reference for a run. You should also recover the parameters, metric, and
artifact.

## Stage 2: Package and Deploy One Model

Next, package one trained model as a batch job or a small API. Add input
validation, prediction logging, and error handling. Add a repeatable release
path and a rollback note. Use the stage to understand the handoff from training
code to prediction code before building a full platform.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
separates batch inference from online serving around 31:15 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He then connects those paths to orchestration around 31:51 and unified
prediction schemas around 54:15.

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) adds the
practical engineering advice around 33:24 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
She recommends moving production logic out of notebooks into packages and
CI/CD.

Keep the infrastructure boring at this stage. [Ben Wilson]({{ '/people/benwilson/' | relative_url }})
argues for maintainability over novelty in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
especially around 6:50-13:19 and 44:23. He contrasts simple, maintainable
solutions with overcomplicated ones. A container, scheduled job, or one managed
serving option is enough if it exposes the release and runtime questions.

## Stage 3: Registry, Monitoring, and Retraining Decisions

After one model can run, add a registry or registry-like convention. Track the
artifact, owner, and training-data reference. Track the evaluation metric,
approval status, deployment target, and rollback path. This stage connects
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}) to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
places model persistence and downstream consumption around 30:32 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) shows the
lighter implementation boundary around 20:49 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
Artifactory, S3, MLflow, or another artifact store can work when teams preserve
traceability and deployment context.

Monitoring should start with actionable signals such as input quality,
prediction distributions, and service errors. Teams should also watch latency
and a business or proxy outcome.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) ties
model monitoring to upstream ETL root causes around 27:35 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) adds live
test sets and small A/B tests. She also adds stakeholder impact, post-mortems,
data drift, and logging around 24:34-49:28 in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Don't automate retraining first. Decide which signal justifies retraining. Then
decide who approves it and how the candidate model is compared with the current
model.

## Stage 4: Turn Repeated Work Into a Platform

Build platform pieces only after multiple projects repeat the same work. Add
repository templates, CI/CD, and deployment paths. Add common logging,
standard prediction schemas, and self-service compute. Add access patterns and
support channels where they remove real friction.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes this adoption path around 23:01-36:55 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
A central team supports product teams, gathers pain points, delivers quick
wins, and measures value through deployment frequency and impact.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) adds
a platform trigger around 16:52-20:04 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Standardization becomes more compelling when repeated deployment, tracking,
serving, or governance problems appear across teams.

This is also where developer experience becomes an MLOps skill. [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
discusses cookie-cutter repositories, service principals, and Databricks
conventions around 29:55-35:21 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
She also covers DevOps buy-in and reusable standards. The platform should help
product teams ship and operate models. It shouldn't
become a detached infrastructure project that ships tools nobody adopts.

## Stage 5: Specialize by Organization Constraint

Choose one constraint and deepen the roadmap instead of trying to master every
MLOps category in one pass.

- Regulated MLOps covers validation, approvals, release governance,
  dev/test/prod separation, monitoring, auditability, and risk controls.
  [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
  covers those finance constraints around 18:52-35:57 in
  [MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).
- Startup MLOps covers minimal stacks, SaaS choices, vendor lock-in,
  portability, technical debt, and rapid MVP delivery.
  [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
  covers this around 7:54-21:35 and 37:54-48:11 in
  [Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
- Platform MLOps covers internal users, templates, CI/CD, serving modes,
  support models, adoption metrics, and governance.
  [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
  and [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
  anchor this path in
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  and [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- Monitoring and observability covers drift, data quality, feature logging,
  incident response, and upstream root causes.
  [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})
  and [Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) anchor
  this path in
  [MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
  and [Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
- Feature-platform MLOps covers online features, training-serving skew,
  materialization and serving, plus validation, registry, and monitoring.
  [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }})
  explains where feature stores matter around 6:30-28:00 and 36:30-52:00 in
  [Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

LLMOps can be a later specialization, but it shouldn't replace the core model
lifecycle. The roadmap still needs reproducible configuration, deployment, and
evaluation. It also needs monitoring, ownership, cost control, and rollback
paths.

## Project Sequence

Build projects in this order, and write a short operating note for each one.
Name who owns the model, what can fail, which signals are monitored, and what
happens after an alert.

1. Tracked training project: include versioned code, environment, data
   reference, metrics, parameters, artifacts and a short reproducibility note.
   This practices the tracking work discussed by
   [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
   around 29:41 and 42:48 in
   [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
2. Batch inference pipeline: include scheduled predictions, input checks,
   prediction output, run history, and a rollback note. This follows the batch
   path
   [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
   separates from online serving around 31:15 in
   [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
3. Online service: include API serving and schema validation. Add model
   artifact lookup, request and response logging, latency checks, and
   deployment notes. This combines
   [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})'s
   package-and-CI/CD advice around 33:24 in
   [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
   with Simon's unified prediction schema around 54:15.
4. Monitoring dashboard and response path: track input quality, prediction
   distribution, errors and latency, then add one business or proxy metric.
   Ground the post-mortem template in
   [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})'s
   production framing in
   [MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
   Ground the response side in [Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})'s
   incident-response chapters in
   [Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
5. Mini-platform: include a repository template, CI, and a model registry
   convention, then add a deployment guide. Include a monitoring hook and an
   adoption note explaining which team pain it solves. This mirrors
   [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})'s
   pain-point and quick-win adoption strategy around 27:56-36:55 in
   [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

One finished lifecycle is stronger than five disconnected tool demos.
[Ben Wilson]({{ '/people/benwilson/' | relative_url }})'s production ML advice
in [Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }})
repeatedly favors maintainable systems, cross-functional trust, and
cost-benefit tradeoffs over novelty.

## Role Milestones

Entry-level readiness means you can reproduce runs and package inference code.
You can log predictions and explain training metrics. You can compare them with
production behavior and debug a failed run. That aligns with
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})'s
minimum maturity base around 18:41-24:01 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
It also aligns with [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})'s
beginner stack advice around 45:04-56:19 in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).

Mid-level readiness means you can own deployment, monitoring, and registry
usage. You can also own CI/CD and retraining decisions. You can communicate with
data scientists and product teams.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) frames the
MLOps architect role as a technical-business bridge around 8:11-10:32 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) shows why
stakeholder engagement, service levels, post-mortems, and feedback channels
belong in production ML work in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).

Senior readiness means you can design adoption paths, choose build-versus-buy
boundaries, and create platform standards. You can support regulated or
high-risk systems and measure whether MLOps work improves deployment speed or
reliability.
[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) covers
adoption strategy, quick wins, and KPIs. He also covers deployment frequency
and impact tracking around 27:56-36:55 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) adds
build-versus-buy, platform triggers, metadata, and lineage. He also adds
governance and business-first platform timing in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

## Study-Build Boundary

Stop studying and build when you can already train a simple model in Python.
You should be able to use Git and dependency management. You should also be
able to write a batch job or small API. Save and load model artifacts, then
define one offline metric plus one production signal.

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) recommends
hands-on projects, fundamentals, and tool-agnostic end-to-end stitching. She
also recommends ML fundamentals, software engineering, and system design around
39:29-57:14 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

Don't wait until you know every MLOps platform. Build the smallest lifecycle
that works, then study the next tool when the project exposes the problem that
tool solves.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
recommends prioritizing CI/CD and tangible pain points around 48:41 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) makes
the same point for startups around 44:10-49:00 in
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
Python, CI/CD, and orchestration matter before new platform breadth.
Observability and foundational tools matter too.

## Related Pages

These pages cover adjacent concepts and next steps:

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
