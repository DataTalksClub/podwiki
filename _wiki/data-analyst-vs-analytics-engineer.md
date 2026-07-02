---
layout: article
tags: ["comparison"]
title: "Data Analyst vs Analytics Engineer"
keyword: "data analyst vs analytics engineer"
secondary_keywords:
  - analytics engineer vs data analyst
  - data analyst and analytics engineer
summary: "A role comparison for deciding whether a team needs analyst ownership, analytics engineering ownership, or both."
related_wiki:
  - Data Analyst Role
  - Data Analyst Careers
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
[Data Team Roles Explained](https://datatalks.club/podcast/data-team-roles.html),
which puts analyst work around KPIs and dashboards at 7:51-10:39. It also
covers problem sizing and experiment evaluation.

Then compare it with
[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html) in
[Master Analytics Engineering](https://datatalks.club/podcast/analytics-engineer-skills-tools.html).
At 4:05-10:04, she describes data modeling, pipelines, and data quality.
Looker and `dbt` also sit in that work. Tests, documentation, and dependency
graphs come with it.

For the two role hubs, use
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}) and
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
If you're moving from analyst work toward model ownership, use the
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }}).

## Short Comparison

Use a data analyst when the missing owner has to answer a question, interpret a
metric, and help stakeholders decide what to do next. That person may write SQL
and build dashboards, but the main output is a recommendation, readout, or
business explanation. The analyst side is grounded in
[Data Team Roles Explained](https://datatalks.club/podcast/data-team-roles.html)
and Nikola Maksimovic's
[marketing-to-analytics-engineering role transition discussion](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html).

Use an analytics engineer when the missing owner has to make analytical data
reusable and safer to change. That person may support BI and product analytics,
but the main output is a tested model or documented metric. It can also be a
transformation layer or BI-ready mart. The engineering side is grounded in
[Victoria Perez Mola's analytics engineering role discussion](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
and Juan Manuel Perafan's
[analytics engineering foundations discussion](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html).

The practical split is:

- Data analyst: KPIs, ad hoc analysis, dashboards, and metric movement.
  Analysts also own experiment readouts, segment analysis, stakeholder
  explanation, and recommendations.
- Analytics engineer: table grain and source-to-mart transformations.
  Analytics engineers also own `dbt` models with tests and docs, semantic
  definitions, data quality checks, and BI-ready datasets.
- Shared surface: SQL, business context, metric definitions, product analytics,
  dashboard trust, event semantics, and source-data debugging.

This split follows
[Data Team Roles Explained](https://datatalks.club/podcast/data-team-roles.html),
[Master Analytics Engineering](https://datatalks.club/podcast/analytics-engineer-skills-tools.html),
and
[Foundations of the Analytics Engineer Role](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html).

Because the boundary sits inside the same stack, the adjacent concepts matter:

- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

## Data Analyst Fit

Choose a data analyst when the team has to understand what happened and what
decision should follow. In
[Data Team Roles Explained](https://datatalks.club/podcast/data-team-roles.html),
the analyst tracks business metrics such as profit, listings, and buyer-seller
contacts. The analyst builds executive reports, uses SQL and dashboards, and
helps quantify whether a product problem deserves team time at 8:24-10:21.

The same episode links analysts to experiment evaluation. At 10:39, the
analyst checks whether a model-backed product change reduces posting-flow
drop-off or wrong-category listings. That makes
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[Experimentation]({{ '/wiki/experimentation/' | relative_url }}) analyst-facing
skills, not only data-science skills.

Analysts usually own metric interpretation and the recommendation that follows.
They decide how to size the question and which KPI answers it. They also decide
which segment or cohort matters and how to explain the caveats to a stakeholder.
Grigorev's analyst example includes KPI definition and executive reporting. It
also includes product problem sizing and post-launch experiment evaluation
([Data Team Roles Explained at 7:51-10:39](https://datatalks.club/podcast/data-team-roles.html),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})).

For product-facing work, the analyst often owns the question and the
interpretation. In
[From Marketing to Analytics Engineering](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html),
[Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) describes
work with product managers on experiments and new features at 14:20. The same
work includes A/B testing, cohort sizing, and RFM analysis. Dashboards and
presentations of insights sit in the same analyst mode, even when the title
includes analytics engineering.

The analyst should still understand where numbers come from.
[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) explains why
teams need documented events and properties in
[How to Build a Data-Led Growth Stack](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html).
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
([Master Analytics Engineering at 4:05-5:47](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).
That isn't a one-off chart. It's maintained data modeling.

`dbt` matters because it changes how teams operate SQL work. At 6:49-10:04,
Victoria explains SQL files, YAML docs, and GitHub version control. She also
covers non-null and unique tests, dependency graphs, and scheduled runs. Those
practices turn warehouse SQL into something closer to production code. Use the
[dbt]({{ '/wiki/dbt/' | relative_url }}) page for the tool-level context.

[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html) gives
the deeper role definition in
[Foundations of the Analytics Engineer Role](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html).
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

Analytics engineers usually own canonical metric logic when several teams reuse
it. Analytics engineers should model revenue or retention definitions when many
dashboards use them. The same rule applies to active users and to sessions or
listings.
Perafan's modeling discussion asks whether tables and columns match the business
concepts stakeholders use
([Analytics engineering foundations at 20:21-26:23](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).
Perez Mola's role discussion puts data modeling and quality checks behind the
BI surface
([Master Analytics Engineering at 4:05-10:04](https://datatalks.club/podcast/analytics-engineer-skills-tools.html),
[Data Products]({{ '/wiki/data-products/' | relative_url }})).

## Boundary Blurs

The title split depends on company size. In
[Victoria Perez Mola's comparison of analytics engineers, analysts, and data engineers](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
at 14:34-25:18, the analytics engineer sits between data analyst and data
engineer. She says the lines are blurry across companies and even within one
team.

Analysts bring business knowledge and SQL that answers stakeholder questions.
Data engineers bring software practices, infrastructure ownership, and pipeline
concerns. Analytics engineers bring those worlds together around modeled,
curated data.
Perez Mola presents the role as a bridge because analysts should spend less
time cleaning and modeling data. Data engineers often prefer infrastructure
work over business-specific models
([Master Analytics Engineering at 14:34-19:05](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).

Nikola's
[small analytics engineering and BI team story](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)
shows the same blur from inside the job. At 14:14, he says he worked as both an
analytics engineer and a data analyst on a four-person team. His work included
KPI reassessment, dashboards, product-team support, and A/B testing. It also
included ad hoc analysis, RFM analysis, and data model changes. Later, at
19:07-22:08, he describes the `dbt` migration and transformation layers that
turned that work into a reusable model.

Nikola returns to the title question in
[From Marketing to Analytics Engineering](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)
at 25:06-28:40. His official role combined analytics engineer and data analyst
because the BI team was small. He says small and medium-sized teams shouldn't
get stuck on the title split. The work still needs analytical skill, KPI
fluency, and domain modeling. In a larger data department, though, separating
analysts and analytics engineers can make structural sense because people can
focus.

Perafan agrees that the role sits near the analyst-engineer gap. But he pushes
against defining analytics engineering only by what analysts and data engineers
don't do. For him, analytics engineers add rigor, testability, and
reproducibility to analytical modeling
([Analytics engineering foundations at 7:56-18:35](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).

[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) gives a
growth-stack version of the split. Early companies may have one data person,
while larger teams split the work among data engineers, analysts, and analytics
engineers. Product operations, DataOps, and self-service users sit around the
same split
([Data-led growth team structure at 46:13-51:06](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html),
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})).

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
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }}).

## Dashboards, Metrics, and Models

Dashboards don't decide the role boundary by themselves. A data analyst can
own a dashboard when it's a stakeholder view, an exploratory readout, or a
communication surface. The analyst owns chart choices, caveats, and the
business recommendation.

An analytics engineer should own the reusable layer behind the dashboard when
the dashboard depends on shared logic. Victoria's
[`dbt` modeling and documentation discussion](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
ties that layer to docs, tests, version control, and a dependency graph. Juan's
[business-domain modeling discussion](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)
asks what each row represents and how the business domain should fit into tables
at 20:21-22:09. Those are analytics-engineering questions because the answer
affects many future analyses.

Metrics follow the same rule. Analysts can define a KPI for a decision and
explain movement to a product manager or executive. Analytics engineers should
encode the canonical definition when many teams reuse the metric. They should
also encode grain, filters, and time windows. Exclusions and source assumptions
belong in the same modeled definition.

Analyst SQL becomes analytics engineering work after it becomes documented and
tested transformations. Perez Mola ties that shift to SQL files and YAML
documentation. She also ties it to GitHub version control, tests, and a DAG
([Master Analytics Engineering at 6:49-8:59 and 38:53-40:42](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).

Maksimovic's team shows the same boundary in practice. For that team, KPI and
dashboard work came before the `dbt` migration. Looker reporting and the shared
transformation layer came later
([From Marketing to Analytics Engineering at 18:34-25:17](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html),
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})).

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
([event tracking and warehouse flow at 22:50-30:03](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).
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

The same project can switch modes because a one-off funnel readout can stay
analyst-owned. Reusable funnel logic belongs with analytics engineering when
dashboards and experiment analysis depend on it. Reverse ETL audiences and
executive reporting create the same pressure
([Data-led growth activation and reverse ETL discussion at 28:52-37:25](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Hiring and Portfolio Signals

For a data analyst, look for proof that the person can move from a question to
a decision. Grigorev's role definition names SQL and Python or R. It also names
dashboard tools, basic statistics, reports, and recommendations.
Problem sizing and A/B test interpretation also matter
([Data Team Roles Explained at 7:51-10:39](https://datatalks.club/podcast/data-team-roles.html),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})).

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
reusable. Perez Mola names data modeling and SQL transformations. She also names
tests, documentation, version control, and DAG awareness. Perafan adds
robustness and testability as the role boundary
([Master Analytics Engineering at 4:05-10:04 and 26:10](https://datatalks.club/podcast/analytics-engineer-skills-tools.html),
[Analytics engineering foundations at 16:25-18:35](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html),
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

Strong examples include:

- a modeled mart with clear table grain
- a `dbt` project with tests and docs
- a metric layer
- a dashboard model migration
- a source-to-presentation transformation path

The useful signal isn't "knows `dbt`." The stronger signal is "made trusted
analytical data easier to reuse and safer to change."

People often move from BI and domain work into analytics engineering.
Maksimovic moved from marketing reporting into BI and SQL before he worked with
Looker and `dbt`. Data modeling and product analytics came next, followed by
A/B testing.

Marketing funnels gave the modeling work a business target. KPIs and user
journeys did too
([From Marketing to Analytics Engineering at 7:18-23:12 and 38:27-41:50](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html),
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})).

[Alicja Notowska](https://datatalks.club/people/alicjanotowska.html) gives the
hiring-screen version in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html).
At 21:32-32:40, she describes sourcing from the job description, checking
responsibilities instead of titles alone, and reading beyond tool lists and
buzzwords. For this comparison, that means a data analyst CV should show the
questions, decisions, and stakeholders behind the analysis. An analytics
engineer CV should show the models, tests, docs, and ownership behind the
tools.

[Tereza Iofciu](https://datatalks.club/people/terezaiofciu.html) adds the job-ad
side in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html).
At 27:18-30:44, she recommends checking whether the team is described,
responsibilities are well-defined, and objectives appear instead of a long
technology checklist. A posting for either role should name the work. If it
asks for every data tool without saying whether the person owns decisions or
models, the title is weak evidence. Quality ownership and stakeholder ownership
should be visible too.

The overlap matters because analysts who understand modeling can avoid bad
joins and mixed grains. Analytics engineers who understand stakeholder
questions can model the right entities instead of only making tidy tables.
Victoria's
[analytics engineering role comparison](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
and Juan's
[analytics engineering foundations discussion](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)
both make that boundary practical. The title matters less than who owns the
question, who owns the reusable model, and who owns the quality path.

## Related Pages

These role definitions, adjacent workflows, and learning paths go deeper:

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Roles Guide]({{ '/wiki/data-roles/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Product Analyst article]({{ '/wiki/product-analyst/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})

