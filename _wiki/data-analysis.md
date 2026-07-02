---
layout: article
tags: ["guide"]
title: "Data Analysis: Practical Work, Skills, and Portfolio Projects"
keyword: "data analysis"
summary: "A podcast-backed guide to practical data analysis: SQL, metrics, dashboards, experiments, stakeholder communication, role boundaries, and portfolio evidence."
search_intent: "People searching for data analysis want a practical definition, examples of analysis work, core skills such as SQL and dashboards, differences from data science and analytics engineering, and project ideas they can use for a portfolio or career move."
related_wiki:
  - Data Analyst Role
  - Data Analyst Careers
  - Product Analytics
  - Metrics
  - Experimentation
  - Analytics Engineering
  - Data Products
---

Data analysis is the work of turning data into evidence for a decision. In the
DataTalks.Club podcast discussions, analysts first find the right data and check what the
numbers mean. They choose metrics, build dashboards or written readouts, and
explain what a team should do next. It's close to
[[data-analyst-role|data analyst work]], but the
practice also appears in [[product analytics]]
and [[analytics engineering]].
It also appears in experimentation and data leadership.

In [[podcast:data-team-roles|Data Team Roles Explained]],
the analyst knows what company data exists. They retrieve it and define KPIs.
They also build dashboards, quantify product problems, and check whether
shipped work changed user behavior around 7:51-10:39. That makes data analysis
more than charting. It's a loop from question to evidence to decision
([[Data Analyst Role]]).

## Practical Definition

Practical data analysis starts with the decision, not the tool. A good analysis
asks who will act on the result and which metric will change the decision. It
also asks which data is trustworthy enough to use and which caveats need to be
visible.

[[person:caitlinmoorman|Caitlin Moorman]] makes this
point in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].
She argues for outcome-first analytics around 34:00, then connects metrics to
real meetings and decisions around 38:15. A dashboard that nobody trusts or
uses isn't finished analysis.

That outcome-first view also explains why analysts spend time on source data.
[[person:arpitchoudhury|Arpit Choudhury]] shows the
product analytics version in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]].
He starts with tracking plans, event names, event properties, and ownership
around 13:34-18:27. He then follows events through storage, transformation, BI,
and activation around 22:50-41:30. A funnel or retention chart is only useful
when the analyst knows how the underlying events were captured.

For career planning, "data analysis" isn't a narrow task. Analysts can work
on ad hoc SQL, dashboard design, cohort analysis, and experiment readouts. They
can also own metric definitions, stakeholder interviews, and written
recommendations. The
[[Data Analyst Careers]]
page collects the career side of that work.

## SQL, Metrics, and Dashboards

SQL is the usual base skill because analysts need command of the tables before
they can explain what happened. They use SQL to join data, filter records,
aggregate rows, and check assumptions.

In
[[podcast:data-team-roles|Data Team Roles Explained]],
SQL and dashboarding sit next to KPI definition and product problem sizing.

In
[[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]],
[[person:irinabrudaru|Irina Brudaru]] names SQL and
data visualization as analyst fundamentals around 58:08. Cohort analysis and
retention metrics appear earlier around 31:50.

Metrics are the bridge between data and action. The
[[Metrics]] wiki page defines them as
decision rules expressed as numbers. That's more useful than treating metrics
as dashboard fields. [[person:jakobgraff|Jakob Graff]]
shows why in
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]:
a subscription-versus-points experiment can tell different stories. The
interpretation changes when the team measures revenue, conversion, retention,
or long-term value around 14:27-18:06.

Analysts often deliver dashboards, but they shouldn't stop there.
[[person:tammyliang|Tammy Liang]] describes building
business health dashboards first in
[[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]]
around 7:22. The team then had to streamline reporting and build trust. They
also had to handle spreadsheet culture and support adoption around 8:51-10:06.

Liang later discusses dashboard checks, monitoring, and operational visibility
around 40:09-41:42. Dashboards work when the team trusts the definitions,
checks the numbers, and connects the view to a recurring decision.

## Product Analytics and Experiments

Product-facing data analysis often asks how users behave and whether a change
improved the product. That work depends on
[[event tracking]],
[[tracking plans]], and
[[product analytics]]. Arpit's
growth-stack episode shows why analysis starts before the dashboard. Teams need
event definitions and properties before they can trust funnels. They also need
source context and ownership before they can trust activation metrics or anomaly
investigations
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth at 13:34-30:03]]).

Experiments ask whether the change caused the metric movement.
Jakob's A/B testing episode moves from product analytics into causality. He
covers randomization around 8:13 and feature de-risking around 18:06. He then
covers assignment tracking around 24:44, A/A testing around 27:52, and power
analysis around 37:44. Product teams can make the wrong decision when results
are noisy or underpowered
([[Experimentation]],
[[Experimentation and Causal Inference]]).

This doesn't mean every analysis needs a full statistical test. Moorman's
last-mile discussion is a useful counterweight. Around 28:42, she talks about
simplifying A/B test reporting for decision makers. Around 39:32-45:35, she
uses low-fidelity prototypes, narrow measurable wins, and adoption work to
make analytics useful. The analyst's job is to match the analysis method to
the decision, not to make every question look like the same experiment.

## Analysis, Data Science, and Analytics Engineering

Data analysis overlaps with data science, but the center of gravity differs.
Analysts usually explain what happened and why it happened. They also explain
what decision should follow. Data scientists are more likely to own prediction
and modeling. They also tend to own model-backed product decisions
([[Data Scientist Role]]).

In
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]],
[[person:rishabhbhargava|Rishabh Bhargava]] describes
analysts as people who build dashboards and reports. They also write ad hoc
queries and recommendations around 18:39-24:23. He then connects analysts to experiment
uplift, segment differences, and root-cause analysis around 31:19-33:30.

Analytics engineering is another neighboring role. Analysts own the question,
interpretation, and recommendation, while analytics engineers own reusable
models and BI-ready data layers. They also own tests and documentation.

[[person:victoriaperezmola|Victoria Perez Mola]]
grounds analytics engineering in data modeling, pipelines, data quality, and
Looker in
[[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]
around 4:05-10:04. She also explains the overlap with analysts around
14:34-16:54. The
[[Data Analyst vs Analytics Engineer]]
page gives the practical boundary. Analysts own decision support. Analytics
engineers own reusable and tested analytical models.

Small teams often blur those boundaries.
[[person:nikolamaksimovic|Nikola Maksimovic]]
describes an analytics engineering role that included product support and
A/B testing. The same role included Looker dashboards, `dbt`, and data
modeling. It also included growth analysis, retention analysis, and RFM
analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing to analytics engineering at 14:14-39:36]]).

For a learner or hiring manager, the title matters less than the ownership.
Ask which decision, model, metric, or data product the person improves.

## Communication and Storytelling

Data analysis becomes useful when someone can understand it and act on it.
That requires writing, visualization, and stakeholder communication. In
[[podcast:data-journalism-python-visualization-storytelling|Practical Data Journalism]],
[[person:angelicaloduca|Angelica Lo Duca]] distinguishes
data journalism from broader data science around 8:01. She then moves into
data sourcing, storytelling, and visualization. Around 36:20, she recommends
one concept per chart and tables when they're clearer.

The same communication standard appears in hiring and team discussions.
[[person:alicjanotowska|Alicja Notowska]] says in
[[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]
that candidates should show clear responsibilities, dates, and practical
examples around 28:41-32:40. Around 54:09-59:30, she also warns that data
analyst titles are ambiguous. A resume or portfolio needs to explain the actual
analysis work, not just list tools.

[[person:katiebauer|Katie Bauer]] brings the team
quality view in
[[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|Hiring and Managing Data Science Teams]].
Around 11:58, she connects analytics craft to maintainability, documentation,
and peer review. Around 34:16, she discusses stakeholder conversations with PMs
and senior leaders. Analysts need statistical care and social trust. People
need to trust the method, understand the caveats, and know what happens next.

## Portfolio Projects for Data Analysis

A strong data analysis portfolio should show the path from question to
decision. It shouldn't be a gallery of disconnected charts. The project should
state the decision and define the metric. It should explain the data source,
show the SQL or Python work, and visualize the result. It should finish with a
recommendation and caveats
([[Data Analyst Careers]],
[[Job Search]]).

Good project shapes follow the podcast evidence:

- a product funnel or cohort analysis with a tracking plan, based on Arpit's
  event-tracking and warehouse flow
  ([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth at 13:34-30:03]])
- an experiment readout with a primary metric, guardrails, assignment checks,
  and power discussion, based on Jakob's A/B testing workflow
  ([[podcast:ab-testing-and-product-experimentation|A/B testing at 24:44-40:23]])
- a business health dashboard with definitions, monitoring checks, and adoption
  notes, based on Tammy's data team buildout
  ([[podcast:building-and-scaling-data-team|building a data team at 7:22-10:06 and 40:09-41:42]])
- a written analysis or data story that gives each chart a single point and
  explains the data source, based on Angelica's data journalism workflow
  ([[podcast:data-journalism-python-visualization-storytelling|data journalism at 29:19-40:47]])

For analysts who want to move toward analytics engineering, add reusable data
models, tests, and documentation. Perez Mola's role episode ties that direction
to SQL transformations and version control. It also ties the path to tests and
dependency graphs around 6:49-10:04. The
[[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
turns that move into a learning and project sequence.

For analysts who want to move toward data science, add prediction, evaluation,
and experiment interpretation. Then
connect those choices to the
[[Data Scientist Role]] and
[[Machine Learning Portfolio Projects]].

The practical standard is simple: show that you can move from messy data and an
ambiguous question to a trustworthy recommendation. That's the useful core of
data analysis. The final artifact can be a SQL query, a dashboard, an
experiment memo, or a stakeholder presentation.

