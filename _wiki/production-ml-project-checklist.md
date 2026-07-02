---
layout: wiki
title: "Production ML Project Checklist"
summary: "Checklist for a production ML portfolio project that proves reproducible training, tracked experiments, registry handoff, deployment, monitoring, and rollback criteria."
related:
  - Portfolio Projects
  - Machine Learning Portfolio Projects
  - MLOps
  - MLOps Roadmap
  - ML Platforms
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Reproducibility
---

A production ML project proves that a model can leave the notebook without
losing reproducibility, ownership, or observability. It should show the problem
framing and baseline from
[[Machine Learning Portfolio Projects]].
It should add the [[MLOps]] evidence that
matters for [[ML platforms]] and
[[machine-learning-engineer-role|machine learning engineering]].
That evidence includes tracked runs and artifact promotion. It also includes
deployment, monitoring, and a rollback or retraining rule.

Use this page with the broader
[[Portfolio Projects]] hub
when the project is meant to prove production readiness rather than only model
quality. The lifecycle runs from training and evaluation to
[[experiment tracking]] and the
[[model registry]], separates batch and
online deployment, and ties lineage metadata to prediction APIs and logs
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

## Lifecycle Proof

The project should turn a decision problem into a maintained model artifact. A
credible implementation records the code version, data reference, parameters,
and dependencies. It also records the evaluation result and saved artifact. The
same record should name the deployment target, monitoring signals, and owner
action for rollback or retraining — the same lifecycle scaled down to a
reviewable portfolio repository
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The lightweight standard puts Git and CI/CD in the essential stack, along with
artifact storage, registries, documentation, reproducibility, code quality, and
testing
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

Notebook logic should move into packages and CI/CD
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).
A portfolio project can stay small, but it shouldn't hide weak delivery behind a
long tool list.

Scale and adoption add CI and repository structure, parameterization and tests,
and data versioning, traceability, and experiment capture
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). The
portfolio version should expose those same checkpoints even if it uses a local
dataset snapshot rather than a full platform.

## Reproducible Training

Reproducible training starts with a visible run path. Include a training command,
configuration file, and dependency lock or environment file. Also include the
data reference, run parameters, metric output, and saved artifact. For
[[Reproducibility]], a data
snapshot, hash, or manifest can be enough when it lets another person rerun the
training job and compare the result.

This bar rests on repository structure, tests, data traceability, and experiment
capture
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]), and the
same project structure moves notebook code into packages and CI/CD
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

## Experiment Records and Registry Handoff

Track at least one baseline run and one improved run. Each run should store the
dataset reference and parameters. It should also store metric values and the
artifact path. Keep failure notes with the run record before promoting one
artifact with a registry record.

The handoff from experimentation to deployment should be explicit, linking
[[experiment tracking]] to the
[[model registry]] so the registry
becomes a release boundary rather than a storage folder
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

A simple interim registry is an acceptable lightweight version
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]). The record
still needs model version, data version, environment, evaluation result,
approval state, and deployment target. For a portfolio project, a table or YAML
manifest can satisfy that requirement when it gives reviewers the exact
artifact and approval state.

## Deployment Boundary

Show either batch scoring or online serving. Batch scoring can write
predictions to a table, while online serving can be a small API. The project
should include input validation, output schema, logs, and one fallback rule.
Batch and online deployment are separate modes
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]),
so the README should name which serving mode it implements and why.

Simple, maintainable systems with modular, testable code are the priority;
production ML capstones include tests, monitoring, A/B testing, and CI/CD
([[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]).
Use [[ci-cd|CI/CD]] and
[[Production]] when the project needs a
release note, a deployment command, or a rollback path.

## Monitoring, Incidents, and Feedback

Monitoring should cover service health, input quality, and prediction
distributions. It should also cover business outcomes and name upstream causes
that could break the model. [[model monitoring]]
connects to upstream ETL and data pipeline causes, making data profiling and
root-cause visibility part of the project rather than an optional dashboard
([[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).

Business value and incident readiness start from business KPIs and add incident
prep, postmortems, and live test sets
([[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring]]).

Input shifts, unit changes, and feature drift are monitoring concerns, and
logging and reproducibility become monitoring concerns too
([[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring]]).
Use
[[Evaluation]] for metric choices and
[[Model Monitoring]] for the
model-specific signals.

## Feature Reliability

Feature-heavy projects should address training-serving consistency, feature
validation, and ownership, and review drift and served-feature logs. Feature
responsibilities, validation, ownership, and governance ground that work
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores]]).

If the project uses a feature table, the README should state who owns each
feature and how training data maps to served inputs. It should also name the
drift or freshness check that would alert the owner.

## Review Checklist

A production ML portfolio project is ready for review when it includes:

- a problem statement, baseline, and metric tied to
  [[Machine Learning Portfolio Projects]]
  and [[Evaluation]]
- a reproducible training command, configuration, dependency record, data
  reference, and saved artifact
- at least two tracked runs with parameters, metrics, artifact paths, and
  failure notes
- a registry or manifest entry with model version, data version, environment,
  evaluation result, approval state, and deployment target
- a batch scoring job or online API with input validation, output schema, logs,
  and fallback behavior
- monitoring signals for service health, input quality, prediction behavior,
  business outcomes, and upstream data causes
- a rollback or retraining rule with the owner action that follows an incident

The surrounding topic pages cover each piece of the project:

- [[Machine Learning Portfolio Projects]]
- [[MLOps]]
- [[MLOps Roadmap]]
- [[ML Platforms]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Reproducibility]]
- [[ci-cd|CI/CD]]
- [[Production]]
