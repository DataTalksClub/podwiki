---
layout: wiki
title: "Causal Inference"
summary: "How the podcast archive explains causal inference as the discipline for reasoning about interventions, counterfactuals, treatment effects, and policy decisions."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - Evaluation
  - Metrics
  - Machine Learning
---

## Definition and Scope

Causal inference asks what will happen if a team intervenes. The intervention
may launch a feature, target a customer, or change a recommender. It may also
send a campaign or deploy a new policy. Causal inference differs from ordinary
prediction because the decision changes the world that produces the data.

In the DataTalks.Club archive, guests discuss causal inference through A/B
testing, counterfactuals, and uplift modeling. Conditional average treatment
effects and unconfoundedness also appear, along with causal feature selection,
refutation tests, and baseline policy comparison.

## Contents

Use these sections:

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Prediction isn't enough when a system makes decisions. Aleksander Molak uses
marketing, recommendations, and the Zillow example to distinguish estimating
what's likely from estimating what would happen under a different action.

A/B tests with random assignment are the cleanest source of causal evidence.
The A/B testing episode treats randomization as the practical way to isolate a
product change from seasonality, marketing campaigns, and user-level
differences.

Observational causal inference needs stronger assumptions. The causal ML
episode explains that unconfoundedness can come from randomized treatment data
or from causal feature selection. When teams can't randomize, they must reason
explicitly about observed variables, missing confounders, and causal structure.

Uplift modeling changes the decision unit. Instead of asking who's likely to
buy, the team asks who's likely to buy because of treatment. This prevents
wasting budget on people who would buy anyway and avoids treating people who
may react negatively.

Teams evaluate causal work in layers. They compare a causal policy with a
baseline using the same business metric. They also use refutation tests and bias
checks because ordinary cross-validation can't validate causal structure.

## Episode Evidence

These episodes give the strongest evidence:

- [Causal Inference for Real-World ML](https://datatalks.club/podcast.html),
  7:31-15:36, distinguishes association from causation and explains why
  decision-making needs counterfactual reasoning. Source:
  `../datatalksclub.github.io/_podcast/causal-inference-for-machine-learning.md`.
- [Causal Inference for Real-World ML](https://datatalks.club/podcast.html),
  24:24-28:35, introduces conditional average treatment effects and targeting
  decisions based on treatment versus non-treatment outcomes.
- [Causal Inference for Real-World ML](https://datatalks.club/podcast.html),
  26:17-32:40, explains unconfoundedness through A/B tests or causal feature
  selection. It then connects uplift modeling to revenue, churn, or another
  business metric.
- [Causal Inference for Real-World ML](https://datatalks.club/podcast.html),
  33:14-43:52, covers refutation tests and estimator quality. It also covers
  cost-benefit reasoning, wasted marketing spend, and A/B testing as a
  deployment baseline.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  8:13-13:25, gives the randomized-experiment foundation that causal inference
  can use when experiments are possible.

## Related Pages

Useful adjacent pages:

- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})

## Maintenance Notes

Future maintainers should preserve these source paths and boundaries:

- Preserve the distinction between predictive accuracy, causal unbiasedness,
  estimator quality, and policy/business-metric evaluation.
- Best source file:
  `../datatalksclub.github.io/_podcast/causal-inference-for-machine-learning.md`.
  Use `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`
  for randomized experiment grounding.
- Add a podcast summary for the causal inference episode before expanding this
  page into a deeper teaching resource.
