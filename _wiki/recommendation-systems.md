---
layout: wiki
title: "Recommendation Systems"
summary: "How DataTalks.Club guests discuss recommendation systems as data, ranking, personalization, experimentation, and production operations work."
related:
  - Search
  - Machine Learning System Design
  - A/B Testing
  - Production Search Evaluation
  - Vector Databases
  - Embeddings
  - Data Pipelines
  - Data Engineering Platforms
  - MLOps
  - Model Monitoring
  - Evaluation
  - Product Analytics
  - Data Products
---

Recommendation systems choose what to show to a person in a product context.
The recommendation may be an item or content card. It may also be an action or
next step.

The topic uses [[machine learning system design]]
vocabulary. It shares retrieval and ranking problems with
[[search]]. It also borrows measurement
discipline from
[[production search evaluation]].

Modern recommenders also use
[[embeddings]] and
[[vector databases]] when a team
retrieves similar items before ranking them. Teams need
[[data pipelines]] so the model can
learn from behavior. They use
[[a-b-testing|A/B testing]] and
[[product analytics]] to prove
that the ranked output helped. [[MLOps]]
covers the release and retraining path.

A recommender is a system that needs data pipelines, candidate generation, and
ranking. It also needs product constraints, evaluation, and monitoring.

[[person:roksolanadiachuk|Roksolana Diachuk]] frames a Netflix-like
recommendation project as a streaming and batch data problem
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).
[[person:danielsvonava|Daniel Svonava]] connects recommenders to search
architecture and ranking, to vector retrieval, and to business metrics
([[podcast:building-production-search-systems|Building Search Systems]]).
In healthcare, recommendations become personalized interventions that need
experimentation and safety review
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

## Ranked Product Decisions

A recommendation system turns behavioral data, item data, and context into a
ranked product decision. The output may be a movie, product, brand, or article.
In other domains, it may be an exercise, route, or next action. Teams need to
know what they can recommend and whom they recommend to. They also need to know
which signals must stay fresh and which outcome proves that the recommendation
helped.

In the data-platform view, user information, ratings, and search history are
inputs to streaming and batch pipelines, and data scientists train the model
after those pipelines prepare the data
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).
Streaming updates stay separate from historical batch data.

Flink and Spark can each play a part, while Parquet and S3 appear alongside
databases in this example. Production recommendation systems depend on
[[data pipelines]],
[[data engineering platforms]],
and [[batch-vs-streaming|batch versus streaming]].

In the retrieval-and-ranking view, search systems split into candidate
generation and ranking, and that same split fits recommendations
([[podcast:building-production-search-systems|Building Search Systems]]).

First, narrow the item universe to plausible candidates. Then score and reorder
the list through the same path that handles filters and serving.

Personalization shows why behavioral data, content, and user context usually
meet in the ranking step
([[podcast:building-production-search-systems|Building Search Systems]]).

## System Boundaries and Product Intent

The guests differ less on the definition than on the boundary they start from.
Some start from data movement, some from retrieval and ranking, and some from
the product outcome the recommendation should change.

[[person:roksolanadiachuk|Roksolana Diachuk]] starts from the data engineering
boundary. This recommender example depends on events and historical storage,
plus cleaned training data. Deployment handoffs among data engineers, data
scientists, and machine learning engineers also matter
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).

[[person:danielsvonava|Daniel Svonava]] starts from ranking architecture,
treating recommender systems and personalized search as neighboring problems.
Both need candidate generation, ranking, contextual signals, and business
metrics
([[podcast:building-production-search-systems|Building Search Systems]]).
That view ties recommender design to
[[Search]],
[[Embeddings]], and
[[Machine Learning System Design]].

[[person:atitaarora|Atita Arora]] starts from modern retrieval infrastructure,
using vector databases for session-based recommendations and contrasting that
with collaborative filtering. These recommendations update from clicks during
the current session
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

[[person:abouzarabbaspour|Abouzar Abbaspour]] centers product intent in a
theme-park setting, and [[person:stefangudmundsson|Stefan Gudmundsson]] does the
same in healthcare. The theme-park system recommended the next best move for
each group, with the product goal of reducing waiting time and redistributing
visitors. It joined prediction with an operational
[[data-products|data product]]
([[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).

The healthcare example recommends content, exercises, and behavior changes, but
the system has an explicit health agenda. It isn't only maximizing similarity to
past preferences
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

## Candidate Generation, Ranking, and Retrieval

Recommendation systems share much of their structure with
[[search|production search]]. A team needs to find
plausible items quickly. It then ranks them using signals that match the product
decision. [[person:danielsvonava|Daniel Svonava]]'s candidate-generation and
ranking split is the clearest architecture anchor
([[podcast:building-production-search-systems|Building Search Systems]]).
Retrieval narrows the full inventory, while ranking brings in context and
machine learning.

That ranking layer can combine text, behavior, freshness, and popularity.
Business rules belong there too. A strict waterfall of constraints can
overconstrain results: the user may want a compromise among relevance, recency,
popularity, and "popular for people like me"
([[podcast:building-production-search-systems|Building Search Systems]]). Custom
embeddings and custom ranking models connect to the MLOps work that follows.

The vector-database view adds the session-based version: recommendations can
update per session based on clicks rather than being precomputed once per user,
with context as the important signal
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Session context brings recommendation systems close to [[vector databases]],
[[production search evaluation]],
and [[information retrieval]].

## Data Pipelines and Feature Freshness

Recommendations depend on current and historical data at the same time. A
Netflix-style example uses streaming data for new ratings and behavior and batch
storage for history
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).

That mix lets data scientists train on cleaned history while the product keeps
collecting new signals. It also forces teams to assign ownership. One team may
maintain the stream. Another may prepare training data or deploy the model.
Someone also has to write results back for the product and analysts.

The same freshness issue appears inside ranking, where embeddings for title,
content, and images belong alongside behavioral signals
([[podcast:building-production-search-systems|Building Search Systems]]).

Timestamp encoding lets teams represent recency without recomputing everything
naively, and query-time weights help because the right balance can differ by
page type
([[podcast:building-production-search-systems|Building Search Systems]]).

This is why recommender work belongs near
[[machine learning infrastructure]],
[[model monitoring]], and
[[data quality and observability]].
A stale event stream can break recommendations even when the model code didn't
change. Duplicate records, missing item metadata, and changed user behavior can
do the same.

## Personalization Modes

Guests describe several personalization modes rather than one universal
recommender design.

Collaborative filtering is the familiar user-item starting point, explained
through Spotify and Netflix: people similar to you liked content you haven't seen
yet
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).
The same matrix-and-vectors idea contrasts with session-aware recommendations
that can react to the current click path
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

Next-best-action systems add an operational goal.
[[person:abouzarabbaspour|Abouzar Abbaspour]]'s Efteling example recommended the
next attraction for a group using queue predictions, ride capacity, transaction
signals, and route preferences
([[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
The recommendation wasn't only "people like you liked this"; it was a routing
decision meant to reduce waiting and improve the park experience.

Agenda-driven personalization adds a normative goal. At Sidekick Health, the
recommender nudges people toward healthier behavior rather than only reinforcing
past preferences
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

The item catalog includes educational content, cards, and exercises, making the
recommendation problem closer to a treatment plan than a media feed
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).
It links recommender design to [[data products]]
and [[data product management]].

## Evaluation and Experimentation

Guests repeatedly treat evaluation as the hard part of recommendation systems
([[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
In the Bol.com favorite-brand project, likely favorite brands were tested before
releasing the new product surface, using an employee swiping game for that check,
which reached about 85 percent accuracy in that validation setup.

In the business-metric version, a team replaced a recommendation SaaS provider
with a word2vec-based internal model, then used A/B tests and saw a 2-3 percent
transaction lift from recommendations
([[podcast:from-software-engineering-to-leading-data-science-teams|From Software Engineering to Leading Data Science Teams]]).
The project also included training, data gathering, production hosting, and a
retraining job, so the result wasn't only a model comparison. At that point,
recommendation systems become
[[machine learning system design]]
problems rather than only modeling problems.

In the staged-experimentation version, teams should avoid jumping directly into
collaborative filtering or deep learning for recommenders. The approach starts
with A/B tests and variant availability, then uses segments and accumulated data
to move toward clustering or collaborative filtering, treating analytics and good
data as prerequisites for machine learning
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).

In the search-recommender metric discipline, teams get more support when
recommender or search metrics connect to business performance, and offline tests,
A/B tests, and engineer-facing metrics speed up iteration
([[podcast:building-production-search-systems|Building Search Systems]]). Use
[[evaluation]],
[[metrics]],
[[experimentation and causal inference]],
and [[a-b-testing|A/B testing]] for the surrounding
measurement discipline.

## Safety, Product Constraints, and Guardrails

Recommendation quality isn't only click-through rate; healthcare adds a safety
boundary. Hydration advice for heart-failure patients is an example: a suggestion
that helps most people may be unsafe for a specific medical group
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]]).
The team needs medical review before testing risky recommendations, even if the
product can test low-risk features quickly.

Product constraints are lower risk but still important: freshness, relevance, and
popularity are constraints that teams must balance, and prototyping e-commerce
personalization with embeddings and product images is a practical starting point
([[podcast:building-production-search-systems|Building Search Systems]]).

Descriptions, behavior and frequent queries can guide that prototype too. The
guardrail is practical: prove that the new results differ usefully
from the current production system before committing to a larger build.


These examples connect recommendation systems to
[[evaluation]], [[product analytics]],
and [[model monitoring]]. A good
recommender must optimize the intended outcome. It also has to avoid known
harms and stale suggestions. Impossible inventory, unsafe advice, and
misleading aggregate metrics need guardrails too.

## Operations, Monitoring, and Ownership

Recommendation systems become production systems when teams need repeatable
training and serving. They also need retraining, monitoring, and rollback.

[[person:sadatanwar|Sadat Anwar]]'s word2vec recommendation project included data
engineering, data gathering, production hosting on AWS, and a retraining job
([[podcast:from-software-engineering-to-leading-data-science-teams|From Software Engineering to Leading Data Science Teams]]).

The same ownership question appears from the data engineering side: deployment
may sit with machine learning engineers, data scientists, or data engineers
depending on the team
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist]]).

In the MLOps platform view, monitoring and A/B testing were important next
standardization areas, with demand forecasting and recommendation engines as use
cases that fit into standard monitoring tools, and personalization and loyalty
programs as common retail problems across brands
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

In the product-ownership version, a METRO recommender uses API-first design and
scaling as the operating frame, connects production ML hiring to data scientists,
machine learning engineers, and MLOps, and relies on collaborative filtering and
Word2Vec variants
([[podcast:building-data-products-product-owner-vs-product-manager|Building Data Products at Scale]]).
That makes the recommender a [[data-products|data product]] with an API, owners,
metrics, and production staffing.

Teams may start a recommender as a notebook or a small batch job. They may also
start with a search-ranking tweak. They turn it into shared infrastructure when
several product surfaces need the same events and features.

When teams need shared models and experiments, the recommender connects back to
[[MLOps]] and
[[machine learning infrastructure]].
It also connects to [[model registry]]
and [[model monitoring]].

## Related Pages

Use these pages for the surrounding architecture, evaluation, and operating
details.

- [[Search]]
- [[Production Search Evaluation]]
- [[Machine Learning System Design]]
- [[a-b-testing|A/B Testing]]
- [[Vector Databases]]
- [[Embeddings]]
- [[Data Pipelines]]
- [[Data Engineering Platforms]]
- [[MLOps]]
- [[Model Monitoring]]
- [[Evaluation]]
- [[Product Analytics]]
- [[Data Products]]
