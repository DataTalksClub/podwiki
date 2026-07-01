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
dashboard, or [data product]({{ '/wiki/data-products/' | relative_url }}) is
good enough to ship. Across the DataTalks.Club discussions, a metric needs a
unit and a grain. It also needs a time window, an owner, and a decision.

The topic sits between [evaluation]({{ '/wiki/evaluation/' | relative_url }})
and [product analytics]({{ '/wiki/product-analytics/' | relative_url }}). It
also overlaps with [A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[data product management]({{ '/wiki/data-product-management/' | relative_url }}).
[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) frames KPI design as a
cost-and-impact comparison in
[KPI Design & Metrics Strategy at 12:06-30:30]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) shows why an
experiment metric has to match the rollout decision in
[Product Analytics & A/B Testing at 14:27-37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) ties KPIs,
service levels, feedback, and feature drift together in
[Human-Centered MLOps and Model Monitoring at 4:50-29:23 and 46:28-49:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).

## Metrics as Decision Rules

A metric should connect a measurable signal to a decision. The same metric name
can mislead teams when each team measures it differently. One team may use
account-level monthly revenue. Another may use user-level daily conversion. A
third may use a delayed label after a support case closes.

Sroka makes this practical in
[KPI Design & Metrics Strategy at 12:06-30:30]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
He moves from "measurement matters" into merit functions and comparable units.
He also covers sales pipeline metrics, professional services metrics, vanity
metrics, and competing KPIs.

A revenue KPI can be valid. So can an operational burn-down, margin-aware
composite, or safety threshold. They don't answer the same question.

Graff gives the experimentation version of the same rule. In
[Product Analytics & A/B Testing at 14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
a subscription-versus-points change can look different under revenue per user
than under conversion. Retention and long-term value can favor a different
rollout choice. The metric is part of the product choice, not a reporting
detail after the test. Metric design belongs in
[experimentation]({{ '/wiki/experimentation/' | relative_url }}) and
[power analysis]({{ '/wiki/power-analysis/' | relative_url }}) because an
unstable or underpowered metric can't support the launch decision.

## Metric Failure Modes

Metrics fail in different ways depending on the system. Sroka's KPI discussion
warns that teams can optimize easy numbers that don't change ROI. They can also
design KPIs that people can game
([22:41-37:19]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).
That risk belongs with [data product management]({{ '/wiki/data-product-management/' | relative_url }})
because roadmap and prioritization decisions can drift toward visible activity
instead of impact.

Graff worries about statistical reliability. He warns against noisy metrics,
too many primary metrics, seasonality, and underpowered experiments in
[Product Analytics & A/B Testing at 30:05-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
For an [A/B test]({{ '/wiki/a-b-testing/' | relative_url }}), the metric fails
when it can't support a causal rollout decision.

[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) adds an
intervention boundary in
[Causal Inference for Real-World ML at 32:40-43:25]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}).
A model can predict an outcome well and still be the wrong tool for deciding who
receives a treatment, discount, recommendation, or marketing message. Teams
need policy metrics, refutation tests, and sometimes A/B validation before they
trust an intervention claim.

Weichbrodt adds the operational failure mode. A metric is weak when nobody can
respond to it. Her MLOps discussion ties project intake and KPIs to stakeholder
fears. It also covers service levels, post-mortems, monitoring signals, and
recovery work
([4:50-29:23]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
That places metric ownership next to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[production]({{ '/wiki/production/' | relative_url }}), not only dashboard
design.

## Product Metrics and Experiments

Product metrics describe user behavior and product value through activation,
conversion, retention, and engagement. They also cover churn, revenue, and usage
depth. They depend on consistent event definitions, so they overlap with
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[data-led growth]({{ '/wiki/data-led-growth/' | relative_url }}).

Graff's monetization example shows why product teams choose the metric before
interpreting an experiment. One change can support one conclusion under
short-term revenue and another under conversion, retention, or customer lifetime
value
([14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
He also covers assignment tracking, A/A tests, and traffic splitting before
statistical tests
([24:44-30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
Those checks make product metrics trustworthy enough for experiments rather than
post-hoc storytelling.

Experiment metrics need one primary decision metric and a small set of
guardrails. The primary metric answers whether the team should ship the change.
Guardrails catch harm such as churn, latency, reliability problems, or degraded
user experience. They can also catch revenue cannibalization.

Graff recommends simple first tests and warns against many primary metrics
because the decision becomes unclear
([30:05-33:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
He then links metric stability and seasonality to sample size. Test duration
also shapes whether an uplift number is believable
([33:23-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

Metric distributions also affect the statistical test. Graff discusses
histograms and tails in
[Product Analytics & A/B Testing at 40:23-59:08]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
He also covers nonparametric options, p-values, Bayesian intervals, and multiple
comparisons. That's where experiment metrics meet
[A/A testing]({{ '/wiki/a-a-testing/' | relative_url }}),
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}),
and [evaluation]({{ '/wiki/evaluation/' | relative_url }}).

## ML Metrics and System Design

ML metrics measure model behavior, but the podcast discussions repeatedly tie
model scores back to product and business outcomes. Accuracy, precision, recall,
and ranking quality need that context. So do calibration, uplift, latency, and
cost. A higher offline score matters only
when it improves the decision the system supports.

[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }})
describes [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
as problem-first work in
[Building Scalable and Reliable Machine Learning Systems at 29:01-32:37]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}).
He places goals, non-goals, assumptions, and baselines before implementation
detail. Metrics, data strategy, and pipeline components come next. Teams define
the product scenario first. They then choose offline and online metrics before
they design serving and monitoring around those metrics.

[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) connects ML
metrics to live business analysis in
[From Analytics to Production ML at 28:42-32:47]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}).
He discusses model experiments, A/B testing, and shadow mode. He then connects
segmentation, uplift, and root-cause analysis to live results. The model metric
isn't enough. Analysts still need to explain which segments moved and whether
the model changed the business outcome.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) adds a cost-benefit
constraint in
[Machine Learning Engineering Best Practices at 32:03-55:41]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
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
([4:50-29:23 and 46:28-49:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
Her framing links [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
to both [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[production]({{ '/wiki/production/' | relative_url }}).

Monitoring metrics should also name who acts because a latency alert differs
from a feature-drift alert. A user complaint also differs from a business KPI
moving in the wrong direction. Weichbrodt's post-mortem sections tie metric movement
to facts, investigation steps, action items, and operating changes
([27:14-42:03]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

## Business Metrics and Data Product Impact

Business metrics translate data and ML work into money, risk, time, and
customer value. They include revenue, margin, and weighted pipeline. Burn-down
rate is another business metric.

They can also track maintainability of earnings, downtime, and service
reliability. Time saved and ROI belong here too.
For [data products]({{ '/wiki/data-products/' | relative_url }}), these metrics
explain why a technically correct dashboard, model, or pipeline deserves
continued investment.

Sroka's KPI episode is the strongest business-metrics discussion. In
[KPI Design & Metrics Strategy at 15:11-51:12]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}),
he covers merit functions, project prioritization, and comparable units. He also
covers sales pipeline metrics, professional services metrics, and top-down KPI
alignment. Competing KPIs and composite metrics appear in the same discussion.

Workshop design and dashboard visibility also matter in Sroka's framing. So do
North Star metrics, threshold metrics, health metrics, and data team metrics.
Later, he links data-team work to pound-value or time-saved estimates
([51:12-56:35]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).
That matters for [data product management]({{ '/wiki/data-product-management/' | relative_url }})
because the impact story has to survive prioritization, funding, and adoption
decisions.

Molak adds that business metrics aren't automatically causal metrics. In
[Causal Inference for Real-World ML at 32:40-43:25]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
teams compare policies on the same business metric. They still need estimator
checks and sometimes experimental validation before trusting the intervention
claim.

## Related Pages

These pages cover adjacent metric decisions in more detail.

- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
