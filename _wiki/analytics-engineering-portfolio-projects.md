---
layout: wiki
title: "Analytics Engineering Portfolio Projects"
summary: "Guidance for analytics engineering portfolio projects that prove SQL modeling, metric ownership, dbt-style tests, documentation, BI readiness, and stakeholder judgment."
related:
  - Portfolio Projects
  - Analytics Engineering
  - Dashboard and Metric Layer Project Checklist
  - Analytics Engineering Roadmap
  - Data Engineering Portfolio Projects
  - Product Analytics
  - Data Quality and Observability
  - Job Search
---

An analytics engineering portfolio project is evidence that a candidate can turn
messy source data into reusable models. It also shows shared metric definitions
and a trusted analytical surface.

The strongest projects go beyond SQL or a dashboard because they explain table
grain and modeled layers. They add tests and BI consumption around those
definitions. They also show the business question behind the model.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
describes analytics engineering as daily work around data modeling, data
quality, dbt transformations, and Looker exposure
([4:05-10:04](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).

This project checklist is one branch of the broader
[Portfolio Projects]({{ '/wiki/portfolio-projects/' | relative_url }}) hub. It
sits beside the broader
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
role page, the
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}),
and the implementation-focused
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }}).
For ingestion, orchestration, and platform-heavy work, use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}).

[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html)
adds the second half of the definition: the model should make business reality
match the data. Engineering discipline should make that representation safer
([Foundations of the Analytics Engineer Role at 11:03 and 46:34](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).

## Reviewable Analytics Project

Across these episodes, a good analytics engineering portfolio project starts with
a repeated business question and ends with a trusted analytical surface. The
repository should make source assumptions and staging models easy to review. It
should also show intermediate logic, marts, tests, and docs. The final
analytical surface should be a dashboard or query layer that consumes shared
models.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
grounds the role in SQL models that analysts and data scientists can use.
Looker is the consumption layer, and dbt is the transformation layer
([4:05-8:59](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).
That makes a dashboard-only project weak unless the dashboard sits on reusable
models. It also makes a dbt-only project weak unless the models answer a
business question and expose definitions to consumers.

[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html)
pushes the definition beyond "between analyst and engineer." He frames the work
as making data reflect business reality. He then adds robustness and
software-engineering discipline
([7:56-16:25 and 46:34](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).
A portfolio should therefore explain why the model represents the business
correctly. It should state what one row means, which joins preserve the grain,
and which caveats stakeholders should know.

[Natalie Kwong](https://datatalks.club/people/nataliekwong.html) places the same
work inside [ETL and ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}). Data
arrives first, and analysts or analytics engineers then transform it with SQL and
dbt and publish data marts or consumption tables
([7:57-18:47 and 31:31](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html)).
That favors projects that show source assumptions and warehouse-side
transformations, even when the portfolio isn't a full data-engineering
project.

## Review Signals

Guests don't disagree that modeling matters, but they place the portfolio
boundary differently. For some guests, the proof is a distinct
analytics-engineer role. For others, it's business modeling,
career-transition evidence, or activation work.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
describes a recognizable analytics-engineer role with modeling and quality.
Looker and dbt are part of that role. So is collaboration with analysts, data
scientists, and backend engineers
([14:34-20:52 and 33:02](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).

[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html)
is more cautious about defining the role only by the gap between analysts and
engineers. His evidence points portfolio builders toward modeling business
reality, testing dashboards, and bringing rigor to data workflows
([7:56-11:03 and 38:41-46:34](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).

[Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) shows a
transition version of the portfolio, and the proof didn't start as a public
repository. It started with marketing reporting and BI-team conversations.
Looker work, SQL practice, and BI projects happened alongside marketing work.
The later role included dbt migration, LookML, product analytics, and A/B
testing
([7:18-23:12 and 38:27](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).
That supports portfolios that turn domain knowledge into modeled metrics
instead of treating domain context as background.

Analysts can use the
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})
to turn dashboard and KPI work into this kind of portfolio.

[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) widens the
project boundary toward [Data Activation]({{ '/wiki/data-activation/' | relative_url }}).
His episode connects tracking plans and event collection with warehouse
transformations and BI. Reverse ETL then sends modeled data to support, sales,
and engagement tools
([13:34-30:03 and 37:25-46:13](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).
For portfolio builders, this makes activation projects legitimate
analytics-engineering evidence when the work documents event ownership, data
meaning, and downstream consequences.

## Metric Mart and Dashboard Project

A metric mart and dashboard project is the clearest portfolio option because it
connects [Metrics]({{ '/wiki/metrics/' | relative_url }}), modeled tables, and
a visible consumption surface. Pick a domain with repeated decisions. Useful
domains include marketing funnels, product usage, business-health reporting,
and finance reporting. Build source models before staging tables, facts,
dimensions, and metric definitions. Then add tests and one documented dashboard
that uses only the modeled layer.

This mirrors [Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
on modeling and Looker exposure
([Master Analytics Engineering at 4:05-8:59](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).
It also mirrors [Tammy Liang](https://datatalks.club/people/tammyliang.html) on
business-health monitoring and streamlined reporting. Her discussion adds
documentation, testing, and adoption workshops
([Building and Scaling a Data Team at 7:22-22:32 and 35:38-49:00](https://datatalks.club/podcast/building-and-scaling-data-team.html)).

For a portfolio, the README should show who uses the dashboard. It should
explain what changed from the old spreadsheet or duplicated query. It should
also show how another analyst finds the definitions.

The project should answer these review questions:

- Business question: name the decision and metric owner. This follows
  [Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) from
  performance marketing into BI and product analytics. Funnels, retention, RFM
  analysis, and A/B testing gave modeling work a target
  ([2:53 and 38:27-41:50](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).
- Row grain: state what one row represents and which joins preserve or change
  that grain, because [Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html)
  ties this modeling question to representing business reality
  ([11:03-20:21](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).
- Modeled layers: separate sources, staging logic, intermediate joins, and
  marts, since [Natalie Kwong](https://datatalks.club/people/nataliekwong.html) distinguishes
  warehouses, transformations, and data marts inside the modern stack
  ([10:00-18:47](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html)).
- Consumption: make the dashboard use shared models instead of embedded
  duplicate metric logic because [Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html)
  connects Looker, LookML, dbt migration, and product analytics in the same
  BI stack
  ([20:34-23:12](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).

## dbt Migration or Refactor Project

A dbt migration or refactor project works when the starting point is messy SQL,
duplicated dashboard logic, or spreadsheet-defined metrics. Refactor the logic
into model layers and add tests, docs, lineage, and a deployment note. Use
reusable macros only where they remove duplication.

[Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html)
grounds this in a real dbt migration and LookML reporting. He also discusses
wide-versus-narrow tables and incrementalization tradeoffs
([18:34-33:46](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).
[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) adds the
[DataOps]({{ '/wiki/dataops/' | relative_url }}) standard for version control
and tests. He also covers CI/CD, runbooks, documentation, and end-to-end
versioning
([33:47-51:21](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).

This project is strongest when it shows before-and-after behavior. Include the
old query or dashboard calculation, the new
[dbt]({{ '/wiki/dbt/' | relative_url }}) model structure, the tests that catch
broken assumptions, and a reconciliation note for stakeholders. That
reconciliation belongs in the portfolio because
[Barr Moses](https://datatalks.club/people/barrmoses.html) connects schema
changes, lineage, ownership, and SLAs to data reliability
([19:10-35:24 and 58:51](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html)).

## Product Analytics and Event Model Project

A product analytics project should start with events, not charts. Write a
tracking plan, then simulate or instrument events. Model user journeys and
publish activation, retention, funnel, or experiment metrics.

[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html)
names signup and project-created events as SaaS examples. Invite and invoice
events fit there too. He then connects collection and storage with
transformation, analysis, and activation
([13:34-30:03](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).
[Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) shows why
marketing and product domain knowledge matter for funnels, retention, RFM, and
A/B testing
([38:27-41:50](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).

This project should connect
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}), and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) through modeled
tables. Document event owners and required properties. Also explain
late-arriving events, user identity rules, and which modeled metrics feed the
dashboard or experiment readout. That source-semantics work follows
[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) on tracking
plans with events, properties, and ownership
([13:34-20:47](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Reverse ETL or Activation Project

A reverse ETL or activation project is useful when the portfolio needs to show
operational consequences. Model a customer or account segment in the warehouse.
Then push it to a mock CRM, support tool, or marketing destination. Document
ownership, refresh cadence, and privacy assumptions. Also explain the
consequence of a wrong segment.

[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) covers
reverse ETL and product-led activation in
[Data-Led Growth Stack at 37:25-56:08](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html).
[Natalie Kwong](https://datatalks.club/people/nataliekwong.html) covers warehouse
tables flowing back into operational systems in
[ETL, ELT, and the Modern Data Stack at 35:42](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html).

For analytics engineering, the important proof isn't the connector. It's that
a trusted modeled segment can safely leave the warehouse. Link the segment to
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}),
[Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}), and the metric or
event definitions that produced it. Include one failure example, such as a
stale trial-status field or a duplicated account. Operational activation makes
wrong analytical definitions visible to sales, support, or lifecycle marketing.

## Hiring-Focused Fundamentals Project

A hiring-focused fundamentals project should go deep on SQL and modeling before
adding tools. [Jeff Katz](https://datatalks.club/people/jeffkatz.html) places an
analytics-engineering module around dbt, Snowflake, Mode, and Fivetran. He also
emphasizes SQL mastery, window functions, OLTP versus OLAP, and sample
database modeling practice
([36:18-45:14](https://datatalks.club/podcast/data-engineering-career-path-and-skills.html)).

The concrete artifact can be a small warehouse model over a sample
transactional database. Show OLTP-to-OLAP modeling and window functions. Then
add dimensional choices and a concise dashboard or query notebook. The
[Data Analysis]({{ '/wiki/data-analysis/' | relative_url }}) guide covers the
analyst-facing side of this evidence, while this page keeps the focus on
reusable modeling and handoff.

Junior candidates can win with a smaller project when the grain definitions and
tests are strong. Docs and SQL explanations can matter more than a broad stack
that hides the modeling decisions. Connect the writeup to
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
when the project explains the move from interpreting a dashboard to owning
reusable analytical models.

## Quality, Documentation, and Handoff

Every portfolio project should be reviewable as if another analyst had to
maintain it next month. That means the repository and dashboard docs should
make quality rules and handoff assumptions visible.

Tests and docs aren't ornamental. Add non-null checks, unique checks, and
accepted-values checks where they match the data rules. Add relationship checks
and freshness checks where they protect consumers. Use custom tests when the
business rule is specific.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
discusses dbt tests and upstream checks. She also covers warnings, errors,
docs, and profiling tools
([36:44-38:53 and 50:46](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).
[Barr Moses](https://datatalks.club/people/barrmoses.html) frames freshness,
volume, distribution, and schema as reliability signals. She then ties lineage,
ownership, and SLAs to data trust
([16:38-35:24 and 58:51](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html)).

Documentation should make owners and purpose visible. It should also make
caveats, columns, dependencies, and example queries findable.
[Tammy Liang](https://datatalks.club/people/tammyliang.html)
uses a Notion wiki plus dashboard checks, and she connects workshops to data
adoption outside the data team
([22:32 and 49:00](https://datatalks.club/podcast/building-and-scaling-data-team.html)).
That links portfolio quality to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}), not just to model count.

## Anti-Patterns

Avoid a dashboard built directly from raw tables with metric logic hidden in
charts. [Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html)
places analytics-engineering value in modeled data, dbt transformations, and
Looker exposure, not in isolated charts
([4:05-8:59](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)).

Avoid a dbt repository with many models but no business definitions, tests,
owners, or BI consumer. [Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html)
argues that the work should map business reality and make the data safer
([11:03 and 46:34](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)).
[Tammy Liang](https://datatalks.club/people/tammyliang.html) shows that adoption,
documentation, and trust matter after the models exist
([22:32 and 49:00](https://datatalks.club/podcast/building-and-scaling-data-team.html)).

Avoid copying a public template without explaining grain, joins, slowly
changing attributes, or incremental logic. [Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html)
grounds the role in practical data-modeling tradeoffs during a dbt migration,
including wide versus narrow tables and incrementalization
([30:28-33:46](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html)).

Avoid final KPI screenshots without source caveats, data-quality checks, or
reconciliation notes. [Barr Moses](https://datatalks.club/people/barrmoses.html)
shows how silent failures, schema changes, freshness, and lineage break trust.
Ownership matters too when teams only look at the final output
([13:40-29:00](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html)).

Avoid treating analytics engineering as "SQL plus dashboard." The podcast
discussions return to software practices and tests, then to docs and lineage.
They also cover version control, warehouse transformations, and adoption. See
[Victoria Perez Mola on dbt tests, documentation, and role fit](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
for the role view. See
[Christopher Bergh on DataOps automation and reliable pipelines](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
and [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
for the workflow view.

## Related Pages

These pages cover the role, stack, and adjacent portfolio context:

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})
- [Data Analysis]({{ '/wiki/data-analysis/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability for Data Engineering]({{ '/wiki/data-observability-for-data-engineering/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})
