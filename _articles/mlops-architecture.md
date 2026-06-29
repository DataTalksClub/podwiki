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
predictions. It should also show how teams reproduce and approve the model, then
detect when the system no longer matches reality.

The DataTalks.Club podcast archive treats this architecture as a set of
operating decisions, not a vendor diagram.

Guests return to the same components:

- version control and CI/CD
- experiment tracking and model registries
- serving, monitoring, and compute
- containers and package registries
- data lineage and governance

The architecture earns its keep when each team can see what it owns and which
signal sends a model back for investigation or retraining.

For the broader discipline, start with
[MLOps]({{ '/wiki/mlops/' | relative_url }}). Use
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) for build order and
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) for the shared
platform layer.


## The Architecture in One Flow

A practical MLOps architecture has one main flow and one return path.

The main flow starts with data inputs. Source systems feed ingestion and
transformation jobs, which create features or training datasets. A training
pipeline uses the data, records parameters and metrics, and stores the model
artifact.

A registry or registry-like convention promotes the artifact into a deployable
model. CI/CD packages the code and model service, then deploys either a batch
job or an online endpoint. The team monitors the service, the model, and the
data around it.

The return path starts when production evidence contradicts training-time
assumptions. Drift, data quality issues, latency, and errors can send the team
back to investigation. User feedback or business outcomes can do the same. The
team may fix data, change features, roll back, or retrain. It may also replace
the model or change the product workflow.

That return path matters as much as the forward path. Without it, the
architecture only explains how to launch a model once. It doesn't explain how
the team keeps the model useful.

## Data Inputs and Feature Pipelines

MLOps architecture starts before the model. Data inputs may come from product
events, operational databases, files, and third-party feeds. They may also come
from analytics tables or human labels. The diagram should show ownership and
arrival cadence. It should also show the expected schema and checks for missing
or changed data.

Feature and training pipelines transform those inputs into model-ready data. In
simple systems, the pipeline may be SQL plus a scheduled Python job. In larger
systems, teams may add orchestration and a feature store. Validation checks and
lineage may come next.

The important architectural question isn't whether the diagram uses a feature
store. The team needs to explain how training data and inference data stay
consistent enough for the model's use case. That includes batch and online
inference paths when both exist.

Danny Leybzon makes the upstream dependency explicit in
[MLOps Architect Guide](https://datatalks.club/podcast.html). Around 27:35, he
ties model problems to ETL and data pipelines. He also ties them to drift and
quality. If the monitoring view stops at the model endpoint, the team can miss
the root cause when the source system or feature pipeline changed first.

See [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}) for the
overlap between pipeline reliability and model reliability.

## Training Pipelines and Experiment Tracking

Training architecture connects code and data to parameters, metrics, and model
artifacts.

At minimum, the team needs:

- version control
- a reproducible environment
- a data reference
- saved metrics
- a model artifact

Once several people train models or compare runs, experiment tracking becomes
the shared memory of the system.

Simon Stiebellehner describes experiment tracking as an early platform win in
[Building Production ML Platforms](https://datatalks.club/podcast.html). Around
29:41-30:58, he frames tracking as a move away from spreadsheet run logs toward
shared, transparent model history. He also connects experiment tracking, model
registries, and metadata stores because teams often need those pieces together.

Raphaël Hoogvliets makes the same architecture broader in
[MLOps at Scale](https://datatalks.club/podcast.html). Around 39:06-44:22, the
episode covers CI and repository structure. It also covers parameterization,
testing, data versioning, and traceability. Experiment capture keeps
notebook-era knowledge from disappearing when a model becomes production
software.

See [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) for deeper
archive synthesis.

## Model Registry and Release Gates

A model registry is the handoff point between training and production. It stores
the model artifact and the context needed to use it safely.

A useful registry record should include:

- model version and owner
- artifact location and code version
- training data reference and evaluation result
- approval state and deployment target
- rollback note

The registry doesn't have to be a large product on day one. For a small team, a
structured table plus object storage can be enough if everyone follows the same
promotion rules. For a larger or regulated team, the registry often needs access
control and lineage. Approval history, audit trails, and deployment system
integration may come next.

In [Building Production ML Platforms](https://datatalks.club/podcast.html),
Simon connects the registry to downstream consumption around 30:32. Later in the
same episode, he connects metadata and lineage to reproducibility, plus
governance. The registry turns a training output into a model another job,
service, or team can depend on.

See [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) and
[Governance]({{ '/wiki/governance/' | relative_url }}) for related details.

## CI/CD, Packaging, and Deployment

CI/CD in MLOps architecture should cover ordinary software checks and
model-specific checks. The pipeline may test code and validate data
transformations. It may also package dependencies and build containers. Later
steps can publish model services, run deployment checks, and promote changes
between environments.

Raphaël gives a complete MLOps component set around 52:39 in
[MLOps at Scale](https://datatalks.club/podcast.html). He names version control,
CI/CD, and containerization. He also names model registry and experiment
tracking. Container registry, monitoring, and compute come next. Serving and
package registry round out the list.

That list puts CI/CD next to reproducibility and deployment infrastructure
instead of treating it as a generic software checkbox.

The simplest architecture can start with a repository template and one CI
workflow. That workflow can run tests, build an image, and record how to deploy
or roll back. A platform architecture may add shared templates and environment
promotion. It may also add central registries, self-service deployment paths, and
standard logging hooks. Make the release path repeatable before adding more
tools.

## Serving: Batch, Online, and Hybrid

Serving architecture answers how other systems consume predictions. Batch
serving writes predictions to a table, file, queue, or downstream system on a
schedule. Online serving exposes a model through an API or managed endpoint.
Some systems use both: batch jobs for broad scoring and online endpoints for
fresh decisions.

Simon separates batch inference and online serving in
[Building Production ML Platforms](https://datatalks.club/podcast.html) around
31:15-31:51. His batch example looks similar to training. The job loads data,
pre-processes it, runs inference, and stores output. Online serving changes the
architecture because the team must care about request schemas, response schemas,
latency, and fallbacks. It must also care about service reliability.

Serving also sets up monitoring. Where the use case allows it, the system should
log the model version and request schema. It should also log prediction,
response, latency, and errors.
Around 54:15 in the same episode, Simon connects API and logging design to later
monitoring and analytics. Without that logging, the team may know the service is
up but still not know whether the model is behaving well.

See [Production]({{ '/wiki/production/' | relative_url }}) for broader production
design concerns.

## Monitoring, Feedback Loops, and Retraining

Monitoring architecture should watch both software and model behavior. Service
health, latency, errors, and resource use tell the team whether the serving path
works.

Model behavior needs another set of signals:

- input quality
- feature and prediction distributions
- drift
- label feedback
- business outcomes

Danny's monitoring discussion in
[MLOps Architect Guide](https://datatalks.club/podcast.html) is production-first.
He focuses on deployed models and argues that teams often need to look at the
data pipeline when model behavior changes. Thom Ives adds the maintenance side
in [Feature Engineering, Model Monitoring, and Data Governance](https://datatalks.club/podcast.html).
Models need ongoing oversight because data drift, concept drift, and new
features can change what "best model for production" means.

Don't automate retraining before the architecture names the trigger and the
approval path. A drift alert may mean the data pipeline broke. It may also mean
the business process changed or the model needs retraining. The feedback loop
should route evidence to someone who can choose the right response.

See [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
model-specific monitoring page.

## Governance, Lineage, and Ownership

Governance belongs in the architecture when the model affects customers,
regulated decisions, private data, or important business processes. It shouldn't
be a separate document that appears after deployment. Governance changes what
teams log and which data they keep. It also changes who can approve a model, how
long metadata lives, and how a team explains a decision later.

At the architecture level, governance usually means:

- owners for data, model artifacts, services, and alerts
- access control for datasets, features, model artifacts, and logs
- lineage from source data to features, model runs, registry entries, and
  deployments
- approval states before promotion
- retention and deletion rules for data plus metadata
- incident, rollback, and post-incident review practices

Simon discusses security, compliance, metadata, and lineage in the ML platform
episode. Raphaël adds data governance as a maturity concern in the MLOps at
Scale discussion. The archive gives a practical rule: add governance where the
model lifecycle creates risk. Connect it to the systems teams already use.

See [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) for the data
side and [Governance]({{ '/wiki/governance/' | relative_url }}) for the broader
operating topic.

## Simple Architecture vs Platform Architecture

Start with a reproducible path for one model. That path can use Git, a scheduled
training job, an experiment tracker, and object storage. Add a registry
convention.

Add one deployment path and prediction logs, then add a basic monitoring
dashboard.
That's often enough for a startup, a prototype that's becoming real, or a team
with one production model.

A platform architecture makes sense when several teams repeat the same work.
Then the organization benefits from shared repository templates, self-service
compute, standard tracking, and registry integration. It can also standardize
deployment paths and logging schemas. Monitoring hooks, documentation, and
support can follow.
Platform architecture should reduce repeated work for product teams, not force
every model into a heavy process before the business value is clear.

The archive is consistent on this tradeoff. In
[Building Production ML Platforms](https://datatalks.club/podcast.html), Simon
warns against heavy platform investment before model value exists and favors thin
abstractions that support data scientist workflows. In
[MLOps at Scale](https://datatalks.club/podcast.html), Raphaël frames a
centralized MLOps team as an enabling layer that earns adoption through feedback
loops, quick wins, and developer experience.

Use [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) when the
main risk is whether teams will use the architecture.

## Architecture Checklist

Check these points before you add another platform component:

- Data inputs feed the model and have named owners.
- One pipeline creates training data, features, and inference inputs.
- The team can reproduce the model from code, data reference, parameters,
  metrics, and artifact.
- The model artifact has a storage location and promotion path.
- A CI/CD path tests, packages, and deploys the model.
- The serving path covers batch jobs, online APIs, or both.
- Logs connect a prediction to a model version and input schema.
- Monitoring signals trigger investigation, rollback, retraining, or product
  change.
- Alerting, release approval, and incident ownership have named owners.
- Governance, lineage, access, and retention rules are explicit.
- Move repeat work into a shared platform only when keeping it local creates
  the same friction across teams.

Good MLOps architecture isn't the most complete diagram. It's the smallest
production map that lets the team reproduce a model and deploy it safely. It
also lets the team observe what changes after release, then improve or retire
the model when the evidence demands it.
