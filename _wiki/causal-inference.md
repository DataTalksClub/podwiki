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
effects, and treatment-aware machine learning. [[a-b-testing=>A/B testing]]
covers randomized product-test design. [[experimentation]] covers the broader
product and ML experiment portfolio, and [[experimentation and causal
inference]] covers the applied choice between experiments and causal methods.

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

In randomized experiments, teams use the same causal structure by defining the
treatment, control, and outcome for a population and comparison. For product-test
mechanics, use [[a-b-testing=>A/B testing]].

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

Randomization is one identification strategy. It can make treatment independent
of user characteristics, but it still relies on trustworthy assignment, exposure
logging, and metric calculation
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
The detailed operating checks belong on [[a-b-testing=>A/B testing]],
[[a-a-testing=>A/A testing]], and [[power analysis]].

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

Production ML validation can combine A/B tests, causal reasoning, and human
labels. Causal inference adds value when the model output changes a future
action or policy
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].

## Observational Measurement Settings

Marketing measurement often shows causal inference outside a clean product
experiment. Customers may see several channels before converting, so attribution
can become ambiguous. Privacy changes and cookieless tracking reduce user-level
tracking quality. That pushes teams toward aggregate models, stronger
assumptions, and clearer communication with stakeholders
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]].
Readers coming from marketing analytics can use
[[marketing-to-analytics-engineering=>Marketer to Analytics Engineer]]
when campaign reporting starts to require modeled attribution, BI-ready metrics,
and experiment-aware caveats.

Media mix modeling and time-series counterfactuals estimate campaign impact when
clean assignment is unavailable. Uplift modeling connects marketing decisions
back to treatment/control design and data pitfalls
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]].
[[Experimentation and causal inference]] covers the applied choice between these
methods, A/B tests, and discovery experiments.

## Related Pages

Experiments, power analysis, marketing measurement, and analytics engineering
set the nearby decision context.

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
