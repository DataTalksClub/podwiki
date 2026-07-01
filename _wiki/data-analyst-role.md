---
layout: wiki
title: "Data Analyst Role"
summary: "Archive-backed guide to the data analyst role: SQL, metrics, dashboards, experiments, stakeholder communication, and boundaries with analytics engineering, data science, and data engineering."
related:
  - Data Analyst Careers
  - Product Analytics
  - Analytics Engineering
  - Metrics
  - Experimentation
---

## Definition

A data analyst helps a team understand what happened, why it happened, and what
decision should follow. In DataTalks.Club discussions, the technical base is
SQL and dashboards. The decision work uses metrics, product context, experiment
analysis, and clear communication with people who own decisions.

In [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst knows what company data exists and how to retrieve it. The analyst
builds dashboards and defines KPIs. The analyst also quantifies product
problems and checks whether a shipped feature improved user behavior around
7:51-10:39. That framing makes the role broader than report production. The
analyst connects data to a product, operational, or business decision.

## Common Definition

Across the archive, a data analyst turns company data into reusable evidence for
decisions. In
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
analysts as people who build dashboards and reports around 18:39-24:23. They
also run ad hoc queries, make recommendations, and support product teams. At
24:23, he adds a practical detail for real teams. Analysts often know where the
data lives better than data scientists because they work with the tables every
day.

The role is especially visible in
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}).
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) explains the
growth data flow in [How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})
from collection to storage around 22:50-30:03. He then connects storage to
analysis and activation. That places analysts between source events and
downstream activation.

At 46:13, he separates analyst work from data engineering and product
operations. He also names analytics engineering as a neighboring role. That
split shows why analysts need both source awareness and stakeholder context.

## Role Disagreements

Guests agree that analysts work with metrics and decisions, but they draw the
role boundary differently.

In the role-definition episode, the analyst sits close to the product manager.
The product manager owns the product direction. The analyst quantifies the
problem and helps decide whether the work deserves team time. In
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
Rishabh extends the boundary toward experimentation. Around 31:19-33:30, he
describes analysts helping explain uplift, segment differences, and root causes
when online experiment results differ from model expectations.

Recruiting discussions show a different source of disagreement: the title is
unstable. In
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }}),
[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }}) discusses
data analyst hiring around 54:09-59:30 and treats title ambiguity as a real
hiring problem. A job called "data analyst" may mean BI reporting or product
analytics. It can also mean light data science or business analysis. The
responsibilities matter more than the title.

Analytics engineering guests move part of the old analyst workload into a more
engineered role. In
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
contrasts analytics engineering with data analyst work around 14:34. She also
compares it with data engineering and links the role to reducing analysts'
cleaning workload around 16:54. In
[Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) describes
an overlap between data analyst and analytics engineer work around 25:06. That
overlap appears when dashboard logic, metric definitions, and transformation
code need stronger ownership.

## Responsibilities

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

The archive repeatedly shows that analysts need to know how a metric is
created, not only how to plot it. In
[How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
Arpit discusses tracking plans, event properties, and ownership around
13:34-18:27. He also traces anomaly investigation back to event origins. For an
analyst, a dashboard number is only useful when the event definition,
collection path, and business meaning are clear.

Analysts also support experimentation, and Rishabh's episode connects analysts to
A/B testing, shadow mode, and segmentation around 28:42-33:30. He also connects
the role to uplift and root-cause analysis. The related
[experimentation]({{ '/wiki/experimentation/' | relative_url }}) work isn't only
statistical because analysts also define success metrics and important
segments. They then explain mixed results to product stakeholders.

## Skills

The skill stack is practical and communication-heavy.

SQL is the central technical skill because analysts use it for joins,
aggregation, and windows. They also need dates, funnels, cohorts, and enough
data modeling sense to avoid mixing grains.

In
[Designing FinTech Data Analytics Curriculum]({{ '/podcasts/teaching-mentoring-data-analytics-fintech/' | relative_url }}),
[Irina Brudaru]({{ '/people/irinabrudaru/' | relative_url }}) names SQL and
data visualization as core analyst fundamentals around 58:08. She also includes
soft skills and product understanding. Around 31:50, she uses cohort analysis
and retention metrics as examples of product analytics work.

BI and visualization matter because analysts communicate through dashboards,
charts, and recurring views. Nikola's transition episode shows a practical path:
Excel and SQL first, then dashboard practice and small projects around 41:50.
His work then moves into Looker, LookML, reporting, and dashboard building
around 23:12. That path connects the analyst role with
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
when modeled tables and metric definitions become reusable team assets.

Statistics matter when the decision depends on uncertainty. Analysts don't need
every model family, but they need descriptive statistics and sampling basics.
They also need variance, experiment interpretation, and basic causal caution.
The archive's analyst examples connect statistics to product decisions, not
abstract calculation. See
Rishabh on experiment analysis around 31:19 and Irina on cohort and retention
analysis around 31:50.

Communication is part of the role, not a soft add-on. The role-definition
episode describes analyst documentation as material for management and decision
makers around 18:17-19:08. Alicja's hiring episode reinforces this from the
candidate side: around 28:41-32:40, she emphasizes clear responsibilities,
dates, and practical examples over vague buzzwords.

## Boundaries

The boundary with the
[data scientist role]({{ '/wiki/data-scientist-role/' | relative_url }}) is
messy because titles vary. In many teams, analysts explain what happened and
recommend decisions. Data scientists add prediction, modeling, and model
integration. Rishabh's analytics-to-ML discussion makes this distinction
through the goals of analytics work versus ML work around 10:48-13:48. His
later comments show that both roles share data infrastructure and experiment
feedback.

The boundary with
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
is about repeatability and ownership of the analytical data layer. Analysts
answer questions and interpret metrics. Analytics engineers build tested,
documented, BI-ready models.

Victoria's episode connects analytics engineering to data modeling, pipelines,
and data quality. She also links the role to Looker, `dbt`, and version
control. Tests and DAGs also appear around 4:05-6:49.

[Data Analyst vs Analytics Engineer]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
defines the adjacent boundary. The
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
covers the transition when analysts want to own reusable models.

The boundary with the
[data engineer role]({{ '/wiki/data-engineer-role/' | relative_url }}) is
about data paths and operations. Data engineers build ingestion, storage,
orchestration, and platform systems. Analysts use those systems to interpret
the business. In the role-definition episode, data engineers appear after the
analyst discussion as the people who make the needed data usable around 13:58.
Arpit's growth-stack episode gives the operating version of the same boundary
when teams split tracking, warehousing, analysis, and activation work
around 46:13.

The boundary with product management is about ownership of the decision.
Product managers own product direction and prioritization. Analysts provide
evidence about problem size, affected users, and metric movement. They also
explain experiment outcomes and tradeoffs. The role therefore overlaps strongly with
[metrics]({{ '/wiki/metrics/' | relative_url }}), product analytics, and
[data teams]({{ '/wiki/data-teams/' | relative_url }}).

## Related Pages

These pages connect the analyst role to adjacent skills and career paths.

- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
