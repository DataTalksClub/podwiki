---
layout: wiki
title: "Causal Inference"
summary: "Causal inference as reasoning about interventions, counterfactuals, and treatment effects."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - Product Analytics
  - Evaluation
  - Metrics
  - Machine Learning
---

Causal inference estimates what would change if a team intervened. It starts
with a treatment, outcome, population, and counterfactual comparison. Then it
asks which assumptions let the observed data stand in for the outcome the team
can't observe.

The method vocabulary covers treatments, counterfactuals, identification, and
confounding. It also covers conditional average treatment effect, uplift, policy
effects, and treatment-aware machine learning. Use [[a-b-testing=>A/B testing]]
for randomized product-test design. Use [[experimentation]] for the broader
product and ML experiment portfolio, and use [[experimentation and causal
inference]] for the applied choice between experiments and causal methods.

The recurring contrast is association versus causation. Product experiments,
marketing models, recommendation systems, and churn treatments can all produce
strong predictive signals. Causal inference asks whether the action caused the
change
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]].

## Interventions and Counterfactuals

Causal inference starts with an intervention question. A team may change a
product launch, marketing campaign, or pricing policy. It may also change a
recommender or churn treatment. The method asks what would have happened under a
different action.
Ordinary [[machine learning]] prediction can miss that question because the model
output may change the behavior that creates the next data point.

Prediction, marketing, and recommendation examples show why a team often needs a
counterfactual answer, not only a correlation. The team needs to know what would
have happened under another action
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

That counterfactual vocabulary connects causal inference to
[[experimentation and causal inference]] and [[product analytics]]. Product teams
still have to choose an evidence standard for the decision. Causal reasoning
checks whether the comparison isolates the effect of the intervention.

## Treatment Effects and Comparisons

Product experiments and causal ML use different data, as does marketing
measurement. The team still names the treatment and outcome. It also names the
population, comparison, and decision.

A causal inference problem needs these pieces:

- a treatment or change
- an outcome the team cares about
- a population or segment
- a comparison between treatment and no treatment
- a decision about rollout, targeting, budget, or product design

Counterfactuals connect to Judea Pearl's intervention view and to conditional
average treatment effect, or CATE. CATE estimates how much the treatment changes
the outcome for a given person or segment. CATE makes causal inference depend on
[[metrics]] because the outcome has to match the product or business decision
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

A lead indicator is useful only when the team can explain why an event or
condition is likely to produce stickiness. The same explanation has to cover
lower churn or higher lifetime value. Teams then turn a [[metrics=>metric]]
discussion into a causal story about customer behavior
[[cite:data-professionals-business-skills-in-saas@15:46=>SaaS Business Skills]].

Product teams use randomized experiments with the same structure. One group gets the
change, another stays as control, and the team compares outcomes
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
The operating mechanics sit in [[a-b-testing=>A/B testing]]. The causal structure
names treatment, control, outcome, and comparison.

## Identification and Confounding

Causal claims need an identification strategy. The team has to explain why the
observed comparison can stand in for the missing counterfactual. Randomization
is one strategy, and observational data needs other checks. Teams may use causal
feature selection and causal graphs. They may also use sensitivity analysis,
refutation tests, or partial identification.

Unconfoundedness can come from randomized treatment assignment or from careful
causal feature selection. Refutation tests and estimator checks matter because
standard validation doesn't prove that a causal structure is correct
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

Observational data creates the main risk because the data may mix the treatment
effect with confounders. A relationship can look predictive without being
causal. Teams therefore need either randomized treatment data or a defensible way
to choose causal features. When the data can't identify one clean answer, causal
graphs and minimal observables help narrow the claim
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

## Randomization and Identification

Randomization can make treatment independent of user characteristics. The team
can then attribute a measured difference to the intervention with fewer
assumptions. A/B tests use that strategy when assignment, exposure logging, and
metric calculation are trustworthy
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

That trust is still an assumption about the experiment system. [[a-a-testing=>A/A
testing]] checks whether the machinery can split traffic and measure outcomes
without inventing a difference. The detailed operating questions belong on
[[a-b-testing=>A/B testing]] and [[power analysis]].

## Treatment-Aware Machine Learning

Causal inference changes ML work when the model output triggers an action. A
churn model predicts who may leave, while an uplift model asks who stays because
the team intervenes. A recommender predicts engagement, while a causal
recommender asks what engagement changes because a specific item was shown.

Treatment-aware targeting compares a causal policy with a baseline on the same
business metric. Revenue, churn, retention, and cost can each be the metric when
they match the decision. Causal models are worth the added complexity only when
they change a valuable decision, such as reducing wasted marketing spend
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].

Production ML validation links causal thinking with [[evaluation]] and
[[machine learning system design]]. Metrics, baselines, and A/B tests are part
of the end-to-end ML pipeline. Production validation can combine A/B tests,
causality, and human labels
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].

## Observational Measurement Settings

Marketing measurement often shows causal inference outside a clean product
experiment. Customers may see several channels before converting, so attribution
can become ambiguous. Privacy changes and cookieless tracking reduce user-level
tracking quality. That pushes teams toward aggregate models, stronger
assumptions, and clearer communication with stakeholders
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]].

Media mix modeling and time-series counterfactuals estimate campaign impact when
clean assignment is unavailable. Uplift modeling connects marketing decisions
back to treatment/control design and data pitfalls
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]].
[[Experimentation and causal inference]] covers the applied choice between these
methods, A/B tests, and discovery experiments.

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
