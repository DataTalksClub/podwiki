---
layout: article
tags: ["comparison"]
title: "Data Analyst vs Analytics Engineer"
seo_title: "Analyst vs Analytics Engineer"
keyword: "data analyst vs analytics engineer"
secondary_keywords:
  - analytics engineer vs data analyst
  - data analyst and analytics engineer
summary: "A role comparison for deciding whether a team needs analyst ownership, analytics engineering ownership, or both."
related_wiki:
  - Data Analyst Role
  - Data Analyst Careers
  - Data Analyst to Analytics Engineer
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Analytics Engineering Portfolio Projects
  - Product Analytics
  - Metrics
  - dbt
  - Data Quality and Observability
  - Event Tracking
  - Tracking Plans
  - Data Products
  - Data-Led Growth
  - Modern Data Stack
  - Dashboard and Metric Layer Project Checklist
---

Data analysts and analytics engineers both work near SQL, dashboards, metrics,
and business questions. They don't own the same risk. A data analyst usually
owns the path from question to decision. An analytics engineer usually owns the
path from repeated analytical logic to a trusted model other people can reuse.

Analyst work centers KPI definition, dashboards, problem sizing, and experiment
evaluation [[cite:data-team-roles=>Data Team Roles Explained]].
The analyst-versus-engineer boundary is about decision ownership versus modeled
data ownership.

Analytics engineering centers reusable models, pipelines, and data quality, and
[[Analytics Engineering]] covers the broader practice
[[cite:analytics-engineer-skills-tools@06:49=>Master Analytics Engineering]].

The two role hubs are
[[Data Analyst Role]] and
[[Analytics Engineering]].
Movement from analyst work toward model ownership belongs to the
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
transition path.
[[Data Analyst Careers]] covers entry routes and broad career options before
that transition.

## Decision Surface

Use a data analyst when the missing owner has to answer a question, interpret a
metric, and help stakeholders decide what to do next. That person may write SQL
and build dashboards, but the main output is a recommendation, readout, or
business explanation. Grigorev and Maksimovic both tie analyst work to business
questions, metrics, dashboards, and decisions
[[cite:data-team-roles=>Data Team Roles]]
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's role transition discussion]].

Use an analytics engineer when the missing owner has to make analytical data
reusable and safer to change. The role became useful where analysts were
spending too much time cleaning, quality-checking, and modeling data before
analysis. Perez Mola and Perafan connect the engineering side to reusable
models, quality checks, and reproducible analytical data
[[cite:analytics-engineer-skills-tools@16:54=>Perez Mola]]
[[cite:analytics-engineer-skills-tools=>Perez Mola]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan]].

The practical split is:

- Data analyst: KPIs, ad hoc analysis, dashboards, and metric movement.
  Analysts also own experiment readouts, segment analysis, stakeholder
  explanation, and recommendations.
- Analytics engineer: table grain and source-to-mart transformations.
  Analytics engineers also own `dbt` models with tests and docs, semantic
  definitions, data quality checks, and BI-ready datasets
  [[cite:analytics-engineer-skills-tools@14:34=>Perez Mola]].
- Shared surface: SQL, business context, metric definitions, dashboard trust,
  event semantics, source-data debugging, and funnel or experiment data.

Grigorev frames the analyst side around KPIs, dashboards, and product decisions.
Perez Mola and Perafan frame the analytics-engineering side around modeled,
tested, reusable data
[[cite:data-team-roles=>Data Team Roles]]
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].

Compare the roles by asking who owns the decision and who owns the reusable
analytical data.

## Data Analyst Fit

Choose a data analyst when the team has to understand what happened, why it
changed, and what decision should follow. In
[[cite:data-team-roles=>Data Team Roles]],
the analyst tracks business metrics such as profit, listings, and buyer-seller
contacts. The analyst builds executive reports, uses SQL and dashboards, and
helps quantify whether a product problem deserves team time. [[Data Analyst
Role]] owns the broader role definition. Here, the boundary question is whether
the work should stay with an analyst or move into modeled data ownership.

Analysts usually own metric interpretation and the recommendation that follows.
They decide how to size the question and which KPI answers it. They also choose
the segment or cohort that matters and explain caveats to a stakeholder.
Grigorev's analyst example includes KPI definition and executive reporting. It
also includes product problem sizing and post-launch experiment evaluation
([[cite:data-team-roles=>Data Team Roles]],
[[Data Analyst Careers]]).

Experiment evaluation can still be analyst-owned. The analyst checks whether a
model-backed product change reduces posting-flow drop-off or wrong-category
listings [[cite:data-team-roles=>Data Team Roles]]. That makes
[[a-b-testing=>A/B Testing]] and
[[Experimentation]] analyst-facing skills, while reusable exposure tables,
metric definitions, and dashboard models can move to analytics engineering.

This comparison answers whether the work is still analysis or has become
reusable analytics-engineering work.

The analyst should still understand where numbers come from.
[[person:arpitchoudhury=>Arpit Choudhury]] explains why
teams need documented events and properties
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's event tracking discussion]].
Without that source context, analysts can misread funnels, activation workflows,
or signup spikes. The same source awareness connects the analyst role to
[[Event Tracking]] and [[Tracking Plans]].

## Analytics Engineer Fit

Choose an analytics engineer when repeated analytical logic has become a team
dependency. That isn't a one-off chart. It's maintained data modeling behind
dashboards, forecasts, experiments, and activation flows.

Use the distinction to assign ownership. Analysts can move quickly when a
stakeholder needs an answer today. Analytics engineers should take over when
many future analyses would otherwise copy the same joins, filters, or metric
logic. Perez Mola ties that work to tables, views, and Looker exposure. She also
ties it to failure handling and reusable data for analytical users
([[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]).

Canonical metrics make the boundary clear. Analysts can define a KPI for a
decision and explain the movement. Analytics engineers should encode the
reusable definition when a metric appears across many dashboards. Revenue and
retention can create that pressure. Active users, sessions, and listings can do
the same.

Perafan's modeling discussion asks whether tables and columns match the business
concepts stakeholders use. Perez Mola puts data modeling and quality checks
behind the BI surface
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's modeling discussion]],
[[cite:analytics-engineer-skills-tools=>Perez Mola's role discussion]],
[[Data Products]]).

[[dbt]] provides tool-level context, and [[Analytics Engineering]] covers the
broader role definition.

## Title Blur

The title split depends on company size. In
[[cite:analytics-engineer-skills-tools=>Perez Mola's comparison of analytics engineers, analysts, and data engineers]],
the analytics engineer sits between data analyst and data engineer. The lines
are blurry across companies and even within one team.
The Spotify-origin story makes the boundary practical. Analysts needed to spend
less time cleaning and preparing data, while data engineers stayed closer to
infrastructure and pipelines
[[cite:analytics-engineer-skills-tools@16:54=>Perez Mola's role-origin discussion]].

Analysts bring business knowledge and SQL that answers stakeholder questions.
Data engineers bring software practices, infrastructure ownership, and pipeline
concerns. Analytics engineers bring those worlds together around modeled,
curated data.
Perez Mola presents the role as a bridge because analysts should spend less
time cleaning and modeling data. Data engineers often prefer infrastructure
work over business-specific models
([[cite:analytics-engineer-skills-tools=>Perez Mola's role comparison]]).

Nikola Maksimovic's small analytics engineering and BI team shows the same blur
from inside the job. His role combined KPI reassessment, dashboards, and
product-team support. It also included A/B testing and ad hoc analysis. RFM
analysis, data model changes, and a later `dbt` migration were part of the same
role. Small and medium-sized teams shouldn't get stuck on the title split.
Larger data
departments can separate analysts and analytics engineers so people can
focus.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch@25:17=>Maksimovic's team story]][[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch@26:45=>Maksimovic's title discussion]]

Perafan agrees that the role sits near the analyst-engineer gap. But he pushes
against defining analytics engineering only by what analysts and data engineers
don't do. For him, analytics engineers add rigor, testability, and
reproducibility to analytical modeling
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's analytics engineering foundations discussion]]).

[[person:arpitchoudhury=>Arpit Choudhury]] gives a
growth-stack version of the split. Early companies may have one data person,
while larger teams split the work among data engineers, analysts, and analytics
engineers. Product operations, DataOps, and self-service users sit around the
same split
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's data-led growth team structure discussion]],
[[data-led-growth=>Data-Led Growth]]).

Use work mode instead of title when one person covers both sides:

- Stay in analyst mode for a one-off question, an experiment readout, a metric
  explanation, or a stakeholder recommendation.
- Move into analytics-engineering mode when copied SQL, inconsistent filters,
  slow joins, unclear table grain, or repeated metric disputes keep returning.
- Split the role when the same person can't both answer urgent questions and
  maintain the modeled analytical layer.

After the role boundary is clear, the career path depends on skill order,
projects, and job targets. [[data-analyst-to-analytics-engineer=>Data Analyst to
Analytics Engineer]] covers that analyst-to-analytics-engineer move.

## Dashboards, Metrics, and Models

Dashboards don't decide the role boundary by themselves. A data analyst can
own a dashboard when it's a stakeholder view, an exploratory readout, or a
communication surface. The analyst owns chart choices, caveats, and the
business recommendation.

An analytics engineer should own the reusable layer behind the dashboard when
the dashboard depends on shared logic. Victoria ties that layer to docs, tests,
version control, and a dependency graph
[[cite:analytics-engineer-skills-tools=>Perez Mola's dbt modeling and documentation discussion]].
Juan asks what each row represents and how the business domain should fit into
tables
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's business-domain modeling discussion]].
Those are analytics-engineering questions because the answer affects many
future analyses.

Metrics follow the same rule. Analysts can define a KPI for a decision and
explain movement to a product manager or executive. Analytics engineers should
encode the canonical definition when many teams reuse the metric. They should
also encode grain, filters, and time windows. Exclusions and source assumptions
belong in the same modeled definition.

Analyst SQL becomes analytics engineering work after it becomes documented and
tested transformations. Perez Mola ties that shift to SQL files and YAML
documentation. She also ties it to GitHub version control, tests, and a DAG
([[cite:analytics-engineer-skills-tools=>Perez Mola's SQL workflow discussion]]).

Maksimovic's team shows the same boundary in practice. For that team, KPI and
dashboard work came before the `dbt` migration. Looker reporting and the shared
transformation layer came later
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's dbt migration discussion]],
[[Dashboard and Metric Layer Project Checklist]]).

[[Metrics]] and
[[Data Products]] cover the broader metric topic.

## Product and Growth Data

Product and growth data create shared surfaces, but this comparison still has
one boundary. Analysts interpret funnels, cohorts, retention, and experiment
results. Analytics engineers make the repeated event logic, assignment logic,
and modeled tables safe to reuse.

Arpit's data-led growth episode starts with a tracking plan. Engineers then
instrument events before data flows into analytics tools and warehouses
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's event tracking and warehouse flow discussion]]).
Teams store and transform structured data in the warehouse before analyzing it
in BI. Choudhury also connects modeled data to reverse ETL. Sales and marketing
systems, advertising platforms, support tools, and product tools consume the
same definitions
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's warehouse and reverse ETL discussion]].

In that flow, analysts own interpretation and decisions. Analytics engineers
own modeled data that can survive reuse in BI and activation. The broader
adoption surface belongs to [[data-led-growth=>Data-Led Growth]],
[[Data Activation]], and [[Data Product Adoption]].

A team can switch modes inside one project because a one-off funnel readout can
stay analyst-owned. Reusable funnel logic belongs with analytics engineering
when dashboards and experiment analysis depend on it. Reverse ETL audiences and
executive reporting create the same pressure
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's activation and reverse ETL discussion]],
[[Modern Data Stack]]).

## Assignment Signals

Assign the work before titles harden into team structure. Give a data analyst
the work when the missing owner must choose the metric, interpret movement,
explain caveats, and recommend a decision. Grigorev's role definition ties
analyst work to SQL and dashboards. It also ties the role to reports,
recommendations, problem sizing, and A/B-test interpretation.[[cite:data-team-roles=>Data Team Roles]]

Give an analytics engineer the work when the missing owner must make analytical
data easier to reuse and safer to change. Look for modeled tables and
documented grain. Also look for tests, version control, and quality checks
instead of tool familiarity.
Perez Mola names data modeling and SQL transformations. Perafan adds
robustness and testability as the role boundary.[[cite:analytics-engineer-skills-tools@42:05=>Perez Mola's analytics engineering skill discussion]][[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's analytics engineering foundations discussion]]

Titles and job ads still need responsibility checks. Notowska describes checking
job descriptions, responsibilities, and concrete work rather than buzzwords.
Iofciu recommends job ads that name the team and its responsibilities. The
objectives should be visible too.[[cite:hiring-data-scientists-and-analysts=>Notowska's hiring-screen discussion]][[cite:data-science-job-red-flags-and-mismatched-roles=>Iofciu's job-ad mismatch discussion]]
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
covers the career move after this responsibility check.

## Related Pages

These role definitions, adjacent workflows, and learning paths go deeper:

- [[Data Analyst Role]]
- [[Data Analyst Careers]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
- [[Analytics Engineering]]
- [[data-roles=>Data Roles Guide]]
- [[Analytics Engineering Roadmap]]
- [[analytics-engineering-portfolio-projects=>Analytics Engineer Portfolio]]
- [[Product Analytics]]
- [[Metrics]]
- [[dbt]]
- [[Modern Data Stack]]
- [[Data Quality and Observability]]
- [[Data Products]]
- [[data-led-growth=>Data-Led Growth]]
- [[Event Tracking]]
- [[Tracking Plans]]
- [[Dashboard and Metric Layer Project Checklist]]
