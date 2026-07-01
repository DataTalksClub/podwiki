---
layout: "person"
title: "Mehdi OUAZZA"
summary: "Mehdi OUAZZA's DataTalks.Club podcast discussions, organized for topic exploration."
source_url: "https://datatalks.club/people/mehdiouazza.html"
podcast_episodes: ["scaling-data-engineering-teams-self-service-platforms"]
curated: "true"
github: "mehd-io"
twitter: "mehd_io"
linkedin: "mehd-io"
web: "https://mehd.io/"
expertise: ["data engineering", "data engineering platforms", "self-service data platforms", "Kafka", "data governance", "technical leadership"]
---

## Background

Mehdi OUAZZA is a data engineer, entrepreneur, and technical content creator. In his DataTalks.Club conversation on [scaling data engineering teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}), he described a path from classic BI and on-prem Big Data work into staff-level [data engineering]({{ '/wiki/data-engineering/' | relative_url }}). His work spans batch and streaming pipelines, data modeling, and orchestration. It also covers infrastructure and analytics.

## Scaling Data Engineering In Hypergrowth

Mehdi framed a scale-up as a company where user growth, hiring, funding pressure, and product pressure rise together. Leaders aren't only dealing with more traffic. They're also coordinating more internal users, more stakeholders, and more decisions before the organization has settled its habits. In that setting, he said [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) teams constantly trade speed against quality. They must keep onboarding smooth while asking whether internal data products can scale with the company ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

He warned that shortcuts become expensive sooner in a scale-up than in a small startup. A pipeline, spreadsheet workflow, or manual fix may work for one narrow use case. A new market, a large customer, or a burst of analyst demand can make the same choice break under volume and coordination pressure ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Self-Service Platforms And Onboarding

Mehdi treated [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}) as internal products for analysts, data scientists, analytics engineers, and other data consumers. The platform team should avoid becoming a dependency. It does that with tools, documentation, support channels, and onboarding paths that help other data people build and operate their own pipelines ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

He connected [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}) and [self-service analytics]({{ '/wiki/self-service-data-platforms/' | relative_url }}) to more than Airflow, storage, or cloud infrastructure. Mehdi said the team also needs education, clear documentation, reactive support, and realistic assumptions about users' technical level. Without those operating habits, a team may ship tools. It can still become the bottleneck for every new pipeline or data use case ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Naming Conventions And Sequencing Rules

When the conversation turned to whether a data platform is an Airflow cluster, Mehdi pushed the definition toward the rules around the tool. He named pipeline structure, Airflow sequencing, and naming conventions. He also mentioned YAML-generated DAGs, playbooks, and best practices for repeated pipeline families. These guardrails keep a fast-growing platform usable after the tenth or twentieth similar pipeline appears ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

Teams practicing [DataOps]({{ '/wiki/dataops/' | relative_url }}) or driving [platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}) need repeatable conventions before usage sprawls. Mehdi's point wasn't to over-engineer every early pipeline. Teams should notice when they keep copying similar work and invest in a reusable framework before the platform becomes hard to control ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Kafka, Streaming, And Data Contracts

Mehdi used [Kafka and streaming]({{ '/wiki/streaming/' | relative_url }}) as the clearest example of why scale-ups need experienced engineers early. Consuming a topic or making a high-level architecture decision is different from running Kafka as a production service that other teams depend on. He described how one or two topics can quickly become hundreds, making early choices about schemas, ownership, and change processes difficult to unwind ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

For [data governance]({{ '/wiki/data-governance/' | relative_url }}), he recommended data contracts with producers. Those contracts should define typed schemas, schema registry usage, controlled schema evolution, and guidelines for new users. Without that, software teams may publish flexible JSON for service-to-service use. Downstream data teams then absorb parsing work, model drift, warehouse cost, and breakage caused by poorly governed source events ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Senior Hiring And Team Growth

Mehdi argued that scale-ups shouldn't rely only on junior engineers to create systems that must scale immediately. Senior engineers set architecture decisions and establish best practices. They also bring prior experience with niche technologies such as Kafka or cloud migrations. Even strong engineers need time to learn unfamiliar operational failure modes. Scale-ups often don't have that time when traffic or product launches arrive next month ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

He still saw scale-ups as useful environments for junior growth because the work exposes people to real projects, rapid feedback, and visible impact. He described senior engineers leading platform architecture. Juniors and mid-level engineers can grow through delivery, documentation, and open source. Writing and broader collaboration also help. That ties his hiring view to [career development]({{ '/wiki/career-development/' | relative_url }}) and [technical leadership]({{ '/wiki/leadership/' | relative_url }}) rather than to hiring headcount alone ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Platform Operating Habits

Mehdi's operating advice was to make recurring pain visible and negotiate time to fix it. A senior data engineer shouldn't only complete team tickets. They should step back, talk with neighboring teams, identify shared platform problems, and create work that helps multiple teams. In his promotion framing, engineers grow by expanding their impact from one team to adjacent teams and company-wide engineering concerns ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

He also recommended reverse interviews for candidates evaluating scale-ups. Asking future teammates about boring work, weekend expectations, and the team's mood helps reveal whether the company has a healthy culture. Candidates can use those answers to judge how the team balances urgent delivery with platform improvement. That habit matters because scale-ups can create rapid learning. They can also trap engineers in repeated firefighting if managers and teams don't protect time for better systems ([episode]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).
