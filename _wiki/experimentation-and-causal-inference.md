---
layout: wiki
title: "Experimentation and Causal Inference"
summary: "How DataTalks.Club podcast guests connect randomized experiments, causal reasoning, metric design, uplift modeling, and product decisions."
related:
  - Experimentation
  - Causal Inference
  - A/B Testing
  - Metrics
  - Product Analytics
  - Evaluation
---

Experimentation and causal inference both help teams decide whether an action
changed an outcome. [[person:jakobgraff|Jakob Graff]]
explains the randomized version in
[[podcast:ab-testing-and-product-experimentation|8:13|Product Analytics and A/B Testing]].
He describes splitting comparable users or sessions, exposing one group to a
change, keeping another as control, and comparing the metric chosen before
launch. The broader causal version comes through
[[person:aleksandermolak|Aleksander Molak]] in
[[podcast:causal-inference-for-machine-learning|7:31|Causal Inference for Real-World ML]].
He separates association from causation, then asks what would have happened
under a different intervention.

Teams use [[experimentation]] when
they can test a live change or product direction. That test can be an
[[a-b-testing|A/B test]], an A/A check, or a
prototype. Teams use
[[causal inference]] when they
need to name the intervention, outcome, population, and counterfactual
comparison. Both practices turn a
[[metrics|metric]] into evidence for rolling out a
feature, targeting a campaign, changing a recommender, or validating a model
policy.

## Intervention Questions

Experiments and observational causal inference both ask whether a treatment
changes an outcome for a defined population. In a randomized experiment, the
team creates the comparison through assignment. In observational causal
inference, the team estimates the counterfactual from existing data or from
settings where it didn't control assignment.

Jakob's A/B testing episode grounds the experimental side. At
[[podcast:ab-testing-and-product-experimentation|11:48]],
he describes experiments as a way to establish causality in noisy product
conditions. At
[[podcast:ab-testing-and-product-experimentation|24:44]],
he moves from the idea to traffic splitting, assignment tracking, and monitoring.
At [[podcast:ab-testing-and-product-experimentation|27:52]],
he uses [[a-a-testing|A/A testing]] to check whether
the system can split traffic and measure outcomes before an A/B result is
trusted.

Aleksander's causal inference episode grounds the causal side. At
[[podcast:causal-inference-for-machine-learning|15:36]],
he uses marketing and recommendation examples to show why prediction alone may
not answer an intervention question. At
[[podcast:causal-inference-for-machine-learning|24:24]],
he introduces conditional average treatment effect, or CATE, for estimating how
the effect changes by person or segment. CATE puts causal inference close to
[[product analytics]] when a team
decides who should receive a discount, message, recommendation, or churn
intervention.

Both paths require the same practical definitions:

- define the intervention or treatment
- define the outcome metric
- define the population and assignment unit
- define the comparison group or counterfactual
- decide what action the evidence will support

## Randomized Experiments

Jakob's clearest example of experimentation and causal inference working
together is the randomized experiment. His
[[podcast:ab-testing-and-product-experimentation|8:13|clinical-trial analogy]]
shows why randomization matters. It makes the treatment group and control group
comparable enough to attribute a metric difference to the tested change. His
[[podcast:ab-testing-and-product-experimentation|24:44|traffic-splitting discussion]]
adds the operational requirements. Teams need stable assignment, exposure
logging, monitoring, and debuggable metrics.

Teams also need system checks before they trust randomized evidence. In
[[podcast:ab-testing-and-product-experimentation|27:52|Product Analytics and A/B Testing]],
Jakob uses [[a-a-testing|A/A testing]] to validate
randomization, tracking, and metric calculation before interpreting an A/B
result. At
[[podcast:ab-testing-and-product-experimentation|37:44]],
he uses [[power analysis]] to plan
duration. The plan uses baseline rates, variance, traffic, and detectable
effect.

A randomized experiment still has to match the decision. In Jakob's
[[podcast:ab-testing-and-product-experimentation|14:27|subscription-versus-points example]],
the result depends on which revenue or retention metric the team chooses. His
[[podcast:ab-testing-and-product-experimentation|33:23|noise and seasonality discussion]]
keeps metric design tied to timing, business cycles, and sample size. Those
details connect randomized experiments to [[metrics]]
and [[power analysis]], not only to
statistics.

## Observational Causal Inference

Observational causal inference enters when the team can't run a clean
experiment. Aleksander's
[[podcast:causal-inference-for-machine-learning|8:55|confounder discussion]]
shows why a predictive relationship can mislead a decision. At
[[podcast:causal-inference-for-machine-learning|26:16]],
he explains that unconfoundedness can come from randomization or from careful
causal feature selection. At
[[podcast:causal-inference-for-machine-learning|59:33]]
and
[[podcast:causal-inference-for-machine-learning|1:04:03]],
he discusses partial identification and sensitivity when the available data
can't identify one clean answer.

Teams need different checks for observational causal work than for ordinary
predictive modeling. At
[[podcast:causal-inference-for-machine-learning|33:14]],
Aleksander adds refutation tests and policy metrics because a causal model must
survive questions about hidden assumptions, not only predict held-out labels.

[[person:juanorduz|Juan Orduz]] gives the clearest
marketing setting. His
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|10:18|multi-channel journey discussion]]
shows why attribution gets ambiguous when customers see several channels before
conversion. His
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|20:49|privacy and cookieless tracking discussion]]
pushes the problem toward aggregate models, assumptions, and stakeholder
communication. These constraints push marketing measurement beyond A/B tests and
into [[causal inference]].

Juan also connects marketing measurement to uplift. At
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|30:54]],
he links uplift modeling with treatment/control thinking and data pitfalls. In
that setting, the team still asks a treatment question. The evidence comes from
attribution models, media mix models, time-series counterfactuals, or
observational treatment/control data instead of a clean traffic split.

## Product and Design Experiments

Not every useful experiment is a causal estimate.
[[person:liesbethdingemans|Liesbeth Dingemans]] uses
parallel experiments and proofs of concept in
[[podcast:ai-ml-product-design-and-experimentation|16:02|AI Product Design]].
Teams can remove weak solution paths before they invest in an AI product. Her
[[podcast:ai-ml-product-design-and-experimentation|12:12|Double Diamond discussion]]
separates problem framing from solution exploration. Her
[[podcast:ai-ml-product-design-and-experimentation|23:16|design sprint discussion]]
uses prototypes to test whether a direction deserves investment.

These activities don't replace A/B tests. They reduce product uncertainty
before a team has enough traffic, instrumentation, or user trust for a
randomized rollout.

For data and AI products, a technically valid model can still solve the wrong
problem. Liesbeth's
[[podcast:ai-ml-product-design-and-experimentation|28:18|data scientist involvement point]]
connects product discovery to ML feasibility. Her
[[podcast:ai-ml-product-design-and-experimentation|31:04|scoping-document discussion]]
uses repeated "why" questions to challenge a proposed solution before the team
turns it into an experiment or build plan. Her
[[podcast:ai-ml-product-design-and-experimentation|54:11|experimentation culture discussion]]
connects prioritization to measurable learning. Those ideas fit beside
[[data product management]],
[[data products]], and
[[data product adoption]].

## Production ML Decisions

In production ML, an offline model metric may improve while the product metric
doesn't.

[[person:rishabhbhargava|Rishabh Bhargava]] discusses
staged validation at
[[podcast:production-ml-mlops-and-data-team-building|28:42 in From Analytics to Production ML]].
He names offline experiments, shadow mode, and A/B tests. His
[[podcast:production-ml-mlops-and-data-team-building|31:19|uplift and segment-analysis discussion]]
shows why analysts look at cohorts and root causes after a live model test.
They don't stop at the top-line model score.

[[person:valeriybabushkin|Valeriy Babushkin]] links the
same concern to ML system design. In
[[podcast:machine-learning-system-design-interview|24:28|ML System Design Interviews]],
he treats metrics, baselines, and A/B tests as part of the end-to-end ML
pipeline. At
[[podcast:machine-learning-system-design-interview|57:23]],
he discusses production validation through A/B tests, causality, and human
labels. His production-validation discussion connects the topic to
[[machine learning system design]],
[[MLOps]], and
[[model registry]] work.

## Choosing the Evidence Standard

Choose a randomized experiment when the product can assign comparable users or
sessions and log exposure. The team also needs enough time for the metric to
stabilize. This is Jakob's path through
[[a-b-testing|A/B testing]]. Start with a simple
two-group design at
[[podcast:ab-testing-and-product-experimentation|30:05]],
validate the system with [[a-a-testing|A/A testing]]
at [[podcast:ab-testing-and-product-experimentation|27:52]],
and plan sample size before launch at
[[podcast:ab-testing-and-product-experimentation|37:44]].

Use causal inference when the decision is about an intervention but the team
can't rely only on randomized evidence. Aleksander's causal ML episode makes
that boundary explicit through confounding at
[[podcast:causal-inference-for-machine-learning|8:55]],
unconfoundedness at
[[podcast:causal-inference-for-machine-learning|26:16]],
and policy evaluation at
[[podcast:causal-inference-for-machine-learning|32:40]].
The method is heavier than ordinary prediction, so these episodes frame it as
most valuable when it changes a rollout or targeting decision. Pricing and
allocation decisions can justify the same work.

Use discovery experiments when the team is still unsure what to build. Liesbeth's
[[podcast:ai-ml-product-design-and-experimentation|16:02|parallel proof-of-concept discussion]]
and
[[podcast:ai-ml-product-design-and-experimentation|31:04|scoping-document discussion]]
support the early product phase. These experiments produce evidence about
problem fit, feasibility, and user signals before the team reaches the stricter
causal question.

## Related Pages

The adjacent topics are:

- [[Experimentation]]
- [[Causal Inference]]
- [[a-b-testing|A/B Testing]]
- [[a-a-testing|A/A Testing]]
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
