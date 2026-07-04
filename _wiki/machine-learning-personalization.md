---
layout: wiki
title: "ML Personalization"
summary: "How personalization uses ranking, user context, analytics, privacy, healthcare safeguards, evaluation, and monitoring in ML systems."
related:
  - Recommendation Systems
  - Product Analytics
  - Data-Led Growth
  - A/B Testing
  - Production Search Evaluation
  - Model Monitoring
  - Privacy Engineering for ML
  - Healthcare ML Validation and Adoption
  - Data Products
---

ML personalization adapts rankings and recommendations to a person's context
and the product's constraints. It can also adapt product messages or clinical
nudges. It sits between [[recommendation systems]], [[product analytics]],
[[a-b-testing=>A/B testing]], and [[model monitoring]].

Personalization isn't only a model choice. Teams need reliable user events and
a clear product decision. They also need safety and privacy constraints, plus
evaluation that shows the personalized experience helped.

Data pipelines and dashboards matter too. Experiment capabilities, privacy
safeguards, and medical-risk review determine whether personalization is ready
for users.[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]]

## Personalization Decisions

ML personalization is a ranked or selected product decision for a user or
session context. It can also operate at the account or patient level. It may use
collaborative filtering or embeddings. It may also use clustering, rules, or
learned ranking.
Simple segmentation may be enough when the product has too little data for a
heavier model.

Candidate generation is separate from ranking. That same search structure also
appears in personalization requirements.[[cite:building-production-search-systems=>Building Search Systems]]

Recommender systems often narrow possible items first. They then rank them with
context, freshness, popularity, and business constraints.

Recommendations based on the current session contrast with collaborative
filtering. Session-aware personalization can react to the current click path.
Collaborative filtering relies more on accumulated user-item signals.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
That distinction matters for privacy and cold-start behavior: a session-based
system can use immediate intent. Collaborative filtering depends on enough
historical behavior to compare users or items.

## Domain Boundaries

Personalization changes meaning by domain. In ecommerce or search, teams may
optimize relevance and conversion. They may also optimize contact rate or
revenue. Ranking needs filters and recency. It also needs popularity and
product constraints, not only vector similarity.[[cite:building-production-search-systems=>Building Search Systems]]

Healthcare personalization uses a stricter boundary. Digital therapeutics nudge
people toward healthier behavior, not just more engagement. Agenda-driven
recommender systems choose interventions from the patient's program goals and
context. They then use segmentation and A/B testing to learn which variants help
([[cite:ai-in-healthcare-and-digital-therapeutics@35:39=>Digital Therapeutics Personalization]]
[[cite:ai-in-healthcare-and-digital-therapeutics@39:57=>A/B Testing Foundation]]).
Some recommendations can be unsafe for specific medical groups, so
personalization has to stay linked to [[healthcare ML validation and adoption]].

This healthcare boundary sits close to
[[Healthcare ML Validation and Adoption]].
The model has to fit the clinical workflow and risk level. It also has to fit
patient context and the review path. A personalized exercise, reminder, or
intervention can be a recommendation system, but it also needs medical review
when the suggestion can affect care.

Behavioral design changes the objective too: Stefan Gudmundsson describes a
low-in-app-time strategy. The product succeeds when people build habits in daily
life, not when they spend more time inside the app
([[cite:ai-in-healthcare-and-digital-therapeutics@15:04=>Low In-App Time Strategy]]).
Reward design follows that health objective. Charity incentives may fit better
than leaderboards when the product wants motivation without unhealthy
competition
([[cite:ai-in-healthcare-and-digital-therapeutics@25:43=>Charity Incentives vs Leaderboards]]).

## User Context and Activation

Personalization needs usable context before it needs advanced modeling. Teams
need tracking plans, event properties, source context, and a clear client-side
or server-side collection choice. Without them, a team can't trust an
activation metric or user segment.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

Data activation and reverse ETL let product event data flow to support, sales,
marketing, and engagement tools. Activation events also tie into personalized
onboarding in product-led growth.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]
A recommendation model may not be necessary yet. A reliable activation event can
already change the next email, support response, or product prompt.

This is why ML personalization belongs near
[[data-led-growth=>data-led growth]],
[[event tracking]], and
[[data activation]]. A model trained
on ambiguous events can personalize the wrong behavior with more confidence.

## Ranking, Embeddings, and Retrieval

Recommendation and personalization systems often share infrastructure with
search. Embeddings, vector databases, and hybrid search sit alongside custom
ranking models and query-time weights.[[cite:building-production-search-systems=>Building Search Systems]]
Multiple embeddings can cover titles and content. They can also cover images
and behavioral signals. Late-binding query weights matter when the same item
catalog serves different product contexts.[[cite:building-production-search-systems=>Building Search Systems]]

A related production-search path covers hybrid search and behavior signals.[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]
It also covers popularity and context-specific weighting. Business KPIs also
affect ecommerce personalization.
Use it with [[production search evaluation]]
when the personalization problem looks like ranking a catalog rather than
choosing a standalone prediction.

[[Vector databases]] can help
retrieve candidates, images, sessions, or similar products. They don't replace
ranking, filtering, evaluation, or product constraints. Vector retrieval belongs
beside session context and re-ranking.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Evaluation and Experimentation

Personalization needs both offline and online evidence. Offline tests help a
team compare candidate retrieval and ranking features. They can also compare
embeddings, segments, and fallbacks. Online experiments show whether the
personalized experience changed the product outcome under real traffic.

Experiments need traffic splitting and assignment tracking.[[cite:ab-testing-and-product-experimentation=>A/B Testing]]
Teams also monitor metric stability and seasonality.
Those checks matter for personalization because a top-line uplift can hide
assignment bugs, segment-level harm, or noisy metrics.

KPIs and success criteria come before build work.[[cite:building-data-products-lead-data-scientist=>Data Products at Scale]]
Pilots and A/B tests decide whether the work keeps moving.
Personalization therefore works as a [[data-products=>data product]] with
users, metrics, and owners.

## Privacy and Safety

Personalization often pushes teams to collect more user history than they need.
Personalization based on session context can retain less history.
Privacy-enhancing technologies and differential privacy extend the toolkit. The
practical starting point is deciding what data the product needs and what risk
the team is accepting.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Engineering, GDPR, and Machine Learning]]

In healthcare, GDPR and HIPAA sit alongside de-identification and empathy. App
experiments aren't medical recommendations.[[cite:ai-in-healthcare-and-digital-therapeutics=>Digital Therapeutics]]
In high-impact domains, teams should define the guardrail path before they build
a larger model.

## Monitoring and Ownership

Personalization can drift when user behavior or item catalogs change. Event
definition changes can cause drift too. A ranking weight can also stop matching
the product goal. Monitoring therefore needs product signals and model signals.

It should watch input distributions and prediction distributions. It should also
watch ranking distributions, service health, business outcomes, and user
feedback where the product allows it.

A human-centered monitoring approach combines live test sets and small A/B
tests.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]
It also uses user feedback and bug reports.
That matters for personalization because the worst failures may first appear as
complaints, support tickets, or unexplained segment drops.

A lighter operational example uses monitoring with Evidently. Dashboards and
alerts make the checks visible.[[cite:building-data-products-lead-data-scientist=>Building Data Products at Scale]]
These systems need the same ownership rule as other production ML systems. The
platform can provide monitoring tools, but a product owner or model owner must
decide what a bad alert means for users.

## Analytics Before Models

Teams need a reliable measurement base before complex ML.
Data pipelines, dashboards, and experimentation capabilities come before
advanced recommender models
([[cite:ai-in-healthcare-and-digital-therapeutics@27:02=>Analytics Foundation]]).
Variant availability comes first too
([[cite:ai-in-healthcare-and-digital-therapeutics@43:00=>Experimentation Platform]]).
That sequence starts with A/B tests and segmentation, then moves toward
clustering or collaborative filtering when the team has enough data and
confidence.

A well-defined activation event can personalize onboarding without a model.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

Intake criteria route the work.[[cite:building-data-products-lead-data-scientist=>Data Products]]
A Definition of Done clarifies whether it's analytics, data science, or
production ML.

Use simpler analytics when the team mostly needs trustworthy events, segments,
dashboards, or reverse ETL. Move toward ML personalization when the product has
many possible actions or items. The team also needs enough behavior to learn
from, a measurable decision, privacy controls, and ownership for evaluation and
monitoring.

## Related Pages

These pages cover the adjacent architecture, analytics, privacy, and operations
work:

- [[Recommendation Systems]]
- [[Product Analytics]]
- [[data-led-growth=>Data-Led Growth]]
- [[a-b-testing=>A/B Testing]]
- [[Production Search Evaluation]]
- [[Privacy Engineering for ML]]
- [[Healthcare ML Validation and Adoption]]
- [[Model Monitoring]]
