---
layout: wiki
title: "A/B Testing"
summary: "How the podcast archive explains A/B testing as randomized product evaluation, with assignment, metrics, noise, power, and rollout decisions."
related:
  - Experimentation and Causal Inference
  - Experimentation
  - A/A Testing
  - Metrics
  - Power Analysis
  - Event Tracking
  - Product Analytics
  - Data-Led Growth
  - Data Product Management
  - Evaluation
  - Production
  - Machine Learning System Design
  - Model Monitoring
  - Production Search Evaluation
  - Data Products
  - Search
---

A/B testing is a randomized product experiment. A team assigns comparable users
or sessions to a control experience and one changed experience. It then compares
the outcomes on metrics chosen before the test starts.

A/B testing bridges
[[product analytics]],
[[experimentation]], and
[[causal inference]]. The test
turns a product question into a rollout decision, which is why it also matters
for [[data product management]].
Teams also use A/B tests in
[[machine learning system design]],
[[data products]], and
[[production search evaluation]]
when they need online evidence before rollout.

The clinical-trial analogy matters because randomization separates the tested
change from market noise and seasonality, and it reduces bias from user
differences ([[podcast:ab-testing-and-product-experimentation|8:13|Product Analytics and A/B Testing]]).
Experimentation establishes causality under live product conditions.

## Randomization and Assignment

A practical A/B test is narrower than "try two variants and look at a
dashboard." The test needs stable assignment and logged exposure. It needs a
control group, a treatment group, a primary metric, and an agreed decision
rule.
That definition connects directly to
[[a-a-testing|A/A Testing]],
[[Power Analysis]], and
[[Metrics]].

Traffic splitting, assignment tracking, and monitoring make the difference
([[podcast:ab-testing-and-product-experimentation|24:44|Product Analytics and A/B Testing]]).
Without those controls, the team can't explain why a metric moved: the cause
could be the product change or incorrect assignment. A/A testing serves as the
trust check ([[podcast:ab-testing-and-product-experimentation|27:52|A/A testing]]).
If two identical groups show a large difference, the measurement system needs
attention before an A/B result is credible.

## Operating Contexts

A/B testing keeps the same causal structure in product analytics, production
ML, and causal inference. It also appears in healthcare personalization,
marketing, and search. The operating context changes what teams must protect,
measure, and debug.

As a product analytics discipline, the recommended starting point is a simple
first test with two groups and clear triggering, on a metric the team can
explain ([[podcast:ab-testing-and-product-experimentation|30:05|the A/B testing episode]]).
The goal is organizational learning: teams should learn how their product and
users behave, not only whether one button color won.

A/B tests also apply to production machine learning, where model work is
experimental and iterative and teams can use A/B tests and shadow mode before
full rollout ([[podcast:production-ml-mlops-and-data-team-building|28:42|From Analytics to Production ML]]).
Post-test analysis investigates uplift by segment and looks for root causes when
a model performs better or worse than expected.

A/B testing also sits inside a broader causal inference toolkit, where
randomized experiments are one route to unconfoundedness and serve as a
validation baseline for causal models and incremental rollouts
([[podcast:causal-inference-for-machine-learning|26:16|Causal Inference for Machine Learning]]).
The open question is what to do when experiments are impossible, incomplete, or
too expensive.

In a higher-risk personalization context, A/B testing connects to segmentation,
iterative personalization, variant availability, and measurement
([[podcast:ai-in-healthcare-and-digital-therapeutics|39:57|AI in Healthcare and Digital Therapeutics]]).
This frame adds patient safety, privacy, and responsible experimentation to the
usual product-growth concerns.

The marketing measurement boundary covers treatment/control design and data
pitfalls for uplift ([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|30:54|Marketing Data Science]]).
Attribution and media mix modeling show why A/B testing isn't always available
for every channel, campaign, or customer journey.

As part of ML system design, metrics, baselines, and A/B testing sit inside the
end-to-end ML pipeline, and production validation ties A/B tests to causality
and human labels ([[podcast:machine-learning-system-design-interview|24:28|ML System Design Interviews]]).

In the search and retrieval version, search changes connect to business KPIs
such as clicks, orders, contacts, and revenue, alongside offline tests and A/B
tests ([[podcast:building-production-search-systems|1:01:25|Building Search Systems]]).
Search teams should treat A/B testing as one part of the evaluation loop, not a
replacement for relevance diagnostics.

## Test Design and Rollout

Teams start design by choosing the unit of assignment. Account-level product
changes often use users, while short-lived experiences can use sessions. Some
production ML systems use traffic or requests. This is why
[[event tracking]] is adjacent: the
treatment exposure must be logged at the same level the analysis will use.
Traffic splitting grounds that rule in assignment tracking rather than dashboard
reporting ([[podcast:ab-testing-and-product-experimentation|24:44]]).

The first experiment should be boring: a two-group design exposes assignment
bugs, tracking gaps, and stakeholder disagreements faster than a complex
multi-arm test ([[podcast:ab-testing-and-product-experimentation|30:05|Product Analytics and A/B Testing]]).
A/B/C/D tests take longer and increase multiple-comparison risk, so extra
variants should earn their cost.

The tooling decision is secondary to the control logic. Third-party and in-house
experimentation platforms differ, but the important capabilities are traffic
splitting, stable assignment, and exposure logging
([[podcast:ab-testing-and-product-experimentation|23:54|the same episode]]).
Teams also need metric monitoring and a way to debug the test before
stakeholders trust the result.

Teams with model-backed products often stage rollout: offline model work, shadow
mode, and A/B tests come before full rollout
([[podcast:production-ml-mlops-and-data-team-building|28:42|production ML discussion]]).
Baselines and metrics fit the same sequence
([[podcast:machine-learning-system-design-interview|24:28|system-design discussion]]).
Live test sets and small A/B tests detect model issues before they become wider
incidents ([[podcast:human-centered-mlops-and-model-monitoring|29:23|model-monitoring discussion]]).

## Metrics and Decision Rules

A/B testing fails when the metric doesn't match the decision. A
subscription-versus-points example shows why the same product change can look
good or bad depending on the selected revenue metric
([[podcast:ab-testing-and-product-experimentation|14:27|Product Analytics and A/B Testing]]).
A test needs one primary metric for the rollout decision and supporting metrics
for diagnosis.

Metric stability matters as much as metric relevance. Noise, seasonality, and
business cycles all affect results
([[podcast:ab-testing-and-product-experimentation|33:23 in the A/B testing episode]]).
A/B testing depends on [[Power Analysis]] because
teams need enough sample size and duration to detect the effect they care about,
which ties duration planning to statistical power rather than calendar
convenience.

Statistical significance is separate from product significance. P-values can be
explained through an A/A comparison, and a passing threshold is only part of the
decision ([[podcast:ab-testing-and-product-experimentation|47:44|the A/B testing episode]]).
The team still needs to ask whether the estimated uplift is large enough and
worth the implementation cost.

The test result is also separate from the statistical procedure. Choosing tests
for different metric distributions, distribution checks, and the choice between
frequentist and Bayesian framing all matter
([[podcast:ab-testing-and-product-experimentation|40:23]]).
Teams should choose a statistical method that fits the metric and the decision,
not only one that produces a familiar number.

Guardrail metrics keep A/B tests from improving one number while damaging the
product. In healthcare personalization, patient trust sits beside engagement
([[podcast:ai-in-healthcare-and-digital-therapeutics|31:41|privacy and ethics discussion]]).
In search, relevance work connects to clicks, contacts, orders, and revenue
([[podcast:building-production-search-systems|1:01:25|business-KPI discussion]]).
In production ML, segment analysis keeps the team from reading only the
top-line average ([[podcast:production-ml-mlops-and-data-team-building|31:19]]).

## Product Analytics Decisions

In product analytics, A/B testing is a decision system, not only a statistics
exercise. It helps teams decide whether product changes should roll out. Those
changes can include pricing tests, onboarding flows, recommendation models, and
messaging experiments.

This topic links closely to
[[data-led-growth|Data-Led Growth]],
[[Product Analytics]], and the
[[Product Analyst]] guide.
It also gives
[[data product management]]
a measurement discipline for deciding whether a product, data workflow, or
model-backed feature should roll out.

Experiments serve as feature de-risking and organizational learning
([[podcast:ab-testing-and-product-experimentation|18:06|Product Analytics and A/B Testing discussion]]).
A test doesn't only answer whether a change worked. It teaches the team which
user behavior moved and where the effect appeared, and it shows which
assumptions were wrong.

Other product examples use the same analytics layer. A/B testing reports work as
decision products for business stakeholders
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|28:42|Last-Mile Data Delivery discussion]]).
A/B tests support segmentation and iteration
([[podcast:ai-in-healthcare-and-digital-therapeutics|39:57|personalization chapter]]),
connect product analytics to marketing interventions
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|30:54|uplift discussion]]),
and put online experiments beside offline search tests
([[podcast:building-production-search-systems|1:03:50|search evaluation discussion]]).

Production ML adds another analytics responsibility: analysts use business
context, segments, and root-cause analysis to explain the observed uplift
([[podcast:production-ml-mlops-and-data-team-building|31:19|From Analytics to Production ML]]).
That work connects A/B testing with
[[Evaluation]],
[[Machine Learning System Design]],
and [[Production]].

## Causal Inference Boundaries

A/B testing is powerful because random assignment blocks many confounding paths,
but it's not the whole field of causal inference. Experiments can be too slow,
too expensive, unethical, or impossible when the product can't withhold a
treatment from a control group. They can also answer only the question the team
actually randomized, not every causal question around the product.

The difference between association and causation is the starting point, leading
into counterfactuals
([[podcast:causal-inference-for-machine-learning|7:31|Causal Inference for Machine Learning episode]]).
The decision question is often what would have happened to the same user under a
different action. A/B testing gets closest to that question when the test is
randomized, logged, and analyzed on the right unit.

Randomized experiments contrast with causal feature selection for
unconfoundedness ([[podcast:causal-inference-for-machine-learning|26:16]]).
Uplift modeling and business metrics extend A/B testing beyond "did the average
user respond?" The next question is which users should receive the treatment.
Those ideas connect this page to
[[Experimentation and Causal Inference]]
and [[Causal Inference]].

Marketing measurement shows the same boundary from another direction. Multi-channel
journeys introduce ambiguity
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|10:18|attribution discussion]]),
and media mix modeling and time-series counterfactuals cover cases where random
assignment is hard or unavailable. A/B testing remains the clean evidence source
when the team can randomize. Attribution, uplift modeling, and causal inference
handle many decisions outside that clean setup.

## Related Pages

These pages cover the adjacent concepts used throughout the A/B testing
episodes:

- [[Experimentation]]
- [[a-a-testing|A/A Testing]]
- [[Power Analysis]]
- [[Metrics]]
- [[Event Tracking]]
- [[Causal Inference]]
- [[Product Analytics]]
- [[data-led-growth|Data-Led Growth]]
- [[Data Product Management]]
- [[Evaluation]]
- [[Production]]
- [[Data Products]]
- [[Model Monitoring]]
- [[Production Search Evaluation]]
- [[Search]]
- [[Product Analyst]]
- [[Data Product Manager Roadmap]]
- [[Machine Learning System Design]]
