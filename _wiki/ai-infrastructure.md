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

[[person:andreycheptsov=>Andrey Cheptsov]] frames AI
infrastructure through post-ChatGPT cloud costs and on-prem GPU ownership. He
also discusses distributed training
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
[[person:meryemarik=>Meryem Arik]] adds the production
LLM serving side in [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
where model size and compression influence the deployment decision. Latency,
cost, and hosted API risk matter there too.

Yuan Tang's
[[book:20240115-distributed-machine-learning-patterns=>Distributed Machine Learning Patterns]]
catalogs the distributed-training architectures that underlie Andrey's GPU and
scheduling discussion. Those architectures include data parallelism, model
parallelism, and parameter-server patterns for scaling training across nodes.

Chris Fregly and Antje Barth cover cloud-native ML infrastructure in [[book:20210628-data-science-on-aws|Data Science on AWS]]. Their AWS-side
discussion includes compute, storage, and serving layers. It also includes
SageMaker and deployment pipelines.

## Production Infrastructure Scope

Across these episodes, teams use AI infrastructure to train and adapt AI
models. They also use it to serve, observe, and pay for those models in
production. Andrey Cheptsov makes the AI-specific version explicit. After
ChatGPT, teams began caring more about infrastructure cost of ownership and
cloud-to-on-prem tradeoffs. He then ties that work to GPU capacity, distributed
training, and AI workload schedulers
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

Simon and Raphaël define the overlapping ML layer. In [[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[person:simonstiebellehner=>Simon Stiebellehner]]
places cloud infrastructure and Kubernetes inside the platform discussion. He
also names Terraform and notebooks.

Later he covers experiment tracking and model registries. He connects them to
batch inference, online serving, and orchestration. That places
[[Experiment Tracking]],
[[Model Registry]], metadata, and
governance inside the infrastructure boundary.

In [[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
[[person:raphaelhoogvliets=>Raphaël Hoogvliets]]
adds CI/CD, reproducibility, and package registries. He also discusses serving
and monitoring. Containers, Kubernetes, and Databricks appear as pieces that
keep models deployed and maintained.

For LLM systems, infrastructure also includes the serving and data path around
the model. Meryem Arik ties open-source and API choices to control, privacy,
model drift, and serving optimization. She also ties them to latency, cost, and
hardware
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]). [[person:bartoszmikulski|Bartosz Mikulski]]
adds production AI engineering concerns around data pipeline testing, Spark
choices, and preprocessing for fine-tuning data. He also covers prompt
evaluation, token optimization, and prompt caching
([[cite:production-ready-ai-engineering|Production AI Engineering]]).

## Infrastructure Priorities

The podcast discussions differ less on definition than on the first bottleneck
to optimize. Andrey starts from infrastructure ownership, with emphasis on cost
and GPU availability. He also covers orchestration and the limits of
general-purpose schedulers. His discussion moves from on-prem economics to
PyTorch and NCCL.

Communication bottlenecks, DeepSpeed, Kubernetes, and SLURM appear next. He
then covers GPU coordination and bare-metal provisioning
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

Simon starts from the platform product. He argues that teams should understand
data science workflows and notebooks before standardizing too much
infrastructure. He also ties platform work to deployment blockers, governance
constraints, and developer experience
([[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]). Use
[[Platform Engineering]] and
[[Developer Experience]] for
the platform side of that discussion.

Raphaël starts from adoption and operating discipline. His MLOps team supports
product teams, collects pain points, and measures value. The team prioritizes
CI/CD and reproducibility. It also prioritizes serving and monitoring before
chasing a complete tool stack
([[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

Meryem starts from deployability and control.
Teams choose among hosted APIs, compressed open-source models, and fine-tuning.
They also choose between retrieval and self-hosting.

Privacy and drift matter, and latency, cost, and hardware matter too. [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
covers those deployment tradeoffs.

## Compute, GPUs, and Cloud Boundaries

AI infrastructure compute work starts with where jobs run and how much they
cost to keep running. Andrey anchors that question in ownership cost and
cloud-versus-on-prem choices
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
He later narrows the issue to GPU requirements and distributed training
bottlenecks, then turns the same theme into practical on-prem GPU coordination
and bare-metal provisioning.

The platform view is broader but still compute-centered. Simon names cloud
infrastructure and Kubernetes as core platform skills in [[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He also covers Terraform and self-service compute.

Raphaël adds Docker, Kubernetes, and Databricks tradeoffs in [[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
Together, these episodes imply a practical boundary. Small and
standardized workloads can often live on managed platforms. GPU-heavy training
and serving push teams toward scheduling, utilization, and hardware ownership
questions.

Daniel Egbo adds an edge-deployment version of the same boundary [[cite:from-radio-astronomy-to-machine-learning-and-data-engineering|From Radio Astronomy to Machine Learning and Data Engineering]].
His internship work tested models on Intel hardware. The example frames
infrastructure as model-to-device fit, not only cloud-platform choice.

## Orchestration and Distributed Training

AI orchestration covers more than pipeline scheduling because it also covers
multi-GPU training jobs and resource contention. Model-serving workloads and
shared compute access matter too. Andrey discusses PyTorch, NCCL, and
communication bottlenecks. He then moves to optimization strategies and
DeepSpeed. He also contrasts Kubernetes with SLURM-like scheduling and smaller
alternatives for AI workflows
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

Classic MLOps orchestration still matters because AI systems depend on data,
training, evaluation, and deployment workflows. Simon covers Airflow and
pipelines in [[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].

Raphaël covers CI, repository structure, parameterization, and testing in [[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
He then covers reproducibility, dependency management, and package registries
there too. That puts AI infrastructure close to
[[Orchestration]],
[[Reproducibility]], and
[[MLOps Tools]].

## Serving, Deployment, and Latency

Model serving is where users encounter AI infrastructure. Meryem's discussion
of open-source versus API models connects serving to control, privacy, and
hidden API drift. It also connects serving to model size, compression, and
inference optimization
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Her later prototype-versus-production section adds latency, cost,
self-hosting performance, and hardware choices.

Those model size and compression decisions are covered in depth as
[[Model Optimization]].

The same boundary appears in ML platform language. Simon separates batch
inference from online serving in [[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].

Raphaël includes serving and monitoring in the MLOps toolset in [[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].

Bartosz adds an application-engineering example in [[cite:production-ready-ai-engineering|Production AI Engineering]].
His Chrome extension discussion uses backend AI integration instead of putting
all AI behavior in the client. Those discussions connect serving to
[[LLM Production Patterns]]
and [[AI Engineering]], not only to
infrastructure tooling.

## Cost, Efficiency, and Caching

These episodes repeatedly tie AI infrastructure to cost. Andrey discusses
infrastructure ownership cost and cloud-versus-on-prem limits
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).
His distributed-training sections then make efficiency a technical issue.
Communication bottlenecks and GPU coordination determine whether more hardware
actually helps. DeepSpeed-style optimization appears in the same discussion.

Meryem turns cost into a serving decision. API models may be convenient for
prototypes, but self-hosted or optimized open-source models can matter in
production. Privacy and latency drive that choice. Cost and hardware control
drive it too
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]). Bartosz adds request-level efficiency in [[cite:production-ready-ai-engineering|Production AI Engineering]].

Bartosz discusses prompt evaluation and prompt compression, then adds token
optimization and prompt caching. That makes
[[Caching]] part of AI infrastructure when
it reduces model calls, tokens, latency, or load.

## Observability, Governance, and Operations

AI infrastructure must expose logs and metrics, plus lineage and ownership
signals. Teams need those signals to keep systems running after launch. Raphaël
defines the core MLOps challenge as keeping models deployed, monitored, and
maintained
([[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Earlier in that episode, he connects reproducibility to data versioning,
traceability, and experiment capture. Dependency management appears in the same
chapter range.

Simon adds the governance side. In [[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
metadata, lineage, and unified prediction logging all sit inside the platform
responsibility. GDPR, security, compliance, and API design do too.

Those concerns make observability a design requirement rather than a dashboard
added after deployment. For AI workloads, Andrey's GPU-utilization and on-prem
coordination themes extend observability to infrastructure usage and contention
([[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

## Relationship to MLOps and AI Engineering

AI infrastructure supplies the runtime substrate. [[MLOps]]
defines the operating discipline around reproducible releases and registries.
It also covers monitoring, governance, and adoption. [[AI Engineering]]
uses that substrate to build product behavior with prompts and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].
It also covers fine-tuning, agents, and application integrations.

The episodes make the distinction visible. Simon's platform discussion
describes the shared foundation for models and teams
([[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Raphaël explains the operating model for
adoption, CI/CD, and reproducibility
([[cite:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). He also connects that operating model to
deployment and monitoring.

Meryem and Bartosz show the AI engineering layer, where teams choose between
APIs and open-source models. They also choose between retrieval and
fine-tuning. Prompt optimization and caching appear in the same layer. Backend
integration appears there too
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]), while [[cite:production-ready-ai-engineering|Production AI Engineering]] adds the Bartosz examples.

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
