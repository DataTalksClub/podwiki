---
layout: wiki
title: "Evaluation"
summary: "How DataTalks.Club guests judge whether ML, LLM, RAG, product, and production systems are good enough to trust."
related:
  - Metrics
  - A/B Testing
  - Causal Inference
  - Model Monitoring
  - Retrieval-Augmented Generation
---

Evaluation is the practice of judging whether a model, product change, data
system, or AI workflow is good enough for the decision it supports. In the
DataTalks.Club podcast discussions, guests treat evaluation as more than a
score. They tie it to [metrics]({{ '/wiki/metrics/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}),
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}), and human
review.

The practical definition is direct. Compare the system against a baseline with
a metric that maps to a real decision. Then keep checking whether that judgment
holds in production.

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }})
frames metric work as top-down alignment with executive decisions in
[KPI Design & Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})
at 22:41. He warns against vanity metrics at 26:07 and KPI gaming at 28:04.
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) extends the
same idea to production ML in
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }})
at 28:42. Offline experiments, shadow mode, and A/B tests bridge model work to
product impact.

## Common Definition

Across these episodes, evaluation usually means naming the decision that
will change and the baseline for comparison. It also means naming the evidence
that would make the team stop, roll back, or continue.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the clearest
product version in
[Product Analytics & A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
at 8:13 and 11:48. Teams use randomized experiments to decide whether a product
change caused an outcome, but metric choice shapes the conclusion. At 33:23 and
37:44, he ties that conclusion to metric stability, seasonality, and power
analysis. Those concerns connect directly to
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }}), and
[Power Analysis]({{ '/wiki/power-analysis/' | relative_url }}).

[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) gives the
causal version in
[Causal Inference for Real-World ML]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }})
at 32:40 and 33:14. A causal model needs refutation tests and estimator checks,
but the final policy comparison still uses a business metric. That separates
predictive accuracy from the action decision.

## Guest Differences

Guests differ on where evaluation should start. Product analytics guests start
from user behavior, randomization, and product metrics. ML engineering guests
start from model behavior, baselines, and production constraints. LLM guests
start from task-specific examples, retrieval quality, and answer faithfulness.
They also account for cost, latency, and human review.

The difference reflects the system under test. In
[KPI Design & Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})
at 51:12, [Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) says data
teams need to translate model performance into money, saved time, or another
decision metric. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 53:34 and 56:39, [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
talks about gold-standard examples and output-driven evaluation. She also
separates classification metrics, generative metrics, and human judgment.

In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 48:09, [Atita Arora]({{ '/people/atitaarora/' | relative_url }}) describes
RAG evaluation through multiple metric levels, offline tests, and
human-in-the-loop review.

## ML Evaluation

For supervised machine learning, evaluation starts before deployment. Teams
need a baseline, a holdout strategy, and a metric that matches the business
decision. That can be precision and recall for fraud, uplift for targeting, or
cost-weighted error for operational decisions. The guests repeatedly warn
that the metric alone isn't enough.

[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
ML work as experimental in
[From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }})
at 28:42. Teams can use shadow mode and A/B tests before a model fully controls
a user-facing workflow. At 31:19, he adds segment analysis and root-cause
investigation: a model can improve the average and still fail for a customer
segment that matters.

[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) adds a
different boundary in
[Causal Inference for Real-World ML]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }})
at 12:41. Predictive ML often assumes the future looks like the training data,
but decisions change the system. At 43:25, he points back to A/B testing as a
validation baseline for causal models. That's why [machine learning]({{ '/wiki/machine-learning/' | relative_url }})
evaluation and [causal inference]({{ '/wiki/causal-inference/' | relative_url }})
often meet in product decisions.

## LLM and RAG Evaluation

LLM evaluation depends on the task. Classification-like use cases can still use
labels and accuracy-style metrics. Generative use cases need examples, rubric
checks, human review, and failure analysis because the output can be fluent and
wrong at the same time.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) makes this split in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 53:34 and 56:39. She connects data quality, gold-standard examples, and
human evaluation to production LLM choices. At 18:46, she also flags model
drift and hidden API changes, which means evaluation needs to keep running
after launch.

RAG evaluation adds retrieval to the problem. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 42:49, [Atita Arora]({{ '/people/atitaarora/' | relative_url }}) frames RAG
as retrieval, augmentation, and generation. She also includes prompt design and
citations. At 48:09 and 50:52, she discusses offline tests and human review for
RAG systems.
Evaluation connects RAG to [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[search]({{ '/wiki/search/' | relative_url }}),
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}).

Agentic systems add tool calls and goal completion. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
at 51:17, [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
recommends custom datasets and system benchmarks. At 53:20 and 56:02, she
separates tool-mocking and integration tests from regression tests. She also
uses goal-based assertions.

For [agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}), the
path an agent takes may vary. Evaluation often checks whether the outcome meets
the goal instead of matching every intermediate step.

## Product Metrics

Product evaluation asks whether a change improved user or business outcomes.
Metric design is part of the evaluation system, not a reporting step at the end.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) uses product
experiments to connect causality, metric design, and product decisions in
[Product Analytics & A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
at 14:27 and 18:06. He also discusses A/A tests at 27:52 to validate
randomization and instrumentation before teams trust an experiment platform.
These details connect product evaluation to [product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[metrics]({{ '/wiki/metrics/' | relative_url }}).

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) adds a strategic layer
in
[KPI Design & Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})
at 37:19 and 41:07. Teams need review cadence, dashboards, and executive
communication, not only a mathematically valid metric. At 46:34 and 48:48, he
also separates threshold metrics and health metrics from north-star goals. A
service can be valuable while still requiring guardrails for downtime, safety,
or reliability.

## Monitoring

Production evaluation checks whether the earlier judgment still holds after
data changes. It also has to account for users, infrastructure, and upstream
pipelines. This is where
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[data observability]({{ '/wiki/data-observability/' | relative_url }}), and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) become part
of evaluation.

In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
at 25:04 and 27:35, [Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }})
focuses on production model monitoring and upstream root causes. His discussion
of data profiling at 31:50 shows why production evaluation often starts with
input data and pipeline behavior before the team blames the model.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) connects
monitoring to incident response in
[Master Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
at 24:34 and 27:14. She also discusses live test sets and small A/B tests at
29:23, then input distribution and feature drift at 46:28. Teams turn
evaluation into an operating practice when they define failure, watch for it,
and decide who responds.

## Human Review

Human review appears in these discussions when automatic metrics can't capture the
whole task. It shows up in stakeholder demos and user feedback. It also appears
in RAG quality checks, LLM outputs, and incident investigation.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) emphasizes
stakeholder trust in
[Master Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
at 12:22, 15:07, and 22:36. A demo or report isn't enough if the people who
own the workflow can't see how the model behaves. At 36:41 and 50:30, she
adds user feedback channels and direct user testing as signals that automated
monitoring can miss.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) and
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) make the same point
for LLM systems.

In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 48:09 and 50:52, RAG evaluation includes human-in-the-loop review. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 56:39, generative evaluation includes human judgment because automatic
metrics alone don't prove answer quality. Reviewers still need to judge whether
the answer is useful, grounded, and safe.

## Related Pages

These pages cover adjacent evaluation decisions in more detail.

- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
