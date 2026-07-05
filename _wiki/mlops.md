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
[[cite:building-production-ml-platform-and-mlops-team@4:42=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

[[DataOps]] owns the operating path for data pipelines and analytical delivery.
MLOps adds model artifacts and experiment capture. It also adds drift,
retraining, deployment approval, and model governance. [[MLOps vs DataOps]]
covers that boundary in detail. For the narrower incident boundary between
upstream data reliability and deployed-model behavior, use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]].

[[MLOps Architecture]] owns the component map, and [[MLOps Roadmap]] owns
rollout order. [[MLOps Engineer]] owns role responsibilities, while
[[MLOps Tools]] owns stack categories and selection tradeoffs.

## Operating Boundary

MLOps covers the repeatable path from model development to a maintained
production system. Emmanuel Raj's
[[book:20210705-engineering-mlops=>Engineering MLOps]] conversation frames that
path as an end-to-end lifecycle with CI/CD, serving, monitoring, and governance.
Simon Stiebellehner's platform discussion places experiment tracking, model
registries, and serving on the same production path. Orchestration, metadata,
lineage, and governance join that path too
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

A notebook metric doesn't end the lifecycle. A team still has to reproduce the
run, approve the artifact, and deploy it. Teams use the
[[notebook-to-production-workflow=>notebook to production workflow]] to make that
handoff explicit before monitoring, rollback, retraining, or retirement
decisions start.

[[Experiment Tracking]] and [[Model Registry]] cover the training-to-production
handoff, while [[Model Monitoring]] covers the post-release signal layer.
[[Machine Learning System Design]] covers latency, reliability, and product
ownership choices around the model.

Pipeline automation sits inside this boundary when it moves models from data
ingestion and validation into training, deployment, and monitoring. Theofilos
Papapanagiotou separates MLOps from DevOps through model lifecycle concerns such
as drift, fairness, and retraining triggers. The same lifecycle concerns
separate the disciplines in [[mlops-vs-devops=>MLOps vs DevOps]]
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]].

## Lifecycle Decisions

MLOps begins when a model must become a maintained system. Teams need tracked
experiments and approved model artifacts. They also need deployment paths and
serving patterns.

Post-release evidence helps teams decide whether to retrain, roll back, or stop
a model. Experiment tracking leads into registries and serving. It then extends
into batch inference, online inference, orchestration, and metadata
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Raphael Hoogvliets adds the reproducibility side of the lifecycle. Data
versioning and traceability help another team member understand what ran and
why. Experiment capture and model registries help too. Serving, monitoring, and
dependency management complete the route
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
Daily batch scoring jobs, low-latency APIs, and managed endpoints create
different ownership and rollback questions.

MLOps also includes the decision to stop. One production-failure discussion
covers a proofreading-AI project that ended after a BERT regressor couldn't
reach the needed precision. The same episode connects deployment discipline to
production stability. SSH deploys without CI/CD caused repeated crashes, and
serving latency forced a re-ranking scope reduction
[[cite:data-science-failures-and-mlops-lessons=>MLOps Lessons from Failures]].

## Context Changes the Boundary

The amount of shared platform work depends on context. Startups may keep the
discipline lean with SaaS, managed services, and CI/CD-first orchestration.
[[Lean MLOps for Startups]] covers that smaller operating model.
They may add only enough custom automation to keep the product maintainable
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].

Multi-team organizations move more of the route into shared templates and
registries. They also share serving paths, monitoring hooks, and governance
conventions when teams repeat the same work
[[cite:building-production-ml-platform-and-mlops-team@17:14=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Risk also changes the boundary. Finance teams need model versioning, separate
development, test, and production environments. They also need validation,
monitoring, governance, and release controls earlier than a low-risk internal
model
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]. Customer-facing
or decision-support systems need visible explanations, review paths, and audit
context when model outputs influence finance decisions
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]].

Monitoring sits on the boundary between MLOps and data operations. Model
failures often trace back to upstream ETL, feature pipelines, schema changes, or
late labels
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].
[[Data Quality and Observability]] and
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
cover that split. Tool-using LLM systems have adjacent production practices in
[[Agent Ops]].
