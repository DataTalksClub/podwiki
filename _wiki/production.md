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

## Definition

Production is the point where a data system, ML system, or AI system becomes
part of normal work. People depend on it. Other systems call it. Failures have
a cost.

Across DataTalks.Club episodes, guests use production to mean more than
deployment. Teams need reproducible code, reliable data, and repeatable
releases. They also need monitoring, ownership, security, and recovery paths.

That definition shows up clearly in
[Ben Wilson]({{ '/people/benwilson/' | relative_url }})'s episode on
[practical ML engineering]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
He connects production readiness with maintainable code, business buy-in, and
simple baselines. He also covers cost-benefit tradeoffs and testing before
release.

In [Nadia Nahar]({{ '/people/nadianahar/' | relative_url }})'s
[software engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})
discussion, production problems often start before deployment. She identifies
unclear requirements, weak data access, and poor documentation. Team silos and
the mismatch between exploratory ML work and normal software delivery matter
too.

## Common Definition

The podcast discussions give a practical definition. A production system has an owner, a
release path, observable behavior, and a failure plan. It doesn't have to be
large, real-time, or deep-learning-heavy. It has to be dependable enough for the
decision it supports.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
frames this through the platform layer in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
At the 4:42 chapter, he defines
[MLOps]({{ '/wiki/mlops/' | relative_url }}) as people, operating practices,
and technology.

Later chapters connect that definition to experiment tracking and a
[model registry]({{ '/wiki/model-registry/' | relative_url }}). They also cover
batch inference, online serving, and orchestration. Metadata and lineage matter
after launch. Governance, API design, and prediction logging matter too.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) gives the
same definition from the AI application side in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His production concerns are pipeline tests, data trust, and prompt evaluation.
He also covers prompt compression, caching, and model efficiency. For AI
products, teams need
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for evaluation, caching, and prompt cost control. Model hosting alone isn't
enough.

## Guest Disagreements

Guests agree that production means operational responsibility, but they differ
on where to invest first.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) starts with
maintainability and simplicity. In the 44:23 chapter of
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
he argues for SQL or statistical baselines before deep learning. If the simpler
system can solve the business problem, it belongs in the comparison. This view
treats production risk as
unnecessary complexity, cloud cost, and systems that nobody can maintain.

[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }}) starts
from [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
In
[Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}),
he emphasizes goals, non-goals, and assumptions. He also covers data strategy,
system diagrams, and latency constraints. His edge and mobile chapters turn
production into a constraint problem. Teams have to account for frames per
second, energy use, hardware limits, and whether the model can run where users
need it.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) shifts the production
question toward model supply and serving choices in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
Her episode contrasts API models with open-source models, then connects that
choice to privacy and hidden API model changes. She also covers model size,
compression, and latency. Hardware,
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
and output evaluation are part of the same serving decision.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) brings the
security boundary into the definition. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 9:28 to 18:01 chapters cover chatbot attacks, hallucinations, and data
exfiltration. They also cover output validation, query analysis, and layered
defenses.
Production readiness for a chatbot includes
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) and human review,
not only deployment and uptime.

## Deployment

Deployment is the handoff from a working prototype to a repeatable running
system. In these episodes, good deployment starts before release because teams need
to know the model artifact and runtime environment. They also need the data
inputs, serving interface, and rollback path.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
separates deployment options in the 31:15 chapter of
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He discusses batch inference, online serving, orchestration, and production
workflows. That maps production to
[batch vs streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}) choices.
A nightly scoring job, a real-time API, and a feature pipeline need different
reliability controls.

[Theofilos Papapanagiotou]({{ '/people/theofilospapapanagiotou/' | relative_url }})
connects deployment to [MLOps]({{ '/wiki/mlops/' | relative_url }}) automation in
[Mastering MLOps]({{ '/podcasts/mlops-kubeflow-model-monitoring/' | relative_url }}).
The episode covers Kubeflow pipelines and model monitoring. It also covers
automated retraining, fairness checks, and edge deployment. This expands
production beyond a single release event. Teams also need pipeline scheduling,
trigger logic, and a way to decide when to replace a model.

For LLM systems, [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
adds model serving as a deployment decision.

In the 49:44 and 51:35 chapters of
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she contrasts fast API prototypes with open-source deployment. Teams may need
more control over cost, latency, and privacy. Model behavior matters too.

## Monitoring

Monitoring tells the team whether production behavior still matches the
decision the system supports. In data and ML systems, that means watching more
than service uptime. Teams need input quality, feature freshness, and prediction
distributions. They also need latency, errors, business outcomes, and fairness
checks when the use case needs them.

[Ioannis Mesionis]({{ '/people/ioannismesionis/' | relative_url }}) discusses
this through data products in
[Building Data Products at Scale]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }}).
The 25:17 chapter uses pilots and A/B testing to validate models against
baseline KPIs. The 53:33 chapter connects model monitoring with drift detection
and tool integration. Production monitoring therefore has to connect model
signals with product metrics, not only model metrics.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) makes the same
point for search systems in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
The 1:01:25 and 1:03:50 chapters separate business impact from operational
metrics. They also cover A/B testing and offline evaluation. A
[search and RAG system]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
can look technically healthy while relevance gets worse, so monitoring has to
include user-facing quality.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) adds
[testing]({{ '/wiki/testing/' | relative_url }}) as an early monitoring
practice in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His 9:05 to 13:14 chapters cover data trust, snapshot tests, and integration
tests. They also cover Great Expectations, Soda, SQL tests, and Spark tests. The
same idea applies to prompt evaluation at 28:16. If teams can't measure prompt
output quality, they can't know whether the AI system is fit for production.

## Reliability

Reliability is the ability to keep serving the intended decision when data or
traffic changes. Models, dependencies, and users change too. Guests treat
reliability as a system property, not as a property of a model alone.

[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }})'s
[software engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})
episode is useful because it names failures that happen before runtime. Teams
hit unmet requirements, poor data, deployment gaps, and silos before the service
ever fails. Her 39:05 and 42:47 chapters recommend workshops, shared
vocabulary, and documentation. They also discuss model cards, datasheets,
factsheets, and checklists.
These practices make production systems easier to maintain because they
preserve context that a notebook alone doesn't include.

[Arseny Kravchenko]({{ '/people/arsenykravchenko/' | relative_url }}) puts
reliability into design constraints. In
[Building Scalable and Reliable Machine Learning Systems]({{ '/podcasts/building-scalable-and-reliable-machine-learning-systems/' | relative_url }}),
the 14:49 chapter covers known unknowns, unknown unknowns, and early tests. The
31:42 to 37:15 chapters connect that to baselines, metrics, and pipeline
components. They also cover data strategy, dependencies, and
batch-versus-real-time choices.

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) applies the same idea
to data teams in
[DataOps and GitOps Best Practices]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
His episode links reproducibility with infrastructure as code and branch-based
changes. Review and safer platform onboarding matter too. This is the
[DataOps]({{ '/wiki/dataops/' | relative_url }}) side of production: teams make
pipeline changes traceable so they can reason about failures and recover.

## Cost and Latency

Cost and latency are production requirements because they decide whether a
system can run at the scale and response time the product needs.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) treats cost as a reason
to avoid unnecessary model complexity in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
His 32:03 and 46:22 chapters connect experimentation with cost-benefit tradeoffs
and reproducibility problems when teams copy academic papers into cloud
production without checking assumptions.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) treats cost
and latency as prompt and serving concerns. In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
the 28:16 to 31:45 chapters cover prompt evaluation, prompt compression, and
[caching]({{ '/wiki/caching/' | relative_url }}). That makes cost control part of
AI reliability: a useful feature can still fail operationally if every request
is slow or too expensive.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) makes the serving
version of the same point in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
The 25:26 and 51:35 chapters cover model size, compression, and inference
optimization. They also cover hardware choices, latency, and cost tradeoffs.

## Security and Governance

Security and governance become production concerns once models interact with
private data, regulated decisions, or external users. The podcast discussions connect these
risks to both platform controls and AI-specific failure modes.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
discusses regulatory constraints, GDPR, and metadata in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
His 39:54 to 45:50 chapters also cover lineage and data governance. He treats
governance as part of platform design rather than a later audit task.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) shows why LLM
products need a different security checklist. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
prompt injection, data exfiltration, and hallucinations all belong to
production. Output validation, query analysis, and human-in-the-loop review
belong there too. These controls
connect directly to
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
when a chatbot can influence customer, employee, or compliance outcomes.

## Related Pages

These pages cover the operating disciplines, architecture choices, and adjacent
roles that production systems depend on.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
- [Testing]({{ '/wiki/testing/' | relative_url }})
- [Caching]({{ '/wiki/caching/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
