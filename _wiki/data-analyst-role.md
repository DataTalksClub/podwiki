---
layout: wiki
title: "Data Analyst Role"
summary: "DataTalks.Club podcast guide to the data analyst role: SQL, metrics, dashboards, experiments, stakeholder communication, and boundaries with analytics engineering, data science, and data engineering."
related:
  - Data Analyst Careers
  - Product Analytics
  - Analytics Engineering
  - Metrics
  - Experimentation
---

A data analyst helps a team understand what happened, why it happened, and what
decision should follow. In DataTalks.Club discussions, the technical base is
SQL and dashboards. The decision work uses metrics, product context, experiment
analysis, and clear communication with people who own decisions.

In [[podcast:data-team-roles|Data Team Roles Explained]],
the analyst knows what company data exists and how to retrieve it. The analyst
builds dashboards and defines KPIs. The analyst also quantifies product
problems and checks whether a shipped feature improved user behavior around
7:51-10:39. That framing makes the role broader than report production. The
analyst connects data to a product, operational, or business decision.

## From Dashboards to Decisions

Across these discussions, a data analyst turns company data into reusable
evidence for decisions. In
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]],
[[person:rishabhbhargava|Rishabh Bhargava]] describes
analysts as people who build dashboards and reports around 18:39-24:23. They
also run ad hoc queries, make recommendations, and support product teams. At
24:23, he adds a practical detail for real teams. Analysts often know where the
data lives better than data scientists because they work with the tables every
day.

The role is especially visible in
[[product analytics]].
[[person:arpitchoudhury|Arpit Choudhury]] explains the
growth data flow in [[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]
from collection to storage around 22:50-30:03. He then connects storage to
analysis and activation. That places analysts between source events and
downstream activation.

At 46:13, he separates analyst work from data engineering and product
operations. He also names analytics engineering as a neighboring role. That
split shows why analysts need both source awareness and stakeholder context.

## Boundary Choices in Teams

Guests agree that analysts work with metrics and decisions, but they draw the
role boundary differently.

In [[podcast:data-team-roles|Data Team Roles Explained]],
the analyst sits close to the product manager. The product manager owns the
product direction. The analyst quantifies the problem and helps decide whether
the work deserves team time. In
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]],
Rishabh extends the boundary toward experimentation. Around 31:19-33:30, he
describes analysts helping explain uplift, segment differences, and root causes
when online experiment results differ from model expectations.

Recruiting discussions show a different source of disagreement: the title is
unstable. In
[[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]],
[[person:alicjanotowska|Alicja Notowska]] discusses
data analyst hiring around 54:09-59:30 and treats title ambiguity as a real
hiring problem. A job called "data analyst" may mean BI reporting or product
analytics. It can also mean light data science or business analysis. The
responsibilities matter more than the title.

Analytics engineering guests move part of the old analyst workload into a more
engineered role. In
[[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]],
[[person:victoriaperezmola|Victoria Perez Mola]]
contrasts analytics engineering with data analyst work around 14:34. She also
compares it with data engineering and links the role to reducing analysts'
cleaning workload around 16:54. In
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]],
[[person:nikolamaksimovic|Nikola Maksimovic]] describes
an overlap between data analyst and analytics engineer work around 25:06. That
overlap appears when dashboard logic, metric definitions, and transformation
code need stronger ownership.

## Decision-Support Responsibilities

The analyst's core responsibility is decision support.

That work can include:

- query company data with SQL and BI tools
- define KPIs, metric logic, segments, cohorts, funnels, and dashboard views
- investigate metric movement, anomalies, instrumentation gaps, and source
  issues
- build dashboards and recurring reports for product, leadership, growth, and
  operations teams
- analyze launches, experiments, and A/B tests
- explain caveats and recommendations in language stakeholders can act on

Guests repeatedly show that analysts need to know how a metric is
created, not only how to plot it. In
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]],
Arpit discusses tracking plans, event properties, and ownership around
13:34-18:27. He also traces anomaly investigation back to event origins. For an
analyst, a dashboard number is only useful when the event definition,
collection path, and business meaning are clear.

Analysts also support experimentation, and Rishabh's episode connects analysts to
A/B testing, shadow mode, and segmentation around 28:42-33:30. He also connects
the role to uplift and root-cause analysis. The related
[[experimentation]] work isn't only
statistical because analysts also define success metrics and important
segments. They then explain mixed results to product stakeholders.

## Skill Stack

The skill stack is practical and communication-heavy.

SQL is the central technical skill because analysts use it for joins,
aggregation, and windows. They also need dates, funnels, cohorts, and enough
data modeling sense to avoid mixing grains.

In
[[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]],
[[person:irinabrudaru|Irina Brudaru]] names SQL and
data visualization as core analyst fundamentals around 58:08. She also includes
soft skills and product understanding. Around 31:50, she uses cohort analysis
and retention metrics as examples of product analytics work.

BI and visualization matter because analysts communicate through dashboards,
charts, and recurring views. Nikola's transition episode shows a practical path:
Excel and SQL first, then dashboard practice and small projects around 41:50.
His work then moves into Looker, LookML, reporting, and dashboard building
around 23:12. That path connects the analyst role with
[[analytics engineering]]
when modeled tables and metric definitions become reusable team assets.

Statistics matter when the decision depends on uncertainty. Analysts don't need
every model family, but they need descriptive statistics and sampling basics.
They also need variance, experiment interpretation, and basic causal caution.
Rishabh and Irina connect statistics to product decisions, not abstract
calculation. See Rishabh on experiment analysis around 31:19 and Irina on
cohort and retention analysis around 31:50.

Communication is part of the role, not a soft add-on.
[[podcast:data-team-roles|Data Team Roles Explained]]
describes analyst documentation as material for management and decision makers
around 18:17-19:08. Alicja's hiring episode reinforces this from the candidate
side: around 28:41-32:40, she emphasizes clear responsibilities, dates, and
practical examples over vague buzzwords.

## Adjacent Roles

The boundary with the
[[data scientist role]] is
messy because titles vary. In many teams, analysts explain what happened and
recommend decisions. Data scientists add prediction, modeling, and model
integration. Rishabh's analytics-to-ML discussion makes this distinction
through the goals of analytics work versus ML work around 10:48-13:48. His
later comments show that both roles share data infrastructure and experiment
feedback.

The boundary with
[[analytics engineering]]
is about repeatability and ownership of the analytical data layer. Analysts
answer questions and interpret metrics. Analytics engineers build tested,
documented, BI-ready models.

Victoria's episode connects analytics engineering to data modeling, pipelines,
and data quality. She also links the role to Looker, `dbt`, and version
control. Tests and DAGs also appear around 4:05-6:49.

[[Data Analyst vs Analytics Engineer]]
defines the adjacent boundary. The
[[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
covers the transition when analysts want to own reusable models.

The boundary with the
[[data engineer role]] is
about data paths and operations. Data engineers build ingestion and storage
systems. They also own orchestration and platform work. Analysts use those
systems to interpret the business.

In
[[podcast:data-team-roles|Data Team Roles Explained]],
data engineers appear after the analyst discussion as the people who make the
needed data usable around 13:58. Arpit's growth-stack episode gives the
operating version of the same boundary when teams split tracking, warehousing,
analysis, and activation work around 46:13.

The boundary with product management is about ownership of the decision.
Product managers own product direction and prioritization. Analysts provide
evidence about problem size, affected users, and metric movement. They also
explain experiment outcomes and tradeoffs. The role therefore overlaps strongly with
[[metrics]], product analytics, and
[[data teams]].

## Related Pages

These pages connect the analyst role to adjacent skills and career paths.

- [[Data Analyst Careers]]
- [[Data Analyst vs Analytics Engineer]]
- [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Metrics]]
- [[Experimentation]]
- [[Career Transitions in Data]]
