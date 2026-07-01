---
layout: wiki
title: "MLOps"
summary: "Podcast-grounded reference page for MLOps as the operating discipline for production machine learning systems."
related:
  - ML Platforms
  - MLOps Roadmap
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
---

MLOps is the operating discipline for machine learning systems after they leave
experimentation. It starts with reproducible training and model artifacts. It
continues through deployment and serving. It also covers monitoring,
retraining, governance, and ownership.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
defines MLOps through people, workflows, and technology around 4:42. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
connects that operating discipline to CI and repository structure around
39:06-56:50. He also covers reproducibility, serving, monitoring, and package
management.

Use [DataOps]({{ '/wiki/dataops/' | relative_url }}) for the separate
discipline around data pipelines and analytical delivery. Use
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}) when
the boundary between model operations and data operations matters. The MLOps
side adds model artifacts and experiment capture. It also adds drift,
retraining, and model governance.

The production-platform thread appears most clearly in two sources.
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
shows the adoption and reproducibility side.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
shows the platform path through experiment tracking and registries. He also
covers serving, orchestration, metadata, and governance.

Other episodes add tool standardization, monitoring, regulated finance
constraints, and startup tradeoffs.

## Production Model Lifecycle

Across these episodes, MLOps means the repeatable path from model development to a
maintained production system. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Raphaël covers adoption by product teams around 23:01-36:55. Around
39:06-56:50, he moves into CI, repository structure, and parameterization. He
also covers reproducibility and monitoring. Raphaël also covers package
registries and containers.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
Simon frames MLOps through people, workflows, and technology around 4:42. Around
28:20-54:15, he walks through experiment tracking and model registries. He then
covers batch and online serving, orchestration, and metadata. The same sequence
ties those pieces to lineage and governance.

The common thread is ownership after training. MLOps doesn't stop when a
notebook produces a good metric. It asks whether another person can reproduce a
run and approve an artifact. It also asks whether the team can deploy and
monitor the model. The team also needs rollback, retraining, and retirement
decisions.

Theofilos makes that lifecycle boundary explicit in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }})
around 7:28-15:29. He contrasts DevOps with model lifecycle, drift, and
fairness. He also covers monitoring and retraining triggers.

## Platform Timing and Tool Boundaries

Guests differ on how much platform to build and how early to build it. In
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}),
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
emphasizes minimal operational discipline for small teams around 7:54-21:35.
Small teams can use SaaS and managed services when those tools help them
launch, but they still need to watch vendor lock-in and operational overhead. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
Simon makes the platform layer more important when multiple teams repeat the
same training and deployment work. Around 16:52-20:04 and 47:08-49:19, he also
connects that platform need to registries and monitoring.

Guests also differ on tooling emphasis. In
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
stresses standard engineering primitives around 16:27-20:49. She names Git,
CI/CD, and registries. She also names Kubernetes, reusable repositories, and
monitoring.

In
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) shifts the
emphasis toward business cases and stakeholder buy-in around 4:50-29:23. She
also covers monitoring and incident response. Both views agree that tools
aren't the strategy. Maria starts from standardization and reuse, while Lina
starts from the people who need to trust and debug the model.

## Model Lifecycle

MLOps begins when a model must become a maintained system. Teams need tracked
experiments and model artifacts. They also need approval and deployment.

Teams need serving and monitoring after deployment. Once the model runs, teams
need feedback and retraining decisions.

The same lifecycle includes the decision to stop. [Yury Kashnitsky]({{ '/people/yurykashnitsky/' | relative_url }})
describes killing a proofreading-AI project after a BERT regressor reached only
60% precision. He gathered stakeholders, recommended third-party tools, and
avoided months of wasted effort. The same episode documents how SSH deploys
without CI/CD created constant production crashes, and how serving-layer latency
forced a re-ranking scope reduction — infrastructure, not model quality, can be
the real bottleneck
([Data Science Failures and MLOps Lessons]({{ '/podcasts/data-science-failures-and-mlops-lessons/' | relative_url }})).

The
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}) and
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) pages
cover the handoff from training to production. Simon describes that handoff in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
around 29:41-31:51. Experiment tracking leads into registries and serving, then
into batch inference and orchestration.

[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
adds the reproducibility side of the same lifecycle around 42:31-53:08. Raphaël
covers data versioning and traceability. He also covers experiment capture and
model registries. He also covers serving, monitoring, and dependency management.
That distinction matters because a daily batch scoring job, a low-latency API,
and a managed endpoint have different failure modes and rollback paths.

## Monitoring and Feedback

MLOps monitoring covers model behavior, service behavior, and the data around
the model. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) connects model
monitoring to upstream ETL, data pipelines, and observability around
25:04-34:25.

A model can degrade because features shifted or labels arrived late. It can
also degrade because a schema changed or the serving path broke. Lina adds the
product operations side in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
around 24:34-49:28. She covers service levels and post-mortems. She also
covers live test sets and user bug reports.

Her monitoring discussion includes
input distribution checks, feature drift, and logging. She also covers feature
stores and reproducibility.

Use [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
model-specific layer. Use
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
when the root cause sits in the data pipeline rather than the model artifact.
Theofilos marks that overlap around 50:35 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
where the discussion turns to the continuation and divergence between DataOps
and MLOps.

## Governance and Risk

MLOps becomes stricter when models affect regulated decisions in finance and
healthcare. The same concern applies to fraud, risk, and customer-facing
workflows. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
Nemanja ties deployment to CI/CD, monitoring, and governance around
14:57-23:39. He also covers validation and risk controls.

He later describes a minimal finance stack around 31:57-35:57 with dev, test,
and production environments. In the same discussion, he covers monitoring, model
versioning, and simple interim registries. Those
requirements make approval history, lineage, model versioning, and rollback
paths part of the system design.

This is where [Production]({{ '/wiki/production/' | relative_url }}),
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[Governance]({{ '/wiki/governance/' | relative_url }}) connect to MLOps. A team
needs to explain which model produced which output. It also needs the data,
approval path, and monitoring path. Simon covers the same governance trail around
42:48-45:50 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
where metadata and lineage influence the platform design. He also covers
artifact logging, tracking, and GDPR concerns.

## Related Pages

These pages cover adjacent MLOps concepts:

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
- [MLOps Frameworks]({{ '/guides/mlops-frameworks/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
