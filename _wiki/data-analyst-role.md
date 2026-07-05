---
layout: wiki
title: "Data Analyst Role"
summary: "How data analyst work connects SQL, dashboards, metrics, experiments, stakeholder communication, and nearby data roles."
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
dashboards and define KPIs. They quantify product problems and check whether a
shipped feature improved user behavior.[[cite:data-team-roles=>Data Team Roles Explained]]
That makes the role broader than report production. The analyst connects data to
a product, operational, or business decision.

The role definition belongs here. [[Data Analyst Careers]] covers entry routes,
portfolios, hiring signals, and next moves.
[[product-analyst-vs-data-analyst=>product analyst vs data analyst]]
and [[Data Analyst vs Analytics Engineer]] cover boundaries between adjacent
titles.

## From Dashboards to Decisions

A data analyst turns company data into reusable evidence for decisions. They
build dashboards and reports, run ad hoc queries, make recommendations, and
support product teams. Analysts often know where the data lives better than data
scientists because they work with the tables every day.[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]

The role is especially visible in [[product analytics]]. The growth data flow
runs from collection to storage, then to analysis and activation. Analysts sit
between source events and downstream activation. Their work is distinct from data
engineering and product operations, with analytics engineering as a neighboring
role. That split shows why analysts need both source awareness and stakeholder
context.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

## Boundary Choices in Teams

Analysts work with metrics and decisions, but the role boundary is drawn
differently across teams.

When analysts work close to product managers, the product manager owns product
direction. The analyst quantifies the problem and helps decide whether the work
deserves team time.[[cite:data-team-roles=>Data Team Roles Explained]] The
boundary can also extend toward experimentation. Analysts explain uplift,
segment differences, and root causes when online experiment results differ from
model expectations.[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]

The title is unstable, and that creates a real hiring problem. A job called
"data analyst" may mean BI reporting, product analytics, light data science, or
business analysis. Responsibilities matter more than the title.[[cite:hiring-data-scientists-and-analysts=>Hiring Data Scientists and Analysts]]

Analytics engineering moves part of the old analyst workload into a more
engineered role. That shift contrasts with both data analyst and data
engineering work. It also reduces analysts' cleaning workload.[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
The overlap between data analyst and analytics engineer work appears when
dashboard logic needs stronger ownership. Metric definitions and transformation
code can need the same ownership.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]

## Decision Support Responsibilities

Decision support includes:

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
definition, collection path, and business meaning are clear.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

Analysts also support experimentation through A/B testing and shadow mode. They
also work with segmentation, uplift, and root-cause analysis.[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]
The related [[experimentation]] work isn't only statistical. Analysts also define
success metrics and important segments, then explain mixed results to product
stakeholders.

Type A analysts explore data before modeling starts by building dashboards and
visualizations. They help choose the problem to solve and translate findings
into a commercial or project decision.[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]]

That makes the analyst path a legitimate target, not only a stepping stone to
modeling. Exploration, visualization, and storytelling can be the main evidence
when the job is decision support.[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]]

The analyst version of data science starts with curiosity about the data, but
it doesn't end with charts. Danny Ma places experimentation, statistics, and
storytelling beside SQL and visualization tools. The analyst has to
show what changed, why it matters, and which decision should follow
[[cite:data-science-career-abc-framework@13:17=>Data Science Career ABC Framework]].
That connects the role to [[Communication]], [[Metrics]], and
[[Experimentation]], not only to BI tooling.

The Type A path can also grow from analyst work toward data science without
discarding the analyst base. SQL, Excel, Tableau, and visualization remain
useful. Python or R, statistics, experiment design, and basic ML add range.
Communication stays central because analyst-style data science still has to
move a business or product decision.[[cite:data-science-career-abc-framework@18:20=>Data Science Career ABC Framework]]

## Skill Stack

The skill stack is practical and communication-heavy.

SQL is the central technical skill for joins, aggregation, and window functions.
Analysts also use it for dates, funnels, and cohorts. They need enough data
modeling sense to avoid mixing grains. SQL and data visualization are core analyst
fundamentals, alongside soft skills and product understanding. Cohort analysis
and retention metrics are examples of product analytics work.[[cite:teaching-mentoring-data-analytics-fintech=>Designing FinTech Data Analytics Curriculum]]

BI and visualization matter because analysts communicate through dashboards,
charts, and recurring views. A practical path starts with Excel and SQL. It then
adds dashboard practice and small projects. Later work adds Looker and LookML
plus reporting and dashboard building.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]

That path connects the analyst role with [[analytics engineering]] when modeled
tables and metric definitions become reusable team assets.

The analyst toolkit can start with SQL, Excel, Tableau, and visualization. It can
extend into Python or R plus statistics, ML theory, and experiment design.
Storytelling and visualization stay central, while the broader stack creates a
base for light data science work.[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]]

Statistics matter when the decision depends on uncertainty, but analysts don't
need every model family. They need descriptive statistics, sampling basics, and
variance. They also need experiment interpretation and basic causal caution.
Those skills stay tied to product decisions through experiment analysis.[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]

Cohort and retention analysis tie the same statistics work to product
decisions.[[cite:teaching-mentoring-data-analytics-fintech=>Designing FinTech Data Analytics Curriculum]]

Communication is part of the role, not a soft add-on. Analyst documentation
serves management and decision makers.[[cite:data-team-roles=>Data Team Roles Explained]]

From the candidate side, clear responsibilities, dates, and practical examples
beat vague buzzwords.[[cite:hiring-data-scientists-and-analysts=>Hiring Data Scientists and Analysts]]

## Adjacent Roles

The boundary with the [[data scientist role]] is messy because titles vary. In
many teams, analysts explain what happened and recommend decisions. Data
scientists add prediction, modeling, and model integration. The distinction runs
through the goals of analytics work versus ML work. Both roles share data
infrastructure and experiment feedback.[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]

The boundary with [[analytics engineering]] is about repeatability and ownership
of the analytical data layer. Analysts answer questions and interpret metrics.
Analytics engineers build tested, documented, BI-ready models. Analytics
engineering connects to data modeling, pipelines, and data quality. It also uses
Looker and `dbt` with version control, tests, and DAGs.[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]

[[Data Analyst vs Analytics Engineer]] defines the adjacent boundary. The
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
covers the transition when analysts want to move from role understanding into
reusable-model ownership.

The boundary with the [[data engineer role]] is about data paths and operations.
Data engineers build ingestion and storage systems. They also own orchestration
and platform work. Analysts use those systems to interpret the business. Data
engineers make the needed data usable.[[cite:data-team-roles=>Data Team Roles Explained]]

An analyst may want to own those upstream paths. The
[[data-analyst-to-data-engineer=>data analyst to data engineer]] transition
turns source-aware SQL work into pipeline evidence while keeping business
context visible.

The operating version of the same boundary appears when teams split tracking,
warehousing, analysis, and activation work.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

The boundary with product management is about ownership of the decision. Product
managers own product direction and prioritization. Analysts provide evidence
about problem size, affected users, and metric movement. They also explain
experiment outcomes and tradeoffs. The role therefore overlaps strongly with
[[metrics]], product analytics, and [[data teams]].

## Related Pages

Adjacent role, career, and topic pages:

- [[Data Analyst Careers]]
- [[Data Analyst vs Analytics Engineer]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Metrics]]
- [[Experimentation]]
- [[Career Transitions in Data]]
