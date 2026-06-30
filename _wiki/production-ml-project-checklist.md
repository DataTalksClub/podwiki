---
layout: wiki
title: "Production ML Project Checklist"
summary: "Archive-backed checklist for a production ML portfolio project that proves reproducible training, tracked experiments, registry handoff, deployment, monitoring, and rollback criteria."
related:
  - Machine Learning Portfolio Projects
  - MLOps
  - MLOps Roadmap
  - ML Platforms
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Reproducibility
---

## Definition

A production ML project proves that a model can move through a repeatable
lifecycle. The portfolio should show training and evaluation. It should also
show artifact promotion and deployment. It should also show logging,
monitoring, and a rule for rollback or retraining.

Use this checklist with
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
when the target role is [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}), or
[machine learning engineering]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
gives the core lifecycle in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He moves from training and evaluation at 21:03 to
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) at
29:41. At 30:32, he adds the
[model registry]({{ '/wiki/model-registry/' | relative_url }}).

At 31:15, he separates batch and online deployment. At 42:48 and 54:15,
metadata and lineage appear with prediction APIs and logging.


## Common Definition

Guests treat production ML as an operating loop, not a model score. The loop
starts with a business decision and a baseline. It records code and data. It
also records parameters and dependencies.

The loop then promotes an artifact. After deployment, it watches service health
and input quality, plus prediction behavior and downstream outcomes.

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) gives the
pragmatic standard in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
At 18:41 and 22:23, she puts Git and CI/CD in the essential stack. Artifact
storage and registries belong there too. Documentation and reproducibility
matter, and code quality plus testing matter as well. At 33:24, she moves
notebook logic into packages and CI/CD.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) adds
the reproducibility layer in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
At 39:06, he covers CI and repository structure. He also covers
parameterization and tests. At
42:31, he covers data versioning and traceability. He also covers experiment
capture.

## Guest Differences

For Simon, the platform path turns an experiment into a registered artifact and
then into a served model.

Maria's standardization view supports a lightweight portfolio stack when the
lifecycle is clear. The project shouldn't hide weak delivery behind a large
tool list.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) starts with
monitoring. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he connects [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
to upstream ETL and data pipeline causes at 27:35.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) starts with
business value and incident readiness. In
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
she covers business KPIs at 4:50 and incident prep at 24:34. She covers
postmortems at 27:14 and live test sets at 29:23. Feature drift appears at
46:28.

## Reproducible Training

The project should record the code version and parameters. It should also
record dependency versions, data reference, saved artifact, and run command.
Keep configuration separate from code.

That evidence connects to
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}). A simple data
snapshot or hash can be enough, and a manifest also works when it lets another
person rerun the training job.

## Registry And Deployment

Track at least one baseline run and one improved run. Each run should store the
dataset reference, parameters, metric values, and artifact path. Keep failure
notes too.
Then promote one artifact with a registry record.

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) makes
the lightweight version acceptable in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).
At 35:57, he describes a simple interim registry. The record still needs model
version and data version. It also needs the environment, evaluation result,
approval state, and deployment target.

Show either batch scoring or online serving. Batch scoring can write
predictions to a table, while online serving can be a small API. The project
should include input validation, output schema, logs, and one fallback rule.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) argues for simple,
maintainable systems in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
At 6:50 and 8:49, he emphasizes modular and testable code. At 57:38, he
describes production ML capstones with tests and monitoring. He also includes
A/B testing and CI/CD.

## Monitoring And Features

Monitoring should cover service health, input quality, and prediction
distributions. It should also cover business outcomes and name upstream causes
that could break the model.

Danny links production failures to upstream data pipelines and profiling at
27:35-31:50. Lina adds input shifts and unit changes at 46:28-49:28. She also
adds feature drift, logging, and reproducibility. Use
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) for metric choices.

Feature-heavy projects should address training-serving consistency. They
should also address feature validation, ownership, and drift, plus
served-feature logs. [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) grounds
that in
[Feature Stores]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
where he covers feature responsibilities and validation. He also covers
ownership and governance.

## Related Pages

Use these pages to follow the lifecycle pieces.

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
