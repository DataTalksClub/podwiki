---
layout: "person"
title: "Simon Stiebellehner"
summary: "Simon Stiebellehner's DataTalks.Club podcast discussions, organized for topic exploration."
source_url: "https://datatalks.club/people/simonstiebellehner.html"
podcast_episodes: ["building-production-ml-platform-and-mlops-team"]
curated: "true"
linkedin: "simonstiebellehner"
expertise: ["MLOps", "ML platform engineering", "production ML", "model governance", "ML teams"]
---

## Background

Simon Stiebellehner has spent more than half a decade building ML platforms. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he describes moving from research roles into deployment and model serving work.
He later moved into platform leadership at bol.com and Transaction
Monitoring Netherlands. He frames [MLOps]({{ '/wiki/mlops/' | relative_url }})
as a practical response to a recurring blocker. Teams could train useful models,
but they struggled to turn them into reliable [production]({{ '/wiki/production/' | relative_url }})
systems.

## MLOps as People, Process, and Technology

Simon says people often think first about feature stores, experiment trackers,
and model registries. He argues that MLOps is broader than those tools. In the
episode's MLOps definition section, he describes successful operations through
people, process, and technology. Teams need to understand how they develop
models and move them into deployment. They also need to know how they
collaborate once many models run in production
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Readers can use his contribution when they treat [ML platform engineering]({{ '/wiki/ml-platforms/' | relative_url }})
as adoption work, not just infrastructure work. Simon wants platforms to
streamline the work of product and [data teams]({{ '/wiki/data-teams/' | relative_url }}).
They should reduce cognitive load and automate the model lifecycle only after
the team understands that lifecycle.

## Platform Triggers and Build-vs-Buy Choices

Simon is cautious about building a full platform too early. He says the clearest
trigger appears when several engineering teams own ML-powered products. If they
rebuild training, serving, and deployment flows differently, look for the
reason. Without a strong reason, a platform can standardize repeated work and
make the business case visible
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

He also pushes against the idea that buying SageMaker, Vertex AI, or another
managed platform removes the platform work. Teams still need to integrate tools,
adapt them to internal workflows, and sometimes build thin layers for developer
experience. They may also need thin layers for security and compliance. For a
single team, Simon recommends starting with useful pieces such as
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) before
investing in a broad platform.

## Team Skills and Operating Load

For ML platform teams, Simon puts infrastructure and cloud knowledge first. He
adds software engineering and enough model-development knowledge to understand
data scientists' workflows.

He doesn't expect every platform engineer to understand model internals deeply.
He does expect the team to mix cloud
specialists and software engineers. It should also include people who understand
experimentation and notebooks. They should know training, evaluation, and
deployment too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

His staffing discussion connects [leadership]({{ '/wiki/leadership/' | relative_url }})
with operations. If the platform has availability requirements, the team has to
plan for on-call coverage and business criticality, not only feature delivery.
That means platform headcount depends on how many teams use it, how much
operational load it creates, and how costly downtime would be.

## Workflow, Deployment, and Tool Integration

Simon starts from the data scientist's workflow. Data scientists pull data into
notebooks or exploratory compute, then train and evaluate models. They track
experiments, register models, and serve them through batch inference or online
APIs
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

The platform priorities follow that workflow. Prioritize batch support if most
models run in batch, and make self-service compute easy. Use a model registry
so downstream jobs or services can consume stable model artifacts.

Simon treats tool selection as integration work, so teams usually shouldn't
build their own experiment tracker. They still have to choose the right hosted
or self-managed pieces and make them fit one coherent platform. His episode
connects [MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}),
[model registry]({{ '/wiki/model-registry/' | relative_url }}), and
[orchestration]({{ '/wiki/orchestration/' | relative_url }}). The useful
platform matches the organization's actual training, serving, and monitoring
paths.

## Governance and Production Operations

Simon brings a regulated-finance lens to platform design. In fintech and other
sensitive settings, security and compliance raise the bar for deployment
choices. Auditability, explainability, and fairness requirements raise it too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
He points out that even ecommerce can have sensitive cases such as fraud
detection. Teams then need to explain why a decision happened and keep enough
history to audit it.

His governance discussion is especially useful for [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
and reproducibility. Model registries and managed services can store parts of
the record, but teams still need end-to-end metadata. They need to know which
code version and data reference produced a model. They also need the container
image, inputs, outputs, and pipeline run.

Simon is also careful about data logging. Copying full training datasets for
every run may help reproducibility, but it can create cost and retention
problems. It can also make GDPR deletion difficult if the data includes personal
information.

## Learning by Building

For people moving toward MLOps or platform work, Simon recommends practical
projects over only reading books. He names books such as Designing Machine
Learning Systems and Practical MLOps. His stronger advice is to build small
projects that exercise real cloud, deployment, tracking, and operations
decisions
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
That makes his episode a useful companion for the [MLOps roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})
and [machine learning engineer role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
pages.
