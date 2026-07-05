---
layout: wiki
title: "Experimentation"
summary: "Experiments for reducing product, ML, and organizational uncertainty before rollout."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - A/A Testing
  - Power Analysis
  - Causal Inference
  - Product Analytics
  - Data Product Management
  - Production
  - Machine Learning System Design
---

Experimentation tests a product, ML, or data-product change before a team commits
to a wider rollout. It includes live product tests and offline model
experiments. It also includes shadow-mode checks, prototypes, proofs of concept,
and small demand signals. Teams use those experiments to decide what to build
next, what to ship, and what to debug or pause.

[[a-b-testing=>A/B testing]] covers randomized product-test design, and
[[power analysis]] covers sample size planning.
[[experimentation and causal inference]] covers the evidence-standard choice,
while [[causal inference]] covers counterfactual methods. For product
and ML practice, teams still choose which experiment fits the uncertainty. They
also decide how to run it and reuse what they learn.

Product experiments de-risk features under noisy product conditions, but they do
more than approve or reject a release. They show which behavior moved, where the
effect appeared, and which assumption was wrong
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

## Product and ML Experiment Shapes

Experimentation turns an uncertain decision into evidence the team can act on.
The evidence may be statistical, behavioral, technical, or organizational. It
has to connect to a rollout, prioritization, or design decision.

In [[product analytics]], the live-test format usually compares a control group
with a treatment group. The team needs logged exposure and one agreed
[[metrics=>metric]] before it can connect the result to a rollout decision
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
[[a-b-testing=>A/B testing]] covers the detailed assignment, metric, and readout
work.

In [[production=>production ML]] and AI product work, experimentation spans
offline model development, validation after deployment, and live rollout checks.
Teams may compare features and hyperparameters before deployment. Then they can
use shadow mode or [[a-b-testing=>A/B tests]] before exposing a model to all
traffic
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

In product discovery, parallel experiments and proofs of concept remove weak
solution paths before an AI roadmap becomes expensive. Teams use Double Diamond
problem framing to test the problem, not only the proposed model or feature
[[cite:ai-ml-product-design-and-experimentation@16:02=>AI Product Design]].

## Questions Experiments Answer

Each setting reduces a different kind of uncertainty.

Product analytics starts from whether a product change changed the chosen
metric. Traffic splitting, assignment tracking, and [[a-a-testing=>A/A tests]]
protect the comparison. Metric stability and [[power analysis]] matter because a
broken measurement system creates false confidence
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Production ML starts from the boundary between offline validation and live model
behavior. A live model test still needs uplift, segmentation, and root-cause
analysis after the top-line result appears
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

AI product discovery starts before the team commits to a solution. Scoping
documents and repeated "why" questions challenge the proposed solution, while
experimentation culture connects discovery work to measurable prioritization
[[cite:ai-ml-product-design-and-experimentation@54:11=>AI Product Design]].

The same measurement habit turns qualitative product discovery into a decision
system. If a team can't define the signal it will learn from, the roadmap bet
isn't ready
[[cite:ai-ml-product-design-and-experimentation@56:36=>AI Product Design]].

When the decision depends on whether the action caused the outcome, the team
should move from a product-experiment framing to
[[experimentation and causal inference]]. For choices between A/B tests,
observational causal methods, and discovery experiments, use that bridge instead
of this product portfolio.

## Choosing the Experiment Type

Experiment design starts with the decision. A team should know what it will do
if the experiment wins, loses, or returns an unclear result. Without that
decision, the team is only watching dashboards.

Use a randomized product test when the team can assign users, sessions,
accounts, or requests and log exposure at the same level. A simple two-group
test exposes platform bugs, instrumentation gaps, and stakeholder disagreement
before the team adds variants or complex analysis
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
The design details belong on [[a-b-testing=>A/B testing]].

Use an offline model experiment or shadow-mode check when the team needs to
compare model behavior before full exposure. Production teams still need live
validation because offline metrics can improve without improving the product
metric
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

For AI products, design can happen before a live test exists. Liesbeth
Dingemans' design sprint discussion uses a one-week prototype to test whether a
solution direction is worth more investment. It also brings data scientists into
problem definition so the team avoids building the wrong ML solution
[[cite:ai-ml-product-design-and-experimentation@23:16=>AI Product Design]].

## Decision Metrics

Metrics define what the experiment means. A team can randomize perfectly and
still learn the wrong thing if the primary metric doesn't match the decision.

A pricing or monetization change can look different depending on whether the
team measures immediate revenue or retention. Points usage, conversion, and
long-term value can tell different stories too. A useful experiment needs one
primary decision metric and supporting diagnostic metrics
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Product metrics and model metrics answer different questions because model work
can happen before live validation. Live decisions still need uplift by segment
and root-cause analysis
[[cite:production-ml-mlops-and-data-team-building=>Production ML]]. This connects
experimentation to [[evaluation]] and [[machine learning system design]] for
[[production]] systems.

Guardrail metrics keep the team from optimizing one number while damaging
another. Common guardrails include latency, crashes, complaints, and churn. Teams
may also track revenue cannibalization, fraud exposure, cost, and manual review
load. These guardrails turn experiments into rollout decisions rather than
isolated metric exercises
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

## Product Analytics Infrastructure

Product analytics supplies the instrumentation and interpretation layer for
experiments. The team needs event definitions, cohorts, funnels, and exposure
logs. It also needs metric calculations, dashboards, and readouts that
stakeholders can trust.

Experimentation depends on [[product analytics]] infrastructure. Third-party and
in-house experimentation platforms both need traffic splitting and stable
assignment. They also need exposure logging, monitoring, and debuggable metrics
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

The product analyst's work isn't only the final p-value. It also includes the
setup that makes the test credible. For that role split,
[[product-analyst-vs-data-analyst=>product analyst vs data analyst]] connects
experiment ownership to broader analyst responsibilities.

Product analytics also turns experiments into reusable knowledge. Feature
de-risking and learning matter even when the tested change doesn't ship. A
failed test can still reveal a bad assumption, a weak segment, or a metric that
doesn't behave as expected
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

That learning role makes experimentation part of
[[data-led-growth=>data-led growth]] and [[data product management]]. The same
product-facing responsibilities appear in the [[Data Product Manager]] article.

## Causal Evidence Boundaries

Product experiments often produce enough evidence for a rollout decision. They
don't automatically answer every causal question around a product. Marketing,
recommendation, and churn-treatment decisions may need a counterfactual
comparison with the same person under another action
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

[[experimentation and causal inference]] covers the choice between randomized
and observational causal evidence. Discovery experiments stay with product
learning. [[causal inference]] covers confounding and identification. It also
covers CATE, uplift modeling, and policy evaluation.

## Power, Duration, and Safety Checks

Power, duration, and guardrails decide whether an experiment can settle the
question. A test that's too short can turn noise into a product decision. A test
without guardrails can make a metric improve while the product gets worse.

Noise, stability, seasonality, and business cycles affect whether a product
experiment can settle the question. [[Power analysis]] connects sample size and
test duration. The team needs the baseline rate, expected effect size, variance,
and traffic before it promises a timeline
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

[[a-a-testing=>A/A testing]] is another guardrail because an identical-group
test validates randomization and measurement. If an A/A test finds a large
difference, the platform may be assigning traffic incorrectly or measuring
outcomes inconsistently
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

In ML systems, shadow mode is a related guardrail. Shadow mode and A/B tests
validate a model before full rollout. This lowers risk when model errors can
affect customers, revenue, fraud decisions, or operational load
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

For production-search and recommendation experiments, Sadat Anwar describes
using feature flags, backups, and monitoring. He combines them with controlled
experimentation. Teams can then try ML changes without betting the whole system
on one rollout
[[cite:from-software-engineering-to-leading-data-science-teams@21:58=>Software Engineer to Data Science Manager]].

## Related Pages

These pages cover the concepts that experiments depend on or feed into:

- [[a-b-testing=>A/B Testing]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Metrics]]
- [[Causal Inference]]
- [[Experimentation and Causal Inference]]
- [[Product Analytics]]
- [[Event Tracking]]
- [[Evaluation]]
- [[Production]]
- [[Machine Learning System Design]]
