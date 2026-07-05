---
layout: wiki
title: "ML Infrastructure"
summary: "Compute, storage, orchestration, serving, monitoring, and platform foundations for production machine learning systems."
related:
  - ML Platforms
  - Platform Engineering
  - AI Infrastructure
  - ai-infrastructure-cost-and-ownership
  - MLOps
  - Model Monitoring
  - Model Registry
  - Orchestration
---

Machine learning infrastructure gives teams the components they need to train
models and run predictions. Those components cover compute and storage, plus
the runtime controls around orchestration and serving. They also cover
monitoring and networking.
It's the technical base for
[[ML Platforms]],
[[MLOps]], and
[[Machine Learning System Design]].

Machine-learning infrastructure work asks what has to exist under ML workloads.
It also asks where those components fail under scale, regulation, latency, or
cost pressure. [[ML Platforms]] owns the shared internal product surface that
turns those components into a supported path for data scientists and ML
engineers. The [[ml-platform-engineer-role=>ML platform engineer role]] sits at
that handoff from infrastructure pieces to a user-facing platform.

The skill set spans cloud infrastructure, notebooks, Kubernetes, and Terraform.
It also covers managed compute, batch inference, online serving, and
orchestration
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Infrastructure is therefore broader than model serving but narrower than the
whole platform product.

[[book:20210927-effective-data-science-infrastructure=>Effective Data Science Infrastructure]]
by Ville Tuulos covers the same compute, orchestration, and serving layers
from the data science side, built around his Metaflow experience.

Vin Vashishta frames the ML architect's infrastructure work as a business
translation role. The architect turns user, customer, and business requirements
into a platform vision. They check whether existing systems can support the work
and estimate what production and maintenance will cost
([[cite:make-money-with-machine-learning-roles-skills@54:50=>ML architecture platform vision]]).
That puts infrastructure decisions close to [[ML Product Manager Role]] because
buy-versus-build and platform reuse can decide whether a model-backed product
deserves funding.

## Infrastructure Baseline

The MLOps toolset also includes release and reproducibility concerns. Those
concerns include experiment tracking and a [[model registry]], serving and
monitoring, and package registries with deployment compatibility
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
Docker, Kubernetes, and Databricks matter here because a model artifact isn't
enough if runtime images and dependencies drift.

Large-model workloads push the same topic toward
[[AI Infrastructure]], especially when
[[ai-infrastructure-cost-and-ownership=>cloud-versus-on-prem cost and GPU
requirements]] dominate.
Distributed-training bottlenecks and Kubernetes limits also matter
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).
Machine learning infrastructure at that scale includes hardware access, network
layout, utilization, and scheduler choice.

## Platform Timing and Scale

The disagreement is less about components than about timing and scale.
Infrastructure work starts when a workload needs reliable compute, storage,
release paths, or runtime ownership. Platform investment pays off later when
teams repeat deployment, serving, governance, and registry work across projects.
Building heavy platform pieces too early is a mistake because real models and
business needs come first
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
For the platform-product side of that decision, see [[ML Platforms]].

A centralized MLOps team reframes adoption by gathering pain points, supporting
product teams, and measuring value before standardizing too much
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]). The
infrastructure succeeds when ML teams use it repeatedly and can trace value back
to release speed, reproducibility, or operational reliability.

For smaller production systems, the boundary sits lower. Start with Lambda and
queues before moving toward Airflow or Kubernetes when the workload doesn't yet
justify heavier [[orchestration]]
([[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]).

Finance regulation can impose the opposite constraint: ML teams may work on
Hadoop and OpenShift rather than self-service cloud. Linux and networking then
become part of the infrastructure skill set. SSH/SCP, firewall requests, and
internal platform behavior matter too
([[cite:mlops-and-ml-engineering-in-finance@27:51=>MLOps and ML Engineering in Finance]]).

Large-model work points the other way. Once
[[ai-infrastructure-cost-and-ownership=>GPU cost and distributed training]]
dominate, normal cloud-managed ML services may no longer be the right operating
model. SLURM-like scheduling and bare-metal provisioning enter the infrastructure
picture
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).

Vashishta adds a roadmap lens to the same infrastructure decision. A platform
purchase may look too expensive for one project but become justified when it
supports several products over one to three years. The architect's job is to
compare existing infrastructure and cloud options. They also compare on-prem
constraints and product roadmap reuse before the team commits to a path
([[cite:make-money-with-machine-learning-roles-skills@58:04=>ML architecture buy vs build]]).

## Compute and GPU Infrastructure

Compute starts with ordinary cloud resources for notebooks, training jobs, and
batch work. AWS, GCP, and Azure are
[[platform engineering]]
skills. Kubernetes, Terraform, and managed compute belong there too
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
The [[developer experience]]
goal is practical: teams need compute access without opening a support ticket
for every run.

In regulated finance, compute can become an on-prem platform constraint. Teams
may run Hadoop and OpenShift instead of elastic cloud services. They may also
request hardware through internal processes. Deployment work has to fit approved
platforms, so infrastructure ownership becomes part of governance
([[cite:mlops-and-ml-engineering-in-finance@27:51=>MLOps and ML Engineering in Finance]]).

Large-model workloads add another layer of GPU requirements. Teams have to handle
PyTorch and NCCL, communication bottlenecks, optimization strategies, and
DeepSpeed
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).
Teams design for network layout, coordinate GPUs, and weigh training
efficiency against the
[[ai-infrastructure-cost-and-ownership=>cost tradeoff between cloud and on-prem
hardware]].

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
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Those systems create the handoff from training to batch inference, online
serving, and audit.

Package registries and dependency compatibility matter because the model
artifact alone isn't enough if the runtime image changes. Python packages and
deployment dependencies can drift too. Container strategy with Docker and
Kubernetes affects reproducibility and team autonomy
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

The simpler production path stores Parquet on S3, Dockerizes training, and
persists model files where later jobs can load them
([[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]).
The team needs stable storage for data, code, and models before it can reason
about [[Reproducibility]].

## Orchestration and Scheduling

Orchestration coordinates training and evaluation, plus inference, retraining,
and data movement. Airflow and pipelines sit inside production workflows, which
links ML infrastructure to
[[data pipelines]] and
[[Batch vs Streaming]]
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Some models need scheduled batch scoring, while others need online inference or
streaming features.

Metaflow is a workflow-tool example. It integrates across AWS, Kubernetes, and
Argo
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).
Data scientists shouldn't have to assemble the cloud and workflow stack from
scratch before they can run a reproducible ML flow.

Kubernetes is useful but not a universal answer because AI workflows may need
SLURM
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).
At the opposite scale, Lambda and queues or simpler schedulers fit when the
workload doesn't justify heavier orchestration
([[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]).

Simulation-heavy work adds a pre-ML boundary. Teams need infrastructure that
moves data to high-performance clusters and retrieves results. They also need to
keep competing client datasets separate before models or pipelines use the
outputs. For those workloads, engineers treat
[[simulation-and-digital-twins=>simulation and digital-twin]] systems as
orchestration work rather than model serving alone
([[cite:from-academic-research-to-data-engineering-freelancing=>Lean Data Consulting]]).

## Serving and Deployment

Serving infrastructure turns trained models into predictions through two
recurring deployment shapes: batch inference and online serving
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Batch inference can run as scheduled jobs. Online serving needs request-time
latency, logging, API contracts, and rollback paths.

A concrete product example chooses between live API calls and precomputed
predictions. It then weighs SageMaker endpoints and cost tradeoffs
([[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]).

Serving is a business and latency decision, not just a framework choice. In LLM
systems, the same serving choice becomes
[[llm-cost-optimization=>LLM cost optimization]]. Token volume and request
latency affect the production operating model. Caching and model selection do
too.

Edge and mobile serving push deployment constraints even further. Offline mobile
models are still a mostly manual deployment space today. Vendors extend
Kubernetes toward edge devices so model and application updates can be scheduled
closer to the user
([[cite:mlops-kubeflow-model-monitoring@51:44=>Kubeflow Model Monitoring]]).
That puts edge deployment beside [[orchestration]], [[Model Monitoring]], and
runtime ownership rather than treating it as only an app packaging problem.

Teams in low-resource healthcare face a clinical infrastructure decision because
connectivity and local hardware can vary. Before a team can claim the model fits
the care setting, it may have to choose between cloud inference and on-device
execution. That ties serving infrastructure to
[[healthcare-ml-validation-and-adoption=>healthcare ML validation]] and local
operations, not only latency. A pediatric monitoring device in a hospital with
intermittent internet may need local inference and local update procedures. Its
runtime also has to fit the rest of the device software
[[cite:building-healthcare-machine-learning-systems@50:50=>Healthcare ML Systems]].

Deployment ties to release discipline, so the MLOps toolset includes CI and
repository structure. It also includes parameterization, tests, and serving
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
Infrastructure should therefore support both the runtime and the release path
that gets code into that runtime.

## Monitoring and Feedback Loops

Monitoring links deployment to maintenance. The core challenge is keeping models
deployed, monitored, and maintained. CI/CD and tests also need ties to
traceability, experiment capture, and monitoring
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
[[Model monitoring]]
belongs on the infrastructure page because the runtime needs logs, metrics,
alerts, and ownership.

Governance and observability requirements also influence infrastructure design.
They include metadata and lineage, GDPR constraints, deletion rules, and unified
prediction schemas
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Prediction logs should support monitoring and analytics, but they also need
security and data-governance controls.

For large AI workloads, monitoring also includes utilization and cost. The
[[ai-infrastructure-cost-and-ownership=>cloud-versus-on-prem tradeoff]]
makes compute ownership an operating concern
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).
GPU clusters can fail as business infrastructure if teams can't see usage,
contention, and idle cost.

## Infrastructure Handoff to Platform Teams

Infrastructure becomes valuable when teams can use it without becoming
infrastructure specialists. A user-centric platform starts from data science
workflows and notebooks, then adds thin abstraction layers over cloud providers
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
The lower layer has to make cloud resources, runtimes, and schedulers reliable.
Images and observability controls have to work too before the platform can
expose them.

The team model behind that experience is a centralized MLOps team supporting
product teams and ML engineers. It starts with CI/CD and tangible pain points
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
[[ai-infrastructure-cost-and-ownership=>Infrastructure ownership]] becomes a
service model, not only a cluster-maintenance job. [[ML Platforms]] covers the
product roadmap, self-service workflow, and adoption side of that service model.

Metaflow shows the open-source developer experience version. Its flow
abstraction sits across AWS, Kubernetes, and Argo
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

AWS, Kubernetes, and Argo still have to work before the abstraction can feel
simple. Storage and execution environments matter too. The user works through a
tool that fits ML workflows. The infrastructure layer keeps the underlying
execution path dependable.

## Related Pages

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
