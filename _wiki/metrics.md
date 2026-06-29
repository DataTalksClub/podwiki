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

## Definition and Scope

Metrics are decision rules expressed as numbers. They define what a team is
trying to improve and what failure looks like. They also tell a team when a
model, experiment, dashboard, or data product is good enough to act on.

DataTalks.Club guests treat metrics as more than dashboard fields.
[Adam Sroka]({{ '/people/adamsroka/' | relative_url }})
frames KPI design as a way to compare impact and cost. He also covers tradeoffs in
[the metrics strategy episode at 12:06-30:30]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) shows why a product
experiment needs a metric that matches the rollout decision in
[the product analytics and A/B testing episode at 14:27-37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) connects
business KPIs and service levels with user feedback. She also covers feature drift in
[the human-centered MLOps episode at 4:50-29:23 and 46:28-49:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).

Metrics connect
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[evaluation]({{ '/wiki/evaluation/' | relative_url }}),
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}). They also
connect [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[data product management]({{ '/wiki/data-product-management/' | relative_url }}).

## Common Definition

The common definition is practical: a metric should connect a measurable signal
to a decision. It needs a unit, a grain, a time window, and an owner. Without
those details, two teams can use the same metric name and make different
decisions.

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) makes this explicit
when he moves from "measurement matters" into merit functions and comparable
units. He covers sales pipeline and professional services metrics. He also
covers KPIs, vanity metrics, and competing KPIs in
[the KPI design episode at 12:06-30:30]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
His examples show why a KPI needs a clear business interpretation. A team
shouldn't treat revenue-based KPIs, operational burn-down, margin-aware
composites, and safety thresholds as interchangeable numbers.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the
experimentation version of the same rule. A subscription-versus-points test can
look different depending on the team's target. Revenue per user, conversion,
retention, and long-term value support different rollout choices
([product analytics and A/B testing at 14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
The metric is part of the product choice, not a reporting detail after the test.

## Guest Differences

Guests differ in which failure they worry about first. Sroka focuses on
business alignment, and he warns that teams can optimize easy numbers that
don't change ROI. They can also design KPIs that people can game
([KPI design at 22:41-37:19]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).

Graff focuses on statistical reliability. He warns against noisy metrics, too
many primary metrics, seasonality, and underpowered experiments
([A/B testing at 30:05-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
For him, a metric fails when it can't support a causal decision.

[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) focuses on
intervention validity. In
[the causal inference episode at 32:40-43:25]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he separates policy metrics from ordinary predictive validation. A model can
predict an outcome well and still be the wrong tool for deciding who receives a
treatment, discount, recommendation, or marketing message.

Weichbrodt focuses on whether people can respond when a metric changes. Her
MLOps discussion ties KPIs to project intake and stakeholder fears. It also
connects service levels, post-mortems, and monitoring signals
([human-centered MLOps at 4:50-29:23]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
For her, a metric fails when it doesn't help a team debug, communicate, or
recover.

## Product Metrics

Product metrics describe user behavior and product value through activation,
conversion, retention, and engagement. They also cover churn, revenue, and
usage depth.
They depend on consistent event definitions, so they connect directly to
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}).

Graff's product analytics episode uses a monetization change to show why
product teams must choose the metric before interpreting a result. One
experiment can support one conclusion under short-term revenue and another
under conversion, retention, or customer lifetime value
([product analytics and A/B testing at 14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

Product metrics also need a measurement system. Graff covers assignment
tracking, A/A tests, and traffic splitting before he moves to statistical tests
([A/B testing at 24:44-30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
Those checks make product metrics trustworthy enough for
[experimentation]({{ '/wiki/experimentation/' | relative_url }}) and
[data-led growth]({{ '/wiki/data-led-growth/' | relative_url }}).

## ML Metrics

ML metrics measure model behavior, but the podcast discussions repeatedly tie
them back to product or business outcomes. Accuracy, precision, recall, and
ranking quality only matter when they match the decision the system supports.
The same rule applies to calibration, uplift, latency, and cost.

[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }})
describes ML system design as problem-first work, and he places goals,
non-goals, and assumptions before implementation details. He then adds
baselines, metrics, data strategy, and pipeline components in
[the scalable ML systems episode at 29:01-32:37]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}).
That matches the
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
sequence: define the product scenario, choose offline and online metrics, then
design serving and monitoring around those metrics.

[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) connects
ML metrics to live business analysis in
[the production ML episode at 28:42-32:47]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}).
He discusses model experiments, A/B testing, and shadow mode. He then connects
segmentation, uplift, and root-cause analysis to live results. The model metric
isn't enough. Analysts
still need to explain which segments moved and whether the model changed the
business outcome.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) adds a cost-benefit
constraint in
[the practical ML engineering episode at 32:03-55:41]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
He emphasizes timeboxed bake-offs, simple baselines, feature engineering, and
testing. ML teams should compare model metrics against maintainability, cloud
cost, and delivery risk instead of treating a higher offline score as the only
success criterion.

## Monitoring Metrics

Monitoring metrics watch whether a deployed system is still healthy. For ML
systems, teams watch input data quality, feature distributions, and prediction
distributions. They also track latency, errors, and service levels. Teams
complete the picture with delayed labels, user feedback, and business proxy
outcomes.

Weichbrodt's MLOps episode is the clearest monitoring anchor. She starts project
intake with business cases and KPIs, then moves to stakeholder fears and service
levels. She also covers incident response, live test sets, and small A/B tests.
Feature drift, logs, and reproducibility sit in the same monitoring discussion
([human-centered MLOps at 4:50-29:23 and 46:28-49:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
That connects [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
to both [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[production]({{ '/wiki/production/' | relative_url }}).

Monitoring metrics should also tell a team who needs to act. A latency alert is
different from a feature drift alert. A user complaint is different from a
business KPI moving in the wrong direction. Weichbrodt's post-mortem sections
tie metric movement to facts, investigation steps, action items, and operating
changes
([human-centered MLOps at 27:14-42:03]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

## Experiment Metrics

Experiment metrics need one primary decision metric and a small set of
guardrails. The primary metric answers whether the team should ship the change.
Guardrails catch harm such as churn, latency, and reliability problems. They
can also catch revenue cannibalization or degraded user experience.

Graff recommends simple first tests and warns against many primary metrics
because the decision becomes unclear
([A/B testing at 30:05-33:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
He also explains why metric stability, seasonality, and test duration matter.
Sample size and [power analysis]({{ '/wiki/power-analysis/' | relative_url }})
also matter before a team trusts an uplift number
([A/B testing at 33:23-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

The same episode links metric distributions to test choice. Histograms and tails
affect which statistical test fits the data. Nonparametric options and p-values
change how a team communicates uncertainty. Bayesian intervals and multiple
comparisons change the conversation too
([A/B testing at 40:23-59:08]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
That's why experiment metrics sit next to
[A/A testing]({{ '/wiki/a-a-testing/' | relative_url }}),
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}),
and [evaluation]({{ '/wiki/evaluation/' | relative_url }}).

## Business Metrics

Business metrics translate data and ML work into money, risk, time, or customer
value. They include revenue and margin, plus weighted pipeline and burn-down
rate. They also include maintainability of earnings and downtime. Service
reliability, time saved, and ROI belong in the same group.

Sroka's KPI episode is the strongest business-metrics discussion. He starts
with merit functions, project prioritization, and comparable units. He then
covers sales pipeline metrics and professional services metrics. He also covers
top-down KPI alignment, competing KPIs, and composite metrics.

Later sections cover workshop design and dashboard visibility. They also cover North Star
metrics, threshold metrics, health metrics, and data team metrics
([KPI design at 15:11-51:12]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).

He also links data-team work to pound-value or time-saved estimates in
[the same episode at 51:12-56:35]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
That matters for [data products]({{ '/wiki/data-products/' | relative_url }})
and [data product management]({{ '/wiki/data-product-management/' | relative_url }})
because a technically correct dashboard, model, or pipeline still needs an
impact story.

Molak adds that business metrics aren't automatically causal metrics. In
[the causal inference episode at 32:40-43:25]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
teams compare policies on the same business metric. They also need refutation
tests, estimator checks, and sometimes A/B validation before they trust an
intervention claim.

## Related Pages

Metrics sit next to these topic pages in the wiki graph.

- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
