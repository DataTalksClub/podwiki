---
layout: wiki
title: "AI Infrastructure"
summary: "Compute, GPUs, orchestration, model serving, cost, and operations behind production AI systems."
related:
  - Machine Learning Infrastructure
  - MLOps
  - MLOps Tools
  - LLM Production Patterns
  - AI Engineering
  - Orchestration
  - Model Monitoring
  - Caching
---

AI infrastructure covers compute and orchestration as well as serving and
operations for production AI. It overlaps with
[[Machine Learning Infrastructure]] and [[MLOps]]. AI workloads add GPU pressure
and large-model serving. They also add distributed training, retrieval-heavy
applications, and cost-sensitive inference.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Large AI systems stretch the same platform boundary in several directions.
Training across nodes brings data parallelism and model parallelism into the
infrastructure discussion. It also adds parameter-server designs.[[book:20240115-distributed-machine-learning-patterns=>Distributed Machine Learning Patterns]]
Cloud-native ML platforms add compute, storage, and serving layers. They also
add SageMaker and deployment pipelines.[[book:20210628-data-science-on-aws=>Data Science on AWS]]
Production LLMs add model-size and compression choices. They also surface
latency and cost concerns plus privacy, hosted API risk, and hardware
tradeoffs.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Infrastructure Boundary

AI infrastructure is the shared runtime layer teams use to train and adapt AI
models. Teams also use it to serve, observe, and pay for those models in
production. For foundation-model work, that layer includes GPU capacity and
distributed training. It also includes workload schedulers and cloud-to-on-prem
ownership decisions.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

The overlapping ML platform layer includes cloud infrastructure and Kubernetes.
Terraform and notebooks belong there too. It also includes experiment tracking
and model registries. Metadata and governance sit alongside batch inference and
online serving. Orchestration sits in the same layer.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

That puts [[Experiment Tracking]] and [[Model Registry]] inside the
infrastructure boundary. Governance belongs there when teams need one platform
for data scientists and production services.

Operating discipline belongs in the same boundary. CI/CD and reproducibility
keep models releasable, while package registries support the same release path.
Serving and monitoring keep models maintained after release, with containers,
Kubernetes, and Databricks in the deployment path.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

For LLM systems, the serving path includes API versus open-source model choices.
It also includes privacy, model drift, retrieval, and fine-tuning. Data pipeline
testing and prompt evaluation sit in the same operational path. Token
optimization and prompt caching belong there too.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

## Priorities and Tradeoffs

Teams differ on which bottleneck to optimize first. A cost-first view starts
with infrastructure ownership, cloud costs, GPU availability, and orchestration
limits. It then moves into PyTorch, NCCL, communication bottlenecks, and
DeepSpeed. Scheduling and hardware work add Kubernetes, SLURM-like scheduling,
GPU coordination, and bare-metal provisioning.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

A platform-first view starts with the platform product. Teams need to understand
data science workflows and notebooks before they standardize too much
infrastructure. Deployment blockers and governance constraints then guide the
platform work. Developer experience guides it too.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Use [[Platform Engineering]] and [[Developer Experience]] for the platform side
of that discussion.

A discipline-first view starts with adoption. An MLOps team can support product
teams, collect pain points, and measure value. The same team can prioritize
CI/CD and reproducibility before chasing a complete tool stack. Serving and
monitoring matter in the same sequence.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

An LLM deployment view starts with deployability and control. Teams choose among
hosted APIs and compressed open-source models, then decide whether to use
fine-tuning, retrieval, or self-hosting. Privacy, drift, latency, and cost guide
those choices. Hardware constraints and hosted API risk matter too.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Compute, GPUs, and Cloud Boundaries

AI infrastructure compute work starts with where jobs run and how much they cost
to keep running. Ownership cost and cloud-versus-on-prem tradeoffs become
concrete when GPU-heavy training and serving expose distributed-training
bottlenecks, GPU coordination problems, and bare-metal provisioning needs.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

Platform teams keep the compute boundary broader because cloud infrastructure
and Kubernetes belong in the platform skill set. Terraform and self-service
compute belong there too.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Docker, Kubernetes, and Databricks add more deployment tradeoffs and operations
tradeoffs.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Small and standardized workloads can often live on managed platforms. GPU-heavy
training and serving push teams toward scheduling and utilization. They also
raise hardware ownership questions.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]][[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

In edge deployment, hardware fit can matter more than cloud platform choice.
Daniel Egbo's internship example tested models on Intel hardware
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@31:26=>Radio Astronomy to ML]].
That shifted the question from notebook success to whether the model fit the
target deployment environment.
Packaging, GPU availability, and device constraints become part of the model
evaluation surface when the target is edge hardware rather than a generic cloud
endpoint.
That connects AI infrastructure to [[Notebook to Production AI Systems]] and to
the portfolio discipline in
[[end-to-end-data-pipeline-project=>end-to-end data pipeline projects]].

Small on-prem devices matter for modest local inference or cost-sensitive
inference.
Abbaspour describes weekend projects where optimized vision-language models can
run slowly on a Raspberry Pi. He also names Nvidia Orin development kits and
Mac Minis as practical local inference hardware. A shared Orin device can lower
occasional coding-help costs for a small team
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@47:05=>Theme Park to Tesla]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@48:53=>Local Inference Cost]]).

## Orchestration and Distributed Training

AI orchestration covers pipeline scheduling and multi-GPU training jobs. It also
covers resource contention, model-serving workloads, and shared compute access.
Training jobs bring PyTorch, NCCL, communication bottlenecks, and optimization
strategies into the infrastructure layer. The same discussion covers DeepSpeed.
Scheduling work brings Kubernetes, SLURM-like schedulers, and
smaller AI-workload schedulers into the same boundary.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

Classic MLOps orchestration still matters because AI systems depend on data and
training. They also depend on evaluation and deployment workflows. Airflow and
pipelines connect AI infrastructure to orchestration. CI and repository
structure connect it to orchestration too.

Parameterization, testing, and reproducibility connect it to delivery
discipline. Dependency management and package registries connect it to
[[Orchestration]], [[Reproducibility]], and [[MLOps Tools]].[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Serving, Deployment, and Latency

Model serving is where users encounter AI infrastructure. Open-source versus API
models connect serving to control and privacy. They also expose hidden API drift
and model-size constraints. Compression belongs in that serving choice too.
Inference optimization connects serving to latency and cost. It also affects
self-hosting performance and hardware choices.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Those model-size and compression decisions are covered in depth as
[[Model Optimization]].

ML platform work treats batch inference and online serving as separate platform
concerns. Serving and monitoring also belong in the MLOps toolset.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
Production AI applications also need backend integration choices and prompt
evaluation. Token optimization and prompt caching matter too. Production AI is
not only client-side AI behavior.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
This links serving to [[LLM Production Patterns]] and [[AI Engineering]] as well
as infrastructure tooling.

## Cost, Efficiency, and Caching

AI infrastructure cost starts with ownership and cloud-versus-on-prem limits,
then becomes a technical efficiency problem. Communication bottlenecks and
GPU coordination determine whether more hardware helps. DeepSpeed-style
optimization appears in the same distributed-training discussion.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

Serving cost creates a different tradeoff because API models may fit
prototypes. Production teams may still self-host open-source models. They may
also optimize those models. That can control privacy and latency as well as cost
and hardware.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Local hardware is relevant only when the device fits the model and usage.
Abbaspour ties the on-prem option to smaller specialized models, especially
coding models. He doesn't treat every LLM workload as an edge-hardware
candidate. That boundary keeps [[LLM Production Patterns]] tied to throughput
and latency. It also keeps them tied to privacy and team cost instead of
treating on-prem inference as a default
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@49:25=>Small LLMs]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@49:38=>Coding Models]]).

Request-level efficiency adds prompt evaluation and prompt compression. Token
optimization and prompt caching can reduce model calls and tokens. They can also
reduce latency or load.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
That makes [[Caching]] part of AI infrastructure when it changes serving cost or
capacity.

## Observability, Governance, and Operations

AI infrastructure needs logs, metrics, lineage, and ownership signals. Teams
also need dependency information to keep models deployed, monitored, and
maintained. Reproducibility depends on data versioning and traceability. It also
depends on experiment capture.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Platform governance extends that responsibility. Metadata and lineage sit inside
the platform boundary with unified prediction logging. GDPR and security belong
there too. Compliance and API design also matter when teams need shared model
infrastructure.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

For AI workloads, observability also needs to cover infrastructure usage and
contention. GPU utilization, on-prem coordination, and distributed workload
scheduling make infrastructure behavior part of the operating signal.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

## Relationship to MLOps and AI Engineering

AI infrastructure supplies the runtime substrate. [[MLOps]] defines the
operating discipline around reproducible releases and registries. It also covers
monitoring, governance, and adoption. [[AI Engineering]] uses that substrate to
build product behavior with prompts, [[Retrieval-Augmented Generation]], and
fine-tuning. Agents and application integrations sit in the same
layer.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

Teams use shared infrastructure for compute and serving as well as
orchestration, metadata, and logging. MLOps turns that foundation into
repeatable delivery and operations. AI engineering uses the foundation to choose
between APIs and open-source models.

AI engineering also covers retrieval versus fine-tuning. Prompt optimization
and caching sit in the same application layer. Backend integration patterns sit
there too.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

## Related Pages

Use these pages for nearby infrastructure, MLOps, and AI engineering topics.

- [[Machine Learning Infrastructure]]
- [[MLOps]]
- [[MLOps Tools]]
- [[LLM Production Patterns]]
- [[AI Engineering]]
- [[Orchestration]]
- [[Model Monitoring]]
- [[Caching]]
