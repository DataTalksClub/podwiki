---
layout: "person"
title: "Natalie Kwong"
summary: "Natalie Kwong's DataTalks.Club podcast discussions, organized for topic exploration."
source_url: "https://datatalks.club/people/nataliekwong.html"
podcast_episodes: ["data-engineering-tools-modern-data-stack"]
curated: "true"
linkedin: "nataliekwong"
expertise: ["modern data stack", "ELT and ETL", "analytics engineering", "data integration", "CDC"]
---

Natalie Kwong is a Growth Product Manager at Airbyte focused on user
experience and analytics. Before Airbyte, she worked across analytics and
operations roles. Those roles included Harness, KeepTruckin, AppDynamics, and
earlier marketing analytics work. In
[her modern data stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
she turns data platform vocabulary into operating choices. She draws on
analytics team building and business-facing ingestion work.

## ELT as an Analytics-Team Operating Model

Natalie frames [ETL]({{ '/wiki/etl/' | relative_url }}) as the older model for
moving data. Teams extract data from source systems, apply business logic
before loading, and serve the result in a warehouse or BI tool. Her marketing
example is customer acquisition cost. CRM revenue and source attribution must
be joined with upper-funnel ad spend before the business can trust a CAC
dashboard
([3:46-7:27]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Natalie uses [ELT]({{ '/wiki/elt/' | relative_url }}) to argue for flexibility
and analyst autonomy. Raw data arrives first and transforms later in the
warehouse. New source fields and business logic can arrive without rebuilding
the whole pipeline. Analysts and
[analytics engineers]({{ '/wiki/analytics-engineering/' | relative_url }}) can
use SQL and dbt-style workflows instead of waiting on a platform engineering
team for every business change
([7:57-15:03]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
For role comparisons, her explanation belongs beside
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) and
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}).

## Raw Layers, Marts, and Trusted Business Tables

Natalie's warehouse model separates raw ingestion from business consumption.
She places the ingestion database at the raw edge of the warehouse. Business
users shouldn't pull directly from it because each person may apply different
transformations and create inconsistent metrics. The transformation layer turns
that raw data into data marts. These are finished and guarded tables for use
cases in go-to-market, finance, product, and operations
([15:30-19:26]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Her view makes [data engineering]({{ '/wiki/data-engineering/' | relative_url }})
less about moving bytes for its own sake and more about creating layers with
clear ownership. Natalie also connects quality to cleanup discipline. Teams
weaken trust when schemas and ad hoc storage keep growing without review. They
need to define each schema's purpose and agree how long data should remain
there
([21:22-24:23]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Warehouses, Lakes, and Team-Specific Architecture

Natalie distinguishes data warehouses from data lakes by structure and use
case. Warehouses fit relational, SQL-friendly analytics work. Lakes fit
unstructured data such as files, logs, and media. Her KeepTruckin example is
IoT video data: the company used Snowflake for structured analytics, but video
files belonged in a more flexible lake-style store
([19:50-21:22]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

She doesn't present a lake-plus-warehouse architecture as mandatory because the
warehouse may be enough for analytics teams. Engineering or data science teams
may need lake storage when they work with application data or unstructured
inputs. The decision depends on business complexity, team needs, and required
capabilities
([24:24-28:07]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
That makes her episode useful context for [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

## Tool Boundaries in the Modern Data Stack

Natalie is careful about where tools sit in the stack. Airbyte handles the E-L
part: reliable extraction and loading into a warehouse. dbt handles
warehouse-side SQL transformations. Airflow belongs in
[orchestration]({{ '/wiki/orchestration/' | relative_url }}): scheduling and
running jobs such as Airbyte syncs, rather than being the transformation system
there
([30:59-33:45]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Her definition of the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
is a best-of-breed toolchain instead of one platform that tries to own every
step.

She names examples across the stack:

- Airbyte and Fivetran for ingestion
- Snowflake and BigQuery for warehousing
- dbt or SQL for transformation
- Superset and Looker for visualization
- Airflow for orchestration

Natalie places these tools in the stack at
[33:45-35:42]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
For tool taxonomy, connect this discussion to
[data engineering tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
and [tools]({{ '/wiki/tools/' | relative_url }}).

## Operational Analytics, Reverse ETL, and CDC

Natalie describes [reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) as
moving finalized warehouse outputs back into operational systems. Her lead
scoring example shows why dashboards aren't always enough. Salespeople need
the score in Salesforce or another working system. She still calls this reverse
ETL because the transformation happens before the data leaves the warehouse,
not inside the destination tool
([35:42-38:36]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Natalie defines [CDC]({{ '/wiki/cdc/' | relative_url }}) as a sync strategy.
It captures only changed records instead of replicating a full database every
time. She emphasizes cost, speed, and delete handling. When only a small share
of rows changed, CDC moves that delta instead of re-copying the entire source
([45:59-48:30]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Tooling and Data Engineering Work

Natalie rejects the idea that low-code and no-code data tools make
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) disappear.
Her view is that they move engineers away from repetitive connector maintenance
and broken pipeline repair. Engineers can then focus on infrastructure and
governance. They can also set standards, validation checks, and delivery
practices that make analytics teams more effective
([39:06-43:05]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

She also gives a pragmatic reason for open-source ingestion tools. The long
tail of business systems and APIs is too large for closed vendors to cover
alone. Airbyte's connector model lets teams adapt less common systems. The
cloud product can then focus on enterprise SSO and security features such as
RBAC
([43:45-49:32]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
