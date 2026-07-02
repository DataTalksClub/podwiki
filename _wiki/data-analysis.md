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

Data analysis is the work of turning data into evidence for a decision. Analysts
first find the right data and check what the
numbers mean. They choose metrics, build dashboards or written readouts, and
explain what a team should do next. It's close to
[[data-analyst-role|data analyst work]], but the
practice also appears in [[product analytics]]
and [[analytics engineering]].
It also appears in experimentation and data leadership.

An analyst knows what company data exists, retrieves it, and defines KPIs. They
also build dashboards, quantify product problems, and check whether shipped work
changed user behavior ([[podcast:data-team-roles|Data Team Roles Explained]]).
That makes data analysis more than charting. It's a loop from question to
evidence to decision
([[Data Analyst Role]]).

## Practical Definition

Practical data analysis starts with the decision, not the tool. A good analysis
asks who will act on the result and which metric will change the decision. It
also asks which data is trustworthy enough to use and which caveats need to be
visible.

Analytics should be outcome-first, with metrics connected to real meetings and
decisions
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]).
A dashboard that nobody trusts or uses isn't finished analysis.

That outcome-first view also explains why analysts spend time on source data.
The product analytics version starts with tracking plans, event names, event
properties, and ownership, then follows events through storage, transformation,
BI, and activation
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).
A funnel or retention chart is only useful when the analyst knows how the
underlying events were captured.

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

SQL and data visualization are analyst fundamentals, alongside cohort analysis
and retention metrics
([[podcast:teaching-mentoring-data-analytics-fintech|Designing FinTech Data Analytics Curriculum]]).

Metrics are the bridge between data and action. The
[[Metrics]] wiki page defines them as
decision rules expressed as numbers, which is more useful than treating metrics
as dashboard fields. A subscription-versus-points experiment can tell different
stories, and the interpretation changes when the team measures revenue,
conversion, retention, or long-term value
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]).

Analysts often deliver dashboards, but they shouldn't stop there. Business health
dashboards can come first, after which the team has to streamline reporting,
build trust, handle spreadsheet culture, and support adoption
([[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]]).

Dashboard checks, monitoring, and operational visibility matter too
([[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]]).
Dashboards work when the team trusts the definitions,
checks the numbers, and connects the view to a recurring decision.

## Product Analytics and Experiments

Product-facing data analysis often asks how users behave and whether a change
improved the product. That work depends on
[[event tracking]],
[[tracking plans]], and
[[product analytics]]. Analysis starts before the dashboard: teams need
event definitions and properties before they can trust funnels, and source
context and ownership before they can trust activation metrics or anomaly
investigations
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

Experiments ask whether the change caused the metric movement. This is where
product analytics moves into causality, covering randomization, feature
de-risking, assignment tracking, A/A testing, and power analysis
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]).
Product teams can make the wrong decision when results are noisy or underpowered
([[Experimentation]],
[[Experimentation and Causal Inference]]).

This doesn't mean every analysis needs a full statistical test. Simplifying A/B
test reporting for decision makers, low-fidelity prototypes, narrow measurable
wins, and adoption work all make analytics useful
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]).
The analyst's job is to match the analysis method to
the decision, not to make every question look like the same experiment.

## Analysis, Data Science, and Analytics Engineering

Data analysis overlaps with data science, but the center of gravity differs.
Analysts usually explain what happened and why it happened. They also explain
what decision should follow. Data scientists are more likely to own prediction
and modeling. They also tend to own model-backed product decisions
([[Data Scientist Role]]).

Analysts build dashboards and reports and write ad hoc queries and
recommendations, and their work connects to experiment uplift, segment
differences, and root-cause analysis
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

Analytics engineering is another neighboring role. Analysts own the question,
interpretation, and recommendation, while analytics engineers own reusable
models and BI-ready data layers. They also own tests and documentation.

Analytics engineering is grounded in data modeling, pipelines, data quality, and
Looker, and it overlaps with analyst work
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]).
The
[[Data Analyst vs Analytics Engineer]]
page gives the practical boundary. Analysts own decision support. Analytics
engineers own reusable and tested analytical models.

Small teams often blur those boundaries. One analytics engineering role included
product support, A/B testing, Looker dashboards, `dbt`, data modeling, growth
analysis, retention analysis, and RFM analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]]).

For a learner or hiring manager, the title matters less than the ownership.
Ask which decision, model, metric, or data product the person improves.

## Communication and Storytelling

Data analysis becomes useful when someone can understand it and act on it.
That requires writing, visualization, and stakeholder communication. Data
journalism is distinct from broader data science and moves through data
sourcing, storytelling, and visualization, with a preference for one concept per
chart and tables when they're clearer
([[podcast:data-journalism-python-visualization-storytelling|Practical Data Journalism]]).

The same communication standard appears in hiring and team discussions.
Candidates should show clear responsibilities, dates, and practical examples, and
data analyst titles are ambiguous
([[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]).
A resume or portfolio needs to explain the actual
analysis work, not just list tools.

Analytics craft connects to maintainability, documentation, and peer review, as
well as stakeholder conversations with PMs and senior leaders
([[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|Hiring and Managing Data Science Teams]]).
Analysts need statistical care and social trust. People
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

- a product funnel or cohort analysis with a tracking plan, following an
  event-tracking and warehouse flow
  ([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]])
- an experiment readout with a primary metric, guardrails, assignment checks,
  and power discussion
  ([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]])
- a business health dashboard with definitions, monitoring checks, and adoption
  notes
  ([[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]])
- a written analysis or data story that gives each chart a single point and
  explains the data source
  ([[podcast:data-journalism-python-visualization-storytelling|Practical Data Journalism]])

For analysts who want to move toward analytics engineering, add reusable data
models, tests, and documentation. That direction ties to SQL transformations,
version control, tests, and dependency graphs
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]). The
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
