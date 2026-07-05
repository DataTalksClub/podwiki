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

Causal inference is the part of analytics and machine learning that estimates
what would change if a team intervened. It connects to
[[experimentation and causal inference]], [[a-b-testing=>A/B testing]], and
[[product analytics]]. Causal claims also depend on [[metrics]] and
[[machine learning]] because the decision and the evidence have to match.

Causal inference is most useful when teams need a counterfactual answer.
Product, marketing, and ML teams may need to reason about a launch or campaign.
The same logic applies to recommendations, treatments, and policy changes.

[[person:aleksandermolak=>Aleksander Molak]] frames this as the difference
between association and causation. [[person:jakobgraff=>Jakob Graff]] grounds it
in randomized product experiments. [[person:juanorduz=>Juan Orduz]] applies it
to marketing attribution and media mix modeling
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]],
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]],
[[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

## Interventions and Counterfactuals

Causal inference estimates what would change if a team intervened. The
intervention can be a product launch, a marketing campaign, or a pricing
change. It can also be a recommender update, a churn treatment, or a policy
change. That makes causal inference different from ordinary
[[machine learning]] prediction:
the model result can change the behavior that creates the next data point.

[[person:aleksandermolak=>Aleksander Molak]] starts from this difference in
the causal ML episode. He separates association from causation, then uses
prediction, marketing, and recommendation examples to show why a team often
needs a counterfactual answer. The team needs to know what would have happened
under another action
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

Causal inference therefore sits next to
[[experimentation and causal inference]],
[[a-b-testing=>A/B testing]], and
[[product analytics]]. Each
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

[[person:jakobgraff=>Jakob Graff]] gives the randomized
version of the same idea in
the product experimentation episode. He explains A/B testing through the
clinical-trial setup. Teams randomly assign people, expose one group to the
change, keep another as control, and compare outcomes. He frames the goal as
causality in a noisy product environment
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).

## Practice Boundaries

Causal inference should support a decision, but the operating constraint changes
the practice.

Molak starts from causal structure. In the causal ML episode, he explains that
unconfoundedness can come from randomized treatment assignment or from careful
causal feature selection. He adds refutation tests and estimator checks because
standard validation doesn't prove that a causal structure is correct
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

Graff starts from the experimentation system. In the A/B testing episode, he
focuses on assignment and tracking. He also covers metric choice, sample size,
and trust in the platform. He recommends A/A tests to check whether the
machinery can split traffic and measure outcomes without inventing a difference
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).

[[person:juanorduz=>Juan Orduz]] starts from marketing
measurement in
the marketing data science episode. He describes media mix modeling and
time-series counterfactuals for estimating campaign impact, then connects
uplift modeling with treatment/control design and data pitfalls
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

[[person:liesbethdingemans=>Liesbeth Dingemans]] uses a
broader product-design lens in
the AI product design episode. She discusses parallel experiments, proofs of
concept, and design sprints. These aren't always causal estimates, but they
reduce uncertainty before a team invests in a full AI or ML product
([[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]).

## Observational Data and Confounding

Observational data is useful when a randomized experiment is unavailable. It's
also useful when randomization would be expensive, unethical, or too slow. It
creates the main risk in causal inference because the data may mix the treatment
effect with confounders.

Molak illustrates the problem early in the causal ML episode. He uses
confounder examples to show how a relationship can look predictive without
being causal. He then explains why teams need either randomized treatment data
or a defensible way to choose causal features. He also discusses partial
identification and sensitivity. For cases where the data can't identify one
clean answer, he uses causal graphs and minimal observables
([[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]]).

Marketing measurement often lives in this observational setting. In Orduz's
episode, attribution becomes ambiguous because customers see several channels
before converting. He describes multi-channel journeys and discusses privacy
changes and cookieless tracking, which reduce the quality of user-level
tracking data. That pushes teams toward aggregate models, stronger assumptions,
and clearer communication with stakeholders
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

## Randomized Product Experiments

Teams get cleaner causal evidence from randomized experimentation when the
product and ethics allow it. Randomization makes treatment independent of user
characteristics, so the
team can attribute a measured difference to the intervention with fewer
assumptions.

Graff's A/B testing episode gives the practical structure. The
subscription-versus-points example shows that the primary metric changes the
meaning of the experiment. He also discusses noisy metrics and stability, along
with seasonality and business cycles
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).

Power analysis turns effect size and variance into a test duration. It also
uses the baseline rate and traffic
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).

These concerns connect causal inference to
[[experimentation]] and
[[a-b-testing=>A/B testing]]. A causal answer is
only useful if the experiment answers the decision the team actually faces. A
test with broken assignment or unclear triggering can still produce a p-value.
The same is true for a test with a proxy metric that nobody trusts, but it
won't settle the rollout decision.

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

## Product Decisions Under Uncertainty

Product teams use causal inference when they need to know whether a feature or
policy caused an outcome. Pricing changes, onboarding steps, and AI behaviors
raise the same question. Product teams also need
[[product analytics]] because
causal claims depend on event tracking and metric definitions. Teams also need
cohorts, guardrails, and stakeholder decisions.

Graff's episode shows the controlled product experiment path. Teams define the
decision, pick the metric, randomize, and validate the platform. Then they wait
long enough to learn.

Dingemans' product design episode covers earlier product uncertainty through
interfaces that collect useful signals. She also uses scoping documents and
"why" questions to challenge assumptions before a team commits to a solution.
She connects experimentation culture with measurable product decisions. Teams
can then avoid treating the first AI or ML idea as the committed plan
([[cite:ai-ml-product-design-and-experimentation=>AI Product Design]]).

For product managers and analysts, the practical question isn't whether a
method is labeled causal. The question is whether the evidence supports the
decision. Use randomized tests when possible. Use observational causal methods
when randomization is unavailable and the assumptions can be defended. Use
prototypes and discovery experiments when the team still needs to learn what to
build.

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
