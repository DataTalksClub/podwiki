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

Use [[causal inference]] for treatment and counterfactual vocabulary, including
confounding and identification. It also covers CATE and causal ML. For
standalone experimentation mechanics, use [[experimentation]] and
[[a-b-testing=>A/B testing]]. The combined frame asks which evidence standard fits
the product decision.

[[person:jakobgraff=>Jakob Graff]] explains the randomized product experiment
path through traffic splitting, metric choice, A/A checks, and power
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
[[person:aleksandermolak=>Aleksander Molak]] explains when teams need a
counterfactual intervention answer instead of ordinary prediction
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
[[person:liesbethdingemans=>Liesbeth Dingemans]] covers earlier design
experiments that reduce uncertainty before a team is ready for a causal estimate
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].

## Decision Frame for Product Teams

The shared frame is practical. Before choosing a method, the team defines the
action and metric. It also names the affected population. Then it names the comparison
and decision threshold. That turns [[metrics]] and [[product analytics]] into
decision evidence instead of a dashboard review.

Use an [[a-b-testing=>A/B test]] when the product can assign comparable users or
sessions and log exposure. Use [[causal inference]] when the decision is still an
intervention question but the team can't rely on clean randomized assignment.
Use design or discovery experiments when the team isn't yet sure what to build.
Graff, Molak, and Dingemans describe those as different points in the decision
path. They aren't interchangeable labels
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]],
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]],
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]).

## Matching Evidence to the Decision Stage

The podcast discussions draw different boundaries around useful evidence.
Product experimentation emphasizes live assignment, metric design, sample size,
and platform checks before rollout
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

## Randomized Experiments

Teams use randomized product experiments for the cleanest applied overlap. They
split traffic, expose treatment users or sessions to a change, keep a control
group, and compare a launch metric chosen in advance. Graff uses a
clinical-trial analogy to explain why randomization matters. It makes treatment
and control comparable enough to attribute a metric difference to the tested
change
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
Teams need stable assignment, exposure logging, monitoring, and debuggable
metrics.

Teams also need system checks before they trust randomized evidence.
[[a-a-testing=>A/A testing]] validates randomization, tracking, and metric
calculation before interpreting an A/B result. [[power analysis]] plans duration
from baseline rates, variance, traffic, and detectable effect
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

A randomized experiment still has to match the decision. In a
subscription-versus-points example, the result depends on which revenue or
retention metric the team chooses. Metric design also stays tied to timing,
business cycles, and sample size through noise and seasonality
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
Those details connect randomized experiments to [[metrics]]
and [[power analysis]], not only to
statistics.

## Missing Randomization

Some decisions still ask whether an intervention changed an outcome even when a
clean traffic split is unavailable. In the causal ML episode, Molak covers
confounders and unconfoundedness. He also covers causal feature selection,
partial identification, and sensitivity. Refutation tests and policy metrics
also matter
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

Those method details belong on [[causal inference]]. In an applied product frame,
they matter because the team still has to decide whether to launch or stop. The
team also has to decide whether to target or allocate.

Marketing is the clearest setting. Attribution gets ambiguous when customers see
several channels before conversion. Privacy and cookieless tracking push the
problem toward aggregate models, assumptions, and stakeholder communication
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Attribution and Marketing Mix Modeling]].
These constraints push marketing measurement beyond A/B tests and into
[[causal inference]].

Marketing measurement also connects to uplift, linking uplift modeling with
treatment/control thinking and data pitfalls
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
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]].
Those ideas fit beside
[[data product management]],
[[data products]], and
[[data product adoption]].

## Production ML Decisions

In production ML, an offline model metric may improve while the product metric
doesn't.

Teams stage validation through offline experiments, shadow mode, and A/B tests.
Uplift and segment analysis show why analysts look at cohorts and root causes
after a live model test. They don't stop at the top-line model score
[[cite:production-ml-mlops-and-data-team-building=>From Analytics to Production ML]].

The same concern links to ML system design. Metrics, baselines, and A/B tests
are part of the end-to-end ML pipeline. Production validation runs through A/B
tests, causality, and human labels
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
That connects the topic to
[[machine learning system design]],
[[MLOps]], and
[[model registry]] work.

## Choosing the Evidence Standard

Choose a randomized experiment when the product can assign comparable users or
sessions, log exposure, and wait long enough for the metric to stabilize. The
[[a-b-testing=>A/B testing]] path starts with a simple two-group design. The team
validates the system with [[a-a-testing=>A/A testing]] and plans sample size
before launch
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Use causal inference when the decision is about an intervention but the team
can't rely only on randomized evidence. That boundary is explicit through
confounding, unconfoundedness, and policy evaluation
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
The method is heavier than ordinary prediction, so it's most valuable when it
changes a rollout or targeting decision. Pricing and allocation decisions can
justify the same work.

Use discovery experiments when the team is still unsure what to build. Parallel
proofs of concept and a scoping document support the early product phase
[[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]. These
experiments produce evidence about problem fit, feasibility, and user signals
before the team reaches the stricter causal question.

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
