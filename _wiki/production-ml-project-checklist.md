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
quality. [[person:simonstiebellehner|Simon Stiebellehner]]
gives the lifecycle in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He moves from training and evaluation at 21:03 to
[[experiment tracking]] at
29:41 and the [[model registry]] at
30:32. At 31:15, he separates batch and online deployment. Around 42:48 and
54:15, he ties lineage metadata to prediction APIs and logs.

## Lifecycle Proof

The project should turn a decision problem into a maintained model artifact. A
credible implementation records the code version, data reference, parameters,
and dependencies. It also records the evaluation result and saved artifact. The
same record should name the deployment target, monitoring signals, and owner
action for rollback or retraining. Simon describes the same lifecycle in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
but scaled down to a reviewable portfolio repository.

[[person:mariavechtomova|Maria Vechtomova]] gives the
lightweight standard in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]].
At 18:41 and 22:23, she puts Git and CI/CD in the essential stack. She also
includes artifact storage, registries, documentation, and reproducibility.
Code quality and testing belong there too.

At 33:24, notebook logic moves into packages and CI/CD. A portfolio project can
stay small, but it shouldn't hide weak delivery behind a long tool list.

[[person:raphaelhoogvliets|Raphaël Hoogvliets]] adds
the scale and adoption focus in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
At 39:06, he covers CI and repository structure. He also covers
parameterization and tests. At 42:31, he adds data versioning, traceability,
and experiment capture. The
portfolio version should expose those same checkpoints even if it uses a local
dataset snapshot rather than a full platform.

## Reproducible Training

Reproducible training starts with a visible run path. Include a training command,
configuration file, and dependency lock or environment file. Also include the
data reference, run parameters, metric output, and saved artifact. For
[[Reproducibility]], a data
snapshot, hash, or manifest can be enough when it lets another person rerun the
training job and compare the result.

[[person:raphaelhoogvliets|Raphaël Hoogvliets]] grounds
this bar in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]
through repository structure, tests, data traceability, and experiment capture
at 39:06-42:31. [[person:mariavechtomova|Maria Vechtomova]]
supports the same project structure in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]
when she moves notebook code into packages and CI/CD at 33:24.

## Experiment Records and Registry Handoff

Track at least one baseline run and one improved run. Each run should store the
dataset reference and parameters. It should also store metric values and the
artifact path. Keep failure notes with the run record before promoting one
artifact with a registry record.

The handoff from experimentation to deployment should be explicit. Simon's
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
sequence links [[experiment tracking]]
at 29:41 to the [[model registry]]
at 30:32. The registry becomes a release boundary rather than a storage folder.

[[person:nemanjaradojkovic|Nemanja Radojkovic]] makes
the lightweight version acceptable in
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]].
At 35:57, he describes a simple interim registry. The record still needs model
version and data version. It also needs the environment, evaluation result,
approval state, and deployment target. For a portfolio project, a table or YAML
manifest can satisfy that requirement when it gives reviewers the exact
artifact and approval state.

## Deployment Boundary

Show either batch scoring or online serving. Batch scoring can write
predictions to a table, while online serving can be a small API. The project
should include input validation, output schema, logs, and one fallback rule.
Simon separates batch and online deployment at 31:15 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
so the README should name which serving mode it implements and why.

[[person:benwilson|Ben Wilson]] argues for simple,
maintainable systems in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
At 6:50 and 8:49, he emphasizes modular and testable code. At 57:38, he
describes production ML capstones with tests and monitoring. He also includes
A/B testing and CI/CD. Use [[ci-cd|CI/CD]] and
[[Production]] when the project needs a
release note, a deployment command, or a rollback path.

## Monitoring, Incidents, and Feedback

Monitoring should cover service health, input quality, and prediction
distributions. It should also cover business outcomes and name upstream causes
that could break the model. [[person:dannyleybzon|Danny Leybzon]]
connects [[model monitoring]] to
upstream ETL and data pipeline causes at 27:35 in
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]].
His 27:35-31:50 discussion makes data profiling and root-cause visibility part
of the project, not an optional dashboard.

[[person:linaweichbrodt|Lina Weichbrodt]] adds business
value and incident readiness in
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring]].
At 4:50, she starts from business KPIs. At 24:34 and 27:14, she covers
incident prep and postmortems. At 29:23, she adds live test sets.

At 46:28-49:28, Lina covers input shifts, unit changes, and feature drift.
Logging and reproducibility become monitoring concerns in the same discussion.
Use
[[Evaluation]] for metric choices and
[[Model Monitoring]] for the
model-specific signals.

## Feature Reliability

Feature-heavy projects should address training-serving consistency, feature
validation, and ownership. They should also review drift and served-feature
logs. [[person:willempienaar|Willem Pienaar]]
grounds that in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores]],
where he covers feature responsibilities and validation. He also covers
ownership and governance.

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
