---
layout: wiki
title: "MLOps Engineer"
summary: "The MLOps engineer role across model delivery and production ownership."
related:
  - MLOps
  - MLOps Roadmap
  - ML Platforms
  - Machine Learning Engineer Role
  - Data Engineer Role
  - Platform Engineering
  - Model Monitoring
  - Model Registry
  - Experiment Tracking
---

An MLOps engineer makes machine learning deliverable after the notebook stage.
The role gives model builders a repeatable path from experiment to artifact and
from release to repair
([MLOps]({{ '/wiki/mlops/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

## Common Definition

The common definition in the interviews is enablement. An MLOps engineer does
not own every model idea, every data pipeline, or every cloud resource. The role
owns the operating path that makes model work reproducible and deployable.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
frames MLOps as people, process, and technology at 4:42 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) gives a
similar practical definition at 11:10 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
Her version enables data scientists with reproducible practices, teaching,
reusable infrastructure, and clear standards.

## Points of Disagreement

Guests disagree mostly on where to start and how much platform to build.
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes centralized MLOps as an enabling team at 23:01 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
His version starts with product-team pain at 33:13, quick wins at 32:46, and
adoption signals such as deployment frequency at 36:55.

Maria's version starts from existing engineering primitives and names Git,
CI/CD, registries, and Kubernetes. She also covers standardized repositories and
monitoring at 16:27 and 18:41 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) pulls the role
toward production observability and customer architecture at 8:11 and 25:04 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) adds the
human side. Her version emphasizes incident preparation, stakeholder trust,
debugging, and feedback channels in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) shows
that finance and startup environments set different constraints in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
and [Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).

## Operating Scope

An MLOps engineer owns the operating path around models. That includes
reproducible experiments and model artifacts, plus release automation and
serving. Monitoring, rollback, and retraining decisions belong in the same path
([MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}),
[Production]({{ '/wiki/production/' | relative_url }})).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
frames MLOps around people, processes, and technology in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
His platform discussion moves from self-service compute at 28:20 into
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and
[model registries]({{ '/wiki/model-registry/' | relative_url }}) at 30:32.
Batch inference and online serving appear at 31:15, orchestration at 31:51, and
metadata and lineage at 42:48. Prediction logging appears at 54:15. Developer
experience and governance round out the platform scope.

That makes the job broader than deployment, but narrower than "own all ML."
Data scientists may still own problem framing and model evaluation. Machine
learning engineers may own a product-facing inference service. Data engineers
may own ingestion, transformation, freshness, and data quality. The MLOps
engineer connects those surfaces.

The model then has a path to reproduction and promotion. It also has a path to
serving and monitoring, plus repair when something breaks
([Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }})).

## Responsibilities

The interviews support a compact responsibility set for an MLOps engineer:

- Make experiments recoverable with code versions and full dependency records.
  Track run parameters and data references with metrics. Store artifacts and
  environment details with each training run too
  ([Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}),
  [MLOps at Scale, 42:31]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
- Create a model handoff path with artifact storage and registry metadata.
  Record the owner, version, and evaluation result. Add approval state,
  deployment target, and rollback notes
  ([Model Registry]({{ '/wiki/model-registry/' | relative_url }}),
  [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
- Standardize CI/CD, packaging, tests, and repository layout. Add dependency
  management and deployment checks so model releases stop depending on manual
  handoffs
  ([Pragmatic and Standardized MLOps, 29:55 and 33:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
  [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})).
- Support the right serving mode for the use case. Common options include batch
  scoring, online APIs, managed endpoints, and scheduled jobs. Containers and
  platform-specific serving may also fit
  ([Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
  [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
- Monitor service health, input quality, feature and prediction distributions,
  drift signals, latency, and errors. Add feedback and business outcomes where
  they can be observed
  ([Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
  [Human-Centered MLOps, 46:28 and 49:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
- Build reusable templates, deployment guides, logging standards, support
  paths, and self-service workflows only where repeated team pain justifies
  platform work
  ([ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
- Add lineage, access control, validation, approvals, retention, and audit
  trails when the domain requires governance
  ([Governance]({{ '/wiki/governance/' | relative_url }}),
  [MLOps in Finance, 21:21 and 31:57]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

This role is strongest when it starts from a concrete failure mode. If a team
can't reproduce old experiments, start with tracking and artifact discipline.
Simon calls experiment tracking a low-hanging platform win at 29:41 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

If models can't be deployed safely, start with CI/CD and one release path.
Raphaël names CI/CD and tangible pain points at 48:41 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
If production behavior is invisible, start with logging and monitoring. Add
response ownership
([Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})).

## Skills

An MLOps engineer needs enough software engineering to make ML work testable
and maintainable. That means Python and modular code. Configuration, APIs, and
batch jobs matter too. Dependency management and containers matter as well.
Package registries and code review complete the base alongside CI/CD
([Pragmatic and Standardized MLOps, 18:41 and 33:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})).

Maria's episode is more tool-agnostic. Learn fundamentals before chasing a new
platform
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

The role also needs ML literacy. You don't need to be the strongest modeler on
the team, but you do need to understand training versus inference. Features,
labels, and metrics matter too. Artifacts and drift affect useful release paths.
Error analysis affects monitoring paths
([Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
[MLOps at Scale, 45:10]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Data engineering awareness isn't optional. [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})
connects model monitoring to upstream ETL and data pipelines at 27:35. Profiling and
data observability sit in the same discussion in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
A model may look broken because a source schema changed or labels arrived late.
It may also fail because features shifted or a pipeline stopped producing fresh
data
([Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }})).

Communication is part of the job because MLOps is a support and adoption
function. [Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})
ties monitoring to business cases at 4:50, stakeholder buy-in at 12:22, and
service levels at 24:34. Debugging, user feedback, and post-mortems belong
there too. Incident response is part of the same discussion in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Raphaël's enabling-team discussion adds internal-user feedback and quick wins
as operating skills, not soft extras
([Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}),
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## Boundaries With Nearby Roles

The boundary with a
[machine learning engineer]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
depends on ownership. A machine learning engineer often owns a specific
model-backed product capability. That includes serving code, latency,
scalability, and maintainability. Product integration belongs there too.

An MLOps engineer usually owns the shared path that many model builders use.
That path includes tracking, registries, CI/CD, and deployment templates.
Monitoring hooks, governance, and self-service infrastructure belong there too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

The boundary with a
[data engineer]({{ '/wiki/data-engineer-role/' | relative_url }}) is the
handoff from reliable data to reliable models. Data engineers own ingestion,
storage, transformations, and orchestration. Schemas and freshness are part of
the same ownership. MLOps engineers use that data foundation for model artifacts
and serving paths. Monitoring and
retraining decisions build on the same foundation
([MLOps]({{ '/wiki/mlops/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})).

The boundary with DevOps or SRE is model-specific uncertainty because MLOps
borrows Git and CI/CD. It also borrows containers and observability. Incident
response and deployment discipline still apply, with training-data references
added.
Feature freshness and model versions matter alongside offline-versus-online
metrics. Drift, delayed labels, and retraining decisions make the operating
model different.

[MLOps vs DevOps]({{ '/comparisons/mlops-vs-devops/' | relative_url }}) explains
this boundary.
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[MLOps Architect Guide at 27:35]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
cover the monitoring side.

The boundary with
[platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}) is
ML specialization because platform engineers build general internal developer
platforms. MLOps engineers adapt that work to model lifecycles and data
scientist workflows. Experiment tracking and registries are part of that
specialization. Serving and model monitoring are too
([ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})).

## Tools and Stack

Treat tools as coverage areas before treating them as a shopping list. The
interviews repeatedly favor standard engineering habits and adopted workflows
over broad tool collections
([MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}),
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

A practical MLOps engineer stack should cover:

- version control, code review, CI/CD, tests, and release automation
  ([CI/CD]({{ '/wiki/ci-cd/' | relative_url }})).
- Python packaging, containers, dependency locks, registries, and environment
  management
  ([Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})).
- experiment tracking for runs, metrics, parameters, artifacts, code versions,
  and data references
  ([Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})).
- model registry or registry-like metadata for artifact promotion, ownership,
  approval, deployment target, and rollback
  ([Model Registry]({{ '/wiki/model-registry/' | relative_url }})).
- batch inference, online serving, scheduled jobs, APIs, managed endpoints, or
  orchestration, depending on product needs
  ([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
- service, data, and model monitoring with prediction logging and alert routing
  ([Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})).
- platform templates, shared libraries, self-service compute, documentation,
  and support workflows when several teams repeat the same work
  ([ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) shows
why the stack changes by context. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
the minimum expands at 31:57 toward dev/test/prod environments, monitoring, and
CI/CD. Model versioning, data versioning, governance, and release controls
matter too. At 21:21 he also stresses release management. Exact builds,
approvals, rollback procedures, and knowing what's in production all matter.

In
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}),
the same guest argues at 11:54 for SaaS-first choices. At 44:10, he argues for a
leaner stack while still keeping enough automation to avoid unmaintainable MVPs.

## Roadmap

Use the roadmap as a build sequence, not a course catalog
([MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})).

1. Train one model and save the artifact, metric, code, dependencies, and data
   reference.
2. Make the run reproducible with experiment tracking or a structured logging
   convention.
3. Package inference as a batch job or API with input validation, prediction
   logging, error handling, and a clear runtime environment.
4. Add CI/CD for tests, packaging, container builds, deployment checks, and
   configuration changes.
5. Add a registry convention with owner, version, evaluation result, approval
   state, deployment target, and rollback notes.
6. Monitor input quality, prediction distributions, latency, errors, service
   health, and one business or proxy metric.
7. Turn repeated work into platform templates, shared logging, deployment
   guides, and self-service paths only after several projects repeat the same
   steps.

The sequence matches the practical bias in the interviews. Simon treats
experiment tracking and registries as early platform wins at 29:41 and 30:32.
Maria starts with version control, CI/CD, registries, and monitoring at 18:41.
Raphaël starts from team pain and adoption, then uses quick wins before broad
standardization
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## Portfolio and Interview Signals

Strong MLOps engineer candidates show how a model behaves after release. A
notebook isn't enough. A strong portfolio operates the lifecycle. It recovers
the run, promotes the artifact, and deploys the model. It also monitors the
system and explains what happens when something fails
([Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})).

Good projects include a tracked training run and a batch scoring pipeline. Add
an online service, a registry convention, and a monitoring dashboard. Include a
short operations note that names the model owner, data owner, and alert owner.
The same note should cover rollback, known failure modes, and retraining
criteria
([Model Registry]({{ '/wiki/model-registry/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})).

In interviews, expect ownership and tradeoff questions. A startup answer may
favor managed services and a simple artifact convention. It should still name
one observable deployment path
([Lean MLOps for Startups, 7:54 and 11:54]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }})).

A finance answer should name approvals, validation, and lineage. It should also
cover dev/test/prod separation, release controls, and monitoring
([MLOps in Finance, 21:21 and 31:57]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

A platform answer should explain internal users and support models. Adoption
metrics and templates belong in the same answer. Feedback loops do too
([MLOps at Scale, 23:32 and 33:13]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

## Related Pages

These pages cover the role's adjacent practices and boundaries.

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) defines the broader operating
  discipline.
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) gives a staged
  learning sequence.
- [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
  maps the system design.
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) covers stack
  categories.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) covers shared
  internal platforms.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
  [Model Registry]({{ '/wiki/model-registry/' | relative_url }}), and
  [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
  cover core MLOps components.
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}) and
  [MLOps vs DevOps]({{ '/comparisons/mlops-vs-devops/' | relative_url }}) define
  nearby boundaries.
- [Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
  and [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
  show adjacent responsibilities.
