---
layout: wiki
title: "AI Infrastructure"
summary: "Podcast-grounded reference page for compute, GPUs, orchestration, model serving, cost, and operations behind production AI systems."
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

AI infrastructure covers compute and orchestration. It also covers serving and
operations behind production AI systems. In the DataTalks.Club archive, it overlaps with
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). AI workloads add pressure
from GPUs, large-model serving, and distributed training. They also add
retrieval-heavy applications and cost-sensitive inference.

[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) frames AI
infrastructure through post-ChatGPT cloud costs and on-prem GPU ownership. He
also discusses distributed training in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) adds the production
LLM serving side in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
where model size and compression influence the deployment decision. Latency,
cost, and hosted API risk matter there too.

## Starting Points

Use these pages for the neighboring concepts:

- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Caching]({{ '/wiki/caching/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})

Core podcast discussions:

- [Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}) with [Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }})
- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}) with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}) with [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}) with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
- [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}) with [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }})

## Common Definition

Across these episodes, teams use AI infrastructure to train and adapt AI
models. They also use it to serve, observe, and pay for those models in
production. Andrey Cheptsov makes the
AI-specific version explicit. After ChatGPT, teams began caring more about
infrastructure cost of ownership and cloud-to-on-prem tradeoffs. He then ties
that work to GPU capacity, distributed training, and AI workload schedulers
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
5:27-10:00 and 30:16-34:46).

Simon and Raphaël define the overlapping ML layer. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
places cloud infrastructure and Kubernetes inside the platform discussion. He
also names Terraform and notebooks.

Later he covers experiment tracking and model registries. He connects them to
batch inference, online serving, and orchestration. Metadata and governance
appear in the same discussion
(8:11-10:47 and 28:20-35:26).

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
adds CI/CD, reproducibility, and package registries. He also discusses serving
and monitoring. Containers, Kubernetes, and Databricks appear as pieces that
keep models deployed and maintained (39:06-42:31 and 51:21-57:56).

For LLM systems, infrastructure also includes the serving and data path around
the model. Meryem Arik ties open-source and API choices to control, privacy,
model drift, and serving optimization. She also ties them to latency, cost, and
hardware
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
16:48-25:26 and 49:44-51:35). [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }})
adds production AI engineering concerns around data pipeline testing, Spark
choices, and preprocessing for fine-tuning data. He also covers prompt
evaluation, token optimization, and prompt caching
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
9:05-18:38 and 28:16-31:45).

## Guest Differences

Guests differ on the first bottleneck they optimize. Andrey starts from
infrastructure ownership, with emphasis on cost and GPU availability. He also
covers orchestration and the limits of general-purpose schedulers. His
discussion moves from on-prem economics to PyTorch and NCCL.

Communication bottlenecks, DeepSpeed, Kubernetes, and SLURM appear next. He
then covers GPU coordination and bare-metal provisioning
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
8:25-10:00, 34:46-37:35, and 47:16-56:53).

Simon starts from the platform product. He argues that teams should understand
data science workflows and notebooks before standardizing too much
infrastructure. He also ties platform work to deployment blockers, governance
constraints, and developer experience
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Simon discusses this at 6:55-10:47, 16:52-20:04, and 38:40-45:50. Use
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}) and
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) for
the platform side of that discussion.

Raphaël starts from adoption and operating discipline. His MLOps team supports
product teams, collects pain points, and measures value. The team prioritizes
CI/CD and reproducibility. It also prioritizes serving and monitoring before
chasing a complete tool stack
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
23:01-36:55 and 48:41-57:56).

Meryem starts from deployability and control.
Teams choose among hosted APIs, compressed open-source models, and fine-tuning.
They also choose between retrieval and self-hosting.

Privacy and drift matter, and latency, cost, and hardware matter too.
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
covers this at 16:48-18:46, 23:37-26:30, and 49:44-51:35.

## Compute, GPUs, and Cloud Boundaries

AI infrastructure compute work starts with where jobs run and how much they
cost to keep running. Andrey anchors that question in ownership cost and
cloud-versus-on-prem choices around 5:27-10:00 in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
He later narrows the issue to GPU requirements and distributed training
bottlenecks around 30:16-34:46. Around 54:31-56:53, he turns the same theme
into practical on-prem GPU coordination and bare-metal provisioning.

The platform view is broader but still compute-centered. Simon names cloud
infrastructure and Kubernetes as core platform skills in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
(8:11). He also covers Terraform and self-service compute around 28:20.

Raphaël adds Docker, Kubernetes, and Databricks tradeoffs in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
(56:50). Together, these episodes imply a practical boundary. Small and
standardized workloads can often live on managed platforms. GPU-heavy training
and serving push teams toward scheduling, utilization, and hardware ownership
questions.

## Orchestration and Distributed Training

AI orchestration covers more than pipeline scheduling because it also covers
multi-GPU training jobs and resource contention. Model-serving workloads and
shared compute access matter too. Andrey discusses PyTorch, NCCL, and communication
bottlenecks around 34:46 in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
then discusses optimization strategies and DeepSpeed around 37:35. Around
47:16-50:59, he contrasts Kubernetes, SLURM-like scheduling, and smaller
alternatives for AI workflows.

Classic MLOps orchestration still matters because AI systems depend on data,
training, evaluation, and deployment workflows. Simon covers Airflow and
pipelines around 31:51 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Raphaël covers CI, repository structure, parameterization, and testing around
39:06 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
He then covers reproducibility, dependency management, and package registries
through 53:08. That puts AI infrastructure close to
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}).

## Serving, Deployment, and Latency

Model serving is where users encounter AI infrastructure. Meryem's discussion
of open-source versus API models connects serving to control, privacy, and
hidden API drift. It also connects serving to model size, compression, and
inference optimization
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
16:48-25:26). Her later prototype-versus-production section adds latency, cost,
self-hosting performance, and hardware choices (49:44-51:35).

The same boundary appears in ML platform language. Simon separates batch
inference from online serving around 31:15 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Raphaël includes serving and monitoring in the MLOps toolset around 51:21 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

Bartosz adds an application-engineering example around 41:04 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His Chrome extension discussion uses backend AI integration instead of putting
all AI behavior in the client. Those discussions connect serving to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}), not only to
infrastructure tooling.

## Cost, Efficiency, and Caching

The archive repeatedly ties AI infrastructure to cost. Andrey discusses
infrastructure ownership cost and cloud-versus-on-prem limits around 5:27-10:00
in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
His distributed-training sections then make efficiency a technical issue.
Communication bottlenecks and GPU coordination determine whether more hardware
actually helps. DeepSpeed-style optimization appears in the same discussion
(34:46-37:35 and 54:31-56:53).

Meryem turns cost into a serving decision. API models may be convenient for
prototypes, but self-hosted or optimized open-source models can matter in
production. Privacy and latency drive that choice. Cost and hardware control
drive it too
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
49:44-51:35). Bartosz adds request-level efficiency in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).

Around 28:16-31:45, Bartosz discusses prompt evaluation and prompt compression,
then adds token optimization and prompt caching. That makes
[Caching]({{ '/wiki/caching/' | relative_url }}) part of AI infrastructure when
it reduces model calls, tokens, latency, or load.

## Observability, Governance, and Operations

AI infrastructure must expose logs and metrics, plus lineage and ownership
signals. Teams need those signals to keep systems running after launch. Raphaël defines
the core MLOps challenge as keeping models deployed, monitored, and maintained
around 1:01:58 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Earlier in that episode, he connects reproducibility to data versioning,
traceability, and experiment capture. Dependency management appears in the same
chapter range (42:31-53:08).

Simon adds the governance side. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
metadata and lineage appear around 39:54-45:50. GDPR and security appear there
too. Compliance and API design appear around 54:15. The episode also covers
unified prediction logging there.

Those concerns make observability a design requirement rather than a dashboard
added after deployment. For AI workloads, Andrey's GPU-utilization and on-prem
coordination themes extend observability to infrastructure usage and contention
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
54:31-56:53).

## Relationship to MLOps and AI Engineering

AI infrastructure supplies the runtime substrate. [MLOps]({{ '/wiki/mlops/' | relative_url }})
defines the operating discipline around reproducible releases and registries.
It also covers monitoring, governance, and adoption. [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
uses that substrate to build product behavior with prompts and retrieval. It
also covers fine-tuning, agents, and application integrations.

The episodes make the distinction visible. Simon's platform discussion
describes the shared foundation for models and teams
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
16:52-20:04 and 34:01-38:40). Raphaël explains the operating model for
adoption, CI/CD, and reproducibility
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
23:01-27:56 and 39:06-42:31). He also connects that operating model to
deployment and monitoring.

Meryem and Bartosz show the AI engineering layer, where teams choose between
APIs and open-source models. They also choose between retrieval and
fine-tuning. Prompt optimization and caching appear in the same layer. Backend
integration appears there too
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
40:46-51:35. [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
18:38-31:45 and 41:04).

## See Also

These pages cover the nearby infrastructure, MLOps, and AI engineering topics:

- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Caching]({{ '/wiki/caching/' | relative_url }})
