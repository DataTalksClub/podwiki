---
layout: wiki
title: "Metrics"
summary: "Metrics for product decisions, ML systems, monitoring, experiments, and business impact."
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
dashboard, or [[data-products=>data product]] is good enough to ship. A metric
needs a unit and a grain. It also needs a time window, an owner, and a decision.

The topic sits between [[evaluation]] and [[product analytics]]. It also
overlaps with [[a-b-testing=>A/B testing]] and [[causal inference]], plus
[[model monitoring]] and [[data product management]]. KPI design works as a
cost-and-impact comparison[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Metrics]].
Experiment metrics have to match the rollout decision[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
Operational metrics connect KPIs, service levels, feedback, and feature
drift[[cite:human-centered-mlops-and-model-monitoring=>MLOps Monitoring]].

When teams add [[ai-powered-business-intelligence=>AI-powered BI]], they put
more pressure on metric ownership. AI answers and dashboard summaries need
governed KPI definitions. They also need visible trust states, not just fluent
text
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]].

In [[ai-for-finance-decision-support=>AI Finance Decision Support]], that means
finance teams need a clear business grain before they act on a forecast risk or
cash-flow warning. They also need a review owner. The same applies to
working-capital signals
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]].

## Metrics as Decision Rules

A metric should connect a measurable signal to a decision. The same metric name
can mislead teams when each team measures it differently. One team may use
account-level monthly revenue. Another may use user-level daily conversion. A
third may use a delayed label after a support case closes.

In SaaS, customer-success and data teams can use the same words. They may still
picture different product realities. Before analyzing usage, the team had to
agree what "good usage," "customer," and "churn" meant across
functions[[cite:data-professionals-business-skills-in-saas@12:19=>SaaS Business Skills]][[cite:data-professionals-business-skills-in-saas@18:00=>SaaS Business Skills]].
Teams should treat metric design as part of
[[business skills for data professionals]], not only SQL or dashboard work.

KPI design moves from "measurement matters" into merit functions and comparable
units. Sales pipeline metrics, professional services metrics, vanity metrics,
and competing KPIs need comparable units before teams can prioritize
work[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Metrics]].

A revenue KPI can be valid. So can an operational burn-down, margin-aware
composite, or safety threshold. They don't answer the same question.

Experiments have the same rule. A subscription-versus-points change can look
different under revenue per user than under conversion. Retention can favor a
different rollout choice, and long-term value can change the decision
again[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
The metric is part of the product choice, not a reporting detail after the
test. Metric design belongs in [[experimentation]] and [[power analysis]]
because an
unstable or underpowered metric can't support the launch decision.

## Metric Failure Modes

Metrics fail differently by system. Teams can optimize easy numbers that don't
change ROI or design KPIs that people can
game[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Metrics]].
That risk belongs with [[data product management]]
because roadmap and prioritization decisions can drift toward visible activity
instead of impact.

Experiment metrics fail when they're noisy or underpowered. They also fail when
teams use too many primary metrics or ignore
seasonality[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
For an [[a-b-testing=>A/B test]], the metric fails
when it can't support a causal rollout decision.

A model can predict an outcome well and still be the wrong tool for deciding who
receives a treatment, discount, recommendation, or marketing message. Teams
need policy metrics, refutation tests, and sometimes A/B validation before they
trust an intervention claim[[cite:causal-inference-for-machine-learning=>Causal ML]].

A metric is weak when nobody can respond to it. Project intake and KPIs have to
connect to stakeholder fears and service levels. Post-mortems, monitoring
signals, and recovery work belong in the same operational
system[[cite:human-centered-mlops-and-model-monitoring=>MLOps Monitoring]].
That places metric ownership next to [[MLOps]] and [[production]], not only
dashboard design.

## Product Metrics and Experiments

Product metrics describe user behavior and product value through activation,
conversion, retention, and engagement. They also cover churn, revenue, and usage
depth. They depend on consistent event definitions, so they overlap with
[[event tracking]],
[[tracking plans]], and
[[data-led-growth=>data-led growth]].

In SaaS, a usage metric only became useful after the team discussed what product
success meant. The team could use feature depth or graph complexity. It could
also use advanced feature use or integration into customer workflows.
Teams can use embedded integrations as lead indicators for stickiness because
those integrations can connect to lower churn and higher lifetime
value[[cite:data-professionals-business-skills-in-saas@15:46=>SaaS Business Skills]].

A leading indicator is useful only with a causal direction. The team needs to
explain which action or condition likely moves the customer toward the next
state.

For segment-level decisions, teams can use [[RFM Analysis]] to group customers
by recency, frequency, and monetary value. Those states support retention or
lifecycle work[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].

Product teams choose the metric before interpreting an experiment. The same
change can lead to one conclusion under short-term revenue and another under
conversion, retention, or customer lifetime value[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
Assignment tracking, A/A tests, and traffic splitting come before statistical
tests[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
Those checks make product metrics trustworthy enough for experiments rather than
post-hoc storytelling.
That metric-ownership boundary is one reason
[[product-analyst-vs-data-analyst=>product analyst vs data analyst]] separates
product-facing analysis from broader analyst work.

Experiment metrics need one primary decision metric and a small set of
guardrails. The primary metric answers whether the team should ship the change.
Guardrails catch harm such as churn, latency, reliability problems, or degraded
user experience. They can also catch revenue cannibalization.

Simple first tests help teams keep the decision clear, while too many primary
metrics make it unclear[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
Metric stability and seasonality affect sample size. Test duration also shapes
whether an uplift number is believable[[cite:ab-testing-and-product-experimentation=>Product Experiments]].

Metric distributions affect the statistical test because histograms and tail
behavior matter. Nonparametric options, p-values, Bayesian intervals, and
multiple comparisons influence how teams interpret the experiment
result[[cite:ab-testing-and-product-experimentation=>Product Experiments]].
That's where experiment metrics meet
[[a-a-testing=>A/A testing]],
[[experimentation and causal inference]],
and [[evaluation]].

## ML Metrics and System Design

ML metrics measure model behavior, but production ML work ties model scores
back to product and business outcomes. Accuracy, precision, recall, and ranking
quality need that context. So do calibration, uplift, latency, and cost. A
higher offline score matters only when it improves the decision the system
supports.

[[Machine learning system design]] starts with problem framing before
implementation. Teams define goals, non-goals, assumptions, and baselines before
implementation detail. Metrics, data strategy, and pipeline components come
next. Teams define the product scenario, then choose offline and online metrics.
Serving and monitoring follow those
metrics[[cite:building-scalable-and-reliable-machine-learning-systems=>Scalable ML Systems]].

ML metrics also need live business analysis. Model experiments, A/B testing, and
shadow mode need segmentation once results arrive. They also need uplift and
root-cause analysis. The model metric isn't enough. Analysts still need to explain which
segments moved and whether the model changed the business
outcome[[cite:production-ml-mlops-and-data-team-building=>Production ML]].

ML teams should compare model metrics against maintainability, cloud cost, and
delivery risk instead of treating a higher offline score as the only success
criterion. Teams can use timeboxed bake-offs, simple baselines, feature
engineering, and testing to keep the comparison
grounded[[cite:machine-learning-engineering-production-best-practices=>ML Engineering Practices]].

## Monitoring Metrics

Monitoring metrics watch whether a deployed system is still healthy. For ML
systems, teams watch input data quality and feature distributions. They also
watch prediction distributions, latency, errors, and service levels. Teams add
delayed labels, user feedback, and business proxy outcomes because many model
failures don't show up as immediate infrastructure errors.

Project intake starts with business cases and KPIs, then moves to stakeholder
fears and service levels. The same monitoring discussion includes incident
response, live test sets, and small A/B tests. It also includes feature drift,
logs, and reproducibility[[cite:human-centered-mlops-and-model-monitoring=>MLOps Monitoring]].
That links [[model monitoring]] to both [[MLOps]] and [[production]].

Monitoring metrics should also name who acts because a latency alert differs
from a feature-drift alert. A user complaint also differs from a business KPI
moving in the wrong direction. Post-mortems tie metric movement to facts,
investigation steps, action items, and operating changes[[cite:human-centered-mlops-and-model-monitoring=>MLOps Monitoring]].

## Business Metrics and Data Product Impact

Business metrics translate data and ML work into money, risk, time, and
customer value. They include revenue, margin, and weighted pipeline. Burn-down
rate is another business metric.

They can also track maintainability of earnings, downtime, and service
reliability. Time saved and ROI belong here too.
For [[data products]], these metrics
explain why a technically correct dashboard, model, or pipeline deserves
continued investment.

TV ads and physical banners can be hard to attribute directly. Timely traffic
spikes and post-purchase survey questions can become proxy evidence for campaign
measurement[[cite:building-and-scaling-data-team@45:39=>Data Team Scaling]].

That connects business metrics to [[product analytics]] and [[experimentation]],
and it also shows the measurement limit. When the channel can't emit clean
user-level events, the team still needs a measurement plan that states which
proxy signals it trusts.

Offline attribution can combine several weak signals rather than pretend a
perfect event stream exists. Surveys and community sampling can sit beside
traffic movement and campaign timing. Together, they help a marketing team
reason about TV, banners, or other channels that don't expose deterministic
user-level paths.
[[cite:building-and-scaling-data-team@45:39=>Data Team Scaling]]

The same proxy rule applies to internal data products. When direct ROI is hard
to instrument, teams can use time studies, before-and-after comparisons, and
surveys as early evidence. The metric is weaker than clean event tracking, but it
still gives prioritization a concrete starting point.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@42:18=>Last-Mile Data Delivery]]

Proxy metrics should name what they approximate. A stopwatch time study can
stand in for warehouse-process efficiency. An employee survey can stand in for a
workplace experience metric. The team should treat the proxy as decision
evidence, not as proof with the same strength as an experiment.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@42:18=>Last-Mile Data Delivery]]

Business-metrics work needs merit functions and project prioritization in
comparable units. Sales pipeline and professional services metrics sit beside
top-down KPI alignment. Competing KPIs and composite metrics belong in the same
discussion[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Metrics]].

Finance teams need the same governed KPI work in
[[ai-for-finance-decision-support=>AI finance decision support]]. AI can surface
a forecast warning only after the company names the revenue and pipeline
context. It also needs the cash-flow and working-capital context behind the
warning
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]].

Workshop design and dashboard visibility also matter. North Star metrics,
threshold metrics, health metrics, and data team metrics matter too. Data-team
work still has to connect to pound-value or time-saved
estimates[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Metrics]].
That matters for [[data product management]]
because the impact story has to survive prioritization, funding, and adoption
decisions.

Business metrics aren't automatically causal metrics. Teams can compare
policies on the same business metric and still need estimator checks. They may
also need experimental validation before trusting the intervention
claim[[cite:causal-inference-for-machine-learning=>Causal ML]].

## Related Pages


- [[Evaluation]]
- [[a-b-testing=>A/B Testing]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Experimentation]]
- [[Experimentation and Causal Inference]]
- [[Causal Inference]]
- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
- [[Event Tracking]]
- [[Model Monitoring]]
- [[Machine Learning System Design]]
- [[MLOps]]
- [[Data Products]]
- [[Data Product Management]]
