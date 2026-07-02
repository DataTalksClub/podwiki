---
layout: wiki
title: "Data Science"
summary: "How DataTalks.Club podcast discussions frame data science: product-facing modeling, analysis, experimentation, hiring signals, role ambiguity, and the boundary with ML, data engineering, and AI engineering."
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

Data science turns business questions into evidence someone can use. It also
covers product and operational questions. In DataTalks.Club discussions, that
evidence may be a SQL analysis or a forecast. It may also be a ranking model,
an A/B test, a recommender system, or a model-backed service.

In [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
analysts explain what happened. Data scientists predict what will happen and
help put those predictions into products. Later episodes show why the title
still moves by company. A data scientist may sit close to product analytics or
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}). They may
also work near
[experimentation]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}),
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}), or
first-data-hire responsibilities.

For role-level detail, see
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }}). For
career paths, see
[Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }}) and
[Job Search]({{ '/wiki/job-search/' | relative_url }}).

## Decision Framing and Evaluation

Data science starts from a decision and ends with a usable answer.
In [CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }}), a data
science project starts with business understanding and data preparation. It
then moves through modeling, evaluation, and deployment. At 13:25 and 17:05,
the discussion ties the model objective back to measurable business value
instead of treating the algorithm as the goal. The 18:23 checkpoint keeps
evaluation tied to the same business question.

In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
the analyst-versus-data scientist distinction is practical rather than
academic. At 11:17, analysts quantify what happened, while data scientists
build predictive services. Later, the episode connects data science work to
Python, SQL, and machine learning. It also names Flask, Docker, and simple
model services.

In
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }}) separates product
data scientist and machine-learning-engineer expectations around 15:29. At
32:03, case studies start with business goals and evaluation metrics before
they test modeling, SQL, or coding.

## Boundaries and Role Fit

Data science versus analytics is a difference in emphasis, not a hard wall.
[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }}) shows why the
job description matters in
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }}).
Recruiters may screen analysts and data scientists with similar signals.
Candidates still need to check whether the work is reporting, product analysis,
modeling, or experimentation. Some jobs also expect production ML.

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

[Data Science Job Red Flags]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }})
with [Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }}) gives the
clearest warning about mismatched titles. At 20:06 and 23:01, she recommends
checking the team structure and objectives.
Candidates should also check responsibilities and infrastructure. At 27:18, she
points candidates to data engineering and analytics support. Those neighboring
roles help candidates tell whether the opening is data science or a catch-all
data role.

## Product Decisions and Experiments

Data science work often starts with a product decision before modeling begins.
In
[Data Science Leadership]({{ '/podcasts/data-science-leadership-hiring-mlops/' | relative_url }}),
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) treats
problem framing and feature engineering as transferable data science habits at
23:09. At 29:29 and 30:06, he pushes the work toward user impact and
experiments. He also connects data science to deployment and the practical
rules of shipping ML. At 33:36, he recommends starting simple, testing quickly,
and learning from production use.

Experimentation gives product analysis a causal test. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) explains A/B testing
through randomized clinical-trial logic at 8:13. The
subscription-versus-points example at 14:27 shows why metric design changes how
a team interprets a product test. He covers A/A tests at 27:52, seasonality at
33:23, and power analysis at 37:44. Those details put experimentation next to
data science while giving it its own
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
page.

## Careers and Portfolio Evidence

Career episodes treat data science as a portfolio-backed craft, not a list of
tools. In [Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}),
[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }}) follows recruiting
from role definition through shortlist and interview preparation. He also
covers feedback and offer negotiation. At 19:50 and 25:04, stronger candidates
connect projects to industry context, real use cases, and business impact.

The same signal appears in [Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }})'s
CV and case-study advice. At 18:28, he treats the CV as a screening surface. At
29:32 and 32:03, project stories need to explain the problem and data. Case
studies also need to name the method, metric, and tradeoff. Modeling portfolios
belong with
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
while public contributions belong with
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).

[Ksenia Legostay]({{ '/people/ksenialegostay/' | relative_url }}) adds the
transition view in
[From Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}).
At 22:32, project management experience transfers through planning and
stakeholder communication. Business KPIs transfer in the same way. At 32:43,
she recommends applying analysis at work and building portfolio evidence.

At 41:07, production readiness adds Git and testing to the learning path. It
also adds Docker, deployment, and clean code. Career pages connect data science
to
[career transitions in data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
instead of treating every entrant as a new graduate.

## Engineering Awareness and Model Handoff

Across these episodes, data scientists don't need to become platform
engineers, but they need enough engineering awareness to collaborate. In
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
data scientists build the model and sometimes expose it through a simple
service. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) ties
software engineering practice to reproducibility and code quality at 46:14.

Model quality depends on upstream data and downstream use. Recommendation
systems and batch scoring jobs need data contracts and feature availability.
Model APIs need monitoring and clear owners.

When the question shifts from doing data science to running models, the topic
changes. These pages route model operations toward
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and data-flow reliability toward
[DataOps]({{ '/wiki/dataops/' | relative_url }}).
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }})
handles that boundary, and
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
goes deeper on architecture choices.

## Trust and Responsible Use

Data science doesn't end when an offline metric improves.
[Interpretable Machine Learning]({{ '/podcasts/interpretable-machine-learning/' | relative_url }})
adds trust and debugging methods to the data science toolkit.
[Christoph Molnar]({{ '/people/christophmolnar/' | relative_url }}) covers the
interpretability-versus-accuracy tradeoff and SHAP around 9:27. At 20:27, he
covers conformal prediction and calibrated uncertainty. At 36:21, experiment
notes make model work traceable.

Interpretability links data science to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
and [Interpretability]({{ '/wiki/interpretability/' | relative_url }}). Users
need to know where a prediction is reliable, where it fails, and what evidence
supports deployment. Newer AI work adds another boundary. Data scientists bring
metrics and data splits into
[AI]({{ '/wiki/ai/' | relative_url }}) and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
They also bring experiments and evaluation habits, but LLM applications demand
stronger software design around retrieval, agents, and context management.
