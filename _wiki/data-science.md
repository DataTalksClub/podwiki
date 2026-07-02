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

In [[podcast:data-team-roles|Data Team Roles Explained]],
analysts explain what happened. Data scientists predict what will happen and
help put those predictions into products. Later episodes show why the title
still moves by company. A data scientist may sit close to product analytics or
[[machine learning]]. They may
also work near
[[experimentation-and-causal-inference|experimentation]],
[[data engineering]], or
first-data-hire responsibilities.

For role-level detail, see
[[Data Scientist Role]]. For
career paths, see
[[Data Science Careers]] and
[[Job Search]].

## Decision Framing and Evaluation

Data science starts from a decision and ends with a usable answer.
In [[podcast:crisp-dm|CRISP-DM Methodology]], a data
science project starts with business understanding and data preparation. It
then moves through modeling, evaluation, and deployment. At 13:25 and 17:05,
the discussion ties the model objective back to measurable business value
instead of treating the algorithm as the goal. The 18:23 checkpoint keeps
evaluation tied to the same business question.

In
[[podcast:data-team-roles|Data Team Roles Explained]],
the analyst-versus-data scientist distinction is practical rather than
academic. At 11:17, analysts quantify what happened, while data scientists
build predictive services. Later, the episode connects data science work to
Python, SQL, and machine learning. It also names Flask, Docker, and simple
model services.

In
[[podcast:data-science-interview-and-cv-guide|Data Science Interview Guide]],
[[person:olegnovikov|Oleg Novikov]] separates product
data scientist and machine-learning-engineer expectations around 15:29. At
32:03, case studies start with business goals and evaluation metrics before
they test modeling, SQL, or coding.

## Boundaries and Role Fit

Data science versus analytics is a difference in emphasis, not a hard wall.
[[person:alicjanotowska|Alicja Notowska]] shows why the
job description matters in
[[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
Recruiters may screen analysts and data scientists with similar signals.
Candidates still need to check whether the work is reporting, product analysis,
modeling, or experimentation. Some jobs also expect production ML.

Data science versus data engineering depends on ownership.
[[person:roksolanadiachuk|Roksolana Diachuk]] draws the
boundary in [[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]].
Around 13:56, data scientists clean data and prepare features. They also build
models and think about deployment. Around 24:49, they still need enough
pipeline knowledge to collaborate with engineers.

ETL, storage, and Spark performance sit closer to data engineering. Schema work
and platform reliability do too. The dedicated
[[Data Engineer vs Data Scientist]]
page goes deeper into that overlap.

[[podcast:data-science-job-red-flags-and-mismatched-roles|Data Science Job Red Flags]]
with [[person:terezaiofciu|Tereza Iofciu]] gives the
clearest warning about mismatched titles. At 20:06 and 23:01, she recommends
checking the team structure and objectives.
Candidates should also check responsibilities and infrastructure. At 27:18, she
points candidates to data engineering and analytics support. Those neighboring
roles help candidates tell whether the opening is data science or a catch-all
data role.

## Product Decisions and Experiments

Data science work often starts with a product decision before modeling begins.
In
[[podcast:data-science-leadership-hiring-mlops|Data Science Leadership]],
[[person:marianosemelman|Mariano Semelman]] treats
problem framing and feature engineering as transferable data science habits at
23:09. At 29:29 and 30:06, he pushes the work toward user impact and
experiments. He also connects data science to deployment and the practical
rules of shipping ML. At 33:36, he recommends starting simple, testing quickly,
and learning from production use.

Experimentation gives product analysis a causal test. In
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]],
[[person:jakobgraff|Jakob Graff]] explains A/B testing
through randomized clinical-trial logic at 8:13. The
subscription-versus-points example at 14:27 shows why metric design changes how
a team interprets a product test. He covers A/A tests at 27:52, seasonality at
33:23, and power analysis at 37:44. Those details put experimentation next to
data science while giving it its own
[[Experimentation and Causal Inference]]
page.

## Careers and Portfolio Evidence

Career episodes treat data science as a portfolio-backed craft, not a list of
tools. In [[podcast:get-data-scientist-job|Land Data Scientist Roles]],
[[person:lukewhipps|Luke Whipps]] follows recruiting
from role definition through shortlist and interview preparation. He also
covers feedback and offer negotiation. At 19:50 and 25:04, stronger candidates
connect projects to industry context, real use cases, and business impact.

The same signal appears in [[person:olegnovikov|Oleg Novikov]]'s
CV and case-study advice. At 18:28, he treats the CV as a screening surface. At
29:32 and 32:03, project stories need to explain the problem and data. Case
studies also need to name the method, metric, and tradeoff. Modeling portfolios
belong with
[[Machine Learning Portfolio Projects]],
while public contributions belong with
[[Open Source Portfolio Evidence]].

[[person:ksenialegostay|Ksenia Legostay]] adds the
transition view in
[[podcast:project-manager-to-data-scientist|From Project Manager to Data Scientist]].
At 22:32, project management experience transfers through planning and
stakeholder communication. Business KPIs transfer in the same way. At 32:43,
she recommends applying analysis at work and building portfolio evidence.

At 41:07, production readiness adds Git and testing to the learning path. It
also adds Docker, deployment, and clean code. Career pages connect data science
to
[[career transitions in data]]
instead of treating every entrant as a new graduate.

## Engineering Awareness and Model Handoff

Across these episodes, data scientists don't need to become platform
engineers, but they need enough engineering awareness to collaborate. In
[[podcast:data-team-roles|Data Team Roles Explained]],
data scientists build the model and sometimes expose it through a simple
service. In
[[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]],
[[person:roksolanadiachuk|Roksolana Diachuk]] ties
software engineering practice to reproducibility and code quality at 46:14.

Model quality depends on upstream data and downstream use. Recommendation
systems and batch scoring jobs need data contracts and feature availability.
Model APIs need monitoring and clear owners.

When the question shifts from doing data science to running models, the topic
changes. These pages route model operations toward
[[MLOps]] and data-flow reliability toward
[[DataOps]].
[[MLOps vs DataOps]]
handles that boundary, and
[[Machine Learning System Design]]
goes deeper on architecture choices.

## Trust and Responsible Use

Data science doesn't end when an offline metric improves.
[[podcast:interpretable-machine-learning|Interpretable Machine Learning]]
adds trust and debugging methods to the data science toolkit.
[[person:christophmolnar|Christoph Molnar]] covers the
interpretability-versus-accuracy tradeoff and SHAP around 9:27. At 20:27, he
covers conformal prediction and calibrated uncertainty. At 36:21, experiment
notes make model work traceable.

Interpretability links data science to
[[Responsible AI and Governance]]
and [[Interpretability]]. Users
need to know where a prediction is reliable, where it fails, and what evidence
supports deployment. Newer AI work adds another boundary. Data scientists bring
metrics and data splits into
[[AI]] and
[[LLM Production Patterns]].
They also bring experiments and evaluation habits, but LLM applications demand
stronger software design around retrieval, agents, and context management.
