---
layout: wiki
title: "ML System Design Documents"
summary: "Podcast-grounded reference for ML design docs as fail-fast, ownership, data strategy, monitoring, review, and production-readiness artifacts."
related:
  - Machine Learning System Design
  - Documentation
  - MLOps
  - Model Monitoring
  - Software Engineering
  - Evaluation
  - Data Quality and Observability
---

## Definition

An ML system design document is the written specification for an
[ML system]({{ '/wiki/machine-learning-system-design/' | relative_url }}) before
and during implementation. It names the product decision, goals, and non-goals.
It also records assumptions, data paths, and baselines. Evaluation and serving
belong in the same artifact.

Ownership, monitoring, and fallback behavior do too. It's closer to an
engineering design review than to a research report.

The DataTalks.Club archive treats these documents as coordination tools for
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[documentation]({{ '/wiki/documentation/' | relative_url }}), and
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}).
[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) frames the
design document as a way to fail fast in
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}).
At 7:06 and 8:39, he compares it to a blueprint that can expose weak assumptions
before months of implementation.
[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }})
uses a similar problem-first frame in
[Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}),
where goals and constraints come before model choice. Assumptions, metrics, and
data flow come early too.

## Common Definition

Across the podcast episodes, an ML system design document is a compact, living
agreement about the system the team plans to build. It also states what must be
true for that system to work in production. The shared structure is problem
first, then solution. A useful document starts with the decision the model
supports and the users affected by that decision. It then adds the metric or
business outcome, plus the conditions where the team shouldn't use ML.

Valerii's design-doc episode makes the fail-fast purpose explicit. At 14:36, he
connects shared design docs to stakeholder alignment, feedback, and simplicity.
At 19:01, he argues that the design doc has to stay alive as the system changes.

At 43:53, his outline starts with preliminary research and loss functions. It
then adds metrics, datasets, validation schema, and a baseline solution. Later
sections cover error analysis, training pipelines, features, and reporting. The
outline also includes integration, reliability, and monitoring. Serving,
ownership, and maintenance are part of it too
([ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})).

Arseny describes the same artifact from startup and production-systems work.
In his episode at 20:21 and 29:01, the document splits attention between the
problem and the solution. The problem side records product scenarios, goals, and
non-goals. It also records assumptions, constraints, and metrics.

The solution side records the baseline and model direction. Data flow, pipeline
components, and data strategy belong there too
([Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }})).

## Guest Differences

Valerii emphasizes design documents as long-lived production artifacts. His
episode returns to maintenance, modular chapters, versioning signals, and
review. It also covers ownership, bus-factor risk, monitoring, and fallback
planning. In his view, the team should treat the design doc as part of
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[MLOps architecture]({{ '/guides/mlops-architecture/' | relative_url }}), not just
as a planning note.

Arseny emphasizes early scoping and decision quality through examples that
include startups, edge ML, and mobile ML. Photostock search and retail pricing
appear in the same discussion. At 10:34, mobile constraints make latency and
frames per second first-class design inputs.
Energy use, model size, offline behavior, and runtime choices matter too.

At 37:15, he uses diagrams to reason about data flow. He also uses them for
dependencies and batch versus real-time paths.

[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) adds the software
engineering warning in
[Software Engineering for Machine Learning]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}).
At 10:54 and 29:42, she names poor requirements and unrealistic expectations as
recurring causes of ML project failure. Data access and deployment gaps matter
too. At 56:55, she argues for involving ML practitioners from requirements
through testing.
That broadens the document from a modeling artifact into a cross-functional
review surface.

## Requirements, Non-Goals, and Assumptions

The first job of the document is to turn vague model intent into requirements
that another team can review. Arseny's problem-first design section asks teams
to write goals and non-goals before they choose architecture. Assumptions,
constraints, and metrics come early too
([Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }})).
This protects the design from becoming a model wish list.

Good requirements connect the model to a product action. A fraud system might
block a transaction or route it to manual review. A pricing system might change
a displayed price or only recommend one to an operator. A search system might
rank, filter, or explain.

Teams should write which action is in scope. They should also write which
failure costs matter and where human review is required. Those choices connect
the design work to
[evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), because offline
metrics alone don't define product success.

Requirements are organizational too, and Nadia's episode shows how unclear
vocabulary and data access assumptions create hidden technical debt. Deployment
expectations create the same risk
([Software Engineering for Machine Learning]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})).
An ML design document is useful when it gives data scientists, ML engineers,
software engineers, and product owners the same object to challenge. Domain
experts and operations owners need that review surface too.

## Data Strategy, Baselines, and Evaluation

The archive treats baselines as design work, not as an afterthought. At 55:13,
Valerii recommends simple baseline solutions. Teams can use them to test
hypotheses. They can also iterate before they over-invest
([ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})).

Arseny makes the same point through metrics and data availability. Without a
baseline and a metric, the team can't tell whether the system is useful
([Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }})).

Teams should use the data section to explain whether the required data exists
and who owns it. They should state where the data comes from and how they
process it. They should also say whether features can be computed at prediction
time.

Teams should choose between batch scoring and streaming features. They should
also decide whether the system needs online serving or offline analysis. Those
decisions tie ML design docs to
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[batch versus streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

Evaluation belongs in the same written artifact because model quality and
product quality can diverge. Teams should record the offline metric and the
business metric. They should also record slices or cohorts to look at, the
validation data source, and the error analysis plan. The rollout method belongs
there too.

If the system affects users directly, the review may need an A/B test or shadow
deployment. It may also need a manual-review queue or staged launch rather than
a single offline score.

## Review and Production Readiness

Guests describe written specs as a way to move production risk earlier. Valerii
links design documents to feedback and review at 14:36. At 41:01, he connects
them to design-doc review and update frequency
([ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})).

The review is valuable when it catches missing data and fragile dependencies. It
should also catch unowned components, unrealistic latency targets, weak
baselines, and privacy issues. Governance issues and missing fallback behavior
should be visible before launch.

Production readiness in an ML design doc should cover the system boundary. That
boundary includes training, features, serving, and integrations. It also
includes deployment, monitoring, and alerts. Rollback and ownership belong there
too.

This is where the team's design work overlaps with [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
and [software engineering]({{ '/wiki/software-engineering/' | relative_url }}).
Nadia's software-engineering episode supports this broader review bar by
showing how ML projects stall when documentation and requirements stay separate
from modeling work. Testing and deployment need the same integration
([Software Engineering for Machine Learning]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})).

## Ownership and Living Documentation

Valerii repeatedly argues that a design document isn't finished when the first
version is approved. At 19:01 and 24:37, he connects the artifact to maintenance,
accountability, and explicit responsibility areas. At 31:59, he uses bus-factor
risk to show why the document should reveal people dependencies
([ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})).

That makes ownership a design-doc section, not a project-management appendix.
Teams should state who owns the model and data sources. They should also name
owners for feature definitions, pipelines, and deployment.

Monitoring, incident response, and product decisions need owners too. If
different groups own those pieces, the team should make the handoffs visible.
This connects ML design docs to
[documentation]({{ '/wiki/documentation/' | relative_url }}),
[governance]({{ '/wiki/governance/' | relative_url }}), and
[data product management]({{ '/wiki/data-product-management/' | relative_url }}).

## Monitoring, Drift, and Fallbacks

Monitoring and fallbacks belong in the design before the first production
release. Valerii separates data drift, concept drift, and prediction drift at
47:46. At 51:59, he links fallback strategies to redundancy, simple baselines,
and serving reliability
([ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})).
Those sections should state what can break. They should also state what the
product should do when it breaks.

The answer may be a previous model or a simple rule. It may be a cached
recommendation or a manual-review route. It may also be a disabled automation or
a slower but safer serving path. The right fallback depends on the failure cost.

A healthcare or education system may require stronger human review and
explainability. A pricing or search system may need staged rollout. Fraud and
recommendation systems may need alert thresholds and rollback rules. Teams
should connect those decisions to
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [governance]({{ '/wiki/governance/' | relative_url }}).

## Related Pages

These pages expand the design-doc decisions above.

- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Documentation]({{ '/wiki/documentation/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
