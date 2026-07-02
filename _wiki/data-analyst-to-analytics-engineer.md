---
layout: article
tags: [transition, "roadmap"]
title: "Data Analyst to Analytics Engineer Roadmap"
keyword: "data analyst to analytics engineer"
summary: "A podcast-backed roadmap for analysts moving into analytics engineering through SQL modeling, dbt-style workflows, metric ownership, tests, documentation, and portfolio evidence."
search_intent: "People searching for data analyst to analytics engineer usually want a practical transition path: which analyst skills transfer, what modeling and dbt skills to add, and what project evidence proves readiness."
related_wiki:
  - Data Analyst Role
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Analytics Engineering Portfolio Projects
  - dbt
  - Metrics
  - Data Products
  - Product Analytics
  - Data Quality and Observability
  - Event Tracking
  - Tracking Plans
  - Business Intelligence
---

Moving from data analyst to analytics engineer means moving upstream from
analysis into reusable analytical data. The analyst skill set still matters.
SQL and dashboard work transfer. KPI explanations and stakeholder context
become stronger when the analyst turns repeated logic into tested models.
Experiment readouts can move the same way.

Those analyst skills become more valuable when they're backed by reusable
models.

[[person:juanpablo|Juan Pablo]] gives the clearest
analyst-to-analytics path in
[[podcast:from-math-graduate-to-data-analytics|How to Break into Data Analytics]].
He moved from teaching mathematics into analytics roles, then worked at Amazon
in a BI and data engineering team. His episode connects the transition to SQL,
portfolio proof, networking, and communication. It also clarifies the boundary
between analyst, BI engineer, and analytics engineer
([[podcast:from-math-graduate-to-data-analytics|0:02-3:17]]).

The practical boundary is ownership. A
[[data-analyst-role|data analyst]] usually owns the
question, interpretation, dashboard, and recommendation. An
[[analytics-engineering|analytics engineer]] owns
the reusable model layer that makes those answers safer to repeat. The role
boundary is covered in
[[Data Analyst vs Analytics Engineer]].

The broader skill sequence lives in
[[Analytics Engineering Roadmap]].
For the wider role map, compare
[[Data Analysis]] and
[[Data Roles]].

## Move From Answering Questions to Owning Reusable Data

Guests describe this transition as taking analyst work that used to live
inside one query or dashboard and making it reusable. The analyst already knows
the business question. The new work is to define grain, model entities, add
tests, and document metric logic. Other people can then trust and reuse the
model. That puts the transition between the
[[data analyst role]],
[[analytics engineering]],
and BI-facing [[data products]].

In [[podcast:data-team-roles|Data Team Roles Explained]],
the analyst role sits close to company data, KPIs, and dashboards. Reports and
product evaluation belong there too. Analysts size product problems and
evaluate whether a shipped change improved behavior
([[podcast:data-team-roles|7:51-10:39]]).
That context transfers directly into
[[metrics]],
[[product analytics]], and
[[a-b-testing|A/B testing]].

[[person:victoriaperezmola|Victoria Perez Mola]] gives
the analytics-engineering standard in
[[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]].
She describes modeling data for analysts and data scientists, maintaining
pipelines, and checking quality. She also builds Looker-facing models. Her dbt
workflow includes SQL files, YAML docs, GitHub version control, and tests. The
DAG makes model dependencies visible
([[podcast:analytics-engineer-skills-tools|4:05-10:04]]).

[[person:juanmanuelperafan|Juan Manuel Perafan]] adds
the conceptual boundary in
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]].
He frames analytics engineering as turning business reality into data models,
then applying software-engineering habits so the work becomes reproducible and
robust
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|7:56-18:35]]).

## Choose the Right Transition Target

Rather than aiming for "more technical analyst work" in general, aim for a
specific ownership change. Keep analyst judgment over questions, metrics, and
stakeholders, then add responsibility for the reusable models behind those
answers.

Choose the target from the work you already do:

- If the current work is mostly dashboard interpretation, start with the
  [[data analyst role]] and the
  [[Data Analyst vs Analytics Engineer]]
  boundary.
- If the current work already includes shared SQL, Looker, dbt, or metric
  cleanup, use the
  [[analytics engineering roadmap]]
  as the skills map.
- If the current work comes from campaign reporting or funnel analysis, the
  [[marketing-to-analytics-engineering|marketing-to-analytics-engineering]]
  path is the closest archive example.

[[person:nikolamaksimovic|Nikola Maksimovic]] shows
why this choice matters in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]].
Her work moved through marketing reporting and BI-team collaboration. She then
added SQL and Looker. Later work included a dbt migration, product analytics,
and A/B testing. The title mattered less than the growing ownership of modeled
tables, dashboard definitions, and product metrics
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|7:18-28:40 and 38:27-41:50]]).

## Analyst Skills That Transfer

The strongest transferable skill isn't tool familiarity alone. Analysts know
which definitions confuse stakeholders, which dashboard filters get reused, and
which metric caveats change a decision. That's the domain context an
analytics engineer needs before modeling a trusted table.

Juan Pablo's path started with statistics and hypothesis testing, then moved
through SAS, R, and portfolio work. He later realized SQL was the core skill he
used most often
([[podcast:from-math-graduate-to-data-analytics|9:14-10:16]]).
His bootcamp gave him a practical map of SQL, Tableau, Power BI, and
dashboards. It also showed missing skills, but it didn't give him a job. The job
search took nine months, so the transition needed both skills and visibility
([[podcast:from-math-graduate-to-data-analytics|12:06-13:52]]).

[[marketing-to-analytics-engineering|Maksimovic's marketing-to-analytics-engineering transition]]
shows the same transfer from another business role. She used business and BI
experience to move toward analytics engineering. Her work expanded into product
support and [[a-b-testing|A/B testing]]. Data
modeling, a dbt migration, Looker, and LookML became part of the path
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|8:45-23:12]]).

Those examples show the same rule: keep the analyst context, but move the
logic upstream. A dashboard query becomes a model. A repeated KPI becomes a
tested metric definition. A stakeholder explanation becomes reusable
documentation.

## Add Modeling, dbt, and Review

The missing skill is model ownership. Analyst SQL can answer one question, but
analytics-engineering SQL has to survive reuse. Start by taking a dashboard
query and splitting it into staging, intermediate, and mart layers. Define the
grain and primary key before adding tests. Then document the joins and accepted
assumptions.

Perez Mola names SQL, fact tables, and dimension tables as core preparation.
Kimball-style modeling and Snowflake familiarity also matter
([[podcast:analytics-engineer-skills-tools|26:10-29:15]]).
She also shows why [[dbt]] matters. It makes
SQL transformations reviewable, documented, testable, and visible as lineage.
The tool is useful because it packages engineering habits around analytical
models
([[podcast:analytics-engineer-skills-tools|6:49-10:04]]).

Perafan raises the review bar. Generic tests and singular SQL tests stop broken
assumptions before they reach users. Unit tests and CI checks belong in that
workflow too
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|38:41-46:34]]).
That links the transition to
[[data quality and observability]]
and [[DataOps]], not only to dashboards.

Learn enough of the [[modern data stack]]
to know where your models sit.
[[person:nataliekwong|Natalie Kwong]] explains in
[[podcast:data-engineering-tools-modern-data-stack|ETL, ELT, and the Modern Data Stack]]
that ELT loads raw data first. Analysts and analytics engineers then transform
it in the warehouse with SQL and dbt-style workflows
([[podcast:data-engineering-tools-modern-data-stack|7:57-15:30]]).

## Build Product and Event Context

Analytics engineering gets more valuable when the modeled data supports product
decisions. Analysts already see funnels, cohorts, and experiment readouts. The
transition adds ownership of the event and metric models behind those analyses.

[[person:arpitchoudhury|Arpit Choudhury]] connects
tracking plans and event properties to warehouse transformations in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]].
BI and activation depend on the same event semantics.
He treats event ownership as a system that starts before analysis and continues
into downstream growth tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|13:34-30:03]]).

[[Event tracking]] and
[[tracking plans]] matter when the
roadmap involves user behavior.
[[Product Analytics]] sits next
to that work. A good analytics-engineering transition project doesn't only show
a funnel chart. It shows the event grain, identity rules, metric definition,
and tests.

It also shows the dashboard or activation surface. When a team maintains that
modeled output for analysts, product managers, or growth tools, it becomes a
small [[data-products|data product]] rather than a
one-off analysis.

## Prove the Transition With Portfolio Work

Portfolio evidence should show the move from one-off analysis to reusable data
work. Juan Pablo's first portfolio used R projects for data wrangling,
exploratory analysis, and visualizations. Maps, heat maps, and basic models
were part of the same portfolio
([[podcast:from-math-graduate-to-data-analytics|24:23-25:37]]).
For entry-level roles, he says three projects are enough, and any public
portfolio is better than waiting for a perfect one
([[podcast:from-math-graduate-to-data-analytics|26:39-27:59]]).

For analytics engineering, the strongest project starts with analyst work and
turns it into a trusted model layer.

Good project choices include:

- a dashboard query refactored into dbt-style staging, intermediate, and mart
  models
- a governed metric definition with grain, tests, documentation, and a dashboard
- a funnel, retention, or [[a-b-testing|A/B testing]]
  mart built from event data and a tracking plan
- a data quality improvement that explains user impact and the test that catches
  the failure
- a small semantic layer or [[data-products|data product]]
  for one stakeholder decision

[[person:christopherbergh|Christopher Bergh]] grounds
the reliability side in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
His operating system includes version control, automated tests, CI/CD, and
runbooks. It also includes documentation and end-to-end versioning
([[podcast:dataops-automation-and-reliable-data-pipelines|33:47-38:01 and 43:06-51:21]]).

[[person:gloriaquiceno|Gloria Quiceno]] adds the
transition-project standard in
[[podcast:get-data-analytics-and-data-engineering-job|Get a Data Analytics and Data Engineering Job]].
She recommends a custom capstone and data quality thinking. A custom project
stands out more than a repeated course project when it explains why the data
and checks matter
([[podcast:get-data-analytics-and-data-engineering-job|50:15-53:34]]).

The scope should match
[[Analytics Engineering Portfolio Projects]]
and the
[[Dashboard and Metric Layer Project Checklist]].
Juan Pablo's portfolio advice is direct: make the project easy to look at.
GitHub and GitHub Pages can work. RPubs, WordPress, and Hashnode can work too
as long as the project has a clear description and README
([[podcast:from-math-graduate-to-data-analytics|47:16-48:52]]).

## Get the First Role

The first target role doesn't have to use the exact title "analytics engineer."
Juan Pablo's Amazon team consumed upstream data and ingested it. The team built
pipelines, added business logic, and created dashboards for troubleshooting
consultants.
Amazon called that work Business Intelligence Engineer, while other companies
call similar work Analytics Engineer
([[podcast:from-math-graduate-to-data-analytics|52:51-53:41]]).

He also separates analyst work from analytics-engineering work through his
first job. The title was data scientist, but the work was mostly SQL and
dashboards. Because he wasn't building pipelines, he describes it as data
analyst or data analyst consultant work
([[podcast:from-math-graduate-to-data-analytics|54:08-54:29]]).

That supports a pragmatic job search. Look for analytics engineer, BI engineer,
or data analyst roles with dbt ownership. Product analytics engineer and data
modeler roles can fit the same path.

Visibility matters when the candidate lacks the exact title. Juan Pablo's first
offer came through repeated meetup attendance and a resume that reached the
hiring founder twice
([[podcast:from-math-graduate-to-data-analytics|16:12-17:51]]).
He also recommends active LinkedIn use and an obvious portfolio link. A resume
link should be ready to send. Short-term roles, nonprofit projects, and
small-company trial work can create the first credible experience
([[podcast:from-math-graduate-to-data-analytics|20:17-23:47 and 32:35-40:39]]).

Communication is part of the hiring signal. At
[[podcast:from-math-graduate-to-data-analytics|59:59]],
Juan Pablo recommends concise project communication and STAR framing. At
[[podcast:from-math-graduate-to-data-analytics|1:01:06]],
he adds repo hygiene: a clean README and organized repository help reviewers
understand the work without reverse-engineering the code.

## Related Pages

These pages cover the adjacent roles, skills, and portfolio patterns.

- [[Data Analyst Role]]
- [[Data Analyst vs Analytics Engineer]]
- [[Analytics Engineering]]
- [[Analytics Engineering Roadmap]]
- [[Analytics Engineering Portfolio Projects]]
- [[Marketing to Analytics Engineering]]
- [[Data Analysis]]
- [[Data Roles]]
- [[dbt]]
- [[Metrics]]
- [[Product Analytics]]
- [[a-b-testing|A/B Testing]]
- [[Data Products]]
- [[Event Tracking]]
- [[Tracking Plans]]
- [[Business Intelligence]]
- [[Data Quality and Observability]]

