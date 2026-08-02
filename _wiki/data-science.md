---
layout: wiki
title: "Data Science"
summary: "Data science through decision-first analysis, modeling, experimentation, trust, production handoff, and neighboring domains."
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
  - Bioinformatics Data Science
  - Product Analytics
  - AI for Social Good
---

Data science turns business questions into evidence someone can use. It also
covers product and operational questions. That evidence may be a
[[data-analysis=>SQL analysis]] or a forecast. It may also be a ranking model,
an A/B test, a recommender system, or a model-backed service.

CRISP-DM links data science to older data-mining practice. It treats the work as
business understanding and data preparation before modeling, evaluation, and
deployment rather than model training alone.
[[cite:crisp-dm@05:34=>CRISP-DM Methodology]]

The field sits between [[data-analysis=>analysis]], [[machine learning]],
[[experimentation-and-causal-inference=>experimentation]], and
[[data engineering]]. Product delivery adds the handoff from evidence to a
working decision. For the job title, team variants, and hiring boundaries, use
[[Data Scientist Role]]. For career paths, use [[Data Science Careers]] and
[[Job Search]].
When the transition starts from stakeholder planning and business KPIs, use
[[project-manager-to-data-science=>Project Manager to Data Science]].

## Decision-First Practice

Data science starts from a decision and ends with a usable answer. A CRISP-DM
project starts with business understanding and data preparation. It then moves
through modeling, evaluation, and deployment. The model objective ties back to
measurable business value instead of treating the algorithm as the goal.
Evaluation stays tied to the same business question.
[[cite:crisp-dm=>CRISP-DM Methodology]]

The methods can be descriptive, predictive, or causal. Analysts often quantify
what happened, while predictive systems and model-backed services extend the
work toward future decisions and product behavior.
[[cite:data-team-roles=>Data Team Roles Explained]] Domain-heavy practice in
[[bioinformatics-data-science=>Bioinformatics Data Science]] keeps the same
decision-and-evidence path, but the features stay tied to lab, sequencing, or
biomarker context. Public-policy, nonprofit, and conservation projects apply
the same framing in [[ai-for-social-good=>AI for social good]], where the usable
answer is a public-interest or resource-allocation decision.

When the work needs planning, risk management, and stakeholder alignment around
that modeling path, use [[data-science-project-management=>Data Science Project
Management]].

## Neighboring Domains and Ownership Boundaries

Data science and analytics differ by emphasis, not by a hard wall. Reporting and
diagnostics can sit beside product analysis, prediction, and experimentation on
the same team. Hiring screens may also use similar signals for analysts and data
scientists.
[[cite:hiring-data-scientists-and-analysts=>Hiring Data Scientists and Analysts]]
The role-level boundary belongs in [[Data Scientist Role]]. The field-level
boundary is whether the work stops at measurement or changes a decision,
experiment, model, or product surface.

Data science depends on data engineering but doesn't own the whole platform.
Data preparation, feature work, and modeling sit near the science side.
Deployment awareness connects them to ETL, storage, and Spark performance. It
also connects them to schema work and platform reliability.
[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]

The broader
[[data-engineering-and-data-science=>data engineering and data science]]
comparison follows that shared project lifecycle through handoffs and project
choices. The dedicated [[Data Engineer vs Data Scientist]] page goes deeper
when the question is a job-title split.

Machine learning gives data science one of its main toolsets, but not every data
science problem needs a model. When packaging and serving become the center of
the work, the topic moves toward CI/CD, runtime reliability,
[[machine-learning-engineer-role=>machine learning engineering]] and
[[Machine Learning System Design]].

## Product Decisions and Experiments

Data science work often starts with a product decision before modeling begins.
Problem framing and feature engineering are transferable data science habits.
The work also pushes toward user impact, experiments, deployment, and practical
shipping habits. Shipping starts simple, tests quickly, and learns from
production use.
[[cite:data-science-leadership-hiring-mlops=>Data Science Leadership]]

Experimentation gives product analysis a causal test. A/B testing follows
randomized clinical-trial logic, and a subscription-versus-points example shows
why metric design changes how a team interprets a product test. A/A tests,
seasonality, and power analysis round out the method.
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
Those details put experimentation next to data science while giving it its own
[[Experimentation and Causal Inference]]
page.

## Engineering Awareness and Model Handoff

Data science projects don't end at a notebook. Predictive work often needs a
simple service, a batch scoring path, or a handoff to engineers.
[[cite:data-team-roles=>Data Team Roles Explained]] Reproducibility and code
quality affect whether another person can look at, rerun, or productionize the
work.
[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]

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
For career switchers who already own delivery and stakeholder communication,
[[project-manager-to-data-science=>Project Manager to Data Science]] narrows
the gap to analysis, statistics, and modeling evidence.
That transition keeps data science tied to decisions before it becomes a tool
checklist.

## Trust and Responsible Use

Data science doesn't end when an offline metric improves because deployment
also needs trust and debugging methods. SHAP and
interpretability-versus-accuracy tradeoffs help explain model behavior.
Conformal prediction, calibrated uncertainty, and experiment notes make model
work traceable.
[[cite:interpretable-machine-learning=>Interpretable Machine Learning]]

Interpretability links data science to
[[Responsible AI and Governance]]
and [[Interpretability]]. Users
need to know where a prediction is reliable, where it fails, and what evidence
supports deployment. Newer AI work adds another boundary. Data science brings
metrics, data splits, experiments, and evaluation habits into
[[AI]] and
[[LLM Production Patterns]].
LLM applications demand stronger software design around retrieval, agents, and
context management.
