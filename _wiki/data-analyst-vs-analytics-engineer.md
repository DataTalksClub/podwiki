---
layout: wiki
title: "Data Analyst vs Analytics Engineer"
summary: "A podcast-backed comparison of the data analyst and analytics engineer role boundary: decisions, dashboards, reusable models, dbt, data quality, and team ownership."
related:
  - Data Analyst Role
  - Data Analyst Careers
  - Analytics Engineering
  - Product Analytics
  - Metrics
  - dbt
---

## Definition and Scope

A data analyst helps a team understand what happened, why it happened, and what
decision should follow. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
analysts sit near product decisions. Around 7:51-10:39, they know company data
and define KPIs. They also build dashboards, quantify product problems, and
evaluate experiments. For the broader career and skill hub, start with
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}).

An analytics engineer owns the reusable analytical data layer. Analysts and data
scientists depend on it, as do product teams and BI users. In
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes daily work around data modeling, pipelines, and data quality from
4:05-10:04. Looker is part of that work.

She also connects analytics engineering to SQL, `dbt`, and version control.
Tests and dependency graphs are part of the same discussion.

For the full role hub, start with
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

The comparison matters because the titles overlap. Analysts often write SQL,
clean data, define metrics, and build dashboards. Analytics engineers also need
business context and stakeholder judgment.

Use ownership as the boundary. Analysts own decision support, while analytics
engineers own reusable and tested analytical models
([Perez Mola at 14:34-16:54]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Juan Manuel Perafan at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Link Map

Start with these role and concept pages:

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}) for the analyst side of the boundary.
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }}) for portfolio, hiring, and transition signals.
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}) for reusable models, tests, docs, and semantic layers.
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}) and [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }}) for skill-building paths.
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}), [Metrics]({{ '/wiki/metrics/' | relative_url }}), [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}), and [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}) for analyst-facing decision work.
- [dbt]({{ '/wiki/dbt/' | relative_url }}), [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}), [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}), and [Data Products]({{ '/wiki/data-products/' | relative_url }}) for analytics-engineering practice.

Core podcast discussions for this comparison:

- [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}) defines analysts through data interpretation, dashboards, KPIs, product problem sizing, and experiment evaluation.
- [Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}) defines analytics engineering through data modeling, data quality, Looker, `dbt`, SQL tests, version control, and role comparisons.
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}) separates fast analytics work from robust engineering work and reframes analytics engineering as turning business reality into data.
- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}) shows how one small team combined data analyst and analytics engineer responsibilities around BI, product analytics, `dbt`, Looker, and dashboards.
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) places analysts and analytics engineers in the same growth-data flow with data engineers, product operations, BI, warehouses, and reverse ETL.

## Common Definition

Across the cited episodes, data analysts face the decision. They retrieve
company data, interpret it, define KPIs, and build dashboards. They also prepare
reports and give recommendations. In the product example from
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
analysts quantify how many users a product problem affects. They also help judge
whether a new feature improved behavior after an A/B test
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

The analytics engineer role is model-facing. Analytics engineers turn raw or
messy business data into shared tables, marts, and metric definitions. They also
prepare BI-ready models. Perez Mola ties that work to SQL transformations,
`dbt` documentation, Git-based version control, and tests. She also connects it
to DAGs, warehouses, and Looker
([Master Analytics Engineering at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[dbt]({{ '/wiki/dbt/' | relative_url }})).

Analysts need enough data modeling sense to avoid misreading metrics. Analytics
engineers need enough domain knowledge to model the right entities and grains.
Perafan describes analytics engineering as taking business reality and making
the data resemble it. Software engineering rigor changes how that work is done
([Foundations episode at 11:03-13:18]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

## Common Decision Rule

Choose a data analyst owner when the work mainly answers a business or product
question. That also covers growth and operational questions. Give the analyst
problem sizing and KPI choice. Give them experiment readouts, metric
explanations, and stakeholder recommendations.

The analyst example covers problem sizing and dashboards. It also covers reports
and post-launch experiment evaluation
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})).

Choose an analytics engineer owner when the answer should become reusable
infrastructure for many analyses. That includes canonical models for customers,
listings, and sessions. It can also include orders, subscriptions, or events.
Analytics engineers should also own repeated dashboard logic. They should own
versioned SQL transformations, model tests, documented metric definitions, and
BI-facing marts.

Perez Mola connects that ownership to data modeling, quality checks, and `dbt`.
Looker and Snowflake also appear in the same role discussion. DAGs, analyst
collaboration, and data scientist collaboration appear there too
([Master Analytics Engineering at 4:05-10:04 and 33:02]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

When one person has both titles or both responsibilities, separate the mode of
work. Fast exploratory analysis can stay analyst-owned. Move reused logic into
analytics-engineering ownership when dashboards, experiments, forecasts, or
activation flows depend on it.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) describes
this small-team overlap. The official role combined analytics engineering and
data analysis while covering BI and dashboards. The same job also included
`dbt` and Looker, plus product support and A/B testing
([Maksimovic at 14:14-25:17]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})).

## Guest Differences

Guests differ on whether analytics engineering should be a separate title.
Perez Mola presents it as a bridge between data analysts and data engineers.
Analysts should spend less time cleaning and modeling data, while data engineers
often prefer infrastructure work over business-specific modeling
([Master Analytics Engineering at 14:34-19:05]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) agrees
that the title sits near that gap, but he says the better definition isn't "what
analysts and engineers don't do." For him, analytics engineers add rigor and
testability. They also add reproducibility and robustness to analytical modeling
([Foundations episode at 7:56-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also differ by company size. Maksimovic argues that small and mid-sized
teams may not need to split data analyst and analytics engineer titles. The same
person still needs KPIs and business model knowledge. Domain modeling, SQL, and
dashboard work still matter. He sees the split making more structural sense in
larger data departments
([marketing-to-analytics episode at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
growth-stack version of the same point. Early companies may
have one data person. Larger flows separate data engineers, analysts, analytics
engineers, and product operations. They may also add DataOps and self-service
users
([data-led growth episode at 46:13-51:06]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})).

Tool emphasis differs as well. Perez Mola and Maksimovic both tie the analytics
engineer title strongly to `dbt`, but neither reduces the role to one tool.
Perez Mola uses `dbt` to explain SQL transformations, tests, and documentation.
Version control and dependency graphs matter there too. Maksimovic says `dbt`
popularized the role, but data modeling theory and tradeoffs still matter
([Perez Mola at 6:49-10:04 and 30:06]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Maksimovic at 28:40-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Practical Boundary by Work Item

For metric questions, analysts usually own the interpretation and
recommendation. Analytics engineers usually own the canonical metric logic when
multiple teams reuse it. Grigorev's analyst example includes KPIs, reports, and
feature evaluation. Perafan's modeling example asks whether tables and columns
match the business terms stakeholders expect
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Foundations episode at 20:21-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

For dashboards, analysts can own the stakeholder view and chart choices. They
can also own caveats and recommendations. Analytics engineers should own the
reusable model behind the dashboard when copied SQL or slow joins appear.
Inconsistent filters and repeated business logic are the same warning sign.

Perez Mola's `dbt` discussion ties that model layer to docs, tests, and version
control. It also adds dependency visibility
([Master Analytics Engineering at 6:49-8:59]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Data Products]({{ '/wiki/data-products/' | relative_url }})).

For experiments, analysts usually own success criteria and segment readouts.
They also explain whether the product change worked. Analytics engineers own
stable event tables and assignment tables. They also own exposure tables and
metric tables when teams repeat experiment analysis.

[Data Team Roles Explained at 10:21]({{ '/podcasts/data-team-roles/' | relative_url }})
ties analysts to post-launch A/B test evaluation. In
[Maksimovic's episode at 14:14 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
the team puts product support inside the BI stack and A/B testing inside the
`dbt` stack. See also
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).

For event tracking and activation, analysts need to understand event meaning
before interpreting funnels or anomalies. Analytics engineers help make those
events usable in warehouses and BI. They also help with modeled tables and
reverse ETL flows.
Choudhury places analysts and analytics engineers in the same team flow around
tracking, BI, warehouses, and product operations. Activation sits in that same
flow too
([data-led growth episode at 13:34-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[Data Activation]({{ '/wiki/data-activation/' | relative_url }})).

## Career and Hiring Signals

A data analyst signal is the ability to move from question to decision. Strong
evidence includes SQL, dashboards, and KPI definitions. Cohort or funnel
analysis also matters. Experiment interpretation and written recommendations are
part of the signal. Stakeholder context matters too.

The role definition names SQL, Python or R, dashboard tools, and statistics.
Reports and recommendations appear there too. Problem sizing and A/B test
interpretation also matter
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})).

An analytics engineer signal is the ability to make analytical work reusable
and safer. Strong evidence includes SQL models, clear table grain, dimensional
modeling, and `dbt` tests. Docs and version control matter too. DAG awareness
and warehouse transformations matter too. BI-ready marts also matter.

Perez Mola's role episode names those tools and practices directly. Perafan
explains the role boundary through robustness and testability. Those concerns
change the work from fast dashboarding into engineering
([Master Analytics Engineering at 4:05-10:04 and 26:10]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations episode at 16:25-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

Transition paths often pass through BI and domain knowledge. Maksimovic moved
from marketing reporting into BI, SQL, Looker, and `dbt`. He then worked on
data modeling, product analytics, and A/B testing.

That path worked because marketing funnels and KPIs gave the technical modeling
work a business target. User journeys did too
([marketing-to-analytics episode at 7:18-23:12 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})).

## Related Pages

Use these pages for adjacent role boundaries, tools, and decision workflows.

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Analytics Engineer article]({{ '/articles/analytics-engineer/' | relative_url }})
