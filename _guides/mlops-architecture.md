---
layout: article
title: "MLOps Architecture: Production Map for Models, Pipelines, Platforms, and Feedback"
keyword: "mlops architecture"
summary: "A podcast-backed MLOps architecture guide covering data inputs, training and feature pipelines, experiment tracking, registries, CI/CD, serving, monitoring, feedback loops, governance, and the tradeoff between simple stacks and shared platforms."
related_wiki:
  - MLOps
  - MLOps Roadmap
  - ML Platforms
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Reproducibility
  - DataOps
  - Governance
---

MLOps architecture is the production map for data, training, deployment, and
model improvement. It should show how a model moves from raw inputs to
predictions. It should also show how teams reproduce and approve the model,
monitor what happens after release, and route production evidence back into the
next decision.

DataTalks.Club guests describe this architecture as a production operating
system for machine learning work. It's not a vendor diagram. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
defines MLOps around people, process, and technology at 4:42. Later, around
29:41-31:51, he connects experiment tracking and registries to batch inference.
He also covers online serving and orchestration.

In
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) makes the
same point operationally. Around 18:41, her useful stack starts with version
control and CI/CD. Registries, a model registry, and monitoring follow before
the work becomes a large platform program.

For the broader discipline, start with
[MLOps]({{ '/wiki/mlops/' | relative_url }}). Use
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) for build order,
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) for the shared
platform layer, and [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
for stack selection.

## Architecture Flow

A practical MLOps architecture has one forward path and one return path.

The forward path starts with data inputs. Source systems feed ingestion and
transformation jobs, which create features or training datasets. A training
pipeline uses that data, records metrics, and stores a model artifact.

A registry or registry-like convention promotes the artifact into a deployable
model. CI/CD then packages the code, dependencies, and serving configuration.
The deployment target may be a batch scoring job, an online endpoint, an edge
deployment, or a hybrid setup.

The return path starts when production evidence contradicts training-time
assumptions. Drift and missing inputs can send the team back to investigation.
Schema changes, latency, and errors can do the same. The team may fix data,
change features, roll back, or retrain. It may also update the product workflow.

[Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }})
frames this as a maturity progression in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}).
Around 27:01, he distinguishes manual training from pipeline automation. Around
30:08-33:27, he adds data-driven triggers, automated retraining, and monitoring
as a source of new training data. The return path explains how a deployed model
keeps learning from the world without hiding responsibility behind automation.

## Data Inputs and Feature Pipelines

MLOps architecture starts before the model. Data inputs may come from product
events and operational databases. They may also come from files, third-party
feeds, analytics tables, or human labels. The architecture should name the owner,
arrival cadence, schema expectation, and validation point for each source.

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) gives the data
pipeline side of this picture in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Around 13:25, she compares ML pipelines and analytics data pipelines. Around
18:44, she separates MLOps from DataOps by the kind of production system being
operated. Around 44:57, she describes feature engineering, model training, and
serving as ML pipeline steps. Use those boundaries when deciding
which parts of the system belong to [DataOps]({{ '/wiki/dataops/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), or both.

Feature and training pipelines transform inputs into model-ready data. In a
small architecture, that may be SQL plus a scheduled Python job. In a larger
architecture, the team may add
[orchestration]({{ '/wiki/orchestration/' | relative_url }}) and feature-store
conventions. Validation checks and lineage often follow.

The important question isn't whether the diagram includes a feature store. The
team needs to explain how training data and inference data
stay consistent enough for the use case, especially when batch and online paths
coexist.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) makes the upstream
dependency explicit in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
At 27:35, he ties model problems to ETL and data pipelines. He also brings drift
and quality into the same monitoring view. If the monitoring view stops at the
endpoint, the team can miss the source-system or feature-pipeline change that
caused the model to fail.

## Training and Experiment Tracking

Training architecture connects code and data to parameters, metrics, artifacts,
and review decisions. At minimum, the team needs a reproducible environment and
version control. It also needs a data reference, saved metrics, and an artifact
location. Once several people compare runs,
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) becomes
the shared memory of the system.

Simon calls experiment tracking a low-hanging platform win around 29:41 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He frames it as a move away from spreadsheet run logs toward transparent model
history. Around 42:48, the same discussion connects metadata and lineage to
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), artifacts, and
tracking.

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) broadens
the same requirement in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Around 39:06-44:22, he covers CI and repository structure. He also covers
parameterization, testing, data versioning, and traceability. A team shouldn't
treat training output as production-ready until another person can reproduce it.
That person should also understand the evidence behind it.

## Registry and Release Gates

A [model registry]({{ '/wiki/model-registry/' | relative_url }}) is the handoff
point between training and production. It stores the artifact and the context
needed to deploy it safely.

A useful registry record includes:

- model version and owner
- artifact location and code version
- training-data reference and evaluation result
- approval state and deployment target
- rollback note

The registry doesn't have to be a large platform product on day one. Maria
discusses registry choices around 20:49 in
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
including artifact stores and MLflow-style alternatives. Around 24:01, she
places reproducibility, versioning, and traceability ahead of more elaborate
tooling for early teams.

For a small team, object storage plus a structured promotion convention may be
enough if everyone follows the same rule. For a larger or regulated team, access
control and lineage become harder to avoid. Approval history and
deployment-system integration usually follow.

Simon connects registries to downstream consumption at 30:32 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
The registry's architectural job is to turn a training output into a model
another job, service, or team can depend on.

## CI/CD, Packaging, and Deployment

CI/CD in MLOps should cover ordinary software checks and model-specific checks.
The pipeline may test code and validate data transformations. It may also build
containers, publish packages, run deployment checks, and promote changes between
environments. The architecture should show how code and model artifacts move
together. Configuration and infrastructure should move with them.

Raphaël gives a concrete component set for this around 52:39 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
He names version control, CI/CD, and containerization. He also names model
registry, experiment tracking, and monitoring. Compute, serving, and package
registry also belong in the component set.

Maria adds the standardization work around 29:55 and 33:24 in
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
Her examples include cookie-cutter repositories, service principals, Databricks
workflows, and moving logic out of notebooks into packages and CI/CD.

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) gives the
startup version in
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
Around 44:10, he describes a minimal stack with Python, CI/CD orchestration, and
Dagster. Around 11:54-19:19, he also warns that managed services can accelerate
a young team while creating migration and lock-in tradeoffs. That matters for
[MLOps]({{ '/wiki/mlops/' | relative_url }}): the simplest repeatable release
path usually beats a broad platform that the team can't yet operate.

## Orchestration and Serving

[Orchestration]({{ '/wiki/orchestration/' | relative_url }}) coordinates the
workflow across data preparation, training, evaluation, and deployment. It may
also coordinate batch scoring, monitoring jobs, and retraining. The orchestrator
should describe dependencies and failure handling. It shouldn't hide core
business logic inside scheduler callbacks.

Simon separates batch inference and online serving around 31:15-31:51 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Batch serving looks similar to training. A job loads data, preprocesses it, runs
inference, and stores output.

Online serving changes the architecture because the team must care about request
schemas and response schemas. Latency, fallbacks, and service reliability become
part of the design too. Around 54:15, Simon connects API and logging design to
later monitoring and analytics. Without that logging, the service may look
available while the model behaves badly.

Theofilos gives a Kubernetes-native view around 37:06 and 42:28 in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}),
where Kubeflow Pipelines and KFServing appear as production options. Feast,
Katib, and TFX-style orchestration also appear in that discussion. Treat those
as architecture options, not default requirements. Use them when the team needs
pipeline automation, model serving, metadata, or platform integration at that
level of complexity.

## Monitoring and Feedback

[Model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) should watch
software health and model behavior. Service health, latency, errors, and
resource use show whether the serving path works. Deployment status belongs in
that same view. Input quality and feature distributions show whether production
data still resembles the expected data. Prediction distributions, drift, label
feedback, and business outcomes show whether the model still fits the world.

Danny's monitoring discussion in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
is production-first. At 25:04, he describes the focus on production and model
monitoring. At 27:35, he ties observability back to ETL and data pipelines. At
31:50, he discusses profiling architecture and why summary profiles can support
monitoring without moving every raw row into the monitoring system.

[Thom Ives]({{ '/people/thomives/' | relative_url }}) adds the maintenance view
in
[Feature Engineering, Model Monitoring, and Data Governance]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}).
Around 47:30, he talks about monitoring production models for data drift,
concept drift, and maintenance. The practical release rule is to avoid automatic
retraining until the architecture names the trigger, owner, and approval path.

A drift alert may mean the data pipeline broke. It may also mean the business
changed or the model needs retraining. The feedback loop should route evidence
to someone who can choose the right response.

For the data side of the same problem, see
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}) and
[DataOps]({{ '/wiki/dataops/' | relative_url }}).

## Governance, Lineage, and Ownership

[Governance]({{ '/wiki/governance/' | relative_url }}) belongs in the
architecture when models affect customers, regulated decisions, private data, or
important business processes. It changes what teams log and who can approve a
model. It also changes how long metadata lives and how a team explains a
decision later.

At the architecture level, governance usually means:

- named owners for datasets, model artifacts, services, and alerts
- access control for data, features, artifacts, and logs
- lineage from source data to features, runs, registry entries, and deployments
- visible approval states, retention rules, incident handling, rollback paths,
  and post-incident review practices

Simon discusses regulatory constraints around 39:54 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
then connects security and compliance to metadata, lineage, and GDPR
implications around 42:48-45:50. Raphaël adds data governance as a maturity
concern in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Maria's standardization discussion also matters here. Reusable CI/CD,
repository templates, service principals, and deployment standards make
governance easier because they reduce one-off paths.

For adjacent pages, use
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}),
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
and [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).

## Simple Stack or Shared Platform

Start with a reproducible path for one model. A small architecture can use Git
and a scheduled training job. Add an experiment tracker, object storage, and a
registry convention. One deployment path and prediction logs come next. Add a
basic monitoring view after that.

That's often enough for a startup or a prototype moving into production. It can
also be enough for a team with one important model.

A shared platform makes sense when several teams repeat the same work. Then the
organization benefits from shared templates and self-service compute. Standard
tracking and registry integration become shared assets. Deployment paths,
logging schemas, and monitoring hooks do too. Documentation and support become
part of the platform.

The archive is consistent on this tradeoff. Simon warns against heavy platform
investment before model value exists around 47:08 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Around 49:19, he favors building minimal platform pieces alongside real use.

Raphaël frames a centralized MLOps team as an enabling layer in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
In that discussion, adoption depends on feedback loops and quick wins. Developer
experience matters because adoption is part of the architecture.

Nemanja adds the startup constraint in
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
Use managed tools when they buy speed. Keep an eye on lock-in, technical debt,
security, and future portability.

Use [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}),
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}), and
[MLOps Frameworks]({{ '/guides/mlops-frameworks/' | relative_url }}) when the
main risk is whether teams will use the architecture.

## Architecture Checklist

Before adding another platform component, check whether the current architecture
covers these points:

- Each data input, feature pipeline, training job, model artifact, service, and
  alert has an owner.
- The team can reproduce the model from code, data reference, parameters,
  metrics, and artifact.
- The artifact has a promotion path, approval state, and rollback option.
- CI/CD tests, packages, and deploys the model path repeatably.
- Serving covers the batch jobs, online endpoints, edge targets, or hybrid path
  the product actually uses.
- Logs connect each prediction to a model version, input schema, and serving
  context.
- Monitoring signals trigger investigation, rollback, retraining, or product
  change.
- Governance, lineage, access, retention, and incident practices are visible in
  the architecture.
- Repeated work stays local only when that flexibility is useful.

Good MLOps architecture isn't the largest diagram. It's the smallest production
map that lets a team reproduce a model and deploy it safely. It also lets the
team observe what changes after release, then improve or retire the model when
the evidence demands it.
