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
system, or AI workflow is good enough for the decision it supports. It is more
than a score, tied to [[metrics]],
[[experimentation]],
[[causal inference]], and human
review.

The practical definition is direct. Compare the system against a baseline with
a metric that maps to a real decision. Then keep checking whether that judgment
holds in production.

Metric work is top-down alignment with executive decisions, avoiding vanity
metrics and KPI gaming
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy]]).
The same idea extends to production ML, where offline experiments, shadow mode,
and A/B tests bridge model work to product impact
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

## Decision, Baseline, and Evidence

Across these episodes, evaluation starts by naming the decision that will
change and the baseline for comparison. It also names the evidence that would
make the team stop, roll back, or continue.

The product version uses randomized experiments to decide whether a product
change caused an outcome, where metric choice shapes the conclusion through
metric stability, seasonality, and power analysis
([[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing]]).
Those concerns connect directly to
[[a-b-testing|A/B Testing]],
[[a-a-testing|A/A Testing]], and
[[Power Analysis]].

The causal version needs refutation tests and estimator checks, but the final
policy comparison still uses a business metric, separating predictive accuracy
from the action decision
([[podcast:causal-inference-for-machine-learning|Causal Inference for Real-World ML]]).

## Evaluation by System Type

The podcast archive doesn't present evaluation as one universal checklist.
Product analytics work starts from user behavior, randomization, and product
metrics. ML engineering work starts from model behavior, baselines, and
production constraints. LLM work starts from task-specific examples, retrieval
quality, and answer faithfulness. It also accounts for cost, latency, and
human review.

The difference reflects the system under test. Data teams need to translate
model performance into money, saved time, or another decision metric
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy]]).
For LLMs, gold-standard examples and output-driven evaluation separate
classification metrics, generative metrics, and human judgment
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

RAG evaluation works through multiple metric levels, offline tests, and
human-in-the-loop review
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

## ML Evaluation

For supervised machine learning, evaluation starts before deployment. Teams
need a baseline, a holdout strategy, and a metric that matches the business
decision. That can be precision and recall for fraud, uplift for targeting, or
cost-weighted error for operational decisions. The metric alone isn't enough.

ML work is experimental: teams can use shadow mode and A/B tests before a model
fully controls a user-facing workflow, and segment analysis with root-cause
investigation catches cases where a model improves the average and still fails
for a customer segment that matters
([[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]]).

A different boundary: predictive ML often assumes the future looks like the
training data, but decisions change the system, and A/B testing serves as a
validation baseline for causal models
([[podcast:causal-inference-for-machine-learning|Causal Inference for Real-World ML]]).
That's why [[machine learning]]
evaluation and [[causal inference]]
often meet in product decisions.

## LLM and RAG Evaluation

LLM evaluation depends on the task. Classification-like use cases can still use
labels and accuracy-style metrics. Generative use cases need examples, rubric
checks, human review, and failure analysis because the output can be fluent and
wrong at the same time.

This split connects data quality, gold-standard examples, and human evaluation
to production LLM choices. Model drift and hidden API changes mean evaluation
needs to keep running after launch
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

RAG evaluation adds retrieval to the problem. RAG combines retrieval,
augmentation, and generation, along with prompt design and citations, and its
evaluation uses offline tests and human review
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Evaluation connects RAG to [[retrieval-augmented-generation|retrieval-augmented generation]],
[[search]],
[[embeddings]], and
[[vector databases]].

Agentic systems add tool calls and goal completion. Custom datasets and system
benchmarks, tool-mocking and integration tests separated from regression tests,
and goal-based assertions all apply
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For [[agent engineering]], the
path an agent takes may vary. Evaluation often checks whether the outcome meets
the goal instead of matching every intermediate step.

## Product Metrics

Product evaluation asks whether a change improved user or business outcomes.
Metric design is part of the evaluation system, not a reporting step at the end.

Product experiments connect causality, metric design, and product decisions, and
A/A tests validate randomization and instrumentation before teams trust an
experiment platform
([[podcast:ab-testing-and-product-experimentation|Product Analytics & A/B Testing]]).
These details connect product evaluation to [[product analytics]],
[[experimentation]], and
[[metrics]].

A strategic layer adds review cadence, dashboards, and executive communication,
not only a mathematically valid metric. Threshold metrics and health metrics are
separate from north-star goals: a service can be valuable while still requiring
guardrails for downtime, safety, or reliability
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design & Metrics Strategy]]).

## Monitoring

Production evaluation checks whether the earlier judgment still holds after
data changes. It also has to account for users, infrastructure, and upstream
pipelines. This is where
[[MLOps]],
[[data-quality-and-observability|data observability]], and
[[model monitoring]] become part
of evaluation.

Production model monitoring focuses on upstream root causes, and data profiling
shows why production evaluation often starts with input data and pipeline
behavior before the team blames the model
([[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).

Monitoring connects to incident response, live test sets and small A/B tests,
and input distribution and feature drift
([[podcast:human-centered-mlops-and-model-monitoring|Master Human-Centered MLOps]]).
Teams turn evaluation into an operating practice when they define failure, watch
for it, and decide who responds.

## Human Review

Human review appears in these discussions when automatic metrics can't capture the
whole task. It shows up in stakeholder demos and user feedback. It also appears
in RAG quality checks, LLM outputs, and incident investigation.

Stakeholder trust matters: a demo or report isn't enough if the people who own
the workflow can't see how the model behaves. User feedback channels and direct
user testing are signals that automated monitoring can miss
([[podcast:human-centered-mlops-and-model-monitoring|Master Human-Centered MLOps]]).

The same point applies to LLM systems.

RAG evaluation includes human-in-the-loop review
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Generative evaluation includes human judgment because automatic metrics alone
don't prove answer quality
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Reviewers still need to judge whether the answer is useful, grounded, and safe.

## Related Pages

These pages cover adjacent evaluation decisions in more detail.

- [[Metrics]]
- [[a-b-testing|A/B Testing]]
- [[a-a-testing|A/A Testing]]
- [[Power Analysis]]
- [[Causal Inference]]
- [[Experimentation]]
- [[Machine Learning System Design]]
- [[MLOps]]
- [[Model Monitoring]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[Agent Engineering]]
