---
layout: wiki
title: "ML Infrastructure"
summary: "Compute, storage, orchestration, serving, monitoring, and platform foundations for production machine learning systems."
related:
  - ML Platforms
  - Platform Engineering
  - AI Infrastructure
  - MLOps
  - Model Monitoring
  - Model Registry
  - Orchestration
---

Machine learning infrastructure gives teams the systems they need to train
models and run predictions. Those systems cover compute and storage, plus
orchestration, serving, and monitoring. Across DataTalks.Club discussions, it's
the technical base for
[[ML Platforms]],
[[MLOps]], and
[[Machine Learning System Design]].

Platforms turn that base into a usable path for data scientists and ML
engineers. The infrastructure layer supplies cloud resources, containers, and
GPUs. It also supplies schedulers, registries, runtimes, and observability
controls.

The skill set spans cloud infrastructure, notebooks, Kubernetes, and Terraform.
It also covers managed compute, batch inference, online serving, and
orchestration
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Infrastructure is therefore broader than model serving but narrower than the
whole platform product.

[[book:20210927-effective-data-science-infrastructure=>Effective Data Science Infrastructure]]
by Ville Tuulos covers the same compute, orchestration, and serving layers
from the data science side, built around his Metaflow experience.

The MLOps toolset also includes release and reproducibility concerns. Those
concerns include experiment tracking and a [[model registry]], serving and
monitoring, and package registries with deployment compatibility
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Docker, Kubernetes, and Databricks matter here because a model artifact isn't
enough if runtime images and dependencies drift.

Large-model workloads push the same topic toward
[[AI Infrastructure]], especially when cloud-versus-on-prem cost and GPU
requirements dominate.
Distributed-training bottlenecks and Kubernetes limits also matter
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
Machine learning infrastructure at that scale includes hardware access, network
layout, utilization, and scheduler choice.

## Ownership and Scope

The disagreement is less about components than about timing. Platform investment
pays off when teams repeat deployment, serving, governance, and registry work
across projects. Building heavy platform pieces too early is a mistake because
real models and business needs come first
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Infrastructure is a response to repeated friction, not an up-front shopping list.

A centralized MLOps team reframes adoption by gathering pain points, supporting
product teams, and measuring value before standardizing too much
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). The
infrastructure succeeds when ML teams use it repeatedly and can trace value back
to release speed, reproducibility, or operational reliability.

For smaller production systems, the boundary sits lower. Start with Lambda and
queues before moving toward Airflow or Kubernetes when the workload doesn't yet
justify heavier [[orchestration]]
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]]).

Large-model work points the other way. Once GPU cost and distributed training
dominate, normal cloud-managed ML services may no longer be the right operating
model. SLURM-like scheduling and bare-metal provisioning enter the infrastructure
picture
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

## Compute and GPU Infrastructure

Compute starts with ordinary cloud resources for notebooks, training jobs, and
batch work. AWS, GCP, and Azure are
[[platform engineering]]
skills. Kubernetes, Terraform, and managed compute belong there too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
The [[developer experience]]
goal is practical: teams need compute access without opening a support ticket
for every run.

In regulated finance, compute can become an on-prem platform constraint. Teams
may run Hadoop and OpenShift instead of elastic cloud services. They may also
request hardware through internal processes. Deployment work has to fit approved
platforms, so infrastructure ownership becomes part of governance
([[cite:mlops-and-ml-engineering-in-finance|MLOps and ML Engineering in Finance]]).

Large-model workloads add another layer of GPU requirements. Teams have to handle
PyTorch and NCCL, communication bottlenecks, optimization strategies, and
DeepSpeed
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
Teams design for network layout, coordinate GPUs, and weigh training
efficiency against the cost tradeoff between cloud and on-prem hardware.

This is where [[machine learning system design]]
becomes more than an API and database exercise. A design has to say whether the
model trains on a managed service, a Kubernetes cluster, a Databricks job, or a
GPU pool. It also has to explain when managed compute is enough and when
hardware scheduling becomes a real constraint.

## Storage and Artifact Management

ML infrastructure stores training snapshots and features alongside raw data. It
also stores model files and Docker images. Experiment metadata, prediction logs,
and deployment artifacts belong in the same layer.
This layer ties to
[[experiment tracking]] and model
registries
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Those systems create the handoff from training to batch inference, online
serving, and audit.

Package registries and dependency compatibility matter because the model
artifact alone isn't enough if the runtime image changes. Python packages and
deployment dependencies can drift too. Container strategy with Docker and
Kubernetes affects reproducibility and team autonomy
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

Metaflow is a workflow-tool example. It integrates across AWS, Kubernetes, and
Argo
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).
Data scientists shouldn't have to assemble the cloud and workflow stack from
scratch before they can run a reproducible ML flow.

Kubernetes is useful but not a universal answer because AI workflows may need
SLURM
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
At the opposite scale, Lambda and queues or simpler schedulers fit when the
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

Deployment ties to release discipline, so the MLOps toolset includes CI and
repository structure. It also includes parameterization, tests, and serving
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Infrastructure should therefore support both the runtime and the release path
that gets code into that runtime.

## Monitoring and Feedback Loops

Monitoring links deployment to maintenance. The core challenge is keeping models
deployed, monitored, and maintained. CI/CD and tests also need ties to
traceability, experiment capture, and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
[[Model monitoring]]
belongs on the infrastructure page because the runtime needs logs, metrics,
alerts, and ownership.

Governance and observability requirements also influence infrastructure design.
They include metadata and lineage, GDPR constraints, deletion rules, and unified
prediction schemas
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
workflows and notebooks, then adds thin abstraction layers over cloud providers
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Platform teams use those layers to expose enough control for real work while
hiding repeated setup.

The team model behind that experience is a centralized MLOps team supporting
product teams and ML engineers. It starts with CI/CD and tangible pain points
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Infrastructure ownership becomes a service model, not only a
cluster-maintenance job.

Metaflow shows the open-source developer experience version. Its flow
abstraction sits across AWS, Kubernetes, and Argo
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
