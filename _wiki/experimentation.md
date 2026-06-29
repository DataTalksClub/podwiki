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

Experimentation is deliberate testing before a team commits to a larger
rollout. In the archive, teams experiment with product changes, models,
policies, workflows, randomized A/B tests, A/A platform checks, shadow testing,
proofs of concept, design sprints, and data-driven product discovery.

Use this page for the broader practice. Use
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) for randomized
experiment mechanics, [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
for intervention reasoning beyond randomized tests, and
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
for the full hub.

## Contents

This page uses these sections:

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Experiments reduce risk before rollout. Jakob Graff's A/B testing episode uses
subscription pricing, game features, and release diagnosis to show why teams
test instead of relying only on expert intuition.

Experiments also build organizational learning. Small, lower-risk surfaces can
teach product teams what transfers to larger products. Teams don't only get a
launch decision. They also get reusable knowledge about users, implementation
choices, and metrics.

ML work is experimental before and after deployment. Rishabh Bhargava describes
pre-deployment model experiments over features and hyperparameters, then live
traffic validation with shadow mode or A/B tests. Analysts help translate model
results into business impact and segment-level explanations.

Product-design experiments often aren't statistical tests. Liesbeth Dingemans
describes Double Diamond discovery, parallel proofs of concept, scoping
documents, surveys, and prototypes. Quick measurable changes can collect
evidence before a team spends months on the wrong ML solution.

## Episode Evidence

These episodes give the strongest evidence:

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  18:06-23:54: frames experiments as de-risking and organizational learning.
  Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  30:05-37:44: recommends simple first tests, one decision metric, metric
  stability checks, and planned duration.
- [From Analytics to Production ML](https://datatalks.club/podcast.html),
  28:42-32:47: contrasts analytics iteration with ML experimentation and
  discusses shadow mode and A/B tests. It also covers uplift and segment
  analysis. Source:
  `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`.
- [AI Product Design](https://datatalks.club/podcast.html), 12:12-17:25:
  explains Double Diamond problem framing and parallel proofs of concept.
  Source:
  `../datatalksclub.github.io/_podcast/ai-ml-product-design-and-experimentation.md`.
- [AI Product Design](https://datatalks.club/podcast.html), 54:11-55:54:
  treats surveys, button tests, and lightweight data collection as evidence for
  prioritization when teams pitch new product ideas.

## Related Pages

Useful adjacent pages:

- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})

## Maintenance Notes

Future maintainers should preserve these source paths and boundaries:

- Keep this page broader than A/B testing. Include product discovery,
  prototype, and ML validation evidence when episodes support it.
- Best source files:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`,
  `../datatalksclub.github.io/_podcast/production-ml-mlops-and-data-team-building.md`,
  and `../datatalksclub.github.io/_podcast/ai-ml-product-design-and-experimentation.md`.
- Future expansion should add examples from data product rollout episodes when
  the transcript has concrete experiment design details.
