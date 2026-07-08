---
layout: wiki
title: "Evaluation"
summary: "How teams judge whether ML, LLM, RAG, product, and production systems are good enough to trust."
related:
  - Metrics
  - A/B Testing
  - A/A Testing
  - Power Analysis
  - Causal Inference
  - Experimentation
  - Model Monitoring
  - LLM Evaluation Workflows
  - RAG Evaluation Workflow
  - Production Search Evaluation
  - Search Relevance
  - Testing
  - Agent Ops
  - Information Retrieval
  - Context Engineering
  - Retrieval-Augmented Generation
  - Long-Context LLM Evaluation
  - Algorithmic Trading
---

Evaluation asks whether a model, product change, data system, or AI workflow is
good enough for the decision it supports. Teams need a decision and a baseline.
They also need evidence they trust and a way to keep checking the result after
launch.

Evaluation links [[Metrics]] and [[Testing]]. It also links
[[Experimentation]], [[Causal Inference]], [[Model Monitoring]], and human
review.
Teams align metric work with executive decisions instead of vanity metrics or
KPI gaming
[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].
Production ML uses offline experiments, shadow mode, and A/B tests to connect
model work to product impact
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

## Decision, Baseline, and Evidence

Evaluation starts by naming the decision that will change and the baseline for
comparison. Teams also define the evidence that would make them stop, roll
back, or continue. The
[[data-science-project-management=>Data Science Project Guide]] puts that
baseline work into stakeholder scope, handoff, and delivery decisions before
production ML changes behavior.

Product evaluation uses randomized experiments to decide whether a product
change caused an outcome. Metric stability, seasonality, and power analysis all
affect which result a team trusts
[[cite:ab-testing-and-product-experimentation@33:23=>Product Experiments]]
[[cite:ab-testing-and-product-experimentation@37:44=>Product Experiments]].
Those concerns connect directly to [[a-b-testing=>A/B Testing]],
[[a-a-testing=>A/A Testing]], and [[Power Analysis]].

Causal evaluation needs refutation tests, estimator checks, and a final policy
comparison against a business metric. That metric separates predictive accuracy
from the action decision
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
The same policy boundary applies to [[Reinforcement Learning]]. Teams need
trusted offline evaluation, simulators, or staged tests before a learned policy
affects real users or systems
[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].

## Evaluation by System Type

Evaluation isn't one universal checklist. Product analytics starts from user
behavior, randomization, and product metrics. ML engineering starts from model
behavior, baselines, and production constraints. LLM and agent work starts from
task examples, traces, tool behavior, and human review.

Data teams still need to translate performance into money, saved time, or
another decision metric
[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].
For LLMs, gold-standard examples and output-driven evaluation separate
classification metrics, generative metrics, and human judgment
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@56:39=>Deploying LLMs in Production]].
For RAG and search, teams need to evaluate retrieval before judging final
answers
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]].

## ML Evaluation

For supervised machine learning, evaluation starts before deployment. Teams
need a baseline, a holdout strategy, and a metric that matches the business
decision. That can be precision and recall for fraud, uplift for targeting, or
cost-weighted error for operational decisions. The metric alone isn't enough.
The [[machine-learning-system-design-interview=>Machine Learning System Design Interview]]
page turns the same choices into a structured design conversation.

ML teams can use shadow mode and A/B tests before a model controls a
user-facing workflow. Root-cause and segment analysis catch average gains that
still fail a key customer segment
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

Predictive ML often assumes the future looks like the training data, but
decisions change the system. A/B testing is a validation baseline for causal
models
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
That's why [[Machine Learning]] evaluation and [[Causal Inference]] often meet
in product decisions.

[[algorithmic-trading=>Algorithmic Trading]] is a stricter time-ordered
example. Ivan Brigida warns against random train/test splits for market data,
then evaluates the full buy/sell procedure rather than a standalone classifier
score. The strategy check includes ROI, precision on selected buys, and fees
[[cite:algorithmic-trading-with-python-and-machine-learning=>Algorithmic Trading with Python]].

## LLM and RAG Evaluation

LLM evaluation depends on the task. Classification-like use cases can still use
labels and accuracy-style metrics. Generative use cases need examples, rubric
checks, and human review. They need failure analysis too because the output can
be fluent and wrong at the same time.

[[LLM Evaluation Workflows]] should route failures to the layer that failed.
Hugo Bowne-Anderson describes ranking error categories and focusing on
retrieval when retrieval dominates the failures
[[cite:practical-llm-engineering-and-rag@26:43=>Practical LLM Engineering and RAG]].
That links evaluation to [[Context Engineering]] and prompt design. Schema
checks, tool descriptions, and product policy also belong in the routing.

LLM eval sets should be representative and cheap enough for prompt iteration.
Retriever and model iteration have the same constraint. If a team wants to
iterate many times, the gold set has to be runnable. It can't only be
comprehensive
[[cite:practical-llm-engineering-and-rag@23:00=>Practical LLM Engineering and RAG]].

Debuggable LLM products also need logs, traces, and visible function calls.
Teams use them to separate retrieval failures from context assembly failures.
They also help isolate tool-use and generation failures
[[cite:practical-llm-engineering-and-rag@27:38=>Practical LLM Engineering and RAG]].

For chatbots, that failure analysis extends into
[[prompt-injection-and-chatbot-risk-management=>Prompt Injection and Chatbot Risk Management]]
when users can steer the model. It also applies when the model can trigger
unsafe answers or expose retrieved content. Teams may add generated examples
through [[Synthetic Data]], but evaluation still has to show that the augmented
data helps the real task
[[cite:data-centric-ai=>Data-Centric AI]].

Production LLM choices depend on data quality, gold-standard examples, and
human evaluation. Model drift and hidden API changes mean evaluation needs to
keep running after launch
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@18:46=>Deploying LLMs in Production]]
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@56:39=>Deploying LLMs in Production]].
The [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] puts that
ongoing evaluation into a rollout path from assistant baseline to RAG and
operations.
For large-document workflows,
[[long-context-llm-evaluation=>Long-Context LLM Evaluation]] checks whether the
model actually uses the advertised window before teams choose retrieval,
chunking, or summarization
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

RAG evaluation adds retrieval to the problem because the system combines
retrieval, augmentation, and generation. Prompt design and citations become part
of the quality check too
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Modern Search Systems]].
The [[rag-evaluation-workflow=>RAG Evaluation Workflow]] separates those checks
so teams can debug retrieval, context, answer quality, and review before
changing the model.

RAG answer evaluation shouldn't start only from the final answer. The retriever
first finds context, the prompt includes it, and the model generates. The
retriever may miss the expected document or rank it too low. Chunking may also
strip useful context, so prompt work can hide the real failure
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]].

Evaluation connects RAG to [[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
[[Search]], and [[Production Search Evaluation]]. It also connects RAG to
[[Embeddings]] and [[Vector Databases]].

## Search Evaluation

Production search evaluation separates candidate generation from ranking.
Daniel Svonava describes candidate generation as narrowing the haystack, while
the ranker estimates which candidate best matches the query or user behavior
[[cite:building-production-search-systems@12:45=>Building Search Systems]].
That boundary links [[Information Retrieval]], [[Search Relevance]], and
[[Production Search Evaluation]].

Search relevance is operational, not only semantic. Search teams look at logs
for no-result or wrong-result queries, estimate which failures matter most, and
add fixes for high-impact cases
[[cite:building-production-search-systems@20:02=>Building Search Systems]].
Hybrid search also needs separate checks for filters, freshness, and business
rules. Lucene-style `must` and `should` constraints show the difference between
hard filters and softer ranking preferences
[[cite:building-production-search-systems@39:53=>Building Search Systems]].
Those checks connect to [[vector-search-vs-keyword-search=>Vector Search vs Keyword Search]]
and [[vector-database-vs-search-engine=>Vector Database vs Search Engine]].

Search impact should connect to business outcomes. Svonava ties search
performance to dollars, contacts, clicks, and orders. He also uses control
groups, A/B tests, offline evaluation, and engineer-facing iteration metrics
[[cite:building-production-search-systems@61:25=>Building Search Systems]]
[[cite:building-production-search-systems@63:50=>Building Search Systems]].

## Agent Evaluation

Agentic systems add tool calls plus goal completion, so teams can use custom
datasets and system benchmarks. Public benchmarks test model capability, while
product teams need custom examples that represent real users and workflows
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@51:17=>Building Agentic AI Systems]].

Agent tests should look like software tests. Teams can mock tools, assert
outputs, and keep integration and regression tests for real workflows
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@53:20=>Building Agentic AI Systems]].
[[multi-agent-systems=>Multi-Agent Systems]] need the same software-test
approach when coordination becomes part of the expected outcome.

For [[Agent Engineering]], the path an agent takes may vary. Evaluation often
checks the outcome instead of matching every intermediate step. Ranjitha
Kulkarni's calendar-agent example checks for the correct invite and parameters.
It doesn't require one exact trace
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@56:02=>Building Agentic AI Systems]].
That connects [[Agent Engineering]], [[Agent Ops]], [[Testing]], and
[[LLM Evaluation Workflows]].

## Product Metrics

Product evaluation asks whether a change improved user or business outcomes.
Metric design is part of the evaluation system, not a reporting step at the
end.

Product experiments connect causality, metric design, and product decisions.
A/A tests validate randomization and instrumentation before teams trust an
experiment platform
[[cite:ab-testing-and-product-experimentation@24:44=>Product Experiments]]
[[cite:ab-testing-and-product-experimentation@27:52=>Product Experiments]].
These checks connect product evaluation to [[Product Analytics]],
[[Experimentation]], and [[Metrics]].

Teams also need review cadence, dashboards, and executive communication, not
only a mathematically valid metric. Threshold metrics and health metrics are
separate from north-star goals. A service can be valuable while still requiring
guardrails for downtime, safety, or reliability
[[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design & Metrics Strategy]].

## Monitoring

Production evaluation checks whether the earlier judgment still holds after
data changes. It also has to account for users, infrastructure, and upstream
pipelines. This is where [[MLOps]],
[[data-quality-and-observability=>Data Quality and Observability]], and
[[Model Monitoring]] become part of evaluation.

Production model monitoring focuses on upstream root causes. Data profiling
shows why production evaluation often starts with input data and pipeline
behavior before the team blames the model
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].

Monitoring connects to incident response and live test sets. Small A/B tests,
input distribution, and feature drift also matter
[[cite:human-centered-mlops-and-model-monitoring=>Master Human-Centered MLOps]].
Teams turn evaluation into an operating practice when they define failure, watch
for it, and decide who responds. For sensor alerts,
[[sensor-ml-personal-baselines=>Sensor ML Personal Baselines]] makes that
practice concrete by comparing each subject against its own baseline.

## Human Review

Human review matters when automatic metrics can't capture the whole task. It
appears in stakeholder demos and user feedback. Teams also use it for RAG
quality checks, LLM outputs, and incident investigation.

Stakeholders need to see how the model behaves. A demo or report isn't enough
when people own the workflow. User feedback channels and direct user testing
are signals that automated monitoring can miss
[[cite:human-centered-mlops-and-model-monitoring=>Master Human-Centered MLOps]].

RAG evaluation includes human-in-the-loop review
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]].
Generative evaluation includes human judgment because automatic metrics alone
don't prove answer quality
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@56:39=>Deploying LLMs in Production]].
Reviewers still need to judge whether the answer is useful, grounded, and safe.
For labeled examples, rubric checks, and reviewer agreement,
[[annotation-quality-workflows=>Annotation Quality Workflows]] covers the data
work that makes those judgments usable.

## Related Pages

Evaluation routes into these narrower pages when a team knows which system is
being judged.

- [[Metrics]]
- [[a-b-testing=>A/B Testing]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Causal Inference]]
- [[Experimentation]]
- [[Machine Learning System Design]]
- [[MLOps]]
- [[Model Monitoring]]
- [[LLM Evaluation Workflows]]
- [[rag-evaluation-workflow=>RAG Evaluation Workflow]]
- [[Production Search Evaluation]]
- [[Search Relevance]]
- [[Testing]]
- [[Agent Ops]]
- [[Information Retrieval]]
- [[Context Engineering]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Agent Engineering]]
