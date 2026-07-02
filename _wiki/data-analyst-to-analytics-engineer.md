---
layout: article
tags: ["roadmap"]
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

[Juan Pablo]({{ '/people/juanpablo/' | relative_url }}) gives the clearest
analyst-to-analytics path in
[How to Break into Data Analytics]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }}).
He moved from teaching mathematics into analytics roles, then worked at Amazon
in a BI and data engineering team. His episode connects the transition to SQL,
portfolio proof, networking, and communication. It also clarifies the boundary
between analyst, BI engineer, and analytics engineer
([0:02-3:17]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

The practical boundary is ownership. A
[data analyst]({{ '/wiki/data-analyst-role/' | relative_url }}) usually owns the
question, interpretation, dashboard, and recommendation. An
[analytics engineer]({{ '/wiki/analytics-engineering/' | relative_url }}) owns
the reusable model layer that makes those answers safer to repeat. The role
boundary is covered in
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}).

The broader skill sequence lives in
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).
For the wider role map, compare
[Data Analysis]({{ '/wiki/data-analysis/' | relative_url }}) and
[Data Roles]({{ '/wiki/data-roles/' | relative_url }}).

## Move From Answering Questions to Owning Reusable Data

Guests describe this transition as taking analyst work that used to live
inside one query or dashboard and making it reusable. The analyst already knows
the business question. The new work is to define grain, model entities, add
tests, and document metric logic. Other people can then trust and reuse the
model. That puts the transition between the
[data analyst role]({{ '/wiki/data-analyst-role/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
and BI-facing [data products]({{ '/wiki/data-products/' | relative_url }}).

In [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst role sits close to company data, KPIs, and dashboards. Reports and
product evaluation belong there too. Analysts size product problems and
evaluate whether a shipped change improved behavior
([7:51-10:39]({{ '/podcasts/data-team-roles/' | relative_url }})).
That context transfers directly into
[metrics]({{ '/wiki/metrics/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), and
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) gives
the analytics-engineering standard in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She describes modeling data for analysts and data scientists, maintaining
pipelines, and checking quality. She also builds Looker-facing models. Her dbt
workflow includes SQL files, YAML docs, GitHub version control, and tests. The
DAG makes model dependencies visible
([4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) adds
the conceptual boundary in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
He frames analytics engineering as turning business reality into data models,
then applying software-engineering habits so the work becomes reproducible and
robust
([7:56-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Choose the Right Transition Target

Rather than aiming for "more technical analyst work" in general, aim for a
specific ownership change. Keep analyst judgment over questions, metrics, and
stakeholders, then add responsibility for the reusable models behind those
answers.

Choose the target from the work you already do:

- If the current work is mostly dashboard interpretation, start with the
  [data analyst role]({{ '/wiki/data-analyst-role/' | relative_url }}) and the
  [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
  boundary.
- If the current work already includes shared SQL, Looker, dbt, or metric
  cleanup, use the
  [analytics engineering roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
  as the skills map.
- If the current work comes from campaign reporting or funnel analysis, the
  [marketing-to-analytics-engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
  path is the closest archive example.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows
why this choice matters in
[Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
Her work moved through marketing reporting and BI-team collaboration. She then
added SQL and Looker. Later work included a dbt migration, product analytics,
and A/B testing. The title mattered less than the growing ownership of modeled
tables, dashboard definitions, and product metrics
([7:18-28:40 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

## Analyst Skills That Transfer

The strongest transferable skill isn't tool familiarity alone. Analysts know
which definitions confuse stakeholders, which dashboard filters get reused, and
which metric caveats change a decision. That's the domain context an
analytics engineer needs before modeling a trusted table.

Juan Pablo's path started with statistics and hypothesis testing, then moved
through SAS, R, and portfolio work. He later realized SQL was the core skill he
used most often
([9:14-10:16]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).
His bootcamp gave him a practical map of SQL, Tableau, Power BI, and
dashboards. It also showed missing skills, but it didn't give him a job. The job
search took nine months, so the transition needed both skills and visibility
([12:06-13:52]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

[Maksimovic's marketing-to-analytics-engineering transition]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
shows the same transfer from another business role. She used business and BI
experience to move toward analytics engineering. Her work expanded into product
support and [A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}). Data
modeling, a dbt migration, Looker, and LookML became part of the path
([8:45-23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

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
([26:10-29:15]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
She also shows why [dbt]({{ '/wiki/dbt/' | relative_url }}) matters. It makes
SQL transformations reviewable, documented, testable, and visible as lineage.
The tool is useful because it packages engineering habits around analytical
models
([6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Perafan raises the review bar. Generic tests and singular SQL tests stop broken
assumptions before they reach users. Unit tests and CI checks belong in that
workflow too
([38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
That links the transition to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}), not only to dashboards.

Learn enough of the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
to know where your models sit.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains in
[ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
that ELT loads raw data first. Analysts and analytics engineers then transform
it in the warehouse with SQL and dbt-style workflows
([7:57-15:30]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Build Product and Event Context

Analytics engineering gets more valuable when the modeled data supports product
decisions. Analysts already see funnels, cohorts, and experiment readouts. The
transition adds ownership of the event and metric models behind those analyses.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) connects
tracking plans and event properties to warehouse transformations in
[Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
BI and activation depend on the same event semantics.
He treats event ownership as a system that starts before analysis and continues
into downstream growth tools
([13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

[Event tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}) matter when the
roadmap involves user behavior.
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) sits next
to that work. A good analytics-engineering transition project doesn't only show
a funnel chart. It shows the event grain, identity rules, metric definition,
and tests.

It also shows the dashboard or activation surface. When a team maintains that
modeled output for analysts, product managers, or growth tools, it becomes a
small [data product]({{ '/wiki/data-products/' | relative_url }}) rather than a
one-off analysis.

## Prove the Transition With Portfolio Work

Portfolio evidence should show the move from one-off analysis to reusable data
work. Juan Pablo's first portfolio used R projects for data wrangling,
exploratory analysis, and visualizations. Maps, heat maps, and basic models
were part of the same portfolio
([24:23-25:37]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).
For entry-level roles, he says three projects are enough, and any public
portfolio is better than waiting for a perfect one
([26:39-27:59]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

For analytics engineering, the strongest project starts with analyst work and
turns it into a trusted model layer.

Good project choices include:

- a dashboard query refactored into dbt-style staging, intermediate, and mart
  models
- a governed metric definition with grain, tests, documentation, and a dashboard
- a funnel, retention, or [A/B testing]({{ '/wiki/a-b-testing/' | relative_url }})
  mart built from event data and a tracking plan
- a data quality improvement that explains user impact and the test that catches
  the failure
- a small semantic layer or [data product]({{ '/wiki/data-products/' | relative_url }})
  for one stakeholder decision

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) grounds
the reliability side in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
His operating system includes version control, automated tests, CI/CD, and
runbooks. It also includes documentation and end-to-end versioning
([33:47-38:01 and 43:06-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

[Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }}) adds the
transition-project standard in
[Get a Data Analytics and Data Engineering Job]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}).
She recommends a custom capstone and data quality thinking. A custom project
stands out more than a repeated course project when it explains why the data
and checks matter
([50:15-53:34]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }})).

The scope should match
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
and the
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }}).
Juan Pablo's portfolio advice is direct: make the project easy to look at.
GitHub and GitHub Pages can work. RPubs, WordPress, and Hashnode can work too
as long as the project has a clear description and README
([47:16-48:52]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

## Get the First Role

The first target role doesn't have to use the exact title "analytics engineer."
Juan Pablo's Amazon team consumed upstream data and ingested it. The team built
pipelines, added business logic, and created dashboards for troubleshooting
consultants.
Amazon called that work Business Intelligence Engineer, while other companies
call similar work Analytics Engineer
([52:51-53:41]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

He also separates analyst work from analytics-engineering work through his
first job. The title was data scientist, but the work was mostly SQL and
dashboards. Because he wasn't building pipelines, he describes it as data
analyst or data analyst consultant work
([54:08-54:29]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

That supports a pragmatic job search. Look for analytics engineer, BI engineer,
or data analyst roles with dbt ownership. Product analytics engineer and data
modeler roles can fit the same path.

Visibility matters when the candidate lacks the exact title. Juan Pablo's first
offer came through repeated meetup attendance and a resume that reached the
hiring founder twice
([16:12-17:51]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).
He also recommends active LinkedIn use and an obvious portfolio link. A resume
link should be ready to send. Short-term roles, nonprofit projects, and
small-company trial work can create the first credible experience
([20:17-23:47 and 32:35-40:39]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }})).

Communication is part of the hiring signal. At
[59:59]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }}),
Juan Pablo recommends concise project communication and STAR framing. At
[1:01:06]({{ '/podcasts/from-math-graduate-to-data-analytics/' | relative_url }}),
he adds repo hygiene: a clean README and organized repository help reviewers
understand the work without reverse-engineering the code.

## Related Pages

These pages cover the adjacent roles, skills, and portfolio patterns.

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Data Analysis]({{ '/wiki/data-analysis/' | relative_url }})
- [Data Roles]({{ '/wiki/data-roles/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

