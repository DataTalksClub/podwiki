---
layout: wiki
title: "Power Analysis"
summary: "How the podcast archive uses power analysis to estimate experiment sample size, duration, and detectable effect before teams read A/B test results."
related:
  - A/B Testing
  - Metrics
  - Experimentation and Causal Inference
  - Evaluation
---

## Definition and Scope

Power analysis estimates how many observations an experiment needs to detect a
meaningful effect with acceptable error risk. In the podcast archive, it's a
practical planning tool for A/B tests. Teams combine expected effect size,
baseline metric behavior, variance, and traffic to estimate how long the test
should run.

Use this page for experiment planning, not statistical derivations. Use
[Metrics]({{ '/wiki/metrics/' | relative_url }}) for metric design and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) for the broader
randomized experiment workflow.

## Contents

This page uses these sections:

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Power analysis should happen before launch. Jakob Graff frames it as the answer
to stakeholder pressure: if the team estimates duration upfront, the analyst can
explain why reading results after one day is unsafe.

Metric behavior drives sample size. A stable conversion metric may need less
traffic than a noisy revenue metric with many zeros and a few extreme values.
The statistician's work isn't only plugging numbers into a calculator. They also
check whether the metric distribution makes the chosen test reasonable.

Traffic turns sample size into duration. Once the required observations are
estimated, teams compare that number with daily triggering traffic on the
product surface. Low-traffic surfaces or multi-arm designs can make otherwise
simple experiments run for much longer.

Seasonality is separate from power but still affects duration. The archive
recommends covering a full weekly cycle when behavior differs by weekday. Teams
should also be aware of larger business cycles even when a year-long test is
unrealistic.

## Episode Evidence

These episodes give the strongest evidence:

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  33:23-37:44: explains noisy metrics, stable metrics, and weekly seasonality.
  It also covers retention examples and business cycles that affect experiment
  planning. Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  37:44-40:23: defines power analysis as using expected improvement, metric
  statistics, and test assumptions. Teams use those inputs to estimate required
  observations and test duration.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  40:23-45:09: connects power and test choice to error types, confidence
  levels, p-values, and revenue distributions. The same section discusses fat
  tails and nonparametric tests.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  59:08-1:02:52: explains why A/B/C/D tests take longer because traffic is split
  across more groups and multiple comparisons increase false-positive risk.

## Related Pages

Useful adjacent pages:

- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})

## Maintenance Notes

Future maintainers should preserve these source paths and boundaries:

- Keep this page practical. Don't turn it into a formula reference unless the
  archive later contains a teaching episode with worked calculations.
- Best source file:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- Future expansion should add a compact glossary for type I error, type II
  error, minimum detectable effect, baseline rate, and variance if these pages
  become a statistics learning path.
