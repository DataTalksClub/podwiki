---
layout: wiki
title: "Machine Learning System Design"
summary: "How DataTalks.Club episodes frame ML system design as a production discipline: problem framing, data strategy, baselines, evaluation, serving, monitoring, fallbacks, and ownership."
related:
  - MLOps
  - Machine Learning Infrastructure
  - ML System Design Documents
  - Model Monitoring
  - Experiment Tracking
  - Evaluation
  - A/B Testing
  - Production ML Project Checklist
  - Recommendation Systems
  - Search
---

Machine learning system design decides how an ML system should support a product
or business decision before teams commit to a model. A design names the decision
and data. It also names labels and the feature path. Then it names serving,
evaluation, monitoring, and ownership after release.
[[book:20220627-designing-machine-learning-systems|Designing Machine Learning Systems]]
by Chip Huyen is the canonical reference for this discipline: it covers the full stack from problem framing and data engineering through serving, monitoring, and continuous improvement.

Fraud detection, recommendations, feature work, and metrics connect as design
choices alongside A/B tests, monitoring, fallbacks, and MLOps roles
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).
The same work can be defined through goals, constraints, data flow, and
trade-offs, which matters when the system must run on mobile or edge devices
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).

## Product Decision and Operating Boundary

The practical definition starts with the decision and ends with an operable
system. A fraud model or recommender isn't designed by choosing a model class
first; the same holds for pricing, search, and computer vision. Teams first name
the product decision and users, then the failure cost, baseline, and path from
data to prediction.

The fraud example turns into questions about probabilities and loss functions,
real-time requirements, and class imbalance
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).
The same framing writes goals and non-goals first, then assumptions, metrics, and
a solution blueprint
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).

The term overlaps with [[MLOps]], but it isn't
identical. Machine learning system design decides what system should exist and
which constraints matter.

MLOps covers repeatable operating practices for deployment and reproducibility,
plus monitoring, retraining, and adoption, expressed through CI/CD, data
versioning, containers, and adoption work
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

## Interview, Delivery, and Platform Angles

System design is both an interview skill and a production habit. As an interview
skill it centers on communication, assumptions, baselines, metrics, and A/B
testing, and interviewers need to see how a candidate reasons through ambiguity
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).

On the delivery side, design documents help projects fail early and align
stakeholders, and the document should stay alive as the system changes
([[podcast:ml-system-design|ML System Design Playbook]]).

Constraints and early risk carry more weight for edge systems: mobile and edge ML
force teams to design around latency, frames per second, energy use, and offline
behavior; early tests reduce unknown risks; and diagrams reason about data flow,
dependencies, and batch-versus-real-time paths
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).
Those latency and size constraints drive [[Model Optimization]]
techniques.

Through a software-engineering lens, ML products are software systems with added
uncertainty; recurring problems are poor requirements, unrealistic expectations,
data access, and deployment gaps, with the remedy in shared vocabulary,
documentation, and engineering habits
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]).
That makes
[[software engineering]] part of
ML system design, not a separate afterthought.

Repeated design problems push toward platform capabilities: experiment tracking
and model registries, batch inference and online serving, orchestration,
metadata, and lineage
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]),
plus adoption, developer experience, model serving, and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

## Requirements and Constraints

An ML system design starts by naming the decision, users, and failure cost. Fraud
detection has to account for false positives, false negatives, real-time
decisions, and manual review
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]),
and goals and non-goals turn vague requirements into metrics and assumptions the
team can challenge
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).

Good requirements also say when not to use ML. "Avoid ML" is a real design
outcome when a heuristic, rule, or existing product behavior is enough
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).
In that framing,
[[machine learning]] is a tool
choice rather than a default answer.

Writing requirements down improves them. A design document works like a blueprint,
making weak assumptions visible before a team spends months building
([[podcast:ml-system-design|ML System Design Playbook]]).
This is why
[[ML system design documents]]
matter for production systems.

## Data, Labels, and Features

Data strategy is part of the system design, not a downstream task. Data
availability, processing, features, and data lakes come before the design reaches
model architecture
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]),
and the same idea turns into practical questions about labels, class imbalance,
model selection, and validation
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).

Feature design also decides whether training and serving can stay consistent.
Features matter more than model architecture, and many production systems fail
when the team can't compute the right features at prediction time
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).
That concern connects ML system design to
[[data engineering platforms]],
[[data quality and observability]],
and [[batch-vs-streaming|batch versus streaming]].

Data access, unmet requirements, and deployment failures are common reasons ML
products stall
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]).
A design that ignores data ownership or data quality leaves a major risk for
implementation.

## Baselines and Model Choice

Baselines are design tools. A baseline clarifies the minimum useful comparison
and helps a candidate show progress without pretending the final model is obvious
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]);
simple baselines validate hypotheses quickly
([[podcast:ml-system-design|ML System Design Playbook]]).

Model choice comes after that baseline. A team may choose a rule or a linear
model. It may also choose a tree model or an embedding system. A recommender,
ranking model, or deep model may be enough for other cases.
For a dedicated reference on ranking and recommendation, [[book:20210802-practical-recommender-systems|Practical Recommender Systems]]
by Kim Falk covers the data, algorithms, and evaluation patterns behind recommender design choices.

The team can only make that choice after it understands the decision, data,
latency, evaluation, and failure cost. This is why practical ML decisions stay
separate from research-level detail
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).

## Serving and Runtime Architecture

Serving mode changes the system because batch scoring and online APIs create
different reliability requirements. Streaming features, edge inference, and human
review paths add more constraints.

Serving models and embeddings connect with MLOps roles
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]),
and platform work separates batch inference, online serving, orchestration, and
production workflows
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The clearest constraint-driven example is edge and mobile ML, which forces teams
to account for latency, frames per second, energy use, model size, offline
behavior, and runtime choices
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).
In those systems,
[[machine learning infrastructure]]
includes more than cloud deployment. It also includes the runtime where the
prediction happens.

Real-time serving is not the mature default: real-time and batch data flow are
compared as alternatives
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]),
and platform pieces are justified only when repeated use cases warrant them
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

## Evaluation and Product Validation

Offline metrics don't complete the evaluation design. Metrics, baselines,
business alignment, and proxy metrics connect together, and production validation
rests on A/B testing, causality, and human labels
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]).
The model may score well offline and still fail if it harms the product metric or
increases manual-review load.

The product-experimentation background covers randomization and assignment
tracking, A/A tests, metric selection, and power analysis
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]).
Those topics matter when an ML system affects user-facing decisions and the team
needs causal evidence, not just offline accuracy.

For ML systems, those choices sit beside
[[evaluation]] and
[[experimentation]]. They also
inform [[a-b-testing|A/B testing]] and
[[power analysis]].

## Monitoring, Drift, and Fallbacks

Monitoring belongs in the design because ML systems change when data, users, or
upstream systems change. Monitoring, distribution shift, and fallbacks are part
of production robustness
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]]),
and data drift, concept drift, and prediction drift are distinct, with fallbacks
tied to redundancy, simple baselines, and serving reliability
([[podcast:ml-system-design|ML System Design Playbook]]).

On the operating side, traceability, experiment capture, model registry, serving,
and monitoring round out the toolset
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Those topics explain why ML system design has to name who responds when
[[model monitoring]] shows drift,
latency issues, or a broken upstream feed.

Fallbacks can be simple and still critical. A fallback may use a previous model,
a rule system, a cached recommendation, or a manual review path. The fallback may
also turn off an automated decision. The design has to say what the product does
when the model, feature pipeline, API, or data source is unavailable.

## Design Review Checklist

Before implementation, a design should name the decision the prediction changes.
It should also name the user affected by it. The review should cover the cost
of wrong output. Late output belongs there too. So do unavailable or biased
outputs.

Those questions work as a readiness test: the team should understand the business
problem before it chooses a model
([[podcast:machine-learning-system-design-interview|ML System Design Interviews]],
[[podcast:ml-system-design|ML System Design Playbook]]).

The review should also cover:

- goals, non-goals, assumptions, and data owners
- sources, labels, freshness requirements, leakage risks, and the baseline
- offline, online, and business metrics
- guardrails and slices

Serving and operations need the same review. A design should choose batch or
online serving, then decide whether streaming, edge, or hybrid serving is
required. It should explain validation and monitoring.

Fallback behavior and rollback belong there too. Retraining triggers and
ownership belong in the same operating plan.

The review adds constraints such as latency, battery, frame rate, and runtime
limits when the product runs on mobile or edge devices
([[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]]).

## Platform and Ownership

Single projects can start with simple pieces, but repeated ML systems push teams
toward shared platform capabilities: experiment tracking, model registry,
serving, metadata, lineage, and unified prediction logging
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Teams use these tools to reduce repeated design work when many systems need the
same guarantees.

Ownership is the other platform question. Accountability, responsibility areas,
and bus-factor risk belong in the design
([[podcast:ml-system-design|ML System Design Playbook]]);
team structures and involving ML practitioners from requirements through testing
matter too
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]);
and platform teams use evangelists, technical leads, support models, and user
feedback
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

These angles complement each other. One-system design and shared
[[MLOps tools]] and platform adoption
are two sides of the same discipline: teams need shared tools once many systems
repeat the same needs, and both fail when teams don't align around requirements,
vocabulary, documentation, and responsibility.

## Related Pages

These pages expand the system-design decisions above.

- [[ML System Design Documents]]
- [[Machine Learning Infrastructure]]
- [[MLOps]]
- [[MLOps Architecture]]
- [[Model Monitoring]]
- [[Evaluation]]
- [[a-b-testing|A/B Testing]]
- [[Data Engineering Platforms]]
- [[machine-learning-system-design-interview|Machine Learning System Design Interview guide]]
