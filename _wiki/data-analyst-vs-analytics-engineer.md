---
layout: article
tags: ["comparison"]
title: "Analyst vs Analytics Engineer"
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
[[podcast:data-team-roles=>Data Team Roles Explained]]
for analyst work around KPIs and dashboards, problem sizing, and experiment
evaluation [[cite:data-team-roles=>Data Team Roles]].

Then compare it with
[[person:victoriaperezmola=>Victoria Perez Mola]] in
[[podcast:analytics-engineer-skills-tools=>Master Analytics Engineering]].
She describes data modeling, pipelines, and data quality. Looker and `dbt` also
sit in that work. Tests, documentation, and dependency graphs come with it
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].

For the two role hubs, use
[[Data Analyst Role]] and
[[Analytics Engineering]].
If you're moving from analyst work toward model ownership, use the
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]].

## Short Comparison

Use a data analyst when the missing owner has to answer a question, interpret a
metric, and help stakeholders decide what to do next. That person may write SQL
and build dashboards, but the main output is a recommendation, readout, or
business explanation. Grigorev and Maksimovic both tie analyst work to business
questions, metrics, dashboards, and decisions
[[cite:data-team-roles=>Data Team Roles]]
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's role transition discussion]].

Use an analytics engineer when the missing owner has to make analytical data
reusable and safer to change. That person may support BI and product analytics.
Analytics engineers turn repeated business logic into tested models and
documented metrics. They also build transformation layers and BI-ready marts.

The role became useful where analysts were spending too much time cleaning,
quality-checking, and modeling data before analysis. That left less time for
interpreting the business question
[[cite:analytics-engineer-skills-tools@16:54=>Perez Mola]].

Perez Mola and Perafan connect that work to modeling with quality checks and
reproducible analytical data
[[cite:analytics-engineer-skills-tools=>Perez Mola]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan]].

The practical split is:

- Data analyst: KPIs, ad hoc analysis, dashboards, and metric movement.
  Analysts also own experiment readouts, segment analysis, stakeholder
  explanation, and recommendations.
- Analytics engineer: table grain and source-to-mart transformations.
  Analytics engineers also own `dbt` models with tests and docs, semantic
  definitions, data quality checks, and BI-ready datasets.
- Shared surface: SQL, business context, metric definitions, product analytics,
  dashboard trust, event semantics, and source-data debugging.

Grigorev frames the analyst side around KPIs, dashboards, and product decisions.
Perez Mola and Perafan frame the analytics-engineering side around modeled,
tested, reusable data
[[cite:data-team-roles=>Data Team Roles]]
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].

Because the boundary sits inside the same stack, the adjacent concepts matter:

- [[Product Analytics]]
- [[Metrics]]
- [[dbt]]
- [[Data Quality and Observability]]

## Data Analyst Fit

Choose a data analyst when the team has to understand what happened and what
decision should follow. In
[[cite:data-team-roles=>Data Team Roles]],
the analyst tracks business metrics such as profit, listings, and buyer-seller
contacts. The analyst builds executive reports, uses SQL and dashboards, and
helps quantify whether a product problem deserves team time.

Analyst work also includes experiment evaluation: the analyst checks whether a
model-backed product change reduces posting-flow drop-off or wrong-category
listings [[cite:data-team-roles=>Data Team Roles]]. That makes
[[a-b-testing=>A/B Testing]] and
[[Experimentation]] analyst-facing
skills, not only data-science skills.

Analysts usually own metric interpretation and the recommendation that follows.
They decide how to size the question and which KPI answers it. They also decide
which segment or cohort matters and how to explain the caveats to a stakeholder.
Grigorev's analyst example includes KPI definition and executive reporting. It
also includes product problem sizing and post-launch experiment evaluation
([[cite:data-team-roles=>Data Team Roles]],
[[Data Analyst Careers]]).

For product-facing work, the analyst often owns the question and the
interpretation. [[person:nikolamaksimovic=>Nikola Maksimovic]] describes work
with product managers on experiments and new features. The same work
includes A/B testing, cohort sizing, and RFM analysis. Dashboards and
presentations of insights sit in the same analyst mode, even when the title
includes analytics engineering
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's product analytics discussion]].

The analyst should still understand where numbers come from.
[[person:arpitchoudhury=>Arpit Choudhury]] explains why
teams need documented events and properties
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's event tracking discussion]].
Without that source context, people can't trust funnels, activation workflows,
or signup spikes.

Analysts and product managers see unexpected registration spikes. They need
event origins to trace those spikes
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's registration-spike example]].
The same source-awareness connects the analyst role to
[[Event Tracking]] and
[[Tracking Plans]].

## Analytics Engineer Fit

Choose an analytics engineer when repeated analytical logic has become a team
dependency. Victoria says analytics engineers build tables or views and clean
data. They expose data to Looker, handle failures, and make data available to
analysts and data scientists
([[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]).
That isn't a one-off chart. It's maintained data modeling.

`dbt` matters because it changes how teams operate SQL work. Victoria explains
SQL files, YAML docs, and GitHub version control. She also covers non-null and
unique tests, dependency graphs, and scheduled runs. Those practices turn
warehouse SQL into something closer to production code
[[cite:analytics-engineer-skills-tools=>Perez Mola's dbt workflow discussion]].
Use the [[dbt]] page for the tool-level context.

[[person:juanmanuelperafan=>Juan Manuel Perafan]] gives
the deeper role definition.
He says the role is often misread as only bridging analysts and data engineers.
His stronger definition says analytics engineers take business reality and make
data resemble it. He then adds rigor, robustness, and reproducibility. He also
contrasts fast dashboard work with engineering work that puts testability first
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's role-boundary discussion]].

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
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's modeling discussion]]).
Perez Mola's role discussion puts data modeling and quality checks behind the
BI surface
([[cite:analytics-engineer-skills-tools=>Perez Mola's role discussion]],
[[Data Products]]).

## Boundary Blurs

The title split depends on company size. In
[[cite:analytics-engineer-skills-tools=>Perez Mola's comparison of analytics engineers, analysts, and data engineers]],
the analytics engineer sits between data analyst and data engineer. She says
the lines are blurry across companies and even within one team.
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

Nikola's
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>small analytics engineering and BI team story]]
shows the same blur from inside the job. He says he worked as both an analytics
engineer and a data analyst on a four-person team. His work included KPI
reassessment, dashboards, product-team support, and A/B testing. It also
included ad hoc analysis, RFM analysis, and data model changes. Later, he
describes the `dbt` migration and transformation layers that turned that work
into a reusable model.

Nikola returns to the title question in
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's title discussion]].
His official role combined analytics engineer and data analyst because the BI
team was small. He says small and medium-sized teams shouldn't get stuck on the
title split. The work still needs analytical skill, KPI fluency, and domain
modeling. In a larger data department, though, separating analysts and
analytics engineers can make structural sense because people can focus.

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

The [[Analytics Engineering Roadmap]]
and
[[Analytics Engineering Portfolio Projects]]
pages are useful when an analyst wants to move toward the engineered side of
the boundary. For a step-by-step transition path, use
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]].

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

For the broader metric topic, use
[[Metrics]] and
[[Data Products]].

## Product and Growth Data

Product analytics shows why analysts and analytics engineers need each other.
An analyst can interpret funnels, cohorts, retention, and experiment results.
The same analyst needs event meaning, assignment logic, and trusted modeled
tables before the interpretation is defensible.

Arpit's data-led growth episode traces the full flow. Teams start with a
tracking plan, engineers instrument events, and the data flows into
analytics tools and warehouses
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's event tracking and warehouse flow discussion]]).
He describes the warehouse as the place where teams store and transform
structured data. Teams also clean and model that data before analyzing it in BI
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's warehouse discussion]].

He adds reverse ETL and operational analytics. Teams can then move modeled data
into sales and marketing tools. The same modeled data can also reach
advertising, support, or product tools
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's reverse ETL discussion]].

In that flow, analysts own interpretation and decisions. Analytics engineers
own modeled data that can survive reuse in BI and activation. Data engineers
and product engineers still matter because events need instrumentation,
warehouses need pipelines, and downstream tools need reliable delivery. Use
[[data-led-growth=>Data-Led Growth]],
[[Data Activation]], and
[[Data Product Adoption]]
for the broader adoption surface.

The same project can switch modes because a one-off funnel readout can stay
analyst-owned. Reusable funnel logic belongs with analytics engineering when
dashboards and experiment analysis depend on it. Reverse ETL audiences and
executive reporting create the same pressure
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Choudhury's activation and reverse ETL discussion]],
[[Modern Data Stack]]).

## Hiring and Portfolio Signals

For a data analyst, look for proof that the person can move from a question to
a decision. Grigorev's role definition names SQL and Python or R. It also names
dashboard tools, basic statistics, reports, and recommendations.
Problem sizing and A/B test interpretation also matter
([[cite:data-team-roles=>Data Team Roles]],
[[Data Analyst Careers]]).

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
([[cite:analytics-engineer-skills-tools=>Perez Mola's analytics engineering skill discussion]],
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Perafan's analytics engineering foundations discussion]],
[[Analytics Engineering Portfolio Projects]]).

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
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Maksimovic's marketing-to-analytics engineering path]],
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]).

[[person:alicjanotowska=>Alicja Notowska]] gives the
hiring-screen version.
She describes sourcing from the job description, checking responsibilities
instead of titles alone, and reading beyond tool lists and buzzwords
[[cite:hiring-data-scientists-and-analysts=>Notowska's hiring-screen discussion]].
For this comparison, that means a data analyst CV should show the questions,
decisions, and stakeholders behind the analysis. An analytics engineer CV
should show the models, tests, docs, and ownership behind the tools.

[[person:terezaiofciu=>Tereza Iofciu]] adds the job-ad
side.
She recommends checking whether the team is described, responsibilities are
well-defined, and objectives appear instead of a long technology checklist
[[cite:data-science-job-red-flags-and-mismatched-roles=>Iofciu's job-ad mismatch discussion]].
A posting for either role should name the work. If it asks for every data tool
without saying whether the person owns decisions or models, the title is weak
evidence. Quality ownership and stakeholder ownership should be visible too.

The overlap matters because analysts who understand modeling can avoid bad
joins and mixed grains. Analytics engineers who understand stakeholder
questions can model the right entities instead of only making tidy tables.
Victoria's
[[cite:analytics-engineer-skills-tools=>analytics engineering role comparison]]
and Juan's
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>analytics engineering foundations discussion]]
both make that boundary practical. The title matters less than who owns the
question, who owns the reusable model, and who owns the quality path.

## Related Pages

These role definitions, adjacent workflows, and learning paths go deeper:

- [[Data Analyst Role]]
- [[Data Analyst Careers]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
- [[Analytics Engineering]]
- [[data-roles=>Data Roles Guide]]
- [[Analytics Engineering Roadmap]]
- [[Analytics Engineering Portfolio Projects]]
- [[product-analyst=>Product Analyst article]]
- [[Product Analytics]]
- [[Metrics]]
- [[dbt]]
- [[Modern Data Stack]]
- [[Data Quality and Observability]]
- [[Data Products]]
