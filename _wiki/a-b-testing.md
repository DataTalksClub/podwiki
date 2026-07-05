---
layout: wiki
title: "A/B Testing"
summary: "A/B testing as randomized product evaluation, with assignment, metrics, noise, power, and rollout decisions."
related:
  - Experimentation and Causal Inference
  - Experimentation
  - A/A Testing
  - Metrics
  - Power Analysis
  - Event Tracking
  - Product Analytics
  - Data-Led Growth
  - Data Product Management
  - Evaluation
  - Production
  - Machine Learning System Design
  - Model Monitoring
  - Production Search Evaluation
  - Data Products
  - Search
  - Recommendation Systems
  - Streaming
  - Healthcare ML Validation and Adoption
  - Responsible AI and Governance
---

A/B testing is a randomized product experiment. A team assigns comparable users
or sessions to a control experience and one changed experience. It then compares
outcomes on metrics chosen before the test starts.

A/B testing bridges [[product analytics]], [[experimentation]], and
[[causal inference]]. The randomized test work covers assignment and exposure,
plus metric choice and sample-size planning. It also includes readout,
guardrails, and rollout decisions.

[[experimentation]] covers the broader product and ML experiment portfolio.
[[power analysis]] covers sample size and measurement sensitivity, and
[[causal inference]] covers assumptions outside clean randomization.

Teams also use A/B tests in [[machine learning system design]], [[data products]],
and [[production search evaluation]] when they need online evidence before
rollout. The clinical-trial analogy matters because randomization separates the
tested change from market noise, seasonality, and user differences
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

## Randomization and Assignment

A practical A/B test is narrower than "try two variants and look at a
dashboard." The test needs stable assignment and logged exposure. It needs a
control group, a treatment group, a primary metric, and an agreed decision rule.
That definition connects directly to [[a-a-testing=>A/A Testing]],
[[Power Analysis]], [[Metrics]], and [[Event Tracking]].

Traffic splitting only supports a causal readout when teams also track
assignment and monitor exposure. Without those controls, the team can't explain
why a metric moved. The cause could be the product change or incorrect
assignment
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

[[a-a-testing=>A/A testing]] is the trust check. If two identical groups show a
large difference, the measurement system needs attention before an A/B result is
credible
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

## Test Design and Rollout

Teams start design by choosing the unit of assignment. Account-level product
changes often use users, while short-lived experiences can use sessions. Some
production ML systems use traffic or requests. [[Event tracking]] is adjacent
because treatment exposure must be logged at the same level the analysis will
use.

A boring first experiment is useful: two groups expose assignment bugs and
tracking gaps. They also surface stakeholder disagreements before a complex
multi-arm test
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
A/B/C/D tests take longer and increase multiple-comparison risk, so extra
variants should earn their cost.

The tooling decision is secondary to the control logic because third-party and
in-house experimentation platforms differ. The important capabilities are
traffic splitting and stable assignment. Teams also need exposure logging,
monitoring, and debuggable metrics
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Teams with model-backed products often stage rollout. Offline model work and
shadow mode come before full rollout. A/B tests sit in the same release
sequence, with baselines and metrics included in the pipeline
[[cite:production-ml-mlops-and-data-team-building=>Production ML]]
[[cite:machine-learning-system-design-interview=>ML System Design]].

Live test sets and small 1%-2% A/B tests can detect model issues before they
become wider incidents. They're monitoring instruments as much as experiment
instruments, so the team needs feature logging and a response owner
[[cite:human-centered-mlops-and-model-monitoring@29:23=>Model Monitoring]].

Live data products can make assignment and exposure logging an engineering
problem, not only an analytics problem. An employee-swiping recommender
validation used on-the-fly processing so only employees saw the validation
experience. The team avoided processing millions of users and calculated the
recommendations just before the internal page loaded. That made [[streaming]],
targeting, and application instrumentation part of the experiment design
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@26:01=>Theme Park to Tesla]].

## Metrics and Decision Rules

A/B testing fails when the metric doesn't match the decision. A
subscription-versus-points example shows why the same product change can look
good or bad depending on the selected revenue metric. A test needs one primary
metric for the rollout decision and supporting metrics for diagnosis
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

The favorite-brand recommender used a staged decision rule. First, employees
swiped recommended brands as favorites while rejecting brands inserted as
non-favorite controls. The team treated roughly 85% favorite agreement as
evidence that the model was plausible. Only after that preference check did the
product goal move toward engagement with brand pages and broader rollout
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@31:39=>Theme Park to Tesla]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@33:02=>Brand Engagement]].

A/B tests need metrics that stay stable when noise or business cycles move the
result. They also need enough sample size and duration to detect the effect the
team would act on. [[Power analysis]] covers duration planning, while the A/B
readout still has to distinguish practical significance from statistical
significance.

Statistical significance is separate from product significance, and p-values can
be explained through an A/A comparison. A passing threshold is only part of the
decision. The team still needs to ask whether the estimated uplift is large
enough and worth the implementation cost
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Teams should separate the test result from the statistical procedure. Test
choice and distribution checks matter, as does the choice between frequentist
and Bayesian framing. The statistical method should fit the metric and the
decision, not only produce a familiar number
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].

Guardrail metrics keep A/B tests from improving one number while damaging the
product. In healthcare personalization, patient trust sits beside engagement,
and some interventions need clinical review before they enter an experiment
[[cite:ai-in-healthcare-and-digital-therapeutics@51:55=>Healthcare Personalization]].
In search, relevance work connects to clicks and contacts. It also connects to
orders and revenue
[[cite:building-production-search-systems=>Building Search Systems]]. In
production ML, analysts use segment analysis so they don't read only the
top-line average [[cite:production-ml-mlops-and-data-team-building=>Production ML]].

High-stakes experiments need a risk gate before speed. Low-risk healthcare app
changes can move quickly, but medical recommendations need domain review before
an A/B test starts. A water-intake recommendation can help many patients but
harm others, so safeguards and medical review belong next to the experiment
platform
[[cite:ai-in-healthcare-and-digital-therapeutics@51:55=>Healthcare Personalization]].
That connects A/B testing with [[healthcare ML validation and adoption]] and
[[responsible AI and governance]].

## Randomized Product Settings

As a product analytics discipline, A/B testing starts with two groups, clear
triggering, and a metric the team can explain. Teams should learn how their
product and users behave, not only whether one button color won
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
That operating discipline links to [[Product Analytics]],
[[data-led-growth=>Data-Led Growth]], and the [[Product Analyst]] guide.

A/B tests also apply to model-backed products when the team can randomize
exposure. Production ML teams can use A/B tests and shadow mode before full
rollout. After the test, they analyze uplift by segment and root cause instead
of stopping at the top-line model score
[[cite:production-ml-mlops-and-data-team-building=>Production ML]].

In higher-risk personalization, teams can segment users and iterate on variants
only when the product can measure variant exposure. They also need segment
outcomes through an experimentation platform
[[cite:ai-in-healthcare-and-digital-therapeutics@39:57=>Healthcare Personalization]]
[[cite:ai-in-healthcare-and-digital-therapeutics@43:00=>Experimentation Platform]].
Patient safety, [[privacy engineering for ML]], and [[responsible AI and
governance]] set the risk boundary before a test starts.

The favorite-brand team checked recommendations against controls before rollout
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@26:41=>Theme Park to Tesla]].
The theme-park team collected route preferences before recommending attractions
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@12:59=>Theme Park to Tesla]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@16:40=>Route Modeling]].

Search changes connect online tests to business KPIs such as orders, clicks,
revenue events, and contact events. Search teams should treat A/B testing as one
part of evaluation, not a replacement for relevance diagnostics
[[cite:building-production-search-systems=>Building Search Systems]].

## Causal Boundaries

A/B testing is powerful because random assignment blocks many confounding paths,
but it's not the whole field of [[causal inference]]. Experiments can be too
slow, too expensive, unethical, or impossible when the product can't withhold a
treatment from a control group. They can also answer only the question the team
actually randomized, not every causal question around the product.

The decision question is often what would have happened to the same user under a
different action. A/B testing gets closest to that question when the test is
randomized, logged, and analyzed on the right unit
[[cite:causal-inference-for-machine-learning=>Causal Inference for Real-World ML]].
[[causal inference]] covers confounding, unconfoundedness, uplift modeling, and
policy evaluation. [[experimentation and causal inference]] covers the choice
between a randomized test, an observational causal method, or a discovery
experiment.

## Related Pages


- [[Experimentation]]
- [[a-a-testing=>A/A Testing]]
- [[Power Analysis]]
- [[Metrics]]
- [[Event Tracking]]
- [[Causal Inference]]
- [[Product Analytics]]
- [[data-led-growth=>Data-Led Growth]]
- [[Data Product Management]]
- [[Evaluation]]
- [[Production]]
- [[Data Products]]
- [[Model Monitoring]]
- [[Production Search Evaluation]]
- [[Search]]
- [[Product Analyst]]
- [[Data Product Manager Roadmap]]
- [[Machine Learning System Design]]
