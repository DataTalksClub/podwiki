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

A data analyst helps a team explain what happened and why. The analyst also
helps decide what should follow. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Alexey Grigorev]({{ '/people/alexeygrigorev/' | relative_url }}) places the
analyst near product decisions.

Around 7:51-10:39, the analyst knows company data and retrieves it. They define
KPIs, build dashboards, quantify product problems, and evaluate experiments. The
broader analyst hub is
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}).

An analytics engineer owns the reusable analytical data layer. Analysts and data
scientists build on it, as do product teams and BI users. In
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes daily work around data modeling, pipelines, and data quality from
4:05-10:04. Looker and `dbt` are part of that work.

She also ties the role to SQL transformations, tests, documentation, and
version control. The broader role hub is
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

The data analyst vs analytics engineer comparison matters because both roles
write SQL, clean data, discuss metrics, and build dashboard-facing work. The
archive draws the practical boundary around ownership. Analysts own the
question, interpretation, and recommendation. Analytics engineers own the
tested and documented model layer that makes repeated analysis safer
([Perez Mola at 14:34-16:54]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Juan Manuel Perafan at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Common Definition

Across the cited DataTalks.Club episodes, data analysts face the decision. They
retrieve company data, interpret it, define KPIs, and build dashboards. They
also write reports and recommend what the business or product team should do.
Grigorev's product example has analysts size a category-classification problem
and show how many users it affects. The analyst then judges whether a shipped
feature improved behavior after an A/B test
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

The analytics engineer role is model-facing. Analytics engineers turn raw or
messy business data into shared tables and marts. They also maintain metric
definitions. Perez
Mola ties that work to SQL transformations, `dbt` documentation, and Git-based
version control. Tests and DAGs also sit in that role discussion.

Warehouses and Looker do too
([Master Analytics Engineering at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[dbt]({{ '/wiki/dbt/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

Both roles need business context. Analysts need enough modeling sense to avoid
reading a metric at the wrong grain. Analytics engineers need enough domain
knowledge to model the right entities, states, and definitions. Perafan
describes analytics engineering as taking business reality and making the data
resemble it. He then adds software engineering rigor so analytical work becomes
replicable and safer to reuse
([Foundations of the Analytics Engineer Role at 11:03-13:18]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

## Guest Differences

Guests differ on whether analytics engineering should be a separate title.
Perez Mola presents it as a bridge between data analysts and data engineers.
Analysts should spend less time cleaning and modeling data, while data
engineers often prefer infrastructure work over business-specific models
([Master Analytics Engineering at 14:34-19:05]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) agrees
that the title sits near that gap, but he pushes against defining the role by
what analysts and engineers don't do. For him, analytics engineers add rigor,
testability, and reproducibility to analytical modeling
([Foundations episode at 7:56-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also differ by company size. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
describes an official role that combined analytics engineering and data analysis
in a small team. The same job covered BI, dashboards, `dbt`, and Looker.
Product support, KPI work, and A/B testing also sat in that role.

He argues that large organizations can split data analysts and analytics
engineers more cleanly. Smaller teams may need the same person to cover both
modes
([From Marketing to Analytics Engineering at 14:14-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})).

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives a
growth-stack version of that split. Early companies may have one data person,
while larger flows separate data engineers, analysts, and analytics engineers.
Product operations, DataOps, and self-service users sit around that split
([Data-Led Growth Stack at 46:13-51:06]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})).

Guests also differ in tool emphasis. Perez Mola and Maksimovic both tie
analytics engineering strongly to `dbt`, but neither reduces the role to a
single tool. Perez Mola uses `dbt` to explain SQL transformations and tests.
She also links it to documentation and version control. Maksimovic says `dbt`
popularized the role.

The deeper craft still includes data modeling theory and domain models.
Wide-versus-narrow table tradeoffs and incrementalization choices also matter
([Perez Mola at 6:49-10:04 and 30:06]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Maksimovic at 28:40-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Questions, Metrics, and Recommendations

Analysts usually own metric interpretation and the recommendation that follows.
They decide how to size the question, which KPI answers it, which segment or
cohort matters, and how to explain the caveats to a stakeholder. Grigorev's
analyst example includes KPI definition and executive reporting. It also
includes product problem sizing and post-launch experiment evaluation
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})).

Analytics engineers usually own canonical metric logic when several teams reuse
it. If revenue, retention, or active users appear in many dashboards, the
definition belongs in a modeled layer instead of copied SQL. Sessions, listings,
or other business entities fit the same rule. Perafan's modeling discussion asks
whether tables and columns match the business concepts stakeholders use. Perez
Mola's role discussion puts data modeling and quality checks behind the BI
surface
([Foundations episode at 20:21-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Master Analytics Engineering at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Data Products]({{ '/wiki/data-products/' | relative_url }})).

## Dashboards, Models, and dbt

For dashboards, analysts usually own the stakeholder view. They choose the chart
and filter, then explain the caveat and decision. Analytics engineers own the
model behind the dashboard when copied SQL or inconsistent filters make it hard
to trust. Slow joins and repeated business logic show the same problem.

Perez Mola's `dbt` discussion ties that model layer to SQL files and YAML
documentation. It also ties the layer to GitHub version control, tests, and a
DAG.

Analyst SQL becomes analytics engineering evidence after it becomes documented
and tested transformations
([Master Analytics Engineering at 6:49-8:59 and 38:53-40:42]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})).

Maksimovic's team shows the same boundary in practice because KPI and dashboard
work came before the `dbt` migration. He also describes Looker and LookML
reporting, with product support and A/B testing in the same role.

If individual reports depend on a domain model, the team moves into analytics
engineering. The other sign is shared transformation layers
([From Marketing to Analytics Engineering at 18:34-25:17]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})).

## Experiments, Events, and Activation

For experiments, analysts usually own success criteria, segment readouts, and
the explanation of whether a product change worked. Grigorev ties analysts to
post-launch A/B test evaluation. In his example, the team checks whether a
categorization model reduces drop-off or wrong categories
([Data Team Roles Explained at 10:21-11:17]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})).

Analytics engineers own the repeated experiment tables when the organization
needs stable event, assignment, exposure, and metric models. Maksimovic's
analytics engineering work includes product support and A/B testing. It also
includes the `dbt` and Looker layers that make repeated product analytics
possible
([From Marketing to Analytics Engineering at 14:14 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

Event tracking and activation add another shared boundary. Analysts need to
understand event meaning before interpreting funnels or anomalies. Analytics
engineers help make those events usable in warehouses and BI. They also prepare
the data for reverse ETL flows.

Choudhury places analysts and analytics engineers in the same data-led-growth
flow. That flow includes tracking plans, event properties, and warehouses.
Transformations and BI analysis also sit there. Product operations and
activation do too
([Data-Led Growth Stack at 13:34-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}),
[Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})).

## Team Structure and Ownership

Use ownership, not title, to separate the roles. Give the analyst work that
ends in an answer, such as a product decision or metric explanation. Experiment
readouts, reports, and recommendations belong there too. Give the analytics
engineer work that ends in a reusable analytical asset.

That side includes modeled tables, BI-ready marts, and documented metrics. Test
suites, semantic layers, and transformation DAGs belong there too.

One person can hold both modes. Maksimovic's official role combined analytics
engineer and data analyst work because his team was small. Perez Mola notes
that role definitions vary by company setup around 31:09.

Choudhury also describes early-stage teams with one data person. Later-stage
flows split work across data engineers, analysts, and analytics engineers.
Product operations can be part of the same split
([Maksimovic at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Perez Mola at 31:09-33:02]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Choudhury at 46:13-51:06]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

The same project can also switch modes. A one-off funnel readout can stay
analyst-owned, but reusable funnel logic belongs with analytics engineering when
dashboards and experiment analysis depend on it. Reverse ETL audiences and
executive reporting create the same pressure
([Data-Led Growth Stack at 28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Career and Portfolio Signals

Data analysts show strength by moving from question to decision. Strong
evidence includes SQL, dashboards, and KPI definitions. Cohort or funnel
analysis matters too. Experiment interpretation, written recommendations, and
stakeholder context matter too.

Grigorev's role definition names SQL, Python or R, and dashboard tools. It also
names basic statistics and reports. Recommendations, problem sizing, and A/B
test interpretation matter too
([Data Team Roles Explained at 7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})).

Analytics engineers show strength by making analytical work reusable and safer.
Strong evidence includes clear table grain, dimensional modeling, SQL
transformations, and `dbt` tests. Documentation, version control, and DAG
awareness matter too. Warehouse transformations and BI-ready marts matter too.

Perez Mola names these tools and practices directly, while Perafan adds
robustness and testability as the role boundary. Those concerns turn fast
dashboard work into engineering work
([Master Analytics Engineering at 4:05-10:04 and 26:10]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations episode at 16:25-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

People often move from BI and domain work into analytics engineering.
Maksimovic moved from marketing reporting into BI and SQL. He then worked with
Looker and `dbt`.

Data modeling came next, followed by product analytics and A/B testing.
Marketing funnels and KPIs gave the technical modeling work a business target.
User journeys gave it one too
([From Marketing to Analytics Engineering at 7:18-23:12 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Data Analyst to Analytics Engineer]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})).

## Related Pages

These pages cover adjacent role boundaries, tools, and decision workflows.

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Data Analyst to Analytics Engineer]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
