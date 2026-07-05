---
layout: wiki
title: "Causal Inference"
summary: "How podcast guests explain causal inference as reasoning about interventions, counterfactuals, and treatment effects."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - Product Analytics
  - Evaluation
  - Metrics
  - Machine Learning
---

Causal inference is the reasoning discipline for estimating what would change
if a team intervened. It asks for the treatment and outcome first. It also asks
which population and counterfactual comparison turn a data signal into evidence
of cause. That makes it the concept page for causal structure and treatment
effects. It also covers confounding, identification, and treatment-aware machine
learning.

The applied product question lives in
[[experimentation and causal inference]], where teams choose evidence standards.
That applied frame covers A/B tests and discovery experiments. It also covers
marketing models and production rollout checks.

Causal inference keeps the underlying vocabulary and method boundaries,
including treatments and counterfactuals. It also covers identification,
confounding, and policy effects.

The methods become operating decisions in [[a-b-testing=>A/B testing]],
[[product analytics]], [[metrics]], and [[machine learning]].

[[person:aleksandermolak=>Aleksander Molak]] frames causal inference as the
difference between association and causation. [[person:jakobgraff=>Jakob Graff]]
shows why randomized assignment can identify a product effect. [[person:juanorduz=>Juan Orduz]]
applies causal thinking to marketing attribution and media mix modeling
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]],
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]],
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

## Causal Questions and Counterfactuals

Causal inference starts with an intervention question. A team may change a
product launch, marketing campaign, or pricing policy. It may also change a
recommender or churn treatment. The method asks what would have happened under a
different action. Ordinary [[machine learning]] prediction can miss that question
because the model output may change the behavior that creates the next data
point.

[[person:aleksandermolak=>Aleksander Molak]] starts from this difference in
the causal ML episode. He separates association from causation, then uses
prediction, marketing, and recommendation examples to show why a team often
needs a counterfactual answer. The team needs to know what would have happened
under another action
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

That counterfactual vocabulary is what connects causal inference to
[[experimentation and causal inference]] and [[product analytics]]. Product
teams still have to choose an evidence standard for the decision. Causal
reasoning checks whether the comparison isolates the effect of the
intervention.

## Treatment Effects and Comparisons

Molak, Graff, and Orduz use different settings, but each causal problem keeps
the same structure.

A causal inference problem needs these pieces:

- a treatment or change
- an outcome the team cares about
- a population or segment
- a comparison between treatment and no treatment
- a decision about rollout, targeting, budget, or product design

Molak makes this explicit in the causal ML episode. He connects
counterfactuals to Judea Pearl's intervention view and introduces conditional
average treatment effect, or CATE. CATE estimates how much the treatment
changes the outcome for a given person or segment. CATE makes causal inference
depend on [[metrics]]: the outcome has to match the product or business
decision
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

[[person:lorismarini=>Loris Marini]] gives the SaaS operating version. A lead
indicator is useful only when the team can explain why an event or condition is
likely to produce stickiness. The same explanation has to cover lower churn or
higher lifetime value. Teams then turn a [[metrics=>metric]] discussion into a
causal story about customer behavior
[[cite:data-professionals-business-skills-in-saas@15:46=>SaaS Business Skills]].

[[person:jakobgraff=>Jakob Graff]] gives the randomized version of the same
idea in the product experimentation episode. He explains A/B testing through the
clinical-trial setup. Teams randomly assign people. One group gets the change,
another stays as control, and the team compares outcomes.

The method is experimental, but the causal structure still names treatment and
control. It also names outcome and comparison
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).

## Identification and Confounding

Causal claims need an identification strategy. The team has to explain why the
observed comparison can stand in for the missing counterfactual. Randomization
is one strategy, and observational data needs other checks. Teams may use causal
feature selection, causal graphs, sensitivity analysis, or partial
identification.

Molak starts from causal structure. In the causal ML episode, he explains that
unconfoundedness can come from randomized treatment assignment or from careful
causal feature selection. He adds refutation tests and estimator checks because
standard validation doesn't prove that a causal structure is correct
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

Observational data creates the main risk because the data may mix the treatment
effect with confounders. Molak uses confounder examples to show how a
relationship can look predictive without being causal. He then explains why
teams need either randomized treatment data or a defensible way to choose causal
features. When the data can't identify one clean answer, he uses causal graphs
and minimal observables
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

## Randomization as an Identification Strategy

Teams use randomized experiments in causal inference because assignment can make
treatment independent of user characteristics. The team can then attribute a
measured difference to the intervention with fewer assumptions.

Graff's A/B testing episode covers assignment, tracking, metric choice, and
sample size. He also focuses on trust in the platform. He recommends
[[a-a-testing=>A/A tests]] to check whether the machinery can split traffic and
measure outcomes without inventing a difference
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).
Those operating questions belong in more detail on
[[experimentation and causal inference]] and [[a-b-testing=>A/B testing]].

## Treatment-Aware Machine Learning

Causal inference changes ML work when the model output triggers an action. A
churn model predicts who may leave, while an uplift model asks who stays because
the team intervenes. A recommender predicts engagement, while a causal
recommender asks what engagement changes because a specific item was shown.

Molak makes this targeting distinction in the causal ML episode. The team
should compare a causal policy with a baseline on the same business metric.
Revenue, churn, retention, and cost can each be the metric when they match the
decision. He also warns that causal models are worth the added complexity only
when they change a valuable decision. One example is reducing wasted marketing
spend
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

[[person:valeriybabushkin=>Valerii Babushkin]] connects
this to production ML validation in
the ML system design interview. He treats metrics, baselines, and A/B tests as
part of the end-to-end ML pipeline. He then discusses production validation
through A/B tests, causality, and human labels. This is where
[[evaluation]] and
[[machine learning system design]]
meet causal thinking [[cite:machine-learning-system-design-interview=>ML System Design Interviews]].

## Observational Measurement Settings

Marketing measurement often shows causal inference outside a clean product
experiment. In Orduz's episode, attribution becomes ambiguous because customers
see several channels before converting. Privacy changes and cookieless tracking
reduce user-level tracking quality. That pushes teams toward aggregate models,
stronger assumptions, and clearer communication with stakeholders
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

Orduz describes media mix modeling and time-series counterfactuals for
estimating campaign impact. He also connects uplift modeling with
treatment/control design and data pitfalls
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).
The applied choice between these methods, A/B tests, and discovery experiments
belongs on [[experimentation and causal inference]].

## Related Pages

These pages connect causal inference to adjacent product, ML, and analytics
work:

- [[Experimentation and Causal Inference]]
- [[Experimentation]]
- [[a-b-testing=>A/B Testing]]
- [[Product Analytics]]
- [[Evaluation]]
- [[Metrics]]
- [[Machine Learning]]
- [[Machine Learning System Design]]
- [[Data Product Manager]]
- [[Product Analyst]]
