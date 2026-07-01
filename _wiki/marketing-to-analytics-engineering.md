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
  - Business Intelligence
  - Dashboard and Metric Layer Project Checklist
  - Data Analyst Role
  - A/B Testing
  - Data Warehouse
---

Marketing to analytics engineering moves campaign and growth questions into the
modeled data behind those questions.
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) moving from
performance marketing into BI and analytics engineering at Ecosia. Her path
starts with marketing reporting and Looker work. It then moves through SQL and
BI projects. Pipeline literacy, dbt modeling, and product analytics support
follow
([marketing-to-analytics episode at 2:53-14:14]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The transition isn't a generic switch from "business" to "technical" work.
Marketing gives the person knowledge of acquisition and conversion. It also
adds user-journey context and campaign pressure.

[Analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
adds reusable SQL models, tests, documentation, and BI-ready definitions. The
transition works through a specific change. A campaign report becomes a
maintained model. Funnel intuition becomes
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) or
[data-led growth]({{ '/wiki/data-led-growth/' | relative_url }}) work
([marketing-to-analytics episode at 18:34-39:36]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[data-led growth episode at 13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Common Definition

Marketing to analytics engineering means using marketing domain knowledge as
the entry point into governed analytical data. The marketer already understands
acquisition and activation. They also understand why retention, segments, and
experiments matter. The learner must
turn those questions into reusable tables, tested transformations, documented
metrics, and dashboards that other teams can trust.

Maksimovic's common route started with marketing reporting during a Looker move.
She then explored a marketing-analyst bridge with the BI team. SQL was the main
gap, while pipeline understanding, Python basics, and practice with larger data
models followed
([marketing-to-analytics episode at 7:18-12:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes the target role through SQL transformations and dbt tests. She also
names documentation and DAGs. Her tool examples include Looker and Snowflake,
and she emphasizes collaboration
([analytics-engineer skills episode at 4:05-11:48 and 33:02-36:44]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

That role definition puts the transition next to
[Data Analyst vs Analytics Engineer]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
and the [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).
The broader analyst path is covered in
[Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }}).
Marketing knowledge helps with questions and metric meaning. Analytics
engineering adds ownership of models, quality checks, and shared analytical
assets.

## Role Boundaries and Tradeoffs

Guests differ on how formal the role boundary should be. Maksimovic's team did
not start with a clean analytics-engineer title. The work overlapped BI
analyst, data analyst, and analytics-engineer responsibilities. Small team size
made the boundary blur
([marketing-to-analytics episode at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
pushes against defining analytics engineering only as a role between analyst
and engineer. His foundations episode starts from messy business reality. It
then connects that work to safer data systems, data modeling, and software
engineering practice
([foundations episode at 5:10-16:08 and 25:50-33:52]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also differ on tool centrality: Maksimovic says dbt strongly shaped the
analytics-engineering title, but she still separates the role from the tool.
Data modeling theory matters more than simply using dbt
([marketing-to-analytics episode at 28:40-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places dbt inside
a broader [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
with ingestion and warehouse storage. Orchestration, CDC, and reverse flows
remain part of the same system
([modern-stack episode at 15:30-30:59 and 49:10-58:32]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) adds a
growth-data boundary. In his data-led-growth episode, marketing-adjacent data
work extends beyond dashboards. It includes event tracking and tracking plans.
It also includes BI, warehouse transformations, customer data platforms, and
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
([data-led growth episode at 13:34-44:24]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
That makes the transition useful for people who want to specialize in
[data activation]({{ '/wiki/data-activation/' | relative_url }}) as well as BI.

## Start With Marketing Reporting

The bridge usually begins with reporting that's already close to marketing
work. Maksimovic valued performance marketing because it gave fast feedback on
whether work was effective. When Ecosia moved to Looker, she helped build
marketing-team reporting and already understood the team's numbers and
questions
([marketing-to-analytics episode at 2:53 and 7:18]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

That first step matters: it turns domain knowledge into visible data work. A
marketer can start by cleaning up a campaign report. They can also clarify
funnel definitions or translate repeated dashboard logic into a shared query.
In Maksimovic's case, BI-team conversations and BI projects happened alongside
marketing work. They became proof that she could move from reporting into a
data role
([marketing-to-analytics episode at 9:53-14:14 and 23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Her first reusable data work was marketing reporting during the
Tableau-to-Looker migration. It also included brand-campaign measurement and
dashboard work while she was still close to marketing. That connects the
transition to [Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
and the
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }}),
not only to analytics-engineering titles.

## Build SQL, BI, and Modeling Skill

The technical path is SQL-first. Maksimovic names SQL as the main skill gap,
then adds pipeline understanding and Python basics. She also
describes the need to read and write more complex SQL over larger models, not
only beginner queries
([marketing-to-analytics episode at 8:45-12:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

BI work turns those queries into user-facing evidence. Maksimovic recommends
moving from Excel and pivot tables into SQL datasets, then building dashboards
in tools such as Looker or Tableau. That order lets a learner see how modeled
data becomes stakeholder reporting
([marketing-to-analytics episode at 41:50-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
She also warns that generic SQL exercises leave a gap. Reading real BI-team SQL
that builds main tables is stronger practice when a company can share it.

Model ownership is the next step because Maksimovic's dbt migration covered
transformations and model organization. It also covered wide-versus-narrow
tables and incrementalization tradeoffs.

Victoria ties the role to Looker and LookML. She also covers how warehouse
tooling, orchestration and ingestion fit the stack
([marketing-to-analytics episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
Kwong's modern-stack discussion explains why those skills sit inside an ELT
system. Ingestion and warehouse transformations are part of that system.
Orchestration and reverse flows are part of it too
([modern-stack episode at 15:30-30:59 and 49:10-58:32]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Transfer Funnel Knowledge Into Product Analytics

Marketing context transfers best when the person knows what a funnel means
before writing the model. Maksimovic names marketing funnels, conversion
funnels, and web acquisition funnels as useful prior knowledge. She also names
user journeys, touch points, optimization, and growth. That background helped
her support product managers and keep the user journey visible while building
analytical outputs
([marketing-to-analytics episode at 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Her analytics-engineering work then extended into growth analysis, retention
analysis, and RFM analysis. It also included NLP experiments, dashboards, and
A/B testing support
([marketing-to-analytics episode at 14:14 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

That makes [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[Experimentation]({{ '/wiki/experimentation/' | relative_url }}) direct
adjacent topics for this transition.
Choudhury's growth-stack episode shows why this work needs reliable event
names and properties. It also needs source context and owners. Warehouse
storage, BI, and activation tools matter too, not only a campaign dashboard
([data-led growth episode at 13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

That's the practical connection to [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[Metrics]({{ '/wiki/metrics/' | relative_url }}). The marketer's advantage is
knowing the business question. The analytics-engineering requirement is making
the answer reusable and trustworthy.

## Prove the Transition With Internal Work or Portfolio Projects

Maksimovic used internal proof instead of jumping directly from marketing into
an external analytics-engineering role. Marketing reporting and the Looker
migration showed the transition in the same organization. BI-team conversations,
BI projects, and product analytics work also mattered
([marketing-to-analytics episode at 7:18-14:14 and 23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

An external [analytics-engineering portfolio]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
should make the same evidence visible.

Project examples include:

- a campaign reporting mart
- a web acquisition funnel model
- a retention or RFM model
- an A/B testing readout
- a dbt migration from duplicated dashboard SQL
- a reverse-ETL segment project

These projects fit the transition when they define the grain and document
metric logic. They also need dbt-style tests. BI outputs should come from shared
models
([marketing-to-analytics episode at 18:34-33:46 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[analytics-engineer skills episode at 4:05-11:48 and 33:02-36:44]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[data-led growth episode at 37:25-44:24]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

The strongest project artifact shows the before-and-after. Show the duplicated
campaign or brand-dashboard SQL, then show the modeled table or dbt layer that
replaced it. Include the metric grain and the BI surface that consumes it.

## Find Sponsorship and Team Structure

The transition is easier when an existing BI or data team can sponsor practical
work. Maksimovic describes conversations with a BI colleague and a BI analyst
who helped her learn Looker. Later teammates served as mentors once she joined
the BI team
([marketing-to-analytics episode at 9:53 and 45:09-50:23]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
That makes dashboard migration, dbt adoption, and product analytics support
useful openings for marketers already inside companies with reporting needs.

Small teams can blur role boundaries. Maksimovic's BI team was small enough
that people did both analysis and analytics-engineering work
([marketing-to-analytics episode at 25:06-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) gives a related team
growth example for marketers already near business reporting. Dashboards and
business-health monitoring grew into warehouse and dbt work. Data Studio and
Notion documentation came next, followed by testing and monitoring
([building-and-scaling-data-team episode at 9:02-23:38]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

## Related Pages

Continue through the role, stack, and transition pages that this path depends
on:

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/roadmaps/data-analyst-to-analytics-engineer/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
