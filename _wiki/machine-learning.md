---
layout: wiki
title: "Machine Learning"
summary: "How DataTalks.Club podcast discussions frame machine learning as applied modeling, evaluation, production design, monitoring, tools, roles, and business tradeoffs."
related:
  - Data Science
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
DataTalks.Club guests usually describe it as applied modeling inside a larger
decision. Teams choose the problem and check the data. They define labels and
metrics, compare against a baseline, and decide whether the model belongs in a
production system.

Use this page for classic applied ML. Use
[[Data Science]] for the broader work
around analysis, experiments, and stakeholder work. Use
[[Machine Learning System Design]]
for architecture, serving modes, fallbacks, and design documents. When models
already need release or ownership paths, use
[[MLOps]] and
[[Model Monitoring]]. Use
[[MLOps vs DataOps]] when
the operations boundary matters.

Use [[Machine Learning Tools]]
for trackers, platforms, and libraries. Use
[[AI]] or
[[LLM Production Patterns]]
for LLM applications, RAG, and agents.
Mark Ryan and Luca Massaron's
[[book:20250505-machine-learning-for-tabular-data|Machine Learning for Tabular Data]]
covers the classical modeling workflow that anchors much of this discussion:
feature engineering, gradient-boosted trees, and cross-validation for
structured business data.

## Applied Modeling, Not Model Selection

The podcast archive treats ML as a decision discipline before it treats ML as
algorithm choice. In
[[podcast:data-team-roles|Data Team Roles Explained]],
the discussion separates data science, data engineering, and ML engineering
work.
Around 17:04, the
machine learning engineer helps turn models into services and production
systems. Around 24:55, the episode ties prediction quality to a shared product
goal rather than to a notebook metric.

[[podcast:crisp-dm|CRISP-DM Methodology for Data Science Projects]]
gives the project sequence behind that definition. Teams start with business
understanding and data preparation. They then move through modeling,
evaluation, and deployment. The model sits inside the project rather than
replacing the project.

[[person:valeriybabushkin|Valeriy Babushkin]] makes the
same definition concrete in
[[podcast:machine-learning-system-design-interview|ML System Design Interviews]].
His fraud detection and recommendation examples connect labels, features, and
metrics to baselines and serving choices. They also add monitoring, fallbacks,
and production validation. In
[[podcast:building-scalable-and-reliable-machine-learning-systems|Build Scalable, Reliable ML Systems]],
[[person:arsenykravchenko|Arseny Kravchenko]] uses goals
and constraints to keep modeling tied to the system the team needs to run. Data
strategy and system diagrams serve the same purpose.

[[person:robzinkov|Rob Zinkov]] pushes in a different
direction: probabilistic and [[a-b-testing|Bayesian modeling]]
as a composable alternative to the scikit-learn model-selection mindset. In
[[podcast:bayesian-modeling-workflows-and-tools|Bayesian Modeling Workflows and Tools]],
he argues that the distribution-in/distribution-out structure of Bayesian
inference makes analysis incrementally extensible — you can add data and
variables to an existing posterior rather than starting over. He contrasts this
with frequentist point estimates that often require throwing away prior work, and
connects it to probabilistic programming languages that automate sampler
generation from model specifications.

## Problem Framing and Baselines

[[book:20210531-advanced-algorithms-and-data-structures|Advanced Algorithms and Data Structures]]
by Marcello La Rocca covers the algorithmic foundations that underpin
efficient ML feature engineering and retrieval at scale.

[[book:20210208-ml-design-patterns|Machine Learning Design Patterns]] by Valliappa Lakshmanan, Sara Robinson, and Michael Munn catalogues reusable patterns for data representation, model training, and serving that recur across the production ML episodes below.

DataTalks.Club guests start ML with the decision instead of the model. In
[[podcast:crisp-dm|CRISP-DM Methodology for Data Science Projects]],
business understanding asks whether the problem is important, measurable, and
connected to a clear objective before modeling starts.

Arseny turns the same habit into design-document practice in
[[podcast:building-scalable-and-reliable-machine-learning-systems|Build Scalable, Reliable ML Systems]].
Around 20:21 and 29:01, the team defines product scenarios, goals, and
non-goals. It also names assumptions, metrics, and constraints before
implementation.

Baselines keep teams from treating ML as the default answer.
[[person:benwilson|Ben Wilson]] argues for simple
baselines in
[[podcast:machine-learning-engineering-production-best-practices|Practical ML Engineering]].
He also stresses maintainable code and timeboxed proof points before teams
invest in complex systems. The baseline may be SQL, statistics, an
expert rule, or a rapid prototype.

Valeriy uses baselines around 24:28 and
29:09 in
[[podcast:machine-learning-system-design-interview|ML System Design Interviews]].
They compare model lift and avoid overengineering a product decision that does
not need ML.

## Data, Features, and Labels

Data belongs inside the ML system rather than in a separate data-cleaning
bucket. Valeriy uses fraud detection and recommendation examples in
[[podcast:machine-learning-system-design-interview|ML System Design Interviews]].
The examples surface class imbalance and labeling. He also covers feature
engineering, delayed feedback, and serving-time feature availability.

In
[[podcast:building-scalable-and-reliable-machine-learning-systems|Build Scalable, Reliable ML Systems]],
Arseny adds data availability and system diagrams. He also treats real-time
versus batch data flow as a design question.

ML overlaps here with
[[Data Engineering]] and
[[DataOps]]. It also overlaps with
[[MLOps]] when the model moves toward
release. In
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]],
[[person:nadianahar|Nadia Nahar]] treats data access and
unmet requirements as reasons ML products fail. Documentation and deployment
gaps create the same risk.

Feature freshness and label quality belong in the model design.
Privacy constraints and pipeline ownership belong there too because they change
what the model can learn and what it can serve.

## Evaluation and Product Validation

Offline metrics matter, but they don't settle whether an ML system helps the
product. In
[[podcast:machine-learning-system-design-interview|ML System Design Interviews]],
Valeriy connects model metrics to business alignment and A/B testing. He also
brings in production validation and human labels. Around 40:11, goals and proxy
metrics connect ML quality to long-term product health. Around 57:23, production validation brings
A/B tests, causality, and human labels into the same evaluation story.

[[Evaluation]] links modeling to product
impact. In
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]],
[[person:rishabhbhargava|Rishabh Bhargava]] connects
model experiments, A/B testing, and shadow mode around 28:42. Around 31:19, he
adds segmentation, uplift, and root-cause investigation. In
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]],
[[person:jakobgraff|Jakob Graff]] adds randomization,
assignment tracking, and A/A tests. He also covers metric choice, power
analysis, and test duration.

Those topics connect ML evaluation to
[[Experimentation and Causal Inference]]
when the team needs causal evidence rather than offline accuracy alone.

## Roles and Ownership

ML ownership changes as work moves from exploration to production.
[[podcast:data-team-roles|Data Team Roles Explained]]
draws the first boundary. Data engineers make data usable. Data scientists
frame and evaluate predictive work. ML engineers bring models into software
systems.

The
[[Machine Learning Engineer Role]]
is a production-facing extension of ML, not a renamed data scientist.

Rishabh adds the team-building view in
[[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]].
Around 10:48 and 13:48, he distinguishes analytics from ML by the goal of the
work and the output users consume. Dashboards and reports answer questions,
while production ML creates prediction APIs with service-level expectations.
Around 55:41, he describes a hiring sequence where data engineering and
analysis foundations usually come before production ML can scale.

[[person:vinvashishta|Vin Vashishta]] adds the product
strategy boundary in
[[podcast:make-money-with-machine-learning-roles-skills|Monetize Machine Learning]].
Around 20:15 and 1:14:14, he argues that teams may need research, product
management, and architecture skills. Those skills help turn ML from a technical
project into a business capability. A model should create revenue, reduce cost,
improve adoption, or improve decision quality.

## Production Engineering and Operations

Production ML is software engineering with changing data and uncertain
requirements. In
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]],
Nadia traces ML product failures to unclear requirements and data access gaps.
Monitoring needs, weak documentation, and delivery gaps add more failure modes.

Ben's
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]
turns that risk into engineering practice. Teams need modular code, testable
components, and maintainability. They also need stakeholder buy-in and
iterative MVPs before they can operate larger systems.

[[person:simonstiebellehner|Simon Stiebellehner]] makes
operations explicit in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Around 4:42, he defines MLOps through people, repeatable work, and technology.
Around 21:03-31:51, he walks from exploration to training and evaluation.
Experiment tracking, model registries, deployment patterns, and orchestration
come next.

Around 42:48-45:50, metadata and lineage become part of the
platform design. Artifact logging and governance do too.

That operating scope is why
[[MLOps]] and
[[Machine Learning System Design]]
need separate pages even though both start from the same model.

## Monitoring and Feedback

Monitoring is an ML concern because a deployed model can change behavior even
when the code and model artifact stay fixed. In
[[podcast:machine-learning-system-design-interview|ML System Design Interviews]],
Valeriy includes monitoring, distribution shift, and fallbacks in production
robustness around 46:02. In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
Simon adds unified prediction schemas for logging requests, predictions, and
responses around 54:15.

[[person:elenasamuylova|Elena Samuylova]] explains why
monitoring became a product category in
[[podcast:building-mlops-startup|How to Build a Successful ML Startup]].
Around 43:59, she describes validating model monitoring as a business after
seeing teams struggle to understand production model behavior. The
[[Model Monitoring]] page covers
the investigation signals in more depth. Teams watch inputs, predictions,
and labels. They also watch business outcomes, incidents, and response paths.

## Tools, Platforms, and Build-or-Buy

Podcast guests treat ML tools as support for real work, not as a ranked
shopping list. A tool may help with exploration, reproducibility, feature
computation, and serving. It may also help with monitoring, governance, or
collaboration. The
[[Machine Learning Tools]]
page covers that tool-selection layer.

Simon gives the clearest platform example in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Around 34:01, he argues for stitching together existing SaaS, open-source tools,
and self-hosted tools rather than building everything from scratch. Around 47:08
and 49:19, he cautions that teams should build platform pieces alongside real
use, not before the business has models ready to operate.

Vin adds the business version of that build-or-buy question in
[[podcast:make-money-with-machine-learning-roles-skills|Monetize Machine Learning]].
Around 54:50 and 58:04, architecture choices account for platform vision, cost,
and production constraints. Cloud choices, MLOps, and vendor tradeoffs belong
in the same decision.

## Trust, Interpretability, and Governance

Teams need to know what a model can and can't support before they automate a
decision. In
[[podcast:interpretable-machine-learning|Interpretable Machine Learning]],
[[person:christophmolnar|Christoph Molnar]] presents
interpretability as a way to debug models and understand feature effects. The
episode also covers uncertainty communication, transparent models, and post-hoc
explanations. SHAP and conformal prediction give the discussion concrete
methods.

Governance extends that trust work beyond a single explanation. In
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]],
Nadia connects model cards, datasheets, and checklists to responsible ML
products. Explainability requirements belong in that work too. For deeper
treatment of fairness, privacy, and security, use
[[Responsible AI and Governance]]
and [[Interpretability]]. Human
oversight belongs in that same governance discussion.
