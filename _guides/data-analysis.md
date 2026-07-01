---
layout: article
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
DataTalks.Club archive, analysts first find the right data and check what the
numbers mean. They choose metrics, build dashboards or written readouts, and
explain what a team should do next. It's close to
[data analyst work]({{ '/wiki/data-analyst-role/' | relative_url }}), but the
practice also appears in [product analytics]({{ '/wiki/product-analytics/' | relative_url }})
and [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
It also appears in experimentation and data leadership.

In [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst knows what company data exists. They retrieve it and define KPIs.
They also build dashboards, quantify product problems, and check whether
shipped work changed user behavior around 7:51-10:39. That makes data analysis
more than charting. It's a loop from question to evidence to decision
([Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})).

## Practical Definition

Practical data analysis starts with the decision, not the tool. A good analysis
asks who will act on the result and which metric will change the decision. It
also asks which data is trustworthy enough to use and which caveats need to be
visible.

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) makes this
point in
[Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}).
She argues for outcome-first analytics around 34:00, then connects metrics to
real meetings and decisions around 38:15. A dashboard that nobody trusts or
uses isn't finished analysis.

That outcome-first view also explains why analysts spend time on source data.
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) shows the
product analytics version in
[How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
He starts with tracking plans, event names, event properties, and ownership
around 13:34-18:27. He then follows events through storage, transformation, BI,
and activation around 22:50-41:30. A funnel or retention chart is only useful
when the analyst knows how the underlying events were captured.

For career planning, "data analysis" isn't a narrow task. Analysts can work
on ad hoc SQL, dashboard design, cohort analysis, and experiment readouts. They
can also own metric definitions, stakeholder interviews, and written
recommendations. The
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
page collects the career side of that work.

## SQL, Metrics, and Dashboards

SQL is the usual base skill because analysts need command of the tables before
they can explain what happened. They use SQL to join data, filter records,
aggregate rows, and check assumptions.

In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
SQL and dashboarding sit next to KPI definition and product problem sizing.

In
[Designing FinTech Data Analytics Curriculum]({{ '/podcasts/teaching-mentoring-data-analytics-fintech/' | relative_url }}),
[Irina Brudaru]({{ '/people/irinabrudaru/' | relative_url }}) names SQL and
data visualization as analyst fundamentals around 58:08. Cohort analysis and
retention metrics appear earlier around 31:50.

Metrics are the bridge between data and action. The
[Metrics]({{ '/wiki/metrics/' | relative_url }}) wiki page defines them as
decision rules expressed as numbers. That's more useful than treating metrics
as dashboard fields. [Jakob Graff]({{ '/people/jakobgraff/' | relative_url }})
shows why in
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}):
a subscription-versus-points experiment can tell different stories. The
interpretation changes when the team measures revenue, conversion, retention,
or long-term value around 14:27-18:06.

Analysts often deliver dashboards, but they shouldn't stop there.
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) describes building
business health dashboards first in
[Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})
around 7:22. The team then had to streamline reporting and build trust. They
also had to handle spreadsheet culture and support adoption around 8:51-10:06.

Liang later discusses dashboard checks, monitoring, and operational visibility
around 40:09-41:42. Dashboards work when the team trusts the definitions,
checks the numbers, and connects the view to a recurring decision.

## Product Analytics and Experiments

Product-facing data analysis often asks how users behave and whether a change
improved the product. That work depends on
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}). Arpit's
growth-stack episode shows why analysis starts before the dashboard. Teams need
event definitions and properties before they can trust funnels. They also need
source context and ownership before they can trust activation metrics or anomaly
investigations
([data-led growth at 13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Experiments ask whether the change caused the metric movement.
Jakob's A/B testing episode moves from product analytics into causality. He
covers randomization around 8:13 and feature de-risking around 18:06. He then
covers assignment tracking around 24:44, A/A testing around 27:52, and power
analysis around 37:44. Product teams can make the wrong decision when results
are noisy or underpowered
([Experimentation]({{ '/wiki/experimentation/' | relative_url }}),
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})).

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
([Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})).

In
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
analysts as people who build dashboards and reports. They also write ad hoc
queries and recommendations around 18:39-24:23. He then connects analysts to experiment
uplift, segment differences, and root-cause analysis around 31:19-33:30.

Analytics engineering is another neighboring role. Analysts own the question,
interpretation, and recommendation, while analytics engineers own reusable
models and BI-ready data layers. They also own tests and documentation.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
grounds analytics engineering in data modeling, pipelines, data quality, and
Looker in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
around 4:05-10:04. She also explains the overlap with analysts around
14:34-16:54. The
[Data Analyst vs Analytics Engineer]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
page gives the practical boundary. Analysts own decision support. Analytics
engineers own reusable and tested analytical models.

Small teams often blur those boundaries.
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
describes an analytics engineering role that included product support and
A/B testing. The same role included Looker dashboards, `dbt`, and data
modeling. It also included growth analysis, retention analysis, and RFM
analysis
([marketing to analytics engineering at 14:14-39:36]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

For a learner or hiring manager, the title matters less than the ownership.
Ask which decision, model, metric, or data product the person improves.

## Communication and Storytelling

Data analysis becomes useful when someone can understand it and act on it.
That requires writing, visualization, and stakeholder communication. In
[Practical Data Journalism]({{ '/podcasts/data-journalism-python-visualization-storytelling/' | relative_url }}),
[Angelica Lo Duca]({{ '/people/angelicaloduca/' | relative_url }}) distinguishes
data journalism from broader data science around 8:01. She then moves into
data sourcing, storytelling, and visualization. Around 36:20, she recommends
one concept per chart and tables when they're clearer.

The same communication standard appears in hiring and team discussions.
[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }}) says in
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }})
that candidates should show clear responsibilities, dates, and practical
examples around 28:41-32:40. Around 54:09-59:30, she also warns that data
analyst titles are ambiguous. A resume or portfolio needs to explain the actual
analysis work, not just list tools.

[Katie Bauer]({{ '/people/katiebauer/' | relative_url }}) brings the team
quality view in
[Hiring and Managing Data Science Teams]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }}).
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
([Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }}),
[Job Search]({{ '/wiki/job-search/' | relative_url }})).

Good project shapes follow the podcast evidence:

- a product funnel or cohort analysis with a tracking plan, based on Arpit's
  event-tracking and warehouse flow
  ([data-led growth at 13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}))
- an experiment readout with a primary metric, guardrails, assignment checks,
  and power discussion, based on Jakob's A/B testing workflow
  ([A/B testing at 24:44-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}))
- a business health dashboard with definitions, monitoring checks, and adoption
  notes, based on Tammy's data team buildout
  ([building a data team at 7:22-10:06 and 40:09-41:42]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }}))
- a written analysis or data story that gives each chart a single point and
  explains the data source, based on Angelica's data journalism workflow
  ([data journalism at 29:19-40:47]({{ '/podcasts/data-journalism-python-visualization-storytelling/' | relative_url }}))

For analysts who want to move toward analytics engineering, add reusable data
models, tests, and documentation. Perez Mola's role episode ties that direction
to SQL transformations and version control. It also ties the path to tests and
dependency graphs around 6:49-10:04. The
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
turns that move into a learning and project sequence.

For analysts who want to move toward data science, add prediction, evaluation,
and experiment interpretation. Then
connect those choices to the
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }}) and
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).

The practical standard is simple: show that you can move from messy data and an
ambiguous question to a trustworthy recommendation. That's the useful core of
data analysis. The final artifact can be a SQL query, a dashboard, an
experiment memo, or a stakeholder presentation.
