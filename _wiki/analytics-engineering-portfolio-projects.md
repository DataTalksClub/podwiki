---
layout: wiki
title: "Analytics Engineering Projects"
summary: "Project ideas for showing SQL modeling, metric ownership, dbt tests, documentation, BI readiness, and stakeholder judgment."
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

An analytics engineer portfolio should show how a candidate turns messy source
data into reusable models, shared metric definitions, and a trusted analytical
surface.

Strong projects go beyond SQL or a dashboard. They explain table grain and
modeled layers, add tests, and show how BI consumers use the definitions. They
also show the business question behind the model.

These project ideas focus on reusable models and handoff. The broader role is
covered in [[Analytics Engineering]] and
[[Analytics Engineering Roadmap]]. The role boundary is covered in
[[Data Analyst vs Analytics Engineer]]. Dashboard implementation connects to
[[Dashboard and Metric Layer Project Checklist]]. Ingestion, orchestration, and
platform-heavy work belong with [[Data Engineering Portfolio Projects]].

## Reviewable Analytics Project

A good analytics engineering portfolio project starts with a repeated business
question and ends with a trusted analytical surface. The repository should make
source assumptions and staging models easy to review. It should also show
intermediate logic, marts, tests, and docs. The final analytical surface should
be a dashboard or query layer that consumes shared models.

Perez Mola's role discussion makes a dashboard-only project weak unless the
dashboard sits on reusable models. A dbt-only project is also weak unless the
models answer a business question and expose definitions to consumers
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].
Perafan's modeling discussion makes the writeup part of the evidence: the
project should explain why the model represents the business correctly. It
should also state what one row means, which joins preserve the grain, and which
caveats stakeholders should know
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Analytics Engineer Foundations]].

The same work sits inside [[etl-vs-elt=>ETL and ELT]]. Data
arrives first, and analysts or analytics engineers then transform it with SQL and
dbt and publish data marts or consumption tables
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
That favors projects that show source assumptions and warehouse-side
transformations, even when the portfolio isn't a full data-engineering
project.

## Reviewer Signals

Reviewers should be able to see the model, the business reason for it, and the
handoff. [[person:victoriaperezmola=>Victoria Perez Mola]]
grounds that in modeling and quality. Looker, dbt, and collaboration with
analysts also belong in the evidence
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].
[[person:juanmanuelperafan=>Juan Manuel Perafan]]
adds that the project should make business reality explicit and safer through
testing, documentation, and rigor
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Analytics Engineer Foundations]].

[[person:nikolamaksimovic=>Nikola Maksimovic]] shows a
transition version of the portfolio, and the proof didn't start as a public
repository. It started with marketing reporting and BI-team conversations.
Looker work, SQL practice, and BI projects happened alongside marketing work.
The later role included dbt migration, LookML, product analytics, and A/B
testing
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].
That supports portfolios that turn domain knowledge into modeled metrics
instead of treating domain context as background.

Analysts can use the
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
to turn dashboard and KPI work into this kind of portfolio.

[[person:arpitchoudhury=>Arpit Choudhury]] widens the
project boundary toward [[Data Activation]].
His episode connects tracking plans and event collection with warehouse
transformations and BI. Reverse ETL then sends modeled data to support, sales,
and engagement tools
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
For portfolio builders, this makes activation projects legitimate
analytics-engineering evidence when the work documents event ownership, data
meaning, and downstream consequences.

Use [[Analytics Engineering Roadmap]] for the learning order, and choose
proof-of-work projects that reviewers can look at.

## Metric Mart and Dashboard Project

A metric mart and dashboard project is the clearest portfolio option because it
connects [[Metrics]], modeled tables, and
a visible consumption surface. Pick a domain with repeated decisions. Useful
domains include marketing funnels, product usage, business-health reporting,
and finance reporting. Build source models before staging tables, facts,
dimensions, and metric definitions. Then add tests and one documented dashboard
that uses only the modeled layer.

[[person:victoriaperezmola=>Victoria Perez Mola]]
ties analytics engineering to modeling and Looker exposure
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].
[[person:tammyliang=>Tammy Liang]] adds business-health monitoring and
streamlined reporting. Her team used documentation, testing, and adoption
workshops
[[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]].

For a portfolio, the README should show who uses the dashboard. It should
explain what changed from the old spreadsheet or duplicated query. It should
also show how another analyst finds the definitions.

The project should answer these review questions:

- Business question: name the decision and metric owner. This follows
  [[person:nikolamaksimovic=>Nikola Maksimovic]] from
  performance marketing into BI and product analytics. Funnels, retention,
  [[rfm-analysis=>RFM analysis]], and A/B testing gave modeling work a target
  [[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].
- Row grain: state what one row represents and which joins preserve or change
  that grain, because [[person:juanmanuelperafan=>Juan Manuel Perafan]]
  ties this modeling question to representing business reality
  [[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Analytics Engineer Foundations]].
- Modeled layers: separate sources, staging logic, intermediate joins, and
  marts, since [[person:nataliekwong=>Natalie Kwong]] distinguishes
  warehouses, transformations, and data marts inside the modern stack
  [[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
- Consumption: make the dashboard use shared models instead of embedded
  duplicate metric logic because [[person:nikolamaksimovic=>Nikola Maksimovic]]
  connects Looker, LookML, dbt migration, and product analytics in the same
  BI stack
  [[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].

## dbt Migration or Refactor Project

A dbt migration or refactor project works when the starting point is messy SQL,
duplicated dashboard logic, or spreadsheet-defined metrics. Refactor the logic
into model layers and add tests, docs, lineage, and a deployment note. Use
reusable macros only where they remove duplication.

[[person:nikolamaksimovic=>Nikola Maksimovic]]
grounds this in a real dbt migration and LookML reporting. He also discusses
wide-versus-narrow tables and incrementalization tradeoffs
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].
[[person:christopherbergh=>Christopher Bergh]] adds the
[[DataOps]] standard for version control
and tests. He also covers CI/CD, runbooks, documentation, and end-to-end
versioning
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].

This project is strongest when it shows before-and-after behavior. Include the
old query or dashboard calculation, the new
[[dbt]] model structure, the tests that catch
broken assumptions, and a reconciliation note for stakeholders. That
reconciliation belongs in the portfolio because
[[person:barrmoses=>Barr Moses]] connects schema
changes, lineage, ownership, and SLAs to data reliability
[[cite:data-quality-data-observability-data-reliability=>Data Observability]].

## Product Analytics and Event Model Project

A product analytics project should start with events, not charts. Write a
tracking plan, then simulate or instrument events. Model user journeys and
publish activation, retention, funnel, or experiment metrics.

[[person:arpitchoudhury=>Arpit Choudhury]]
names signup and project-created events as SaaS examples. Invite and invoice
events fit there too. He then connects collection and storage with
transformation, analysis, and activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
[[person:nikolamaksimovic=>Nikola Maksimovic]] shows why
marketing and product domain knowledge matter for funnels, retention,
[[rfm-analysis=>RFM analysis]], and A/B testing
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].

This project should connect
[[Event Tracking]],
[[Product Analytics]], and
[[a-b-testing=>A/B Testing]] through modeled
tables. Document event owners and required properties. Also explain
late-arriving events, user identity rules, and which modeled metrics feed the
dashboard or experiment readout. That source-semantics work follows
[[person:arpitchoudhury=>Arpit Choudhury]] on tracking
plans with events, properties, and ownership
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].

## Reverse ETL Project As An Activation Example

A reverse ETL or activation project is useful when the portfolio needs to show
operational consequences. Model a customer or account segment in the warehouse.
Then push it to a mock CRM, support tool, or marketing destination. Document
ownership, refresh cadence, and privacy assumptions. Also explain the
consequence of a wrong segment.

[[person:arpitchoudhury=>Arpit Choudhury]] covers
reverse ETL and product-led activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
[[person:nataliekwong=>Natalie Kwong]] covers warehouse
tables flowing back into operational systems
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].

For analytics engineering, the important proof isn't the connector. It's that
a trusted modeled segment can safely leave the warehouse. Link the segment to
[[Data Activation]],
[[Reverse ETL]], and the metric or
event definitions that produced it. Include one failure example, such as a
stale trial-status field or a duplicated account. Operational activation makes
wrong analytical definitions visible to sales, support, or lifecycle marketing.

## Hiring-Focused Fundamentals Project

A hiring-focused fundamentals project should go deep on SQL and modeling before
adding tools. [[person:jeffkatz=>Jeff Katz]] places an
analytics-engineering module around dbt, Snowflake, Mode, and Fivetran. He also
emphasizes SQL mastery, window functions, OLTP versus OLAP, and sample
database modeling practice
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path]].

The concrete artifact can be a small warehouse model over a sample
transactional database. Show OLTP-to-OLAP modeling and window functions. Then
add dimensional choices and a concise dashboard or query notebook. The
[[Data Analysis]] guide covers the
analyst-facing side of this work, while this page keeps the focus on
reusable modeling and handoff.

Junior candidates can win with a smaller project when the grain definitions and
tests are strong. Docs and SQL explanations can matter more than a broad stack
that hides the modeling decisions. Connect the writeup to
[[Data Analyst vs Analytics Engineer]]
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

[[person:victoriaperezmola=>Victoria Perez Mola]]
discusses dbt tests and upstream checks. She also covers warnings, errors,
docs, and profiling tools
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].
[[person:barrmoses=>Barr Moses]] frames freshness,
volume, distribution, and schema as reliability signals. She then ties lineage,
ownership, and SLAs to data trust
[[cite:data-quality-data-observability-data-reliability=>Data Observability]].

Documentation should make owners and purpose visible. It should also make
caveats, columns, dependencies, and example queries findable.
[[person:tammyliang=>Tammy Liang]]
uses a Notion wiki plus dashboard checks. She also connects workshops to data
adoption outside the data team
[[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]].
That links portfolio quality to
[[Data Quality and Observability]]
and [[DataOps]], not just to model count.

## Anti-Patterns

Avoid a dashboard built directly from raw tables with metric logic hidden in
charts. [[person:victoriaperezmola=>Victoria Perez Mola]]
places analytics-engineering value in modeled data, dbt transformations, and
Looker exposure, not in isolated charts
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]].

Avoid a dbt repository with many models but no business definitions, tests,
owners, or BI consumer. [[person:juanmanuelperafan=>Juan Manuel Perafan]]
argues that the work should map business reality and make the data safer
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Analytics Engineer Foundations]].
[[person:tammyliang=>Tammy Liang]] shows that adoption,
documentation, and trust matter after the models exist
[[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]].

Avoid copying a public template without explaining grain, joins, slowly
changing attributes, or incremental logic. [[person:nikolamaksimovic=>Nikola Maksimovic]]
grounds the role in practical data-modeling tradeoffs during a dbt migration,
including wide versus narrow tables and incrementalization
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].

Avoid final KPI screenshots without source caveats, data-quality checks, or
reconciliation notes. [[person:barrmoses=>Barr Moses]]
shows how silent failures, schema changes, freshness, and lineage break trust.
Ownership matters too when teams only look at the final output
[[cite:data-quality-data-observability-data-reliability=>Data Observability]].

Avoid treating analytics engineering as "SQL plus dashboard." Strong projects
show software practices and tests, then docs and lineage. They also show version
control, warehouse transformations, and adoption
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].
The broader workflow context belongs with [[Analytics Engineering]].

## Related Pages

These pages cover the role, stack, and adjacent portfolio context:

- [[Analytics Engineering]]
- [[Analytics Engineering Roadmap]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
- [[Data Analysis]]
- [[Data Analyst vs Analytics Engineer]]
- [[Marketing to Analytics Engineering]]
- [[Data Engineering Portfolio Projects]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[Product Analytics]]
- [[Event Tracking]]
- [[Metrics]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[Modern Data Stack]]
- [[ETL vs ELT]]
- [[dbt]]
- [[Data Quality and Observability]]
- [[Data Observability for Data Engineering]]
- [[DataOps]]
- [[Data Product Management]]
- [[Job Search]]
