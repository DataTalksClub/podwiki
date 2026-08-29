---
layout: wiki
title: "Machine Learning"
summary: "Machine learning as applied modeling, evaluation, production design, monitoring, roles, and business tradeoffs."
related:
  - Data Science
  - Machine Learning vs Software Engineering
  - Machine Learning System Design
  - Machine Learning Engineer Role
  - Machine Learning Tools
  - Model Monitoring
  - Evaluation
  - MLOps
  - DataOps
  - Responsible AI and Governance
  - LLM Production Patterns
  - AI
---

Machine learning turns data into predictions and classifications. It also
powers rankings and recommendations that a product or team can use.
Machine learning is applied modeling inside a larger decision. Teams choose the
problem and check the data. They define labels and metrics, compare against a
baseline, and decide whether the model belongs in a production system.

This topic centers on classic applied ML. The broader work around analysis,
experiments, and stakeholder decisions belongs with
[[Data Science]]. The boundary between ML and ordinary software work is covered
in [[Machine Learning vs Software Engineering]]. Architecture, serving modes,
fallbacks, and design documents belong with
[[Machine Learning System Design]].

When models already need release or ownership paths, connect the work to
[[MLOps]] and
[[Model Monitoring]]. The operations boundary is covered in
[[MLOps vs DataOps]].

Trackers and platforms are covered in
[[Machine Learning Tools]]. [[AI]] and [[LLM Production Patterns]] cover LLM
applications such as RAG and agents.
Mark Ryan and Luca Massaron's
[[book:20250505-machine-learning-for-tabular-data=>Machine Learning for Tabular Data]]
covers feature engineering for structured business data alongside
gradient-boosted trees and cross-validation.

## Applied Modeling, Not Model Selection

ML is a decision discipline before it's algorithm choice. Data team role
boundaries separate data science, data
engineering, and ML engineering work. The machine learning engineer helps turn
models into services and production systems. Prediction quality stays tied to a
shared product goal rather than to a notebook metric.
[[cite:data-team-roles=>Data Team Roles Explained]]

CRISP-DM gives the project sequence behind that definition. Teams start with
business understanding and data preparation before modeling, evaluation, and
deployment. The model sits inside the project rather than replacing the project.
[[cite:crisp-dm=>CRISP-DM Methodology for Data Science Projects]]

[[person:valeriybabushkin=>Valerii Babushkin]] makes the
same definition concrete with fraud detection and recommendation examples that
connect labels, features, and metrics to baselines and serving choices. They
also add monitoring, fallbacks, and production validation.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
In [[podcast:building-scalable-and-reliable-machine-learning-systems=>Build Scalable, Reliable ML Systems]],
[[person:arsenykravchenko=>Arseny Kravchenko]] uses goals and constraints to
keep modeling tied to the system the team needs to run. Data strategy and
system diagrams serve the same purpose.

[[person:robzinkov=>Rob Zinkov]] pushes in a different
direction: probabilistic and [[a-b-testing=>Bayesian modeling]]
as a composable alternative to the [[scikit-learn=>scikit-learn]]
model-selection mindset. In
[[podcast:bayesian-modeling-workflows-and-tools=>Bayesian Modeling Workflows and Tools]],
he argues that the distribution-in/distribution-out structure of Bayesian
inference makes analysis incrementally extensible. Teams can add data and
variables to an existing posterior rather than starting over. He contrasts this
with frequentist point estimates that often require throwing away prior work.
He also connects the workflow to probabilistic programming languages that
automate sampler generation from model specifications.

## Problem Framing and Baselines

[[book:20210531-advanced-algorithms-and-data-structures=>Advanced Algorithms and Data Structures]]
by Marcello La Rocca covers the algorithmic foundations that underpin
efficient ML feature engineering and retrieval at scale.

[[book:20210208-ml-design-patterns=>Machine Learning Design Patterns]] by
Valliappa Lakshmanan and coauthors catalogues reusable patterns for data
representation, model training, and serving. Those patterns recur across
production ML systems.

ML starts with the decision instead of the model. In
[[podcast:crisp-dm=>CRISP-DM Methodology for Data Science Projects]],
business understanding asks whether the problem is important, measurable, and
connected to a clear objective before modeling starts.

Arseny turns the same habit into design-document practice.
[[cite:building-scalable-and-reliable-machine-learning-systems=>Build Scalable, Reliable ML Systems]]
The team defines product scenarios, goals, and non-goals. It also names
assumptions, metrics, and constraints before implementation.

Baselines keep teams from treating ML as the default answer.
[[person:benwilson=>Ben Wilson]] argues for simple
baselines.
[[cite:machine-learning-engineering-production-best-practices=>Practical ML Engineering]]
He also stresses maintainable code and timeboxed proof points before teams
invest in complex systems. The baseline may be SQL, statistics, an
expert rule, or a rapid prototype.

Valeriy uses baselines to compare model lift and avoid overengineering a
product decision that doesn't need ML.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]

## Data, Features, and Labels

Data belongs inside the ML system rather than in a separate data-cleaning
bucket. Valeriy uses fraud detection and recommendation examples.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]
The examples surface class imbalance and labeling. He also covers feature
engineering, delayed feedback, and serving-time feature availability.

In
[[podcast:building-scalable-and-reliable-machine-learning-systems=>Build Scalable, Reliable ML Systems]],
Arseny adds data availability and system diagrams. He also treats real-time
versus batch data flow as a design question.

[[person:marianosemelman=>Mariano Semelman]] connects the same
discipline to model debugging. If a model underperforms, practitioners need to
ask whether it's overfitting first. They also need to separate bad data from
weak features and wrong problem framing before they change algorithms.
[[cite:data-science-leadership-hiring-mlops@26:16=>Data Science Leadership, Hiring, and MLOps]]

ML overlaps here with
[[Data Engineering]] and
[[DataOps]]. It also overlaps with
[[MLOps]] when the model moves toward
release. In
[[podcast:software-engineering-for-machine-learning=>Software Engineering for ML]],
[[person:nadianahar=>Nadia Nahar]] treats data access and
unmet requirements as reasons ML products fail. Documentation and deployment
gaps create the same risk.

Feature freshness and label quality belong in the model design.
Privacy constraints and pipeline ownership belong there too because they change
what the model can learn and what it can serve.

Scientific data can delay the modeling step. Daniel Egbo describes
[[astroinformatics-scientific-data-pipelines=>astroinformatics scientific data pipelines]]
where source detection and cross-matching come before supervised ML. The team
first needs trustworthy candidates and labels.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@11:50=>From Radio Astronomy to Applied ML]][[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@17:54=>From Radio Astronomy to Applied ML]]

In automotive R&D, teams can extract a smaller computational graph from a
larger knowledge graph. They then run similarity analysis or graph ML over that
graph. That work belongs with [[Graph Data Science]] rather than ordinary
tabular feature engineering.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@26:15=>Computational Graphs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@28:55=>SimRank Similarity]]

## Evaluation and Product Validation

Offline metrics matter, but they don't settle whether an ML system helps the
product. Valeriy connects model metrics to business alignment and A/B testing.
His evaluation frame includes production validation, human labels, goals, and
proxy metrics. Production validation brings A/B tests, causality, and human
labels into the same story.
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]]

[[Evaluation]] links modeling to product
impact. In
[[podcast:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]],
[[person:rishabhbhargava=>Rishabh Bhargava]] connects
model experiments, A/B testing, and shadow mode. He also adds segmentation,
uplift, and root-cause investigation. In
[[podcast:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]],
[[person:jakobgraff=>Jakob Graff]] adds randomization,
assignment tracking, and A/A tests. He also covers metric choice, power
analysis, and test duration.

Those topics connect ML evaluation to
[[Experimentation and Causal Inference]]
when the team needs causal evidence rather than offline accuracy alone.
Teams use the same validation frame in
[[ai-for-social-good=>AI for social good]].
Nonprofit optimization and healthcare-access examples judge ML by resource
placement rather than model novelty.[[cite:data-science-and-analytics-for-nonprofits-tech-for-good=>Nonprofit Analytics]]

## Roles and Ownership

ML ownership changes as work moves from exploration to production.
Data engineers make data usable. Data scientists frame and evaluate predictive
work. ML engineers bring models into software systems.
[[cite:data-team-roles=>Data Team Roles Explained]]

The
[[Machine Learning Engineer Role]]
is a production-facing extension of ML, not a renamed data scientist.
[[Machine Learning Engineer vs Data Scientist]] covers that role boundary when
the question is whether the work centers modeling, production ownership, or
handoff.

Rishabh adds the team-building view.
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]]
He distinguishes analytics from ML by the goal of the work and the output users
consume. Dashboards and reports answer questions, while production ML creates
prediction APIs with service-level expectations. He also describes a hiring
sequence where data engineering and analysis foundations usually come before
production ML can scale.

[[person:vinvashishta=>Vin Vashishta]] adds the product
strategy boundary.
[[cite:make-money-with-machine-learning-roles-skills=>Monetize Machine Learning]]
He argues that teams may need research, product management, and architecture
skills. Those skills help turn ML from a technical project into a business
capability. A model should create revenue, reduce cost, improve adoption, or
improve decision quality.

Use [[machine-learning-for-business=>machine learning for business]] when
commercial framing is the main question. Use
[[machine-learning-for-startups=>machine learning for startups]] when the team
has to keep the first ML system lean.

## Production Engineering and Operations

Production ML is
[[machine-learning-vs-software-engineering=>software engineering with changing data and uncertain requirements]].
In
[[podcast:software-engineering-for-machine-learning=>Software Engineering for ML]],
Nadia traces ML product failures to unclear requirements and data access gaps.
Monitoring needs, weak documentation, and delivery gaps add more failure modes.

Ben's
[[podcast:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]
turns that risk into engineering practice. Teams need modular code, testable
components, and maintainability. They also need stakeholder buy-in and
iterative MVPs before they can operate larger systems.

[[person:simonstiebellehner=>Simon Stiebellehner]] makes
operations explicit.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

He defines MLOps through people, repeatable work, and technology before walking
from exploration through training into evaluation. Experiment tracking and
model registries become part of the platform design. Deployment patterns and
orchestration join the design too. Metadata, lineage, artifact logging, and
governance are part of the same platform scope.

That operating scope is why
[[MLOps]] and
[[Machine Learning System Design]]
need separate pages even though both start from the same model.
For engineers entering from software roles, use
[[software-engineer-to-machine-learning=>Software Engineer to Machine Learning]]
for the transition path. Use [[machine-learning-for-software-engineers=>Machine
Learning for Software Engineers]] for the broader engineering-to-ML bridge.

## Monitoring and Feedback

Monitoring is an ML concern because a deployed model can change behavior even
when the code and model artifact stay fixed. In
[[podcast:machine-learning-system-design-interview=>ML System Design Interviews]],
Valeriy includes monitoring, distribution shift, and fallbacks in production
robustness. In
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]],
Simon adds unified prediction schemas for logging requests, predictions, and
responses.

[[person:elenasamuylova=>Elena Samuylova]] explains why
monitoring became a product category.
[[cite:building-mlops-startup=>How to Build a Successful ML Startup]]
She describes validating model monitoring as a business after seeing teams
struggle to understand production model behavior. The
[[Model Monitoring]] page covers
the investigation signals in more depth. Teams watch inputs, predictions,
and labels. They also watch business outcomes, incidents, and response paths.

## Tools, Platforms, and Build-or-Buy

ML tools support real work rather than a ranked shopping list. A tool may help
with exploration, reproducibility, feature computation, and serving. It may also
help with monitoring, governance, or collaboration. The
[[Machine Learning Tools]]
page covers that tool-selection layer.

Simon gives the clearest platform example.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
He argues for stitching together existing SaaS, open-source tools, and
self-hosted tools rather than building everything from scratch. He cautions
that teams should build platform pieces alongside real use, not before the
business has models ready to operate.

Vin adds the business version of that build-or-buy question.
[[cite:make-money-with-machine-learning-roles-skills=>Monetize Machine Learning]]
Architecture choices account for platform vision, cost, and production
constraints. Cloud choices, MLOps, and vendor tradeoffs belong in the same
decision.

## Trust, Interpretability, and Governance

Teams need to know what a model can and can't support before they automate a
decision. In
[[cite:interpretable-machine-learning=>Interpretable Machine Learning]],
[[person:christophmolnar=>Christoph Molnar]] presents
interpretability as a way to debug models and understand feature effects. The
episode also covers uncertainty communication, transparent models, and post-hoc
explanations. SHAP and conformal prediction provide concrete methods.

Governance extends that trust work beyond a single explanation. In
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]],
Nadia connects model cards, datasheets, and checklists to responsible ML
products. Explainability requirements belong in that work too. For deeper
treatment of fairness, privacy, and security, use
[[Responsible AI and Governance]]
and [[Interpretability]]. Human
oversight belongs in that same governance discussion.

For the direct boundary between applied modeling and ordinary software work,
use [[Machine Learning vs Software Engineering]].
