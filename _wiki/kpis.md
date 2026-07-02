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

Key performance indicators are the small set of [[metrics]]
that a team uses to steer decisions, communicate tradeoffs, and judge whether
work changed the business. In the DataTalks.Club discussions, KPIs aren't just
dashboard numbers. They're decision metrics with an owner, a time window, a
known audience, and a behavior they're meant to influence.

[[person:adamsroka|Adam Sroka]] gives the most direct
KPI treatment in
[[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design and Metrics Strategy]].
He starts from merit functions and comparable units at 12:06-16:51, then
defines KPIs as top-down executive decision metrics at 22:41-25:56. Other
episodes show where KPI work meets [[data strategy]],
[[product analytics]],
[[model monitoring]], and
[[a-b-testing|A/B testing]].

## Executive Decision Metrics

In Sroka's sales pipeline example, weighted revenue becomes a KPI because it
helps executives compare lead quality with likely conversion and expected value
([[podcast:ml-engineering-kpis-and-metrics-strategy|22:41-25:56]]).
The same episode discusses units and comparability at 16:51. Those units matter
when teams compare revenue, cost, risk, and time saved. A metric without a
shared unit can still describe a system, but it's weak as a KPI because it can't
support a clear tradeoff.

This is why KPIs sit close to [[business intelligence]]
and [[analytics engineering]].
Sroka's consultancy examples at 6:32 and 20:46 include BI dashboards,
professional-services burn-down, and maintainability of earnings. Those
examples make KPI work a translation layer between operational facts and
leadership choices, not a detached reporting exercise.

## Alignment and Ownership

The strongest KPI discussions treat alignment as a design constraint.
Sroka argues that KPIs should follow top-down business priorities, then become
visible enough that teams can use them in day-to-day decisions
([[podcast:ml-engineering-kpis-and-metrics-strategy|22:41-25:56 and 41:07-44:59]]).
He later discusses a North Star metric at 44:59-46:34 as a single guiding
indicator for strategy. Not every team needs one universal number. A KPI still
has to say what direction matters when choices compete.

[[person:liorbarak|Lior Barak]] makes a similar
alignment argument from the [[data strategy]]
side. In
[[podcast:mindful-data-strategy-for-business-impact|Mindful Data Strategy for Business Impact]],
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
[[evaluation]] and
[[causal inference]]. The team
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
any visible warning, the team has a [[data-quality-and-observability|data quality]]
problem and a communication problem. Reliable KPI dashboards need lineage,
ownership, and user feedback loops, which also links KPI work to
[[data governance]] and
[[documentation]].

## Data and ML Impact

For data and ML teams, Sroka argues that model performance should be translated
into a business-facing unit such as money or time saved
([[podcast:ml-engineering-kpis-and-metrics-strategy|51:12-56:35]]).
That claim is central to [[data product management]]
and [[machine learning system design]].
In those systems, accuracy and AUC matter most when the team can say which KPI
they protect or improve. Latency and pipeline freshness need the same business
link.

[[person:linaweichbrodt|Lina Weichbrodt]] makes the
same point during project intake in
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps]].
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
([[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps]]).
For [[production]] systems, KPI
movement should trigger investigation, user communication, or rollback work. A
KPI that nobody can act on is only a status label.

## Experimentation and Search Impact

KPIs also decide whether experiments and search changes ship.
[[person:jakobgraff|Jakob Graff]] explains in
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]
that a product experiment can imply different choices. The choice changes when
the primary metric is revenue or conversion. It changes again when the team
prioritizes retention or long-term value
([[podcast:ab-testing-and-product-experimentation|14:27-18:06]]).

At 30:05-40:23, Graff warns about too many primary metrics and noisy metrics.
He also covers seasonality and underpowered tests. KPI choice therefore belongs
before [[power analysis]] and
rollout decisions, not after a dashboard is already built.

[[person:danielsvonava|Daniel Svonava]] gives the
search-system version in
[[podcast:building-production-search-systems|Building Search Systems]].
At 1:01:25, he ties search impact to business metrics, A/B tests, and revenue.
At 1:03:50, he separates operational metrics from offline evaluation. Search
KPIs therefore bridge [[information retrieval]],
[[embeddings]], and
[[production search evaluation]].
Offline relevance can guide engineering, but shipping requires a business or
user-facing KPI that moves for the right audience.
