---
layout: wiki
tags: ["transition"]
title: "DevOps to Data Engineering"
summary: "Podcast-backed transition notes for DevOps, SRE, cloud, and platform engineers moving into data engineering through automation, DataOps, pipelines, cloud platforms, and portfolio proof."
related:
  - Career Transitions in Data
  - Data Engineering
  - DataOps
  - Data Engineering Platforms
  - Data Quality and Observability
  - Open Source Portfolio Evidence
---

DevOps to data engineering is a move from operating software platforms to
building and operating data platforms. [[person:agitajaunzeme|Agita Jaunzeme]]
gives the strongest transition story in the podcast archive. She moved from
configuration management and early DevOps automation into open-source DataOps
work on Versatile Data Kit
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|5:22-9:20]]).

The transition sits near [[Data Engineering]]
and [[DataOps]], with overlap in
[[Data Engineering Platforms]].
Those overlaps help, but DevOps experience becomes data engineering evidence
only when it shows data delivery. Repeatable ingestion, tested transformations,
and scheduled pipelines show one side of that evidence. Recovery paths,
cost-aware cloud choices, and [[data-quality-and-observability|Data Observability]]
show the operations side.

## DevOps Skills That Transfer

The podcast episodes converge on one practical definition. DevOps-to-data
engineering work applies automation, reliability, and platform habits to data
pipelines. Jaunzeme's career story starts with configuration management and
scripts that removed repetitive manual work. She treats the important skill as
spotting repeated operational work and turning it into a maintained workflow
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|5:22 and 14:29]]).

[[person:christopherbergh|Christopher Bergh]] gives the
DataOps version of the same move. In his DataOps episodes, teams use tests
under version control to reduce data-pipeline fear and rework. They also add
CI/CD plus monitoring. Bergh ties runbooks to deployment automation as part of
the same DataOps discipline
([[podcast:dataops-automation-and-reliable-data-pipelines|33:47-38:01]],
[[podcast:dataops-for-data-engineering|30:55-42:39]]).
That makes DataOps the most direct bridge between DevOps practice and production
data engineering.

[[person:slawomirtulski|Slawomir Tulski]] defines the
target role more sharply by separating platform data engineers from product
data engineers. Platform engineers build shared warehouses, infrastructure,
tooling, and processing systems. Product data engineers work closer to business
use cases, SQL-heavy data work, and data products
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|11:54-21:50]]).

The cited episodes point DevOps and SRE readers first toward the platform data
engineering lane. Cloud engineers and platform engineers fit there too.
Candidates need to show data-system proof, not only infrastructure ownership.

## Career Story and Hiring Bar

Jaunzeme frames the move as transferable problem solving, automation, and
documentation. She also emphasizes volunteer leadership, open source, and
community routes back into corporate technical work
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|19:16-40:23]]).
Her episode is useful when a candidate needs to turn nonlinear experience into a
credible data engineering story.

Tulski focuses on what the market expects after the transition. He emphasizes
specialization, SQL, and cloud exposure. He also emphasizes cost awareness and
projects that prove the candidate can build useful platforms
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|21:50-42:08]]).
He also warns against oversized platforms, unnecessary real-time systems, and
expensive tools chosen before the business problem is clear
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|25:33-38:01]]).

[[person:nataliekwong|Natalie Kwong]] gives a stack
map rather than a transition recipe. Her modern data stack discussion places
ingestion, ELT, dbt-style transformations, and warehouses into one vocabulary.
She also covers data marts, orchestration, CDC, and reverse data flows
([[podcast:data-engineering-tools-modern-data-stack|3:46-35:42]]).
For a DevOps candidate, that episode names the data-specific surface area, but
it shouldn't become a checklist of tools to install.

Bergh and [[person:barrmoses|Barr Moses]] start from
failure modes. Bergh starts with deployment fear, rework, regression risk, and
weak recovery in data work
([[podcast:dataops-for-data-engineering|13:27-18:46]]).

Moses starts with data downtime, silent failures, and schema changes. He then
connects lineage, ownership, SLAs, and runbooks to data reliability
([[podcast:data-quality-data-observability-data-reliability|13:40-41:03]]).
Together they show that DevOps monitoring knowledge transfers only after the
candidate expands it from service health into [[data-quality-and-observability|Data Observability]].

## Platform Habits in Data Work

Automation transfers when it acts on data delivery, and Jaunzeme's scripting
story shows the career signal. She found repetitive manual work, automated it,
and earned more responsibility
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|14:29-19:16]]).
In data engineering, the same habit can become ingestion code, scheduled
backfills, and repeatable transformations. It can also become automated checks
and recovery playbooks.

Bergh describes this DataOps path through version control, tests, and CI/CD.
Runbooks and automation belong in the same practice
([[podcast:dataops-automation-and-reliable-data-pipelines|33:47-37:13]]).

Infrastructure skills transfer most clearly to platform data engineering because
Tulski names DevOps and infrastructure as platform-side skills. He also names
cloud engineering and processing engines. Cost awareness becomes a competitive
advantage because cloud data systems can become expensive when teams overbuild
them
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|11:54-30:56]]).
The transition belongs near [[Data Engineering Platforms]]
and [[Modern Data Stack]], but
the strongest signal is judgment about scope.

Observability transfers when service metrics turn into data-health signals.
Moses traces data observability back to DevOps observability, then explains why
batch data needs freshness and volume checks. He also covers distribution and
schema checks. Lineage, ownership, SLAs, and runbooks matter when teams handle
data incidents
([[podcast:data-quality-data-observability-data-reliability|6:56-41:03]]).

Bergh adds the production habit. Watch real systems, use monitoring to drive
change, and make failures easier to diagnose
([[podcast:dataops-for-data-engineering|50:29-54:05]]).

Documentation habits transfer when they make data work easier to hand off.
Jaunzeme describes applying corporate documentation and agile practices in
volunteer organizations
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|21:03-25:07]]).
Bergh links runbooks, documentation, automated playbooks, and replaceability to
lower on-call pressure in data teams
([[podcast:dataops-automation-and-reliable-data-pipelines|34:37-40:29]]).

## Data Engineering Gaps

SQL and modeling don't come for free from DevOps. Tulski names SQL as a core
skill because both platform and product data engineers need to work with data
directly
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|20:55-21:50]]).
Kwong's modern-stack episode shows why. ELT and analytics engineering move many
transformations into SQL in the warehouse. dbt-style workflows and data marts
become part of the delivery path
([[podcast:data-engineering-tools-modern-data-stack|7:57-18:47]]).

Pipeline correctness differs from service uptime. A job can finish and still
deliver late or semantically wrong data. It can also duplicate or omit records.

Moses's observability episode covers silent failures and schema changes. He also
covers freshness, lineage, ownership, and data SLAs
([[podcast:data-quality-data-observability-data-reliability|13:40-35:24]]).
Bergh adds regression tests and realistic test data for analytics workflows
([[podcast:dataops-for-data-engineering|30:55-34:13]]).

[[Data Quality and Observability]]
is central to this transition because pipeline health includes freshness and
volume. It also includes distribution, schema, and lineage, not only job
success.

Real-time infrastructure doesn't automatically prove senior data engineering.
Tulski warns that streaming engines, Spark clusters, cloud warehouses, and
custom platforms should follow the problem and the cost model
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|30:56-38:01]]).
For a DevOps candidate, a smaller batch platform with clear tradeoffs can be a
stronger signal than a large stack copied from a tutorial.

Business semantics are the other gap. Product data engineering and
[[Analytics Engineering]]
need modeled tables, metric definitions, and consumer context. Tulski's
platform/product split shows why a candidate should pick the target lane before
building proof
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|11:54-17:29]]).

## Portfolio Proof

The practical transition starts by turning infrastructure evidence into data
evidence. A DevOps script becomes stronger when it ingests data and stores raw
inputs. It should also transform those inputs into useful tables, report
failures, and support a rerun or backfill path. This follows Jaunzeme's
automation route and Tulski's advice to build around a concrete platform
problem
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|Jaunzeme at 14:29-19:16]],
[[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Tulski at 57:35-1:04:42]]).

Build the first project as a small data platform rather than a tutorial clone.
Tulski's portfolio advice includes DuckDB, dbt, Superset, and orchestration. He
also expects the candidate's own extensions around a specific problem
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|57:35-1:04:42]]).
That makes [[Data Engineering Portfolio Projects]]
and the [[data-engineer-roadmap|Data Engineering Roadmap]]
natural next pages.

Add DataOps evidence before adding exotic tooling. A DevOps-to-data project
should show Git-based changes, tests, scheduled runs, and environment setup. It
should also show rerun behavior, alerts, and an incident or recovery story.

Bergh's DataOps guidance supports that proof through CI/CD, regression tests,
and observability. Deployment automation, versioning, and runbooks belong in the
same proof
([[podcast:dataops-for-data-engineering|30:55-58:34]],
[[podcast:dataops-automation-and-reliable-data-pipelines|33:47-51:21]]).

Use open source when the current job can't provide data projects. Jaunzeme
returned to corporate technical work through open-source and community work at
VMware. That work included Versatile Data Kit
([[podcast:from-devops-to-data-engineering-automation-open-source-volunteering|9:20 and 36:25-40:23]]).

For this transition, useful public proof can include data connectors,
orchestration examples, and dbt packages. Observability checks and documentation
also count. Tests, issues, and pull requests connect the route to
[[Open Source Portfolio Evidence]].

## Role Fit

This transition fits DevOps engineers, SREs, cloud engineers, and platform
engineers who want the platform side of data engineering. It also fits release
engineers and infrastructure automation specialists. Tulski's role split makes
the fit explicit. Platform data engineers need software engineering and
infrastructure. They also need DevOps, cloud, and processing-engine skills
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|11:54-21:50]]).

The fit is weaker when the candidate wants a dashboard, analyst, or
analytics-engineering role but avoids SQL and data modeling. Those roles sit
closer to modeled business data and metrics. They also require stakeholder
definitions and warehouse-side transformations
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Tulski at 11:54-17:29]],
[[podcast:data-engineering-tools-modern-data-stack|Kwong at 12:39-18:47]],
[[Data Analyst vs Analytics Engineer]]).

The practical advice in these episodes is to narrow the target before building
proof. For platform data engineering, build a small data platform and make
operability visible. For product data engineering or analytics engineering, add
SQL modeling, metric definitions, and consumer-facing data products
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Tulski at 42:08-1:04:42]]).

## Nearby Topics

The transition is easiest to compare against nearby role, stack, portfolio, and
reliability topics.

- [[career-transitions-in-data|Career Transition]]
- [[Career Transitions in Data]]
- [[Data Engineering]]
- [[data-engineer-roadmap|Data Engineering Roadmap]]
- [[Data Engineering Platforms]]
- [[Data Engineering Portfolio Projects]]
- [[DataOps]]
- [[data-quality-and-observability|Data Observability]]
- [[Data Quality and Observability]]
- [[Modern Data Stack]]
- [[MLOps vs DevOps]]
- [[Open Source Portfolio Evidence]]
