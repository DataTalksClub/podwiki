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
changed an outcome. [Jakob Graff]({{ '/people/jakobgraff/' | relative_url }})
explains the randomized version in
[Product Analytics and A/B Testing at 8:13]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
He describes splitting comparable users or sessions, exposing one group to a
change, keeping another as control, and comparing the metric chosen before
launch. The broader causal version comes through
[Aleksander Molak]({{ '/people/aleksandermolak/' | relative_url }}) in
[Causal Inference for Real-World ML at 7:31]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}).
He separates association from causation, then asks what would have happened
under a different intervention.

Teams use [experimentation]({{ '/wiki/experimentation/' | relative_url }}) when
they can test a live change or product direction. That test can be an
[A/B test]({{ '/wiki/a-b-testing/' | relative_url }}), an A/A check, or a
prototype. Teams use
[causal inference]({{ '/wiki/causal-inference/' | relative_url }}) when they
need to name the intervention, outcome, population, and counterfactual
comparison. Both practices turn a
[metric]({{ '/wiki/metrics/' | relative_url }}) into evidence for rolling out a
feature, targeting a campaign, changing a recommender, or validating a model
policy.

## Intervention Questions

Experiments and observational causal inference both ask whether a treatment
changes an outcome for a defined population. In a randomized experiment, the
team creates the comparison through assignment. In observational causal
inference, the team estimates the counterfactual from existing data or from
settings where it didn't control assignment.

Jakob's A/B testing episode grounds the experimental side. At
[11:48]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he describes experiments as a way to establish causality in noisy product
conditions. At
[24:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he moves from the idea to traffic splitting, assignment tracking, and monitoring.
At [27:52]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he uses [A/A testing]({{ '/wiki/a-a-testing/' | relative_url }}) to check whether
the system can split traffic and measure outcomes before an A/B result is
trusted.

Aleksander's causal inference episode grounds the causal side. At
[15:36]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he uses marketing and recommendation examples to show why prediction alone may
not answer an intervention question. At
[24:24]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he introduces conditional average treatment effect, or CATE, for estimating how
the effect changes by person or segment. CATE puts causal inference close to
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) when a team
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
[clinical-trial analogy at 8:13]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
shows why randomization matters. It makes the treatment group and control group
comparable enough to attribute a metric difference to the tested change. His
[traffic-splitting discussion at 24:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
adds the operational requirements. Teams need stable assignment, exposure
logging, monitoring, and debuggable metrics.

Teams also need system checks before they trust randomized evidence. In
[Product Analytics and A/B Testing at 27:52]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
Jakob uses [A/A testing]({{ '/wiki/a-a-testing/' | relative_url }}) to validate
randomization, tracking, and metric calculation before interpreting an A/B
result. At
[37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
he uses [power analysis]({{ '/wiki/power-analysis/' | relative_url }}) to plan
duration. The plan uses baseline rates, variance, traffic, and detectable
effect.

A randomized experiment still has to match the decision. In Jakob's
[subscription-versus-points example at 14:27]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
the result depends on which revenue or retention metric the team chooses. His
[noise and seasonality discussion at 33:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})
keeps metric design tied to timing, business cycles, and sample size. Those
details connect randomized experiments to [metrics]({{ '/wiki/metrics/' | relative_url }})
and [power analysis]({{ '/wiki/power-analysis/' | relative_url }}), not only to
statistics.

## Observational Causal Inference

Observational causal inference enters when the team can't run a clean
experiment. Aleksander's
[confounder discussion at 8:55]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }})
shows why a predictive relationship can mislead a decision. At
[26:16]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he explains that unconfoundedness can come from randomization or from careful
causal feature selection. At
[59:33]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }})
and
[1:04:03]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
he discusses partial identification and sensitivity when the available data
can't identify one clean answer.

Teams need different checks for observational causal work than for ordinary
predictive modeling. At
[33:14]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
Aleksander adds refutation tests and policy metrics because a causal model must
survive questions about hidden assumptions, not only predict held-out labels.

[Juan Orduz]({{ '/people/juanorduz/' | relative_url }}) gives the clearest
marketing setting. His
[multi-channel journey discussion at 10:18]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }})
shows why attribution gets ambiguous when customers see several channels before
conversion. His
[privacy and cookieless tracking discussion at 20:49]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }})
pushes the problem toward aggregate models, assumptions, and stakeholder
communication. These constraints push marketing measurement beyond A/B tests and
into [causal inference]({{ '/wiki/causal-inference/' | relative_url }}).

Juan also connects marketing measurement to uplift. At
[30:54]({{ '/podcasts/machine-learning-in-marketing-attribution-marketing-mix-modeling/' | relative_url }}),
he links uplift modeling with treatment/control thinking and data pitfalls. In
that setting, the team still asks a treatment question. The evidence comes from
attribution models, media mix models, time-series counterfactuals, or
observational treatment/control data instead of a clean traffic split.

## Product and Design Experiments

Not every useful experiment is a causal estimate.
[Liesbeth Dingemans]({{ '/people/liesbethdingemans/' | relative_url }}) uses
parallel experiments and proofs of concept in
[AI Product Design at 16:02]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }}).
Teams can remove weak solution paths before they invest in an AI product. Her
[Double Diamond discussion at 12:12]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
separates problem framing from solution exploration. Her
[design sprint discussion at 23:16]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
uses prototypes to test whether a direction deserves investment.

These activities don't replace A/B tests. They reduce product uncertainty
before a team has enough traffic, instrumentation, or user trust for a
randomized rollout.

For data and AI products, a technically valid model can still solve the wrong
problem. Liesbeth's
[data scientist involvement point at 28:18]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
connects product discovery to ML feasibility. Her
[scoping-document discussion at 31:04]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
uses repeated "why" questions to challenge a proposed solution before the team
turns it into an experiment or build plan. Her
[experimentation culture discussion at 54:11]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
connects prioritization to measurable learning. Those ideas fit beside
[data product management]({{ '/wiki/data-product-management/' | relative_url }}),
[data products]({{ '/wiki/data-products/' | relative_url }}), and
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).

## Production ML Decisions

In production ML, an offline model metric may improve while the product metric
doesn't.

[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) discusses
staged validation at
[28:42 in From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}).
He names offline experiments, shadow mode, and A/B tests. His
[uplift and segment-analysis discussion at 31:19]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }})
shows why analysts look at cohorts and root causes after a live model test.
They don't stop at the top-line model score.

[Valeriy Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) links the
same concern to ML system design. In
[ML System Design Interviews at 24:28]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he treats metrics, baselines, and A/B tests as part of the end-to-end ML
pipeline. At
[57:23]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he discusses production validation through A/B tests, causality, and human
labels. His production-validation discussion connects the topic to
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[model registry]({{ '/wiki/model-registry/' | relative_url }}) work.

## Choosing the Evidence Standard

Choose a randomized experiment when the product can assign comparable users or
sessions and log exposure. The team also needs enough time for the metric to
stabilize. This is Jakob's path through
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}). Start with a simple
two-group design at
[30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
validate the system with [A/A testing]({{ '/wiki/a-a-testing/' | relative_url }})
at [27:52]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
and plan sample size before launch at
[37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).

Use causal inference when the decision is about an intervention but the team
can't rely only on randomized evidence. Aleksander's causal ML episode makes
that boundary explicit through confounding at
[8:55]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
unconfoundedness at
[26:16]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}),
and policy evaluation at
[32:40]({{ '/podcasts/causal-inference-for-machine-learning/' | relative_url }}).
The method is heavier than ordinary prediction, so these episodes frame it as
most valuable when it changes a rollout or targeting decision. Pricing and
allocation decisions can justify the same work.

Use discovery experiments when the team is still unsure what to build. Liesbeth's
[parallel proof-of-concept discussion at 16:02]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
and
[scoping-document discussion at 31:04]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})
support the early product phase. These experiments produce evidence about
problem fit, feasibility, and user signals before the team reaches the stricter
causal question.

## Related Pages

The adjacent topics are:

- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [Causal Inference]({{ '/wiki/causal-inference/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }})
- [Power Analysis]({{ '/wiki/power-analysis/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Data Product Manager]({{ '/wiki/data-product-manager/' | relative_url }})
- [Product Analyst]({{ '/wiki/product-analyst/' | relative_url }})
