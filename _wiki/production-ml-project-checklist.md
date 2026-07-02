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
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).
It should add the [MLOps]({{ '/wiki/mlops/' | relative_url }}) evidence that
matters for [ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
[machine learning engineering]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).
That evidence includes tracked runs and artifact promotion. It also includes
deployment, monitoring, and a rollback or retraining rule.

Use this page with the broader
[Portfolio Projects]({{ '/wiki/portfolio-projects/' | relative_url }}) hub
when the project is meant to prove production readiness rather than only model
quality. [Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
gives the lifecycle in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
He moves from training and evaluation at 21:03 to
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) at
29:41 and the [model registry]({{ '/wiki/model-registry/' | relative_url }}) at
30:32. At 31:15, he separates batch and online deployment. Around 42:48 and
54:15, he ties lineage metadata to prediction APIs and logs.

## Lifecycle Proof

The project should turn a decision problem into a maintained model artifact. A
credible implementation records the code version, data reference, parameters,
and dependencies. It also records the evaluation result and saved artifact. The
same record should name the deployment target, monitoring signals, and owner
action for rollback or retraining. Simon describes the same lifecycle in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
but scaled down to a reviewable portfolio repository.

[Maria Vechtomova](https://datatalks.club/people/mariavechtomova.html) gives the
lightweight standard in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html).
At 18:41 and 22:23, she puts Git and CI/CD in the essential stack. She also
includes artifact storage, registries, documentation, and reproducibility.
Code quality and testing belong there too.

At 33:24, notebook logic moves into packages and CI/CD. A portfolio project can
stay small, but it shouldn't hide weak delivery behind a long tool list.

[Raphaël Hoogvliets](https://datatalks.club/people/raphaelhoogvliets.html) adds
the scale and adoption focus in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).
At 39:06, he covers CI and repository structure. He also covers
parameterization and tests. At 42:31, he adds data versioning, traceability,
and experiment capture. The
portfolio version should expose those same checkpoints even if it uses a local
dataset snapshot rather than a full platform.

## Reproducible Training

Reproducible training starts with a visible run path. Include a training command,
configuration file, and dependency lock or environment file. Also include the
data reference, run parameters, metric output, and saved artifact. For
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), a data
snapshot, hash, or manifest can be enough when it lets another person rerun the
training job and compare the result.

[Raphaël Hoogvliets](https://datatalks.club/people/raphaelhoogvliets.html) grounds
this bar in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html)
through repository structure, tests, data traceability, and experiment capture
at 39:06-42:31. [Maria Vechtomova](https://datatalks.club/people/mariavechtomova.html)
supports the same project structure in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)
when she moves notebook code into packages and CI/CD at 33:24.

## Experiment Records and Registry Handoff

Track at least one baseline run and one improved run. Each run should store the
dataset reference and parameters. It should also store metric values and the
artifact path. Keep failure notes with the run record before promoting one
artifact with a registry record.

The handoff from experimentation to deployment should be explicit. Simon's
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)
sequence links [experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
at 29:41 to the [model registry]({{ '/wiki/model-registry/' | relative_url }})
at 30:32. The registry becomes a release boundary rather than a storage folder.

[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) makes
the lightweight version acceptable in
[MLOps in Finance](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html).
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
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
so the README should name which serving mode it implements and why.

[Ben Wilson](https://datatalks.club/people/benwilson.html) argues for simple,
maintainable systems in
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html).
At 6:50 and 8:49, he emphasizes modular and testable code. At 57:38, he
describes production ML capstones with tests and monitoring. He also includes
A/B testing and CI/CD. Use [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) and
[Production]({{ '/wiki/production/' | relative_url }}) when the project needs a
release note, a deployment command, or a rollback path.

## Monitoring, Incidents, and Feedback

Monitoring should cover service health, input quality, and prediction
distributions. It should also cover business outcomes and name upstream causes
that could break the model. [Danny Leybzon](https://datatalks.club/people/dannyleybzon.html)
connects [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) to
upstream ETL and data pipeline causes at 27:35 in
[MLOps Architect Guide](https://datatalks.club/podcast/mlops-model-monitoring-data-observability.html).
His 27:35-31:50 discussion makes data profiling and root-cause visibility part
of the project, not an optional dashboard.

[Lina Weichbrodt](https://datatalks.club/people/linaweichbrodt.html) adds business
value and incident readiness in
[Human-Centered MLOps and Model Monitoring](https://datatalks.club/podcast/human-centered-mlops-and-model-monitoring.html).
At 4:50, she starts from business KPIs. At 24:34 and 27:14, she covers
incident prep and postmortems. At 29:23, she adds live test sets.

At 46:28-49:28, Lina covers input shifts, unit changes, and feature drift.
Logging and reproducibility become monitoring concerns in the same discussion.
Use
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) for metric choices and
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
model-specific signals.

## Feature Reliability

Feature-heavy projects should address training-serving consistency, feature
validation, and ownership. They should also review drift and served-feature
logs. [Willem Pienaar](https://datatalks.club/people/willempienaar.html)
grounds that in
[Feature Stores](https://datatalks.club/podcast/mlops-feature-stores-feature-stores-feast-tecton.html),
where he covers feature responsibilities and validation. He also covers
ownership and governance.

If the project uses a feature table, the README should state who owns each
feature and how training data maps to served inputs. It should also name the
drift or freshness check that would alert the owner.

## Review Checklist

A production ML portfolio project is ready for review when it includes:

- a problem statement, baseline, and metric tied to
  [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
  and [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
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

- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
