---
layout: wiki
title: "Data Analyst vs Analytics Engineer"
summary: "A podcast-backed boundary page for separating analysis work from engineered analytical modeling, tests, documentation, and reusable data products."
related:
  - Analytics Engineering
  - Data Analyst Careers
  - Product Analytics
  - Data Product Management
---

## Definition and Scope

Data analysts help the organization understand what is happening and what to do
next. They work with metrics, dashboards, SQL, experiments, reports, and
stakeholder questions. Analytics engineers build the modeled, tested, documented,
and reusable data layer that makes that analysis trustworthy at scale.

The archive does not treat these as perfectly separate roles. In small teams,
one person may do both. The boundary becomes useful when repeated business logic,
metric definitions, dbt models, semantic layers, and data quality checks need an
owner.

## Contents

- [Comparison](#comparison)
- [Boundary Principles](#boundary-principles)
- [When Each Side Matters](#when-each-side-matters)
- [Podcast Evidence](#podcast-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Comparison

| Question | Data analyst | Analytics engineer |
| --- | --- | --- |
| Center of gravity | Business questions, metrics, experiments, dashboards, recommendations, and stakeholder communication. | Data modeling, warehouse transformations, tests, documentation, semantic layers, and BI-ready data products. |
| Typical output | Analysis, KPI definitions, dashboards, experiment readouts, decision memos, and ad hoc answers. | Staging models, marts, dimensions, facts, dbt projects, documented metrics, tests, and trusted reusable tables. |
| Speed vs robustness | Often optimizes for fast learning and decision support. | Often optimizes for repeatability, testability, lineage, and durable definitions. |
| Main risk | A one-off query or dashboard gets reused as if it were a governed source. | The modeled layer becomes overbuilt, slow to change, or detached from real stakeholder questions. |
| Archive skill signals | SQL, spreadsheets, BI tools, product sense, statistics, communication, domain knowledge. | SQL, data modeling, dbt-style workflows, Git, tests, documentation, warehouse concepts, stakeholder mediation. |

## Boundary Principles

### Analysts explain business movement

The first DataTalks.Club role episode frames analysts as people who know what
data exists, how to retrieve it, and how to interpret it. In the product example,
analysts quantify whether a feature problem is worth solving and evaluate
whether the shipped feature improved user behavior. This is decision work, not
only dashboard production.

### Analytics engineers encode reusable definitions

Analytics engineering episodes repeatedly return to the same work: model the
business reality in tables, clean and standardize source data, write versioned
SQL, add tests, document definitions, and expose reliable tables through BI
tools. The role appears when analysts and data scientists spend too much time
rebuilding the same logic or waiting on data engineers for business-facing
transformations.

### The difference is often philosophy, not task labels

Juan Manuel Perafan's analytics engineering episode is useful because it does
not define the role only as "between analyst and data engineer." He argues that
many tasks existed before the title. The change is the engineering philosophy:
testability, robustness, reproducibility, and safety around analytical work.

### Domain knowledge belongs on both sides

Analysts need domain knowledge to ask useful questions and explain results.
Analytics engineers need it to model entities, grains, dimensions, and metric
definitions correctly. The marketing-to-analytics-engineering episode shows why
marketing funnel knowledge, user journeys, and KPIs made the transition easier,
not less technical.

## When Each Side Matters

Choose a data analyst owner when the work is exploratory, decision-facing, or
stakeholder-specific:

- quantify a product problem or market change
- define success criteria for an experiment
- build an ad hoc dashboard for an urgent question
- interpret metric movement and recommend an action

Choose an analytics engineering owner when the work should become shared
infrastructure for analysis:

- create a canonical customer, order, listing, session, or subscription model
- move repeated dashboard logic into versioned transformations
- add tests for metric definitions and model assumptions
- document lineage, grain, owner, and known caveats
- decide how marts and semantic layers should be consumed

In small teams, one person may own both. The archive's practical advice is to
separate the mode of work even when the title is shared: fast analysis is not
the same as durable data modeling.

## Podcast Evidence

| Episode | Evidence |
| --- | --- |
| [Data Team Roles Explained](https://datatalks.club/podcast.html) | At 7:51-10:39, analysts understand data, build dashboards, define KPIs, quantify product problems, and evaluate experiments. |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | At 4:05-10:04, the role is described through data modeling, pipelines, quality, Looker, dbt, version control, tests, and dependency graphs. |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | At 14:34-16:54, the episode compares analytics engineer, data analyst, and data engineer roles and explains why the title emerged. |
| [Foundations of Analytics Engineer Role](https://datatalks.club/podcast.html) | At 11:03-13:18, analytics engineering is framed as turning business reality into data with engineering practices. At 16:25-18:35, the guest contrasts speed-focused analytics with robustness-focused engineering. |
| [Foundations of Analytics Engineer Role](https://datatalks.club/podcast.html) | At 26:53-29:22, the episode explains why some organizations split infrastructure and data modeling work while others keep them together. |
| [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html) | At 14:14-18:34, a small team combines analytics engineering, data analysis, product support, dashboards, KPIs, and A/B testing. At 25:06-28:40, the guest discusses role overlap and organizational fit. |
| [Data-Led Growth, Event Tracking, and Reverse ETL](https://datatalks.club/podcast.html) | At 25:08-28:40, the episode discusses team composition across data engineers, analysts, analytics engineers, and product operations for tracking and activation work. |

## Related Pages

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/data-team-roles.md`,
  `../datatalksclub.github.io/_podcast/analytics-engineer-skills-tools.md`,
  `../datatalksclub.github.io/_podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.md`,
  `../datatalksclub.github.io/_podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`,
  and `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- Keep this page focused on ownership boundaries. Put implementation depth on
  [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
- Future improvement: expand [Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }})
  with archive-backed role evidence, then link this page to specific analyst
  career clips.
