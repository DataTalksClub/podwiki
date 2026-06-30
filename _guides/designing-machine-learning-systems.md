---
layout: article
title: "Designing Machine Learning Systems: A Practical Archive-Backed Guide"
keyword: "designing machine learning systems"
summary: "A practical guide to designing machine learning systems with podcast-backed advice on problem framing, data strategy, baselines, serving, monitoring, ownership, and tradeoffs."
related_wiki:
  - Machine Learning System Design
  - ML System Design Documents
  - Machine Learning Engineer Role
  - MLOps
  - DataOps
  - ML Platforms
  - Model Monitoring
  - Production
---

Designing machine learning systems means deciding how a model-backed product
will behave before the team invests in training, serving, and platform work. A
useful design names the decision the model changes and the users affected by
that decision. It names the data and labels, plus the baseline to beat. It
records the serving path and monitoring plan. It also names the people who will
own the system after launch.

The DataTalks.Club archive treats this as a production discipline. In
[Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}),
[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }}) frames ML
system design around goals and non-goals. He also covers assumptions,
constraints, data strategy, and system diagrams.

In
[ML System Design]({{ '/podcasts/ml-system-design/' | relative_url }}),
[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) uses design
documents as a fail-fast tool. A good design can show that a project isn't
ready. It can also show that a simpler baseline is enough, or that ownership is
missing.

For a compact reference page, see
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
For interview-specific practice, see
[Machine Learning System Design Interview]({{ '/guides/machine-learning-system-design-interview/' | relative_url }}).
For design-document structure, use
[ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }}).

## Start With the Decision

The first design question isn't "which model should we use?" It's "what
decision changes because of the prediction?" A fraud model may block a
transaction, send it to review, or adjust a risk score. A recommender may choose
which items a user sees next. A churn model may tell a customer-success team
which account to contact.

Each decision changes the rest of the system. Fraud at checkout can require
online serving and calibrated probabilities. It may also need thresholds,
delayed labels, class imbalance handling, and a human-review queue.

Valerii walks through those constraints in
[Machine Learning System Design Interview]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
where the fraud example connects product action to labels and features. It then
connects the same case to metrics and A/B tests. Monitoring, serving, and
MLOps roles come next.

The same decision-first habit applies outside interviews. In Arseny's
[scalable ML systems episode]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}),
edge and mobile ML create constraints that a model-only plan would miss. Those
constraints include latency and frame rate. They also include battery use,
hardware support, and development time.

The design needs to say what "real time" means for the product. Sometimes the
right answer is fewer model calls or interpolation. Sometimes it's caching or a
smaller model instead of a larger architecture.

Write down goals and non-goals before choosing the model class. Record
assumptions, risks, and constraints too. That keeps the design tied to the
product and exposes the unknowns that need experiments.

## Design the Data and Label Path

Data strategy is part of the ML system.

The design should answer practical questions:

1. Which source systems provide training data?
2. Who owns each source and transformation?
3. How fresh do features need to be?
4. When do labels arrive?
5. Can training features be computed the same way at serving time?

When labels arrive late, evaluation and retraining change, and noisy labels
change threshold choice and human review. Missing online features can make an
offline model impossible to serve. Leakage can make the model look strong in
validation while failing in production.

These details decide whether the system can work.

The archive links this directly to
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) connects model
monitoring to upstream ETL, transformations, and data observability. When a
model behaves badly, the root cause may sit before inference. A source may have
changed, a schema may have shifted, a transformation may have broken, or the
world may have moved.

Feature reuse adds another design choice. In
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) describes feature
stores as infrastructure for reliable feature creation and retrieval. The
episode also covers serving, materialization, validation, and ownership. This
doesn't mean every ML project needs a feature store. Adopt one when the system
needs shared, production-grade features because teams repeat feature work or
serve online tabular models.

## Prove the Baseline

A baseline tells the team whether machine learning is needed and how much
complexity the next design must justify. It can be a rule or SQL query. It can
also be a manual workflow, a heuristic, a previous production system, or a
simple model.

Valerii's
[ML System Design]({{ '/podcasts/ml-system-design/' | relative_url }}) episode
ties baselines to fail-fast design. If the baseline solves the product problem,
the team can avoid expensive training, serving, and monitoring work. If the
baseline fails, the team learns what the more complex system must improve.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) makes the same argument
from production engineering work in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
He emphasizes maintainable solutions and modular code. He also emphasizes
business buy-in, subject matter expertise, and cost-benefit tradeoffs. Use SQL,
statistics, or a small model when they solve the decision. Add complexity only
when the gain pays for its operational cost.

## Choose Metrics for the Decision

Model metrics are useful only when they connect to the decision. A fraud system,
ranking system, forecasting system, and recommendation system need different
metric stories.

A practical design usually needs several layers:

1. Offline model metrics for the training loop.
2. Business or product metrics for the decision.
3. Guardrail metrics for latency, cost, fairness, trust, and operations.
4. Slice metrics for important user, item, region, or risk groups.
5. Monitoring metrics for post-launch drift and degradation.

Fraud detection shows why one metric isn't enough. The system may need
precision and recall, calibrated probabilities, and expected loss. It may also
need review-load limits, class-imbalance-aware evaluation, and online
validation. A recommender may optimize clicks while still needing guardrails for
diversity, cold starts, long-term value, and user trust.

At launch, system design connects to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[Production]({{ '/wiki/production/' | relative_url }}). Offline metrics guide
development, but production systems also need validation paths that match the
risk of a wrong decision. That may mean A/B tests, shadow mode, or backtesting.
It may also mean staged rollout or human review.

## Pick the Serving Path

Serving mode changes the architecture. Decide how the prediction reaches the
product before selecting tooling.

Common paths include:

1. Batch scoring: run predictions on a schedule and store the results.
2. Online API: compute predictions at request time.
3. Streaming: update features or predictions as events arrive.
4. Edge or mobile inference: run the model on-device.
5. Human-in-the-loop: send uncertain or high-cost cases to review.
6. Hybrid: precompute candidates or features, then score or rank online.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
separates batch inference from online serving. Batch inference often resembles
training infrastructure. It loads data, preprocesses it, runs inference, and
writes outputs.

Online serving needs latency budgets and API contracts. It also needs logging,
rollback, prediction schemas, and operational support. A platform that only
optimizes online endpoints may be wrong for teams whose main use cases are large
batch jobs.

The design should also specify degradation behavior. If an online model is
unavailable, the product may use cached predictions. If a feature is missing,
the system may fall back to a smaller feature set. If the data is corrupted, a
rule-based path may protect users better than returning a low-confidence model
output.

## Monitor the Whole System

Monitoring belongs in the design because a model can fail while the service is
still up.

At minimum, the system should log and monitor:

1. Model version.
2. Input and feature distributions.
3. Prediction distributions.
4. Latency, errors, and timeouts.
5. Data freshness, schema changes, and volume.
6. Delayed labels and business outcomes.
7. Important slices and high-risk segments.

Valerii's
[ML System Design]({{ '/podcasts/ml-system-design/' | relative_url }}) episode
distinguishes data drift, concept drift, and prediction drift, then connects
monitoring to fallback strategies. Danny's
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
extends that view upstream into data pipelines and profiling. Together, those
episodes make monitoring a system question, not only a dashboard question.

Monitoring also needs a response plan. Decide who receives alerts and what
counts as an incident. Then decide when to roll back, retrain, disable the ML
path, or switch to a fallback. Alerting without ownership only creates noise.

## Assign Ownership Early

Designing ML systems also means designing ownership.

Assign owners for:

1. Data sources and feature definitions.
2. Training code and model artifacts.
3. Evaluation and approval.
4. Deployment and rollback.
5. Monitoring and retraining.
6. Documentation and retirement.

Valerii's design-doc episode covers accountability and bus-factor risk.

Nadia Nahar's
[Software Engineering for Machine Learning]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})
episode explains why ML products create hidden technical debt. Requirements are
uncertain, data workflows change, testing is harder, and monitoring matters
after release. [Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) argues
for involving ML practitioners from requirements through testing instead of
handing off a notebook at the end.

That ownership model links directly to the
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).
The role isn't only model training. In production work, ML engineers often
bridge data and modeling. They also bridge serving, monitoring, software
engineering, and product constraints.

## Add Platform Only When It Solves Repeated Pain

Don't start by building a full ML platform. Design one useful system first,
then look for repeated friction across teams.

Simon frames MLOps as more than tooling.

In his [production ML platforms episode]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
experiment tracking and model registries often make sense early. Heavier
serving and governance layers depend on real use cases.

The same episode emphasizes user-centric platform design. Understand data
science workflows and notebooks before imposing a paved road. Deployment
patterns and regulatory constraints matter too. So do metadata, lineage, and
developer experience.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) adds the
adoption view in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
Platform teams need feedback loops and quick wins. They also need
reproducibility, CI/CD, monitoring, and support for product teams. They should
standardize repeated pain, not every experiment.

Use [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) when multiple
systems need shared training or registry paths. Use it for serving and
monitoring too. Governance and developer experience may belong there as well.

Use
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
when the design depends on compute and orchestration. It also applies to
containers and cloud. GPU work, batch jobs, and online serving infrastructure
belong there too.

## Make the Tradeoffs Explicit

Good ML system design makes tradeoffs visible.

- Batch vs real time: batch is easier to operate and fits churn scoring,
  lead scoring, forecasting, and many periodic recommendations. Real-time
  serving is justified when the product decision needs an immediate prediction,
  such as fraud at checkout or ranking at request time.
- Simple vs sophisticated: simple systems are easier to explain and test. They
  are also easier to monitor and maintain. Use a complex model only when it
  improves the decision enough to justify the extra operating cost.
- Accuracy vs cost: the best offline score may require expensive features,
  large models, GPU serving, or slow inference. The design should show whether
  the added lift changes the business decision enough.
- Flexibility vs standardization: product teams need freedom while discovering
  the right design, while mature teams need standard deployment, logging, and
  monitoring. Registry and rollback paths matter too.
- Automation vs human review: automation reduces manual work, but ambiguous or
  high-cost cases may need review queues. Teams often use them for fraud and
  moderation, and the same control can help in credit or healthcare workflows.

The archive's recurring lesson is that ML design isn't a model diagram. Teams
make the model useful after launch by choosing the right product and data paths.
They also need the right modeling, serving, monitoring, and ownership paths.

## Design Review Checklist

Use this checklist before implementation:

1. Decision: name the action that changes because of the prediction.
2. User: name who sees the output or depends on it.
3. Cost of failure: describe wrong, late, or biased outputs. Include
   unavailable outputs too.
4. Goals and non-goals: write what matters now and what's out of scope.
5. Data: list sources, labels, freshness requirements, and owners.
6. Baseline: name the simple method that sets the comparison point.
7. Metrics: choose offline, online, and business metrics. Add guardrail and
   slice metrics.
8. Model path: choose a model class that fits the decision and constraints.
9. Serving: choose batch, online, streaming, or edge. Add human review or a
   hybrid path when needed.
10. Validation: choose offline tests, A/B tests, or shadow mode. Add backtests
    or human review when needed.
11. Monitoring: name what you log, alert on, and investigate.
12. Fallback: define what happens when the model, data, feature pipeline, or
    service fails.
13. Ownership: name who deploys, monitors, and retrains. Also name who rolls
    back, updates docs, and retires the system.
14. Platform needs: identify repeated pieces that should become shared tools,
    templates, or platform paths.

Continue through the archive with [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}). Use
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}) for the operating layer.
