---
layout: wiki
title: "Metrics"
summary: "How the podcast archive treats metrics as decision definitions for products, experiments, ML systems, data products, and AI evaluation."
related:
  - Evaluation
  - A/B Testing
  - Product Analytics
  - Data Product Management
  - Machine Learning System Design
---

## Definition and Scope

Metrics quantify success, failure, risk, or system behavior. In the
DataTalks.Club archive, teams don't treat metrics as dashboard numbers only.
They use metrics to decide what an experiment means, how a model compares with
a baseline, whether a data product has impact, and when a production system
needs attention.

Use this page for metric design across product analytics, experimentation,
ML evaluation, and data product management. Use
[Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}) for how metric
variance affects experiment duration.

## Contents

This page uses these sections:

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Metric choice changes the decision. Jakob Graff's subscription-versus-points
example shows that a revenue experiment needs a metric that matches the rollout
decision. Revenue per user, conversion, retention, and long-term value can lead
to different product choices.

Stable metrics are easier to act on. The experimentation episode separates
stable metrics from noisy metrics by asking whether two lines can be
distinguished over time. Revenue per install can be much noisier than a
click-through rate, and weekly or yearly seasonality can bias short tests.

Experiments need one primary decision metric and guardrails. The archive warns
against choosing five primary metrics for a first test because the conclusion
becomes unclear. Guardrail metrics still watch for harm, including churn,
latency, cost, crashes, and revenue cannibalization.

Causal and predictive metrics answer different questions. Causal inference
episodes compare policies on the same business metric, but also ask whether the
data and causal structure are unbiased. Ordinary regression metrics can't prove
that an intervention effect is valid.

Data product metrics need semantic ownership. Data product and analytics
engineering episodes show that teams must align definitions such as customer,
activation, conversion, and KPI grain before metrics can be trusted.

## Episode Evidence

These episodes give the strongest evidence:

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  14:27-18:06: uses a subscription model experiment to ground revenue metric
  design. Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  30:05-37:44: recommends one decision metric, explains noisy versus stable
  metrics, and discusses weekly and larger business cycles.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  40:23-57:10: connects metric distributions to test choice and p-values. It
  also compares frequentist intervals, Bayesian intervals, and stakeholder
  communication.
- [Causal Inference for Real-World ML](https://datatalks.club/podcast.html),
  32:40-37:37: distinguishes policy metrics from causal-model validation and
  emphasizes comparing causal and baseline policies with the same business
  metric. Source:
  `../datatalksclub.github.io/_podcast/causal-inference-for-machine-learning.md`.
- [From Analytics to Production ML](https://datatalks.club/podcast.html),
  31:19-32:47: shows analysts connecting live model experiments to business
  metrics. Analysts use uplift, segments, and root-cause analysis to explain
  results.

## Related Pages

Useful adjacent pages:

- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

## Maintenance Notes

Future maintainers should preserve these source paths and boundaries:

- Keep this page about metric design and interpretation. Use
  [Evaluation]({{ '/wiki/evaluation/' | relative_url }}) for the broader
  validation process.
- Best source files:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`,
  `../datatalksclub.github.io/_podcast/causal-inference-for-machine-learning.md`,
  and `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`.
- Future expansion should add metric-governance evidence from analytics
  engineering and data product episodes when transcript timestamps are verified.
