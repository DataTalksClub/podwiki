---
layout: wiki
title: "ML Platform Engineer Role"
summary: "The ML platform engineer role across internal ML platforms, developer experience, MLOps services, infrastructure tradeoffs, and role boundaries."
related:
  - ML Platforms
  - MLOps
  - Platform Engineering
  - Machine Learning Engineer Role
  - Developer Experience
  - Platform Adoption
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
---

An ML platform engineer builds the shared path that model builders use to
train, deploy, monitor, and govern machine learning systems. The role sits
between [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}), and
[machine learning engineering]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).
It's less about owning one model and more about making many model teams faster
and safer.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
describes the platform version directly. His episode starts with deployment
blockers and moves into cloud infrastructure, Kubernetes, and Terraform. It
also covers data science workflows, experiment tracking, and model registries.
Serving and orchestration come next. Metadata, lineage, governance, and
prediction logging follow
([Building Production ML Platforms on deployment blockers to prediction logging at 6:55-54:15]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

## Common Definition

The common definition is internal platform ownership for ML work. The platform
engineer gives data scientists and ML engineers a reliable way to access
compute and track experiments. They also help teams persist models, deploy
predictions, and observe runtime behavior. That connects the role to
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}), and
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}).

Simon frames MLOps as people, workflow, and technology. He then describes a
platform as the reusable system around the data science workflow. Teams start
with exploration, training, and evaluation. They continue through self-service
compute, tracking, and registries. Serving and orchestration follow
([Building Production ML Platforms on MLOps definition to orchestration choices at 4:42-34:01]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

[Krzysztof Szafanek]({{ '/people/krzysztofszafanek/' | relative_url }}) gives
the engineer-as-consultant version from Zalando. His ML platform work includes
the `zflow` library and pipeline architecture. Onboarding, training, and user
support also belong in the role
([How to Grow Your ML Engineering Career on zflow and platform consulting at 13:25-17:48]({{ '/podcasts/how-to-grow-your-ml-engineering-career/' | relative_url }})).
That makes [developer experience]({{ '/wiki/developer-experience/' | relative_url }})
part of the role, not a separate nice-to-have.

Operational ownership also belongs in the role. Simon ties team size and
on-call expectations to ML platform staffing, which means the platform isn't
only a set of libraries. Someone has to support the path when training,
deployment, serving, or monitoring fails
([Building Production ML Platforms on team size and on-call at 15:34]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

## Points of Disagreement

Guests differ on when platform work is justified. Simon warns against building
a heavy platform before real models and repeated business needs exist. He
recommends looking for standardization triggers across teams. Minimal platform
pieces can then grow alongside actual use
([Building Production ML Platforms on platform timing at 16:52-20:04 and 47:08-49:19]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) gives
an enabling-team version in the
[MLOps at Scale discussion of centralized support and adoption at 23:01-32:46]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
His team supports product teams, gathers pain points, and earns adoption
through quick wins. That version is closer to internal consulting and platform
product management.

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) makes the product
management layer explicit. In his ML platform strategy episode, internal data
scientists and analysts are customers. User feedback and platform usability
guide the roadmap. Observability KPIs, release governance, and rollout timing
guide it too. Surveys and shadowing add more evidence
([Become an ML Product Manager on internal users through user research at 11:24-57:20]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) is more
pragmatic about tool choice. Her standardized MLOps discussion emphasizes Git,
CI/CD, registries, and Kubernetes. It also emphasizes reusable repositories and
existing engineering primitives before adding more platform layers
([Pragmatic MLOps on existing infrastructure and reusable repositories at 16:27-33:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

## Core Work

ML platform engineers usually own self-service paths. Simon's episode names
notebooks and BigQuery as examples of self-service compute. Databricks
provisioning appears there too. He then moves into experiment tracking as an
early reproducibility win. Model registries handle the handoff from training to
downstream use
([Building Production ML Platforms on self-service compute through registries at 28:20-30:32]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Serving is another core area. Platform teams may support batch inference,
online serving, scheduled jobs, or APIs. Teams choose between them based on
latency, freshness, cost, and ownership. Simon discusses batch versus online serving
and orchestration choices in the same platform context
([Building Production ML Platforms on batch inference and orchestration at 31:15-34:01]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

The platform also needs governance and observability. Simon connects regulatory
constraints, metadata, lineage, and data governance to the platform role. API
design and unified prediction schemas belong there too
([Building Production ML Platforms on governance through prediction logging at 39:54-54:15]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
That links the role to [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[Governance]({{ '/wiki/governance/' | relative_url }}), and
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}).

Some platform components are situational. [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }})
argues that feature stores fit repeated tabular ML use cases. They help with
feature reuse, online serving, validation, and governance. They can be overkill
without a real-time feature need or shared feature lifecycle
([Feature Stores for MLOps on platform fit at 21:00-52:00]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})).

For larger platform choices, the same caution means starting from repeated pain
instead of tool fashion.

## Skills

The role needs cloud and infrastructure fluency. Simon names cloud
infrastructure and Kubernetes as core platform skills. Terraform belongs in the
same skill set. Software engineering does too
([Building Production ML Platforms on infrastructure skills and software engineering at 8:11-13:50]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

It also needs enough ML workflow knowledge to understand notebooks and training
runs. Evaluation, model handoffs, and deployment friction matter too.

Krzysztof's episode adds durable engineering habits. SQL, Git, shell, and
debugging remain valuable as ML tooling changes. Engineers also need T-shaped
expertise and troubleshooting skill
([How to Grow Your ML Engineering Career on durable engineering skills at 29:00-37:37]({{ '/podcasts/how-to-grow-your-ml-engineering-career/' | relative_url }})).
Those skills matter because platform work often fails in integration details,
not in isolated demos.

The role also needs ML literacy. It doesn't require being the strongest modeler
on the team. Simon discusses when platform engineers should learn model
internals
([Building Production ML Platforms on model internals at 51:41]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Krzysztof frames the useful profile as T-shaped
([How to Grow Your ML Engineering Career on T-shaped expertise at 35:23]({{ '/podcasts/how-to-grow-your-ml-engineering-career/' | relative_url }})).

The boundary with an
[MLOps engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) is porous. MLOps
can be the operating discipline around one model or team. ML platform
engineering turns repeated MLOps needs into shared internal services.

The boundary with a
[machine learning engineer]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
is product ownership. ML engineers often own one model-backed capability.
Platform engineers own the paved paths that many such capabilities use.

## Related Pages

These pages connect this role to the surrounding MLOps and platform topics.

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
