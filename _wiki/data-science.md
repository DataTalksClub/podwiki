---
layout: wiki
title: "Data Science"
summary: "How the DataTalks.Club podcast archive frames data science: product-facing modeling, analysis, experimentation, hiring signals, role ambiguity, and the boundary with ML, data engineering, and AI engineering."
related:
  - Machine Learning
  - Data Engineering
  - Experimentation and Causal Inference
  - Machine Learning System Design
  - Responsible AI and Governance
  - AI
---

## Definition

Data science uses data, statistics, machine learning, experimentation, domain
knowledge, and communication to improve decisions or products. In early
DataTalks.Club episodes, data scientists are distinguished from analysts by
their focus on prediction and product integration. Later episodes show that the
title varies widely across companies. Some data scientists do product analytics,
some build models, some deploy systems, and some cover data engineering as well.

The archive's strongest practical definition is this: data science turns a
business or product question into a data-backed analysis, model, experiment, or
decision workflow, then communicates the result in a way the organization can
use.

## Contents

Use these sections to separate the broad role topic from nearby technical pages.

- [Scope](#scope)
- [Recurring Archive Themes](#recurring-archive-themes)
- [Role and Content Boundaries](#role-and-content-boundaries)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Scope

Use this foundation hub for role expectations, modeling, feature work, product
analytics, experimentation, domain fit, hiring signals, and portfolios. It also
covers collaboration with engineering teams.

For model design and production architecture, use
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
For A/B testing and causal reasoning, use
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
For operating production models, use [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}).

## Recurring Archive Themes

**Data scientists connect prediction to product value.**

The first archive role episode separates analysts and data scientists by their
center of gravity. Analysts explain what is happening in the data. Data
scientists use data to build predictive services and incorporate them into
products.

This distinction is useful but not absolute. Hiring and job-description episodes
show that some companies use "data scientist" for analytics, BI, machine
learning engineering, or a mix of all three. Preserve that ambiguity rather than
force one universal definition.

**Business framing comes before model choice.**

Several interview episodes reward candidates who start with the business goal,
stakeholders, constraints, data availability, and evaluation metric. A candidate
who jumps straight to an algorithm misses a recurring archive lesson. Modeling
is useful only when it improves a decision, workflow, ranking, forecast, or
product behavior.

This is why portfolio and interview advice repeatedly asks for case-study
narratives. Strong data science evidence shows the problem, the data, the method,
the metric, the tradeoff, and the impact.

**Domain knowledge is a hiring and execution signal.**

Recruiter-side episodes emphasize industry and use-case alignment. A project
that uses the same kind of data, customer problem, or business process as the
target company can matter more than a generic list of tools.

The same theme appears in AI engineering episodes. Guests argue that domain
knowledge helps practitioners speak with experts, define useful evaluations, and
avoid solving the wrong problem with impressive tools.

**Engineering awareness matters even when data science isn't engineering.**

The archive doesn't require every data scientist to become a platform engineer.
It does, however, expect practical awareness of SQL, Python, data pipelines,
Docker, deployment constraints, and monitoring. Big-data role episodes warn that
model quality suffers when data scientists don't understand how upstream data
flows or deployment requirements shape their work.

This is also why newer AI episodes put pressure on the role. LLM tools can speed
up exploratory analysis and coding, but they don't remove the need to evaluate
outputs, understand data, reason about metrics, or communicate risk.

**Data science jobs are often mislabeled.**

The archive's hiring episodes repeatedly warn candidates to inspect job
descriptions for team structure, responsibilities, objectives, data maturity,
and tech-stack realism. A "data scientist" posting may really ask for a data
engineer, product analyst, ML engineer, or first data hire.

The practical advice is to ask what data exists, who owns pipelines, who deploys
models, who consumes the output, and how success will be measured.

## Role and Content Boundaries

**Data science versus data analysis.**

Data analysis explains what happened and supports decisions through dashboards,
reports, KPIs, SQL, statistics, and recommendations. Data science overlaps with
analysis but leans more toward prediction, modeling, experimentation, and
product integration.

Many companies combine these roles, especially in smaller teams. When the
archive discusses metrics, dashboards, and analysis-only workflows, future pages
may need a separate data analyst hub.

**Data science versus data engineering.**

Data engineers build and operate the data paths that data scientists depend on.
Data scientists build models, features, experiments, and analyses that depend on
those paths. The boundary blurs around data cleaning, feature engineering, batch
scoring, and model deployment.

Use [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) when the
main question is data availability, platform design, transformation, quality, or
pipeline operation.

**Data science versus machine learning.**

Machine learning is a technical method family. Data science is a role and
practice that may use machine learning, statistics, causal inference, SQL,
visualization, and domain analysis. In the archive, a data scientist may build ML
models, but not every data science task uses ML.

Use [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}) when the
page centers on modeling systems, model evaluation, interpretability, and ML
production tradeoffs.

**Data science versus AI engineering.**

AI engineering in the newest archive mostly means building applications around
LLMs, RAG, agents, context management, evaluations, and production software.
Data scientists can transition into AI engineering because they already know
experimentation, metrics, and data. They may need stronger software engineering
and system-building practice.

## Episode Evidence

These episodes give the strongest starting evidence for the topic.

- [Data Team Roles Explained](https://datatalks.club/podcast.html): At
  11:17-12:45, the episode distinguishes analysts from data scientists by
  explaining versus predicting. It also names ML, Python, SQL, Flask, and Docker
  as practical skills.
- [Big Data Engineer vs Data Scientist](https://datatalks.club/podcast.html):
  At 13:56-15:32, the guest describes data scientists as building models,
  cleaning data, preparing features, and understanding deployment even when
  another role owns it.
- [Land Data Scientist Roles](https://datatalks.club/podcast.html): At
  19:50-27:19, the episode discusses portfolios, use-case alignment, business
  impact, and industry fit as hiring signals.
- [Data Science Interview Guide](https://datatalks.club/podcast.html): At
  15:29-17:13, the episode contrasts product data scientist and ML engineer
  expectations. At 32:03-39:10, it emphasizes business goals, metrics, ML
  fundamentals, SQL, and coding.
- [Master ML and Data Science Interviews](https://datatalks.club/podcast.html):
  Covers recruiter screening, scenario questions, coding, fundamentals, and the
  balance between practical and theoretical ML interview preparation.
- [Data Science Job Red Flags](https://datatalks.club/podcast.html): At
  20:06-30:20, the guest gives a role-clarity checklist. It includes team,
  objectives, responsibilities, data infrastructure, analytics function, and
  warning signs in job descriptions.
- [Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}):
  Shows the experimentation side of data science through causality, metrics,
  randomization, power analysis, and A/A testing.
- [Interpretable Machine Learning](https://datatalks.club/podcast.html): Adds
  model trust, SHAP, conformal prediction, uncertainty, debugging, and
  documentation as data science and ML practice areas.

## Related Pages

Use these pages for adjacent topics and deeper implementation detail.

- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})

## Maintenance Notes

- Highest-value source files for future expansion:
  `../datatalksclub.github.io/_podcast/data-team-roles.md`,
  `../datatalksclub.github.io/_podcast/get-data-scientist-job.md`,
  `../datatalksclub.github.io/_podcast/data-science-interview-and-cv-guide.md`,
  `../datatalksclub.github.io/_podcast/data-science-job-red-flags-and-mismatched-roles.md`,
  and `../datatalksclub.github.io/_podcast/big-data-engineer-vs-data-scientist.md`.
- Good future additions: data science leadership episodes, nonprofit/public
  policy examples, healthcare ML examples, and concrete portfolio project
  evidence.
- Avoid turning this page into a generic "what is data science" article. Keep
  claims tied to role ambiguity, product value, hiring evidence, and
  collaboration in the podcast archive.
