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

AI infrastructure covers the compute, orchestration, serving, and operating
systems behind production AI. In DataTalks.Club podcast discussions, it overlaps
with
[[Machine Learning Infrastructure]]
and [[MLOps]]. AI workloads add pressure
from GPUs, large-model serving, and distributed training. They also add
retrieval-heavy applications and cost-sensitive inference.

[[person:andreycheptsov|Andrey Cheptsov]] frames AI
infrastructure through post-ChatGPT cloud costs and on-prem GPU ownership. He
also discusses distributed training in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]].
[[person:meryemarik|Meryem Arik]] adds the production
LLM serving side in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
where model size and compression influence the deployment decision. Latency,
cost, and hosted API risk matter there too.
Yuan Tang's
[[book:20240115-distributed-machine-learning-patterns|Distributed Machine Learning Patterns]]
catalogs the distributed-training architectures that underlie Andrey's GPU and
scheduling discussion: data parallelism, model parallelism, and parameter-server
patterns for scaling training across nodes.

For cloud-native ML infrastructure, [[book:20210628-data-science-on-aws|Data Science on AWS]] by Chris Fregly and Antje Barth covers the AWS-side implementation of these same compute, storage, and serving layers, from SageMaker through deployment pipelines.

## Production Infrastructure Scope

Across these episodes, teams use AI infrastructure to train and adapt AI
models. They also use it to serve, observe, and pay for those models in
production. Andrey Cheptsov makes the AI-specific version explicit. After
ChatGPT, teams began caring more about infrastructure cost of ownership and
cloud-to-on-prem tradeoffs. He then ties that work to GPU capacity, distributed
training, and AI workload schedulers
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
5:27-10:00 and 30:16-34:46).

Simon and Raphaël define the overlapping ML layer. In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[person:simonstiebellehner|Simon Stiebellehner]]
places cloud infrastructure and Kubernetes inside the platform discussion. He
also names Terraform and notebooks.

Later he covers experiment tracking and model registries. He connects them to
batch inference, online serving, and orchestration. That places
[[Experiment Tracking]],
[[Model Registry]], metadata, and
governance inside the infrastructure boundary (8:11-10:47 and 28:20-35:26).

In
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
[[person:raphaelhoogvliets|Raphaël Hoogvliets]]
adds CI/CD, reproducibility, and package registries. He also discusses serving
and monitoring. Containers, Kubernetes, and Databricks appear as pieces that
keep models deployed and maintained (39:06-42:31 and 51:21-57:56).

For LLM systems, infrastructure also includes the serving and data path around
the model. Meryem Arik ties open-source and API choices to control, privacy,
model drift, and serving optimization. She also ties them to latency, cost, and
hardware
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
16:48-25:26 and 49:44-51:35). [[person:bartoszmikulski|Bartosz Mikulski]]
adds production AI engineering concerns around data pipeline testing, Spark
choices, and preprocessing for fine-tuning data. He also covers prompt
evaluation, token optimization, and prompt caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-18:38 and 28:16-31:45).

## Infrastructure Priorities

The podcast discussions differ less on definition than on the first bottleneck
to optimize. Andrey starts from infrastructure ownership, with emphasis on cost
and GPU availability. He also covers orchestration and the limits of
general-purpose schedulers. His discussion moves from on-prem economics to
PyTorch and NCCL.

Communication bottlenecks, DeepSpeed, Kubernetes, and SLURM appear next. He
then covers GPU coordination and bare-metal provisioning
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
8:25-10:00, 34:46-37:35, and 47:16-56:53).

Simon starts from the platform product. He argues that teams should understand
data science workflows and notebooks before standardizing too much
infrastructure. He also ties platform work to deployment blockers, governance
constraints, and developer experience
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Simon discusses this at 6:55-10:47, 16:52-20:04, and 38:40-45:50. Use
[[Platform Engineering]] and
[[Developer Experience]] for
the platform side of that discussion.

Raphaël starts from adoption and operating discipline. His MLOps team supports
product teams, collects pain points, and measures value. The team prioritizes
CI/CD and reproducibility. It also prioritizes serving and monitoring before
chasing a complete tool stack
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
23:01-36:55 and 48:41-57:56).

Meryem starts from deployability and control.
Teams choose among hosted APIs, compressed open-source models, and fine-tuning.
They also choose between retrieval and self-hosting.

Privacy and drift matter, and latency, cost, and hardware matter too.
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
covers this at 16:48-18:46, 23:37-26:30, and 49:44-51:35.

## Compute, GPUs, and Cloud Boundaries

AI infrastructure compute work starts with where jobs run and how much they
cost to keep running. Andrey anchors that question in ownership cost and
cloud-versus-on-prem choices around 5:27-10:00 in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]].
He later narrows the issue to GPU requirements and distributed training
bottlenecks around 30:16-34:46. Around 54:31-56:53, he turns the same theme
into practical on-prem GPU coordination and bare-metal provisioning.

The platform view is broader but still compute-centered. Simon names cloud
infrastructure and Kubernetes as core platform skills in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
(8:11). He also covers Terraform and self-service compute around 28:20.

Raphaël adds Docker, Kubernetes, and Databricks tradeoffs in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]
(56:50). Together, these episodes imply a practical boundary. Small and
standardized workloads can often live on managed platforms. GPU-heavy training
and serving push teams toward scheduling, utilization, and hardware ownership
questions.

## Orchestration and Distributed Training

AI orchestration covers more than pipeline scheduling because it also covers
multi-GPU training jobs and resource contention. Model-serving workloads and
shared compute access matter too. Andrey discusses PyTorch, NCCL, and
communication bottlenecks around 34:46 in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
then discusses optimization strategies and DeepSpeed around 37:35. Around
47:16-50:59, he contrasts Kubernetes, SLURM-like scheduling, and smaller
alternatives for AI workflows.

Classic MLOps orchestration still matters because AI systems depend on data,
training, evaluation, and deployment workflows. Simon covers Airflow and
pipelines around 31:51 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Raphaël covers CI, repository structure, parameterization, and testing around
39:06 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
He then covers reproducibility, dependency management, and package registries
through 53:08. That puts AI infrastructure close to
[[Orchestration]],
[[Reproducibility]], and
[[MLOps Tools]].

## Serving, Deployment, and Latency

Model serving is where users encounter AI infrastructure. Meryem's discussion
of open-source versus API models connects serving to control, privacy, and
hidden API drift. It also connects serving to model size, compression, and
inference optimization
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
16:48-25:26). Her later prototype-versus-production section adds latency, cost,
self-hosting performance, and hardware choices (49:44-51:35).

Those model size and compression decisions are covered in depth as
[[Model Optimization]].

The same boundary appears in ML platform language. Simon separates batch
inference from online serving around 31:15 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Raphaël includes serving and monitoring in the MLOps toolset around 51:21 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].

Bartosz adds an application-engineering example around 41:04 in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His Chrome extension discussion uses backend AI integration instead of putting
all AI behavior in the client. Those discussions connect serving to
[[LLM Production Patterns]]
and [[AI Engineering]], not only to
infrastructure tooling.

## Cost, Efficiency, and Caching

These episodes repeatedly tie AI infrastructure to cost. Andrey discusses
infrastructure ownership cost and cloud-versus-on-prem limits around 5:27-10:00
in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]].
His distributed-training sections then make efficiency a technical issue.
Communication bottlenecks and GPU coordination determine whether more hardware
actually helps. DeepSpeed-style optimization appears in the same discussion
(34:46-37:35 and 54:31-56:53).

Meryem turns cost into a serving decision. API models may be convenient for
prototypes, but self-hosted or optimized open-source models can matter in
production. Privacy and latency drive that choice. Cost and hardware control
drive it too
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
49:44-51:35). Bartosz adds request-level efficiency in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].

Around 28:16-31:45, Bartosz discusses prompt evaluation and prompt compression,
then adds token optimization and prompt caching. That makes
[[Caching]] part of AI infrastructure when
it reduces model calls, tokens, latency, or load.

## Observability, Governance, and Operations

AI infrastructure must expose logs and metrics, plus lineage and ownership
signals. Teams need those signals to keep systems running after launch. Raphaël
defines the core MLOps challenge as keeping models deployed, monitored, and
maintained around 1:01:58 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
Earlier in that episode, he connects reproducibility to data versioning,
traceability, and experiment capture. Dependency management appears in the same
chapter range (42:31-53:08).

Simon adds the governance side. In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
metadata and lineage appear around 39:54-45:50. GDPR and security appear there
too. Compliance and API design appear around 54:15. The episode also covers
unified prediction logging there.

Those concerns make observability a design requirement rather than a dashboard
added after deployment. For AI workloads, Andrey's GPU-utilization and on-prem
coordination themes extend observability to infrastructure usage and contention
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
54:31-56:53).

## Relationship to MLOps and AI Engineering

AI infrastructure supplies the runtime substrate. [[MLOps]]
defines the operating discipline around reproducible releases and registries.
It also covers monitoring, governance, and adoption. [[AI Engineering]]
uses that substrate to build product behavior with prompts and
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].
It also covers fine-tuning, agents, and application integrations.

The episodes make the distinction visible. Simon's platform discussion
describes the shared foundation for models and teams
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
16:52-20:04 and 34:01-38:40). Raphaël explains the operating model for
adoption, CI/CD, and reproducibility
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
23:01-27:56 and 39:06-42:31). He also connects that operating model to
deployment and monitoring.

Meryem and Bartosz show the AI engineering layer, where teams choose between
APIs and open-source models. They also choose between retrieval and
fine-tuning. Prompt optimization and caching appear in the same layer. Backend
integration appears there too
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
40:46-51:35.
[[podcast:production-ready-ai-engineering|Production AI Engineering]]
adds the Bartosz examples at
18:38-31:45 and 41:04).

## Related Infrastructure Topics

These pages cover the nearby infrastructure, MLOps, and AI engineering topics:

- [[Machine Learning Infrastructure]]
- [[MLOps]]
- [[MLOps Tools]]
- [[LLM Production Patterns]]
- [[AI Engineering]]
- [[Orchestration]]
- [[Model Monitoring]]
- [[Caching]]
