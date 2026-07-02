---
layout: "person"
title: "Victoria Perez Mola"
summary: "Victoria Perez Mola's DataTalks.Club discussion of analytics engineering, dbt, SQL modeling, data quality, and BI reporting."
source_url: "https://datatalks.club/people/victoriaperezmola.html"
podcast_episodes: ["analytics-engineer-skills-tools"]
curated: "true"
expertise: ["analytics engineering", "dbt", "SQL transformations", "data modeling", "data quality", "business intelligence"]
github: "Victoriapm"
linkedin: "victoriaperezmola"
---

## Background

Victoria Perez Mola was born in Argentina and studied Systems Engineering. She moved into [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}) after working with ERP and finance reporting systems. In her [analytics engineering episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}), she described that path. She moved from helping finance teams automate reports toward owning modeled datasets for other data roles and business users.

## Analytics Engineering Between Analysts and Engineers

Victoria framed [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}) as the role between [data analysts and analytics engineers]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}) on one side and data engineers on the other. Analysts bring business context and should spend more time analyzing data than cleaning it. Data engineers bring infrastructure and software engineering practices. They may still lack the domain context needed to model business data.

The analytics engineer connects those sides by turning raw or semi-raw data into reliable tables and views. Victoria said companies added the role because analysts spent too much time on data cleaning. Engineers, meanwhile, focused on infrastructure and [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

She also cautioned that the role varies by company. Some teams expect analytics engineers to lean toward pipeline and tooling work. Others place them closer to reporting, dashboards, and business stakeholders. Her own description covered the full path from data loading and modeling to [BI]({{ '/wiki/business-intelligence/' | relative_url }}) exposure in Looker ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## SQL Modeling and dbt

Victoria treated [data modeling]({{ '/wiki/analytics-engineering/' | relative_url }}#modeling-and-semantic-layers) as practical SQL work, not only diagrams. In her day-to-day description, modeling meant writing SQL that creates tables or views for analysts and data scientists. She named SQL and dimensional modeling as core skills. She also expected analytics engineers to know fact tables, dimension tables, and warehouse concepts from Kimball ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Her main tool example was [dbt]({{ '/wiki/dbt/' | relative_url }}). She described dbt as the layer where the team writes SQL transformations and keeps model documentation in version control. dbt also avoids hand-written DDL for every table or view. It shows upstream and downstream dependencies as a DAG.

For Victoria, dbt mattered because it brought software development practices into data work. She mentioned GitHub repositories and YAML documentation. She also discussed macros, tests, peer review, and scheduled model runs through dbt Cloud ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Data Quality, Tests, and Upstream Limits

Victoria repeatedly tied the analytics engineer role to [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}). Her daily work included checking why data was unavailable or not clean, cleaning source data in dbt, and adding tests. She mentioned uniqueness tests, non-null checks, accepted ranges, and source checks that stop downstream models from being built on bad data. She described dbt tests as SQL queries that return failing rows and can produce warnings or errors ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

At the same time, she didn't present data quality as a problem an analytics engineer can solve alone. She said quality work never reaches a final state where all data is perfect. Some problems start upstream with backend events or source systems. Analytics engineers may not control raw data generation, but they often feel the impact first.

They also have to handle ad hoc investigation when numbers don't match. This makes the role both technical and organizational. Analytics engineers write tests and transformations, and they coordinate with backend engineers and data consumers when data breaks ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Looker, Metrics, and Business Consumption

Victoria placed Looker at the business-facing end of the stack. She described it as the [BI]({{ '/wiki/business-intelligence/' | relative_url }}) tool where business users consume modeled data through dashboards and reports. The data team uses dbt for transformations before exposing models downstream. This links analytics engineering to [metrics]({{ '/wiki/metrics/' | relative_url }}) work because the role turns backend events and external data into consistent datasets for reporting ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Her practical toolstack example started with S3 data arriving in Snowflake through an ETL tool. dbt handled SQL transformations, and Looker exposed reports. She mentioned that some companies ask analytics engineers for Python or distributed processing skills. In her own work, SQL and dbt mattered most alongside Snowflake, Adlib, and Looker ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Business Knowledge and Team Placement

Victoria's clearest theme was that analytics engineering sits at the boundary between business and technology. Analysts understand stakeholder questions and business logic. Engineers understand pipelines and production practices. Analytics engineers need enough of both to translate business models into reliable data models and enough technical judgment to make those models maintainable ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

She described two team placements. In a platform team, analytics engineers work on base datasets and shared modeling foundations. In embedded analytics teams, they sit closer to operations, commercial, or other business areas and talk more directly with stakeholders. In both cases, Victoria saw the work as a service layer for analysts and data scientists. Analytics engineers make data available, model it clearly, document it, and reduce the time other data roles spend cleaning before they can answer questions ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Role Fit and Learning Path

For someone moving from analyst or ERP work, Victoria suggested learning software development practices first. The same advice applies to BI or data engineering backgrounds. She also named strong SQL, dimensional modeling, and dbt. She referenced dbt learning material and analytics reading lists.

The deeper fit signal was interest in modeling and data quality. She also named documentation, peer review, and coding guidelines. In her view, people who enjoy making data reliable and reusable are closer to analytics engineering. People who only want to answer the final business question may fit better in analysis roles ([episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
