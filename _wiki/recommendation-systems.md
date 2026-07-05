---
layout: wiki
title: "Recommendation Systems"
summary: "Recommendation systems as data, ranking, personalization, experimentation, and production operations work."
related:
  - Search
  - Machine Learning System Design
  - A/B Testing
  - Production Search Evaluation
  - Streaming
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
vocabulary, shares retrieval and ranking problems with
[[search]], and borrows measurement discipline from
[[production search evaluation]].

Modern recommenders also use
[[embeddings]] and
[[vector databases]] when a team
retrieves similar items before ranking them. Teams need
[[data pipelines]] so the model can
learn from behavior. They use
[[a-b-testing=>A/B testing]] and
[[product analytics]] to prove
that the ranked output helped. [[MLOps]]
covers the release and retraining path.

A recommender needs a data path and a ranking path. It also needs product
constraints, evaluation, and monitoring.
[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]].
[[cite:building-production-search-systems=>Building Search Systems]].
In healthcare, recommendations also become personalized interventions that need
experimentation and safety review.[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]]

## Ranked Product Decisions

A recommendation system turns behavioral data, item data, and context into a
ranked product decision. The output may be a movie, product, brand, or article.
In other domains, it may be an exercise, route, or next action. Teams need to
know what they can recommend and whom they recommend to. They also need to know
which signals must stay fresh and which outcome proves that the recommendation
helped.

In the data-platform view, user information, ratings, and search history feed
streaming and batch pipelines. Data scientists train the model after those
pipelines prepare the data.[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]
Streaming updates stay separate from historical batch data.

Flink and Spark can each play a part, while Parquet and S3 appear alongside
databases in this example. Production recommendation systems depend on
[[data pipelines]],
[[data engineering platforms]],
and [[batch-vs-streaming=>batch versus streaming]].

In the retrieval-and-ranking view, search systems split into candidate
generation and ranking. Recommendation systems use the same split.[[cite:building-production-search-systems=>Building Search Systems]]

The same ranking mindset extends beyond search and recommender systems.
It also appears when a system allocates attention or money in real time.
Teams need to ask whether the product goal and feedback signal make the ranking
useful [[cite:data-science-leadership-hiring-mlops@19:57=>Data Science Leadership and MLOps]]
[[cite:data-science-leadership-hiring-mlops@21:19=>Data Science Leadership and MLOps]].
Use [[algorithmic-trading=>algorithmic trading]] for the adjacent automated
bidding and decisioning structure when money allocation is the product action.

First, narrow the item universe to plausible candidates. Then score and reorder
the list through the same path that handles filters and serving.

Personalization shows why behavioral data, content, and user context usually
meet in the ranking step.[[cite:building-production-search-systems=>Building Search Systems]]

## System Boundaries and Product Intent

The definition changes less than the system
boundary. Some examples start from data movement, some from retrieval and
ranking, and some from the product outcome the recommendation should change.

The data engineering boundary puts events, historical storage, cleaned training
data, and deployment handoffs at the center. Data engineers, data scientists,
and machine learning engineers may own different parts of the same recommender
path.[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]

The ranking-architecture boundary treats recommender systems and personalized
search as neighboring problems. Both need a candidate set and a ranking step.
They also need contextual signals and business metrics.[[cite:building-production-search-systems=>Building Search Systems]]
That boundary ties recommender design to
[[Search]],
[[Embeddings]], and
[[Machine Learning System Design]].

The modern retrieval boundary uses vector databases for session-based
recommendations and contrasts that with collaborative filtering. These
recommendations update from clicks during the current session.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

The product-intent boundary changes the recommender design. A theme-park
system recommended the next best move for each group. The product goal was to
reduce waiting time and redistribute visitors. The system used queue
predictions, ride capacity, transaction signals, and route preferences rather
than only past item clicks.

That joined prediction with an operational [[data-products=>data product]] and
with [[data-product-adoption=>data product adoption]]. The app and survey had
to attract enough visitors before the model could learn useful routes
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@12:59=>Theme Park Crowd Modeling]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@14:55=>App Adoption]]).

The healthcare example recommends content, exercises, and behavior changes, but
the system has an explicit health agenda. It isn't only maximizing similarity to
past preferences.[[cite:ai-in-healthcare-and-digital-therapeutics@35:39=>AI in Healthcare and Digital Therapeutics]]

## Candidate Generation, Ranking, and Retrieval

Recommendation systems share much of their structure with
[[search=>production search]]. A team needs to find
plausible items quickly. It then ranks them using signals that match the product
decision. Candidate generation and ranking give the architecture its main
split.[[cite:building-production-search-systems=>Building Search Systems]]
Retrieval narrows the full inventory, while ranking brings in context and
machine learning.

That ranking layer can combine text, behavior, freshness, and popularity.
Business rules belong there too. A strict waterfall of constraints can
overconstrain results. A person may want a compromise among relevance, recency,
popularity, and "popular for people like me."[[cite:building-production-search-systems=>Building Search Systems]]
Custom embeddings and custom ranking models connect to the MLOps work that
follows.

The vector-database view adds the session-based version. Recommendations can
update per session based on clicks rather than being precomputed once per user.
Context becomes the important signal.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
Session context brings recommendation systems close to [[vector databases]],
[[production search evaluation]],
and [[information retrieval]].

## Data Pipelines and Feature Freshness

Recommendations depend on current and historical data at the same time. A
Netflix-style example uses streaming data for new ratings and behavior, plus
batch storage for history.[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]

That mix lets data scientists train on cleaned history while the product keeps
collecting new signals. It also forces teams to assign ownership. One team may
maintain the stream. Another may prepare training data or deploy the model.
Someone also has to write results back for the product and analysts.

The same freshness issue appears inside ranking, where embeddings for title,
content, and images belong alongside behavioral signals.[[cite:building-production-search-systems=>Building Search Systems]]

Timestamp encoding lets teams represent recency without recomputing everything
naively. Query-time weights help because the right balance can differ by page
type.[[cite:building-production-search-systems=>Building Search Systems]]

This is why recommender work belongs near
[[machine learning infrastructure]],
[[model monitoring]], and
[[data quality and observability]].
A stale event stream can break recommendations even when the model code didn't
change. Duplicate records, missing item metadata, and changed user behavior can
do the same.

## Personalization Modes

The examples describe several personalization modes rather than one
universal recommender design.

Collaborative filtering starts from user-item behavior, and Spotify and Netflix
examples show the basic idea. People similar to you liked content you haven't
seen yet.
[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]].
The same matrix-and-vectors idea contrasts with session-aware recommendations
that can react to the current click path.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Next-best-action systems add an operational goal. The Efteling example
recommended the next attraction for a group. It used queue predictions, ride
capacity, transaction signals, and route preferences.
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@13:36=>Theme Park Crowd Modeling]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@14:09=>Crowd Signals]].

The recommendation wasn't only "people like you liked this." It was a routing
decision meant to reduce waiting and improve the park experience. The team also
used app survey responses to model about 3,000 route variations. It then mapped
a group's stated preferences to likely attraction paths
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@16:40=>Route Modeling]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@17:50=>Route Recommendations]].

Agenda-driven [[machine-learning-personalization=>ML personalization]] adds a
normative goal. At Sidekick Health, the
recommender nudges people toward healthier behavior rather than only reinforcing
past preferences.[[cite:ai-in-healthcare-and-digital-therapeutics@35:39=>AI in Healthcare and Digital Therapeutics]]

The item catalog includes educational content, cards, and exercises. That makes
the recommendation problem closer to a treatment plan than a media feed.
[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]].
It links recommender design to [[data products]]
and [[data product management]].

## Evaluation and Experimentation

Bol.com tested likely favorite brands before the new product surface was
released. Abbaspour warns that the metric definition can bias recommender A/B
tests. Clicks and sales don't always prove that the recommendation matched user
preference. The employee swiping game provided a direct preference check first.
Employees marked brands as favorites or not.

The validation setup reached about 85 percent agreement before broader release
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@24:16=>Theme Park Crowd Modeling]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@28:19=>Employee Swiping]]
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@31:39=>Validation Result]].

That validation also depended on infrastructure. The team used on-the-fly
processing so only employees saw the internal swiping page. They avoided
precomputing recommendations for millions of users. Live experiments for
recommenders therefore connect evaluation to [[streaming]], targeting, and
application instrumentation
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering@26:01=>Streaming Validation]].

In the business-metric version, a team replaced a recommendation SaaS provider
with a word2vec-based internal model. The team then used A/B tests and saw a
2-3 percent transaction lift from recommendations.
[[cite:from-software-engineering-to-leading-data-science-teams=>From Software Engineering to Leading Data Science Teams]].

The project also included training, data gathering, production hosting, and a
retraining job. That project wasn't only a model comparison. At that point,
recommendation systems become
[[machine learning system design]]
problems rather than only modeling problems.

The staged-experimentation episode warns against starting with recommender
models. Teams shouldn't jump directly into collaborative filtering, and deep
learning has the same risk. They start with A/B tests and variant availability.
Segments and accumulated data come next.

That evidence can support clustering and collaborative filtering. Later machine
learning work still depends on analytics and good data.
[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]]

For lifecycle segmentation, [[rfm-analysis=>RFM analysis]] can be a simpler
analytics baseline before the team has enough evidence for recommendation
models.[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]

Search and recommender teams get more support when metrics connect to business
performance. Offline tests and A/B tests speed up iteration. Engineer-facing
metrics do the same.[[cite:building-production-search-systems=>Building Search Systems]]
Use
[[evaluation]],
[[metrics]],
[[experimentation and causal inference]],
and [[a-b-testing=>A/B testing]] for the surrounding
measurement discipline.

## Safety, Product Constraints, and Guardrails

Recommendation quality isn't only click-through rate because healthcare adds a
safety boundary. Hydration advice for heart-failure patients shows the risk.
A suggestion that helps most people may be unsafe for a specific medical group.
[[cite:ai-in-healthcare-and-digital-therapeutics=>AI in Healthcare and Digital Therapeutics]].
The team needs medical review before testing risky recommendations, even if the
product can test low-risk features quickly.

Product constraints are lower risk but still important because teams must
balance freshness, relevance, and popularity. Prototyping e-commerce
personalization with embeddings and product images is a practical starting
point.[[cite:building-production-search-systems=>Building Search Systems]]

Descriptions, behavior, and frequent queries can guide that prototype too. The
practical guardrail is to prove that the new results differ usefully from the
current production system before committing to a larger build.

These examples connect recommendation systems to
[[evaluation]], [[product analytics]],
and [[model monitoring]]. A good
recommender must optimize the intended outcome. It also has to avoid known
harms and stale suggestions. Impossible inventory, unsafe advice, and
misleading aggregate metrics need guardrails too.

## Operations, Monitoring, and Ownership

Recommendation systems become production systems when teams need repeatable
training and serving. They also need retraining, monitoring, and rollback.

The word2vec recommendation project included data engineering, data gathering,
production hosting on AWS, and a retraining job.[[cite:from-software-engineering-to-leading-data-science-teams=>From Software Engineering to Leading Data Science Teams]]

The same ownership question appears from the data engineering side. Depending on
the team, deployment may sit with machine learning engineers, data scientists,
or data engineers.[[cite:big-data-engineer-vs-data-scientist=>Big Data Engineer vs Data Scientist]]

In the MLOps platform view, monitoring and A/B testing were important next
standardization areas. Demand forecasting and recommendation engines fit into
standard monitoring tools. Personalization and loyalty programs appeared as
common retail problems across brands.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

In the product-ownership version, a METRO recommender uses API-first design and
scaling as the operating frame. The same discussion connects production ML
hiring to data scientists, machine learning engineers, and MLOps. The
recommender relies on collaborative filtering and Word2Vec variants.
[[cite:building-data-products-product-owner-vs-product-manager=>Building Data Products at Scale]].
That makes the recommender a [[data-products=>data product]] with an API, owners,
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
- [[a-b-testing=>A/B Testing]]
- [[Vector Databases]]
- [[Embeddings]]
- [[Data Pipelines]]
- [[Data Engineering Platforms]]
- [[MLOps]]
- [[Model Monitoring]]
- [[Evaluation]]
- [[Product Analytics]]
- [[Data Products]]
