---
layout: wiki
title: "Marketing to Analytics Engineering"
summary: "Podcast-backed transition notes for marketers moving into analytics engineering through SQL, BI, dbt, product analytics, dashboards, and metric ownership."
related:
  - Career Transition
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Product Analytics
  - dbt
---

Marketing to analytics engineering moves campaign and growth questions toward
the modeled data behind those questions. The clearest archive example is
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) moving
from performance marketing into BI and analytics engineering at Ecosia. Her
path starts with marketing reporting and Looker work. It then passes through
SQL and BI projects. Data-pipeline literacy, dbt modeling, and product
analytics support follow
([marketing-to-analytics episode at 2:53-14:14]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The move builds on adjacent domain knowledge. Marketing gives the candidate
familiarity with acquisition, conversion, audience splits, and stakeholder
pressure. [Analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
adds reusable SQL models, tests, documentation, and BI-ready tables. It also
adds shared metric definitions.

The transition works when marketing context becomes technical evidence. A
dashboard becomes a governed model, and a campaign report becomes a metric
definition. Funnel intuition becomes
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) work
([marketing-to-analytics episode at 18:34-39:36]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

## Link Map

Start with these podcast discussions:

- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}) is the core transition episode. Maksimovic covers performance marketing, the marketing-analyst bridge, BI conversations, SQL, pipelines, Looker, dbt, product analytics, A/B testing, mentorship, and the Excel-to-SQL-to-dashboard path.
- [Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}) defines the target role through data modeling, dbt tests, Looker, Snowflake, SQL, DAGs, and collaboration.
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}) treats analytics engineering as translating messy business reality into safer data systems rather than only sitting between analyst and engineer.
- [ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) places dbt and warehouse-side transformations inside the broader modern data stack.
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) connects event tracking, tracking plans, BI, warehouse transformations, customer data platforms, and reverse ETL to growth work.
- [Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }}) shows how early analytics work can grow into dashboards, warehouses, dbt, documentation, tests, and adoption work in a small team.

People connected to the cited interviews:

- [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
- [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
- [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
- [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
- [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
- [Tammy Liang]({{ '/people/tammyliang/' | relative_url }})

Adjacent pages:

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})

## Common Route

Marketing reporting creates the opening, and internal BI work creates the
bridge. Analytics engineering becomes the target once the person can maintain
reusable models. Maksimovic first valued performance marketing because it gave
fast feedback on whether work was effective. When Ecosia moved to Looker, she
helped build marketing-team reporting. She already understood the team's
numbers and questions
([marketing-to-analytics episode at 2:53 and 7:18]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The transition then became explicit through conversations with the BI team.
Maksimovic describes the first intended bridge as a marketing-analyst role. The
required skills pointed toward BI work. SQL was the main gap, with
data-pipeline understanding and Python basics behind it.

She also describes having to read and write more complex SQL. Larger data
models mattered too, not just beginner queries
([marketing-to-analytics episode at 8:45-12:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The final step is ownership of modeled analytical assets. Maksimovic's later
work included KPIs, dashboards, and product-team experiment support. It also
included a dbt migration and wide-versus-narrow data-modeling tradeoffs. The
stack included Looker, LookML, and Redshift. Airflow, Airbyte, and Snowplow
also appear in the tooling discussion
([marketing-to-analytics episode at 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

That matches the broader analytics-engineering role described by
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}).
Her episode ties the job to SQL transformations, dbt tests, and documentation.
DAGs and BI collaboration matter too
([analytics-engineer skills episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Guest Differences

Guests differ on how formal the role boundary should be. Maksimovic's team did
not start with a clean analytics-engineer title. The work overlapped BI analyst,
data analyst, and analytics engineer responsibilities, especially because the
team was small
([marketing-to-analytics episode at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) also
warns that "between analyst and engineer" is an incomplete definition. His
foundations episode emphasizes business reality, data modeling, software
engineering practice, and safer analytical systems
([foundations episode]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also differ on tool centrality. Maksimovic says dbt strongly shaped the
analytics-engineering title, but she still separates the role from the tool.
Data modeling theory matters more than simply using dbt
([marketing-to-analytics episode at 28:40-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places dbt inside
a broader ELT flow. Ingestion, warehouses, and orchestration keep the
transition connected to the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
([modern-data-stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

The growth-oriented episodes add a second boundary difference. For
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}), the
marketing-adjacent data path extends beyond dashboards. It includes event
tracking, tracking plans, and warehouse transformations. It also includes BI,
CDPs, and reverse ETL.
That
makes the marketing-to-analytics transition especially useful for people who
want to specialize in [data-led growth]({{ '/wiki/data-led-growth/' | relative_url }})
or [data activation]({{ '/wiki/data-activation/' | relative_url }})
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Transferable Marketing Context

The strongest transferable skill is knowing what a funnel means before writing
the model. Maksimovic explicitly names comfort with marketing funnels,
conversion funnels, and web acquisition funnels. She also names user journeys
and touch points, plus the pressure to optimize and grow.

That background helped her support product managers and growth work. She could
keep the user journey in view while building analytical outputs
([marketing-to-analytics episode at 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

This domain knowledge maps directly to [product analytics]({{ '/wiki/product-analytics/' | relative_url }}).
Maksimovic's analytics-engineering work included growth analysis, retention
analysis, RFM analysis, and NLP experiments. It also included dashboards and
A/B testing support
([marketing-to-analytics episode at 14:14 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
Choudhury's growth-stack episode explains why those questions need event names,
properties, source context, and ownership rules. They also need warehouses, BI,
and activation tools, not only a campaign dashboard
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Marketing context alone won't meet that bar. Perez Mola's role episode centers
analytics engineering on data modeling and quality checks. It also names
pipelines, Looker, dbt, and Snowflake. SQL, DAGs, and collaboration matter too
([analytics-engineer skills episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

This transition therefore belongs with
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}).
Marketing experience helps with questions and definitions. Analytics
engineering requires maintained models that other people can reuse.

## Technical Learning Path

Maksimovic's learning path puts Excel and pivot tables before SQL datasets.
Real company queries help move the learner beyond beginner examples. She also
recommends building dashboards in Looker or Tableau so the
learner sees how modeled data becomes stakeholder-facing reporting
([marketing-to-analytics episode at 41:50-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The next layer is data modeling. Maksimovic learned it through the dbt
migration, where the work covered transformations and model organization. It
also covered wide-versus-narrow tables and incrementalization tradeoffs
([marketing-to-analytics episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
That aligns with the [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}),
which moves from analytical SQL to reusable models and tests. Documentation,
metric ownership, and domain specialization follow.

Pipeline literacy is a real requirement, but the marketing path in this archive
is SQL-first rather than Python-first. Maksimovic names SQL as the main skill,
then pipeline understanding and Python basics as supporting gaps
([marketing-to-analytics episode at 9:53-12:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
Kwong's modern-stack episode adds the surrounding system. That system includes
ingestion, warehouse storage, dbt transformations, and orchestration. It also
includes CDC and reverse flows
([modern-data-stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Portfolio and Internal Proof

The archive favors internal proof when it's available. Maksimovic didn't jump
directly from marketing into an external analytics-engineering role. She used
marketing reporting, a Looker migration, BI-team conversations, and BI projects
alongside marketing work to prove the transition
([marketing-to-analytics episode at 7:18-14:14 and 23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

For an external portfolio, the same evidence should be made visible. A strong
marketing-to-analytics project should define campaign or product events. It
should model funnel or retention tables, document metric grain, add dbt-style
tests, and publish a dashboard from shared models.

That standard comes from Maksimovic's dbt, Looker, product analytics, and
modeling work. It also comes from Perez Mola's emphasis on dbt tests and
documentation
([marketing-to-analytics episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[analytics-engineer skills episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Good project themes for this transition include these options:

- a campaign reporting mart
- a web-acquisition funnel model
- a retention or RFM model
- an A/B testing readout model
- a dbt migration from duplicated dashboard SQL
- a reverse-ETL segment project

These fit the podcast evidence because Maksimovic covers marketing funnels and
product support. Her episode also covers A/B testing and RFM analysis. dbt
modeling and Looker appear there too. Choudhury connects modeled growth
data to activation workflows
([marketing-to-analytics episode at 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

## Sponsorship and Team Structure

The transition is easier when the existing organization has a BI or data team
that can sponsor practical work. Maksimovic describes conversations with a BI
colleague and a BI analyst who helped her learn Looker. She also describes
later teammates who served as mentors once she joined the BI team
([marketing-to-analytics episode at 9:53 and 45:09-50:23]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
That makes this path a strong fit for marketers in companies with existing
reporting needs. Dashboard migration, dbt adoption, and product analytics needs
also create openings.

Small-team environments can blur the role boundary. Maksimovic's BI team was
small enough that people did both analysis and analytics-engineering work
([marketing-to-analytics episode at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) gives a related team
growth example. Dashboards and business-health monitoring grew into a
warehouse, dbt, Data Studio, and Notion documentation. Testing, monitoring,
forecasting, and adoption work followed
([building-and-scaling-data-team episode]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

## Related Pages

Use these pages for the role, stack, and adjacent transition context.

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
- [Analytics Engineer article]({{ '/articles/analytics-engineer/' | relative_url }})
