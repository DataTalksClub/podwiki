---
layout: wiki
title: "Data Analyst Role"
summary: "Data analyst role across podcast discussions: SQL, dashboards, metrics, experiments, stakeholder communication, and nearby data roles."
related:
  - Data Analyst Careers
  - Product Analytics
  - Analytics Engineering
  - Metrics
  - Experimentation
---

A data analyst helps a team understand what happened, why it happened, and what
decision should follow. SQL and dashboards form the technical base. The decision
work uses metrics, product context, experiment analysis, and clear communication
with people who own decisions.

The analyst knows what company data exists and how to retrieve it. They build
dashboards, define KPIs, quantify product problems, and check whether a shipped
feature improved user behavior
([[podcast:data-team-roles|Data Team Roles Explained]]). That makes the role
broader than report production. The analyst connects data to a product,
operational, or business decision.

## From Dashboards to Decisions

A data analyst turns company data into reusable evidence for decisions. They
build dashboards and reports, run ad hoc queries, make recommendations, and
support product teams. Analysts often know where the data lives better than data
scientists because they work with the tables every day
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

The role is especially visible in [[product analytics]]. The growth data flow
runs from collection to storage, then to analysis and activation. Analysts sit
between source events and downstream activation. Their work is distinct from data
engineering and product operations, with analytics engineering as a neighboring
role. That split shows why analysts need both source awareness and stakeholder
context
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

## Boundary Choices in Teams

Analysts work with metrics and decisions, but the role boundary is drawn
differently across teams.

When analysts work close to product managers, the product manager owns product
direction. The analyst quantifies the problem and helps decide whether the work
deserves team time ([[podcast:data-team-roles|Data Team Roles Explained]]). The
boundary can also extend toward experimentation. Analysts explain uplift,
segment differences, and root causes when online experiment results differ from
model expectations ([[person:rishabhbhargava|Rishabh Bhargava]],
[[podcast:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]).

The title is unstable, and that creates a real hiring problem. A job called
"data analyst" may mean BI reporting, product analytics, light data science, or
business analysis. Responsibilities matter more than the title
([[person:alicjanotowska|Alicja Notowska]],
[[podcast:hiring-data-scientists-and-analysts=>Hiring Data Scientists and Analysts]]).

Analytics engineering moves part of the old analyst workload into a more
engineered role. That shift contrasts with both data analyst and data
engineering work. It also reduces analysts' cleaning workload
([[person:victoriaperezmola|Victoria Perez Mola]],
[[podcast:analytics-engineer-skills-tools=>Master Analytics Engineering]]). The
overlap between data analyst and analytics engineer work appears when dashboard
logic needs stronger ownership. Metric definitions and transformation code can
need the same ownership
([[person:nikolamaksimovic|Nikola Maksimovic]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).

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

Analysts need to know how a metric is created, not only how to plot it. Tracking
plans, event properties, and ownership matter. Anomaly investigation traces back
to event origins. A dashboard number is only useful when the event
definition, collection path, and business meaning are clear
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

Analysts also support experimentation through A/B testing and shadow mode. They
also work with segmentation, uplift, and root-cause analysis
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).
The related [[experimentation]] work isn't only statistical. Analysts also define
success metrics and important segments, then explain mixed results to product
stakeholders.

Danny Ma says Type A analysts explore data, build dashboards, and visualize
findings before modeling starts. They help the team figure out which problem to
solve. He also ties that profile to business presentation. The team can then use
the findings for a commercial or project decision
([[cite:data-science-career-abc-framework|Data Science Career ABC Framework]]).

## Skill Stack

The skill stack is practical and communication-heavy.

SQL is the central technical skill for joins, aggregation, and window functions.
Analysts also use it for dates, funnels, and cohorts. They need enough data
modeling sense to avoid mixing grains. SQL and data visualization are core analyst
fundamentals, alongside soft skills and product understanding. Cohort analysis
and retention metrics are examples of product analytics work
([[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]]).

BI and visualization matter because analysts communicate through dashboards,
charts, and recurring views. A practical path starts with Excel and SQL. It then
adds dashboard practice and small projects. Later work adds Looker and LookML
plus reporting and dashboard building
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]]).
That path connects the analyst role with [[analytics engineering]] when modeled
tables and metric definitions become reusable team assets.

Danny adds Python or R to the analyst toolkit. The traditional toolkit already
includes SQL, Excel and Tableau plus visualization. He also adds more
statistics, ML theory, and experiment design. For analysts, that keeps
storytelling and visualization central to the role. It also turns the skill
stack into a base for light data science work
([[cite:data-science-career-abc-framework|Data Science Career ABC Framework]]).

Statistics matter when the decision depends on uncertainty, but analysts don't
need every model family. They need descriptive statistics, sampling basics, and
variance along with experiment interpretation and basic causal caution. Those
skills stay tied to product decisions through experiment analysis
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).
Cohort and retention analysis tie the same statistics work to product decisions
([[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]]).

Communication is part of the role, not a soft add-on. Analyst documentation
serves management and decision makers
([[podcast:data-team-roles|Data Team Roles Explained]]). From the candidate
side, clear responsibilities, dates, and practical examples beat vague buzzwords
([[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]).

## Adjacent Roles

The boundary with the [[data scientist role]] is messy because titles vary. In
many teams, analysts explain what happened and recommend decisions. Data
scientists add prediction, modeling, and model integration. The distinction runs
through the goals of analytics work versus ML work. Both roles share data
infrastructure and experiment feedback
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

The boundary with [[analytics engineering]] is about repeatability and ownership
of the analytical data layer. Analysts answer questions and interpret metrics.
Analytics engineers build tested, documented, BI-ready models. Analytics
engineering connects to data modeling, pipelines, and data quality. It also uses
Looker and `dbt` with version control, tests, and DAGs
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]).

[[Data Analyst vs Analytics Engineer]] defines the adjacent boundary. The
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
covers the transition when analysts want to own reusable models.

The boundary with the [[data engineer role]] is about data paths and operations.
Data engineers build ingestion and storage systems, then own orchestration and
platform work. Analysts use those systems to interpret the business. Data
engineers make the needed data usable
([[podcast:data-team-roles|Data Team Roles Explained]]). The operating version
of the same boundary appears when teams split tracking, warehousing, analysis,
and activation work
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

The boundary with product management is about ownership of the decision. Product
managers own product direction and prioritization. Analysts provide evidence
about problem size, affected users, and metric movement. They also explain
experiment outcomes and tradeoffs. The role therefore overlaps strongly with
[[metrics]], product analytics, and [[data teams]].

## Related Pages

These pages connect the analyst role to adjacent skills and career paths.

- [[Data Analyst Careers]]
- [[Data Analyst vs Analytics Engineer]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Metrics]]
- [[Experimentation]]
- [[Career Transitions in Data]]
