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
---

A/B testing is a randomized product experiment. A team assigns comparable users
or sessions to a control experience and one changed experience. It then compares
the outcomes on metrics chosen before the test starts.

In the DataTalks.Club archive, A/B testing is the practical bridge between
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}). It turns a
product question into a rollout decision.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the core
definition in
[Product Analytics and A/B Testing at 8:13]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
The clinical-trial analogy matters because randomization separates the tested
change from market noise and seasonality. It also reduces bias from user
differences. At 11:48, he frames experimentation as a way to establish causality
under live product conditions.

## Common Definition

A common archive definition is narrower than "try two variants and look at a
dashboard." A useful A/B test has stable assignment and logged exposure. It has
a control group, a treatment group, a primary metric, and an agreed decision
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

## Guest Differences

The guests agree that A/B testing is about causal decisions, but they use it in
different operating contexts.

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

## Experimentation Design

Teams start design by choosing the unit of assignment. Account-level product
changes often use users, while short-lived experiences can use sessions. Some
production ML systems use traffic or requests. This is why
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) is adjacent: the
treatment exposure must be logged at the same level the analysis will use.

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

## Metrics

A/B testing fails when the metric doesn't match the decision. Jakob's
subscription-versus-points example in
[Product Analytics and A/B Testing at 14:27]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
shows why the same product change can look good or bad. The result depends on
the selected revenue metric. A test needs one primary metric for the rollout
decision and supporting metrics for diagnosis.

Metric stability matters as much as metric relevance. At
[33:23 in the A/B testing episode]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob discusses noise, seasonality, and business cycles. That connects A/B
testing to [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}):
teams need enough sample size and duration to detect the effect they care about.
At 37:44, he ties duration planning to statistical power rather than calendar
convenience.

The archive separates statistical significance from product significance. In
[the A/B testing episode at 47:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob explains p-values through an A/A comparison. A passing threshold is only
part of the decision. The team still needs to ask whether the estimated uplift is
large enough and worth the implementation cost.

## Product Analytics

In product analytics, A/B testing is a decision system, not only a statistics
exercise. It helps teams decide whether product changes should roll out. Those
changes can include pricing tests, onboarding flows, recommendation models, and
messaging experiments.

This topic links closely to
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}), and the
[Product Analyst]({{ '/guides/product-analyst/' | relative_url }}) article.

Jakob's
[Product Analytics and A/B Testing discussion at 18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
frames experiments as feature de-risking and organizational learning. A test
doesn't only answer whether a change worked. It teaches the team which user
behavior moved and where the effect appeared. It also shows which assumptions
were wrong.

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

## Related Pages

These pages cover the adjacent concepts used throughout the A/B testing
archive:

- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
