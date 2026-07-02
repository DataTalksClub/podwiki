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

[[person:simonstiebellehner|Simon Stiebellehner]]
sets a useful boundary in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Around 8:11, he names cloud infrastructure and notebooks as platform skills. He
also names Kubernetes and Terraform. Around 28:20, he adds managed compute.

He also adds batch inference, online serving, and orchestration. Infrastructure
is therefore broader than model serving but narrower than the whole platform
product.

[[book:20210927-effective-data-science-infrastructure|Effective Data Science Infrastructure]]
by Ville Tuulos covers the same compute, orchestration, and serving layers
from the data science side, built around his Metaflow experience.

[[person:raphaelhoogvliets|Raphaël Hoogvliets]]
adds release and reproducibility concerns in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
Around 51:21, he includes experiment tracking and a
[[model registry]] in the MLOps
toolset. He also includes serving and monitoring. Around 53:08 and 56:50, he
expands the discussion to package registries and deployment compatibility.
Docker, Kubernetes, and Databricks matter in that discussion because a model
artifact isn't enough if runtime images and dependencies drift.

Large-model workloads push the same topic toward
[[AI Infrastructure]].
In
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
[[person:andreycheptsov|Andrey Cheptsov]] discusses
cloud versus on-prem costs around 8:25. He then covers GPU requirements around
30:16, distributed-training bottlenecks around 34:46, and Kubernetes limits
around 47:16. Machine learning infrastructure at that scale includes hardware
access, network layout, utilization, and scheduler choice.

## Ownership and Scope

The interviews disagree less about components than about timing. Simon argues
for platform investment when teams repeat deployment and serving work across
projects. He also includes repeated governance and registry work, but warns
against building heavy platform pieces too early. Real models and business
needs should come first
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
16:52 and 47:08). His view makes infrastructure a response to repeated
friction, not an up-front shopping list.

Raphaël frames the same decision through adoption. In
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
his centralized MLOps team gathers pain points and supports product teams.
It also measures value before standardizing too much (23:01, 27:56, and 36:55). The
infrastructure succeeds when ML teams use it repeatedly and can trace value back
to release speed, reproducibility, or operational reliability.

For smaller production systems, [[person:andreaskretz|Andreas Kretz]]
draws the boundary lower. In
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]],
he recommends starting with Lambda and queues before moving
toward Airflow or Kubernetes. That boundary applies when the workload doesn't
yet justify heavier [[orchestration]]
(41:06).

Andrey's large-model discussion points the other way. Once GPU cost and
distributed training dominate the work, normal cloud-managed ML services may no
longer be the right operating model. SLURM-like scheduling and bare-metal
provisioning become part of the infrastructure discussion too
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
5:27 and 47:16, plus 54:31 and 56:53).

## Compute and GPU Infrastructure

Compute starts with ordinary cloud resources for notebooks and training jobs.
It also covers batch work. Simon names AWS, GCP, and Azure as
[[platform engineering]]
skills around 8:11 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He also names Kubernetes and Terraform, and around 28:20 he adds managed
compute. The [[developer experience]]
goal is practical: teams need compute access without opening a support ticket
for every run.

Large-model workloads add another layer. Andrey discusses GPU requirements
around 30:16 in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]].
Around 34:46, he names PyTorch, NCCL, and communication bottlenecks.

Around 37:35, he discusses optimization strategies and DeepSpeed. Teams need to
design for network layout and GPU coordination in that setting. They also need
to weigh training efficiency against the cost tradeoff between cloud and
on-prem hardware.

This is where [[machine learning system design]]
becomes more than an API and database exercise. A design has to say whether the
model trains on a managed service, a Kubernetes cluster, a Databricks job, or a
GPU pool. It also has to explain when managed compute is enough and when
hardware scheduling becomes a real constraint.

## Storage and Artifact Management

ML infrastructure stores more than raw data. It stores training data snapshots,
features, model files, and Docker images. It also stores experiment metadata,
prediction logs, and deployment artifacts. Simon ties this layer to
[[experiment tracking]] around
29:41 and model registries around 30:32 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Those services create the handoff from training to batch inference, online
serving, and audit.

Raphaël adds package registries and dependency compatibility around 53:08 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
The model artifact alone isn't enough if the runtime image, Python packages,
and deployment dependencies drift. Docker and Kubernetes show up in the same
episode around 56:50 because container strategy affects reproducibility and
team autonomy.

Andreas shows the simpler production path around 25:36 and 34:16 in
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]].
He stores Parquet on S3, Dockerizes training, and persists model files where
later jobs can load them. The team needs stable storage for data, code, and
models before it can reason about
[[Reproducibility]].

## Orchestration and Scheduling

Orchestration coordinates training and evaluation, plus inference, retraining,
and data movement. Simon discusses Airflow and pipelines around 31:51 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He places them inside production workflows, which links ML infrastructure to
[[data pipelines]] and
[[Batch vs Streaming]].
Some models need scheduled batch scoring, while others need online inference or
streaming features.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
gives a workflow-tool example through Metaflow in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
Around 13:52, he discusses integrations with AWS, Kubernetes, and Argo. The
developer-experience point is direct. Data scientists shouldn't have to
assemble the full cloud and workflow stack from scratch before they can run a
reproducible ML flow.

Kubernetes is useful, but guests don't treat it as a universal answer.
Andrey discusses Kubernetes limitations for AI workflows and SLURM around 47:16
in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]].
Andreas makes the opposite-scale point around 41:06 in
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]].
Start with Lambda, queues, or simpler schedulers when the workload doesn't
justify heavier orchestration.

## Serving and Deployment

Serving infrastructure turns trained models into predictions. Guests use
two recurring deployment shapes: batch inference and online serving. Simon
discusses this split around 31:15 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Batch inference can run as scheduled jobs. Online serving needs request-time
latency, logging, API contracts, and rollback paths.

Andreas gives a concrete product example around 31:33 in
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]].
He chooses between live API calls and precomputed predictions. Around 37:53, he
also discusses SageMaker endpoints and cost tradeoffs. Serving is a business
and latency decision, not just a framework choice.

Raphaël links deployment to release discipline in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
Around 39:06, he covers CI and repository structure. He also covers
parameterization and tests.
Around 51:21, he includes serving in the MLOps toolset. Infrastructure should
therefore support both the runtime and the release path that gets code into
that runtime.

## Monitoring and Feedback Loops

Monitoring links deployment to maintenance. Raphaël describes the core
challenge as keeping models deployed, monitored, and maintained around
1:01:58 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
His earlier chapters tie CI/CD and tests to traceability, experiment capture,
and monitoring. [[Model monitoring]]
belongs on the infrastructure page because the runtime needs logs, metrics,
alerts, and ownership.

Simon adds governance and observability requirements around 42:48, 45:50, and
54:15 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Metadata and lineage affect infrastructure design. GDPR constraints, deletion
rules, and unified prediction schemas do too. Prediction logs should support
monitoring and analytics, but they also need security and data-governance
controls.

For large AI workloads, monitoring also includes utilization and cost. Andrey's
cloud-versus-on-prem discussion around 8:25 in
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]
frames compute ownership as an operating concern. GPU clusters can fail as
business infrastructure if teams can't see usage, contention, and idle cost.

## Platform Ownership and Developer Experience

Infrastructure becomes valuable when teams can use it without becoming
infrastructure specialists. Simon's user-centric platform discussion around
10:47 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
starts from data science workflows and notebooks. Around 38:40, he describes
thin abstraction layers over cloud providers. Platform teams use those layers
to expose enough control for real work while hiding repeated setup.

Raphaël describes the team model behind that experience. Around 23:01 and 25:20
in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
the centralized MLOps team supports product teams and ML engineers. Around
48:41, he recommends starting with CI/CD and tangible pain points.
Infrastructure ownership becomes a service model, not only a
cluster-maintenance job.

Hugo's Metaflow discussion gives the open-source developer experience version.
Around 2:14 and 13:52 in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]],
the flow abstraction sits across AWS, Kubernetes, and Argo. The infrastructure
still exists, but the user works through a tool that fits ML workflows.

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
