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
decision it supports. That boundary applies to [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), [machine learning system
design]({{ '/wiki/machine-learning-system-design/' | relative_url }}), and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
Khuyen Tran's
[Production-Ready Data Science](https://datatalks.club/books/20250728-production-ready-data-science.html)
extends the same dependence and ownership ideas: it covers the
experiment-to-production handoff, testing, reproducibility, and deployment
templates that turn a notebook into a maintained system.
[Reliable Machine Learning](https://datatalks.club/books/20221121-reliable-machine-learning.html)
by Todd Underwood, Kranti K. Parisa, Cathy Chen, and Niall Murphy extends this reliability lens to ML-specific failure modes: data drift, model decay, and the operational practices that keep a deployed ML system trustworthy over time.

## Operational Responsibility

[Ben Wilson](https://datatalks.club/people/benwilson.html) frames production
readiness around maintainable code, business buy-in, testing, and simple
baselines in
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html).
At 44:23, he argues that SQL or statistical baselines should be compared with
deep learning when they can solve the business problem. At 32:03 and 46:22, he
ties experimentation to cost-benefit tradeoffs and warns against copying
academic papers into cloud production without checking assumptions. His
emphasis is production risk from unnecessary complexity, cloud cost, and systems
that nobody can maintain.

[Nadia Nahar](https://datatalks.club/people/nadianahar.html) puts the same
responsibility earlier in the lifecycle in
[Software Engineering for Machine Learning](https://datatalks.club/podcast/software-engineering-for-machine-learning.html).
The episode names unclear requirements, weak data access, and poor documentation
as production risks before release. Team silos and exploratory ML delivery add
more risk. Her 39:05 and 42:47 chapters recommend workshops and shared
vocabulary. They also cover model cards, datasheets, factsheets, and checklists
so teams can preserve the context that a notebook alone doesn't include.

[Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html) gives
the platform version in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
At 4:42, he defines [MLOps]({{ '/wiki/mlops/' | relative_url }}) as people,
operating practices, and technology. Later chapters connect that definition to
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and the
[model registry]({{ '/wiki/model-registry/' | relative_url }}). They also cover
metadata, lineage, API design, and prediction logging.

## Release Paths and Serving Choices

Deployment is the handoff from a working prototype to a repeatable running
system. Production deployment needs a known model artifact and runtime
environment. It also needs data input shape, serving interface, and rollback
path.

[Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
compares serving modes at 31:15 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
He separates batch inference from online serving, then covers orchestration and
production workflows.
A nightly scoring job, a real-time API, and a feature pipeline need different
controls. Production architecture often starts with
[batch vs streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
rather than with a single deployment tool.

[Theofilos Papapanagiotou](https://datatalks.club/people/theofilospapapanagiotou.html)
links deployment to Kubeflow pipelines and model monitoring in
[Mastering MLOps](https://datatalks.club/podcast/mlops-kubeflow-model-monitoring.html).
The episode also covers automated retraining, fairness checks, and edge
deployment. In that view, the release path includes pipeline scheduling, trigger
logic, and criteria for replacing a model.

[Meryem Arik](https://datatalks.club/people/meryemarik.html) moves the release
choice into model supply in
[Deploying LLMs in Production](https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html).
At 49:44 and 51:35, she contrasts fast API prototypes with open-source
deployment. The same choice shapes privacy and hidden API model changes. It also
shapes cost and latency. Hardware, model size, compression, and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
belong to the serving decision.

## Monitoring, Evaluation, and Feedback

Monitoring tells the team whether production behavior still matches the
decision the system supports. Data and ML systems need more than service
uptime. Input quality, feature freshness, prediction distributions, and latency
can all matter. Errors, business outcomes, and fairness checks can matter too.

[Ioannis Mesionis](https://datatalks.club/people/ioannismesionis.html) discusses
this through data products in
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html).
At 25:17, pilots and A/B testing validate models against baseline KPIs. At
53:33, model monitoring includes drift detection and tool integration. The
operating loop has to connect model signals with product metrics, not only model
metrics.

[Daniel Svonava](https://datatalks.club/people/danielsvonava.html) makes the same
point for search systems in
[Building Production Search Systems](https://datatalks.club/podcast/building-production-search-systems.html).
The 1:01:25 and 1:03:50 chapters separate business impact from operational
metrics, then cover A/B testing and offline evaluation. A
[search and RAG system]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
can look technically healthy while relevance gets worse, so monitoring has to
include user-facing quality.

[Bartosz Mikulski](https://datatalks.club/people/bartoszmikulski.html) adds
[testing]({{ '/wiki/testing/' | relative_url }}) as an early monitoring habit in
[Production AI Engineering](https://datatalks.club/podcast/production-ready-ai-engineering.html).
His 9:05 to 13:14 chapters cover data trust, snapshot tests, and integration
tests. They also cover Great Expectations, Soda, SQL tests, and Spark tests. At
28:16, the same discipline moves to prompt evaluation. If a team can't measure
prompt output quality, it can't know whether an AI system is fit for production.

## Reliability and Change Control

Reliability is the ability to keep serving the intended decision when data,
traffic, or dependencies change. Models and users change too. Guests treat
reliability as a system property, not as a property of a model alone.

[Arseny Kravchenko](https://datatalks.club/people/arsenykravchenko.html) anchors
reliability in design constraints in
[Building Scalable and Reliable Machine Learning Systems](https://datatalks.club/podcast/building-scalable-and-reliable-machine-learning-systems.html).
He emphasizes goals, non-goals, and assumptions. He also covers data strategy,
system diagrams, and latency constraints. At 14:49, he covers known unknowns,
unknown unknowns, and early tests.

At 31:42-37:15, he connects reliability to baselines, metrics, and pipeline
components. He also covers dependencies and batch-versus-real-time choices. His
edge and mobile chapters make frames per second, energy use, and hardware limits
part of production design. On-device execution becomes a design constraint too.

[Tomasz Hinc](https://datatalks.club/people/tomaszhinc.html) applies the same
logic to data teams in
[DataOps and GitOps Best Practices](https://datatalks.club/podcast/dataops-and-gitops-best-practices-for-data-teams.html).
He links reproducibility with infrastructure as code, branch-based changes,
review, and safer platform onboarding. The
[DataOps]({{ '/wiki/dataops/' | relative_url }}) contribution is traceability:
pipeline changes should be reviewable and recoverable enough that teams can
reason about failures.

## Cost, Latency, and Model Constraints

Cost and latency are production requirements because they decide whether a
system can run at the scale and response time the product needs. They're also
design constraints because a model may be accurate but too slow or too
expensive. It may also be too large for the target environment. Either case is a
production failure.

[Yury Kashnitsky](https://datatalks.club/people/yurykashnitsky.html) gives a
concrete example: after a gradient boosting model failed to beat a CTR heuristic
baseline, the team discovered the bottleneck was in the serving infrastructure,
not the model. Reducing the re-ranking scope fixed the latency problem. The same
episode also documents the cost of skipping CI/CD — SSH-based deploys meant every
syntax error crashed production until a manual revert
([Data Science Failures and MLOps Lessons](https://datatalks.club/podcast/data-science-failures-and-mlops-lessons.html)).

[Ben Wilson](https://datatalks.club/people/benwilson.html) treats cost as a reason
to avoid unnecessary model complexity in
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html).
His baseline argument at 44:23 is also a cost argument. The simplest system that
solves the business problem belongs in the comparison before a team accepts
heavier production burden.

[Bartosz Mikulski](https://datatalks.club/people/bartoszmikulski.html) treats cost
and latency as prompt and serving concerns in
[Production AI Engineering](https://datatalks.club/podcast/production-ready-ai-engineering.html).
The 28:16-31:45 chapters cover prompt evaluation, prompt compression, and
[caching]({{ '/wiki/caching/' | relative_url }}). A useful AI feature can still
fail operationally if every request is slow or too expensive.

[Meryem Arik](https://datatalks.club/people/meryemarik.html) makes the serving
version of the same point in
[Deploying LLMs in Production](https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html).
The 25:26 and 51:35 chapters cover model size, compression, and inference
optimization. They also cover hardware choices, latency, and cost tradeoffs.

## Security and Governance

Security and governance become production concerns once models interact with
private data, regulated decisions, or external users. Platform controls and
AI-specific failure modes both belong in the operating design.

[Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
discusses regulatory constraints, GDPR, metadata, and lineage at 39:54-45:50 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
He also covers data governance. His framing puts governance inside platform
design rather than after-the-fact audit work.

[Maria Sukhareva](https://datatalks.club/people/mariasukhareva.html) shows why LLM
products need a different checklist in
[Hardening Generative AI Chatbots](https://datatalks.club/podcast/generative-ai-chatbots-in-production-security.html).
The 9:28-18:01 chapters cover chatbot attacks, hallucinations, and data
exfiltration. They also cover output validation, query analysis, and layered
defenses. Production readiness for a chatbot includes
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) and human review.
[Responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
also belongs here when the system can influence customer, employee, or
compliance outcomes.

## Related Pages

These pages cover the operating disciplines, architecture choices, and adjacent
roles that production systems depend on.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
- [Testing]({{ '/wiki/testing/' | relative_url }})
- [Caching]({{ '/wiki/caching/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
