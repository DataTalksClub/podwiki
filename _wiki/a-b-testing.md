---
layout: wiki
title: "A/B Testing"
summary: "How the podcast archive explains A/B testing as randomized product evaluation: assignment, metrics, noise, power, and rollout decisions."
related:
  - Experimentation and Causal Inference
  - Experimentation
  - A/A Testing
  - Metrics
  - Power Analysis
---

## Definition and Scope

A/B testing is a randomized experiment. One group receives a control
experience, another receives a changed experience, and analysts compare both
groups on preselected metrics. In the DataTalks.Club archive, A/B testing is
the clearest way to establish whether a product or model change caused an
outcome under live conditions.

Use this page for online product and ML experiments. Use
[A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }}) for platform
validation, [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}) for
sample size planning, and [Metrics]({{ '/wiki/metrics/' | relative_url }}) for
metric choice.

## Contents

This page uses these sections:

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Randomization is the core mechanism. Jakob Graff compares A/B tests to clinical
trials. A team splits a stable unit such as a user, session, account, or
device. One group sees the change, another stays on the control, and analysts
compare outcomes over time.

A/B tests protect teams from noisy before-and-after comparisons. Marketing
campaigns, seasonality, user differences, and ordinary metric variance can all
move a dashboard. Random assignment helps isolate the treatment effect when the
experiment is designed and instrumented correctly.

The first test should be simple. The archive recommends two groups, one primary
metric, a product surface that is easy to instrument, and tracking that records
assignment. Complex multi-arm tests, unclear triggering, and fancy metrics make
it harder to learn whether the testing workflow works.

A/B testing is also a production-ML tool. The production-ML episode describes
shadow mode and A/B tests as ways to compare a new model with a baseline before
full rollout, with analysts helping diagnose uplift by segment and business
metric.

## Episode Evidence

These episodes give the strongest evidence:

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  8:13-13:25: defines A/B testing through randomized treatment and control
  groups, then explains why randomization controls external noise. Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  14:27-18:06: uses a subscription-versus-points revenue example to show why the
  selected metric determines the rollout decision.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  24:44-32:39: covers third-party versus in-house tools, traffic splitters,
  assignment tracking, and A/A tests. It also covers simple first-test design.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  59:08-1:02:52: explains why A/B/C/D tests take longer and increase multiple
  comparison risk.
- [From Analytics to Production ML](https://datatalks.club/podcast.html),
  31:19-32:47: connects A/B tests to live model evaluation. Analysts use uplift
  analysis and business-metric knowledge to explain results.

## Related Pages

Useful adjacent pages:

- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

## Maintenance Notes

Future maintainers should preserve these source paths and boundaries:

- Keep this page about randomized online tests, not every product discovery
  experiment.
- Best source file:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
  Use `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`
  for model rollout examples.
- Add more concrete examples only when transcripts include treatment,
  randomization unit, metric, and decision context.
