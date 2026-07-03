---
layout: wiki
title: "Experimentation"
summary: "How DataTalks.Club guests use experiments to reduce product, ML, and organizational uncertainty before rollout."
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

Experimentation is the practice of testing a change before a team commits to a
larger rollout. DataTalks.Club guests describe teams using it for product
features and pricing mechanics. They also discuss recommendation models, AI
interfaces, fraud models, and data product workflows.

The topic is broader than
[[a-b-testing=>A/B testing]]. A randomized
experiment is the cleanest version, but guests also discuss
[[a-a-testing=>A/A testing]], shadow mode, and
offline model experiments. Design sprints, proofs of concept, lightweight
surveys, and button tests appear in the same podcast discussions. The shared
goal is to learn before the team spends too much engineering, product, or
organizational capital.

[[person:jakobgraff=>Jakob Graff]] gives the
clearest product analytics framing: experiments establish causality and support
feature de-risking under noisy product conditions
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
A test doesn't only approve or reject a change. It teaches the team which
behavior moved and which assumptions were wrong.

## Decision Evidence

Guests treat experimentation as a structured way to turn an uncertain decision
into evidence. That evidence can be statistical or behavioral. It can also be
technical or organizational. In each case, it has to connect to a decision the
team can act on.

In product analytics, this usually means a control group and a treatment group.
It also means logged exposure and one agreed metric. Jakob explains the
randomized version through a clinical-trial analogy
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
Product teams need
[[metrics]],
[[event tracking]], and
[[product analytics]] to run
randomized experiments well.

In ML and AI product work, the same idea widens.
[[person:rishabhbhargava=>Rishabh Bhargava]] describes model development as
experimental before deployment and validation as experimental after deployment
[[cite:production-ml-mlops-and-data-team-building|From Analytics to Production ML]].
Teams may compare features and hyperparameters in offline model experiments.
Then they can use shadow mode or
[[a-b-testing=>A/B tests]] before they expose a new
model to all traffic.

[[person:liesbethdingemans=>Liesbeth Dingemans]] uses an
earlier product-design meaning
[[cite:ai-ml-product-design-and-experimentation|AI Product Design]].
Parallel experiments and proofs of concept help teams remove weak solution
paths before an AI roadmap becomes expensive. Her discussion of Double Diamond
problem framing keeps experiments connected to the problem, not only to the
proposed model or feature.

## Product, ML, and Discovery Questions

The guests agree that experiments reduce uncertainty, but they point the method
at different kinds of uncertainty.

[[person:jakobgraff=>Jakob Graff]] starts from product
causality. His concern is whether the product change caused the observed metric
movement. He spends time on traffic splitting and assignment tracking, then
covers [[a-a-testing|A/A tests]]
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
Metric stability and [[power analysis]] matter because a broken measurement
system creates false confidence.

[[person:rishabhbhargava=>Rishabh Bhargava]] starts from
the boundary between analytics and
[[production=>production ML]]. He describes uplift, segmentation, and
root-cause analysis after a live model test
[[cite:production-ml-mlops-and-data-team-building|From Analytics to Production ML]].
The experiment doesn't end when the top-line result appears. Analysts still
need to explain which segments changed and why.

[[person:liesbethdingemans=>Liesbeth Dingemans]] starts
from product discovery. Scoping documents and repeated "why" questions
challenge a proposed solution before the team builds it. Experimentation culture
connects that work to measurable prioritization
[[cite:ai-ml-product-design-and-experimentation|AI Product Design]]. This is
experimentation as product learning, not only statistical testing.

[[person:aleksandermolak=>Aleksander Molak]] starts from
[[causal inference]]. He treats A/B tests as one route to unconfounded evidence.
He then discusses cases where teams can't run clean experiments and need partial
identification, sensitivity checks, or causal graphs
[[cite:causal-inference-for-machine-learning|Causal Inference for Real-World ML]].

## Assignment and Exposure Design

Experiment design starts with the decision. A team should know what it will do
if the experiment wins, loses, or returns an unclear result. Without that
decision, experimentation becomes dashboard watching.

For randomized product tests, the team must define the unit of assignment.
Teams often assign by user or session. Some systems assign by account, device,
market, or request. The team must log exposure and analyze outcomes at that
same unit.

[[person:jakobgraff=>Jakob Graff]] discusses traffic
splitters to show why this matters
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
If assignment and exposure are unclear, the team can't tell whether the
treatment caused the outcome.

Simple first tests are safer than clever first tests. Jakob recommends a
two-group design because it exposes platform bugs, instrumentation gaps, and
stakeholder disagreement. Multi-arm tests add cost, and A/B/C/D tests take
longer and raise multiple-comparison risk
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].

For AI products, design can happen before a live test exists. Liesbeth's
design sprint discussion uses a one-week prototype to test whether a solution
direction is worth more investment. She also argues for involving data
scientists in problem definition so the team avoids building the wrong ML
solution
[[cite:ai-ml-product-design-and-experimentation|AI Product Design]].

## Decision Metrics

Metrics define what the experiment means. A team can randomize perfectly and
still learn the wrong thing if the primary metric doesn't match the decision.

[[person:jakobgraff=>Jakob Graff]] uses a
subscription-versus-points example to show this directly
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
A pricing or monetization change can look different
depending on whether the team measures immediate revenue or retention. Points
usage, conversion, and long-term value can tell different stories too. A useful
experiment needs one primary decision metric and supporting diagnostic metrics.

Guests separate product metrics from model metrics. Rishabh's ML example uses
offline model work before live validation, but the live decision still needs
business context. He connects model experiment analysis to uplift, segments, and
root causes
[[cite:production-ml-mlops-and-data-team-building|From Analytics to Production ML]].
This puts experimentation close to
[[evaluation]],
[[machine learning system design]],
and [[production]].

Guardrail metrics keep the team from optimizing one number while damaging
another. Common guardrails include latency, crashes, complaints, and churn.
Teams may also track revenue cannibalization, fraud exposure, cost, and manual
review load. These guardrails turn experiments into rollout decisions rather
than isolated metric exercises.

## Product Analytics Infrastructure

Product analytics supplies the instrumentation and interpretation layer for
experiments. The team needs event definitions, cohorts, funnels, and exposure
logs. It also needs metric calculations, dashboards, and readouts that
stakeholders can trust.

[[person:jakobgraff=>Jakob Graff]] ties experimentation
to [[product analytics]]
throughout
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
He compares third-party and in-house experimentation platforms. The important
capabilities are traffic splitting, stable assignment, and exposure logging.
Teams also need monitoring and debuggable metrics.

The product analyst's work isn't only the final p-value. It also includes the
setup that makes the test credible.

Product analytics also turns experiments into reusable knowledge. Jakob frames
tests as feature de-risking and learning
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
A failed test can still help a product team if it reveals a bad assumption. It
can also surface a weak segment or a metric that doesn't behave as expected.

That learning role makes experimentation part of
[[data-led-growth=>data-led growth]] and
[[data product management]].
The same product-facing responsibilities appear in the
[[Data Product Manager]] article.

## Randomization and Causal Boundaries

[[Experimentation and Causal Inference]]
overlap, but they aren't identical. Teams use randomized experiments to
estimate causal effects, while [[causal inference]]
covers cases where randomization is impossible or unethical. It also covers
cases where randomization is incomplete or too expensive.

[[person:aleksandermolak=>Aleksander Molak]] separates association from
causation. He then uses marketing and recommender systems to show why prediction
alone may not answer the decision
[[cite:causal-inference-for-machine-learning|Causal Inference for Real-World ML]].
The team often needs a counterfactual comparison with the same user under
another action.

He introduces conditional average treatment effect, or CATE. CATE extends
experimentation from average treatment effects to user-level or segment-level
treatment effects. He also connects uplift modeling, policy evaluation, and
business metrics. Teams need that distinction when they should target only users
who are likely to change behavior
[[cite:causal-inference-for-machine-learning|Causal Inference for Real-World ML]].
The action may be a campaign, recommendation, discount, or intervention.

The practical boundary is evidence quality. Use a randomized experiment when
the product, ethics, and traffic allow it. Use observational causal methods
when the team can defend the assumptions. Use discovery experiments when the
team still needs to learn what to build.

## Power, Duration, and Safety Checks

Power, duration, and guardrails decide whether an experiment can settle the
question. A test that's too short can turn noise into a product decision. A
test without guardrails can make a metric improve while the product gets worse.

[[person:jakobgraff=>Jakob Graff]] discusses noise,
stability, seasonality, and business cycles in
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
He connects sample size and test duration to [[power analysis]]. The team needs
the baseline rate and expected effect size before it promises a timeline. It also
needs variance and traffic.

[[a-a-testing=>A/A testing]] is another guardrail.
Jakob's identical-group example validates randomization and measurement
[[cite:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
If an A/A test finds a large difference, the platform may be assigning traffic
incorrectly or measuring outcomes inconsistently.

In ML systems, shadow mode is a related guardrail.
[[person:rishabhbhargava=>Rishabh Bhargava]] uses shadow
mode and A/B tests as ways to validate a model before full rollout in
[[cite:production-ml-mlops-and-data-team-building|From Analytics to Production ML]].
This lowers risk when model errors can affect customers, revenue, fraud
decisions, or operational load.

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
