---
layout: wiki
title: "Experimentation"
summary: "How the podcast archive treats experimentation as product, model, and organizational learning under uncertainty."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - Causal Inference
  - Product Analytics
  - Data Product Management
---

## Definition and Scope

Experimentation is the deliberate testing of a product, model, policy, or
workflow change before committing to a larger rollout. In the archive, the term
covers randomized A/B tests, A/A platform checks, model shadow testing,
proof-of-concept comparisons, design sprints, and data-driven product discovery.

This page covers the broader practice. Use
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) for randomized
experiment mechanics, [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
for intervention reasoning beyond randomized tests, and
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
for the full hub.

## Contents

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Experiments reduce risk before rollout. Jakob Graff's A/B testing episode uses
subscription pricing, game features, and release diagnosis to show why teams
test instead of relying only on expert intuition.

Experiments also build organizational learning. Small, lower-risk surfaces can
teach product teams what transfers to larger products. The useful result is not
only a launch decision; it is reusable knowledge about users, implementation
choices, and metrics.

ML work is experimental before and after deployment. Rishabh Bhargava describes
pre-deployment model experiments over features and hyperparameters, then live
traffic validation with shadow mode or A/B tests. Analysts help translate model
results into business impact and segment-level explanations.

Product-design experiments are often not statistical tests. Liesbeth Dingemans
describes Double Diamond discovery, parallel proofs of concept, scoping
documents, surveys, prototypes, and quick measurable changes as ways to collect
evidence before a team spends months on the wrong ML solution.

## Episode Evidence

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  18:06-23:54: frames experiments as de-risking and organizational learning.
  Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  30:05-37:44: recommends simple first tests, one decision metric, metric
  stability checks, and planned duration.
- [From Analytics to Production ML](https://datatalks.club/podcast.html),
  28:42-32:47: contrasts analytics iteration with ML experimentation and
  discusses shadow mode, A/B tests, uplift, and segment analysis. Source:
  `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`.
- [AI Product Design](https://datatalks.club/podcast.html), 12:12-17:25:
  explains Double Diamond problem framing and parallel proofs of concept.
  Source:
  `../datatalksclub.github.io/_podcast/ai-ml-product-design-and-experimentation.md`.
- [AI Product Design](https://datatalks.club/podcast.html), 54:11-55:54:
  treats surveys, button tests, and lightweight data collection as evidence for
  prioritization when teams pitch new product ideas.

## Related Pages

- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})

## Maintenance Notes

- Keep this page broader than A/B testing. Include product discovery,
  prototype, and ML validation evidence when episodes support it.
- Best source files:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`,
  `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`,
  and `../datatalksclub.github.io/_podcast/ai-ml-product-design-and-experimentation.md`.
- Future expansion should add examples from data product rollout episodes when
  the transcript has concrete experiment design details.
