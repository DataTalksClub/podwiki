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
nudges. Across DataTalks.Club discussions, it connects
[[recommendation systems]] and [[product analytics]]. It also depends on
[[a-b-testing=>A/B testing]] and [[model monitoring]].

Personalization isn't only a model choice. Teams need reliable user events and
a clear product decision. They also need safety and privacy constraints, plus
evaluation that shows the personalized experience helped.

Data pipelines and dashboards matter too. Experiment capabilities, privacy
safeguards, and medical-risk review determine whether personalization is ready
for users
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

## Working Definition

ML personalization is a ranked or selected product decision for a user or
session context. It can also operate at the account or patient level. It may use
collaborative filtering or embeddings. It may also use clustering, rules, or
learned ranking.
Simple segmentation may be enough when the product has too little data for a
heavier model.

Candidate generation is separate from ranking. That same search structure also
appears in personalization requirements
([[podcast:building-production-search-systems|Building Search Systems]]).

That split is useful for recommender systems because a team first narrows
possible items. It then ranks them with context, freshness, popularity, and
business constraints.

Recommendations based on the current session contrast with collaborative
filtering. Session-aware personalization can react to the current click path.
Collaborative filtering relies more on accumulated user-item signals
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

## Product and Healthcare Boundaries

Personalization changes meaning by domain. In ecommerce or search, the system
may optimize relevance and conversion. It may also optimize contact rate or
revenue. Ranking needs filters and recency, and it needs popularity and
product constraints, not only vector similarity
([[podcast:building-production-search-systems|Building Search Systems]]).

Healthcare personalization needs a stricter boundary because Sidekick Health
works in digital therapeutics with an agenda. The system nudges people toward
healthier behavior, not just toward more engagement. Agenda-driven recommender
systems combine segmentation and A/B testing with safeguards. Some
recommendations could be unsafe for specific medical groups
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

That healthcare boundary sits close to
[[Healthcare ML Validation and Adoption]].
The model has to fit the clinical workflow and risk level. It also has to fit
patient context and the review path. A personalized exercise, reminder, or
intervention can be a recommendation system, but it also needs medical review
when the suggestion can affect care.

## User Context and Activation

Personalization needs usable context before it needs advanced modeling. Teams
need tracking plans, event properties, source context, and a clear client-side
or server-side collection choice. Without them, a team can't trust an
activation metric or user segment
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).

Data activation and reverse ETL let product event data flow to support, sales,
marketing, and engagement tools. Activation events also tie into personalized
onboarding in product-led growth
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).
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
ranking models and query-time weights
([[podcast:building-production-search-systems|Building Search Systems]]).
Multiple embeddings can cover titles and content. They can also cover images
and behavioral signals. Late-binding query weights matter when the same item
catalog serves different product contexts
([[podcast:building-production-search-systems|Building Search Systems]]).

A related production-search path covers hybrid search and behavior signals. It
also covers popularity, context-specific weighting, ecommerce personalization,
and business KPIs ([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
Use it with [[production search evaluation]]
when the personalization problem looks like ranking a catalog rather than
choosing a standalone prediction.

[[Vector databases]] can help
retrieve candidates, images, sessions, or similar products. They don't replace
ranking, filtering, evaluation, or product constraints. Vector retrieval belongs
beside session context and re-ranking
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

## Evaluation and Experimentation

Personalization needs both offline and online evidence. Offline tests help a
team compare candidate retrieval and ranking features. They can also compare
embeddings, segments, and fallbacks. Online experiments show whether the
personalized experience changed the product outcome under real traffic.

Experiment discipline covers traffic splitting, assignment tracking, and
monitoring, along with metric stability and seasonality
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]]).
Those checks matter for personalization because a top-line uplift can hide
assignment bugs, segment-level harm, or noisy metrics.

In the data product operating model, KPIs, success criteria, and fail-fast
checks come before build work. Pilots, A/B tests, and production rollout then
decide whether a model or analytics product should keep moving
([[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]]).
That makes personalization a [[data-products|data product]]
with users, metrics, and owners.

## Privacy and Safety

Personalization often pushes teams to collect more user history than they need.
Personalization based on session context can retain less history.
Privacy-enhancing technologies and differential privacy extend the toolkit. The
practical starting point is deciding what data the product needs and what risk
the team is accepting
([[podcast:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]]).

In healthcare, GDPR and HIPAA sit alongside de-identification and empathy. Safe
app experimentation is separate from recommendations that require medical
review
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).
In high-impact domains, teams should define the guardrail path before they build
a larger model.

## Monitoring and Ownership

Personalization can drift when user behavior or item catalogs change. Event
definition changes can cause drift too. A ranking weight can also stop matching
the product goal. Monitoring therefore needs product signals and model signals.

It should watch input distributions and prediction distributions. It should also
watch ranking distributions, service health, business outcomes, and user
feedback where the product allows it.

A human-centered monitoring approach combines live test sets and small A/B tests
with user feedback and internal bug reports
([[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring]]).
That matters for personalization because the worst failures may first appear as
complaints, support tickets, or unexplained segment drops.

A lighter operational example uses monitoring with Evidently, dashboards, and
alerts ([[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]]).
These systems need the same ownership rule as other production ML systems. The
platform can provide monitoring tools, but a product owner or model owner must
decide what a bad alert means for users.

## Analytics Before Models

Several discussions warn against starting with complex ML before the product
has a reliable measurement base. Data pipelines and dashboards come before
advanced recommender models, and experimentation capabilities and variant
availability come first
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).
That sequence starts with A/B tests and segmentation, then moves toward
clustering or collaborative filtering when the team has enough data and
confidence.

Product analytics makes the same point. If a team can personalize onboarding
from a well-defined activation event, it may not need a model yet
([[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]]).
The intake and Definition of Done should decide whether the work is analytics,
data science, or production ML
([[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]]).

Use simpler analytics when the team mostly needs trustworthy events, segments,
dashboards, or reverse ETL. Move toward ML personalization when the product has
many possible actions or items. The team also needs enough behavior to learn
from, a measurable decision, privacy controls, and ownership for evaluation and
monitoring.

## Neighboring Pages

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
