---
layout: wiki
title: "Causal Inference"
summary: "How podcast guests explain causal inference as the discipline for reasoning about interventions, counterfactuals, treatment effects, and policy decisions."
related:
  - Experimentation and Causal Inference
  - A/B Testing
  - Product Analytics
  - Evaluation
  - Metrics
  - Machine Learning
---

## Interventions and Counterfactuals

Causal inference estimates what would change if a team intervened. The
intervention can be a product launch, a marketing campaign, or a pricing
change. It can also be a recommender update, a churn treatment, or a policy
change. That makes causal inference different from ordinary
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) prediction:
the model result can change the behavior that creates the next data point.

In
[Causal Inference for Real-World ML](https://datatalks.club/podcast/causal-inference-for-machine-learning.html),
[Aleksander Molak](https://datatalks.club/people/aleksandermolak.html)
starts from this difference. Around 7:31, he separates association from
causation. Around 12:41 and 15:36, he uses prediction, marketing, and
recommendation examples to show why a team often needs a counterfactual answer.
The team needs to know what would have happened under another action.

Causal inference therefore sits next to
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}),
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}). Each
field has to separate a change caused by the team from the baseline that would
have happened anyway.

## Treatment Effects and Decision Support

Molak, Graff, and Orduz describe causal inference as decision support under
intervention. They use different vocabulary, but they keep returning to the
same structure.

A causal inference problem needs these pieces:

- a treatment or change
- an outcome the team cares about
- a population or segment
- a comparison between treatment and no treatment
- a decision about rollout, targeting, budget, or product design

Molak makes this explicit in the causal ML episode. Around 18:15, he connects
counterfactuals to Judea Pearl's intervention view. Around 24:24, he introduces
conditional average treatment effect, or CATE. CATE estimates how much the
treatment changes the outcome for a given person or segment. CATE makes
causal inference depend on [metrics]({{ '/wiki/metrics/' | relative_url }}):
the outcome has to match the product or business decision.

[Jakob Graff](https://datatalks.club/people/jakobgraff.html) gives the randomized
version of the same idea in
[Product Analytics and A/B Testing](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html).
Around 8:13, he explains A/B testing through the clinical-trial setup. Teams
randomly assign people, expose one group to the change, keep another as control,
and compare outcomes. Around 11:48, he frames the goal as causality in a noisy
product environment.

## Practice Boundaries

The guests mostly agree that causal inference should support a decision, but
they start from different operating constraints.

Molak starts from causal structure. Around 26:16 in the causal ML episode, he
explains that unconfoundedness can come from randomized treatment assignment or
from careful causal feature selection. Around 33:14, he adds refutation tests
and estimator checks because standard validation doesn't prove that a causal
structure is correct.

Graff starts from the experimentation system. In the A/B testing episode, he
focuses on assignment and tracking. He also focuses on metric choice, sample
size, and trust in the platform. Around 27:52, he recommends A/A tests to check
whether the machinery can split traffic and measure outcomes without inventing
a difference.

[Juan Orduz](https://datatalks.club/people/juanorduz.html) starts from marketing
measurement in
[Marketing Data Science](https://datatalks.club/podcast/machine-learning-in-marketing-attribution-marketing-mix-modeling.html).
Around 13:36 and 14:58, he describes media mix modeling and time-series
counterfactuals for estimating campaign impact. Around 29:13 and 30:54, he
connects uplift modeling with treatment/control design and data pitfalls.

[Liesbeth Dingemans](https://datatalks.club/people/liesbethdingemans.html) uses a
broader product-design lens in
[AI Product Design](https://datatalks.club/podcast/ai-ml-product-design-and-experimentation.html).
Around 16:02 and 23:16, she discusses parallel experiments, proofs of concept,
and design sprints. These aren't always causal estimates, but they reduce
uncertainty before a team invests in a full AI or ML product.

## Observational Data and Confounding

Observational data is useful when a randomized experiment is unavailable. It's
also useful when randomization would be expensive, unethical, or too slow. It
creates the main risk in causal inference because the data may mix the treatment
effect with confounders.

Molak illustrates the problem early in the causal ML episode. Around 8:55, he
uses confounder examples to show how a relationship can look predictive without
being causal. Around 26:16, he explains why teams need either randomized
treatment data or a defensible way to choose causal features. Around 59:33 and
1:04:03, he discusses partial identification and sensitivity. He also discusses
causal graphs and minimal observables for cases where the data can't identify
one clean answer.

Marketing measurement often lives in this observational setting. In Orduz's
episode, attribution becomes ambiguous because customers see several channels
before converting. Around 10:18, he describes multi-channel journeys. Around
20:49, he discusses privacy changes and cookieless tracking, which reduce the
quality of user-level tracking data. That pushes teams toward aggregate models,
stronger assumptions, and clearer communication with stakeholders.

## Randomized Product Experiments

Teams get cleaner causal evidence from randomized experimentation when the
product and ethics allow it. Randomization makes treatment independent of user
characteristics, so the
team can attribute a measured difference to the intervention with fewer
assumptions.

Graff's A/B testing episode gives the practical structure. Around 14:27, the
subscription-versus-points example shows that the primary metric changes the
meaning of the experiment. Around 33:23, he discusses noisy metrics and
stability. He also covers seasonality and business cycles.

Around 37:44, power analysis turns effect size and variance into a test
duration. It also uses the baseline rate and traffic.

These concerns connect causal inference to
[experimentation]({{ '/wiki/experimentation/' | relative_url }}) and
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}). A causal answer is
only useful if the experiment answers the decision the team actually faces. A
test with broken assignment or unclear triggering can still produce a p-value.
The same is true for a test with a proxy metric that nobody trusts, but it
won't settle the rollout decision.

## Treatment-Aware Machine Learning

Causal inference changes ML work when the model output triggers an action. A
churn model predicts who may leave, while an uplift model asks who stays because
the team intervenes. A recommender predicts engagement, while a causal
recommender asks what engagement changes because a specific item was shown.

Molak makes this targeting distinction around 27:52 and 32:40 in the causal ML
episode. The team should compare a causal policy with a baseline on the same
business metric. Revenue, churn, retention, and cost can each be the metric
when they match the decision. Around 38:54 and 41:14, he also warns that causal
models are worth the added complexity only when they change a valuable decision.
One example is reducing wasted marketing spend.

[Valerii Babushkin](https://datatalks.club/people/valeriybabushkin.html) connects
this to production ML validation in
[ML System Design Interviews](https://datatalks.club/podcast/machine-learning-system-design-interview.html).
Around 24:28, he treats metrics, baselines, and A/B tests as part of the
end-to-end ML pipeline. Around 57:23, he discusses production validation through
A/B tests, causality, and human labels. This is where
[evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
meet causal thinking.

## Product Decisions Under Uncertainty

Product teams use causal inference when they need to know whether a feature or
policy caused an outcome. Pricing changes, onboarding steps, and AI behaviors
raise the same question. Product teams also need
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) because
causal claims depend on event tracking and metric definitions. Teams also need
cohorts, guardrails, and stakeholder decisions.

Graff's episode shows the controlled product experiment path. Teams define the
decision, pick the metric, randomize, and validate the platform. Then they wait
long enough to learn.

Dingemans' product design episode covers the earlier product uncertainty.
Around 6:43 and 10:04, she discusses designing interfaces that collect useful
signals. Around 31:04, she uses scoping documents and "why" questions to
challenge assumptions before a team commits to a solution. Around 54:11 and
56:36, she connects experimentation culture with measurable product decisions.

For product managers and analysts, the practical question isn't whether a
method is labeled causal. The question is whether the evidence supports the
decision. Use randomized tests when possible. Use observational causal methods
when randomization is unavailable and the assumptions can be defended. Use
prototypes and discovery experiments when the team still needs to learn what to
build.

## Related Pages

These pages connect causal inference to adjacent product, ML, and analytics
work:

- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Data Product Manager]({{ '/wiki/data-product-manager/' | relative_url }})
- [Product Analyst]({{ '/wiki/product-analyst/' | relative_url }})
