---
layout: wiki
title: "KPIs"
summary: "How DataTalks.Club podcast guests define, choose, operate, and challenge key performance indicators for data and ML work."
related:
  - Metrics
  - Evaluation
  - Product Analytics
  - Data Strategy
  - Data Product Management
  - Model Monitoring
  - A/B Testing
---

Key performance indicators are the small set of [metrics]({{ '/wiki/metrics/' | relative_url }})
that a team uses to steer decisions, communicate tradeoffs, and judge whether
work changed the business. In the DataTalks.Club discussions, KPIs aren't just
dashboard numbers. They're decision metrics with an owner, a time window, a
known audience, and a behavior they're meant to influence.

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) gives the most direct
KPI treatment in
[KPI Design and Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
He starts from merit functions and comparable units at 12:06-16:51, then
defines KPIs as top-down executive decision metrics at 22:41-25:56. Other
episodes show where KPI work meets [data strategy]({{ '/wiki/data-strategy/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}).

## Executive Decision Metrics

In Sroka's sales pipeline example, weighted revenue becomes a KPI because it
helps executives compare lead quality with likely conversion and expected value
([22:41-25:56]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).
The same episode discusses units and comparability at 16:51. Those units matter
when teams compare revenue, cost, risk, and time saved. A metric without a
shared unit can still describe a system, but it's weak as a KPI because it can't
support a clear tradeoff.

This is why KPIs sit close to [business intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
and [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
Sroka's consultancy examples at 6:32 and 20:46 include BI dashboards,
professional-services burn-down, and maintainability of earnings. Those
examples make KPI work a translation layer between operational facts and
leadership choices, not a detached reporting exercise.

## Alignment and Ownership

The strongest KPI discussions treat alignment as a design constraint.
Sroka argues that KPIs should follow top-down business priorities, then become
visible enough that teams can use them in day-to-day decisions
([22:41-25:56 and 41:07-44:59]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).
He later discusses a North Star metric at 44:59-46:34 as a single guiding
indicator for strategy. Not every team needs one universal number. A KPI still
has to say what direction matters when choices compete.

[Lior Barak]({{ '/people/liorbarak/' | relative_url }}) makes a similar
alignment argument from the [data strategy]({{ '/wiki/data-strategy/' | relative_url }})
side. In
[Mindful Data Strategy for Business Impact]({{ '/podcasts/mindful-data-strategy-for-business-impact/' | relative_url }}),
Barak uses core KPI diagnosis at 20:50-23:26. It shows how dashboard
inaccuracies force teams to look at ingestion and SQL logic. The same diagnosis
also covers lineage and ownership.

Later, at 1:00:23, he frames executive ad hoc requests around intent and
expected impact. That makes KPI ownership part of trust and prioritization, not
only metric definition.

## Gaming and Composite Measures

KPIs change behavior, so they can also create bad incentives. Sroka warns about
vanity metrics at 26:07-28:04 and KPI gaming at 28:04-30:30 in the KPI design
episode. His examples distinguish easy-to-count activity from business
outcomes. "Customers spoken to" may be measurable, but it's a poor KPI when it
misses revenue or margin. It's also poor when it misses retention or risk.

Composite KPIs are one response to that problem. Sroka discusses derived KPIs
at 30:30-32:44, where they capture margin and tradeoffs instead of optimizing
one hackable number.

This places KPIs near
[evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}). The team
needs to know whether the number reflects the outcome it claims to represent.
Composite measures can help, but they still need a clear interpretation and a
review cadence.

## Dashboards and Review Cadence

KPIs become useful when teams can see them and review them. They matter when
teams change decisions after the numbers move. Sroka's operational section at
37:19-44:59 covers KPI prioritization and review cadence. It also covers
dashboards, visibility, and executive communication. He recommends a small
shortlist rather than a broad wall of numbers, because too many KPIs weaken the
decision signal.

Barak adds the reliability concern. In the mindful data strategy episode, core KPI
diagnosis at 20:50 and the traffic-light reliability system at 30:47 make
dashboard trust part of KPI governance. If a KPI dashboard can be wrong without
any visible warning, the team has a [data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }})
problem and a communication problem. Reliable KPI dashboards need lineage,
ownership, and user feedback loops, which also links KPI work to
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[documentation]({{ '/wiki/documentation/' | relative_url }}).

## Data and ML Impact

For data and ML teams, Sroka argues that model performance should be translated
into a business-facing unit such as money or time saved
([51:12-56:35]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).
That claim is central to [data product management]({{ '/wiki/data-product-management/' | relative_url }})
and [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
In those systems, accuracy and AUC matter most when the team can say which KPI
they protect or improve. Latency and pipeline freshness need the same business
link.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) makes the
same point during project intake in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
At 4:50-10:26, she starts with the business case, KPIs, and alternatives before
modeling. At 18:29-24:34, stakeholder fears become mitigations, service levels,
and impact assessment. KPI design therefore happens before model selection, and
it shapes whether an ML system should exist at all.

## Production and Trust Signals

Some KPIs guide growth, while others define unacceptable failure. Sroka
discusses threshold metrics at 46:34-48:48 and health or hygiene metrics at
48:48-51:12. Downtime and service reliability are KPI-adjacent because they
tell a team when a product is unsafe. Warning limits show when the product is no
longer meeting the standard users expect.

Weichbrodt's MLOps episode turns those signals into operating practice. Service
levels and impact assessment appear at 24:34, post-mortems at 27:14-42:03, and
feature drift plus data monitoring at 46:28-49:28
([Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).
For [production]({{ '/wiki/production/' | relative_url }}) systems, KPI
movement should trigger investigation, user communication, or rollback work. A
KPI that nobody can act on is only a status label.

## Experimentation and Search Impact

KPIs also decide whether experiments and search changes ship.
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) explains in
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
that a product experiment can imply different choices. The choice changes when
the primary metric is revenue or conversion. It changes again when the team
prioritizes retention or long-term value
([14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

At 30:05-40:23, Graff warns about too many primary metrics and noisy metrics.
He also covers seasonality and underpowered tests. KPI choice therefore belongs
before [power analysis]({{ '/wiki/power-analysis/' | relative_url }}) and
rollout decisions, not after a dashboard is already built.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
search-system version in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
At 1:01:25, he ties search impact to business metrics, A/B tests, and revenue.
At 1:03:50, he separates operational metrics from offline evaluation. Search
KPIs therefore bridge [information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}),
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
Offline relevance can guide engineering, but shipping requires a business or
user-facing KPI that moves for the right audience.
