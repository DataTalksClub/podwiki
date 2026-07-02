---
layout: wiki
title: "Machine Learning Infrastructure"
summary: "Podcast-grounded reference page for compute, storage, orchestration, serving, monitoring, and platform foundations behind ML systems."
related:
  - ML Platforms
  - Platform Engineering
  - AI Infrastructure
  - MLOps
  - Model Monitoring
  - Model Registry
  - Orchestration
---

Machine learning infrastructure gives teams the compute and storage they need to
train models and run batch jobs. It also covers serving predictions and watching
deployed systems. In the DataTalks.Club podcast archive, it sits behind
[[ML Platforms]],
[[MLOps]], and
[[Machine Learning System Design]].

The platform gives data scientists and ML engineers a usable path. The
infrastructure supplies cloud resources, containers, and GPUs. It also supplies
schedulers, registries, runtimes, and observability controls.

Platform skills span cloud infrastructure and notebooks, Kubernetes and
Terraform, managed compute, batch inference, online serving, and orchestration
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Infrastructure is therefore broader than model serving but narrower than the
whole platform product.

[[book:20210927-effective-data-science-infrastructure|Effective Data Science Infrastructure]]
by Ville Tuulos covers the same compute, orchestration, and serving layers
from the data science side, built around his Metaflow experience.

The MLOps toolset also carries release and reproducibility concerns: experiment
tracking, a [[model registry]], serving, monitoring, package registries, and
deployment compatibility
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Docker, Kubernetes, and Databricks matter here because a model artifact isn't
enough if runtime images and dependencies drift.

Large-model workloads push the same topic toward
[[AI Infrastructure]],
where cloud-versus-on-prem cost, GPU requirements, distributed-training
bottlenecks, and Kubernetes limits dominate
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
Machine learning infrastructure at that scale includes hardware access, network
layout, utilization, and scheduler choice.

## Ownership and Scope

The disagreement is less about components than about timing. Platform investment
pays off when teams repeat deployment, serving, governance, and registry work
across projects, but building heavy platform pieces too early is a mistake — real
models and business needs come first
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Infrastructure is a response to repeated friction, not an up-front shopping list.

Adoption reframes the same decision: a centralized MLOps team gathers pain
points, supports product teams, and measures value before standardizing too much
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). The
infrastructure succeeds when ML teams use it repeatedly and can trace value back
to release speed, reproducibility, or operational reliability.

For smaller production systems the boundary sits lower: start with Lambda and
queues before moving toward Airflow or Kubernetes, applicable when the workload
doesn't yet justify heavier [[orchestration]]
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).

Large-model work points the other way. Once GPU cost and distributed training
dominate, normal cloud-managed ML services may no longer be the right operating
model, and SLURM-like scheduling and bare-metal provisioning enter the
infrastructure picture
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

## Compute and GPU Infrastructure

Compute starts with ordinary cloud resources for notebooks, training jobs, and
batch work. AWS, GCP, and Azure are
[[platform engineering]]
skills, alongside Kubernetes, Terraform, and managed compute
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
The [[developer experience]]
goal is practical: teams need compute access without opening a support ticket
for every run.

Large-model workloads add another layer of GPU requirements, with PyTorch, NCCL,
and communication bottlenecks, plus optimization strategies and DeepSpeed
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
Teams design for network layout and GPU coordination and weigh training
efficiency against the cost tradeoff between cloud and on-prem hardware.

This is where [[machine learning system design]]
becomes more than an API and database exercise. A design has to say whether the
model trains on a managed service, a Kubernetes cluster, a Databricks job, or a
GPU pool. It also has to explain when managed compute is enough and when
hardware scheduling becomes a real constraint.

## Storage and Artifact Management

ML infrastructure stores more than raw data. It stores training data snapshots,
features, model files, and Docker images, plus experiment metadata, prediction
logs, and deployment artifacts. This layer ties to
[[experiment tracking]] and model
registries
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]),
which create the handoff from training to batch inference, online serving, and
audit.

Package registries and dependency compatibility matter because the model
artifact alone isn't enough if the runtime image, Python packages, and deployment
dependencies drift; container strategy with Docker and Kubernetes affects
reproducibility and team autonomy
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

The simpler production path stores Parquet on S3, Dockerizes training, and
persists model files where later jobs can load them
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).
The team needs stable storage for data, code, and models before it can reason
about [[Reproducibility]].

## Orchestration and Scheduling

Orchestration coordinates training and evaluation, plus inference, retraining,
and data movement. Airflow and pipelines sit inside production workflows, which
links ML infrastructure to
[[data pipelines]] and
[[Batch vs Streaming]]
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Some models need scheduled batch scoring, while others need online inference or
streaming features.

Metaflow is a workflow-tool example with integrations across AWS, Kubernetes, and
Argo
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).
The developer-experience point is direct: data scientists shouldn't have to
assemble the full cloud and workflow stack from scratch before they can run a
reproducible ML flow.

Kubernetes is useful but not a universal answer. It has limitations for AI
workflows, where SLURM becomes relevant
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]),
and at the opposite scale, Lambda, queues, or simpler schedulers fit when the
workload doesn't justify heavier orchestration
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).

## Serving and Deployment

Serving infrastructure turns trained models into predictions through two
recurring deployment shapes: batch inference and online serving
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Batch inference can run as scheduled jobs. Online serving needs request-time
latency, logging, API contracts, and rollback paths.

A concrete product example chooses between live API calls and precomputed
predictions, then weighs SageMaker endpoints and cost tradeoffs
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).
Serving is a business and latency decision, not just a framework choice.

Deployment ties to release discipline: CI, repository structure,
parameterization, tests, and serving all sit in the MLOps toolset
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Infrastructure should therefore support both the runtime and the release path
that gets code into that runtime.

## Monitoring and Feedback Loops

Monitoring links deployment to maintenance. The core challenge is keeping models
deployed, monitored, and maintained, with CI/CD and tests tied to traceability,
experiment capture, and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
[[Model monitoring]]
belongs on the infrastructure page because the runtime needs logs, metrics,
alerts, and ownership.

Governance and observability requirements shape infrastructure design too:
metadata and lineage, GDPR constraints, deletion rules, and unified prediction
schemas
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Prediction logs should support monitoring and analytics, but they also need
security and data-governance controls.

For large AI workloads, monitoring also includes utilization and cost. The
cloud-versus-on-prem tradeoff makes compute ownership an operating concern
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
GPU clusters can fail as business infrastructure if teams can't see usage,
contention, and idle cost.

## Platform Ownership and Developer Experience

Infrastructure becomes valuable when teams can use it without becoming
infrastructure specialists. A user-centric platform starts from data science
workflows and notebooks and adds thin abstraction layers over cloud providers
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Platform teams use those layers to expose enough control for real work while
hiding repeated setup.

The team model behind that experience is a centralized MLOps team supporting
product teams and ML engineers, starting with CI/CD and tangible pain points
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Infrastructure ownership becomes a service model, not only a
cluster-maintenance job.

The open-source developer experience version is the Metaflow flow abstraction
sitting across AWS, Kubernetes, and Argo
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).
The infrastructure still exists, but the user works through a tool that fits ML
workflows.

## Related Infrastructure Topics

These pages cover adjacent infrastructure, lifecycle, and operating topics.

- [[ML Platforms]]
- [[MLOps]]
- [[AI Infrastructure]]
- [[Platform Engineering]]
- [[Developer Experience]]
- [[Orchestration]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Reproducibility]]
- [[Machine Learning System Design]]
- [[Production]]
