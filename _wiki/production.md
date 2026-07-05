---
layout: wiki
title: "Production"
summary: "Production for data, ML, and AI systems, covering deployment, monitoring, reliability, ownership, and cost."
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

Production is less a deployment label than an
operating commitment. The team can release the system and observe its behavior.
It can change the system, recover from failures, and explain outcomes.

The useful boundary is dependence. A production system has an owner, a release
path, observable behavior, and a failure plan. It doesn't have to be large,
real-time, or deep-learning-heavy. It has to be dependable enough for the
decision it supports.

Field teams face the same dependence test in
[[ai-for-social-good=>AI for social good]]
projects. Accessibility, healthcare-access, and conservation systems have to
leave the demo stage before people depend on their outputs. For physical-world
systems, [[Simulation and Digital Twins]] can be part of that validation path
before release.[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Applied CV]][[cite:ai-for-ecology-biodiversity-and-conservation=>Conservation AI]]

That boundary applies to [[MLOps]],
[[DataOps]], [[machine-learning-system-design=>machine learning system
design]], and
[[LLM production patterns]].

Khuyen Tran's
[[book:20250728-production-ready-data-science=>Production-Ready Data Science]]
extends the same dependence and ownership ideas. It covers handoff, testing,
reproducibility, and deployment templates for turning a notebook into a
maintained system.

[[book:20221121-reliable-machine-learning=>Reliable Machine Learning]]
by Todd Underwood, Kranti K. Parisa, Cathy Chen, and Niall Murphy extends this
reliability lens to ML-specific failure modes. It focuses on data drift, model
decay, and the practices that keep a deployed ML system trustworthy over time.

## Operational Responsibility

[[person:benwilson=>Ben Wilson]] frames production
readiness around maintainable code, business buy-in, testing, and simple
baselines. He argues that SQL or statistical baselines should be compared with
deep learning when they can solve the business problem. He also ties
experimentation to cost-benefit tradeoffs and warns against copying academic
papers into cloud production without checking assumptions
[[cite:machine-learning-engineering-production-best-practices=>Ben Wilson]].
His emphasis is production risk from unnecessary complexity, cloud cost, and
systems that nobody can maintain.

[[person:nadianahar=>Nadia Nahar]] puts the same
responsibility earlier in the lifecycle.
She names unclear requirements, weak data access, and poor documentation as
production risks before release, with team silos and exploratory ML delivery
adding more risk. Nahar recommends workshops and shared vocabulary. She also
connects those practices to model cards, datasheets, factsheets, and checklists.
Those records preserve the context that a notebook alone doesn't include
[[cite:software-engineering-for-machine-learning=>Nadia Nahar]].

[[person:simonstiebellehner=>Simon Stiebellehner]] gives
the platform version. He defines [[MLOps]] as people,
operating practices, and technology, then connects that definition to
[[experiment tracking]] and the
[[model registry]]. He also covers
metadata, lineage, API design, and prediction logging
[[cite:building-production-ml-platform-and-mlops-team=>Simon Stiebellehner]].

## Release Paths and Serving Choices

Deployment is the handoff from a working prototype to a repeatable running
system. Production deployment needs a known model artifact and runtime
environment. It also needs data input shape, serving interface, and rollback
path.

[[person:simonstiebellehner=>Simon Stiebellehner]]
compares serving modes in his ML platform discussion.
He separates batch inference from online serving, then covers orchestration and
production workflows.
A nightly scoring job, a real-time API, and a feature pipeline need different
controls. Production architecture often starts with
[[batch vs streaming]]
rather than with a single deployment tool
[[cite:building-production-ml-platform-and-mlops-team=>Serving modes]].

[[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]]
links deployment to Kubeflow pipelines and model monitoring. The episode also
covers automated retraining, fairness checks, and edge
deployment. In that view, the release path includes pipeline scheduling, trigger
logic, and criteria for replacing a model
[[cite:mlops-kubeflow-model-monitoring=>Kubeflow and monitoring]].

[[person:meryemarik=>Meryem Arik]] moves the release
choice into model supply by contrasting fast API prototypes with open-source
deployment. The same choice shapes privacy, hidden API model changes, cost, and
latency. Hardware, model size, compression, and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
belong to the serving decision
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Meryem Arik]].

## Monitoring, Evaluation, and Feedback

Monitoring tells the team whether production behavior still matches the
decision the system supports. Data and ML systems need more than service
uptime. Input quality, feature freshness, prediction distributions, and latency
can all matter. Errors, business outcomes, and fairness checks can matter too.

[[person:ioannismesionis=>Ioannis Mesionis]] discusses
this through data products. Pilots and A/B testing validate models against
baseline KPIs, while model monitoring covers drift detection and tool
integration. The team has to connect model signals with product metrics, not
only model metrics
[[cite:building-data-products-lead-data-scientist=>Data products]].

[[person:danielsvonava=>Daniel Svonava]] makes the same
point for search systems. He separates business impact from operational metrics,
then covers A/B testing and offline evaluation. A
[[retrieval-augmented-generation=>search and RAG system]]
can look technically healthy while relevance gets worse, so monitoring has to
include user-facing quality
[[cite:building-production-search-systems=>Production search]].

[[person:bartoszmikulski=>Bartosz Mikulski]] adds
[[testing]] as an early monitoring habit in
AI engineering work. He covers data trust, snapshot tests, and integration
tests. He also covers Great Expectations, Soda, SQL tests, and Spark tests. The
same discipline moves to prompt evaluation. A team that can't measure prompt
output quality can't know whether an AI system is fit for production
[[cite:production-ready-ai-engineering=>Production AI engineering]].

## Reliability and Change Control

Reliability is the ability to keep serving the intended decision when data,
traffic, or dependencies change. Models and users change too. It's a system
property, not a property of a model alone.

[[person:arsenykravchenko=>Arseny Kravchenko]] anchors
reliability in design constraints by emphasizing goals, non-goals, and
assumptions. He also covers data strategy and system diagrams. His reliability
discussion includes latency constraints, known unknowns, unknown unknowns, and
early tests
[[cite:building-scalable-and-reliable-machine-learning-systems=>Arseny Kravchenko]].

He also connects reliability to baselines, metrics, and pipeline components.
Dependencies and batch-versus-real-time choices become part of the reliability
discussion. In his edge and mobile examples, frames per second, energy use, and
hardware limits become part of production design. On-device execution becomes a
design constraint too
[[cite:building-scalable-and-reliable-machine-learning-systems=>Edge constraints]].

[[person:tomaszhinc=>Tomasz Hinc]] applies the same
logic to data teams in
[[DataOps]] and GitOps work. He links reproducibility with infrastructure as
code, branch-based changes, review, and safer platform onboarding. The
[[DataOps]] contribution is traceability:
pipeline changes should be reviewable and recoverable enough that teams can
reason about failures
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps]].

## Cost, Latency, and Model Constraints

Cost and latency are production requirements because they decide whether a
system can run at the scale and response time the product needs. They're also
design constraints because a model may be accurate but too slow or too
expensive. It may also be too large for the target environment. Either case is a
production failure.

[[person:yurykashnitsky=>Yury Kashnitsky]] gives a
concrete example in
[[cite:data-science-failures-and-mlops-lessons=>Data science failures]].
After a gradient boosting model failed to beat a CTR heuristic baseline, the
team found the bottleneck in serving infrastructure, not in the model. Reducing
the re-ranking scope fixed the latency problem.

The same episode also documents the cost of skipping CI/CD. The team's SSH-based
deploys meant every syntax error crashed production until a manual revert
[[cite:data-science-failures-and-mlops-lessons=>Manual deploys]].

[[person:benwilson=>Ben Wilson]] treats cost as a reason
to avoid unnecessary model complexity. His baseline argument is also a cost
argument. The simplest system that solves the business problem belongs in the
comparison before a team accepts heavier production burden
[[cite:machine-learning-engineering-production-best-practices=>Baselines and cost]].

[[person:bartoszmikulski=>Bartosz Mikulski]] treats cost
and latency as prompt and serving concerns in
AI engineering. He covers prompt evaluation, prompt compression, and
[[caching]]. A useful AI feature can still
fail operationally if every request is slow or too expensive
[[cite:production-ready-ai-engineering=>Prompt cost and latency]].

[[person:meryemarik=>Meryem Arik]] makes the serving
version of the same point. She covers model size, compression, and inference
optimization. She also covers hardware choices, latency, and cost tradeoffs
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>LLM serving choices]].

## Security and Governance

Security and governance become production concerns once models interact with
private data, regulated decisions, or external users. Platform controls and
AI-specific failure modes both belong in the operating design.

[[person:simonstiebellehner=>Simon Stiebellehner]]
discusses regulatory constraints, GDPR, metadata, and lineage. He also covers
data governance, putting governance inside platform design rather than
after-the-fact audit work
[[cite:building-production-ml-platform-and-mlops-team=>ML platform governance]].

[[person:mariasukhareva=>Maria Sukhareva]] shows why LLM
products need a different checklist in
generative AI chatbot work. She covers chatbot attacks, hallucinations, data
exfiltration. She also covers output validation, query analysis, and layered
defenses.
Production readiness for a chatbot includes
[[AI red teaming]] and human review.
[[Responsible AI and governance]]
also belongs here when the system can influence customer, employee, or
compliance outcomes
[[cite:generative-ai-chatbots-in-production-security=>Chatbot security]].

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
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Batch vs Streaming]]
- [[Testing]]
- [[Caching]]
- [[Software Engineering]]
