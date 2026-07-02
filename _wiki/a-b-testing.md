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

[[person:jakobgraff|Jakob Graff]] gives the core
definition in
[[podcast:ab-testing-and-product-experimentation|8:13|Product Analytics and A/B Testing]].
The clinical-trial analogy matters because randomization separates the tested
change from market noise and seasonality. It also reduces bias from user
differences. At 11:48, he frames experimentation as a way to establish causality
under live product conditions.

## Randomization and Assignment

A practical A/B test is narrower than "try two variants and look at a
dashboard." The test needs stable assignment and logged exposure. It needs a
control group, a treatment group, a primary metric, and an agreed decision
rule.
That definition connects directly to
[[a-a-testing|A/A Testing]],
[[Power Analysis]], and
[[Metrics]].

[[podcast:ab-testing-and-product-experimentation|24:44|Product Analytics and A/B Testing]]
focuses on traffic splitting, assignment tracking, and monitoring. Without those
controls, the team can't explain why a metric moved. The cause could be the
product change or incorrect assignment. Jakob then
uses [[podcast:ab-testing-and-product-experimentation|27:52|A/A testing]]
as the trust check. If two identical groups show a large difference, the
measurement system needs attention before an A/B result is credible.

## Operating Contexts

A/B testing keeps the same causal structure in product analytics, production
ML, and causal inference. It also appears in healthcare personalization,
marketing, and search. The operating context changes what teams must protect,
measure, and debug.

[[person:jakobgraff|Jakob Graff]] treats the subject as
a product analytics discipline. In
[[podcast:ab-testing-and-product-experimentation|30:05|the A/B testing episode]],
he recommends a simple first test with two groups and clear triggering. The
metric should be one the team can explain. His concern is organizational
learning. Teams should learn how their product and users behave, not only
whether one button color won.

[[person:rishabhbhargava|Rishabh Bhargava]] connects
A/B tests to production machine learning. In
[[podcast:production-ml-mlops-and-data-team-building|28:42|From Analytics to Production ML]],
he describes model work as experimental and iterative. Teams can use A/B tests
and shadow mode before full rollout. At 31:19, he shifts to post-test analysis.
Analysts investigate uplift by segment and look for root causes when a model
performs better or worse than expected.

[[person:aleksandermolak|Aleksander Molak]] places A/B
testing inside a broader causal inference toolkit. In
[[podcast:causal-inference-for-machine-learning|26:16|Causal Inference for Machine Learning]],
he treats randomized experiments as one route to unconfoundedness. At 43:25, he
uses A/B testing as a validation baseline for causal models and incremental
rollouts. His concern is what to do when experiments are impossible, incomplete,
or too expensive.

[[person:stefangudmundsson|Stefan Gudmundsson]] uses
A/B testing in a higher-risk personalization context. In
[[podcast:ai-in-healthcare-and-digital-therapeutics|39:57|AI in Healthcare and Digital Therapeutics]],
he connects A/B testing to segmentation and iterative personalization. At
43:00, the discussion moves to variant availability and measurement. His frame
adds patient safety, privacy, and responsible experimentation to the usual
product-growth concerns.

[[person:juanorduz|Juan Orduz]] brings the marketing
measurement boundary. In
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|30:54|Marketing Data Science]],
he discusses treatment/control design and data pitfalls for uplift. His earlier
chapters on attribution and media mix modeling show why A/B testing isn't
always available for every channel, campaign, or customer journey.

[[person:valeriybabushkin|Valeriy Babushkin]] treats
A/B tests as part of ML system design. In
[[podcast:machine-learning-system-design-interview|24:28|ML System Design Interviews]],
he puts metrics, baselines, and A/B testing inside the end-to-end ML pipeline.
At 57:23, he connects production validation to A/B tests, causality, and human
labels.

[[person:danielsvonava|Daniel Svonava]] brings the
search and retrieval version. In
[[podcast:building-production-search-systems|1:01:25|Building Search Systems]],
he connects search changes to business KPIs such as clicks and orders. He also
names contacts and revenue. Around 1:03:50, he adds offline tests and A/B
tests. Search teams should treat A/B testing as one part of the evaluation
loop, not a replacement for relevance diagnostics.

## Test Design and Rollout

Teams start design by choosing the unit of assignment. Account-level product
changes often use users, while short-lived experiences can use sessions. Some
production ML systems use traffic or requests. This is why
[[event tracking]] is adjacent: the
treatment exposure must be logged at the same level the analysis will use.
Jakob's traffic-splitting discussion at
[[podcast:ab-testing-and-product-experimentation|24:44]]
grounds that rule in assignment tracking rather than dashboard reporting.

In
[[podcast:ab-testing-and-product-experimentation|30:05|Product Analytics and A/B Testing]],
Jakob says the first experiment should be boring. A two-group design exposes
assignment bugs, tracking gaps, and stakeholder disagreements faster than a
complex multi-arm test. At 59:08, he explains that A/B/C/D tests take longer and
increase multiple-comparison risk, so extra variants should earn their cost.

The tooling decision is secondary to the control logic. In
[[podcast:ab-testing-and-product-experimentation|23:54|the same episode]],
Jakob compares third-party and in-house experimentation platforms. The important
capabilities are traffic splitting, stable assignment, and exposure logging.
Teams also need metric monitoring and a way to debug the test before
stakeholders trust the result.

Teams with model-backed products often stage rollout. Rishabh's
[[podcast:production-ml-mlops-and-data-team-building|28:42|production ML discussion]]
uses offline model work, shadow mode, and A/B tests before full rollout.
[[person:valeriybabushkin|Valeriy Babushkin]]'s
[[podcast:machine-learning-system-design-interview|24:28|system-design discussion]]
puts baselines and metrics into the same sequence.
[[person:linaweichbrodt|Lina Weichbrodt]]'s
[[podcast:human-centered-mlops-and-model-monitoring|29:23|model-monitoring discussion]]
adds live test sets and small A/B tests as ways to detect model issues before
they become wider incidents.

## Metrics and Decision Rules

A/B testing fails when the metric doesn't match the decision. Jakob's
subscription-versus-points example in
[[podcast:ab-testing-and-product-experimentation|14:27|Product Analytics and A/B Testing]]
shows why the same product change can look good or bad. The result depends on
the selected revenue metric. A test needs one primary metric for the rollout
decision and supporting metrics for diagnosis.

Metric stability matters as much as metric relevance. At
[[podcast:ab-testing-and-product-experimentation|33:23 in the A/B testing episode]],
Jakob discusses noise, seasonality, and business cycles. A/B testing depends
on [[Power Analysis]] because
teams need enough sample size and duration to detect the effect they care about.
At 37:44, he ties duration planning to statistical power rather than calendar
convenience.

Jakob separates statistical significance from product significance. In
[[podcast:ab-testing-and-product-experimentation|47:44|the A/B testing episode]],
Jakob explains p-values through an A/A comparison. A passing threshold is only
part of the decision. The team still needs to ask whether the estimated uplift is
large enough and worth the implementation cost.

Jakob also separates the test result from the statistical procedure. Around
[[podcast:ab-testing-and-product-experimentation|40:23]],
he discusses choosing tests for different metric distributions. Around 44:39,
he moves into distribution checks. Around 51:55, he compares frequentist and
Bayesian framing. Teams should choose a statistical method that fits the metric
and the decision, not only one that produces a familiar number.

Guardrail metrics keep A/B tests from improving one number while damaging the
product. In healthcare personalization, Stefan's
[[podcast:ai-in-healthcare-and-digital-therapeutics|31:41|privacy and ethics discussion]]
puts patient trust beside engagement. In search, Daniel's
[[podcast:building-production-search-systems|1:01:25|business-KPI discussion]]
connects relevance work to clicks and contacts. He also names orders and
revenue. In production ML, Rishabh's segment analysis at
[[podcast:production-ml-mlops-and-data-team-building|31:19]]
keeps the team from reading only the top-line average.

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

Jakob's
[[podcast:ab-testing-and-product-experimentation|18:06|Product Analytics and A/B Testing discussion]]
frames experiments as feature de-risking and organizational learning. A test
doesn't only answer whether a change worked. It teaches the team which user
behavior moved and where the effect appeared. It also shows which assumptions
were wrong.

Other product examples use the same analytics layer in different products.
[[person:caitlinmoorman|Caitlin Moorman]]'s
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|28:42|Last-Mile Data Delivery discussion]]
frames A/B testing reports as decision products for business stakeholders.
Stefan's
[[podcast:ai-in-healthcare-and-digital-therapeutics|39:57|personalization chapter]]
uses A/B tests for segmentation and iteration. Juan's
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|30:54|uplift discussion]]
connects product analytics to marketing interventions. Daniel's
[[podcast:building-production-search-systems|1:03:50|search evaluation discussion]]
puts online experiments beside offline search tests.

Rishabh's production ML example adds another analytics responsibility. In
[[podcast:production-ml-mlops-and-data-team-building|31:19|From Analytics to Production ML]],
analysts use business context, segments, and root-cause analysis to explain the
observed uplift. That work connects A/B testing with
[[Evaluation]],
[[Machine Learning System Design]],
and [[Production]].

## Causal Inference Boundaries

A/B testing is powerful because random assignment blocks many confounding paths,
but it's not the whole field of causal inference. Experiments can be too slow,
too expensive, unethical, or impossible when the product can't withhold a
treatment from a control group. They can also answer only the question the team
actually randomized, not every causal question around the product.

Aleksander's
[[podcast:causal-inference-for-machine-learning|7:31|Causal Inference for Machine Learning episode]]
starts with the difference between association and causation. At 15:36 and
18:15, he moves into counterfactuals. The decision question is often what would
have happened to the same user under a different action. A/B testing
gets closest to that question when the test is randomized, logged, and analyzed
on the right unit.

At [[podcast:causal-inference-for-machine-learning|26:16]],
Aleksander contrasts randomized experiments with causal feature selection for
unconfoundedness. At 32:40, he discusses uplift modeling and business metrics,
which extends A/B testing beyond "did the average user respond?" The next
question is which users should receive the treatment. Those ideas connect this
page to
[[Experimentation and Causal Inference]]
and [[Causal Inference]].

Marketing measurement shows the same boundary from another direction. Juan's
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|10:18|attribution discussion]]
starts with multi-channel journeys and ambiguity. His media mix modeling and
time-series counterfactual chapters at 13:36 and 14:58 cover cases where
random assignment is hard or unavailable. A/B testing remains the clean
evidence source when the team can randomize. Attribution, uplift modeling, and
causal inference handle many decisions outside that clean setup.

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
