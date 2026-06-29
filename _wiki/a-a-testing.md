---
layout: wiki
title: "A/A Testing"
summary: "How the podcast archive uses A/A testing to validate experiment assignment, tracking, and statistical interpretation before A/B tests are trusted."
related:
  - A/B Testing
  - Experimentation and Causal Inference
  - Metrics
  - Power Analysis
---

## Definition and Scope

A/A testing splits traffic into groups that receive the same experience. The
purpose is not to test a product change. It is to check whether randomization,
assignment logging, tracking, and analysis behave as expected before a team
trusts A/B results.

In the archive, A/A testing is a platform trust practice. It sits between
instrumentation and experimentation: if the system cannot produce balanced
groups and comparable metrics when nothing changed, it should not be used to
judge real product changes.

## Contents

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

A/A tests reveal assignment problems. Jakob Graff gives the simple warning sign:
if a planned 50/50 split becomes 60/40, the traffic splitter or triggering logic
needs investigation before any A/B conclusion is credible.

A/A tests also reveal metric and tracking problems. If both groups see the same
experience but conversion rates diverge beyond plausible noise, the team should
look for instrumentation bugs, biased defaults, missing assignment events, or
analysis mistakes.

The practice applies to third-party tools too. The archive notes that external
experimentation platforms can still produce untrusted splits, so teams should
validate them instead of assuming the dashboard is correct.

A/A intuition helps explain p-values. Later in the same episode, Jakob explains
statistical significance by asking how likely it would be to see the observed
uplift in an A/A test, where no treatment exists.

## Episode Evidence

- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  24:44-27:52: explains traffic splitters, assignment tracking, offline users
  defaulting into one group, and the monitoring needed around experimentation
  infrastructure. Source:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  27:52-32:39: defines A/A testing as showing the same experience to both
  groups, then checking split balance and metric comparability.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html),
  47:44-50:12: uses A/A test logic to explain p-value intuition to product
  stakeholders without leading with formal hypothesis-test language.

## Related Pages

- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})

## Maintenance Notes

- Keep A/A testing framed as experiment-system validation, not a substitute for
  A/B testing.
- Best source file:
  `../datatalksclub.github.io/_podcast/ab-testing-and-product-experimentation.md`.
- Future expansion should add examples of assignment bugs from other episodes
  only when transcripts mention concrete split, trigger, or tracking failures.
