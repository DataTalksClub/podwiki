---
layout: wiki
title: "KPIs"
summary: "Key performance indicators for defining, choosing, operating, and challenging metrics in data and ML work."
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
work changed the business. KPIs aren't just dashboard numbers. They're decision
metrics with an owner, a time window, a known audience, and a behavior they're
meant to influence.

In [[person:adamsroka=>Adam Sroka]]'s [[podcast:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]],
he gives the most direct KPI treatment.
He starts from merit functions and comparable units, then defines KPIs as
top-down executive decision metrics. The same KPI questions connect to
[[data strategy]],
[[product analytics]],
[[model monitoring]], and
[[a-b-testing=>A/B testing]].

## Executive Decision Metrics

In Sroka's sales pipeline example, weighted revenue becomes a KPI because it
helps executives compare lead quality with expected
value.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]
It brings likely conversion into the same decision.
The same episode discusses units and comparability. Those units matter
when teams compare revenue, cost, risk, and time saved. A metric without a
shared unit can still describe a system, but it's weak as a KPI because it can't
support a clear tradeoff.

Vin Vashishta applies that executive-language rule to ML strategy. ARR, MRR,
revenue, and cost savings are the metrics that move budget conversations out of
model scores. They put the discussion in business terms.
[[cite:make-money-with-machine-learning-roles-skills@12:07=>ARR and MRR for ML]][[cite:make-money-with-machine-learning-roles-skills@15:59=>Revenue and cost-savings metrics]]

Jack Blandin gives the stakeholder version. When speaking with marketing, use
their KPI language such as CAC. Don't lead with technical model details.
[[cite:from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership@15:25=>Speaking in stakeholder KPIs]]

This is why KPIs sit close to [[business intelligence]]
and [[analytics engineering]].
Sroka's consultancy examples include BI dashboards, professional-services
burn-down, and maintainability of earnings. Those examples make KPI work a
translation layer between operational facts and leadership choices, not a
detached reporting exercise.

## Alignment and Ownership

The strongest KPI discussions treat alignment as a design constraint.
Sroka argues that KPIs should follow top-down business priorities. Teams should
also see the KPIs clearly enough to use them in day-to-day
decisions.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]

He later discusses a North Star metric as a single guiding indicator for
strategy. Not every team needs one universal number. A KPI still has to say what
direction matters when choices compete.

Marco De Sa makes the executive version explicit in the
[[chief-data-officer-role=>Chief Data Officer role]]. A CDO breaks strategy
into goals and owned work. KPIs then show whether the company is moving in the
right direction.[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]]

For internal data platforms, Greg Coquillo frames success metrics as part of
product-management discipline. Teams identify the affected customers and pain
points, define success criteria, and make the SMART goal measurable. Examples
include reducing pipeline latency, meeting an SLA, increasing engagement, or
reducing churn.
[[cite:building-and-scaling-ai-data-products-with-mlops@51:11=>AI Data Products with MLOps]]
That connects KPI design to [[data product management]] and [[Data Quality and Observability]]
when the platform serves downstream teams.

[[person:liorbarak=>Lior Barak]] makes a similar
alignment argument from the [[data strategy]] side. His core KPI diagnosis in [[podcast:mindful-data-strategy-for-business-impact=>Mindful Data Strategy for Business Impact]]
shows how dashboard inaccuracies force teams to look at ingestion and SQL logic.
The same diagnosis also covers lineage and ownership.

Later, he frames executive ad hoc requests around intent and expected impact.
That makes KPI ownership part of trust and prioritization, not only metric
definition.

## Gaming and Composite Measures

KPIs change behavior, so they can also create bad incentives. Sroka warns about
vanity metrics and KPI gaming in the KPI design
episode.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]
His examples distinguish easy-to-count activity from business outcomes.
"Customers spoken to" may be measurable, but it's a poor KPI when it misses
revenue or margin. It's also poor when it misses retention or risk.

Composite KPIs are one response to that problem. Sroka discusses derived KPIs
that capture margin and tradeoffs instead of optimizing one hackable number.

This places KPIs near
[[evaluation]] and
[[causal inference]]. The team
needs to know whether the number reflects the outcome it claims to represent.
Composite measures can help, but they still need a clear interpretation and a
review cadence.

## Dashboards and Review Cadence

KPIs become useful when teams can see them and review them. They matter when
teams change decisions after the numbers move. Sroka's operational section
covers KPI prioritization, review cadence, and dashboard visibility. It also
covers executive communication.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]
He recommends a small shortlist rather than a broad wall of numbers, because too
many KPIs weaken the decision signal.

Barak adds the reliability concern. In the mindful data strategy episode, core
KPI diagnosis makes dashboard trust part of governance. The traffic-light
reliability system reinforces the same point.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy for Business Impact]]
If a KPI dashboard can be wrong without any visible warning, the team has a [[data-quality-and-observability=>data quality]]
problem and a communication problem. Reliable KPI dashboards need lineage,
ownership, and user feedback loops, which also links KPI work to [[data governance]] and
[[documentation]].

## Data and ML Impact

For data and ML teams, Sroka argues that teams should translate model
performance into a business-facing unit. Money or time saved makes the metric
legible to the business.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]
That claim is central to [[data product management]]
and [[machine learning system design]].
In those systems, accuracy and AUC matter most when the team can say which KPI
they protect or improve. Latency and pipeline freshness need the same business
link.

Vin extends the product side of that measurement. Adoption and time per task
belong near ML product KPIs. Learning curve, decision quality, pricing outcomes,
and decision-chain improvement belong there too. Those measures connect
[[data product adoption]] to revenue or cost-savings ranges. They do the same
for [[ai-for-finance-decision-support=>AI finance decision support]], instead
of stopping at model performance.
[[cite:make-money-with-machine-learning-roles-skills@75:14=>ML product adoption metrics]]

Impact measurement also needs a stakeholder loop. A data science manager can
pair client feedback and project-manager perspective with dashboarded KPIs. That
tests whether the model is improving the business process it was built for.

The KPI set should therefore monitor both the model and the surrounding process.
Sales can improve because of seasonality, sales execution, or other operations,
not only because the forecast changed. This links KPI design to [[Model
Monitoring]] and manager judgment about attribution.
[[cite:data-science-manager-vs-expert-hiring-guide@46:14=>Data Science Manager vs Expert]]

Data leaders also use KPIs to make foundation work visible. Tereza Iofciu
connects impact, product mindset, and KPIs. That work can disappear from the
business narrative unless leaders explain which user goal, team goal, or company
goal it supports.[[cite:data-leadership-coaching@24:32=>Data Leadership Coaching]]

Teams with a product mindset use the same rule for dashboards and internal tools.
The KPI should name the business decision or behavior the data product supports,
not only whether the report was delivered. Workshops, adoption evidence, and
time-saved estimates can then become part of the KPI story when the team has to
justify continued investment.
[[cite:building-and-scaling-data-team@47:08=>Building and Scaling a Data Team]]
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@42:18=>Last-Mile Data Delivery]]

For forecasting work, that links [[product analytics]] with [[model monitoring]].
Teams watch the forecast and the business process together. Higher sales may
come from seasonality, sales execution, or other operational changes rather than
the model.[[cite:data-science-manager-vs-expert-hiring-guide@46:14=>Data Science Manager vs Expert]]

[[person:linaweichbrodt=>Lina Weichbrodt]] makes the
same point during project intake in.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]
She starts with the business case, KPIs, and alternatives before modeling, then
turns stakeholder fears into mitigations and service levels. Impact assessment
also belongs in that intake.
KPI design therefore happens before model selection, and it shapes whether an ML
system should exist at all.

## Production and Trust Signals

Some KPIs guide growth, while others define unacceptable failure. Sroka
discusses threshold metrics and health or hygiene
metrics.[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]
Downtime and service reliability are KPI-adjacent because they tell a team when
a product is unsafe. Warning limits show when the product is no longer meeting
the standard users expect.

Weichbrodt's MLOps episode turns those signals into operating practice, and
service levels plus impact assessment set the operating bar. Post-mortems,
feature drift, and data monitoring show how KPI-adjacent signals become production
practice.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]
For [[production]] systems, KPI
movement should trigger investigation, user communication, or rollback work. A
KPI that nobody can act on is only a status label.

## Experimentation and Search Impact

KPIs also decide whether experiments and search changes ship. In [[person:jakobgraff=>Jakob Graff]]'s [[podcast:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]],
a product experiment can imply different choices. The choice changes when the primary
metric is revenue or conversion. It changes again when the team prioritizes retention
or long-term value.

Graff warns about too many primary metrics and noisy metrics. He also covers
seasonality and underpowered tests. KPI choice therefore belongs before
[[power analysis]] and
rollout decisions, not after a dashboard is already built. When KPI choice sits
between product experimentation and shared reporting, the
[[product-analyst-vs-data-analyst=>Product Analyst vs Data Analyst]] boundary
helps teams name ownership. A [[product-analyst=>Product Analyst]] may own the
product decision, while
another maintains the broader metric layer.

[[person:danielsvonava=>Daniel Svonava]] gives the
search-system version in.[[cite:building-production-search-systems=>Building Search Systems]]
He ties search impact to business metrics, A/B tests, and revenue, then
separates operational metrics from offline evaluation. Search KPIs therefore
bridge [[information retrieval]],
[[embeddings]], and
[[production search evaluation]].
Offline relevance can guide engineering, but shipping requires a business or
user-facing KPI that moves for the right audience.
