---
layout: wiki
title: "Machine Learning System Design"
summary: "ML system design as a production reference for requirements, labels, feature paths, evaluation, serving, monitoring, fallbacks, and ownership."
related:
  - MLOps
  - Machine Learning Infrastructure
  - ML System Design Documents
  - Model Monitoring
  - Experiment Tracking
  - Evaluation
  - A/B Testing
  - Production ML Project Checklist
  - Notebook to Production Workflow
  - Algorithmic Trading
  - Recommendation Systems
  - Search
---

Machine learning system design is the production reference for deciding what ML
system should exist before a team commits to a model. A design names
requirements, data contracts, labels, and the feature path. Then it names
serving and evaluation. It also names monitoring, fallback behavior, and
ownership after release.

Production teams use system design for durable artifacts rather than interview
rehearsal. Those artifacts include requirement notes and design documents. They
also include rollout checks, ownership handoffs, runbooks, and operating
boundaries. Use the interview guide when the same material needs to become a
timed answer.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]][[cite:machine-learning-system-design-interview=>ML System Design Interviews]]

Production review adds artifacts that interview prep usually skips:

- SLO targets and ADR records
- schema contracts and feature lineage
- release checklists and migration plans
- capacity budgets and rollback criteria
- alert routes, privacy reviews, security approvals, and cost envelopes
- ownership rotas and paging escalation paths
- schema tests and compatibility matrices
- quota limits and deprecation windows
- incident reviews and retention schedules
- blast radius notes and saturation thresholds
- postmortems, audit packets, and freeze windows
- maintenance calendars and ownership ledgers

[[book:20220627-designing-machine-learning-systems=>Designing Machine Learning Systems]]
by Chip Huyen is the canonical reference for this discipline. It covers the full
stack from problem framing and data engineering through serving, monitoring, and
continuous improvement.

Fraud detection, recommendations, feature work, and metrics are design choices.
They sit alongside A/B tests, monitoring, fallbacks, and MLOps roles.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Teams can define the same work through goals, constraints, data flow, and
trade-offs. That framing matters when the system must run on mobile or edge
devices.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]

For interview preparation, use the
[[machine-learning-system-design-interview=>Machine Learning System Design Interview guide]].
For the underlying reference concept, read the component and requirement
sections here. Use the later sections for production design patterns and failure
modes.

## Product Decision and Operating Boundary

The practical definition starts with the decision and ends with an operable
system. A fraud model or recommender isn't designed by choosing a model class
first. The same holds for pricing, search, and computer vision. Teams first name
the product decision and users, then the failure cost, baseline, and path from
data to prediction. That keeps the design connected to
[[machine learning for business]] before the team chooses a model.

The fraud example turns into questions about probabilities and loss functions,
real-time requirements, and class imbalance.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
The same framing writes goals and non-goals first, then assumptions, metrics, and
a solution blueprint.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]

The term overlaps with [[MLOps]], but it isn't
identical. Machine learning system design decides what system should exist and
which constraints matter.

MLOps covers repeatable operating practices for deployment and reproducibility,
along with monitoring, retraining, and adoption. In practice, that means CI/CD,
data versioning, and containers. It also means adoption work.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Design Documents and Delivery Boundaries

System design is a production discipline before it's an interview format. A
design should make product decisions, data paths, and serving choices reviewable
before implementation. It should make evaluation, monitoring, fallbacks, and
ownership reviewable too. The
[[machine-learning-system-design-interview=>Machine Learning System Design Interview guide]]
turns the same decisions into a timed whiteboard answer. Use this page as the
reference model for production systems.

Design documents help projects fail early and align stakeholders. Teams should
keep the document current as the system changes.
[[cite:ml-system-design=>ML System Design Playbook]]
Use [[ml-system-design-documents=>ML System Design Documents]] for the written
review surface behind those decisions.

Constraints and early risk matter more for edge systems. Mobile and edge ML
force teams to design around latency, frames per second, energy use, and offline
behavior. Early tests reduce unknown risks. Diagrams reason about data flow,
dependencies, and batch-versus-real-time paths.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]
Those latency and size constraints drive
[[model-optimization=>Model Optimization]]
techniques.

Database choice belongs in the same design review. Relational, document, search,
and graph stores fit different data shapes and access paths. Fraud systems can
index entity records as documents. They can use graph databases when
relationship traversal is part of the product or investigation workflow.
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@20:30=>Fraud Data Engineering]][[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@35:33=>Fraud Data Engineering]]
That connects ML system design to
[[knowledge-graph-vs-vector-search=>Graph vs Vector Search]]
when relationship structure becomes a feature or user interface.

Through a software-engineering lens, ML products are software systems with added
uncertainty. Recurring problems include poor requirements, unrealistic
expectations, data access, and deployment gaps. Teams remedy those gaps with
shared vocabulary, documentation, and engineering habits.
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]
That makes
[[software engineering]] part of
ML system design, not a separate afterthought.

When design problems repeat, teams need platform capabilities. They need
experiment tracking and model registries, plus batch inference and online
serving. They also need orchestration, metadata, and lineage.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

At that design boundary, [[metaflow=>Metaflow]] gives one concrete
workflow-tooling example. It connects local model development to reproducible
cloud runs and scheduler infrastructure.
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]
That makes [[machine-learning-tools=>Machine Learning Tools]] a system-design
choice when the tool has to preserve reproducibility, scheduling, and production
handoff.
Adoption, developer experience, model serving, and monitoring matter too.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Requirements and Constraints

An ML system design starts by naming the decision, users, and failure cost. Fraud
detection has to account for false positives, false negatives, real-time
decisions, and manual review.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Goals and non-goals turn vague requirements into metrics and assumptions the
team can challenge.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]

Good requirements also say when not to use ML. "Avoid ML" is a real design
outcome when a heuristic, rule, or existing product behavior is enough.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Fast proof-of-concept work should test the same boundary: start with a
heuristic or manual process. Use ML only after the baseline exposes a real
product improvement.
[[cite:from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership@28:46=>Applied ML Leadership]]
In that framing,
[[machine learning]] is a tool
choice rather than a default answer.

In [[algorithmic-trading=>algorithmic trading]], teams apply the same
requirements discipline to markets. They name the trade horizon and target
alongside position rules, loss limits, fees, and manual review paths before
model choice matters.
[[cite:algorithmic-trading-with-python-and-machine-learning=>Algorithmic Trading with Python]]
Teams can use backtesting instead of [[reinforcement-learning]] when historical
data can test the decision policy. Backtesting avoids unsafe live exploration.

Writing requirements down improves them. A design document works like a blueprint,
making weak assumptions visible before a team spends months building.
[[cite:ml-system-design=>ML System Design Playbook]]
This is why written design docs matter for production systems. The same
front-end scoping and stakeholder alignment work is covered in the
[[data-science-project-management=>Data Science Project Guide]] before a design
becomes production ML.

## Data, Labels, and Features

Data strategy is part of the system design, not a downstream task. Data
availability, processing, features, and data lakes come before the design reaches
model architecture.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]
The same design work raises practical questions about labels, class imbalance,
model selection, and validation.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]

Feature design also decides whether training and serving can stay consistent.
Features matter more than model architecture. Many production systems fail when
the team can't compute the right features at prediction time.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
That concern connects ML system design to
[[feature-stores=>feature stores]],
[[data engineering platforms]],
[[data quality and observability]],
and [[batch-vs-streaming=>batch versus streaming]].

Data access, unmet requirements, and deployment failures are common reasons ML
products stall.
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]
A design that ignores data ownership or data quality leaves a major risk for
implementation.

## Baselines and Model Choice

Baselines clarify the minimum useful comparison before a team commits to a
model family.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Simple baselines validate hypotheses quickly.
[[cite:ml-system-design=>ML System Design Playbook]][[cite:from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership@28:46=>Applied ML Leadership]]
Competition practice reinforces the same habit for production ML. Iterate from
EDA, validation, baselines, and infrastructure. Don't look for a single
modeling shortcut.
[[cite:kaggle-grandmaster-to-production-ml-and-education@21:42=>Production ML from Kaggle]][[cite:kaggle-grandmaster-to-production-ml-and-education@61:48=>Production ML from Kaggle]]

Model choice comes after that baseline. A team may choose a rule or a linear
model. It may also choose a tree model or an embedding system. A recommender,
ranking model, or deep model may be enough for other cases.
For a dedicated reference on ranking and recommendation,
[[book:20210802-practical-recommender-systems=>Practical Recommender Systems]]
by Kim Falk covers the data, algorithms, and evaluation patterns behind
recommender design choices.

The team can only make that choice after it understands the decision, data,
and latency. It also has to understand evaluation and failure cost. Practical ML
decisions stay separate from research-level detail for that reason.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Competition practice transfers to production through system-level discipline.
Validation, reproducible iteration, infrastructure, and error analysis transfer
more directly than leaderboard-specific techniques.
[[cite:kaggle-grandmaster-to-production-ml-and-education@22:45=>Production ML from Kaggle]]

## Serving and Runtime Architecture

Serving mode changes the system because batch scoring and online APIs create
different reliability requirements. Streaming features, edge inference, and human
review paths add more constraints.

Serving choice reaches operations because live APIs and precomputed predictions
create different freshness, latency, cost, and failure-handling paths. Live calls
fit request-time context, while precomputed outputs fit looser freshness needs
and tighter runtime budgets.
[[cite:production-ml-pipelines-with-aws-and-kafka@31:33=>Production ML Pipelines with AWS and Kafka]]

Serving models and embeddings connect with MLOps roles.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Platform work separates batch inference, online serving, orchestration, and
production workflows.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The clearest constraint-driven example is edge and mobile ML. It forces teams to
account for latency, frames per second, and energy use. Teams also have to
account for model size, offline behavior, and runtime choices.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]

[[autonomous-driving-ai=>Autonomous driving AI]] perception adds the same
system-design pressure in a physical vehicle. A team choosing
[[camera-first-vs-lidar-autonomous-driving=>camera-first vs LiDAR]] has to
connect sensor cost with redundancy. It also has to plan labeling, validation,
and on-vehicle inference together.
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Applying Computer Vision Research]]
In those systems,
[[machine learning infrastructure]]
includes more than cloud deployment. It also includes the runtime where the
prediction happens.

Real-time serving isn't the mature default. Real-time and batch data flow are
compared as alternatives.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]
Platform pieces are justified only when repeated use cases warrant them.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

After teams choose the architecture, they still have to move notebook
exploration into reusable code and data paths. They also need evaluation gates,
serving, and monitoring. The
[[notebook-to-production-workflow=>Notebook to Production Workflow]] sequence
focuses on that handoff.

## Evaluation and Product Validation

Offline metrics don't complete the evaluation design because metrics and
baselines connect with business alignment. Proxy metrics matter too, and
production validation rests on A/B testing, causality, and human labels.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
The model may score well offline and still fail if it harms the product metric or
increases manual-review load.

In teaching-oriented system design examples, the product boundary is explicit.
Assignments such as bot detection center the problem and combine ML quality with
technical delivery. They also test teamwork and communication, so the evaluation
isn't only a single offline score.
[[cite:kaggle-grandmaster-to-production-ml-and-education@41:10=>Production ML from Kaggle]][[cite:kaggle-grandmaster-to-production-ml-and-education@46:50=>Production ML from Kaggle]]

Product experimentation adds randomization and assignment tracking. It also
uses A/A tests, metric selection, and power analysis.
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
Those topics matter when an ML system affects user-facing decisions and the team
needs causal evidence, not just offline accuracy.

For ML systems, those choices sit beside
[[evaluation]] and
[[experimentation]]. They also
inform [[a-b-testing=>A/B testing]] and
[[power analysis]].

## Monitoring, Drift, and Fallbacks

Monitoring belongs in the design because ML systems change when data, users, or
upstream systems change. Monitoring, distribution shift, and fallbacks are part
of production robustness.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
Data drift, concept drift, and prediction drift are distinct. Fallbacks are tied
to redundancy, simple baselines, and serving reliability.
[[cite:ml-system-design=>ML System Design Playbook]]

On the operating side, traceability and experiment capture round out the toolset.
So do model registry, serving, and monitoring.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
Those topics explain why ML system design has to name who responds when
[[model monitoring]] shows drift,
latency issues, or a broken upstream feed.

Use [[model-monitoring-vs-data-observability=>Model Monitoring vs Data Observability]]
for that ownership split. Model-behavior signals belong with the model owner.
Freshness, schema, lineage, and pipeline failures stay visible to the upstream
data owner.
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]

Fallbacks can be simple and still critical. A fallback may use a previous model,
a rule system, a cached recommendation, or a manual review path. The fallback may
also turn off an automated decision. The design has to say what the product does
when the model, feature pipeline, API, or data source is unavailable.

## Production Design Review

Before implementation, a design should name the decision the prediction changes.
It should also name the user affected by it. The review should cover the cost
of wrong output. Late output belongs there too. So do unavailable or biased
outputs.

Those questions work as a readiness test. The team should understand the
business problem before it chooses a model.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]][[cite:ml-system-design=>ML System Design Playbook]]

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

The review also covers mobile and edge constraints. These include latency,
battery, frame rate, and runtime limits.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]]

For interview practice, turn the same review questions into a timed answer plan
in the
[[machine-learning-system-design-interview=>Machine Learning System Design Interview guide]].

## Platform and Ownership

Single projects can start with simple pieces, but repeated ML systems push teams
toward shared platform capabilities. Those capabilities include experiment
tracking, model registry, and serving. They also include metadata, lineage, and
unified prediction logging.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Teams use these tools to reduce repeated design work when many systems need the
same guarantees.

Ownership is the other platform question. Accountability, responsibility areas,
and bus-factor risk belong in the design.
[[cite:ml-system-design=>ML System Design Playbook]]
Team structures and involving ML practitioners from requirements through testing
matter too.
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]
Platform teams use evangelists, technical leads, support models, and user
feedback.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

These angles complement each other. One-system design and shared
[[MLOps tools]] and platform adoption
are two sides of the same discipline. Teams need shared tools once many systems
repeat the same needs. Both fail when teams don't align around requirements,
vocabulary, documentation, and responsibility.

## Related Pages

ML system design links requirements to infrastructure and operations while
keeping evaluation close to interview practice.

- [[ML System Design Documents]]
- [[Machine Learning Infrastructure]]
- [[camera-first-vs-lidar-autonomous-driving=>camera-first vs LiDAR]]
- [[MLOps]]
- [[MLOps Architecture]]
- [[Model Monitoring]]
- [[Evaluation]]
- [[a-b-testing=>A/B Testing]]
- [[Data Engineering Platforms]]
- [[machine-learning-system-design-interview=>Machine Learning System Design Interview guide]]
- [[llm-system-design-interview=>LLM system design interview]]
