---
layout: wiki
title: "Metrics"
summary: "How DataTalks.Club podcast guests define metrics for product decisions, ML systems, monitoring, experiments, and business impact."
related:
  - Evaluation
  - A/B Testing
  - Product Analytics
  - Model Monitoring
  - Data Product Management
  - Machine Learning System Design
---

Metrics are numerical decision rules. They name what a team wants to improve
and what damage it must avoid. They also tell a team when a model, experiment,
dashboard, or [[data-products|data product]] is
good enough to ship. Across the DataTalks.Club discussions, a metric needs a
unit and a grain. It also needs a time window, an owner, and a decision.

The topic sits between [[evaluation]]
and [[product analytics]]. It
also overlaps with [[a-b-testing|A/B testing]],
[[causal inference]],
[[model monitoring]], and
[[data product management]].
[[person:adamsroka|Adam Sroka]] frames KPI design as a
cost-and-impact comparison in
[[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy at 12:06-30:30]].
[[person:jakobgraff|Jakob Graff]] shows why an
experiment metric has to match the rollout decision in
[[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing at 14:27-37:44]].
[[person:linaweichbrodt|Lina Weichbrodt]] ties KPIs,
service levels, feedback, and feature drift together in
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring at 4:50-29:23 and 46:28-49:28]].

## Metrics as Decision Rules

A metric should connect a measurable signal to a decision. The same metric name
can mislead teams when each team measures it differently. One team may use
account-level monthly revenue. Another may use user-level daily conversion. A
third may use a delayed label after a support case closes.

Sroka makes this practical in
[[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy at 12:06-30:30]].
He moves from "measurement matters" into merit functions and comparable units.
He also covers sales pipeline metrics, professional services metrics, vanity
metrics, and competing KPIs.

A revenue KPI can be valid. So can an operational burn-down, margin-aware
composite, or safety threshold. They don't answer the same question.

Graff gives the experimentation version of the same rule. In
[[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing at 14:27-18:06]],
a subscription-versus-points change can look different under revenue per user
than under conversion. Retention and long-term value can favor a different
rollout choice. The metric is part of the product choice, not a reporting
detail after the test. Metric design belongs in
[[experimentation]] and
[[power analysis]] because an
unstable or underpowered metric can't support the launch decision.

## Metric Failure Modes

Metrics fail in different ways depending on the system. Sroka's KPI discussion
warns that teams can optimize easy numbers that don't change ROI. They can also
design KPIs that people can game
([[podcast:ml-engineering-kpis-and-metrics-strategy|22:41-37:19]]).
That risk belongs with [[data product management]]
because roadmap and prioritization decisions can drift toward visible activity
instead of impact.

Graff worries about statistical reliability. He warns against noisy metrics,
too many primary metrics, seasonality, and underpowered experiments in
[[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing at 30:05-40:23]].
For an [[a-b-testing|A/B test]], the metric fails
when it can't support a causal rollout decision.

[[person:aleksandermolak|Aleksander Molak]] adds an
intervention boundary in
[[podcast:causal-inference-for-machine-learning|Causal Inference for Real-World ML at 32:40-43:25]].
A model can predict an outcome well and still be the wrong tool for deciding who
receives a treatment, discount, recommendation, or marketing message. Teams
need policy metrics, refutation tests, and sometimes A/B validation before they
trust an intervention claim.

Weichbrodt adds the operational failure mode. A metric is weak when nobody can
respond to it. Her MLOps discussion ties project intake and KPIs to stakeholder
fears. It also covers service levels, post-mortems, monitoring signals, and
recovery work
([[podcast:human-centered-mlops-and-model-monitoring|4:50-29:23]]).
That places metric ownership next to
[[MLOps]] and
[[production]], not only dashboard
design.

## Product Metrics and Experiments

Product metrics describe user behavior and product value through activation,
conversion, retention, and engagement. They also cover churn, revenue, and usage
depth. They depend on consistent event definitions, so they overlap with
[[event tracking]],
[[tracking plans]], and
[[data-led-growth|data-led growth]].

Graff's monetization example shows why product teams choose the metric before
interpreting an experiment. One change can support one conclusion under
short-term revenue and another under conversion, retention, or customer lifetime
value
([[podcast:ab-testing-and-product-experimentation|14:27-18:06]]).
He also covers assignment tracking, A/A tests, and traffic splitting before
statistical tests
([[podcast:ab-testing-and-product-experimentation|24:44-30:05]]).
Those checks make product metrics trustworthy enough for experiments rather than
post-hoc storytelling.

Experiment metrics need one primary decision metric and a small set of
guardrails. The primary metric answers whether the team should ship the change.
Guardrails catch harm such as churn, latency, reliability problems, or degraded
user experience. They can also catch revenue cannibalization.

Graff recommends simple first tests and warns against many primary metrics
because the decision becomes unclear
([[podcast:ab-testing-and-product-experimentation|30:05-33:23]]).
He then links metric stability and seasonality to sample size. Test duration
also shapes whether an uplift number is believable
([[podcast:ab-testing-and-product-experimentation|33:23-40:23]]).

Metric distributions also affect the statistical test. Graff discusses
histograms and tails in
[[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing at 40:23-59:08]].
He also covers nonparametric options, p-values, Bayesian intervals, and multiple
comparisons. That's where experiment metrics meet
[[a-a-testing|A/A testing]],
[[experimentation and causal inference]],
and [[evaluation]].

## ML Metrics and System Design

ML metrics measure model behavior, but the podcast discussions repeatedly tie
model scores back to product and business outcomes. Accuracy, precision, recall,
and ranking quality need that context. So do calibration, uplift, latency, and
cost. A higher offline score matters only
when it improves the decision the system supports.

[[person:arsenykravchenko|Arseny Kravchenko]]
describes [[machine learning system design]]
as problem-first work in
[[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems at 29:01-32:37]].
He places goals, non-goals, assumptions, and baselines before implementation
detail. Metrics, data strategy, and pipeline components come next. Teams define
the product scenario first. They then choose offline and online metrics before
they design serving and monitoring around those metrics.

[[person:rishabhbhargava|Rishabh Bhargava]] connects ML
metrics to live business analysis in
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML at 28:42-32:47]].
He discusses model experiments, A/B testing, and shadow mode. He then connects
segmentation, uplift, and root-cause analysis to live results. The model metric
isn't enough. Analysts still need to explain which segments moved and whether
the model changed the business outcome.

[[person:benwilson|Ben Wilson]] adds a cost-benefit
constraint in
[[podcast:machine-learning-engineering-production-best-practices|Machine Learning Engineering Best Practices at 32:03-55:41]].
He emphasizes timeboxed bake-offs, simple baselines, feature engineering, and
testing. ML teams should compare model metrics against maintainability, cloud
cost, and delivery risk instead of treating a higher offline score as the only
success criterion.

## Monitoring Metrics

Monitoring metrics watch whether a deployed system is still healthy. For ML
systems, teams watch input data quality and feature distributions. They also
watch prediction distributions, latency, errors, and service levels. Teams add
delayed labels, user feedback, and business proxy outcomes because many model
failures don't show up as immediate infrastructure errors.

Weichbrodt's episode is the clearest monitoring anchor. She starts project
intake with business cases and KPIs, then moves to stakeholder fears and service
levels. She also covers incident response and live test sets. Small A/B tests,
feature drift, logs, and reproducibility sit in the same discussion
([[podcast:human-centered-mlops-and-model-monitoring|4:50-29:23 and 46:28-49:28]]).
Her framing links [[model monitoring]]
to both [[MLOps]] and
[[production]].

Monitoring metrics should also name who acts because a latency alert differs
from a feature-drift alert. A user complaint also differs from a business KPI
moving in the wrong direction. Weichbrodt's post-mortem sections tie metric movement
to facts, investigation steps, action items, and operating changes
([[podcast:human-centered-mlops-and-model-monitoring|27:14-42:03]]).

## Business Metrics and Data Product Impact

Business metrics translate data and ML work into money, risk, time, and
customer value. They include revenue, margin, and weighted pipeline. Burn-down
rate is another business metric.

They can also track maintainability of earnings, downtime, and service
reliability. Time saved and ROI belong here too.
For [[data products]], these metrics
explain why a technically correct dashboard, model, or pipeline deserves
continued investment.

Sroka's KPI episode is the strongest business-metrics discussion. In
[[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy at 15:11-51:12]],
he covers merit functions, project prioritization, and comparable units. He also
covers sales pipeline metrics, professional services metrics, and top-down KPI
alignment. Competing KPIs and composite metrics appear in the same discussion.

Workshop design and dashboard visibility also matter in Sroka's framing. So do
North Star metrics, threshold metrics, health metrics, and data team metrics.
Later, he links data-team work to pound-value or time-saved estimates
([[podcast:ml-engineering-kpis-and-metrics-strategy|51:12-56:35]]).
That matters for [[data product management]]
because the impact story has to survive prioritization, funding, and adoption
decisions.

Molak adds that business metrics aren't automatically causal metrics. In
[[podcast:causal-inference-for-machine-learning|Causal Inference for Real-World ML at 32:40-43:25]],
teams compare policies on the same business metric. They still need estimator
checks and sometimes experimental validation before trusting the intervention
claim.

## Related Pages

These pages cover adjacent metric decisions in more detail.

- [[Evaluation]]
- [[a-b-testing|A/B Testing]]
- [[a-a-testing|A/A Testing]]
- [[Power Analysis]]
- [[Experimentation]]
- [[Experimentation and Causal Inference]]
- [[Causal Inference]]
- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
- [[Event Tracking]]
- [[Model Monitoring]]
- [[Machine Learning System Design]]
- [[MLOps]]
- [[Data Products]]
- [[Data Product Management]]
