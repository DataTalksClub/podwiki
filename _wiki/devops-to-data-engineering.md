---
layout: wiki
title: "DevOps to Data Engineering"
summary: "Podcast-backed transition notes for DevOps, SRE, cloud, and platform engineers moving into data engineering through automation, DataOps, pipelines, cloud platforms, and portfolio proof."
related:
  - Career Transition
  - Data Engineering
  - DataOps
  - Data Engineering Platforms
  - Data Quality and Observability
  - MLOps vs DevOps
  - Open Source Portfolio Evidence
---

DevOps to data engineering is a move from operating software platforms to
building and operating data platforms. In the archive's clearest transition
example, [Agita Jaunzeme]({{ '/people/agitajaunzeme/' | relative_url }})
connects configuration management and early DevOps automation to open-source
DataOps work
([Agita transition episode at 5:22-9:20]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

The transition is adjacent, but it isn't automatic. DevOps experience transfers
when the work is platform-shaped, especially around automation and deployment
discipline. Cloud infrastructure, observability, documentation, and recovery
practice matter too.

The data-specific gap starts with SQL and data modeling. It also includes
orchestration, pipeline correctness, data quality, and downstream semantics
([Tulski role episode at 11:54-25:33]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
and [Bergh DataOps episode at 15:52-30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

The transition works best when infrastructure evidence becomes data evidence. A
scripted operational fix becomes repeatable ingestion or backfill logic. A
CI/CD habit becomes tests and deployment confidence for pipelines. Monitoring
becomes owner-aware data observability over freshness, schema, and lineage
([Agita transition episode at 14:29-21:03]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }})).

## Link Map

Start with these podcast discussions:

- [From DevOps to Data Engineering]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}) is the core transition episode. Jaunzeme covers DevOps automation, configuration management, open source, volunteer work, and process transfer.
- [Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}) defines the target split between platform data engineering and product data engineering. [Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) also explains SQL, cloud, cost awareness, and portfolio framing.
- [DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}) shows operating practices that DevOps people can reuse in data teams. It covers automation, observability, CI/CD, and regression tests.
- [Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}) connects DevOps ideas to data work. The bridge runs through version control, tests, CI/CD, runbooks, automation, and documentation.
- [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) places pipelines and orchestration around the infrastructure skills. It also covers warehouses, CDC, and ELT/ETL vocabulary.
- [Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}) defines the monitoring layer DevOps engineers need to translate into data terms. It covers freshness, volume, distribution, schema, lineage, ownership, SLAs, and runbooks.

People connected to the cited interviews:

- [Agita Jaunzeme]({{ '/people/agitajaunzeme/' | relative_url }})
- [Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }})
- [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
- [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
- [Barr Moses]({{ '/people/barrmoses/' | relative_url }})

Adjacent pages:

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [MLOps vs DevOps]({{ '/wiki/mlops-vs-devops/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})

## Common Route

The common route starts with automation. Jaunzeme's story moves from C++ and
configuration-management work into early DevOps, then into automation scripts
that replaced repetitive manual work. The promotion signal wasn't the script
alone. It was the ability to notice repeated operational work and turn it into a
maintained process
([Agita transition episode at 5:22 and 14:29]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

That maps cleanly to [DataOps]({{ '/wiki/dataops/' | relative_url }}). In
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})'s
DataOps episodes, the same operating instinct becomes version control and tests
for data workflows. It also becomes CI/CD, observability, runbooks, and
production monitoring
([Mastering DataOps at 33:47-38:01]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
and [Bergh DataOps episode at 15:52-30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

After automation, the next step is choosing the data-engineering lane. Tulski
separates platform data engineers from product data engineers. Platform data
engineers build warehouses, shared platforms, infrastructure, and tooling. They need software
engineering, DevOps, cloud, and processing-engine skills. Product data
engineers work closer to business use cases, data products, analytics needs,
and SQL-heavy data use
([Tulski role episode at 11:54-21:50]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

For DevOps and SRE backgrounds, the archive points first toward platform data
engineering. The same applies to cloud and platform engineers. That route values
infrastructure skills, but it still requires data-system proof.

Ingestion and orchestration are proof points. Warehouse design, cost awareness,
and data-quality checks matter too
([Tulski role episode at 21:50-30:56]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})
and [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

## Guest Differences

Guests differ on whether the first story should be a career-transition story or
a target-role story. Jaunzeme emphasizes transferable problem solving and
automation. She also emphasizes corporate process habits, open-source work, and
community routes back into technical roles
([Agita transition episode at 19:16-36:25]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

Tulski emphasizes what the data-engineering market expects after the transition.
That means clear specialization and SQL. It also means cloud exposure, cost
awareness, and proof that the candidate can build useful platforms
([Tulski role episode at 21:50-42:08]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

Guests also differ on how much tooling to add. Tulski warns against oversized
platforms and unnecessary real-time systems, and he warns against expensive
technology chosen before the business need is clear. His examples put cost
awareness ahead of tool maximalism because the platform has to match the company
([Tulski role episode at 25:33-38:01]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})'s modern-stack
episode is useful for vocabulary. It maps ingestion, warehouse work,
transformation, and orchestration while also covering CDC and analytics
workflows. Treat it as a map, not a checklist of tools to install
([modern-stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
and [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

The DataOps guests add a third difference. Bergh starts from deployment fear,
rework, regression risk, and weak recovery.
[Barr Moses]({{ '/people/barrmoses/' | relative_url }})
starts from data downtime and observability signals. Together they show why
DevOps monitoring knowledge transfers. It first has to expand from service
health to data health
([Bergh DataOps episode at 13:27-18:46]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }})).

## Transferable DevOps Skills

Automation transfers directly when it acts on data delivery rather than only on
servers. Jaunzeme's automation story is about replacing repeated manual work
with scripts and process. Bergh's DataOps framing turns that same habit into
pipeline deployment and regression testing. It also becomes runbooks and
automated recovery
([Agita transition episode at 14:29]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})
and [Mastering DataOps at 33:47-37:13]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

Infrastructure skills transfer most strongly to platform data engineering.
Tulski names DevOps, infrastructure, cloud engineering, and processing engines
as platform-side skills. He then adds cost awareness as a competitive advantage.
Cloud data systems become expensive when the platform is larger than the company
needs
([Tulski role episode at 11:54-30:56]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

Observability transfers when service signals become data signals. Service
monitoring over availability, latency, errors, and saturation isn't enough.
Data observability adds freshness and schema checks plus lineage, ownership,
and SLAs.

Moses defines those data-specific signals. Bergh connects them to production
monitoring and recovery habits
([Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
[Bergh DataOps episode at 50:29-54:05]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

Documentation and process habits transfer when they make data work easier to
handoff. Jaunzeme describes applying corporate documentation and agile practices
in volunteer organizations. Bergh's DataOps episode links documentation,
handoffs, and runbooks to lower on-call pressure
([Agita transition episode at 21:03-25:07]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}),
[Mastering DataOps at 34:37-40:29]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

Open-source and community work transfer when they produce public technical
evidence.

Jaunzeme returned to corporate technical work through open-source and
community work at VMware. The named project is Versatile Data Kit.

This makes
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
relevant for DevOps candidates who need external data-tooling proof
([Agita transition episode at 9:20 and 36:25]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

## Data-Specific Gaps

SQL doesn't come for free from DevOps. Tulski names SQL as a core data
engineering skill because both platform and product-side data engineers need to
interact with data. The archive's [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
hub places SQL, Python, and modeling before advanced distributed systems
([Tulski role episode at 20:55-21:50]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})).

Pipeline correctness is different from service uptime. A job can finish and
still deliver late or semantically wrong data. It can also duplicate or omit
records. Moses's
observability discussion covers silent failures, schema changes, freshness, and
lineage. Bergh's DataOps episodes add regression tests and realistic test data
for analytics workflows
([Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
[Bergh DataOps episode at 30:55-54:05]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Real-time infrastructure doesn't automatically prove senior data engineering.
Tulski's 2026 discussion warns that streaming engines, Spark clusters, cloud
warehouses, and custom platforms should follow the problem. They should also
follow the cost model. For a DevOps candidate, the stronger transition signal is judgment about
architecture fit
([Tulski role episode at 30:56-38:01]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

Business semantics don't come from infrastructure alone. Product-side data
engineering and analytics engineering need metric definitions, modeled tables,
and consumer context. Tulski's platform/product split and the
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
pages show the role boundary. A DevOps candidate can aim at platform data
engineering first. The other route is deliberate practice with modeled
analytical data
([Tulski role episode at 11:54-17:29]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

## Practical Transition Work

Start by reframing existing work as data-system work. An infrastructure script
becomes stronger evidence when it ingests data and records raw inputs. It should
also transform them into modeled tables and report failures. This follows Jaunzeme's
automation route. It also follows Tulski's small-platform advice for platform
data engineering targets
([Agita transition episode at 14:29-19:16]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}),
[Tulski role episode at 1:04:42]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

Build the first portfolio project as a small platform, not a tutorial clone.
Tulski's example platform can include DuckDB, dbt, Superset, and orchestration.
The project should solve a concrete problem and show the
candidate's own extensions
([Tulski role episode at 57:35-1:04:42]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})).

Add DataOps evidence before adding exotic tooling. A DevOps-to-data project
should show Git-based changes, tests, scheduled runs, and environment setup. It
should also show rerun behavior, alerts, and a short incident or recovery story.

That matches Bergh's DataOps guidance on CI/CD and regression tests.
Observability and deployment automation matter too. Versioning and runbooks also
belong in the proof
([Bergh DataOps episode at 30:55-58:34]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
[Mastering DataOps at 33:47-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

Make cost and scope visible. Tulski treats cost awareness as a data-engineering
advantage, especially when teams overbuild cloud platforms. A portfolio project
can show that judgment with scope choices. Explain batch instead of streaming,
managed services instead of custom infrastructure, or a local stack instead of a
paid warehouse
([Tulski role episode at 25:33-38:01]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

Use open source when the current job can't provide data projects. Jaunzeme's
open-source route and the [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
page both favor visible artifacts. Strong examples include issues, pull
requests, docs, and tests. CI and maintainer feedback matter too.

For this transition, the best targets are data connectors and orchestration
tools. dbt packages, observability examples, and data-platform documentation
also fit
([Agita transition episode at 36:25-40:23]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

## Role Fit

This transition fits DevOps engineers and SREs when they want the platform side
of [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}). It also
fits cloud engineers, platform engineers, release engineers, and infrastructure
automation specialists.

Tulski's role split makes that fit explicit. Platform data engineers need
software engineering and infrastructure, plus DevOps, cloud, and
processing-engine skills
([Tulski role episode at 11:54-21:50]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).

The fit is weaker when the candidate wants a dashboard, analyst, or
analytics-engineering role but avoids SQL and data modeling. Those roles sit
closer to modeled business data and metrics. Stakeholder definitions and
warehouse-side transformations matter too
([Tulski role episode at 11:54-17:29]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})).

The archive's practical advice is to narrow the target before building proof.
If the target is platform data engineering, build a small data platform and make
operability visible. If the target is product data engineering or analytics
engineering, add SQL modeling and metric definitions. Consumer-facing data
products should also be part of the portfolio
([Tulski role episode at 42:08-1:04:42]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})).

## Related Pages

Use these pages for the role, stack, and adjacent transition context.

- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [MLOps vs DevOps]({{ '/wiki/mlops-vs-devops/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
