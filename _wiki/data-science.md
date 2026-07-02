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
covers product and operational questions. That evidence may be a SQL analysis or
a forecast. It may also be a ranking model, an A/B test, a recommender system,
or a model-backed service.

Analysts explain what happened, while data scientists predict what will happen
and help put those predictions into products
([[podcast:data-team-roles|Data Team Roles Explained]]).
The title still moves by company. A data scientist may sit close to product
analytics or
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

Data science starts from a decision and ends with a usable answer. A CRISP-DM
project starts with business understanding and data preparation, then moves
through modeling, evaluation, and deployment. The model objective ties back to
measurable business value instead of treating the algorithm as the goal, and
evaluation stays tied to the same business question
([[podcast:crisp-dm|CRISP-DM Methodology]]).

The analyst-versus-data scientist distinction is practical rather than academic:
analysts quantify what happened, while data scientists build predictive
services. Data science work connects to Python, SQL, and machine learning, along
with Flask, Docker, and simple model services
([[podcast:data-team-roles|Data Team Roles Explained]]).

Product data scientist and machine-learning-engineer expectations differ, and
case studies start with business goals and evaluation metrics before they test
modeling, SQL, or coding
([[podcast:data-science-interview-and-cv-guide|Data Science Interview Guide]]).

## Boundaries and Role Fit

Data science versus analytics is a difference in emphasis, not a hard wall. The
job description matters because recruiters may screen analysts and data
scientists with similar signals
([[podcast:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]]).
Candidates still need to check whether the work is reporting, product analysis,
modeling, or experimentation. Some jobs also expect production ML.

Data science versus data engineering depends on ownership. Data scientists clean
data, prepare features, build models, and think about deployment, while still
needing enough pipeline knowledge to collaborate with engineers
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).

ETL, storage, and Spark performance sit closer to data engineering. Schema work
and platform reliability do too. The dedicated
[[Data Engineer vs Data Scientist]]
page goes deeper into that overlap.

Mismatched titles are a common risk, so candidates should check team structure,
objectives, responsibilities, and infrastructure, along with the data
engineering and analytics support around the role
([[podcast:data-science-job-red-flags-and-mismatched-roles|Data Science Job Red Flags]]).
Those neighboring roles help candidates tell whether the opening is data science
or a catch-all data role.

## Product Decisions and Experiments

Data science work often starts with a product decision before modeling begins.
Problem framing and feature engineering are transferable data science habits,
and the work pushes toward user impact and experiments, deployment, and the
practical rules of shipping ML: start simple, test quickly, and learn from
production use
([[podcast:data-science-leadership-hiring-mlops|Data Science Leadership]]).

Experimentation gives product analysis a causal test. A/B testing follows
randomized clinical-trial logic, and a subscription-versus-points example shows
why metric design changes how a team interprets a product test. A/A tests,
seasonality, and power analysis round out the method
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]).
Those details put experimentation next to data science while giving it its own
[[Experimentation and Causal Inference]]
page.

## Careers and Portfolio Evidence

Data science is a portfolio-backed craft, not a list of tools. Recruiting runs
from role definition through shortlist, interview preparation, feedback, and
offer negotiation, and stronger candidates connect projects to industry context,
real use cases, and business impact
([[podcast:get-data-scientist-job|Land Data Scientist Roles]]).

The same signal appears in CV and case-study advice: the CV is a screening
surface, project stories need to explain the problem and data, and case studies
need to name the method, metric, and tradeoff
([[podcast:data-science-interview-and-cv-guide|Data Science Interview Guide]]).
Modeling portfolios belong with
[[Machine Learning Portfolio Projects]],
while public contributions belong with
[[Open Source Portfolio Evidence]].

Transitions add another view: project management experience transfers through
planning, stakeholder communication, and business KPIs, and applying analysis at
work builds portfolio evidence
([[podcast:project-manager-to-data-scientist|From Project Manager to Data Scientist]]).

Production readiness adds Git, testing, Docker, deployment, and clean code to the
learning path
([[podcast:project-manager-to-data-scientist|From Project Manager to Data Scientist]]).
Career pages connect data science to
[[career transitions in data]]
instead of treating every entrant as a new graduate.

## Engineering Awareness and Model Handoff

Data scientists don't need to become platform engineers, but they need enough
engineering awareness to collaborate. They build the model and sometimes expose
it through a simple service
([[podcast:data-team-roles|Data Team Roles Explained]]), and software
engineering practice ties to reproducibility and code quality
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).

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

Data science doesn't end when an offline metric improves. Interpretability adds
trust and debugging methods to the data science toolkit: the
interpretability-versus-accuracy tradeoff and SHAP, conformal prediction and
calibrated uncertainty, and experiment notes that make model work traceable
([[podcast:interpretable-machine-learning|Interpretable Machine Learning]]).

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
