---
layout: article
tags: ["guide"]
title: "Data Analysis Guide"
keyword: "data analysis"
summary: "Practical data analysis guide covering SQL, metrics, dashboards, experiments, stakeholder communication, role boundaries, and portfolio evidence."
related_wiki:
  - Data Analyst Role
  - Data Analyst Careers
  - Product Analytics
  - Metrics
  - Experimentation
  - Analytics Engineering
  - Data Products
  - Algorithmic Trading
---

Data analysis is the work of turning data into evidence for a decision. Analysts
first find the right data and check what the
numbers mean. They choose metrics, build dashboards or written readouts, and
explain what a team should do next. It's close to
[[data-analyst-role=>data analyst work]], but the
practice also appears in [[product analytics]]
and [[analytics engineering]].
It also appears in experimentation and data leadership.

An analyst knows what company data exists, retrieves it, and defines KPIs. They
also build dashboards, quantify product problems, and check whether shipped work
changed user behavior[[cite:data-team-roles=>Data Team Roles Explained]].
That makes data analysis more than charting. It moves from question to evidence
to decision
([[Data Analyst Role]]).

## Practical Definition

Practical data analysis starts with the decision, not the tool. A good analysis
asks who will act on the result and which metric will change the decision. It
also asks which data is trustworthy enough to use and which caveats need to be
visible.

Analytics should be outcome-first, with metrics connected to real meetings and
decisions[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Delivery]].
A dashboard that nobody trusts or uses isn't finished analysis.

That outcome-first view also explains why analysts spend time on source data.
Analysts doing product analytics start with tracking plans, event names, event
properties, and ownership. They follow those events through storage,
transformation, BI, and activation[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
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

SQL and dashboarding sit next to KPI definition and product problem sizing[[cite:data-team-roles=>Data Team Roles]].

SQL and data visualization are analyst fundamentals, alongside cohort analysis
and retention metrics[[cite:teaching-mentoring-data-analytics-fintech=>FinTech Analytics Curriculum]].

Metrics are the bridge between data and action. The
[[Metrics]] wiki page defines them as
decision rules expressed as numbers. That's more useful than treating metrics
as dashboard fields. A subscription-versus-points experiment can tell different
stories. The interpretation changes when the team measures revenue, conversion,
retention, or long-term value[[cite:ab-testing-and-product-experimentation=>Product A/B Testing]].

Analysts often deliver dashboards, but they shouldn't stop there. Business health
dashboards can come first, but the team still has to streamline reporting and
build trust. Teams also have to handle spreadsheet culture and support
adoption[[cite:building-and-scaling-data-team=>Scaling a Data Team]].

Dashboard checks, monitoring, and operational visibility matter too[[cite:building-and-scaling-data-team=>Scaling a Data Team]].
Dashboards work when the team trusts the definitions,
checks the numbers, and connects the view to a recurring decision.

## Product Analytics and Experiments

Product-facing data analysis often asks how users behave and whether a change
improved the product. That work depends on
[[event tracking]],
[[tracking plans]], and
[[product analytics]]. Analysis starts before the dashboard. Teams need
event definitions and properties before they can trust funnels. They also need
source context and ownership before they can trust activation metrics or anomaly
investigations[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].

Experiments ask whether the change caused the metric movement. At that point,
product analytics moves into causality through randomization, feature
de-risking, and assignment tracking. Experiment work also covers A/A testing and power
analysis[[cite:ab-testing-and-product-experimentation=>Product A/B Testing]].
Product teams can make the wrong decision when results are noisy or underpowered
([[Experimentation]],
[[Experimentation and Causal Inference]]).

This doesn't mean every analysis needs a full statistical test. Simplifying A/B
test reporting for decision makers can make analytics useful. So can
low-fidelity prototypes, narrow measurable wins, and adoption work[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Delivery]].
The analyst's job is to match the analysis method to
the decision, not to make every question look like the same experiment.

## Analysis, Data Science, and Analytics Engineering

Data analysis overlaps with data science, but the center of gravity differs.
Analysts usually explain what happened and why it happened. They also explain
what decision should follow. Data scientists are more likely to own prediction
and modeling. They also tend to own model-backed product decisions
([[Data Scientist Role]]).

Analysts build dashboards and reports, write ad hoc queries, and turn findings
into recommendations. Their work connects to experiment uplift, segment
differences, and root-cause analysis[[cite:production-ml-mlops-and-data-team-building=>Analytics to Production ML]].

Analytics engineering is another neighboring role. Analysts own the question,
interpretation, and recommendation, while analytics engineers own reusable
models and BI-ready data layers. They also own tests and documentation.

Analytics engineering is grounded in data modeling, pipelines, and data quality.
It also uses Looker and overlaps with analyst work[[cite:analytics-engineer-skills-tools=>Analytics Engineering]].
The
[[Data Analyst vs Analytics Engineer]]
page gives the practical boundary. Analysts own decision support. Analytics
engineers own reusable and tested analytical models.

Small teams often blur those boundaries. One analytics engineering role included
product support, A/B testing, Looker dashboards, and `dbt`. It also included
data modeling, growth analysis, retention analysis, and
[[RFM Analysis]][[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].
Teams use that customer segmentation by defining the customer grain, measuring
behavior, and explaining which retention or growth decision should follow.

For a learner or hiring manager, the title matters less than the ownership.
Ask which decision, model, metric, or data product the person improves.

## Communication and Storytelling

Data analysis becomes useful when someone can understand it and act on it.
That requires writing, visualization, and stakeholder communication. Data
journalism is distinct from broader data science. It moves through data
sourcing, storytelling, and visualization. In that episode, the advice is to keep
one concept per chart and use tables when they're clearer[[cite:data-journalism-python-visualization-storytelling=>Data Journalism]].

The same communication standard appears in hiring and team discussions.
Candidates should show clear responsibilities, dates, and practical examples.
Data analyst titles are ambiguous[[cite:hiring-data-scientists-and-analysts=>Hiring Analysts]].
A resume or portfolio needs to explain the actual
analysis work, not just list tools.

Analysts also need maintainability, documentation, and peer review. They need
stakeholder conversations with PMs and senior leaders too[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>Managing Data Science Teams]].
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

Useful project shapes include:

- a product funnel or cohort analysis with a tracking plan, following an
  event-tracking and warehouse flow[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
- a [[algorithmic-trading=>Python stock analysis]] project that starts from
  OHLCV market data and a trading target. The backtest should follow time order
  instead of treating rows as shuffled examples
  [[cite:algorithmic-trading-with-python-and-machine-learning=>Algorithmic Trading with Python]].
- an experiment readout with a primary metric, guardrails, assignment checks,
  and power discussion[[cite:ab-testing-and-product-experimentation=>Product A/B Testing]].
- a business health dashboard with definitions, monitoring checks, and adoption
  notes[[cite:building-and-scaling-data-team=>Scaling a Data Team]].
- a written analysis or data story that gives each chart a single point and
  explains the data source[[cite:data-journalism-python-visualization-storytelling=>Data Journalism]].

For analysts who want to move toward analytics engineering, add reusable data
models, tests, and documentation. That direction ties to SQL transformations and
version control. It also ties to tests and dependency graphs[[cite:analytics-engineer-skills-tools=>Analytics Engineering]].
The
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
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
