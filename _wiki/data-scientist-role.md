---
layout: wiki
title: "Data Scientist Role"
summary: "DataTalks.Club podcast view of the data scientist role: product questions, modeling, experimentation, ambiguity, role boundaries, and supporting episodes."
related:
  - Data Science
  - Machine Learning
  - Product Analytics
  - Data Products
  - Data Engineer vs Data Scientist
  - Data Scientist Interview Roadmap
  - Career Transitions in Data
  - Communication
---

A data scientist turns a business, product, or operational question into
evidence that can change a decision. Across DataTalks.Club discussions, that
evidence may be an analysis or a forecast. It may also be an experiment, a
recommendation system, a model, or a product feature. The role sits between
[data science]({{ '/wiki/data-science/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), and
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}).

[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
gives a useful baseline.
In the 11:17 section, the episode separates analysts from data scientists:
analysts explain what happened, while data scientists predict and help integrate
predictions into products. In that framing, data scientists do more than train
models. They must connect the question and data. They must also connect the
method, evaluation, and product use.

## From Questions To Evidence

Guests usually define the data scientist by the path from problem framing to
evidence. Data scientists often begin with SQL, data exploration, and feature
discovery. They then move into statistics,
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), or
experimentation when those methods are needed.

[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }})
describes the modeling side in
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}).
At 13:56, she ties data science to data cleaning and feature engineering. She
also covers model cycles and deployment awareness. Her framing keeps data
science connected to upstream pipelines and downstream use. Data scientists
therefore work near
[Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}).

Product-facing episodes define the role through decisions rather than only
models. In
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Oleg Novikov]({{ '/people/olegnovikov/' | relative_url }})
starts case-study preparation from business goals and evaluation metrics at
32:03. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }})
shows how randomized experiments turn product questions into causal evidence.
He uses metric design, A/A tests, and power analysis to make that evidence
usable.

## Team-Dependent Role Versions

Guests put different weight on engineering, product ownership, and statistical
depth. They don't treat "data scientist" as a stable job title.

[Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }})
makes role ambiguity the central warning in
[Data Science Job Red Flags]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }}).
At 20:06 and 23:01, she recommends checking the team and objectives. She also
checks responsibilities, data infrastructure, and the presence of analytics or
data engineering support. Her point is that a data scientist title can hide
analytics work, platform work, a first-data-hire job, or an undefined mix.

[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }})
looks at the same problem from recruiting in
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}).
At 16:15, 19:50, and 25:04, he emphasizes industry fit and concrete projects.
He also emphasizes business impact. Fraud and marketing roles reward different
evidence from forecasting, search, or recommendations roles.

[Marijn Markus]({{ '/people/marijnmarkus/' | relative_url }})
argues for another kind of differentiation in
[Data Science Career Playbook]({{ '/podcasts/how-to-stand-out-in-data-science/' | relative_url }}).
At 8:31, he names statistics, programming, and domain knowledge as core pillars.
At 37:49 and 43:08, he pushes candidates toward distinctive portfolio projects
and cross-disciplinary domain expertise instead of interchangeable Kaggle-style
work.

Guests also separate solo, lead, and transition versions of the role.
[Marianna Diachuk]({{ '/people/mariannadiachuk/' | relative_url }})
frames the solo data scientist as a mid-senior owner who has to discover
business problems and check data readiness. She also has to prioritize by
feasibility and impact, then educate the company in
[Solo Data Scientist Playbook]({{ '/podcasts/solopreneur-data-scientist/' | relative_url }}).

[Ioannis Mesionis]({{ '/people/ioannismesionis/' | relative_url }})
describes a lead data scientist operating model in
[Building Data Products at Scale]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }}).
His operating model includes embedded stakeholder meetings and a single intake
path. It also uses definition-of-done templates, pilot tests, and monitoring.
In his version, senior data scientists spend less time on isolated modeling and
more time on product intake, delivery, and organizational trust.

## Core Responsibilities

Data scientists usually own the question before they own the model. In practice,
that means defining the decision and stakeholder. It also means naming the
constraint and success metric. They also check whether the available data can
support the question.

In
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }})
Oleg makes this explicit by moving from business goals to metrics. Only then
does the interview test ML, SQL, and coding.

They then explore data and define features while evaluating assumptions and
choosing a method. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
at 13:56 Roksolana places cleaning, feature preparation, and model iteration on
the data scientist side. At 24:49, she adds that data scientists should
understand pipeline inputs and outputs well enough to collaborate with data
engineers.

They also communicate uncertainty and tradeoffs. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
metric definition changes how a product experiment is interpreted. In
[Interpretable Machine Learning]({{ '/podcasts/interpretable-machine-learning/' | relative_url }}),
[Christoph Molnar]({{ '/people/christophmolnar/' | relative_url }})
connects explanations, conformal prediction, and model trust to the way
stakeholders understand model behavior. Together, Jakob and Christoph connect
the role to [interpretability]({{ '/wiki/interpretability/' | relative_url }}) and
[responsible AI]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

In smaller companies, a data scientist may also prototype a service, batch job,
or dashboard until a dedicated engineer can harden it.
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
names Python, SQL, Flask, and Docker after the analyst-versus-scientist
distinction. Roksolana's episode adds reproducibility and code quality at
46:14. At that point, the role meets
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
and [MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}).

In early-stage or thinly staffed settings, the role may include roadmap and
enablement work. Marianna's 90-day solo data scientist episode moves from first
week stakeholder interviews and data exploration to first-month proofs of
concept. By the first quarter, she expects pipelines and deployment. She also
expects A/B tests.

Ioannis's lead data scientist episode shows a more mature version. The data
scientist helps structure intake, success criteria, and pilots. They also help
with rollout and monitoring so marketing teams know what's being built and why.

## Skills the Role Needs

Data scientists need SQL and data literacy because most data science work starts
by finding, joining, and checking data. In
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }}),
[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }})
describes recruiter screening around experience, education, and actual
responsibilities at 21:32. At 32:40, she warns that buzzwords are weaker than
clear examples.

Python and practical modeling matter, but guests value judgment over tool lists.
A strong data scientist can build a baseline and choose a model. They can
evaluate errors and explain why the result matters. Oleg's interview episode
tests this through business case studies, ML fundamentals, SQL, and coding.
Marijn's career episode adds the missing piece: domain knowledge can be an
advantage when it helps the scientist ask better questions.

Statistics and experimentation are core when the job is product-facing.
Jakob's A/B testing episode covers randomization at 8:13 and metric pitfalls at
14:27. It covers A/A tests at 27:52, noise and seasonality at 33:23, and power
analysis at 37:44. Those skills connect the role to
[data products]({{ '/wiki/data-products/' | relative_url }}) because product
teams need evidence they can act on.

Communication is a first-class skill, not a soft add-on. Luke's recruiting
episode rewards candidates who can explain projects in terms of use case and
industry. It also rewards clear business impact. Tereza's red-flags episode
rewards candidates who ask what problem they'll own. They should also ask who
they'll work with and whether the company has the data maturity to support the
role.

Writing and documentation help data scientists turn project work into shared
memory. In
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
[Eugene Yan]({{ '/people/eugeneyan/' | relative_url }})
connects writing to learning and portfolio proof. He also connects it to design
docs, decision logs, rationales, and clearer READMEs. That links the role to
[technical writing]({{ '/wiki/technical-writing/' | relative_url }}) and
[communication]({{ '/wiki/communication/' | relative_url }}), especially when a
project needs stakeholder buy-in or later handoff.

For career switchers, guests treat the skill set as a gap-finding problem rather
than a fixed checklist.

In
[From Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}),
[Ksenia Legostay]({{ '/people/ksenialegostay/' | relative_url }})
starts from analytics, business KPIs, and planning. She also brings stakeholder
communication. She then adds programming and statistics. Domain expertise also
matters. For production work, she adds Git and testing plus Docker and
deployment readiness.

## Boundaries With Nearby Roles

The boundary with a
[data analyst]({{ '/wiki/data-analyst-role/' | relative_url }}) is fuzzy. A data
scientist usually does more predictive modeling, experiment design, and product
integration. Alicja's recruiting episode notes at 54:09 that analyst and
scientist hiring processes can look similar. The actual responsibilities matter
more than the title.

The boundary with a
[data engineer]({{ '/wiki/data-engineer-role/' | relative_url }}) depends on
ownership. A data scientist owns the decision logic and the model or analysis.
The data engineer owns reliable data movement, storage, orchestration, and
platform quality. Roksolana's episode is the clearest split. ETL, Spark
performance, and storage sit on the engineering side.

Features, models, and deployment awareness sit on the science side. The two
roles meet around feature pipelines, batch scoring, monitoring, and
reproducibility.

The boundary with a
[machine learning engineer]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
often shows up in production work. A data scientist usually owns problem
framing, modeling logic, and evaluation. The ML engineer usually owns packaging
and serving. They also own CI/CD, scalability, and production reliability.
Oleg's 15:29 interview split separates product data scientist expectations from
ML-engineering-heavy expectations.

The boundary with an [AI engineer]({{ '/wiki/ai-engineer-role/' | relative_url }})
is newer. A data scientist brings data, metrics, experiments, and evaluation
habits. AI engineering adds LLM application design and retrieval. It also adds
agents, context management, tool calling, and production UX. The overlap is
strongest when LLM features need evaluation sets, product metrics, and failure
analysis.

## Related Pages

Continue with adjacent roles, career paths, and project patterns:
## Questions to Ask Before Taking a Data Scientist Job

Ask what decisions the team expects the data scientist to improve, and ask how
success will be measured. That keeps the role tied to business or product
outcomes, which is the same framing used in
[CRISP-DM Methodology]({{ '/podcasts/crisp-dm/' | relative_url }}) and
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}).

Ask whether the team needs product analytics or experimentation. Then ask
whether it needs applied ML, research, data engineering support, or a mix.
[Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }})'s
[Data Science Jobs]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }})
episode is the clearest reminder that title clarity isn't enough. Team
maturity, data access, and role ownership matter.

Ask who owns data pipelines and model deployment, then ask who owns monitoring,
dashboards, and production incidents. [Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }})'s
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})
episode shows why these boundaries affect the daily work.
[Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
is the deeper role-boundary reference.

- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }})
- [Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }})
- [Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
- [Machine Learning Engineer vs Data Scientist]({{ '/wiki/machine-learning-engineer-vs-data-scientist/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Communication]({{ '/wiki/communication/' | relative_url }})
- [Technical Writing]({{ '/wiki/technical-writing/' | relative_url }})
- [Data Engineer vs Data Scientist comparison]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})
- [Data Scientist Interview Prep]({{ '/wiki/data-scientist-interview/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
