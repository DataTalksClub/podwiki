---
layout: wiki
title: "MLOps"
summary: "Reference page for MLOps as the operating discipline for production machine learning systems."
related:
  - ML Platforms
  - MLOps Architecture
  - MLOps Roadmap
  - MLOps Adoption at Scale
  - MLOps Tools
  - MLOps Engineer
  - Machine Learning System Design
  - Model Registry
  - Model Monitoring
  - Experiment Tracking
  - Reproducibility
  - Machine Learning Infrastructure
  - CI/CD
  - Production
  - DataOps
  - MLOps vs DataOps
  - LLMOps
  - GitOps for Data Teams
  - MLOps vs DevOps
---

MLOps is the operating discipline for machine learning systems after they leave
experimentation. It starts with reproducible training and model artifacts. It
continues through deployment and serving. It also covers monitoring, retraining,
governance, and ownership. For a plain-language overview of the same lifecycle, see
DataTalks.Club's
[MLOps in 10 Minutes](https://datatalks.club/blog/mlops-10-minutes.html).

DataTalks.Club conversations usually treat MLOps as a socio-technical system
where people, processes, and technology move together. Teams agree on operating
practices, encode those practices in workflows, and make the repeatable path
easier to use through platforms.

Feature stores, experiment trackers, and model registries are only the
technology layer. The operating work also requires model-development processes
and collaboration between model teams, platform engineers, and the people who
own production use
[[cite:building-production-ml-platform-and-mlops-team@4:42=>Production ML Platforms]].

ML platform teams apply that frame to shared lifecycle paths. They share
training and registry paths. They also share serving, monitoring, lineage, and
governance paths. A centralized platform team adds CI, repository structure, and
reproducible model serving and monitoring
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Use [[DataOps]] for the separate discipline around data pipelines and analytical
delivery. Use [[MLOps vs DataOps]] when the boundary between data operations and
model operations matters. The MLOps side adds model artifacts and experiment
capture. It also adds drift, retraining, deployment approval, and model
governance.

That operating frame runs through conversations about production platforms,
MLOps adoption, and human-centered monitoring
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].

## MLOps Scope

Across the MLOps episodes, the center of gravity is the repeatable path from
model development to a maintained production system. Emmanuel Raj's
[[book:20210705-engineering-mlops=>Engineering MLOps]] conversation frames that
path as an end-to-end lifecycle that includes CI/CD and serving. It also
includes monitoring and governance. Simon Stiebellehner's production-platform
discussion adds the handoff from experiment tracking to model registries and
serving. He also covers orchestration, metadata, lineage, and governance
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Raphael Hoogvliets describes the same lifecycle from the adoption side. His
central MLOps team helps product teams make training and packaging
reproducible. It also standardizes serving and monitoring so many teams can use
the same route to production
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Maria Vechtomova makes the engineering baseline explicit with Git, CI/CD, and
registries. Kubernetes, reusable repositories, and monitoring keep production
paths from becoming one-off projects
[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]].

That lifecycle doesn't stop when a notebook produces a promising metric. A team
still needs to reproduce the run and approve the artifact. It also needs to
support deployment, monitoring, rollback, retraining and retirement. The
[[MLOps Architecture]],
[[Model Registry]], and
[[Experiment Tracking]] pages cover the training-to-production handoff in more
detail. [[Machine Learning System Design]] covers broader design choices around
reliability, latency, and ownership.

Hannes Hapke and Catherine Nelson's
[[book:20210607-building-machine-learning-pipelines=>Building Machine Learning Pipelines]]
conversation covers the pipeline automation layer behind that lifecycle. It
covers data ingestion and validation, plus continuous training and deployment.

In that layer, [[metaflow=>Metaflow]] is another workflow-tooling example. It
helps data scientists move from prototype work toward production without owning
all of the cloud and scheduler plumbing
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Theofilos Papapanagiotou draws the boundary with DevOps through model
lifecycle, drift, and fairness. He also links monitoring to retraining triggers
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]].

## Boundaries and Tradeoffs

Guests agree that MLOps should reduce repeated operational work, but the
platform boundary changes by team size. Nemanja Radojkovic argues that startups
should keep operational discipline lean. SaaS and managed services can help a
small team launch, but vendor lock-in and operational overhead still matter
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]. Simon Stiebellehner
puts more weight on shared platform work once several teams repeat the same
training, registry, deployment, and monitoring steps
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Teams should build a broader platform when several teams repeatedly reinvent
training, serving, and governance work. One model isn't enough, though a single
team may still adopt a SaaS tracker or registry. A broader platform earns its
cost when multiple teams train, serve, and govern models in different ways
without a good reason
[[cite:building-production-ml-platform-and-mlops-team@17:14=>Production ML Platforms]].

The tooling emphasis changes by context. Maria Vechtomova starts from
standardization and reuse, using engineering primitives such as Git, CI/CD, and
registries to keep MLOps practical. She also names Kubernetes, reusable
repositories, and monitoring
[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]].

Lina Weichbrodt starts from business cases, stakeholder buy-in, and model trust.
Monitoring and incident response matter because people need to debug model behavior
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].

Both views point away from tool collecting. The team needs enough platform to
make production ML repeatable.

Useful platform work responds to real failure modes:

- irreproducible runs
- unclear model ownership
- slow deployment
- weak monitoring
- missing rollback
- a business stakeholder who can't trust the model's behavior

## Model Lifecycle

MLOps begins when a model must become a maintained system. Teams need tracked
experiments and approved model artifacts. They also need deployment paths and
serving patterns.

Feedback loops after deployment help teams decide whether to retrain, roll back,
or stop a model. Experiment tracking leads into registries and serving. It then
extends into batch inference, online inference, orchestration, and metadata
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Raphael Hoogvliets adds the reproducibility side of that lifecycle. Data
versioning and traceability help another team member understand what ran and
why. Experiment capture and model registries help too. Serving, monitoring, and
dependency management complete the route
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
That distinction matters because a daily batch scoring job, a low-latency API,
and a managed endpoint have different failure modes and rollback paths.

The lifecycle also includes the decision to stop. Yury Kashnitsky describes
killing a proofreading-AI project after a BERT regressor couldn't reach the
needed precision. He gathered stakeholders and recommended third-party tools,
avoiding months of wasted effort.

The same discussion shows why MLOps includes deployment discipline: SSH deploys
without CI/CD caused repeated production crashes. Serving-layer latency also forced
a re-ranking scope reduction
[[cite:data-science-failures-and-mlops-lessons=>MLOps Lessons from Failures]].

## Monitoring and Feedback

MLOps monitoring covers model behavior, service behavior, and nearby data.
Danny Leybzon connects model monitoring to upstream ETL and data pipelines. He
also connects it to observability, which is why a model incident often starts
as a data incident
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].

A model can degrade because features shifted or labels arrived late. It can
also degrade because a schema changed, an upstream job broke, or the serving
path stopped matching the training path.
For supervised systems, those labels may depend on
[[annotation-quality-workflows=>annotation quality workflows]] before they
become monitoring signals or retraining data.

Lina Weichbrodt adds the product operations side. Service levels and
post-mortems help the team respond to incidents. Live test sets and user bug
reports add product feedback. Input distribution checks and feature drift show
how data changed. Logging, feature stores, and reproducibility help a team
investigate model behavior after release
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].

Maria Vechtomova and Raphael Hoogvliets both place monitoring inside the minimum
MLOps operating stack rather than as an optional add-on
[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Use [[Model Monitoring]] for the model-specific layer. Use [[DataOps]] and
[[Data Quality and Observability]] when the root cause sits in a data pipeline
rather than in the model artifact. Theofilos Papapanagiotou treats that overlap
as both continuity with DataOps and a split from it
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]].
For production incidents, use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
when the boundary is the main question. It separates drift and performance from
freshness, lineage, and recovery ownership
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].

## Platform Timing and Team Adoption

MLOps platforms matter most when many teams need the same route to production.
At that point, teams face [[MLOps Adoption at Scale]]. The supported path has to
be useful enough for product teams to choose it over local workarounds
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Raphael Hoogvliets describes a centralized MLOps team as an enabling group that
supports product teams and ML engineers. The team earns adoption by solving
immediate pain. It then standardizes repositories, packages, serving patterns,
and monitoring
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

A shared platform helps several teams share tracking and registry paths.

It can standardize serving and orchestration.

Metadata and governance stay visible
[[cite:building-production-ml-platform-and-mlops-team=>ML Platform]].

Experiment tracking often comes first because it moves run history out of
private spreadsheets. Even a small model team gets a shared record.

Registries and serving paths can follow as the handoff to production becomes
real. Monitoring and governance can follow too
[[cite:building-production-ml-platform-and-mlops-team@29:41=>ML Platform]]
That connects MLOps to [[ML Platforms]], [[Machine Learning Infrastructure]],
and [[CI/CD]]. It also connects MLOps to [[Model Registry]] and
[[Reproducibility]].

For startups and small teams, the same discipline should stay lighter. Nemanja
Radojkovic's startup advice favors managed services and SaaS. He also favors
CI/CD-first orchestration and only enough custom automation to keep the product
maintainable [[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]. That
startup-specific tradeoff is covered in
[[lean-mlops-for-startups=>lean MLOps for startups]]. It's why [[MLOps Tools]]
should be read as a set of operating choices, not a checklist.

## Governance and Risk

MLOps becomes stricter when models affect regulated decisions in finance and
healthcare. The same concern applies to fraud, risk, and customer-facing
workflows. In finance, Nemanja Radojkovic ties deployment to CI/CD and
monitoring. He also connects it to validation, governance, and risk controls.
Finance teams need model versioning and separate development, test, and production
environments
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]].

[[ai-for-finance-decision-support=>AI Finance Decision Support]] shows the
product-facing version of the same constraint. Those signals include ERP and CRM
context, expense data, and operating data. They can support finance decisions
only when teams keep explanations, review paths, and audit context visible
([[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]]).

Those requirements make approval history and lineage part of the system design.
They also make model versioning and rollback paths explicit. A team needs to
explain which model produced which output. It also needs to explain which data
fed the model. Approval and monitoring paths need to stay visible after release.

Simon Stiebellehner's platform discussion makes the same point through metadata
and lineage. He also covers artifact logging, tracking, and GDPR
concerns [[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

This is where [[Production]], [[Reproducibility]], and [[Governance]] connect to
MLOps. As agents enter production, MLOps practices also extend into
[[Agent Ops]]. In agent systems, teams apply monitoring, drift detection, and
governance to autonomous tool-using systems.

## Related Pages

These pages cover adjacent MLOps concepts:

- [[ML Platforms]]
- [[MLOps Tools]]
- [[MLOps Architecture]]
- [[Machine Learning System Design]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Experiment Tracking]]
- [[Reproducibility]]
- [[Production]]
- [[DataOps]]
- [[MLOps vs DataOps]]
