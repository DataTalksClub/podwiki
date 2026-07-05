---
layout: wiki
title: "Experiments and Causality"
summary: "How teams choose evidence standards for product experiments and causal decisions."
related:
  - Experimentation
  - Causal Inference
  - A/B Testing
  - Metrics
  - Product Analytics
  - Evaluation
---

Experimentation and causal inference meet when a team has to choose evidence for
an applied product or ML decision. The decision might be a feature rollout,
pricing change, or marketing budget. It might also be a recommender policy or
model release. The team needs more than a metric movement. It needs evidence
that the action caused enough change to justify what happens next.

Use [[experimentation]] for the product and ML experiment portfolio. Use
[[a-b-testing=>A/B testing]] for randomized test design and interpretation, and
use [[power analysis]] for sample size and sensitivity. Use [[causal inference]]
for methods and assumptions. The combined question is which evidence standard
fits the decision.

Product teams use randomized experiments with traffic splitting, metric choice,
A/A checks, and power planning
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
Causal ML starts from counterfactual intervention questions rather than ordinary
prediction [[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
Design experiments reduce uncertainty before a team is ready for a causal
estimate [[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

## Choosing the Evidence Standard

Before choosing a method, the team defines the action, metric, and affected
population. It also names the comparison and decision threshold. That turns
[[metrics]] and [[product analytics]] into decision evidence instead of a
dashboard review.

Use an [[a-b-testing=>A/B test]] when the product can assign comparable users or
sessions, log exposure, and wait long enough for the metric to stabilize. Use
[[causal inference]] when the decision is still an intervention question but the
team can't rely on clean randomized assignment. Use design or discovery
experiments when the team isn't yet sure what to build. These are different
points in the decision path, not interchangeable labels
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

## Decision Stage and Evidence

Each decision stage needs a different evidence boundary. Product experimentation
emphasizes live assignment, metric design, sample size, and platform checks
before rollout
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
Causal inference weighs confounders, counterfactual assumptions, and policy
evaluation when randomized traffic is unavailable or incomplete
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
Design experimentation uses prototypes and parallel proofs of concept before an
A/B test or causal model is available
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

The product question should choose the evidence standard. A button copy change,
recommendation policy, media budget, and AI product concept can all involve
causal reasoning. They don't need the same experiment.

## Randomized Experiment Fit

Teams use randomized product experiments for the cleanest applied overlap. They
split traffic and expose treatment users or sessions to a change. They keep a
control group and compare a launch metric chosen in advance. Randomization makes
treatment and control comparable enough to attribute a metric difference to the
tested change
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

The bridge question is whether those requirements are realistic. Teams need
stable assignment, exposure logging, monitoring, and debuggable metrics. They
also need a decision rule. [[a-a-testing=>A/A testing]] validates randomization,
tracking, and metric calculation before interpreting an A/B result. [[Power analysis]]
plans duration from baseline rates, variance, traffic, and detectable effect
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

If the required traffic or time is unavailable, the team hasn't failed at
experimentation. Risk or missing instrumentation can also force a different
evidence standard.

## Missing Randomization

Some decisions still ask whether an intervention changed an outcome even when a
clean traffic split is unavailable. Confounders and unconfoundedness set the
assumptions. Causal feature selection and partial identification define part of
the causal claim. Sensitivity checks, refutation tests, and policy metrics define
the rest
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

[[Causal inference]] covers those method details. In an applied product frame,
they matter because the team still has to decide whether to launch or stop. It
may also need to target or allocate.

Marketing is the clearest setting. Attribution gets ambiguous when customers see
several channels before conversion. Privacy and cookieless tracking push the
problem toward aggregate models, assumptions, and stakeholder communication
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Attribution and Marketing Mix Modeling]].
These constraints push marketing measurement beyond A/B tests and into
[[causal inference]].

Marketing measurement also connects to uplift by linking treatment/control
thinking with data pitfalls
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Attribution and Marketing Mix Modeling]].
In that setting, the team still asks a treatment question. The evidence comes
from attribution models, media mix models, time-series counterfactuals, or
observational treatment/control data instead of a clean traffic split.

## Product and Design Experiments

Not every useful experiment is a causal estimate. Parallel experiments and
proofs of concept let teams remove weak solution paths before they invest in an
AI product. The Double Diamond separates problem framing from solution
exploration, and design sprints use prototypes to test whether a direction
deserves investment
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

These activities don't replace A/B tests. They reduce product uncertainty
before a team has enough traffic, instrumentation, or user trust for a
randomized rollout.

For data and AI products, a technically valid model can still solve the wrong
problem. Data scientists connect product discovery to ML feasibility. A scoping
document uses repeated "why" questions to challenge a proposed solution before
the team turns it into an experiment or build plan. The discussion also ties
experimentation culture to prioritization and measurable learning
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]. Those ideas
fit beside [[data product management]], [[data products]], and
[[data product adoption]].

## Production ML Decisions

In production ML, an offline model metric may improve while the product metric
doesn't. Teams stage validation through offline experiments, shadow mode, and
A/B tests. Uplift and segment analysis show why analysts look at cohorts and
root causes after a live model test. They don't stop at the top-line model score
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

The same concern links to ML system design. Metrics, baselines, and A/B tests
are part of the end-to-end ML pipeline. Production validation runs through A/B
tests, causality, and human labels
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
That connects the topic to [[machine learning system design]], [[MLOps]], and
[[model registry]] work.

## Reading the Result

The evidence standard also shapes the readout.

A randomized A/B test can support rollout when the measured effect is large
enough. The effect also has to be stable and justify the cost
[[cite:ab-testing-and-product-experimentation=>A/B Testing]].

An observational causal estimate needs the assumptions and sensitivity checks
beside the result [[cite:causal-inference-for-machine-learning=>Causal ML]].

A discovery experiment should name what it ruled out or name the next idea to
build [[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

The team shouldn't read every experiment as the same kind of win or loss. A
design sprint can invalidate a weak concept. A shadow-mode check can expose a
model failure before users see it. A causal model can support a targeting
decision when an A/B test is unavailable. A live randomized test can decide a
rollout when assignment, metrics, and duration support the comparison.

## Related Pages

The adjacent topics are:

- [[Experimentation]]
- [[Causal Inference]]
- [[a-b-testing=>A/B Testing]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Metrics]]
- [[Product Analytics]]
- [[Evaluation]]
- [[Data Product Management]]
- [[Data Products]]
- [[Machine Learning System Design]]
- [[Production]]
- [[Data Product Manager]]
- [[Product Analyst]]
