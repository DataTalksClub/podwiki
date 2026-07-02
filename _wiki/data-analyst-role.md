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
decision should follow. The technical base is SQL and dashboards; the decision
work uses metrics, product context, experiment analysis, and clear communication
with people who own decisions.

The analyst knows what company data exists and how to retrieve it, builds
dashboards and defines KPIs, quantifies product problems, and checks whether a
shipped feature improved user behavior
([[podcast:data-team-roles|Data Team Roles Explained]]). That makes the role
broader than report production: the analyst connects data to a product,
operational, or business decision.

## From Dashboards to Decisions

A data analyst turns company data into reusable evidence for decisions: building
dashboards and reports, running ad hoc queries, making recommendations, and
supporting product teams. Analysts often know where the data lives better than
data scientists because they work with the tables every day
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

The role is especially visible in [[product analytics]]. The growth data flow
runs from collection to storage, then to analysis and activation, placing
analysts between source events and downstream activation; analyst work is
distinct from data engineering and product operations, with analytics engineering
as a neighboring role. That split shows why analysts need both source awareness
and stakeholder context
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

## Boundary Choices in Teams

Analysts work with metrics and decisions, but the role boundary is drawn
differently across teams.

Close to the product manager: the product manager owns product direction while
the analyst quantifies the problem and helps decide whether the work deserves
team time ([[podcast:data-team-roles|Data Team Roles Explained]]). The boundary
can also extend toward experimentation, with analysts explaining uplift, segment
differences, and root causes when online experiment results differ from model
expectations ([[person:rishabhbhargava|Rishabh Bhargava]],
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

The title is unstable, which is a real hiring problem: a job called "data
analyst" may mean BI reporting, product analytics, light data science, or
business analysis, so responsibilities matter more than the title
([[person:alicjanotowska|Alicja Notowska]],
[[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]).

Analytics engineering moves part of the old analyst workload into a more
engineered role, contrasting with both data analyst and data engineering work and
reducing analysts' cleaning workload
([[person:victoriaperezmola|Victoria Perez Mola]],
[[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]). The
overlap between data analyst and analytics engineer work appears when dashboard
logic, metric definitions, and transformation code need stronger ownership
([[person:nikolamaksimovic|Nikola Maksimovic]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]]).

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

Analysts need to know how a metric is created, not only how to plot it: tracking
plans, event properties, and ownership matter, and anomaly investigation traces
back to event origins. A dashboard number is only useful when the event
definition, collection path, and business meaning are clear
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

Analysts also support experimentation, connecting to A/B testing, shadow mode,
segmentation, uplift, and root-cause analysis
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).
The related [[experimentation]] work is not only statistical, because analysts
also define success metrics and important segments, then explain mixed results to
product stakeholders.

## Skill Stack

The skill stack is practical and communication-heavy.

SQL is the central technical skill, used for joins, aggregation, and windows,
plus dates, funnels, cohorts, and enough data modeling sense to avoid mixing
grains. SQL and data visualization are core analyst fundamentals, alongside soft
skills and product understanding, with cohort analysis and retention metrics as
examples of product analytics work
([[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]]).

BI and visualization matter because analysts communicate through dashboards,
charts, and recurring views. A practical path runs Excel and SQL first, then
dashboard practice and small projects, then Looker, LookML, reporting, and
dashboard building
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]]).
That path connects the analyst role with [[analytics engineering]] when modeled
tables and metric definitions become reusable team assets.

Statistics matter when the decision depends on uncertainty. Analysts do not need
every model family, but they need descriptive statistics and sampling basics,
variance, experiment interpretation, and basic causal caution — tied to product
decisions rather than abstract calculation, through experiment analysis
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]])
and cohort and retention analysis
([[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]]).

Communication is part of the role, not a soft add-on. Analyst documentation
serves management and decision makers
([[podcast:data-team-roles|Data Team Roles Explained]]), and from the candidate
side, clear responsibilities, dates, and practical examples beat vague buzzwords
([[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]).

## Adjacent Roles

The boundary with the [[data scientist role]] is messy because titles vary. In
many teams, analysts explain what happened and recommend decisions, while data
scientists add prediction, modeling, and model integration. The distinction runs
through the goals of analytics work versus ML work, though both roles share data
infrastructure and experiment feedback
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

The boundary with [[analytics engineering]] is about repeatability and ownership
of the analytical data layer. Analysts answer questions and interpret metrics;
analytics engineers build tested, documented, BI-ready models. Analytics
engineering connects to data modeling, pipelines, and data quality, and to
Looker, `dbt`, version control, tests, and DAGs
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]).
[[Data Analyst vs Analytics Engineer]] defines the adjacent boundary, and the
[[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
covers the transition when analysts want to own reusable models.

The boundary with the [[data engineer role]] is about data paths and operations.
Data engineers build ingestion and storage systems and own orchestration and
platform work; analysts use those systems to interpret the business. Data
engineers make the needed data usable
([[podcast:data-team-roles|Data Team Roles Explained]]), and the operating version
of the same boundary appears when teams split tracking, warehousing, analysis,
and activation work
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

The boundary with product management is about ownership of the decision. Product
managers own product direction and prioritization; analysts provide evidence
about problem size, affected users, and metric movement, and explain experiment
outcomes and tradeoffs. The role therefore overlaps strongly with [[metrics]],
product analytics, and [[data teams]].

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
