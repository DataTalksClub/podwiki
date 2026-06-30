---
layout: wiki
title: "Machine Learning System Design"
summary: "How DataTalks.Club episodes frame ML system design as a production discipline: problem framing, data strategy, baselines, evaluation, serving, monitoring, fallbacks, and ownership."
related:
  - MLOps
  - Machine Learning Infrastructure
  - ML System Design Documents
  - Model Monitoring
---

## Definition

Machine learning system design decides how an ML system should support a product
or business decision before teams commit to a model. A design names the decision
and data. It also names labels and the feature path. Then it names serving,
evaluation, monitoring, and ownership after release.

In [ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }})
[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) connects
fraud detection, recommendations, feature work, and metrics. He also treats A/B
tests, monitoring, fallbacks, and MLOps roles as design choices. In
[Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }})
[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }}) defines the
same work through goals, constraints, data flow, and trade-offs. That framing
matters when the system must run on mobile or edge devices.

## Common Definition

The common definition across the episodes is practical: design starts with the
decision and ends with an operable system. Teams don't design a fraud model or
recommender by choosing a model class first. The same holds for pricing, search,
and computer vision. They first name the product decision and users. Then they
name the failure cost, baseline, and path from data to prediction.

Valerii's interview episode makes this explicit at 13:58 and 16:43. The fraud
example turns into questions about probabilities and loss functions. It also
raises real-time requirements and class imbalance.

Arseny's episode adds the same framing at 7:54, 20:21, and 29:01. A team writes
goals and non-goals first. It then writes assumptions, metrics, and a solution
blueprint.

The term overlaps with [MLOps]({{ '/wiki/mlops/' | relative_url }}), but it isn't
identical. Machine learning system design decides what system should exist and
which constraints matter.

MLOps covers repeatable operating practices for deployment and reproducibility,
plus monitoring, retraining, and adoption. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) describes
those concerns through CI/CD, data versioning, containers, and adoption work.

## Guest Differences

Valerii treats system design as both an interview skill and a production habit.
In the interview episode at 20:33 and 24:28, he focuses on communication and
assumptions. He also covers baselines, metrics, and A/B testing. Interviewers
need to see how a candidate reasons through ambiguity.

In
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}),
he shifts from interviews to delivery. At 7:06 and 14:36, he argues that design
documents help projects fail early and align stakeholders. At 19:01, he says
teams should keep the design document alive as the system changes.

Arseny puts more weight on constraints and early risk. In his scalable systems
episode at 10:34, mobile and edge ML force teams to design around latency and
frames per second. They also account for energy use and offline behavior. At
14:49, he uses early tests to reduce unknown risks. At 37:15, he uses diagrams to
reason about data flow, dependencies, and batch versus real-time paths.

[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) approaches the same
topic through software engineering. In
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}),
she frames ML products as software systems with added uncertainty. At 10:54 and
29:42, the recurring problems are poor requirements and unrealistic expectations.
She also names data access and deployment gaps.

At 39:05, she moves the remedy toward shared vocabulary, documentation, and
engineering habits. That makes
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}) part of
ML system design, not a separate afterthought.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) and
Raphael focus on repeated design problems. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
Simon connects experiment tracking and model registries to platform design. He
also covers batch inference and online serving. He includes orchestration,
metadata, and lineage.

Raphael's MLOps episode at 23:01 and 27:56 adds adoption
and developer experience. At 51:21, he adds model serving and monitoring.

## Requirements and Constraints

An ML system design starts by naming the decision, users, and failure cost. In
Valerii's fraud-detection discussion at 13:58, a design has to account for false
positives and false negatives. It also has to account for real-time decisions and
manual review. In Arseny's
episode at 29:01, goals and non-goals turn vague requirements into metrics and
assumptions the team can challenge.

Good requirements also say when not to use ML. Valerii's interview episode at
52:25 treats "avoid ML" as a real design outcome when a heuristic, rule, or
existing product behavior is enough. That connects the page to
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) as a tool
choice, not a default answer.

Teams improve requirements when they write them down. Valerii's design-doc
episode at 7:06 and 8:39 compares a design document to a blueprint. It makes
weak assumptions visible before a team spends months building. This is why
[ML system design documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
matter for production systems.

## Data, Labels, and Features

Data strategy is part of the system design, not a downstream task. Arseny's
episode at 32:37 covers data availability, processing, features, and data lakes
before the design reaches model architecture. Valerii's interview episode at
16:43 and 44:11 turns the same idea into practical questions about labels, class
imbalance, model selection, and validation.

Feature design also decides whether training and serving can stay consistent.
At 47:52 in Valerii's interview episode, features matter more than model
architecture. Many production systems fail when the team can't compute the right
features at prediction time. That concern connects ML system design to
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [batch versus streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}).

Nadia's episode adds a software-engineering warning. At 10:54 and 29:42, she
names data access, unmet requirements, and deployment failures as common reasons
ML products stall. A design that ignores data ownership or data quality leaves a
major risk for implementation.

## Baselines and Model Choice

The podcast archive consistently treats baselines as design tools. In Valerii's
interview episode at 24:28 and 29:09, a baseline clarifies the minimum useful
comparison. It also helps the candidate show progress without pretending the
final model is obvious. In the design-doc episode at 55:13, Valerii recommends
simple baselines to validate hypotheses quickly.

Model choice comes after that baseline. A team may choose a rule or a linear
model. It may also choose a tree model or an embedding system. A recommender,
ranking model, or deep model may be enough for other cases.

The team can only make that choice after it understands the decision, data, and
latency. It must also understand evaluation and failure cost. This is why
Valerii's episode separates practical ML decisions from research-level detail at
31:58.

## Serving and Runtime Architecture

Serving mode changes the system because batch scoring and online APIs create
different reliability requirements. Streaming features, edge inference, and human
review paths add more constraints.

Valerii's interview episode at 50:57 connects serving models and embeddings with
MLOps roles. Simon's platform episode at 31:15 and 31:51 separates batch
inference, online serving, orchestration, and production workflows.

Arseny's episode gives the clearest constraint-driven example. At 10:34, edge and
mobile ML force teams to account for latency and frames per second. They also
have to account for energy use, model size, offline behavior, and runtime
choices.
In those systems,
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
includes more than cloud deployment. It also includes the runtime where the
prediction happens.

The archive doesn't treat real-time serving as the mature default. Arseny
compares real-time and batch data flow at 37:15. Simon recommends platform pieces
only when repeated use cases justify them. He returns to that point at 16:52,
17:14, 47:08, and 49:19.

## Evaluation and Product Validation

Offline metrics don't complete the evaluation design. Valerii's interview
episode at 24:28 and 40:11 connects metrics, baselines, business alignment, and
proxy metrics. At 57:23, he connects production validation to A/B testing,
causality, and human labels. The model may score well offline and still fail if
it harms the product metric or increases manual-review load.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the product
experimentation background in
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
At 8:13 and 24:44, he covers randomization and assignment tracking. At 27:52, he
covers A/A tests. At 33:23 and 37:44, he covers metric selection and power
analysis.
Those topics matter when an ML system affects user-facing decisions and the team
needs causal evidence, not just offline accuracy.

This connects the page to [evaluation]({{ '/wiki/evaluation/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}),
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[power analysis]({{ '/wiki/power-analysis/' | relative_url }}).

## Monitoring, Drift, and Fallbacks

Monitoring belongs in the design because ML systems change when data, users, or
upstream systems change. Valerii's interview episode at 46:02 covers monitoring,
distribution shift, and fallbacks as part of production robustness. In the
design-doc episode at 47:46, he separates data drift, concept drift, and
prediction drift. At 51:59, he links fallbacks to redundancy, simple baselines,
and serving reliability.

Raphael's MLOps episode adds the operating side by covering traceability and
experiment capture at 42:31, then model registry, serving and monitoring at
51:21. Those topics explain why ML system design has to name who responds when
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) shows drift,
latency issues, or a broken upstream feed.

Fallbacks can be simple and still critical. A fallback may use a previous model,
a rule system, a cached recommendation, or a manual review path. The fallback may
also turn off an automated decision. The design has to say what the product does
when the model, feature pipeline, API, or data source is unavailable.

## Platform and Ownership

Single projects can start with simple pieces, but repeated ML systems push teams
toward shared platform capabilities. Simon's platform episode covers experiment
tracking and model registry at 29:41 and 30:32. At 31:15, he covers serving.

At 42:48 and 54:15, Simon covers metadata, lineage, and unified prediction
logging. Teams use these tools to reduce repeated design work when many systems
need the same guarantees.

Ownership is the other platform question. Valerii's design-doc episode at 24:37
and 31:59 covers accountability, responsibility areas, and bus-factor risk.
Nadia's episode at 36:28 and 56:55 discusses team structures and involving ML
practitioners from requirements through testing. Raphael's episode at 16:58 and
23:01 shows how platform teams use evangelists and technical leads. At 27:56, he
adds support models and feedback from users.

These episodes mostly complement each other. Valerii and Arseny focus on one
system's design, while Simon and Raphael focus on shared
[MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}) and platform adoption.
Teams need those tools once many systems repeat the same needs. Nadia explains
why both fail when teams don't align around requirements, vocabulary,
documentation, and responsibility.

## Related Pages

These pages expand the system-design decisions above.

- [ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Machine Learning System Design Interview article]({{ '/guides/machine-learning-system-design-interview/' | relative_url }})
