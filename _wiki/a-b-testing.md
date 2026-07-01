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
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}). The test
turns a product question into a rollout decision, which is why it also matters
for [data product management]({{ '/wiki/data-product-management/' | relative_url }}).
Teams also use A/B tests in
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[data products]({{ '/wiki/data-products/' | relative_url }}), and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
when they need online evidence before rollout.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the core
definition in
[Product Analytics and A/B Testing at 8:13]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
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
[A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }}),
[Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}), and
[Metrics]({{ '/wiki/metrics/' | relative_url }}).

[Product Analytics and A/B Testing at 24:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
focuses on traffic splitting, assignment tracking, and monitoring. Without those
controls, the team can't explain why a metric moved. The cause could be the
product change or incorrect assignment. Jakob then
uses [A/A testing at 27:52]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
as the trust check. If two identical groups show a large difference, the
measurement system needs attention before an A/B result is credible.

## Operating Contexts

A/B testing keeps the same causal structure in product analytics, production
ML, and causal inference. It also appears in healthcare personalization,
marketing, and search. The operating context changes what teams must protect,
measure, and debug.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) treats the subject as
a product analytics discipline. In
[the A/B testing episode at 30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he recommends a simple first test with two groups and clear triggering. The
metric should be one the team can explain. His concern is organizational
learning. Teams should learn how their product and users behave, not only
whether one button color won.

[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) connects
A/B tests to production machine learning. In
[From Analytics to Production ML at 28:42]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
he describes model work as experimental and iterative. Teams can use A/B tests
and shadow mode before full rollout. At 31:19, he shifts to post-test analysis.
Analysts investigate uplift by segment and look for root causes when a model
performs better or worse than expected.

[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) places A/B
testing inside a broader causal inference toolkit. In
[Causal Inference for Machine Learning at 26:16]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he treats randomized experiments as one route to unconfoundedness. At 43:25, he
uses A/B testing as a validation baseline for causal models and incremental
rollouts. His concern is what to do when experiments are impossible, incomplete,
or too expensive.

[Stefan Gudmundsson]({{ '/people/stefangudmundsson/' | relative_url }}) uses
A/B testing in a higher-risk personalization context. In
[AI in Healthcare and Digital Therapeutics at 39:57]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}),
he connects A/B testing to segmentation and iterative personalization. At
43:00, the discussion moves to variant availability and measurement. His frame
adds patient safety, privacy, and responsible experimentation to the usual
product-growth concerns.

[Juan Orduz]({{ '/people/juanorduz/' | relative_url }}) brings the marketing
measurement boundary. In
[Marketing Data Science at 30:54]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }}),
he discusses treatment/control design and data pitfalls for uplift. His earlier
chapters on attribution and media mix modeling show why A/B testing isn't
always available for every channel, campaign, or customer journey.

[Valeriy Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) treats
A/B tests as part of ML system design. In
[ML System Design Interviews at 24:28]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he puts metrics, baselines, and A/B testing inside the end-to-end ML pipeline.
At 57:23, he connects production validation to A/B tests, causality, and human
labels.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) brings the
search and retrieval version. In
[Building Search Systems at 1:01:25]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he connects search changes to business KPIs such as clicks and orders. He also
names contacts and revenue. Around 1:03:50, he adds offline tests and A/B
tests. Search teams should treat A/B testing as one part of the evaluation
loop, not a replacement for relevance diagnostics.

## Test Design and Rollout

Teams start design by choosing the unit of assignment. Account-level product
changes often use users, while short-lived experiences can use sessions. Some
production ML systems use traffic or requests. This is why
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) is adjacent: the
treatment exposure must be logged at the same level the analysis will use.
Jakob's traffic-splitting discussion at
[24:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
grounds that rule in assignment tracking rather than dashboard reporting.

In
[Product Analytics and A/B Testing at 30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob says the first experiment should be boring. A two-group design exposes
assignment bugs, tracking gaps, and stakeholder disagreements faster than a
complex multi-arm test. At 59:08, he explains that A/B/C/D tests take longer and
increase multiple-comparison risk, so extra variants should earn their cost.

The tooling decision is secondary to the control logic. In
[the same episode at 23:54]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob compares third-party and in-house experimentation platforms. The important
capabilities are traffic splitting, stable assignment, and exposure logging.
Teams also need metric monitoring and a way to debug the test before
stakeholders trust the result.

Teams with model-backed products often stage rollout. Rishabh's
[production ML discussion at 28:42]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }})
uses offline model work, shadow mode, and A/B tests before full rollout.
[Valeriy Babushkin]({{ '/people/valeriybabushkin/' | relative_url }})'s
[system-design discussion at 24:28]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }})
puts baselines and metrics into the same sequence.
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})'s
[model-monitoring discussion at 29:23]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
adds live test sets and small A/B tests as ways to detect model issues before
they become wider incidents.

## Metrics and Decision Rules

A/B testing fails when the metric doesn't match the decision. Jakob's
subscription-versus-points example in
[Product Analytics and A/B Testing at 14:27]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
shows why the same product change can look good or bad. The result depends on
the selected revenue metric. A test needs one primary metric for the rollout
decision and supporting metrics for diagnosis.

Metric stability matters as much as metric relevance. At
[33:23 in the A/B testing episode]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob discusses noise, seasonality, and business cycles. A/B testing depends
on [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}) because
teams need enough sample size and duration to detect the effect they care about.
At 37:44, he ties duration planning to statistical power rather than calendar
convenience.

Jakob separates statistical significance from product significance. In
[the A/B testing episode at 47:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob explains p-values through an A/A comparison. A passing threshold is only
part of the decision. The team still needs to ask whether the estimated uplift is
large enough and worth the implementation cost.

Jakob also separates the test result from the statistical procedure. Around
[40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he discusses choosing tests for different metric distributions. Around 44:39,
he moves into distribution checks. Around 51:55, he compares frequentist and
Bayesian framing. Teams should choose a statistical method that fits the metric
and the decision, not only one that produces a familiar number.

Guardrail metrics keep A/B tests from improving one number while damaging the
product. In healthcare personalization, Stefan's
[privacy and ethics discussion at 31:41]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }})
puts patient trust beside engagement. In search, Daniel's
[business-KPI discussion at 1:01:25]({{ '/podcasts/building-production-search-systems/' | relative_url }})
connects relevance work to clicks and contacts. He also names orders and
revenue. In production ML, Rishabh's segment analysis at
[31:19]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }})
keeps the team from reading only the top-line average.

## Product Analytics Decisions

In product analytics, A/B testing is a decision system, not only a statistics
exercise. It helps teams decide whether product changes should roll out. Those
changes can include pricing tests, onboarding flows, recommendation models, and
messaging experiments.

This topic links closely to
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}), and the
[Product Analyst]({{ '/guides/product-analyst/' | relative_url }}) guide.
It also gives
[data product management]({{ '/wiki/data-product-management/' | relative_url }})
a measurement discipline for deciding whether a product, data workflow, or
model-backed feature should roll out.

Jakob's
[Product Analytics and A/B Testing discussion at 18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
frames experiments as feature de-risking and organizational learning. A test
doesn't only answer whether a change worked. It teaches the team which user
behavior moved and where the effect appeared. It also shows which assumptions
were wrong.

Other product examples use the same analytics layer in different products.
[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})'s
[Last-Mile Data Delivery discussion at 28:42]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
frames A/B testing reports as decision products for business stakeholders.
Stefan's
[personalization chapter at 39:57]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }})
uses A/B tests for segmentation and iteration. Juan's
[uplift discussion at 30:54]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }})
connects product analytics to marketing interventions. Daniel's
[search evaluation discussion at 1:03:50]({{ '/podcasts/building-production-search-systems/' | relative_url }})
puts online experiments beside offline search tests.

Rishabh's production ML example adds another analytics responsibility. In
[From Analytics to Production ML at 31:19]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
analysts use business context, segments, and root-cause analysis to explain the
observed uplift. That work connects A/B testing with
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
and [Production]({{ '/wiki/production/' | relative_url }}).

## Causal Inference Boundaries

A/B testing is powerful because random assignment blocks many confounding paths,
but it's not the whole field of causal inference. Experiments can be too slow,
too expensive, unethical, or impossible when the product can't withhold a
treatment from a control group. They can also answer only the question the team
actually randomized, not every causal question around the product.

Aleksander's
[Causal Inference for Machine Learning episode at 7:31]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }})
starts with the difference between association and causation. At 15:36 and
18:15, he moves into counterfactuals. The decision question is often what would
have happened to the same user under a different action. A/B testing
gets closest to that question when the test is randomized, logged, and analyzed
on the right unit.

At [26:16]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
Aleksander contrasts randomized experiments with causal feature selection for
unconfoundedness. At 32:40, he discusses uplift modeling and business metrics,
which extends A/B testing beyond "did the average user respond?" The next
question is which users should receive the treatment. Those ideas connect this
page to
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
and [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }}).

Marketing measurement shows the same boundary from another direction. Juan's
[attribution discussion at 10:18]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }})
starts with multi-channel journeys and ambiguity. His media mix modeling and
time-series counterfactual chapters at 13:36 and 14:58 cover cases where
random assignment is hard or unavailable. A/B testing remains the clean
evidence source when the team can randomize. Attribution, uplift modeling, and
causal inference handle many decisions outside that clean setup.

## Related Pages

These pages cover the adjacent concepts used throughout the A/B testing
episodes:

- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Product Analyst]({{ '/guides/product-analyst/' | relative_url }})
- [Data Product Manager Roadmap]({{ '/roadmaps/data-product-manager-roadmap/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
