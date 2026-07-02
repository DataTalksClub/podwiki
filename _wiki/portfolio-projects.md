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

[Jeff Katz](https://datatalks.club/people/jeffkatz.html) and
[Ellen König](https://datatalks.club/people/ellenkonig.html) ground the data
engineering version. In
[Data Engineering Job Prep](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html)
and
[How to Become a Data Engineer](https://datatalks.club/podcast/from-software-engineering-data-science-to-data-engineering-leadership.html),
they connect project evidence to fundamentals and clean code. They also connect
it to domain work and reviewable pipelines.
Use the data engineering job-prep clips at
[1:49, 2:22, and 2:46](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html).
Use the transition clips at
[41:29 and 44:00](https://datatalks.club/podcast/from-software-engineering-data-science-to-data-engineering-leadership.html).

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html) and
[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html) ground
the analytics engineering version. Their episodes connect portfolio evidence to
SQL modeling, data quality, and documentation. They also connect it to business
reality and BI consumption.
Use the analytics-engineering skills clips at
[40:42 and 42:05](https://datatalks.club/podcast/analytics-engineer-skills-tools.html).
Use the foundations clips at
[12:09 and 1:08:24](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html).

[Valeriy Babushkin](https://datatalks.club/people/valeriybabushkin.html) grounds
the machine learning version through baselines, validation, and production
robustness. [Ben Wilson](https://datatalks.club/people/benwilson.html) and
[Nadia Nahar](https://datatalks.club/people/nadianahar.html) add maintainable code
and tests. They also add serving boundaries, monitoring, and software
integration. Use the system-design interview clips at
[24:28 and 37:59](https://datatalks.club/podcast/machine-learning-system-design-interview.html),
the production-ML clip at
[52:14](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html),
and the software-engineering clips at
[24:03 and 36:28](https://datatalks.club/podcast/software-engineering-for-machine-learning.html).

[Atita Arora](https://datatalks.club/people/atitaarora.html) and
[Hugo Bowne-Anderson](https://datatalks.club/people/hugobowneanderson.html) ground
the RAG version. Their episodes make chunking, retrieval evidence, citations,
and gold tests part of the project. Failure labels and traces aren't optional
polish. Use the modern-search clips at
[38:24, 42:49, and 48:09](https://datatalks.club/podcast/modern-search-systems-vector-databases-llms-semantic-retrieval.html).
Use the practical-RAG clips at
[26:43 and 44:26](https://datatalks.club/podcast/practical-llm-engineering-and-rag.html).

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

[Eugene Yan](https://datatalks.club/people/eugeneyan.html) adds the writeup
standard in
[Technical Writing for Data Scientists](https://datatalks.club/podcast/technical-writing-for-data-scientists.html).
Around 20:18, he describes outlines, section headers, and topic sentences. He
also describes supporting evidence. That structure works for portfolio case
studies because the project has to explain its assumptions and evidence.

## Portfolio Signals Across Roles

Start with reviewable fundamentals instead of tool lists.
[Jeff Katz](https://datatalks.club/people/jeffkatz.html) says portfolios should
show Python, SQL, code structure, and tests. They should also show public or
personal projects in
[Data Engineering Job Prep](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html).
Jeff gives that standard at 1:49, 2:22, and 2:46.
That advice applies to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) portfolios.

Every project needs a consumer, a decision, or a business question.
[Luke Whipps](https://datatalks.club/people/lukewhipps.html) frames projects as
resume evidence in
[Land Data Scientist Roles](https://datatalks.club/podcast/get-data-scientist-job.html).
[Nick Singh](https://datatalks.club/people/nicksingh.html) treats project
walkthroughs as interview evidence in
[Ace Data Interviews](https://datatalks.club/podcast/data-interview-behavioral-and-portfolio-prep-guide.html).
Luke gives the resume version at 19:50. Nick gives the interview walkthrough
version at 25:13, 27:50, 31:06, and 37:18.

Portfolio work becomes part of [job search]({{ '/wiki/job-search/' | relative_url }})
and [CV screening]({{ '/wiki/cv-screening/' | relative_url }}) when it gives
hiring teams concrete evidence to review.

End-to-end proof beats notebook-only proof. [Santona Tuli](https://datatalks.club/people/santonatuli.html)
shows how a pipeline moves from ingestion to transformation, modeled outputs,
and consumers in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html).
[Natalie Kwong](https://datatalks.club/people/nataliekwong.html) adds modern-stack
boundaries in
[ETL vs ELT and the Modern Data Stack](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html).
Santona covers pipeline stages at 13:25, 18:44, and 26:43.

Natalie covers ingestion, transformation, marts, and warehouse boundaries from
3:19 through 17:55.
Those episodes support
[End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
as the concrete data-pipeline blueprint.

## Choosing a Project Type

Choose [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) when
the project should prove ingestion, modeling, orchestration, and recovery. The
best project has a real source behavior, a modeled output, and a rerun path.
[Santona Tuli](https://datatalks.club/people/santonatuli.html) grounds that choice in
pipeline stages, orchestration, and consumers
([Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
13:25 / 18:44 / 26:43). [End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
is the concrete data-pipeline blueprint.

Choose [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
when the project should prove business definitions and reusable SQL models. The
best project has source assumptions and table grain. It also has tests,
documentation, and a BI or query surface.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html) and
[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html) connect
those signals to dbt and data quality. They also connect them to business
definitions and BI consumption
([Master Analytics Engineering](https://datatalks.club/podcast/analytics-engineer-skills-tools.html),
40:42 / 42:05.
[Foundations of the Analytics Engineer Role](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html),
12:09 / 1:08:24).
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
covers metric-centered portfolio evidence.

Choose [machine learning]({{ '/wiki/machine-learning/' | relative_url }}) when
the project should prove problem framing and data strategy. It also needs
baselines, evaluation, and software boundaries.
[Valeriy Babushkin](https://datatalks.club/people/valeriybabushkin.html) anchors this
in baselines and validation. He also covers features, labels, and production
robustness
([Machine Learning System Design Interview](https://datatalks.club/podcast/machine-learning-system-design-interview.html),
24:28 / 37:59 / 44:11).
[Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
fits target roles in [MLOps]({{ '/wiki/mlops/' | relative_url }}), ML platforms,
or machine learning engineering.

Choose [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) when
the project should prove retrieval quality and grounded generation. The best
project shows the corpus and chunks. It also shows metadata, retrieved evidence,
citations, and failure analysis.

[Atita Arora](https://datatalks.club/people/atitaarora.html) ties this to chunking
and embeddings. She also ties it to citations and evaluation
([Modern Search Systems](https://datatalks.club/podcast/modern-search-systems-vector-databases-llms-semantic-retrieval.html),
38:24 / 42:49 / 48:09).
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
is the practical review checklist.

Choose [open source]({{ '/wiki/open-source/' | relative_url }}) when public
collaboration is the strongest evidence. A smaller issue or docs fix can be
more credible than a large unfinished app. A reproducible bug, test, or example
can work too.

[Vincent Warmerdam](https://datatalks.club/people/vincentwarmerdam.html) grounds that
path in reproducible issues and small fixes. He also covers tests and CI.
Packaging and maintainer discussion matter too
([Contribute to Open Source ML](https://datatalks.club/podcast/open-source-ml-contributions.html),
25:50 / 27:40 / 29:30).
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and the
[Open Source Contributor Roadmap]({{ '/wiki/open-source-contributor-roadmap/' | relative_url }})
cover that path.

## Role-Specific Project Evidence

A project becomes credible when the repository and writeup expose the tradeoffs.
Data projects should show source behavior, table grain, and orchestration. They
should also show quality checks and recovery. Analytics projects should show
metric ownership and a consumption surface.

ML projects should show a baseline, validation, serving boundary, and monitoring
plan. RAG projects should show retrieval examples, citations, and failure
labels.

Don't add tools before the project needs them. [Adrian Brudaru](https://datatalks.club/people/adrianbrudaru.html)
ties modern tool choices to requirements in
[Modern Data Engineering Trends](https://datatalks.club/podcast/trends-in-modern-data-engineering.html).
[Slawomir Tulski](https://datatalks.club/people/slawomirtulski.html) warns against
over-engineered platforms in
[Data Engineer Career in 2026](https://datatalks.club/podcast/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for.html).
Adrian's tool-selection guidance appears at 44:42. Slawomir's cost-aware
platform warning appears at 26:05, 26:22, 28:30, and 30:33.

The same rule applies to AI projects. Start with a reliable retrieval or model
baseline before adding agents, long-context tricks, or fine-tuning.
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
and
[Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
cover those design choices.

Production awareness is stronger than model novelty. [Ben Wilson](https://datatalks.club/people/benwilson.html)
connects maintainable code, tests, and production engineering in
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html).
[Mariano Semelman](https://datatalks.club/people/marianosemelman.html) shows the
notebook-to-production path in
[From Notebook to Production](https://datatalks.club/podcast/s24e03-from-notebook-to-production-building-end-to-end-ai-systems.html).
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

## Public Proof and Open Source

Open-source work is portfolio evidence when review pressure is visible. Issues,
docs, tests, and demos can be stronger than a private tutorial repository. Pull
requests, CI, and maintainer discussion strengthen the proof.

[Vincent Warmerdam](https://datatalks.club/people/vincentwarmerdam.html) treats
open-source contribution as practical work in
[Contribute to Open Source ML](https://datatalks.club/podcast/open-source-ml-contributions.html).
[Merve Noyan](https://datatalks.club/people/mervenoyan.html) shows how public
Hugging Face work, model cards, demos, and community contributions create NLP
portfolio evidence in
[Hugging Face Contributions and NLP Portfolio](https://datatalks.club/podcast/hugging-face-contributions-and-nlp-portfolio.html).
Vincent grounds the contributor path at 25:50, 27:40, and 29:30. Merve grounds
the Hugging Face path at 17:37, 23:26, 25:09, and 51:12.

Kaggle and competitions count when they're repackaged as engineering evidence.
[Andrada Olteanu](https://datatalks.club/people/andradaolteanu.html) connects
Kaggle work to an analytics-to-data-science transition in
[Analytics to Data Science with Kaggle](https://datatalks.club/podcast/analytics-to-data-science-with-kaggle-portfolio.html).
[Tatiana Gabruseva](https://datatalks.club/people/tatianagabruseva.html) pushes
competition work beyond leaderboard chasing in
[Competitions Beyond the Kaggle Leaderboard](https://datatalks.club/podcast/s24e01-competitions-beyond-kaggle-leaderboard.html).
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

## Role-Specific Review Signals

Guests differ on which proof matters most because each role values a different
signal. [Jeff Katz](https://datatalks.club/people/jeffkatz.html) asks for Python
and SQL. He also asks for clean code, tests, and open-source review pressure
([Data Engineering Job Prep](https://datatalks.club/podcast/get-data-engineering-job-prep-and-interview.html),
1:49 / 2:22 / 2:46). [Ellen König](https://datatalks.club/people/ellenkonig.html)
adds professional software habits and domain-specific pipeline projects
([How to Become a Data Engineer](https://datatalks.club/podcast/from-software-engineering-data-science-to-data-engineering-leadership.html),
26:20 / 41:29 / 44:00).

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html) and
[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html) connect
reusable models to metric definitions and data quality. They also connect those
models to business reality
([Master Analytics Engineering](https://datatalks.club/podcast/analytics-engineer-skills-tools.html),
40:42 / 42:05.
[Foundations of the Analytics Engineer Role](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html),
12:09 / 1:08:24).

[Valeriy Babushkin](https://datatalks.club/people/valeriybabushkin.html) asks for
baselines and validation. [Ben Wilson](https://datatalks.club/people/benwilson.html)
and [Nadia Nahar](https://datatalks.club/people/nadianahar.html) add production
and software boundaries
([Machine Learning System Design Interview](https://datatalks.club/podcast/machine-learning-system-design-interview.html),
24:28 / 37:59 / 44:11.
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html),
8:49 / 52:14.
[Software Engineering for ML](https://datatalks.club/podcast/software-engineering-for-machine-learning.html),
24:03 / 36:28).

[Atita Arora](https://datatalks.club/people/atitaarora.html) and
[Hugo Bowne-Anderson](https://datatalks.club/people/hugobowneanderson.html) focus on
retrieval evidence and citations. They also focus on failure analysis and gold
tests
([Modern Search Systems](https://datatalks.club/podcast/modern-search-systems-vector-databases-llms-semantic-retrieval.html),
38:24 / 42:49 / 48:09.
[Practical LLM Engineering and RAG](https://datatalks.club/podcast/practical-llm-engineering-and-rag.html),
26:43 / 44:26). [Vincent Warmerdam](https://datatalks.club/people/vincentwarmerdam.html)
and [Merve Noyan](https://datatalks.club/people/mervenoyan.html) focus on public
review, docs, and community-visible work
([Contribute to Open Source ML](https://datatalks.club/podcast/open-source-ml-contributions.html),
25:50 / 27:40 / 29:30.
[Hugging Face Contributions and NLP Portfolio](https://datatalks.club/podcast/hugging-face-contributions-and-nlp-portfolio.html),
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
