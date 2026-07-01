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

Machine learning infrastructure gives teams the compute and storage they need
to train models. It also covers orchestration, serving, and monitoring for
models that keep running after deployment. DataTalks.Club guests discuss it as
the foundation behind [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}).

The platform gives data scientists and ML engineers a usable path. The
infrastructure supplies cloud services, containers, and GPUs. It also supplies
schedulers, registries, and runtime controls.

Guests connect infrastructure to specific work instead of treating it as a
generic tool list. Teams need to provision compute and store artifacts. They
also need to deploy batch and online models, keep dependencies reproducible, and
operate systems that other teams can use.

## Common Definition

Machine learning infrastructure means the shared technical
foundation for model development and operation. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
names cloud infrastructure and Kubernetes as platform
skills around 8:11. He also names Terraform and notebooks.

Around 28:20, he adds managed compute and batch inference alongside online
serving and orchestration. His definition makes infrastructure broader than
model serving but narrower than the whole platform product.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
adds the release and reproducibility side. Around 51:21,
he includes experiment tracking and a [model registry]({{ '/wiki/model-registry/' | relative_url }})
in the MLOps toolset. He also includes serving and monitoring.

Around 53:08, Raphaël connects
package registries to deployment compatibility. Around 56:50, he extends that
discussion to Docker, Kubernetes, and Databricks. Dependency management belongs
in the infrastructure layer, not only in developer habits.

[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})
pushes the same definition into large-model workloads. [Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) covers
cloud versus on-prem costs around 8:25. He then covers GPU requirements around
30:16, distributed-training bottlenecks around 34:46, and Kubernetes limits
around 47:16. For those workloads,
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) and
machine learning infrastructure overlap.

## Guest Differences

Guests differ on how much infrastructure a team should own.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
argues for platform investment when teams repeat deployment work across
projects. The same argument applies when teams repeat governance and registry
work. It also applies to repeated serving work. He warns that teams should have
real models and business needs before they invest heavily in platform pieces
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
16:52 and 47:08).

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) frames infrastructure through adoption. His centralized
MLOps team gathers pain points and gives support. It also measures value before
standardizing too much
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
23:01, 27:56, and 36:55). For him, infrastructure succeeds when product teams
use it repeatedly, not when the stack is technically complete.

[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) puts more
weight on cost, hardware access, and orchestration limits. His post-ChatGPT
discussion starts with cloud spend and ownership.

It then moves into on-prem GPUs and distributed training. The same episode also
covers SLURM-like scheduling and bare-metal provisioning
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
5:27 and 47:16). It also covers GPU coordination and bare-metal provisioning
around 54:31 and 56:53. That view matters when the workload outgrows
normal cloud-managed ML services.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the pragmatic smaller-system boundary in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 41:06, he recommends starting simple with Lambda, queues, or managed
services before moving toward Airflow or Kubernetes. That advice keeps
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}) tied to workload
complexity instead of tool fashion.

## Compute and GPU Infrastructure

Compute starts with ordinary cloud resources for notebooks and training jobs.
It also covers batch work.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
names AWS, GCP, and Azure as
platform-engineering skills around 8:11 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He also names Kubernetes and Terraform.
Around 28:20, he adds managed compute.

That connects this page to
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}) and
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}):
teams need compute access without opening a support ticket for every run.

Large-model workloads add another layer. Andrey Cheptsov discusses GPU
requirements and distributed-training challenges around 30:16 in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
Around 34:46, he names PyTorch, NCCL, and communication bottlenecks.

Around 37:35, he discusses optimization strategies and DeepSpeed. For that
workload,
teams need to design for network layout and GPU coordination. They also need to
weigh training efficiency against the cost tradeoff between cloud and on-prem
hardware.

This is where [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
becomes more than an API and database exercise. The design needs to say whether
the model trains on a managed service, a Kubernetes cluster, a Databricks job,
or a GPU pool. It also needs to explain when the workload is small enough for
managed compute and when hardware scheduling becomes a real system constraint.

## Storage and Artifact Management

ML infrastructure stores more than raw data. It stores training data snapshots,
features, model files, and Docker images. It also stores experiment metadata,
prediction logs, and deployment artifacts. Simon Stiebellehner ties this layer to experiment
tracking around 29:41 and model registries around 30:32 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Those services create the handoff from training to batch inference, online
serving, and audit.

Raphaël Hoogvliets adds package registries and dependency compatibility around
53:08 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
The model artifact alone isn't enough if the runtime image, Python packages,
and deployment dependencies drift. Docker and Kubernetes show up in the same
episode around 56:50 because container strategy affects reproducibility and
team autonomy.

Andreas Kretz shows the simpler production path around 25:36 and 34:16 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
He stores Parquet on S3, Dockerizes training, and persists model files where
later jobs can load them. The team needs stable storage for data, code, and
models before it can reason about
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}).

## Orchestration and Scheduling

Orchestration coordinates training and evaluation. It also covers inference and
retraining as well as data movement. Simon Stiebellehner discusses Airflow and pipelines around
31:51 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He connects them to production workflows.

That orchestration work connects ML infrastructure to
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) and
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}).
Some models need scheduled batch scoring. Others need online inference or
streaming features.

Hugo Bowne-Anderson gives a workflow-tool example through Metaflow in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
Around 13:52, he discusses integrations with AWS, Kubernetes, and Argo. The
developer-experience point is direct. Data scientists shouldn't have to
assemble the full cloud and workflow stack from scratch
before they can run a reproducible ML flow.

Kubernetes is useful, but guests don't treat it as a universal answer.
Andrey Cheptsov discusses Kubernetes limitations for AI workflows and SLURM
around 47:16 in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
Andreas Kretz makes the opposite-scale point around 41:06 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Start with Lambda, queues, or simpler schedulers when the workload doesn't
justify heavier orchestration.

## Serving and Deployment

Serving infrastructure turns trained models into predictions. Guests use
two recurring deployment shapes: batch inference and online serving. Simon
Stiebellehner discusses this split around 31:15 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Batch inference can run as scheduled jobs. Online serving needs request-time
latency, logging, API contracts, and rollback paths.

Andreas Kretz gives a concrete product example around 31:33 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
He chooses between live API calls and precomputed predictions. Around 37:53, he
also discusses SageMaker endpoints and cost tradeoffs. That makes serving a
business and latency decision, not just a framework choice.

Raphaël Hoogvliets connects deployment to release discipline in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Around 39:06, he covers CI and repository structure. He also covers
parameterization and tests.
Around 51:21, he includes serving in the MLOps toolset. Infrastructure should
therefore support both the runtime and the release path that gets code into
that runtime.

## Monitoring and Feedback Loops

Monitoring connects deployment to maintenance. Raphaël Hoogvliets describes
the core challenge as keeping models deployed, monitored, and maintained around
1:01:58 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
His earlier chapters connect CI/CD and tests to traceability, experiment
capture, and monitoring. [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
belongs on the infrastructure page because the runtime needs logs, metrics,
alerts, and ownership.

Simon Stiebellehner adds governance and observability requirements around
42:48, 45:50, and 54:15 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Metadata and lineage affect infrastructure design. GDPR constraints, deletion
rules, and unified prediction schemas do too. Prediction logs should support
monitoring and analytics, but they also need security and data-governance
controls.

For large AI workloads, monitoring also includes utilization and cost. Andrey
Cheptsov's cloud-versus-on-prem discussion around 8:25 in
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})
frames compute ownership as an operating concern. GPU clusters can fail as
business infrastructure if teams can't see usage, contention, and idle cost.

## Platform Ownership and Developer Experience

Infrastructure becomes valuable when teams can use it without becoming
infrastructure specialists. Simon Stiebellehner's user-centric platform
discussion around 10:47 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
starts from data science workflows and notebooks. Around 38:40, he describes
thin abstraction layers over cloud providers. Platform teams use those layers
to expose enough control for real work while hiding repeated setup.

Raphaël Hoogvliets describes the team model behind that experience. Around
23:01 and 25:20 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
the centralized MLOps team supports product teams and ML engineers. Around
48:41, he recommends starting with CI/CD and tangible pain points. That turns
infrastructure ownership into a service model, not only a cluster-maintenance
job.

Hugo Bowne-Anderson's Metaflow discussion gives the open-source developer
experience version. Around 2:14 and 13:52 in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
the flow abstraction sits across AWS, Kubernetes, and Argo. The infrastructure
still exists, but the user works through a tool that fits ML workflows.

## Related Pages

These pages cover adjacent infrastructure, lifecycle, and operating topics.

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
