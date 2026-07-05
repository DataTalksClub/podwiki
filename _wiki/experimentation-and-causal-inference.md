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

[[experimentation]] covers the product and ML experiment portfolio.
[[a-b-testing=>A/B testing]] covers randomized test design and interpretation,
and [[power analysis]] covers sample size and sensitivity. [[causal inference]]
covers methods and assumptions. The combined question is which evidence standard
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

## Evidence Options

A button copy change and a recommendation policy can both involve causal
reasoning. The same is true for media budget and AI product concepts, but they
don't need the same experiment.

Teams use randomized product tests when they can assign comparable users or
sessions. They also need logged exposure, stable metrics, and a result they can
act on
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
For operating details, use [[a-b-testing=>A/B testing]], [[a-a-testing=>A/A
testing]], and [[power analysis]].

Causal methods fit when the decision still asks what the intervention changed,
but clean randomization is unavailable or incomplete. Product discovery
experiments fit earlier, when the team is still testing the problem or solution
direction
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

## Missing Randomization

Some decisions still ask whether an intervention changed an outcome even when a
clean traffic split is unavailable. Confounders and unconfoundedness set the
assumptions. Causal feature selection and partial identification define part of
the causal claim. Sensitivity checks, refutation tests, and policy metrics define
the rest
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

[[causal inference]] covers those method details. The applied question is
whether the team has enough support to launch, stop, target, or allocate.

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

## Discovery and Release Checks

Not every useful experiment is a causal estimate. Parallel experiments and
proofs of concept can rule out weak AI-product directions early. Design sprints
serve the same purpose before a team has enough traffic, instrumentation, or
user trust for a randomized rollout
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]. That
decision work belongs with [[experimentation]], [[data product management]],
[[data products]], and [[data product adoption]].

Production ML adds another boundary. An offline model metric may improve while
the product metric doesn't. Teams can stage evidence through offline experiments
and shadow mode. Live A/B tests, segment analysis, and root-cause review then
support rollout
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].
[[experimentation]] covers the release practice, and
[[machine learning system design]] covers the pipeline context.

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
