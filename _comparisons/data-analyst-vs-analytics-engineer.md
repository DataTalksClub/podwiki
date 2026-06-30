---
layout: article
title: "Data Analyst vs Analytics Engineer"
keyword: "data analyst vs analytics engineer"
secondary_keywords:
  - analytics engineer vs data analyst
  - data analyst and analytics engineer
summary: "A podcast-grounded role comparison for deciding whether a team needs analyst ownership, analytics engineering ownership, or both."
related_wiki:
  - Data Analyst Role
  - Data Analyst Careers
  - Data Analyst vs Analytics Engineer
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Analytics Engineering Portfolio Projects
  - Product Analytics
  - Metrics
  - dbt
  - Data Quality and Observability
---

Data analysts and analytics engineers both work near SQL, dashboards, metrics,
and business questions. They don't own the same risk. A data analyst usually
owns the path from question to decision. An analytics engineer usually owns the
path from repeated analytical logic to a trusted model other people can reuse.

Start with
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}).
At 7:51-10:39, the episode frames analyst work around KPIs and dashboards. It
also covers problem sizing and experiment evaluation.

Then compare it with
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
At 4:05-10:04, she describes data modeling and pipelines. She also covers data
quality, Looker, and `dbt`. Tests, documentation, and dependency graphs come
with that workflow.

For the archive reference page, use
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}).
For the two role hubs, use
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}) and
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
If you're moving from analyst work toward model ownership, use the
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }}).

## Short Comparison

Use a data analyst when the missing owner has to answer a question, interpret a
metric, and help stakeholders decide what to do next. That person may write SQL
and build dashboards, but the main output is a recommendation, readout, or
business explanation.

Use an analytics engineer when the missing owner has to make analytical data
reusable and safer to change. That person may support BI and product analytics,
but the main output is a tested model or documented metric. It can also be a
transformation layer or BI-ready mart.

The practical split is:

- Data analyst: KPIs, ad hoc analysis, dashboards, and metric movement.
  Analysts also own experiment readouts, segment analysis, stakeholder
  explanation, and recommendations.
- Analytics engineer: table grain and source-to-mart transformations.
  Analytics engineers also own `dbt` models with tests and docs, semantic
  definitions, data quality checks, and BI-ready datasets.
- Shared surface: SQL, business context, metric definitions, product analytics,
  dashboard trust, event semantics, and source-data debugging.

Because the boundary sits inside the same stack, read this page alongside:

- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

## Data Analyst Fit

Choose a data analyst when the team has to understand what happened and what
decision should follow. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst tracks business metrics such as profit, listings, and buyer-seller
contacts. The analyst builds executive reports, uses SQL and dashboards, and
helps quantify whether a product problem deserves team time at 8:24-10:21.

The same episode links analysts to experiment evaluation. At 10:39, the
analyst checks whether a model-backed product change reduces posting-flow
drop-off or wrong-category listings. That makes
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[Experimentation]({{ '/wiki/experimentation/' | relative_url }}) analyst-facing
skills, not only data-science skills.

For product-facing work, the analyst often owns the question and the
interpretation. In
[From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) describes
work with product managers on experiments and new features at 14:20. The same
work includes A/B testing, cohort sizing, and RFM analysis. Dashboards and
presentations of insights sit in the same analyst mode, even when the title
includes analytics engineering.

The analyst should still understand where numbers come from.
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) explains why
teams need documented events and properties in
[How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
Without that source context, people can't trust funnels, activation workflows,
or signup spikes.

At 18:27-19:12, analysts and product managers see unexpected registration
spikes. They need event origins to trace those spikes. The same
source-awareness connects the analyst role to
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}).

## Analytics Engineer Fit

Choose an analytics engineer when repeated analytical logic has become a team
dependency. Victoria says analytics engineers build tables or views and clean
data. They expose data to Looker, handle failures, and make data available to
analysts and data scientists
([Master Analytics Engineering at 4:05-5:47]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
That isn't a one-off chart. It's maintained data modeling.

`dbt` matters because it changes how teams operate SQL work. At 6:49-10:04,
Victoria explains SQL files, YAML docs, and GitHub version control. She also
covers non-null and unique tests, dependency graphs, and scheduled runs. Those
practices turn warehouse SQL into something closer to production code. Use the
[dbt]({{ '/wiki/dbt/' | relative_url }}) page for the tool-level context.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) gives
the deeper role definition in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
At 8:20-8:42, he says the role is often misread as only bridging analysts and
data engineers. His stronger definition starts at 11:03: analytics engineers
take business reality and make data resemble it. He then adds rigor,
robustness, and reproducibility. At 16:25-18:35, he contrasts fast dashboard
work with engineering work that puts testability first.

Use the distinction to assign ownership. Analysts can move quickly when a
stakeholder needs an answer today. Analytics engineers slow down when the same
answer will feed many dashboards, experiments, forecasts, or activation flows.
They build a model other people can trust without copying business logic into
every query.

## Boundary Blurs

The title split depends on company size. In Victoria's role comparison at
14:34-25:18, the analytics engineer sits between data analyst and data
engineer. She says the lines are blurry across companies and even within one
team.

Analysts have business knowledge and often write business-heavy SQL, while
data engineers have software practices and infrastructure ownership. Analytics
engineers bring those worlds together around modeled, curated data.

Nikola's small-team story shows the same blur from inside the job. At 14:14,
he says he worked as both an analytics engineer and a data analyst on a
four-person team. His work included KPI reassessment, dashboards, product-team
support, and A/B testing. It also included ad hoc analysis, RFM analysis, and
data model changes. Later, at 19:07-22:08, he describes the `dbt` migration and
transformation layers that turned that work into a reusable model.

Nikola returns to the title question at 25:06-28:40. His official role combined
analytics engineer and data analyst because the BI team was small. He says
small and medium-sized teams shouldn't get stuck on the title split. The work
still needs analytical skill, KPI fluency, and domain modeling. In a
larger data department, though, separating analysts and analytics engineers can
make structural sense because people can focus.

Use work mode instead of title when one person covers both sides:

- Stay in analyst mode for a one-off question, an experiment readout, a metric
  explanation, or a stakeholder recommendation.
- Move into analytics-engineering mode when copied SQL, inconsistent filters,
  slow joins, unclear table grain, or repeated metric disputes keep returning.
- Split the role when the same person can't both answer urgent questions and
  maintain the modeled analytical layer.

The [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
and
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
pages are useful when an analyst wants to move toward the engineered side of
the boundary. For a step-by-step transition path, use
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }}).

## Dashboards, Metrics, and Models

Dashboards don't decide the role boundary by themselves. A data analyst can
own a dashboard when it's a stakeholder view, an exploratory readout, or a
communication surface. The analyst owns chart choices, caveats, and the
business recommendation.

An analytics engineer should own the reusable layer behind the dashboard when the
dashboard depends on shared logic. Victoria's `dbt` discussion ties that layer
to docs, tests, version control, and a dependency graph. Juan's discussion of
data modeling asks what each row represents and how the business domain should
fit into tables at 20:21-22:09. Those are analytics-engineering questions
because the answer affects many future analyses.

Metrics follow the same rule. Analysts can define a KPI for a decision and
explain movement to a product manager or executive. Analytics engineers should
encode the canonical definition when many teams reuse the metric. They should
also encode grain, filters, and time windows. Exclusions and source assumptions
belong in the same modeled definition.

For the broader metric topic, use
[Metrics]({{ '/wiki/metrics/' | relative_url }}) and
[Data Products]({{ '/wiki/data-products/' | relative_url }}).

## Product and Growth Data

Product analytics shows why analysts and analytics engineers need each other.
An analyst can interpret funnels, cohorts, retention, and experiment results.
The same analyst needs event meaning, assignment logic, and trusted modeled
tables before the interpretation is defensible.

Arpit's data-led growth episode traces the full flow. Teams start with a
tracking plan, engineers instrument events, and the data flows into
analytics tools and warehouses
([22:50-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
At 35:56, he describes the warehouse as the place where teams store and
transform structured data. Teams also clean and model that data before
analyzing it in BI.

At 37:25, he adds reverse ETL and operational analytics. Teams can then move
modeled data into sales and marketing tools. The same modeled data can also
reach advertising, support, or product tools.

In that flow, analysts own interpretation and decisions. Analytics engineers
own modeled data that can survive reuse in BI and activation. Data engineers
and product engineers still matter because events need instrumentation,
warehouses need pipelines, and downstream tools need reliable delivery. Use
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }}),
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}), and
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
for the broader adoption surface.

## Hiring and Portfolio Signals

For a data analyst, look for proof that the person can move from a question to
a decision.

Strong examples include:

- SQL analysis
- KPI definitions
- dashboards
- cohort or funnel analysis
- experiment readouts
- stakeholder memos
- clear caveats

The useful signal isn't "made a chart." The stronger signal is "changed or
clarified a decision with evidence."

For an analytics engineer, look for proof that the person can make analysis
reusable.

Strong examples include:

- a modeled mart with clear table grain
- a `dbt` project with tests and docs
- a metric layer
- a dashboard model migration
- a source-to-presentation transformation path

The useful signal isn't "knows `dbt`." The stronger signal is "made trusted
analytical data easier to reuse and safer to change."

[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }}) gives the
hiring-screen version in
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }}).
At 21:32-32:40, she describes sourcing from the job description, checking
responsibilities instead of titles alone, and reading beyond tool lists and
buzzwords. For this comparison, that means a data analyst CV should show the
questions, decisions, and stakeholders behind the analysis. An analytics
engineer CV should show the models, tests, docs, and ownership behind the
tools.

[Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }}) adds the job-ad
side in
[Data Science Jobs]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }}).
At 27:18-30:44, she recommends checking whether the team is described,
responsibilities are well-defined, and objectives appear instead of a long
technology checklist. A posting for either role should name the work. If it
asks for every data tool without saying whether the person owns decisions or
models, the title is weak evidence. Quality ownership and stakeholder ownership
should be visible too.

The overlap matters because analysts who understand modeling can avoid bad
joins and mixed grains. Analytics engineers who understand stakeholder
questions can model the right entities instead of only making tidy tables.
Victoria's role comparison and Juan's foundations episode both make that
boundary practical. The title matters less than who owns the question, who owns
the reusable model, and who owns the quality path.

## Related Pages

These pages cover the role definitions, adjacent workflows, and learning paths
behind the comparison:

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineer article]({{ '/guides/analytics-engineer/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Product Analyst article]({{ '/guides/product-analyst/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
