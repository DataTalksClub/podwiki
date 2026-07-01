---
layout: wiki
title: "Data Science"
summary: "How the DataTalks.Club podcast archive frames data science: product-facing modeling, analysis, experimentation, hiring signals, role ambiguity, and the boundary with ML, data engineering, and AI engineering."
related:
  - Data Scientist Role
  - Data Science Careers
  - Machine Learning
  - Data Engineering
  - Data Engineer vs Data Scientist
  - Experimentation and Causal Inference
  - Machine Learning System Design
  - Responsible AI and Governance
  - AI
---

Data science turns business and product questions into evidence someone can
use. It also covers operations questions. In the DataTalks.Club archive, that
evidence may be a SQL analysis or a forecast. It may be a ranking model, an A/B
test, or a recommender system. It may also be a model-backed service.

[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
sets the teaching boundary. Analysts explain what happened, and data scientists
predict what will happen. They also help put those predictions into a product.

The archive also warns that the boundary moves by company. In some companies, a
data scientist job means product analytics or
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}). In others,
it means
[experimentation]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
It may also mean
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) or
first-data-hire work.

Use [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
for the role-level definition and
[Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }}) for
career paths. When evaluating a specific opening, use
[Job Search]({{ '/wiki/job-search/' | relative_url }}).

## Common Definition

Across the podcast archive, practitioners start data science work from a
decision and end with a usable answer.
[CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }}) frames that
work around business understanding and data preparation. It then moves through
modeling, evaluation, and deployment. At 13:25 and 17:05, the discussion ties
the model objective
back to measurable business value instead of treating the algorithm as the goal.
The 18:23 checkpoint keeps evaluation tied to the same business question.

In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst-versus-data scientist distinction is practical rather than
academic. At 11:17, analysts quantify what happened, while data scientists
build predictive services. Later, the episode connects data science work to
Python and SQL. It also names machine learning, Flask, Docker, and simple model
services.

Interview discussions reinforce that broad definition. In
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }}) separates product
data scientist and machine-learning-engineer expectations around 15:29. At
32:03, case studies start with business goals and evaluation metrics before
they test modeling, SQL, or coding.

## Boundaries and Role Fit

Data science versus analytics is a difference in emphasis, not a hard wall.
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }})
shows why the job description matters. Recruiters may screen analysts and data
scientists with similar signals. Candidates still need to check whether the
work is reporting, product analysis, modeling, or experimentation. Some jobs
also expect production ML.

Data science versus data engineering depends on ownership.
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) draws the
boundary in [Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}).
Around 13:56, data scientists clean data and prepare features. They also build
models and think about deployment. Around 24:49, they still need enough
pipeline knowledge to collaborate with engineers.

ETL, storage, and Spark performance sit closer to data engineering. Schema work
and platform reliability do too. The dedicated
[Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
page goes deeper into that overlap.

[Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }}) gives the
archive's strongest warning about mismatched titles.
She recommends checking the team structure and objectives in
[Data Science Job Red Flags]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }})
at 20:06 and 23:01.
Candidates should also check responsibilities and infrastructure. At 27:18 she
points candidates to data engineering and analytics support. That support helps
candidates tell whether the job is data science or a catch-all data role.

## Project Framing and Product Decisions

The archive treats data science as a product and decision practice before
modeling. In
[Data Science Leadership]({{ '/podcasts/data-science-leadership-hiring-mlops/' | relative_url }}),
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) describes
transferable data science habits around problem framing and feature engineering
at 23:09. At 29:29 and 30:06, he pushes the work toward user impact and
experiments. He also connects data science to deployment and the practical
rules of shipping ML. At 33:36, he recommends starting simple, testing quickly,
and learning from production use.

The archive often connects analysis with decisions through experimentation. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
the 8:13 section explains A/B testing through randomized clinical-trial logic.
The subscription-versus-points example at 14:27 shows why metric design changes
how a team interprets a product test. The episode covers A/A tests at 27:52 and
seasonality at 33:23. Power analysis at 37:44 explains why experimentation
belongs next to data science but needs its own
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
page.

## Careers, Transitions, and Portfolio Evidence

Career episodes treat data science as a portfolio-backed craft, not a list of
tools. In [Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}),
[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }}) describes recruiting
from role definition through shortlist and interview preparation. He also
covers feedback and offer negotiation. At 19:50 and 25:04, stronger candidates
connect projects to
industry context, real use cases, and business impact.

[Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }}) gives the same
signal in CV and case-study form. At 18:28, he treats the CV as a screening
surface. At 29:32 and 32:03, project stories need to explain the problem and
data. Case studies also need to name the method, metric, and tradeoff. That's
why data science portfolios often link to
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
when the work centers on modeling.

When public contributions are the strongest proof, portfolios link to
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
instead.

[Ksenia Legostay]({{ '/people/ksenialegostay/' | relative_url }}) adds the
transition view in
[From Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}).
At 22:32, project management experience transfers through planning and
stakeholder communication. Business KPIs transfer in the same way. At 32:43,
she recommends applying analysis at work and building portfolio evidence.

At 41:07, production readiness adds Git and testing to the learning path. It
also adds Docker, deployment, and clean code. This is why career pages connect
data science to
[career transitions in data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
instead of treating every entrant as a new graduate.

## Engineering Awareness and Production Handoff

The podcast archive doesn't require every data scientist to become a platform
engineer, but it repeatedly values engineering awareness. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
data scientists build the model and may expose it through a simple service. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
the 46:14 section ties software engineering practice to reproducibility and
code quality.

Model quality depends on upstream data and downstream use. Recommendation
systems and batch scoring jobs need data contracts and feature availability.
Model APIs need monitoring and clear owners.

When the question shifts from doing data science to running models, the topic
changes. The archive routes model operations toward
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and data-flow reliability toward
[DataOps]({{ '/wiki/dataops/' | relative_url }}). Use
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
when the boundary matters, and use
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
for architecture choices.

## Trust, Interpretability, and Responsible Use

Data science doesn't end when an offline metric improves.
[Interpretable Machine Learning]({{ '/podcasts/interpretable-machine-learning/' | relative_url }})
adds trust and debugging methods to the data science toolkit. Around 9:27, the
discussion covers the interpretability-versus-accuracy tradeoff and SHAP. At
20:27, it covers conformal prediction and calibrated uncertainty. At 36:21,
experiment notes make model work traceable.

Those practices connect data science to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
and [Interpretability]({{ '/wiki/interpretability/' | relative_url }}). Users
need to know where a prediction is reliable, where it fails, and what evidence
supports deployment. Newer AI work adds another boundary. Data scientists bring
metrics and data splits into
[AI]({{ '/wiki/ai/' | relative_url }}) and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
They also bring experiments and evaluation habits, but LLM applications demand
stronger software design around retrieval, agents, and context management.
