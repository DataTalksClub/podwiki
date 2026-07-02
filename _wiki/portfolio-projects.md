---
layout: wiki
title: "Portfolio Projects"
summary: "Guidance for choosing data, analytics, ML, AI, and open-source portfolio projects that prove role fit, practical judgment, public proof, and interview-ready ownership."
related:
  - Career Development
  - Job Search
  - CV Screening
  - Data Engineering Portfolio Projects
  - Analytics Engineering Portfolio Projects
  - Machine Learning Portfolio Projects
  - RAG Portfolio Projects
  - Open Source Portfolio Evidence
  - End-to-End Data Pipeline Project
  - Dashboard and Metric Layer Project Checklist
  - Production ML Project Checklist
  - Search and RAG Project Checklist
---

A portfolio project is public evidence of judgment, not a tool demo. It
connects a real problem to data, code, and evaluation. It also shows operation
and a defensible interview story.

Project choices split by role.
[[Data Engineering Portfolio Projects]]
focuses on pipelines and platform data work.
[[Analytics Engineering Portfolio Projects]]
covers modeled metrics and BI-ready marts.
[[Machine Learning Portfolio Projects]]
covers modeling, baselines, evaluation, and production awareness.
[[RAG Portfolio Projects]]
covers retrieval-backed LLM systems with citations and evaluation.

[[person:jeffkatz|Jeff Katz]] and
[[person:ellenkonig|Ellen König]] ground the data
engineering version. In
[[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep]]
and
[[podcast:from-software-engineering-data-science-to-data-engineering-leadership|How to Become a Data Engineer]],
they connect project evidence to fundamentals and clean code. They also connect
it to domain work and reviewable pipelines.
Use the data engineering job-prep clips at
[[podcast:get-data-engineering-job-prep-and-interview|1:49, 2:22, and 2:46]].
Use the transition clips at
[[podcast:from-software-engineering-data-science-to-data-engineering-leadership|41:29 and 44:00]].

[[person:victoriaperezmola|Victoria Perez Mola]] and
[[person:juanmanuelperafan|Juan Manuel Perafan]] ground
the analytics engineering version. Their episodes connect portfolio evidence to
SQL modeling, data quality, and documentation. They also connect it to business
reality and BI consumption.
Use the analytics-engineering skills clips at
[[podcast:analytics-engineer-skills-tools|40:42 and 42:05]].
Use the foundations clips at
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|12:09 and 1:08:24]].

[[person:valeriybabushkin|Valeriy Babushkin]] grounds
the machine learning version through baselines, validation, and production
robustness. [[person:benwilson|Ben Wilson]] and
[[person:nadianahar|Nadia Nahar]] add maintainable code
and tests. They also add serving boundaries, monitoring, and software
integration. Use the system-design interview clips at
[[podcast:machine-learning-system-design-interview|24:28 and 37:59]],
the production-ML clip at
[[podcast:machine-learning-engineering-production-best-practices|52:14]],
and the software-engineering clips at
[[podcast:software-engineering-for-machine-learning|24:03 and 36:28]].

[[person:atitaarora|Atita Arora]] and
[[person:hugobowneanderson|Hugo Bowne-Anderson]] ground
the RAG version. Their episodes make chunking, retrieval evidence, citations,
and gold tests part of the project. Failure labels and traces aren't optional
polish. Use the modern-search clips at
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|38:24, 42:49, and 48:09]].
Use the practical-RAG clips at
[[podcast:practical-llm-engineering-and-rag|26:43 and 44:26]].

## Reviewable Project Standard

A strong portfolio project makes the work reviewable by naming the consumer or
decision. It shows the input data and the transformation or modeling path. It
includes quality checks, evaluation, or both. It also has a README or writeup
that lets another person run, review, or question the work.

The project should answer these review questions:

- What decision or workflow changes if the project works?
- Which data enters the system, and what assumptions come with it?
- Which baseline or simpler version does the project improve on?
- Which checks catch bad data, bad logic, weak retrieval, or model failure?
- How can a reviewer run the project or look at the result?

[[person:eugeneyan|Eugene Yan]] adds the writeup
standard in
[[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]].
Around 20:18, he describes outlines, section headers, and topic sentences. He
also describes supporting evidence. That structure works for portfolio case
studies because the project has to explain its assumptions and evidence.

## Portfolio Signals Across Roles

Start with reviewable fundamentals instead of tool lists.
[[person:jeffkatz|Jeff Katz]] says portfolios should
show Python, SQL, code structure, and tests. They should also show public or
personal projects in
[[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep]].
Jeff gives that standard at 1:49, 2:22, and 2:46.
That advice applies to
[[data engineering]],
[[analytics engineering]],
[[machine learning]], and
[[AI engineering]] portfolios.

Every project needs a consumer, a decision, or a business question.
[[person:lukewhipps|Luke Whipps]] frames projects as
resume evidence in
[[podcast:get-data-scientist-job|Land Data Scientist Roles]].
[[person:nicksingh|Nick Singh]] treats project
walkthroughs as interview evidence in
[[podcast:data-interview-behavioral-and-portfolio-prep-guide|Ace Data Interviews]].
Luke gives the resume version at 19:50. Nick gives the interview walkthrough
version at 25:13, 27:50, 31:06, and 37:18.

Portfolio work becomes part of [[job search]]
and [[CV screening]] when it gives
hiring teams concrete evidence to review.

End-to-end proof beats notebook-only proof. [[person:santonatuli|Santona Tuli]]
shows how a pipeline moves from ingestion to transformation, modeled outputs,
and consumers in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].
[[person:nataliekwong|Natalie Kwong]] adds modern-stack
boundaries in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Santona covers pipeline stages at 13:25, 18:44, and 26:43.

Natalie covers ingestion, transformation, marts, and warehouse boundaries from
3:19 through 17:55.
Those episodes support
[[end-to-end-data-pipeline-project|End-to-End Data Pipeline Project]]
as the concrete data-pipeline blueprint.

## Choosing a Project Type

Choose [[data engineering]] when
the project should prove ingestion, modeling, orchestration, and recovery. The
best project has a real source behavior, a modeled output, and a rerun path.
[[person:santonatuli|Santona Tuli]] grounds that choice in
pipeline stages, orchestration, and consumers
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]],
13:25 / 18:44 / 26:43). [[end-to-end-data-pipeline-project|End-to-End Data Pipeline Project]]
is the concrete data-pipeline blueprint.

Choose [[analytics engineering]]
when the project should prove business definitions and reusable SQL models. The
best project has source assumptions and table grain. It also has tests,
documentation, and a BI or query surface.

[[person:victoriaperezmola|Victoria Perez Mola]] and
[[person:juanmanuelperafan|Juan Manuel Perafan]] connect
those signals to dbt and data quality. They also connect them to business
definitions and BI consumption
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]],
40:42 / 42:05.
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]],
12:09 / 1:08:24).
[[Dashboard and Metric Layer Project Checklist]]
covers metric-centered portfolio evidence.

Choose [[machine learning]] when
the project should prove problem framing and data strategy. It also needs
baselines, evaluation, and software boundaries.
[[person:valeriybabushkin|Valeriy Babushkin]] anchors this
in baselines and validation. He also covers features, labels, and production
robustness
([[podcast:machine-learning-system-design-interview|Machine Learning System Design Interview]],
24:28 / 37:59 / 44:11).
[[Production ML Project Checklist]]
fits target roles in [[MLOps]], ML platforms,
or machine learning engineering.

Choose [[retrieval-augmented-generation|RAG]] when
the project should prove retrieval quality and grounded generation. The best
project shows the corpus and chunks. It also shows metadata, retrieved evidence,
citations, and failure analysis.

[[person:atitaarora|Atita Arora]] ties this to chunking
and embeddings. She also ties it to citations and evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
38:24 / 42:49 / 48:09).
[[Search and RAG Project Checklist]]
is the practical review checklist.

Choose [[open source]] when public
collaboration is the strongest evidence. A smaller issue or docs fix can be
more credible than a large unfinished app. A reproducible bug, test, or example
can work too.

[[person:vincentwarmerdam|Vincent Warmerdam]] grounds that
path in reproducible issues and small fixes. He also covers tests and CI.
Packaging and maintainer discussion matter too
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]],
25:50 / 27:40 / 29:30).
[[Open Source Portfolio Evidence]]
and the
[[Open Source Contributor Roadmap]]
cover that path.

## Role-Specific Project Evidence

A project becomes credible when the repository and writeup expose the tradeoffs.
Data projects should show source behavior, table grain, and orchestration. They
should also show quality checks and recovery. Analytics projects should show
metric ownership and a consumption surface.

ML projects should show a baseline, validation, serving boundary, and monitoring
plan. RAG projects should show retrieval examples, citations, and failure
labels.

Don't add tools before the project needs them. [[person:adrianbrudaru|Adrian Brudaru]]
ties modern tool choices to requirements in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]].
[[person:slawomirtulski|Slawomir Tulski]] warns against
over-engineered platforms in
[[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]].
Adrian's tool-selection guidance appears at 44:42. Slawomir's cost-aware
platform warning appears at 26:05, 26:22, 28:30, and 30:33.

The same rule applies to AI projects. Start with a reliable retrieval or model
baseline before adding agents, long-context tricks, or fine-tuning.
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
and
[[Graph RAG vs Vector RAG]]
cover those design choices.

Production awareness is stronger than model novelty. [[person:benwilson|Ben Wilson]]
connects maintainable code, tests, and production engineering in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
[[person:marianosemelman|Mariano Semelman]] shows the
notebook-to-production path in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
Ben's maintainability and testing discussion starts at 8:49.

Mariano's end-to-end production ownership discussion starts at 16:29 and
continues through monitoring and evaluation at 22:05 and 26:32.
[[Production ML Project Checklist]]
keeps production-readiness claims tied to reviewable evidence.

RAG and AI projects need evidence, not only a chat UI. Strong RAG portfolios
expose corpus choice, chunking, metadata, and retrieval baselines. They also
show citations, logs, and failure analysis.
[[Search and RAG Project Checklist]]
covers those review points.

## Public Proof and Open Source

Open-source work is portfolio evidence when review pressure is visible. Issues,
docs, tests, and demos can be stronger than a private tutorial repository. Pull
requests, CI, and maintainer discussion strengthen the proof.

[[person:vincentwarmerdam|Vincent Warmerdam]] treats
open-source contribution as practical work in
[[podcast:open-source-ml-contributions|Contribute to Open Source ML]].
[[person:mervenoyan|Merve Noyan]] shows how public
Hugging Face work, model cards, demos, and community contributions create NLP
portfolio evidence in
[[podcast:hugging-face-contributions-and-nlp-portfolio|Hugging Face Contributions and NLP Portfolio]].
Vincent grounds the contributor path at 25:50, 27:40, and 29:30. Merve grounds
the Hugging Face path at 17:37, 23:26, 25:09, and 51:12.

Kaggle and competitions count when they're repackaged as engineering evidence.
[[person:andradaolteanu|Andrada Olteanu]] connects
Kaggle work to an analytics-to-data-science transition in
[[podcast:analytics-to-data-science-with-kaggle-portfolio|Analytics to Data Science with Kaggle]].
[[person:tatianagabruseva|Tatiana Gabruseva]] pushes
competition work beyond leaderboard chasing in
[[podcast:s24e01-competitions-beyond-kaggle-leaderboard|Competitions Beyond the Kaggle Leaderboard]].
Andrada's public-notebook portfolio discussion starts at 32:14 and 36:41.
Tatiana's competition discussion starts at 8:06 and separates learning from
career use at 11:45.

Decomposition and reproducible code create the public proof, while README
quality and domain explanation matter too.

## Interview Readiness

A portfolio project should be easy to discuss under interview pressure. The
candidate should explain why the project matters and which simpler baseline
came first. They should also explain which parts failed and what they would
change with more time.

The hiring context connects to [[Job Search]]
and the longer arc connects to [[Career Development]].
[[Machine Learning System Design]]
covers projects discussed as system design examples.

## Role-Specific Review Signals

Guests differ on which proof matters most because each role values a different
signal. [[person:jeffkatz|Jeff Katz]] asks for Python
and SQL. He also asks for clean code, tests, and open-source review pressure
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep]],
1:49 / 2:22 / 2:46). [[person:ellenkonig|Ellen König]]
adds professional software habits and domain-specific pipeline projects
([[podcast:from-software-engineering-data-science-to-data-engineering-leadership|How to Become a Data Engineer]],
26:20 / 41:29 / 44:00).

[[person:victoriaperezmola|Victoria Perez Mola]] and
[[person:juanmanuelperafan|Juan Manuel Perafan]] connect
reusable models to metric definitions and data quality. They also connect those
models to business reality
([[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]],
40:42 / 42:05.
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]],
12:09 / 1:08:24).

[[person:valeriybabushkin|Valeriy Babushkin]] asks for
baselines and validation. [[person:benwilson|Ben Wilson]]
and [[person:nadianahar|Nadia Nahar]] add production
and software boundaries
([[podcast:machine-learning-system-design-interview|Machine Learning System Design Interview]],
24:28 / 37:59 / 44:11.
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]],
8:49 / 52:14.
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]],
24:03 / 36:28).

[[person:atitaarora|Atita Arora]] and
[[person:hugobowneanderson|Hugo Bowne-Anderson]] focus on
retrieval evidence and citations. They also focus on failure analysis and gold
tests
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
38:24 / 42:49 / 48:09.
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
26:43 / 44:26). [[person:vincentwarmerdam|Vincent Warmerdam]]
and [[person:mervenoyan|Merve Noyan]] focus on public
review, docs, and community-visible work
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]],
25:50 / 27:40 / 29:30.
[[podcast:hugging-face-contributions-and-nlp-portfolio|Hugging Face Contributions and NLP Portfolio]],
17:37 / 23:26 / 51:12).

The common thread is reviewability. A project can be small if another person can
understand the decision, run the work, look at the evidence, and challenge the
tradeoffs.

## Related Pages

These pages cover project types and role-specific checklists.

- [[Data Engineering Portfolio Projects]]
- [[Analytics Engineering Portfolio Projects]]
- [[Machine Learning Portfolio Projects]]
- [[RAG Portfolio Projects]]
- [[end-to-end-data-pipeline-project|End-to-End Data Pipeline Project]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[Production ML Project Checklist]]
- [[Search and RAG Project Checklist]]
- [[Open Source Portfolio Evidence]]
- [[Job Search]]
