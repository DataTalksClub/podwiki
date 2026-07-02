---
layout: wiki
title: "Production"
summary: "How DataTalks.Club guests define production systems across data, ML, and AI through deployment, monitoring, reliability, ownership, cost, security, and operational feedback."
related:
  - MLOps
  - DataOps
  - Data Quality and Observability
  - Machine Learning System Design
  - LLM Production Patterns
---

Production is the point where a data system, ML system, or AI system becomes
part of normal work. People depend on it. Other systems call it. Failures have
a cost.

In DataTalks.Club discussions, production is less a deployment label than an
operating commitment. The team can release the system and observe its behavior.
It can change the system, recover from failures, and explain outcomes.

The useful boundary is dependence. A production system has an owner, a release
path, observable behavior, and a failure plan. It doesn't have to be large,
real-time, or deep-learning-heavy. It has to be dependable enough for the
decision it supports. That boundary applies to [[MLOps]],
[[DataOps]], [[machine-learning-system-design|machine learning system
design]], and
[[LLM production patterns]].
Khuyen Tran's
[[book:20250728-production-ready-data-science|Production-Ready Data Science]]
extends the same dependence and ownership ideas: it covers the
experiment-to-production handoff, testing, reproducibility, and deployment
templates that turn a notebook into a maintained system.
[[book:20221121-reliable-machine-learning|Reliable Machine Learning]]
by Todd Underwood, Kranti K. Parisa, Cathy Chen, and Niall Murphy extends this reliability lens to ML-specific failure modes: data drift, model decay, and the operational practices that keep a deployed ML system trustworthy over time.

## Operational Responsibility

[[person:benwilson|Ben Wilson]] frames production
readiness around maintainable code, business buy-in, testing, and simple
baselines in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
At 44:23, he argues that SQL or statistical baselines should be compared with
deep learning when they can solve the business problem. At 32:03 and 46:22, he
ties experimentation to cost-benefit tradeoffs and warns against copying
academic papers into cloud production without checking assumptions. His
emphasis is production risk from unnecessary complexity, cloud cost, and systems
that nobody can maintain.

[[person:nadianahar|Nadia Nahar]] puts the same
responsibility earlier in the lifecycle in
[[podcast:software-engineering-for-machine-learning|Software Engineering for Machine Learning]].
The episode names unclear requirements, weak data access, and poor documentation
as production risks before release. Team silos and exploratory ML delivery add
more risk. Her 39:05 and 42:47 chapters recommend workshops and shared
vocabulary. They also cover model cards, datasheets, factsheets, and checklists
so teams can preserve the context that a notebook alone doesn't include.

[[person:simonstiebellehner|Simon Stiebellehner]] gives
the platform version in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
At 4:42, he defines [[MLOps]] as people,
operating practices, and technology. Later chapters connect that definition to
[[experiment tracking]] and the
[[model registry]]. They also cover
metadata, lineage, API design, and prediction logging.

## Release Paths and Serving Choices

Deployment is the handoff from a working prototype to a repeatable running
system. Production deployment needs a known model artifact and runtime
environment. It also needs data input shape, serving interface, and rollback
path.

[[person:simonstiebellehner|Simon Stiebellehner]]
compares serving modes at 31:15 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He separates batch inference from online serving, then covers orchestration and
production workflows.
A nightly scoring job, a real-time API, and a feature pipeline need different
controls. Production architecture often starts with
[[batch vs streaming]]
rather than with a single deployment tool.

[[person:theofilospapapanagiotou|Theofilos Papapanagiotou]]
links deployment to Kubeflow pipelines and model monitoring in
[[podcast:mlops-kubeflow-model-monitoring|Mastering MLOps]].
The episode also covers automated retraining, fairness checks, and edge
deployment. In that view, the release path includes pipeline scheduling, trigger
logic, and criteria for replacing a model.

[[person:meryemarik|Meryem Arik]] moves the release
choice into model supply in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 49:44 and 51:35, she contrasts fast API prototypes with open-source
deployment. The same choice shapes privacy and hidden API model changes. It also
shapes cost and latency. Hardware, model size, compression, and
[[retrieval-augmented-generation|retrieval-augmented generation]]
belong to the serving decision.

## Monitoring, Evaluation, and Feedback

Monitoring tells the team whether production behavior still matches the
decision the system supports. Data and ML systems need more than service
uptime. Input quality, feature freshness, prediction distributions, and latency
can all matter. Errors, business outcomes, and fairness checks can matter too.

[[person:ioannismesionis|Ioannis Mesionis]] discusses
this through data products in
[[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]].
At 25:17, pilots and A/B testing validate models against baseline KPIs. At
53:33, model monitoring includes drift detection and tool integration. The
operating loop has to connect model signals with product metrics, not only model
metrics.

[[person:danielsvonava|Daniel Svonava]] makes the same
point for search systems in
[[podcast:building-production-search-systems|Building Production Search Systems]].
The 1:01:25 and 1:03:50 chapters separate business impact from operational
metrics, then cover A/B testing and offline evaluation. A
[[search-rag-and-knowledge-systems|search and RAG system]]
can look technically healthy while relevance gets worse, so monitoring has to
include user-facing quality.

[[person:bartoszmikulski|Bartosz Mikulski]] adds
[[testing]] as an early monitoring habit in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His 9:05 to 13:14 chapters cover data trust, snapshot tests, and integration
tests. They also cover Great Expectations, Soda, SQL tests, and Spark tests. At
28:16, the same discipline moves to prompt evaluation. If a team can't measure
prompt output quality, it can't know whether an AI system is fit for production.

## Reliability and Change Control

Reliability is the ability to keep serving the intended decision when data,
traffic, or dependencies change. Models and users change too. Guests treat
reliability as a system property, not as a property of a model alone.

[[person:arsenykravchenko|Arseny Kravchenko]] anchors
reliability in design constraints in
[[podcast:building-scalable-and-reliable-machine-learning-systems|Building Scalable and Reliable Machine Learning Systems]].
He emphasizes goals, non-goals, and assumptions. He also covers data strategy,
system diagrams, and latency constraints. At 14:49, he covers known unknowns,
unknown unknowns, and early tests.

At 31:42-37:15, he connects reliability to baselines, metrics, and pipeline
components. He also covers dependencies and batch-versus-real-time choices. His
edge and mobile chapters make frames per second, energy use, and hardware limits
part of production design. On-device execution becomes a design constraint too.

[[person:tomaszhinc|Tomasz Hinc]] applies the same
logic to data teams in
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps Best Practices]].
He links reproducibility with infrastructure as code, branch-based changes,
review, and safer platform onboarding. The
[[DataOps]] contribution is traceability:
pipeline changes should be reviewable and recoverable enough that teams can
reason about failures.

## Cost, Latency, and Model Constraints

Cost and latency are production requirements because they decide whether a
system can run at the scale and response time the product needs. They're also
design constraints because a model may be accurate but too slow or too
expensive. It may also be too large for the target environment. Either case is a
production failure.

[[person:yurykashnitsky|Yury Kashnitsky]] gives a
concrete example: after a gradient boosting model failed to beat a CTR heuristic
baseline, the team discovered the bottleneck was in the serving infrastructure,
not the model. Reducing the re-ranking scope fixed the latency problem. The same
episode also documents the cost of skipping CI/CD — SSH-based deploys meant every
syntax error crashed production until a manual revert
([[podcast:data-science-failures-and-mlops-lessons|Data Science Failures and MLOps Lessons]]).

[[person:benwilson|Ben Wilson]] treats cost as a reason
to avoid unnecessary model complexity in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
His baseline argument at 44:23 is also a cost argument. The simplest system that
solves the business problem belongs in the comparison before a team accepts
heavier production burden.

[[person:bartoszmikulski|Bartosz Mikulski]] treats cost
and latency as prompt and serving concerns in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
The 28:16-31:45 chapters cover prompt evaluation, prompt compression, and
[[caching]]. A useful AI feature can still
fail operationally if every request is slow or too expensive.

[[person:meryemarik|Meryem Arik]] makes the serving
version of the same point in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
The 25:26 and 51:35 chapters cover model size, compression, and inference
optimization. They also cover hardware choices, latency, and cost tradeoffs.

## Security and Governance

Security and governance become production concerns once models interact with
private data, regulated decisions, or external users. Platform controls and
AI-specific failure modes both belong in the operating design.

[[person:simonstiebellehner|Simon Stiebellehner]]
discusses regulatory constraints, GDPR, metadata, and lineage at 39:54-45:50 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He also covers data governance. His framing puts governance inside platform
design rather than after-the-fact audit work.

[[person:mariasukhareva|Maria Sukhareva]] shows why LLM
products need a different checklist in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
The 9:28-18:01 chapters cover chatbot attacks, hallucinations, and data
exfiltration. They also cover output validation, query analysis, and layered
defenses. Production readiness for a chatbot includes
[[AI red teaming]] and human review.
[[Responsible AI and governance]]
also belongs here when the system can influence customer, employee, or
compliance outcomes.

## Related Pages

These pages cover the operating disciplines, architecture choices, and adjacent
roles that production systems depend on.

- [[MLOps]]
- [[DataOps]]
- [[MLOps vs DataOps]]
- [[Machine Learning System Design]]
- [[Machine Learning Infrastructure]]
- [[ML Platforms]]
- [[Data Quality and Observability]]
- [[LLM Production Patterns]]
- [[AI Red Teaming]]
- [[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]]
- [[Batch vs Streaming]]
- [[Testing]]
- [[Caching]]
- [[Software Engineering]]
