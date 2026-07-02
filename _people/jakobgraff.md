---
layout: "person"
title: "Jakob Graff"
summary: "Jakob Graff's DataTalks.Club podcast discussions, organized for topic exploration."
source_url: "https://datatalks.club/people/jakobgraff.html"
podcast_episodes: ["ab-testing-and-product-experimentation"]
curated: "true"
linkedin: "jakob-graff-a6113a3a"
expertise: ["A/B testing", "product analytics", "causal inference", "metrics", "power analysis", "experimentation"]
---

## Background

Jakob Graff is a data science and analytics leader. In
[Product Analytics and A/B Testing](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html),
he brings an econometrics background into practical
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}). His
episode is the main source for the podwiki pages on
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}),
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}), and
[power analysis]({{ '/wiki/power-analysis/' | relative_url }}).

## Experiments as Causal Evidence

Jakob frames A/B testing as a way to establish causality, not only as a way to
compare dashboard numbers. Around 5:11, he connects his econometrics background
to product analytics. Around 8:13, he uses the clinical-trial analogy to explain
why randomization matters. Around 11:48, he describes experimentation as a way
to control noise and learn whether a product change caused the observed
outcome.

That makes his contribution useful for [data science]({{ '/wiki/data-science/' | relative_url }}),
[evaluation]({{ '/wiki/evaluation/' | relative_url }}), and
[metrics]({{ '/wiki/metrics/' | relative_url }}). Jakob's point is that a
better-looking metric isn't enough. The team has to know who was
assigned to each variant, whether randomization worked, and whether the measured
change is larger than normal product noise.

## Metric Design and Business Context

Jakob treats metric choice as part of experiment design. Around 14:27, he uses
a subscription-versus-points example to show why teams must choose the business
metric before they interpret a test. Around 33:23, he discusses noise and
stability. He also covers seasonality and business cycles. A metric can be easy
to measure and still be too noisy for a useful product decision.

This is why several wiki pages cite Jakob when they discuss
[KPIs]({{ '/wiki/kpis/' | relative_url }}), [metrics]({{ '/wiki/metrics/' | relative_url }}),
and [machine learning personalization]({{ '/wiki/machine-learning-personalization/' | relative_url }}).
Product teams need metrics that match the decision they'll make after the
test. Otherwise, a statistically clean result may still answer the wrong
business question.

## Assignment, A/A Tests, and Trust

Jakob spends time on the mechanics that make an experiment trustworthy. Around
23:54, he compares third-party experimentation tools with in-house systems.
Around 24:44, he covers traffic splitting, assignment tracking, and monitoring.
Around 27:52, he explains why A/A tests help validate randomization and system
trust before teams rely on A/B results.

[A/A testing]({{ '/wiki/a-a-testing/' | relative_url }}),
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}), and
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}) all depend on
this mechanics work. A product experiment isn't only a statistical calculation.
The data collection path has to preserve assignments, exposures, outcomes, and
enough context to debug unexpected results.

## Power Analysis and Test Duration

Around 37:44, Jakob explains test duration and sample-size planning through
power analysis. Teams shouldn't stop a test just because the first few days
look promising. They also shouldn't start tests that can't reach a useful
sample size. Power analysis makes the tradeoff explicit before the experiment
runs.

This is the practical reason his page belongs near
[power analysis]({{ '/wiki/power-analysis/' | relative_url }}) and
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
The experiment plan should define the expected effect size, sample size,
duration, and decision threshold before the team sees the result.

## Statistical Tests and Distribution Checks

Jakob gives a pragmatic view of statistics: around 40:23, he compares Z-tests,
T-tests, and nonparametric options. Around 44:39, he recommends looking at
histograms, tails, and distributions before trusting a single significance
number. Around 47:44, he explains p-values through A/A comparisons.

His guidance fits the podwiki's broader [evaluation]({{ '/wiki/evaluation/' | relative_url }})
pages because the statistical method has to match the data. Product metrics can
have skewed distributions, outliers, and seasonal behavior. The team should
look at the distribution before deciding which test result to trust.

## Product Analyst Practice

Jakob's episode is also a practical source for [product analyst]({{ '/wiki/product-analyst/' | relative_url }})
work. Around 18:06, he describes experiments as a way to de-risk features and
build organizational learning. Around 30:05, he recommends keeping a first test
simple with two groups. Around 59:08, he discusses multi-arm tests and the
extra duration, power, and multiple-comparison concerns they introduce.

For product analysts and data scientists, Jakob's recurring advice is to keep
the experiment tied to the decision. Use randomization to make the causal claim
credible. Use the right metric to make the claim useful. Use power and
distribution checks so the result isn't an artifact of noise.
