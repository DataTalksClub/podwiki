---
layout: wiki
title: "Analytics Engineering Portfolio Projects"
summary: "Archive-backed guidance for analytics engineering portfolio projects that prove SQL modeling, metric ownership, dbt-style tests, documentation, BI readiness, and stakeholder judgment."
related:
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Data Analyst vs Analytics Engineer
  - Data Engineering Portfolio Projects
  - Product Analytics
  - Data Quality and Observability
  - Job Search
---

## Definition

An analytics engineering portfolio project should prove that you can turn messy
source data into reusable models and shared metric definitions. The strongest
projects show more than SQL or a dashboard. They show table grain, modeled
layers, and tests. They show documentation and BI consumption too. They also
show the business question behind the model.

The DataTalks.Club analytics-engineering episodes set that bar.
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes daily work around data modeling and data quality. Pipelines and
Looker exposure are part of the same job.
She also describes dbt handling SQL transformations and tests. Documentation
and dependency graphs belong in that workflow too
([Master Analytics Engineering at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
adds that analytics engineering should make business reality match the data.
Engineering discipline then makes the result safer
([Foundations of the Analytics Engineer Role at 11:03 and 46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Use this page for portfolios aimed at
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
BI-heavy data roles, and analyst-to-engineer transitions. For ingestion,
orchestration, and platform-heavy work, use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}).
For learning order, use
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).

## Link Map

Start with these role and project pages:

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
  for the role definition.
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
  for sequencing SQL, modeling, dbt, and testing.
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
  for the boundary between dashboard interpretation and reusable model
  ownership.
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
  for a transition path through BI, Looker, SQL, and dbt. It also covers
  product analytics and funnels.
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
  [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}), and
  [dbt]({{ '/wiki/dbt/' | relative_url }}) for the stack behind project choices.
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
  [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
  [Metrics]({{ '/wiki/metrics/' | relative_url }}), and
  [Data Activation]({{ '/wiki/data-activation/' | relative_url }}) for
  growth and product-oriented projects.
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for tests, alerts,
  lineage, and run behavior.

The main podcast anchors are:

- [Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
  with [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
  for data modeling, Looker, dbt, and tests. It also covers docs, DAGs, and
  role-fit signals.
- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})
  with [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
  for BI projects, dbt migration, LookML, and product analytics. It also covers
  A/B testing and wide-versus-narrow modeling tradeoffs.
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})
  with [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
  for business-reality modeling, testing dashboards, and software-engineering
  rigor.
- [ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
  with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) for
  ELT, data marts, warehouses, and dbt. It also covers orchestration, CDC, and
  reverse flows.
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})
  with [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
  for tracking plans, event semantics, warehouse transformations, and BI. It
  also covers reverse ETL.
- [Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})
  with [Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) for business
  health dashboards, dbt, documentation, and testing. It also covers monitoring
  and adoption.
- [Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
  with [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) for SQL mastery,
  OLTP versus OLAP, and modeling practice. The analytics-engineering module
  uses dbt, Snowflake, Mode, and Fivetran.

## Common Definition

Across the archive, a good analytics engineering portfolio project starts with
a repeated business question and ends with a trusted analytical surface. The
repository should make the path easy to review. Show raw source assumptions and
staging models. Add intermediate logic, marts, tests, and docs. Then show a
dashboard or query layer that consumes the shared models.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
grounds the role in SQL models that analysts and data scientists can use.
Looker is the consumption layer, and dbt is the transformation layer
([4:05-8:59]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
That makes a dashboard-only project weak unless the dashboard sits on reusable
models. It also makes a dbt-only project weak unless the models answer a
business question and expose definitions to consumers.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
pushes the definition beyond "between analyst and engineer." He frames the
work as making data reflect business reality, then adding robustness and
software-engineering discipline
([7:56-16:25 and 46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
A portfolio should therefore explain why the model represents the business
correctly. It should state what one row means and which joins preserve the
grain. It should also name accepted edge cases and caveats for stakeholders.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places the same
work inside ELT. Data arrives first, then analysts or analytics engineers
transform it with SQL and dbt. They publish data marts and consumption tables
([7:57-18:47 and 31:31]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
That evidence favors projects that show both source ingestion assumptions and
warehouse-side transformations, even when the portfolio isn't a full
data-engineering project.

## Guest Differences

Guests differ on whether the portfolio should sell a distinct job title or a
way of working. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes a recognizable analytics-engineer role with modeling, quality,
Looker, and dbt. The role also collaborates with analysts, data scientists, and
backend engineers
([14:34-20:52 and 33:02]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
is more cautious about defining the role only by the gap between analysts and
engineers. His evidence points portfolio builders toward the craft: modeling
business reality and testing dashboards. Rigor in data workflows matters too
([7:56-11:03 and 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows a
transition version of the portfolio, and the proof didn't start as a public
repository. It started with marketing reporting, BI-team conversations, and
Looker work. SQL practice and BI projects happened alongside marketing work.
The later role
included dbt migration, LookML, product analytics, and A/B testing
([7:18-23:12 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

That evidence supports portfolios that turn domain knowledge into modeled
metrics instead of treating domain context as background.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) widens the
project boundary toward growth systems. His episode connects tracking plans,
event collection, warehouse transformations, and BI to activation work. Reverse
ETL then sends modeled data to support, sales, and engagement tools
([13:34-30:03 and 37:25-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
That makes activation projects legitimate analytics-engineering evidence when
you document event ownership, data meaning, and downstream consequences.

## Project Evidence

A strong project makes the analytical promise visible. Start with a consumer
such as a growth manager, finance stakeholder, operations team, or product
manager. Then show how the modeled data supports that decision.

[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) gives a useful
adoption test. Her first data-team work focused on business-health monitoring,
streamlined reporting, and rebuilding trust. The stack later included Stitch,
GCP, dbt, and Data Studio. A Notion wiki documented the work. The team then
added testing, monitoring, and workshops for adoption
([7:22-22:32 and 35:38-49:00]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

For a portfolio, the README shouldn't stop at "here's the dashboard." It should
show who uses the dashboard and what changed from the old spreadsheet or
duplicated query. It should also show how another analyst finds the definitions.

The minimum evidence set is:

- Business question: name the decision and the metric owner. This follows
  [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) from
  performance marketing into BI and product analytics. Funnels, retention, RFM
  analysis, and A/B testing gave modeling work a target
  ([2:53 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
- Source semantics: document source tables or events, update cadence, known
  defects, and ownership because [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
  grounds this in tracking plans with events, properties, and ownership
  ([13:34-20:47]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
- Modeled layers: separate sources, staging logic, intermediate joins, and marts.
  [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) distinguishes
  warehouses, transformations, and data marts inside ELT
  ([10:00-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
- Metric definitions: state grain, dimensions, facts, filters, and accepted
  business logic, because [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
  ties this to making data resemble business reality
  ([11:03-20:21]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
- Tests and docs: add non-null checks, unique checks, accepted-values checks,
  relationship checks, and freshness checks. Add custom tests where they match
  the data rules, as [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
  discusses dbt tests and upstream checks. She also covers warnings, errors,
  docs, and profiling tools
  ([36:44-38:53 and 50:46]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
- BI or activation surface: publish a dashboard, semantic layer, notebook, or
  reverse-ETL segment that consumes only modeled data. [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
  connects warehouse transformations to BI and operational activation
  ([28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
- Run behavior: explain which failures block the build, which warnings need
  review, and how consumers learn about data issues. [Barr Moses]({{ '/people/barrmoses/' | relative_url }})
  frames freshness, volume, distribution, and schema as reliability signals.
  She also covers lineage, ownership, and SLAs
  ([16:38-35:24 and 58:51]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

## Project Types

A metric mart and dashboard project is the clearest portfolio option. Pick a
domain with repeatable decisions. Good domains include subscriptions and
ecommerce. Marketing spend and SaaS usage also work. Logistics and finance can
work too.

Build source models first before adding staging tables plus facts and
dimensions. Define KPIs and add tests. Publish one documented dashboard that
uses only the modeled layer.

This matches [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
on modeling and Looker exposure. It also matches
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) on dashboards,
documentation and adoption
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

A dbt migration or refactor project works when the starting point is messy SQL,
duplicated dashboard logic, or spreadsheet-defined metrics. Refactor the logic
into model layers and add tests, docs, lineage, and a deployment note. Use
reusable macros only where they remove duplication.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
grounds this in a real dbt migration, LookML reporting, wide-versus-narrow
tables, and incrementalization tradeoffs
([18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) adds the
DataOps standard. He covers version control and tests. He also covers CI/CD,
runbooks, documentation, and end-to-end versioning
([33:47-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

A product analytics project should start with events, not charts. Write a
tracking plan, then simulate or instrument events. Model user journeys and
publish activation, retention, funnel, or experiment metrics.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
names signup and project-created events as SaaS examples. Invite and invoice
events fit there too. He then connects collection and storage with
transformation, analysis, and activation
([13:34-30:03]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows why
marketing and product domain knowledge matter for funnels, retention, RFM, and
A/B testing
([38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

A reverse ETL or activation project is useful when the portfolio needs to show
operational consequences. Model a customer or account segment in the warehouse.
Then push it to a mock CRM, support tool, or marketing destination. Document
ownership, refresh cadence, and privacy assumptions. Also explain the
consequence of a wrong segment.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) covers reverse
ETL and product-led activation in
[Data-Led Growth Stack at 37:25-56:08]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) covers warehouse
tables flowing back into operational systems in
[ETL, ELT, and the Modern Data Stack at 35:42]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).

A hiring-focused fundamentals project should go deep on SQL and modeling before
adding tools. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) places an
analytics-engineering module around dbt, Snowflake, Mode, and Fivetran. He also
emphasizes SQL mastery and window functions.

Katz also treats OLTP versus OLAP and sample database modeling practice as
fundamentals
([36:18-45:14]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})).
Junior candidates can win with a smaller project. Strong grain definitions,
tests, docs and SQL explanations can beat a broad stack that hides the modeling
decisions.

## Portfolio Proof

Review the project as if another analyst must maintain it next month.

They should be able to find these answers from the repository, dashboard, and
docs:

- Row grain: state what one row represents and which joins preserve or change
  that grain, because [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
  ties this modeling question to representing business reality
  ([11:03-20:21]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
- Source fields: name fields from user events, backend systems, ads platforms,
  finance tools, and manual inputs. [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
  makes source awareness and tracking-plan ownership part of data-led work
  ([10:45-20:47]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
- Model layers: explain why the models are layered this way and where business
  logic lives, as [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) separates
  warehouse storage, transformations, and marts in the modern stack
  ([15:30-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
- Failure rules: state which assumptions fail the build and which assumptions
  warn a human, since [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
  discusses dbt checks and upstream checks. She also covers warnings and errors
  ([38:53]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
- Documentation: make owners, purpose, caveats, and columns findable. Include
  dependencies and example queries because [Tammy Liang]({{ '/people/tammyliang/' | relative_url }})
  uses a Notion wiki plus dashboard checks. Workshops make data work adopted
  outside the data team
  ([22:32 and 49:00]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).
- Consumption: make the dashboard or activation flow use shared models instead
  of embedded duplicate metric logic. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
  connects Looker, LookML, dbt migration, and product analytics in the same
  BI stack
  ([20:34-23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
- Reconciliation: explain how a stakeholder would reconcile changed numbers
  after a migration or source fix. [Barr Moses]({{ '/people/barrmoses/' | relative_url }}) connects
  schema changes, lineage, ownership, and SLAs to data reliability
  ([19:10-35:24 and 58:51]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

## Anti-Patterns

Avoid a dashboard built directly from raw tables with metric logic hidden in
charts. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
places analytics-engineering value in modeled data, dbt transformations, and
Looker exposure, not in isolated charts
([4:05-8:59]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Avoid a dbt repository with many models but no business definitions, tests,
owners, or BI consumer. [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
argues that the work should map business reality and make the data safer.
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) shows that adoption,
documentation, and trust matter after the models exist
([Foundations episode]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

Avoid copying a public template without explaining grain, joins, slowly
changing attributes, or incremental logic. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
grounds the role in practical data-modeling tradeoffs during a dbt migration,
including wide versus narrow tables and incrementalization
([30:28-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Avoid final KPI screenshots without source caveats, data-quality checks, or
reconciliation notes. [Barr Moses]({{ '/people/barrmoses/' | relative_url }})
shows how silent failures, schema changes, freshness, and lineage break trust.
Ownership matters too when teams only look at the final output
([13:40-29:00]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Avoid treating analytics engineering as "SQL plus dashboard." The archive
returns to software practices and tests, then to docs and lineage. Version
control, warehouse transformations and adoption matter too
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

## Related Pages

Use these pages for the role, stack, and adjacent portfolio context:

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})
