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

Data science turns business and product questions into analysis, models,
experiments, and decisions. It also covers research and operations questions. In
the DataTalks.Club archive,
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
sets the starting boundary. Analysts explain what happened, while data
scientists predict and help put the predictions into a product.

The archive doesn't treat that boundary as fixed. Recruiters and practitioners
repeatedly warn that "data scientist" may mean product analytics or machine
learning. It may also mean experimentation, data engineering, or first-data-hire
work. Use [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
for the role page. Use [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
for modeling methods, [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
for data paths, and use
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
for A/B testing and causal decisions.

## Link Map

Use these wiki paths for adjacent questions:

- [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
- [Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }})
- [Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }})
- [Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})

Start with these podcast discussions:

- [Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
- [CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }})
- [Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})
- [Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }})
- [Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }})
- [Data Science Job Red Flags]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }})
- [Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
- [Interpretable Machine Learning]({{ '/podcasts/interpretable-machine-learning/' | relative_url }})

These contributor pages connect the topic to named guests and hosts:

- [DataTalks.Club host profile]({{ '/people/alexeygrigorev/' | relative_url }})
- [Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }})
- [Luke Whipps]({{ '/people/lukewhipps/' | relative_url }})
- [Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }})
- [Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }})
- [Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }})
- [Jakob Graff]({{ '/people/jakobgraff/' | relative_url }})
- [Christoph Molnar]({{ '/people/christophmolnar/' | relative_url }})

## Common Definition

The archive converges on a practical definition: data science starts from a
question and ends with evidence someone can use. That evidence may be a notebook
or dashboard. It may also be a forecast or classifier. Other outputs include
recommenders, A/B tests, written analyses, and model-backed services.

[CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }}) organizes
projects around business understanding and measurable objectives. It then moves
through data preparation, modeling, evaluation, and deployment. The checkpoints
at 13:25, 17:05, and 18:23 keep the business objective tied to model
evaluation.

Data science also combines methods that other pages cover separately. A
practitioner may use SQL and statistics to look at data. They may use machine
learning to predict, experiments to test interventions, and storytelling to
explain a decision. In
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
the case-study section starts from business goals and evaluation metrics at
32:03. It then tests ML fundamentals, SQL, and coding.

## Disagreements and Boundaries

Data science versus data analysis is a difference in emphasis, not a wall.
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
uses a clean teaching distinction at 11:17: analysts explain what happened,
while data scientists predict and integrate predictions into products. Alicja
Notowska's recruiting discussion in
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }})
complicates that distinction. At 54:09, data analyst hiring and data scientist
hiring share many screening patterns, so candidates still need to read the
actual responsibilities.

Data science versus data engineering depends on ownership. Data engineers own
the data path, while data scientists own the decision and the model or analysis
behind it. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
the 13:56 section ties data science to cleaning data and preparing features. It
also covers building models and understanding deployment.

The same episode puts ETL, storage, and Spark performance on the engineering
side. It also puts monitoring and schema work there. Features, batch scoring,
and deployment create overlap, so the boundary page
[Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
goes deeper.

Data science versus machine learning is also narrower than the job title makes
it sound. [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}) is a
method family for classification and ranking. It also covers forecasting,
recommendation, and optimization.

Data science may use ML, but it also includes product framing and statistics.
It also includes experiments, data analysis, and communication. The interview
split in
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }})
at 15:29 shows the difference between product data scientist and
machine-learning-engineer expectations.

Newer AI episodes create another boundary. Data scientists bring metrics,
experiments, data splits, and evaluation habits into AI engineering. AI
engineering also demands stronger software practice around LLM applications and
production systems. RAG, agents, and context management add more design work.
The broader [AI]({{ '/wiki/ai/' | relative_url }})
page tracks that shift and routes LLM-specific work to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

## Project Framing and Lifecycle

Data science work should begin with the decision that the analysis or model will
support. In [CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }}),
the project example asks whether users fail to post listings and whether the
problem is measurable. It also asks whether a baseline is good enough before
moving deeper into modeling. This makes data science a product and decision
practice, not only an algorithm choice.

Hiring advice uses the same project framing. In
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }})
at 19:50 and 25:04, candidates are asked to show concrete projects and industry
fit. They should also show use-case alignment and business impact.

A portfolio that names only
Python, scikit-learn, or cloud tools is weaker than a case study. Stronger case
studies explain the problem and data. They also name the method, metric,
tradeoff, and result.

## Product Analytics and Experimentation

The archive treats experimentation as one of the core ways data science turns
analysis into product decisions. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
the 8:13 section explains A/B testing through randomized clinical-trial logic.
At 14:27, the subscription-versus-points example shows why revenue metric
design changes the interpretation of a product test.

Good experimentation work also needs operational discipline. The episode covers
A/A tests at 27:52 to validate randomization and tracking. It covers metric
noise and seasonality at 33:23, then power analysis at 37:44. That's why this
page routes causal questions to
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
instead of treating every product question as a modeling task.

## Hiring Signals and Role Fit

Hiring episodes rank role fit above generic credentials. In
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }})
the recruiting workflow moves from role definition to shortlist, interview
preparation, feedback, and offer negotiation. The advice at 16:15 and 19:50
rewards candidates who connect their experience to the target industry's data
and problems.

Candidates get the matching preparation advice in
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}).
At 18:28, the CV is treated as a screening surface. At 29:32 and 32:03,
candidates prepare project stories and case studies that start with business
goals and end with evaluation metrics.

The
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }})
episode adds recruiter-side evidence. At 21:32, recruiters screen experience,
education, and responsibilities. At 32:40, buzzword-heavy CVs become a warning
sign.

Tereza Iofciu's
[Data Science Job Red Flags]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }})
is the archive's strongest warning that a "data scientist" title may hide the
wrong job. At 20:06 and 23:01, she recommends checking team structure,
objectives, and responsibilities. She also recommends checking data
infrastructure and whether the company has data engineering or analytics
support.

## Engineering Awareness and Production Handoff

The archive doesn't require every data scientist to become a platform engineer,
but it repeatedly values engineering awareness.
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
names practical skills around ML, Python, and SQL after the
analyst-versus-data-scientist distinction. It also names Flask, Docker, and
simple services.
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})
extends that boundary at 24:49 by asking what data scientists should understand
about pipelines. At 46:14, software engineering practice is tied to
reproducibility and code quality.

This engineering awareness matters because model quality depends on upstream
data as much as downstream use. Recommendation systems and batch scoring jobs
need data contracts, feature availability, and deployment paths. Model APIs need
monitoring plus clear owners. Use [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
when the question shifts from data science work to operating models and data
flows.

## Trust, Interpretability, and Responsible Use

Data science doesn't end when a metric improves.
[Interpretable Machine Learning]({{ '/podcasts/interpretable-machine-learning/' | relative_url }})
episode adds trust and debugging methods to the data science toolkit. At 9:27,
the discussion covers interpretability versus accuracy and SHAP for
understanding model behavior. At 20:27, it covers conformal prediction and
calibrated uncertainty. At 36:21, experiment notes make model work traceable.

Those practices connect data science to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).
Model users need to know where a prediction is reliable, where it fails, and
what evidence supports deployment. These practices also connect to
[Interpretability]({{ '/wiki/interpretability/' | relative_url }}) when the
main question is model explanation rather than the broader data science role.

## Related Pages

Use these pages for deeper role, method, and production detail.

- [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
- [Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }})
- [Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
