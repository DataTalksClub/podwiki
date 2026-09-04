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
  - Feature Stores
  - Experiment Tracking
  - Reproducibility
  - Machine Learning Infrastructure
  - Production ML Project Checklist
  - CI/CD
  - Production
  - DataOps
  - MLOps vs DataOps
  - LLMOps
  - GitOps for Data Teams
  - MLOps vs DevOps
---

MLOps is the operating discipline for machine learning systems after
experimentation. It starts when a team has to reproduce training, approve a
model artifact, and deploy it. After release, the team has to monitor behavior,
decide when to retrain or roll back, and keep ownership visible. For a
plain-language overview, DataTalks.Club's
[MLOps in 10 Minutes](https://datatalks.club/blog/mlops-10-minutes.html)
covers the same lifecycle.

Simon Stiebellehner frames MLOps as people, operating habits, and technology
working together. Feature stores, experiment trackers, and model registries are
tools inside that operating model. The harder boundary is often the handoff
between model teams, platform teams, and production owners.
When that handoff becomes shared-service ownership, the
[[ml-platform-engineer-role=>ML platform engineer role]] owns the reusable path
rather than a single model.
[[cite:building-production-ml-platform-and-mlops-team@04:42=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

[[DataOps]] owns the operating path for data pipelines and analytical delivery.
MLOps adds model artifacts and experiment capture. It also adds drift,
retraining, deployment approval, and model governance. [[MLOps vs DataOps]]
covers that boundary in detail. For the narrower incident boundary between
upstream data reliability and deployed-model behavior, use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]].

[[MLOps Architecture]] owns the component map, and [[MLOps Roadmap]] owns
rollout order. [[MLOps Engineer]] owns role responsibilities, while
[[MLOps Tools]] owns stack categories and selection tradeoffs. For a concrete
project path, use the [[production-ml-project-checklist=>production ML project
checklist]].

## Operating Boundary

MLOps covers the repeatable path from model development to a maintained
production system. Emmanuel Raj's
[[book:20210705-engineering-mlops=>Engineering MLOps]] conversation frames that
path as an end-to-end lifecycle with CI/CD, serving, monitoring, and governance.
Simon Stiebellehner's platform discussion places experiment tracking, model
registries, and serving on the same production path. Orchestration, metadata,
lineage, and governance join that path too.
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]

A notebook metric doesn't end the lifecycle. A team still has to reproduce the
run, approve the artifact, and deploy it. Teams use the
[[notebook-to-production-workflow=>notebook to production workflow]] to make that
handoff explicit before monitoring, rollback, retraining, or retirement
decisions start. For a
[[data-scientist-to-machine-learning-engineer=>data scientist to machine learning engineer]],
the handoff turns modeling evidence into reproducible runs, artifacts, and
deployment decisions.

[[Experiment Tracking]] and [[Model Registry]] cover the training-to-production
handoff, while [[Model Monitoring]] covers the post-release signal layer.
[[Machine Learning System Design]] covers latency, reliability, and product
ownership choices around the model.

Pipeline automation sits inside this boundary when it moves models from data
ingestion and validation into training, deployment, and monitoring. Theofilos
Papapanagiotou separates MLOps from DevOps through model lifecycle concerns such
as drift, fairness, and retraining triggers. The same lifecycle concerns
separate the disciplines in [[mlops-vs-devops=>MLOps vs DevOps]].
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]

## Platform Components

MLOps becomes concrete when the team names the handoffs. In Simon
Stiebellehner's data-science workflow, teams pull data and explore it. Then
they train, evaluate, and persist a model for another job or service.
[[cite:building-production-ml-platform-and-mlops-team@21:03=>Production ML Platforms]][[cite:building-production-ml-platform-and-mlops-team@29:41=>Production ML Platforms]][[cite:building-production-ml-platform-and-mlops-team@30:32=>Production ML Platforms]]

That's why [[Experiment Tracking]] and [[Model Registry]] are early platform
components. They turn experiment history and model artifacts into shared
production evidence.

Serving is the next boundary. Batch inference and online serving create
different operating questions, so one MLOps path may support both. Batch scoring
can look like a scheduled data job. Online serving adds request schemas,
latency, availability, and logging. API and logging design matter because later
monitoring depends on the prediction records the service emits.
[[cite:building-production-ml-platform-and-mlops-team@31:15=>Production ML Platforms]][[cite:building-production-ml-platform-and-mlops-team@54:15=>Production ML Platforms]]

Feature work sits between [[DataOps]] and MLOps. Feature stores and feature
pipelines matter when a team has to keep training and inference features
consistent. Willem Pienaar's feature-store episode makes that boundary
operational. Feature creation and retrieval belong there. On-demand transforms
and real-time lookup belong there too when the product depends on fresh
features.
[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]
[[Feature Stores]].

The component list should stay smaller than the operating problem. A single team
may start with SaaS components, managed cloud services, and a few conventions.
A multi-team platform may need reusable compute and orchestration such as
[[metaflow=>Metaflow]]. It may also need registries, serving templates,
monitoring hooks, and governance defaults.
[[cite:building-production-ml-platform-and-mlops-team@20:04=>Production ML Platforms]][[cite:building-production-ml-platform-and-mlops-team@34:01=>Production ML Platforms]]
[[ML Platforms]] covers that shared infrastructure layer.

## Lifecycle Decisions

MLOps begins when a model must become a maintained system. Teams need tracked
experiments and approved model artifacts. They also need deployment paths and
serving patterns.

Post-release evidence helps teams decide whether to retrain, roll back, or stop
a model. Experiment tracking leads into registries and serving. It then extends
into batch inference, online inference, orchestration, and metadata.
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]

Raphael Hoogvliets adds the reproducibility side of the lifecycle. Data
versioning and traceability help another team member understand what ran and
why. Experiment capture and model registries help too. Serving, monitoring, and
dependency management complete the route.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
Daily batch scoring jobs, low-latency APIs, and managed endpoints create
different ownership and rollback questions.

The design phase belongs in the same lifecycle. Arseny Kravchenko argues for a
lightweight design document before implementation. Define the problem, turn
requirements into metrics, and map the data flow and dependencies. That keeps
MLOps from becoming only a post-training deployment exercise.
[[cite:building-scalable-and-reliable-machine-learning-systems@20:21=>Scalable and Reliable ML Systems]][[cite:building-scalable-and-reliable-machine-learning-systems@29:01=>Scalable and Reliable ML Systems]][[cite:building-scalable-and-reliable-machine-learning-systems@37:15=>Scalable and Reliable ML Systems]]
[[Machine Learning System Design]] owns that broader product and system design.

MLOps also includes the decision to stop. One production-failure discussion
covers a proofreading-AI project that ended after a BERT regressor couldn't
reach the needed precision. The same episode connects deployment discipline to
production stability. SSH deploys without CI/CD caused repeated crashes, and
serving latency forced a re-ranking scope reduction.
[[cite:data-science-failures-and-mlops-lessons=>MLOps Lessons from Failures]]

## Monitoring and Response

MLOps doesn't end when the model reaches production. Theofilos Papapanagiotou
puts monitoring beside drift, fairness, and retraining triggers. Monitoring
output can become training data when production feeds model development.
[[cite:mlops-kubeflow-model-monitoring@11:17=>Mastering MLOps]][[cite:mlops-kubeflow-model-monitoring@33:27=>Mastering MLOps]]

Danny Leybzon draws the production boundary differently. Model monitoring often
has to follow symptoms upstream into ETL, data pipelines, and root causes. That
doesn't make MLOps and DataOps the same practice. It means the incident path has
to connect model signals with data observability and lineage.
[[cite:mlops-model-monitoring-data-observability@25:04=>MLOps Architect Guide]][[cite:mlops-model-monitoring-data-observability@27:35=>MLOps Architect Guide]]

Use [[Model Monitoring]] for model behavior and prediction signals. Use
[[Data Quality and Observability]] for freshness, volume, schema, and lineage.

Lina Weichbrodt adds the human response path. Teams need service levels, impact
assessment, post-mortems, and ML-specific recovery steps. Live test sets, small
[[a-b-testing=>A/B tests]], feature logging, and user feedback help teams find
problems before delayed labels arrive.
[[cite:human-centered-mlops-and-model-monitoring@24:34=>Human-Centered MLOps]][[cite:human-centered-mlops-and-model-monitoring@29:23=>Human-Centered MLOps]][[cite:human-centered-mlops-and-model-monitoring@49:28=>Human-Centered MLOps]]
That makes MLOps a response discipline, not just a metrics dashboard.

## Context Changes the Boundary

The amount of shared platform work depends on context. Startups may keep the
discipline lean with SaaS, managed services, and CI/CD-first orchestration.
[[Lean MLOps for Startups]] covers that smaller operating model.
They may add only enough custom automation to keep the product maintainable.
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]

Multi-team organizations move more of the route into shared templates and
registries. They also share serving paths, monitoring hooks, and governance
conventions when teams repeat the same work.
[[cite:building-production-ml-platform-and-mlops-team@17:14=>Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Theofilos Papapanagiotou describes maturity as a path from manual training to
pipeline automation and later data-driven retraining. The useful question isn't
whether a team has a named MLOps platform. It's whether another person can
reproduce the run and deploy the approved artifact. They also need to observe
production behavior and respond when the model or data changes.
[[cite:mlops-kubeflow-model-monitoring@27:01=>Mastering MLOps]][[cite:mlops-kubeflow-model-monitoring@30:08=>Mastering MLOps]]
[[MLOps Adoption at Scale]] covers the larger rollout sequence.

Risk also changes the boundary. Finance teams need model versioning, separate
development, test, and production environments. They also need validation,
monitoring, governance, and release controls earlier than a low-risk internal
model.
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]] Customer-facing
or decision-support systems need visible explanations, review paths, and audit
context when model outputs influence finance decisions.
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]]

[[algorithmic-trading=>Python stock analysis]] is the market-execution version
of that operating concern. Backtests, costs, model versions, and execution
cadence become part of the MLOps boundary.
[[cite:algorithmic-trading-with-python-and-machine-learning=>Algorithmic Trading with Python]]

Monitoring sits on the boundary between MLOps and data operations. Model
failures often trace back to upstream ETL, feature pipelines, schema changes, or
late labels.
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]
[[Data Quality and Observability]] and
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
cover that split. Tool-using LLM systems have adjacent production practices in
[[Agent Ops]].

For a structured entry into the discipline, [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) walks the same
lifecycle — experiment tracking, orchestration, deployment, monitoring, and
best practices — around one NY Taxi use case, and podcast discussions of
pragmatic MLOps practice point hands-on projects plus this course at
learning paths.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]
