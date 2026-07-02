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

In DataTalks.Club discussions, the topic uses
[[machine learning system design]]
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

Guests treat a recommender as a system that needs data pipelines, candidate
generation, and ranking. It also needs product constraints, evaluation, and
monitoring.

[[person:roksolanadiachuk|Roksolana
Diachuk]] walks through a
Netflix-like recommendation project as a streaming and batch data problem in
[[podcast:big-data-engineer-vs-data-scientist|18:54|Big Data Engineer vs Data Scientist]].
[[person:danielsvonava|Daniel Svonava]] connects
recommenders to search architecture and ranking in
[[podcast:building-production-search-systems|12:45|Building Search Systems]].
He also connects them to vectors at
[[podcast:building-production-search-systems|21:55]]
and business metrics at
[[podcast:building-production-search-systems|1:01:25]].
[[person:stefangudmundsson|Stefan Gudmundsson]] adds
the healthcare version, where recommendations are personalized interventions
that need experimentation and safety review
([[podcast:ai-in-healthcare-and-digital-therapeutics|35:39|AI in Healthcare and Digital Therapeutics]]).

## Ranked Product Decisions

A recommendation system turns behavioral data, item data, and context into a
ranked product decision. The output may be a movie, product, brand, or article.
In other domains, it may be an exercise, route, or next action. Teams need to
know what they can recommend and whom they recommend to. They also need to know
which signals must stay fresh and which outcome proves that the recommendation
helped.

Roksolana gives the data-platform definition. In
[[podcast:big-data-engineer-vs-data-scientist|19:18|Big Data Engineer vs Data Scientist]],
she describes user information, ratings, and search history as inputs to
streaming and batch pipelines. Data scientists train the model after those
pipelines prepare the data. At
[[podcast:big-data-engineer-vs-data-scientist|22:51]],
she separates streaming updates from historical batch data.

Flink and Spark can each play a part, while Parquet and S3 appear with databases
in her example. Production recommendation systems depend on
[[data pipelines]],
[[data engineering platforms]],
and [[batch-vs-streaming|batch versus streaming]].

Daniel gives the retrieval-and-ranking definition. In
[[podcast:building-production-search-systems|12:45|Building Search Systems]],
he splits search systems into candidate generation and ranking. That same split
fits recommendations.

First, narrow the item universe to plausible candidates. Then score and reorder
the list through the same path that handles filters and serving.

Around
[[podcast:building-production-search-systems|21:55]],
he uses personalization to show why behavioral data, content, and user context
usually meet in the ranking step.

## System Boundaries and Product Intent

The guests differ less on the definition than on the boundary they start from.
Some start from data movement, some from retrieval and ranking, and some from
the product outcome the recommendation should change.

[[person:roksolanadiachuk|Roksolana Diachuk]] starts
from the data engineering boundary. Her recommender example depends on events and
historical storage, plus cleaned training data. Deployment handoffs among data
engineers, data scientists, and machine learning engineers also matter
([[podcast:big-data-engineer-vs-data-scientist|Big Data Engineer vs Data Scientist at 18:54-23:40]]).

[[person:danielsvonava|Daniel Svonava]] starts from
ranking architecture. He treats recommender systems and personalized search as
neighboring problems. Both need candidate generation, ranking, contextual
signals, and business metrics
([[podcast:building-production-search-systems|Building Search Systems at 12:45 and 21:55]]).
That view ties recommender design to
[[Search]],
[[Embeddings]], and
[[Machine Learning System Design]].

[[person:atitaarora|Atita Arora]] starts from modern
retrieval infrastructure. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|52:07|Modern Search Systems]],
she discusses vector databases for session-based recommendations. At
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|54:54]],
she contrasts that with collaborative filtering. She describes recommendations
that update from clicks during the current session.

[[person:abouzarabbaspour|Abouzar Abbaspour]] centers
product intent in a theme-park setting, while
[[person:stefangudmundsson|Stefan Gudmundsson]] does the
same in healthcare. Abouzar's theme-park system recommended the next best move
for each group. The product goal was to reduce waiting time and redistribute
visitors. The system joined prediction with an operational
[[data-products|data product]]
([[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|12:59|Theme Park Crowd Modeling]]).

Stefan's healthcare example recommends content and exercises. It also recommends
behavior changes, but the system has an explicit health agenda. It isn't only
maximizing similarity to past preferences
([[podcast:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics at 36:01-38:53]]).

## Candidate Generation, Ranking, and Retrieval

Recommendation systems share much of their structure with
[[search|production search]]. A team needs to find
plausible items quickly. It then ranks them using signals that match the product
decision.
[[person:danielsvonava|Daniel Svonava]]'s
candidate-generation and ranking split at
[[podcast:building-production-search-systems|12:45]]
is the clearest architecture anchor. Retrieval narrows the full inventory, while
ranking brings in context and machine learning.

That ranking layer can combine text, behavior, freshness, and popularity.
Business rules belong there too. Daniel's discussion at
[[podcast:building-production-search-systems|34:00]]
warns that a strict waterfall of constraints can overconstrain results. The user
may want a compromise among relevance, recency, popularity, and "popular for
people like me." At
[[podcast:building-production-search-systems|36:21]],
he connects custom embeddings and custom ranking models to the MLOps work that
follows.

[[person:atitaarora|Atita Arora]]'s vector-database
discussion adds the session-based version. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|52:27|Modern Search Systems]],
she says recommendations can update per session based on clicks rather than
being precomputed once per user. At
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|56:44]],
she treats context as the important signal. Session context brings
recommendation systems close to [[vector databases]],
[[production search evaluation]],
and [[information retrieval]].

## Data Pipelines and Feature Freshness

Recommendations depend on current and historical data at the same time.
[[person:roksolanadiachuk|Roksolana Diachuk]]'s
Netflix-style example uses streaming data for new ratings and behavior. It also
uses batch storage for history
([[podcast:big-data-engineer-vs-data-scientist|19:18|Big Data Engineer vs Data Scientist]]).

That mix lets data scientists train on cleaned history while the product keeps
collecting new signals. It also forces teams to assign ownership. One team may
maintain the stream. Another may prepare training data or deploy the model.
Someone also has to write results back for the product and analysts.

Daniel shows the same freshness issue inside ranking. Around
[[podcast:building-production-search-systems|38:11]],
he discusses embeddings for title, content and images. Behavioral signals belong
in the same design too.

At [[podcast:building-production-search-systems|41:56]],
Daniel uses timestamp encoding so teams can represent recency without
recomputing everything naively. At
[[podcast:building-production-search-systems|44:36]],
he moves to query-time weights because the right balance can differ by page
type.

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

Collaborative filtering appears as the familiar user-item starting point, and
Stefan explains it through Spotify and Netflix at
[[podcast:ai-in-healthcare-and-digital-therapeutics|36:01]].
People similar to you liked content you haven't seen yet. Atita revisits the
same matrix-and-vectors idea at
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|54:03]],
then contrasts it with session-aware recommendations that can react to the
current click path.

Next-best-action systems add an operational goal.
[[person:abouzarabbaspour|Abouzar Abbaspour]]'s
Efteling example recommended the next attraction for a group by using queue
predictions and ride capacity. He also used transaction signals and route
preferences
([[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling at 12:59-17:50]]).
The recommendation wasn't only "people like you liked this." It was a routing
decision meant to reduce waiting and improve the park experience.

Agenda-driven personalization adds a normative goal. Stefan describes Sidekick
Health as building a recommender that nudges people toward healthier behavior.
It doesn't only reinforce past preferences
([[podcast:ai-in-healthcare-and-digital-therapeutics|36:01|AI in Healthcare and Digital Therapeutics]]).

At [[podcast:ai-in-healthcare-and-digital-therapeutics|38:53]],
the item catalog includes educational content, cards, and exercises. The
recommendation problem is closer to a treatment plan than a media feed. It links
recommender design to [[data products]]
and [[data product management]].

## Evaluation and Experimentation

Guests repeatedly treat evaluation as the hard part of recommendation systems.
Abouzar says this directly in
[[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|24:16|Theme Park Crowd Modeling]].
In the Bol.com favorite-brand project, he tested likely favorite brands before
releasing the new product surface. He used an employee swiping game for that
check. At
[[podcast:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|31:39]],
he reports about 85 percent accuracy in that validation setup.

[[person:sadatanwar|Sadat Anwar]] gives the business
metric version in
[[podcast:from-software-engineering-to-leading-data-science-teams|18:58|From Software Engineering to Leading Data Science Teams]].
His team replaced a recommendation SaaS provider with a word2vec-based internal
model, then used A/B tests and saw a 2-3 percent transaction lift from
recommendations. The same story also included training and data gathering. The
team also handled production hosting and a retraining job, so the result wasn't
only a model comparison.
At that point, recommendation systems become
[[machine learning system design]]
problems rather than only modeling problems.

Stefan gives the staged-experimentation version. In
[[podcast:ai-in-healthcare-and-digital-therapeutics|39:57|AI in Healthcare and Digital Therapeutics]],
he argues against jumping directly into collaborative filtering or deep learning
for recommenders. He starts with A/B tests and variant availability, then uses
segments and accumulated data to move toward clustering or collaborative
filtering. At
[[podcast:ai-in-healthcare-and-digital-therapeutics|43:00]],
the discussion makes analytics and good data prerequisites for machine
learning.

Daniel adds the search-recommender metric discipline. In
[[podcast:building-production-search-systems|1:01:25|Building Search Systems]],
he argues that teams get more support when recommender or search metrics connect
to business performance. At
[[podcast:building-production-search-systems|1:03:50]],
he adds offline tests, A/B tests, and engineer-facing metrics for faster
iteration. Use [[evaluation]],
[[metrics]],
[[experimentation and causal inference]],
and [[a-b-testing|A/B testing]] for the surrounding
measurement discipline.

## Safety, Product Constraints, and Guardrails

Recommendation quality isn't only click-through rate, and Stefan's healthcare
discussion adds a safety boundary. In
[[podcast:ai-in-healthcare-and-digital-therapeutics|51:55|AI in Healthcare and Digital Therapeutics]],
he uses hydration advice for heart-failure patients as an example. A suggestion
that helps most people may be unsafe for a specific medical group. The team
needs medical review before testing risky recommendations, even if the product
can test low-risk features quickly.

Daniel's product constraints are lower risk but still important. At
[[podcast:building-production-search-systems|34:00]],
he describes freshness and relevance as constraints that teams must balance.
Popularity belongs in that balance too. At
[[podcast:building-production-search-systems|58:17]],
he recommends prototyping e-commerce personalization with embeddings and product
images.

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

[[person:sadatanwar|Sadat Anwar]]'s word2vec
recommendation project included data engineering and data gathering. It also
included production hosting on AWS and a retraining job
([[podcast:from-software-engineering-to-leading-data-science-teams|18:58|From Software Engineering to Leading Data Science Teams]]).

Roksolana's walkthrough asks the same ownership question from the data
engineering side. Deployment may sit with machine learning engineers, data
scientists, or data engineers depending on the team
([[podcast:big-data-engineer-vs-data-scientist|19:18|Big Data Engineer vs Data Scientist]]).

[[person:mariavechtomova|Maria Vechtomova]] gives the
MLOps platform view. In
[[podcast:pragmatic-and-standardized-mlops|43:24|Pragmatic MLOps]],
she says monitoring and A/B testing were important next standardization areas.
At [[podcast:pragmatic-and-standardized-mlops|44:19]],
she names demand forecasting and recommendation engines as use cases that can
fit into standard monitoring tools. At
[[podcast:pragmatic-and-standardized-mlops|51:07]],
she mentions personalization and loyalty programs as common retail problems
across brands.

[[person:annahannemann|Anna Hannemann]] adds the product
ownership version in
[[podcast:building-data-products-product-owner-vs-product-manager|22:08|Building Data Products at Scale]].
Her METRO recommender discussion uses API-first design and scaling as the
operating frame. At
[[podcast:building-data-products-product-owner-vs-product-manager|30:01]],
she connects production ML hiring to data scientists, machine learning
engineers, and MLOps. At
[[podcast:building-data-products-product-owner-vs-product-manager|34:53]],
she discusses collaborative filtering and Word2Vec variants. That makes the
recommender a [[data-products|data product]] with
an API, owners, metrics, and production staffing.

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
