---
layout: wiki
title: "Data Trust and Strategy"
summary: "How data teams lose trust through unclear KPIs, brittle lineage, spreadsheet workarounds, weak communication, and impact-blind strategy choices."
related:
  - Data Strategy
  - Data Quality and Observability
  - Metrics
  - Data Governance
  - Data Product Management
  - Data Product Adoption
---

Data trust is the belief that a data product is reliable enough for the decision
at hand. It's narrower than [data strategy]({{ '/wiki/data-strategy/' | relative_url }})
and more business-facing than
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
People need to understand what a number means, where it came from, whether it's
current, and what risk they take when they act on it.

In the DataTalks.Club podcast discussions, trust fails when business users have
to re-audit every dashboard or reconcile competing KPIs. It also fails when they
rebuild context from spreadsheets. [Lior Barak](https://datatalks.club/people/liorbarak.html)
frames a mindful data strategy as a way to accept imperfect data while
communicating its limits. The team diagnoses root causes and chooses work by
business impact in
[Mindful Data Strategy for Business Impact](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html).
[Anusha Akkina](https://datatalks.club/people/anushaakkina.html) shows the finance
version in
[From Black-Box Systems to Augmented Decision-Making](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html),
where rigid ERPs push analysis into spreadsheet workarounds and hidden knowledge.

## Operational Confidence

Across these episodes, data trust means operational confidence. A stakeholder
can use a number or dashboard without starting a private verification project.
The same applies to a model output or finance insight. Barak's core KPI example
makes the failure visible.

When a CEO asks a CFO whether a management dashboard is accurate every day, the
dashboard is no longer a decision system. It's a recurring audit request
([20:50-21:26](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).

That puts trust close to [metrics]({{ '/wiki/metrics/' | relative_url }}) and
[KPIs]({{ '/wiki/kpis/' | relative_url }}), because the number needs a shared
definition and owner. It also needs a time window and decision.

Trust also depends on strategy choices. Barak argues that teams shouldn't jump
straight to a new catalog, lineage tool, or monitoring layer before they know
where trust is breaking. The cause may be ingestion or SQL logic. It may also be
changing product data structures or a missing process rather than tool
malfunction
([22:02-23:26](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).

Trust restoration works like
[data product management]({{ '/wiki/data-product-management/' | relative_url }}).
Teams diagnose the consumer problem, choose the highest-impact fix, and keep the
consumer informed while the product remains unreliable.

## First Trust Breaks

Barak and Akkina focus on different trust failures. Barak starts inside the data
team and dashboard lifecycle, where his strategy exposes status and classifies
incidents. It balances maintenance with innovation. It also
communicates business impact while the team fixes root causes
([28:12-37:29](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
His version sits near [data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
and [communication]({{ '/wiki/communication/' | relative_url }}).

Akkina starts from finance operations, where the trust problem isn't only a bad
dashboard. ERP systems are built for compliance and transaction storage. Finance
teams still need strategic analysis across sales and purchasing. They also need
operations, renewal, asset, and timing views.

When ERP structure can't represent those questions, teams fall back to
spreadsheets, add-ons, and manual joins
([17:15-24:31](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html)).
Her version sits near
[business intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
because the trust gap appears when operational systems can't answer the
business question fast enough.

The episodes therefore disagree on the first place to intervene. Barak would
ask which process failure makes a KPI untrusted and what impact the fix creates.
Akkina would ask whether the system structure forces people to preserve meaning
in side files and personal memory. Both paths lead back to mindful strategy.
Don't confuse a visible symptom with the system that keeps producing it.

## KPI Trust and Misunderstanding

KPI trust fails when leaders see one official number and another team presents a
different number. The damage grows when nobody can quickly explain the
difference. Barak describes marketing numbers diverging from a core KPI
dashboard.

He also describes delayed corrections after numbers were used externally.
Executives need credible numbers for investors too
([24:11-28:02](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
That's a strategic problem, not only a dashboard bug. The organization loses the
ability to make and defend decisions.

The diagnosis starts by treating the KPI as a data product. Teams review the
grain and source systems. They also review transformations and the downstream
audience. If the SQL that computes the dashboard is wrong, the KPI can be
published and still untrusted.
The same is true when ingestion misses data or when the source team changes
structures without coordination
([22:02-23:07](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).

Use [metrics]({{ '/wiki/metrics/' | relative_url }}) for KPI design in more
depth. Use this page for what happens after a KPI has lost credibility.

## Lineage Gaps and Process Failures

Lineage matters because trust failures need a path back to cause and forward to
impact. Barak names lineage alongside ingestion checks and SQL checks. He uses
those checks when diagnosing a core management KPI
([22:02-22:43](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
Without lineage, the team can't tell whether the issue starts in source data or
transformation logic. The issue may also come from dashboard semantics or a
downstream interpretation.

Process gaps are often the real failure. Barak warns that teams default to
rebuilding pipelines or buying monitoring tools. The root cause may be a product
team ingesting incorrect data every day or changing structures upstream
([22:43-23:26](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
[Data governance]({{ '/wiki/data-governance/' | relative_url }}) helps when it
records owners, definitions, access rules, and lineage. It doesn't restore
trust unless those controls change how teams detect, explain, and fix
recurring failures.

## Spreadsheet Dependence and Hidden Knowledge

Akkina's finance examples show a different route to lost trust. Some systems
store transactions but can't support strategic questions. ERPs are supposed to
integrate finance, procurement, sales, and operations. They also cover
manufacturing, supply chain, and logistics. Akkina says they often become
black-box systems with heavy manuals and expensive change paths
([17:15-20:48](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html)).

When finance teams need answers about renewals and project performance, they
create spreadsheet layers around the ERP. The same workaround appears for assets,
depreciation, stock, and seasonal demand
([24:31-26:52](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html)).

Those spreadsheets preserve business context, but they also create a trust
liability. Akkina describes manual Excel files where one mistake breaks the
analysis, while links live in someone's head. Turnover leaves the next person
with unknown formats and competing versions
([26:52-29:10](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html)).

The issue isn't that spreadsheets are always bad. Critical definitions, joins,
and exceptions become invisible to the data platform. They also become
undocumented for successors and hard to audit when the business needs speed.

## Communicating Uncertainty and AI Output Limits

Trust restoration is partly communication design, so Barak proposes a
green-yellow-red status on KPI dashboards. Green means reliable, yellow means
usable with known issues, and red means broken or not trustworthy
([30:47-31:31](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
That shifts the executive conversation from "can I trust this?" to "what's the
current status, what's the risk, and when will it be fixed?"

Generative AI raises the same expectation-management problem. Barak uses model
hallucinations to explain why users shouldn't blindly trust an output. Teams
also have to define the right level of confidence for the use case
([11:47-14:09](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).

Akkina similarly frames AI in finance as augmentation rather than full
automation. Finance teams need faster insight from ERP, CRM, expense, and other
systems. The product still has to respect compliance, explainability, and trust
([0:00-13:20 and 47:24](https://datatalks.club/podcast/s22e06-from-black-box-systems-to-augmented-decision-making.html)).

For AI products, trust work overlaps with
[AI product feedback loops]({{ '/wiki/ai-product-feedback-loops/' | relative_url }})
because users need ways to challenge outputs and feed corrections back into the
system.

## Choosing Business-Impact Work

Mindful data strategy chooses trust work by impact. Barak recommends tracking
where incidents happen, how often they recur, and which products cause most of
the damage. If three core products produce most incidents, root-cause work on
those products can restore more trust than broad platform polish
([29:16-30:10](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
That's also how teams avoid treating every complaint as equal.

Impact also decides the balance between maintenance, rollout, and innovation.
Barak describes healthy strategy as controlling those three work types. Users
stay involved during maintenance and rollouts, so teams understand frequency,
root causes, and business damage
([28:12-29:16 and 38:19-43:12](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
If innovation keeps shipping while maintenance is ignored, bugs and
inconsistencies accumulate until users stop trusting the product
([41:21-43:12](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).

Legacy replacement should use the same logic. Barak's legacy example replaces
daily Excel copy-paste with a simpler PostgreSQL/API/Tableau path, then sells
the change through user impact rather than architecture purity
([56:19-59:11](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
For executive ad hoc requests, he recommends asking why the request matters and
what impact it's expected to create
([1:00:23](https://datatalks.club/podcast/mindful-data-strategy-for-business-impact.html)).
That keeps [data strategy]({{ '/wiki/data-strategy/' | relative_url }}) tied to
decisions, revenue, risk, and time saved rather than a generic queue of fixes.

## Related Pages

Use these pages for adjacent strategy, quality, metric, and adoption context.

- [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [KPIs]({{ '/wiki/kpis/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
