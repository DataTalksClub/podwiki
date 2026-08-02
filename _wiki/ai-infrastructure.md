---
layout: wiki
title: "AI Infrastructure"
summary: "Inference APIs, retrieval, evaluation, tooling, cost, and runtime operations behind LLM and AI product systems."
related:
  - ai-infrastructure-cost-and-ownership
  - Machine Learning Infrastructure
  - MLOps
  - MLOps Tools
  - LLM Production Patterns
  - AI Engineering
  - Orchestration
  - Model Monitoring
  - Caching
---

AI infrastructure covers runtime paths for LLM systems and modern AI products.
It includes hosted inference APIs, self-hosted model serving, retrieval, and
evaluation. It also covers prompt and tool pipelines, cost controls, and the
compute capacity behind those choices. It overlaps with
[[Machine Learning Infrastructure]] and [[MLOps]]. Here, AI product workloads
matter more than the classical ML lifecycle.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Use [[ai-infrastructure-cost-and-ownership=>AI infrastructure cost and ownership]]
for ownership tradeoffs across cloud, on-prem systems, and GPU capacity.
Use [[llm-cost-optimization=>LLM cost optimization]]
for request-level decisions around tokens, caching, compression, and hosted
versus self-hosted serving.

Large AI systems stretch infrastructure in two directions. Training or adapting
large models brings data parallelism and model parallelism into the discussion.
Parameter-server designs belong there too.[[book:20240115-distributed-machine-learning-patterns=>Distributed Machine Learning Patterns]]

Product AI systems add inference APIs, retrieval services, evaluation harnesses,
and prompt compression. They also add tool routing and backend integrations.
Production LLMs also surface model-size and compression choices. They bring
latency concerns, cost concerns, and privacy requirements. The same serving
decision brings hosted API risk and hardware tradeoffs.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Infrastructure Boundary

Teams use AI infrastructure to serve and adapt foundation-model systems in
production. They also use it to observe and pay for those systems. For model
builders, that includes GPU capacity and distributed training. Workload
schedulers and cloud-to-on-prem ownership decisions sit there too.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]].

For product teams, hosted model APIs and self-hosted inference sit beside
retrieval services and evaluation jobs. Pipeline logs connect prompt and tool
behavior to backend systems.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]].

The overlapping classical ML layer includes experiment tracking and model
registries. It also includes batch inference, online serving, and pipeline
orchestration. Those
lifecycle components belong in [[Machine Learning Infrastructure]] and
[[ML Platforms]]. AI infrastructure reuses some of them when they support
retrieval, fine-tuning, evaluation, or serving for AI applications.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

For LLM systems, the serving path includes API versus open-source model choices.
It also includes privacy, model drift, retrieval, and fine-tuning. Data pipeline
testing and prompt evaluation sit in the same operational path. Token
optimization and prompt caching belong there too.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

## Priorities and Tradeoffs

Teams differ on which bottleneck to optimize first. A cost-first view starts
with [[ai-infrastructure-cost-and-ownership=>infrastructure ownership]],
cloud costs, GPU availability, and orchestration limits. It then moves into
PyTorch, NCCL, communication bottlenecks, and DeepSpeed. Scheduling and hardware
work add Kubernetes, SLURM-like scheduling, GPU coordination, and bare-metal
provisioning.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

In a platform-first view, teams start with the product path. They map model
calls, context fetches, output evaluation, and tool handoffs before they
standardize infrastructure. Deployment blockers, governance constraints, and
developer experience guide the platform work.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
Use [[Platform Engineering]] and [[Developer Experience]] for the internal
platform side of that discussion.

Teams use an [[llm-deployment=>LLM deployment]] view to decide how much control
they need. They compare hosted APIs with compressed open-source models. Then
they choose the mix of retrieval, fine-tuning, and self-hosting. Privacy and
model drift guide that choice. Latency, cost, hardware constraints, and hosted
API risk guide it too.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

The [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] turns those
choices into a staged path for retrieval, evaluation, agents, and production
operations.

## Compute, GPUs, and Cloud Boundaries

AI infrastructure compute work starts with where jobs run and how much they cost
to keep running. [[ai-infrastructure-cost-and-ownership=>Ownership cost]]
and cloud-versus-on-prem tradeoffs become concrete when GPU-heavy training and
serving expose distributed-training bottlenecks, GPU coordination problems, and
bare-metal provisioning needs.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

Platform teams keep the compute boundary broader because cloud infrastructure
and Kubernetes belong in the platform skill set. Terraform and self-service
compute belong there too.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
For AI products, those pieces matter when they determine inference capacity and
privacy boundaries. They also affect deployment control, retrieval throughput,
and evaluation throughput.

Small and standardized workloads can often live on managed platforms.
GPU-heavy training and serving push teams toward scheduling and utilization.
They also raise
[[ai-infrastructure-cost-and-ownership=>hardware ownership questions]].[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]][[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Startup-scale managed-service choices need a narrower default. Use
[[lean-mlops-for-startups=>lean MLOps for startups]] before treating platform
ownership as the default.

In edge deployment, hardware fit can matter more than cloud platform choice.
Daniel Egbo's internship example tested models on Intel hardware.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@31:26=>Radio Astronomy to ML]]
That shifted the question from notebook success to whether the model fit the
target deployment environment.
Packaging, GPU availability, and device constraints become part of the model
evaluation surface when the target is edge hardware rather than a generic cloud
endpoint.

Autonomous driving shows the higher-stakes version of the same edge constraint.
In [[camera-first-vs-lidar-autonomous-driving=>Camera-First vs LiDAR Autonomous Driving]],
Aishwarya Jadhav contrasts camera-first systems with multi-sensor stacks. Those
stacks combine cameras, LiDAR, and radar. They also use GPS,
driving-condition metadata, and system responses.
Teams pay for that sensor choice through hardware cost, data volume, on-car
latency, and the validation infrastructure needed before release.
[[cite:from-computer-vision-research-to-autonomous-driving-ai@31:07=>Autonomous Driving AI]]

That connects AI infrastructure to [[Notebook to Production AI Systems]] and to
the portfolio discipline in
[[end-to-end-data-pipeline-project=>end-to-end data pipeline projects]].

Small on-prem devices matter for modest local inference or cost-sensitive
inference.
Abbaspour describes weekend projects where optimized vision-language models can
run slowly on a Raspberry Pi. He also names Nvidia Orin development kits and
Mac Minis as practical local inference hardware. A shared Orin device can lower
occasional coding-help costs for a small team.
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@47:05=>Theme Park to Tesla]][[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@48:53=>Local Inference Cost]]

## Orchestration for AI Workloads

AI orchestration covers pipeline scheduling and multi-GPU training jobs. It also
covers resource contention, model-serving workloads, and shared compute access.
Training jobs bring PyTorch, NCCL, communication bottlenecks, and optimization
strategies into the infrastructure layer. The same discussion covers DeepSpeed.
Scheduling work brings Kubernetes, SLURM-like schedulers, and
smaller AI-workload schedulers into the same boundary.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]].

Product AI orchestration adds a different path for retrieval index refreshes
and prompt-response evaluations. Teams route model calls through tools before
connecting AI services to backend systems. Parameterization and testing still
matter because AI services still need delivery discipline.

Dependency management and package registries matter too. The AI-specific
question is whether orchestration protects product behavior and inference
cost.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:production-ready-ai-engineering=>Production AI Engineering]].
Use [[Orchestration]], [[Reproducibility]], and [[MLOps Tools]] for the shared
workflow layer.

## Serving, Deployment, and Latency

Model serving is where users encounter AI infrastructure. Open-source versus API
models connect serving to control and privacy. They also expose hidden API drift
and model-size constraints. Compression belongs in that serving choice too.
Inference optimization connects serving to latency and cost. It also affects
self-hosting performance and hardware choices.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Those model-size and compression decisions are covered in depth as
[[model-optimization=>Model Optimization]].

Production AI applications also need retrieval paths and backend integration
choices. Prompt evaluation, token optimization, and prompt caching matter too.
Production AI isn't only client-side AI behavior.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
This links serving to [[LLM Production Patterns]], [[AI Engineering]],
[[Retrieval-Augmented Generation]], and infrastructure tooling.

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
treating on-prem inference as a default.
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@49:25=>Small LLMs]][[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@49:38=>Coding Models]]

Request-level efficiency adds prompt evaluation and prompt compression. Token
optimization and prompt caching can reduce model calls and tokens. They can also
reduce latency or load.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
That makes [[Caching]] part of AI infrastructure when it changes serving cost or
capacity. It also connects the infrastructure layer to
[[llm-cost-optimization=>LLM cost optimization]].

## Observability, Governance, and Operations

AI infrastructure needs logs, metrics, traces, and lineage alongside ownership
signals. In product AI, those signals should connect model calls to prompts and
retrieved context. They should also connect tools, backend actions, and
evaluation results. Latency and cost belong in the same signal. Prompt
evaluation, prompt caching, and token optimization become operating concerns
when they change reliability or spend.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Platform governance extends that responsibility. Metadata and lineage sit inside
the platform boundary with unified prediction logging. GDPR and security belong
there too. Compliance and API design also matter when teams need shared model
infrastructure.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

For AI workloads, observability also needs to cover infrastructure usage and
contention. GPU utilization and on-prem coordination make infrastructure
behavior part of the operating signal. Teams should track hosted API behavior
and distributed workload scheduling too.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

## Relationship to MLOps and AI Engineering

AI infrastructure supplies the runtime substrate for LLM and AI product systems.
[[MLOps]] defines the operating discipline around reproducible releases and
registries, plus monitoring, governance, and adoption.
[[AI Engineering]] uses the AI infrastructure layer to build product behavior
with prompts, [[Retrieval-Augmented Generation]], fine-tuning, and agents. Tools
and backend integrations sit in the same product layer.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

Use [[Machine Learning Infrastructure]] for classical ML training and
feature/data pipelines. It also covers registries, batch or online serving, and
monitoring. Use this page when inference APIs, retrieval, evaluation, and tool
use drive the infrastructure question. Model hosting, GPU capacity, and AI
product cost belong here too.
