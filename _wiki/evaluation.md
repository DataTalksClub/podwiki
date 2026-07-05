---
layout: wiki
title: "Evaluation"
summary: "How teams judge whether ML, LLM, RAG, product, and production systems are good enough to trust."
related:
  - Metrics
  - A/B Testing
  - Causal Inference
  - Model Monitoring
  - Retrieval-Augmented Generation
  - Long-Context LLM Evaluation
  - Algorithmic Trading
---

Evaluation means judging whether a model, product change, data system, or AI
workflow is good enough for the decision it supports. It's more than a score.
It connects [[metrics]], [[experimentation]], [[causal inference]], and human
review.

In practice, teams compare the system against a baseline with a metric that maps
to a real decision. Then they keep checking whether that judgment holds in
production.

Teams align metric work with executive decisions instead of vanity metrics or
KPI gaming[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].
Production ML uses offline experiments, shadow mode, and A/B tests to connect
model work to product impact[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

## Decision, Baseline, and Evidence

Evaluation starts by naming the decision that will change and the baseline for
comparison. Teams also define the evidence that would make them stop, roll back,
or continue.

Product evaluation uses randomized experiments to decide whether a product
change caused an outcome. Metric stability, seasonality, and power analysis all
affect which result a team trusts[[cite:ab-testing-and-product-experimentation=>Product Analytics & A/B Testing]].
Those concerns connect directly to
[[a-b-testing=>A/B Testing]],
[[a-a-testing=>A/A Testing]], and
[[Power Analysis]].

Causal evaluation needs refutation tests and estimator checks. The final policy
comparison still uses a business metric, which separates predictive accuracy
from the action decision[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

## Evaluation by System Type

Evaluation isn't one universal checklist. Product analytics work starts from
user behavior, randomization, and product metrics. ML engineering work starts
from model behavior, baselines, and production constraints. LLM work starts from
task-specific examples, retrieval quality, and answer faithfulness. It also
accounts for cost, latency, and human review.

Different systems need different evaluation evidence. Data teams need to
translate model performance into money, saved time, or another decision
metric[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].
For LLMs, gold-standard examples and output-driven evaluation separate
classification metrics, generative metrics, and human judgment[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

RAG evaluation works through multiple metric levels, offline tests, and
human-in-the-loop review[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

## ML Evaluation

For supervised machine learning, evaluation starts before deployment. Teams
need a baseline, a holdout strategy, and a metric that matches the business
decision. That can be precision and recall for fraud, uplift for targeting, or
cost-weighted error for operational decisions. The metric alone isn't enough.

ML teams can use shadow mode and A/B tests before a model controls a
user-facing workflow. Root-cause and segment analysis catch average gains that
still fail a key customer segment[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

Predictive ML often assumes the future looks like the training data, but
decisions change the system. A/B testing is a validation baseline for causal
models[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
That's why [[machine learning]]
evaluation and [[causal inference]]
often meet in product decisions.

[[algorithmic-trading=>Algorithmic trading]] is a stricter time-ordered
example. Ivan Brigida warns against random train/test splits for market data,
then evaluates the full buy/sell procedure rather than a standalone classifier
score. The strategy check includes ROI, precision on selected buys, and fees
[[cite:algorithmic-trading-with-python-and-machine-learning=>Algorithmic Trading with Python]].

## LLM and RAG Evaluation

LLM evaluation depends on the task. Classification-like use cases can still use
labels and accuracy-style metrics. Generative use cases need examples, rubric
checks, human review, and failure analysis because the output can be fluent and
wrong at the same time.

Production LLM choices depend on data quality, gold-standard examples, and
human evaluation. Model drift and hidden API changes mean evaluation needs to
keep running after launch[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
For large-document workflows,
[[long-context-llm-evaluation=>long-context LLM evaluation]] checks whether the
model actually uses the advertised window before teams choose retrieval,
chunking, or summarization[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

RAG evaluation adds retrieval to the problem because the system combines
retrieval, augmentation, and generation. Prompt design and citations become part
of the quality check too. Teams evaluate RAG with offline tests and human
review[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
Evaluation connects RAG to
[[retrieval-augmented-generation=>retrieval-augmented generation]], [[search]],
[[embeddings]], and [[vector databases]].

Agentic systems add tool calls plus goal completion, so teams can use custom
datasets and system benchmarks. Tool-mocking, integration tests separated from
regression tests, and goal-based assertions also apply[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

For [[agent engineering]], the
path an agent takes may vary. Evaluation often checks whether the outcome meets
the goal instead of matching every intermediate step.

## Product Metrics

Product evaluation asks whether a change improved user or business outcomes.
Metric design is part of the evaluation system, not a reporting step at the end.

Product experiments connect causality, metric design, and product decisions.
A/A tests validate randomization and instrumentation before teams trust an
experiment platform[[cite:ab-testing-and-product-experimentation=>Product Analytics & A/B Testing]].
These checks connect product evaluation to [[product analytics]],
[[experimentation]], and [[metrics]].

Teams also need review cadence, dashboards, and executive communication, not
only a mathematically valid metric. Threshold metrics and health metrics are
separate from north-star goals. A service can be valuable while still requiring
guardrails for downtime, safety, or reliability[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].

## Monitoring

Production evaluation checks whether the earlier judgment still holds after
data changes. It also has to account for users, infrastructure, and upstream
pipelines. This is where
[[MLOps]],
[[data-quality-and-observability=>data observability]], and
[[model monitoring]] become part
of evaluation.

Production model monitoring focuses on upstream root causes. Data profiling
shows why production evaluation often starts with input data and pipeline
behavior before the team blames the model[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].

Monitoring connects to incident response and live test sets. Small A/B tests,
input distribution, and feature drift also matter[[cite:human-centered-mlops-and-model-monitoring=>Master Human-Centered MLOps]].
Teams turn evaluation into an operating practice when they define failure, watch
for it, and decide who responds.

## Human Review

Human review matters when automatic metrics can't capture the whole task. It
appears in stakeholder demos and user feedback. Teams also use it for RAG
quality checks, LLM outputs, and incident investigation.

Stakeholders need to see how the model behaves. A demo or report isn't enough
when people own the workflow. User feedback channels and direct
user testing are signals that automated monitoring can miss[[cite:human-centered-mlops-and-model-monitoring=>Master Human-Centered MLOps]].

RAG evaluation includes human-in-the-loop review[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
Generative evaluation includes human judgment because automatic metrics alone
don't prove answer quality[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Reviewers still need to judge whether the answer is useful, grounded, and safe.
For labeled examples, rubric checks, and reviewer agreement,
[[annotation-quality-workflows=>annotation quality workflows]] covers the data
work that makes those judgments usable.

## Related Pages

These pages cover adjacent evaluation decisions in more detail.

- [[Metrics]]
- [[a-b-testing=>A/B Testing]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Causal Inference]]
- [[Experimentation]]
- [[Machine Learning System Design]]
- [[MLOps]]
- [[Model Monitoring]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Agent Engineering]]
