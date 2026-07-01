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
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
focuses on pipelines and platform data work.
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
covers modeled metrics and BI-ready marts.
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
covers modeling, baselines, evaluation, and production awareness.
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
covers retrieval-backed LLM systems with citations and evaluation.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) and
[Ellen König]({{ '/people/ellenkonig/' | relative_url }}) ground the data
engineering version. In
[Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
and
[How to Become a Data Engineer]({{ '/podcasts/from-software-engineering-data-science-to-data-engineering-leadership/' | relative_url }}),
they connect project evidence to fundamentals and clean code. They also connect
it to domain work and reviewable pipelines
([Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:49 / 2:22 / 2:46.
[How to Become a Data Engineer]({{ '/podcasts/from-software-engineering-data-science-to-data-engineering-leadership/' | relative_url }}),
41:29 / 44:00).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) ground
the analytics engineering version. Their episodes connect portfolio evidence to
SQL modeling, data quality, and documentation. They also connect it to business
reality and BI consumption
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
and
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
40:42 / 42:05 and 12:09 / 1:08:24).

[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) grounds
the machine learning version through baselines, validation, and production
robustness. [Ben Wilson]({{ '/people/benwilson/' | relative_url }}) and
[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) add maintainable code
and tests. They also add serving boundaries, monitoring, and software
integration
([Machine Learning System Design Interview]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
24:28 / 37:59.
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
52:14.
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}),
24:03 / 36:28).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) and
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) ground
the RAG version. Their episodes make chunking, retrieval evidence, citations,
and gold tests part of the project. Failure labels and traces aren't optional
polish
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
and
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
38:24 / 42:49 / 48:09 and 26:43 / 44:26).

## Common Definition

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

[Eugene Yan]({{ '/people/eugeneyan/' | relative_url }}) adds the writeup
standard in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}).
Around 20:18, he describes outlines, section headers, and topic sentences. He
also describes supporting evidence. That structure works for portfolio case
studies because the project has to explain its assumptions and evidence.

## Portfolio Signals Across Roles

Start with reviewable fundamentals instead of tool lists.
[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) says portfolios should
show Python, SQL, code structure, and tests. They should also show public or
personal projects in
[Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}).
Jeff gives that standard at 1:49, 2:22, and 2:46.
That advice applies to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) portfolios.

Every project needs a consumer, a decision, or a business question.
[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }}) frames projects as
resume evidence in
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}).
[Nick Singh]({{ '/people/nicksingh/' | relative_url }}) treats project
walkthroughs as interview evidence in
[Ace Data Interviews]({{ '/podcasts/data-interview-behavioral-and-portfolio-prep-guide/' | relative_url }}).
Luke gives the resume version at 19:50. Nick gives the interview walkthrough
version at 25:13, 27:50, 31:06, and 37:18.

This connects portfolio work to [job search]({{ '/wiki/job-search/' | relative_url }})
and [CV screening]({{ '/wiki/cv-screening/' | relative_url }}).

End-to-end proof beats notebook-only proof. [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
shows how a pipeline moves from ingestion to transformation, modeled outputs,
and consumers in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) adds modern-stack
boundaries in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Santona covers pipeline stages at 13:25, 18:44, and 26:43.

Natalie covers ingestion, transformation, marts, and warehouse boundaries from
3:19 through 17:55.
Those episodes support
[End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
as the concrete data-pipeline blueprint.

## Choosing A Project Type

Choose [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) when
the project should prove ingestion, modeling, orchestration, and recovery. The
best project has a real source behavior, a modeled output, and a rerun path.
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) grounds that choice in
pipeline stages, orchestration, and consumers
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
13:25 / 18:44 / 26:43). [End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
is the concrete data-pipeline blueprint.

Choose [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
when the project should prove business definitions and reusable SQL models. The
best project has source assumptions and table grain. It also has tests,
documentation, and a BI or query surface.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) connect
those signals to dbt and data quality. They also connect them to business
definitions and BI consumption
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
40:42 / 42:05.
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
12:09 / 1:08:24).
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
covers metric-centered portfolio evidence.

Choose [machine learning]({{ '/wiki/machine-learning/' | relative_url }}) when
the project should prove problem framing and data strategy. It also needs
baselines, evaluation, and software boundaries.
[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) anchors this
in baselines and validation. He also covers features, labels, and production
robustness
([Machine Learning System Design Interview]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
24:28 / 37:59 / 44:11).
[Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
fits target roles in [MLOps]({{ '/wiki/mlops/' | relative_url }}), ML platforms,
or machine learning engineering.

Choose [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) when
the project should prove retrieval quality and grounded generation. The best
project shows the corpus and chunks. It also shows metadata, retrieved evidence,
citations, and failure analysis.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) ties this to chunking
and embeddings. She also ties it to citations and evaluation
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24 / 42:49 / 48:09).
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
is the practical review checklist.

Choose [open source]({{ '/wiki/open-source/' | relative_url }}) when public
collaboration is the strongest evidence. A smaller issue or docs fix can be
more credible than a large unfinished app. A reproducible bug, test, or example
can work too.

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) grounds that
path in reproducible issues and small fixes. He also covers tests and CI.
Packaging and maintainer discussion matter too
([Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
25:50 / 27:40 / 29:30).
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and the
[Open Source Contributor Roadmap]({{ '/roadmaps/open-source-contributor-roadmap/' | relative_url }})
cover that path.

## Role-Specific Project Evidence

A project becomes credible when the repository and writeup expose the tradeoffs.
Data projects should show source behavior, table grain, and orchestration. They
should also show quality checks and recovery. Analytics projects should show
metric ownership and a consumption surface.

ML projects should show a baseline, validation, serving boundary, and monitoring
plan. RAG projects should show retrieval examples, citations, and failure
labels.

Don't add tools before the project needs them. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
ties modern tool choices to requirements in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) warns against
over-engineered platforms in
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).
Adrian's tool-selection guidance appears at 44:42. Slawomir's cost-aware
platform warning appears at 26:05, 26:22, 28:30, and 30:33.

The same rule applies to AI projects. Start with a reliable retrieval or model
baseline before adding agents, long-context tricks, or fine-tuning.
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
and
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
cover those design choices.

Production awareness is stronger than model novelty. [Ben Wilson]({{ '/people/benwilson/' | relative_url }})
connects maintainable code, tests, and production engineering in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) shows the
notebook-to-production path in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
Ben's maintainability and testing discussion starts at 8:49.

Mariano's end-to-end production ownership discussion starts at 16:29 and
continues through monitoring and evaluation at 22:05 and 26:32.
[Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
keeps production-readiness claims tied to reviewable evidence.

RAG and AI projects need evidence, not only a chat UI. Strong RAG portfolios
expose corpus choice, chunking, metadata, and retrieval baselines. They also
show citations, logs, and failure analysis.
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
covers those review points.

## Public Proof And Open Source

Open-source work is portfolio evidence when review pressure is visible. Issues,
docs, tests, and demos can be stronger than a private tutorial repository. Pull
requests, CI, and maintainer discussion strengthen the proof.

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) treats
open-source contribution as practical work in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) shows how public
Hugging Face work, model cards, demos, and community contributions create NLP
portfolio evidence in
[Hugging Face Contributions and NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
Vincent grounds the contributor path at 25:50, 27:40, and 29:30. Merve grounds
the Hugging Face path at 17:37, 23:26, 25:09, and 51:12.

Kaggle and competitions count when they're repackaged as engineering evidence.
[Andrada Olteanu]({{ '/people/andradaolteanu/' | relative_url }}) connects
Kaggle work to an analytics-to-data-science transition in
[Analytics to Data Science with Kaggle]({{ '/podcasts/analytics-to-data-science-with-kaggle-portfolio/' | relative_url }}).
[Tatiana Gabruseva]({{ '/people/tatianagabruseva/' | relative_url }}) pushes
competition work beyond leaderboard chasing in
[Competitions Beyond the Kaggle Leaderboard]({{ '/podcasts/s24e01-competitions-beyond-kaggle-leaderboard/' | relative_url }}).
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

The hiring context connects to [Job Search]({{ '/wiki/job-search/' | relative_url }})
and the longer arc connects to [Career Development]({{ '/wiki/career-development/' | relative_url }}).
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
covers projects discussed as system design examples.

## Guest Differences

Guests differ on which proof matters most because each role values a different
signal. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) asks for Python
and SQL. He also asks for clean code, tests, and open-source review pressure
([Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:49 / 2:22 / 2:46). [Ellen König]({{ '/people/ellenkonig/' | relative_url }})
adds professional software habits and domain-specific pipeline projects
([How to Become a Data Engineer]({{ '/podcasts/from-software-engineering-data-science-to-data-engineering-leadership/' | relative_url }}),
26:20 / 41:29 / 44:00).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) connect
reusable models to metric definitions and data quality. They also connect those
models to business reality
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
40:42 / 42:05.
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
12:09 / 1:08:24).

[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) asks for
baselines and validation. [Ben Wilson]({{ '/people/benwilson/' | relative_url }})
and [Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) add production
and software boundaries
([Machine Learning System Design Interview]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
24:28 / 37:59 / 44:11.
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
8:49 / 52:14.
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}),
24:03 / 36:28).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) and
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) focus on
retrieval evidence and citations. They also focus on failure analysis and gold
tests
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24 / 42:49 / 48:09.
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
26:43 / 44:26). [Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }})
and [Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) focus on public
review, docs, and community-visible work
([Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
25:50 / 27:40 / 29:30.
[Hugging Face Contributions and NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}),
17:37 / 23:26 / 51:12).

The common thread is reviewability. A project can be small if another person can
understand the decision, run the work, look at the evidence, and challenge the
tradeoffs.

## Related Pages

These pages cover project types and role-specific checklists.

- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
- [Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
- [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
- [Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})
