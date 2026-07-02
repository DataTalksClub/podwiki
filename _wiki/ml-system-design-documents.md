---
layout: wiki
title: "ML System Design Documents"
summary: "How ML design docs capture product decisions, assumptions, data strategy, baselines, evaluation, monitoring, ownership, and production readiness."
related:
  - Machine Learning System Design
  - Documentation
  - MLOps
  - Model Monitoring
  - Software Engineering
  - Evaluation
  - Data Quality and Observability
---

An ML system design document is the written specification for a
[[machine-learning-system-design|machine learning system]]
before a team commits to an architecture. Teams use it to name the product
decision, users, goals, and non-goals. They also record assumptions, data
paths, and baselines.

They keep evaluation plans and serving mode in the same
document. Monitoring, fallback behavior, and owners belong there too. Teams
review it like an engineering design doc, not a research report.

[[person:valeriybabushkin|Valerii Babushkin]] frames the
design doc as a way to fail fast in
[[podcast:ml-system-design|ML System Design Playbook]].
At 7:06 and 8:39, he compares it to a blueprint that exposes weak assumptions
before the team spends months implementing them. At 14:36, he ties the design
doc to stakeholder feedback and simplicity. At 19:01, he says teams should
update it after the system changes.

[[person:arsenykravchenko|Arseny Kravchenko]] uses a
similar problem-first frame in
[[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]].
In his framing, teams write goals, constraints, and assumptions before model
choice. Metrics and data flow come early too. Both guests place design docs
inside
[[MLOps]],
[[documentation]], and
[[software engineering]].

## Scoping Before Model Choice

Teams should start with the decision the model supports and the people affected
by that decision. A fraud system may block a transaction or route it to
manual review. A pricing system may change a displayed price or recommend one
to an operator. A search system may rank, filter, or explain results.

Teams should write which action is in scope and which failure costs matter.
Teams should also write where a human must review the decision.

Arseny's design-doc discussion at 20:21 and 29:01 splits the document into a
problem side and a solution side
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).
On the problem side, teams record product scenarios, goals, and non-goals.
They also record assumptions, constraints, and metrics. On the solution side,
they record the baseline, model direction, and data flow. Pipeline components
and data strategy belong there too.

By writing the problem before the solution, teams keep the document from
becoming a model wish list.

[[person:nadianahar|Nadia Nahar]] adds the software
engineering warning in
[[podcast:software-engineering-for-machine-learning|Software Engineering for Machine Learning]].
At 10:54 and 29:42, she names weak requirements and unrealistic expectations as
recurring causes of ML project failure. Poor data access and deployment gaps
matter too.

At 56:55, she argues for involving ML practitioners from requirements through
testing. Teams can use a design doc to give data scientists, ML engineers, and
software engineers the same review surface.
Product owners, domain experts, and operations owners need the same shared
document.

## Data, Baselines, and Evaluation

At 43:53, Valerii starts the outline with preliminary research and loss
functions. He then adds metrics, datasets, validation schema, and a baseline
solution
([[podcast:ml-system-design|ML System Design Playbook]]).
He later adds error analysis, training pipelines, features, and reporting.
He also includes integration, reliability, and monitoring. Serving, ownership,
and maintenance appear in the same outline.

At 55:13, he recommends simple baseline solutions so teams can test hypotheses
before they over-invest.

Arseny makes the same point through metrics and data availability
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).
Without a baseline and a metric, a team can't tell whether the system is useful.
In the data section, teams should state whether the required data exists and who
owns it. They should name where it comes from, how features are computed, and
whether those features are available at prediction time.

Teams may choose batch scoring or streaming features, online serving or offline
analysis. Each serving choice creates different design obligations. Teams often
need the same vocabulary used in
[[data pipelines]],
[[batch-vs-streaming|batch versus streaming]],
and
[[data quality and observability]].

Teams should keep evaluation in the same document because offline model quality
and product quality can diverge. They should record the offline metric, business
metric, validation data, and cohort or slice checks. The error analysis plan and
rollout method belong there too. User-facing systems may need an
[[a-b-testing|A/B test]], shadow deployment,
manual-review queue, or staged launch rather than a single offline score.

## Constraints, Diagrams, and Serving

Arseny puts special weight on early constraints because some ML systems fail
when the model is reasonable but the runtime is wrong. At 10:34, mobile and edge
ML make latency and frames per second first-class design inputs. Energy use,
model size, offline behavior, and runtime choices matter too
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).

At 37:15, Arseny uses diagrams to reason about data flow, dependencies, and
batch versus real-time paths. Reviewers can use those diagrams to ask concrete
serving questions. They can check the service that calls the model and the
feature data that must be fresh. They can also check the dependency that can
fail and whether the system can answer from a cached or batch result. Those
questions link the design doc to
[[machine learning infrastructure]]
and [[MLOps architecture]].

## Review and Production Readiness

At 14:36, Valerii links design docs to feedback and review. At 41:01, he
returns to review cadence
([[podcast:ml-system-design|ML System Design Playbook]]).
Reviewers should catch missing data, fragile dependencies, unowned components,
and unrealistic latency targets before launch. They should also catch weak
baselines, privacy issues, governance gaps, and missing fallback behavior.

For production readiness, teams should cover the full system boundary. Training,
feature definitions, serving, and integration points belong there. Deployment
and monitoring belong there too. Alerts, rollback, and ownership need the same
review.

Nadia's software-engineering episode supports that broader bar by showing how ML
projects stall when teams separate documentation and requirements from modeling
work. Testing and deployment need the same shared review
([[podcast:software-engineering-for-machine-learning|Software Engineering for Machine Learning]]).

## Ownership and Living Documentation

Valerii argues that a design doc isn't finished when the first version is
approved. At 19:01 and 24:37, he ties the document to maintenance,
accountability, and explicit responsibility areas. At 31:59, he uses
bus-factor risk to show why the document should reveal people dependencies
([[podcast:ml-system-design|ML System Design Playbook]]).

Teams should put ownership in the design doc, not in a separate
project-management note. They should name the owners for the model, data
sources, and feature definitions. They should also name owners for pipelines,
deployment, and monitoring. Incident response and the product decision need
named owners too.

If different groups own those pieces, teams should make the handoffs visible in
the document. Ownership choices link ML design docs to
[[governance]],
[[data product management]],
and [[model monitoring]].

## Monitoring, Drift, and Fallbacks

Monitoring and fallbacks belong in the design before the first production
release. Valerii separates data drift, concept drift, and prediction drift at
47:46. At 51:59, he links fallback strategies to redundancy, simple baselines,
and serving reliability
([[podcast:ml-system-design|ML System Design Playbook]]).
Before launch, teams should write what can break and what the product should do
when it breaks.

A fallback may use a previous model, a rule, or a cached recommendation. It may
route to manual review, disable automation, or choose a slower but safer serving
path. The right fallback depends on the failure cost.

Healthcare or education systems may require stronger human review plus
explainability. Pricing or search systems may need staged rollout. Fraud or
recommendation systems may need alert thresholds and rollback rules. Those
decisions depend on
[[data quality and observability]],
[[model monitoring]], and
[[governance]].

## Related Pages

These pages expand the design-doc decisions above.

- [[Machine Learning System Design]]
- [[Documentation]]
- [[MLOps]]
- [[Machine Learning Infrastructure]]
- [[Model Monitoring]]
- [[Evaluation]]
- [[Data Quality and Observability]]
- [[Software Engineering]]
