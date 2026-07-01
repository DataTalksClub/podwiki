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
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
vocabulary. It shares retrieval and ranking problems with
[search]({{ '/wiki/search/' | relative_url }}). It also borrows measurement
discipline from
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

Modern recommenders also use
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) and
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}) when a team
retrieves similar items before ranking them. Teams need
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) so the model can
learn from behavior. They use
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) to prove
that the ranked output helped. [MLOps]({{ '/wiki/mlops/' | relative_url }})
covers the release and retraining path.

Guests treat a recommender as a system that needs data pipelines, candidate
generation, and ranking. It also needs product constraints, evaluation, and
monitoring.

[Roksolana
Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) walks through a
Netflix-like recommendation project as a streaming and batch data problem in
[Big Data Engineer vs Data Scientist at 18:54]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}).
[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) connects
recommenders to search architecture and ranking in
[Building Search Systems at 12:45]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
He also connects them to vectors at
[21:55]({{ '/podcasts/building-production-search-systems/' | relative_url }})
and business metrics at
[1:01:25]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
[Stefan Gudmundsson]({{ '/people/stefangudmundsson/' | relative_url }}) adds
the healthcare version, where recommendations are personalized interventions
that need experimentation and safety review
([AI in Healthcare and Digital Therapeutics at 35:39]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }})).

## Ranked Product Decisions

A recommendation system turns behavioral data, item data, and context into a
ranked product decision. The output may be a movie, product, brand, or article.
In other domains, it may be an exercise, route, or next action. Teams need to
know what they can recommend and whom they recommend to. They also need to know
which signals must stay fresh and which outcome proves that the recommendation
helped.

Roksolana gives the data-platform definition. In
[Big Data Engineer vs Data Scientist at 19:18]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
she describes user information, ratings, and search history as inputs to
streaming and batch pipelines. Data scientists train the model after those
pipelines prepare the data. At
[22:51]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
she separates streaming updates from historical batch data.

Flink and Spark can each play a part, while Parquet and S3 appear with databases
in her example. That connects recommendation
systems to [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [batch versus streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}).

Daniel gives the retrieval-and-ranking definition. In
[Building Search Systems at 12:45]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he splits search systems into candidate generation and ranking. That same split
fits recommendations.

First, narrow the item universe to plausible candidates. Then score and reorder
the list through the same path that handles filters and serving.

Around
[21:55]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he uses personalization to show why behavioral data, content, and user context
usually meet in the ranking step.

## System Boundaries and Product Intent

The guests differ less on the definition than on the boundary they start from.
Some start from data movement, some from retrieval and ranking, and some from
the product outcome the recommendation should change.

[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) starts
from the data engineering boundary. Her recommender example depends on events and
historical storage, plus cleaned training data. Deployment handoffs among data
engineers, data scientists, and machine learning engineers also matter
([Big Data Engineer vs Data Scientist at 18:54-23:40]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})).

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) starts from
ranking architecture. He treats recommender systems and personalized search as
neighboring problems. Both need candidate generation, ranking, contextual
signals, and business metrics
([Building Search Systems at 12:45 and 21:55]({{ '/podcasts/building-production-search-systems/' | relative_url }})).
That view ties recommender design to
[Search]({{ '/wiki/search/' | relative_url }}),
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) starts from modern
retrieval infrastructure. In
[Modern Search Systems at 52:07]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she discusses vector databases for session-based recommendations. At
[54:54]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she contrasts that with collaborative filtering. She describes recommendations
that update from clicks during the current session.

[Abouzar Abbaspour]({{ '/people/abouzarabbaspour/' | relative_url }}) centers
product intent in a theme-park setting, while
[Stefan Gudmundsson]({{ '/people/stefangudmundsson/' | relative_url }}) does the
same in healthcare. Abouzar's theme-park system recommended the next best move
for each group. The product goal was to reduce waiting time and redistribute
visitors. The system joined prediction with an operational
[data product]({{ '/wiki/data-products/' | relative_url }})
([Theme Park Crowd Modeling at 12:59]({{ '/podcasts/theme-park-crowd-modeling-to-tesla-full-stack-data-engineering/' | relative_url }})).

Stefan's healthcare example recommends content and exercises. It also recommends
behavior changes, but the system has an explicit health agenda. It isn't only
maximizing similarity to past preferences
([AI in Healthcare and Digital Therapeutics at 36:01-38:53]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }})).

## Candidate Generation, Ranking, and Retrieval

Recommendation systems share much of their structure with
[production search]({{ '/wiki/search/' | relative_url }}). A team needs to find
plausible items quickly. It then ranks them using signals that match the product
decision.
[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }})'s
candidate-generation and ranking split at
[12:45]({{ '/podcasts/building-production-search-systems/' | relative_url }})
is the clearest architecture anchor. Retrieval narrows the full inventory, while
ranking brings in context and machine learning.

That ranking layer can combine text, behavior, freshness, and popularity.
Business rules belong there too. Daniel's discussion at
[34:00]({{ '/podcasts/building-production-search-systems/' | relative_url }})
warns that a strict waterfall of constraints can overconstrain results. The user
may want a compromise among relevance, recency, popularity, and "popular for
people like me." At
[36:21]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he connects custom embeddings and custom ranking models to the MLOps work that
follows.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }})'s vector-database
discussion adds the session-based version. In
[Modern Search Systems at 52:27]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she says recommendations can update per session based on clicks rather than
being precomputed once per user. At
[56:44]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she treats context as the important signal. This connects
recommendation systems to [vector databases]({{ '/wiki/vector-databases/' | relative_url }}),
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
and [information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).

## Data Pipelines and Feature Freshness

Recommendations depend on current and historical data at the same time.
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }})'s
Netflix-style example uses streaming data for new ratings and behavior. It also
uses batch storage for history
([Big Data Engineer vs Data Scientist at 19:18]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})).

That mix lets data scientists train on cleaned history while the product keeps
collecting new signals. It also forces teams to assign ownership. One team may
maintain the stream. Another may prepare training data or deploy the model.
Someone also has to write results back for the product and analysts.

Daniel shows the same freshness issue inside ranking. Around
[38:11]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he discusses embeddings for title, content and images. Behavioral signals belong
in the same design too.

At [41:56]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel uses timestamp encoding so teams can represent recency without
recomputing everything naively. At
[44:36]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he moves to query-time weights because the right balance can differ by page
type.

This is why recommender work belongs near
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
A stale event stream can break recommendations even when the model code didn't
change. Duplicate records, missing item metadata, and changed user behavior can
do the same.

## Personalization Modes

Guests describe several personalization modes rather than one universal
recommender design.

Collaborative filtering appears as the familiar user-item starting point, and
Stefan explains it through Spotify and Netflix at
[36:01]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}).
People similar to you liked content you haven't seen yet. Atita revisits the
same matrix-and-vectors idea at
[54:03]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
then contrasts it with session-aware recommendations that can react to the
current click path.

Next-best-action systems add an operational goal.
[Abouzar Abbaspour]({{ '/people/abouzarabbaspour/' | relative_url }})'s
Efteling example recommended the next attraction for a group by using queue
predictions and ride capacity. He also used transaction signals and route
preferences
([Theme Park Crowd Modeling at 12:59-17:50]({{ '/podcasts/theme-park-crowd-modeling-to-tesla-full-stack-data-engineering/' | relative_url }})).
The recommendation wasn't only "people like you liked this." It was a routing
decision meant to reduce waiting and improve the park experience.

Agenda-driven personalization adds a normative goal. Stefan describes Sidekick
Health as building a recommender that nudges people toward healthier behavior.
It doesn't only reinforce past preferences
([AI in Healthcare and Digital Therapeutics at 36:01]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }})).

At [38:53]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}),
the item catalog includes educational content, cards, and exercises. The
recommendation problem is closer to a treatment plan than a media feed. It links
recommender design to [data products]({{ '/wiki/data-products/' | relative_url }})
and [data product management]({{ '/wiki/data-product-management/' | relative_url }}).

## Evaluation and Experimentation

Guests repeatedly treat evaluation as the hard part of recommendation systems.
Abouzar says this directly in
[Theme Park Crowd Modeling at 24:16]({{ '/podcasts/theme-park-crowd-modeling-to-tesla-full-stack-data-engineering/' | relative_url }}).
In the Bol.com favorite-brand project, he tested likely favorite brands before
releasing the new product surface. He used an employee swiping game for that
check. At
[31:39]({{ '/podcasts/theme-park-crowd-modeling-to-tesla-full-stack-data-engineering/' | relative_url }}),
he reports about 85 percent accuracy in that validation setup.

[Sadat Anwar]({{ '/people/sadatanwar/' | relative_url }}) gives the business
metric version in
[From Software Engineering to Leading Data Science Teams at 18:58]({{ '/podcasts/from-software-engineering-to-leading-data-science-teams/' | relative_url }}).
His team replaced a recommendation SaaS provider with a word2vec-based internal
model, then used A/B tests and saw a 2-3 percent transaction lift from
recommendations. The same story also included training and data gathering. The
team also handled production hosting and a retraining job, so the result wasn't
only a model comparison.
At that point, recommendation systems become
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
problems rather than only modeling problems.

Stefan gives the staged-experimentation version. In
[AI in Healthcare and Digital Therapeutics at 39:57]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}),
he argues against jumping directly into collaborative filtering or deep learning
for recommenders. He starts with A/B tests and variant availability, then uses
segments and accumulated data to move toward clustering or collaborative
filtering. At
[43:00]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}),
the discussion makes analytics and good data prerequisites for machine
learning.

Daniel adds the search-recommender metric discipline. In
[Building Search Systems at 1:01:25]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he argues that teams get more support when recommender or search metrics connect
to business performance. At
[1:03:50]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he adds offline tests, A/B tests, and engineer-facing metrics for faster
iteration. Use [evaluation]({{ '/wiki/evaluation/' | relative_url }}),
[metrics]({{ '/wiki/metrics/' | relative_url }}),
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}),
and [A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}) for the surrounding
measurement discipline.

## Safety, Product Constraints, and Guardrails

Recommendation quality isn't only click-through rate, and Stefan's healthcare
discussion adds a safety boundary. In
[AI in Healthcare and Digital Therapeutics at 51:55]({{ '/podcasts/ai-in-healthcare-and-digital-therapeutics/' | relative_url }}),
he uses hydration advice for heart-failure patients as an example. A suggestion
that helps most people may be unsafe for a specific medical group. The team
needs medical review before testing risky recommendations, even if the product
can test low-risk features quickly.

Daniel's product constraints are lower risk but still important. At
[34:00]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he describes freshness and relevance as constraints that teams must balance.
Popularity belongs in that balance too. At
[58:17]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he recommends prototyping e-commerce personalization with embeddings and product
images.

Descriptions, behavior and frequent queries can guide that prototype too. The
guardrail is practical: prove that the new results differ usefully
from the current production system before committing to a larger build.


These examples connect recommendation systems to
[evaluation]({{ '/wiki/evaluation/' | relative_url }}), [product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
and [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}). A good
recommender must optimize the intended outcome. It also has to avoid known
harms and stale suggestions. Impossible inventory, unsafe advice, and
misleading aggregate metrics need guardrails too.

## Operations, Monitoring, and Ownership

Recommendation systems become production systems when teams need repeatable
training and serving. They also need retraining, monitoring, and rollback.

[Sadat Anwar]({{ '/people/sadatanwar/' | relative_url }})'s word2vec
recommendation project included data engineering and data gathering. It also
included production hosting on AWS and a retraining job
([From Software Engineering to Leading Data Science Teams at 18:58]({{ '/podcasts/from-software-engineering-to-leading-data-science-teams/' | relative_url }})).

Roksolana's walkthrough asks the same ownership question from the data
engineering side. Deployment may sit with machine learning engineers, data
scientists, or data engineers depending on the team
([Big Data Engineer vs Data Scientist at 19:18]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }})).

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) gives the
MLOps platform view. In
[Pragmatic MLOps at 43:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she says monitoring and A/B testing were important next standardization areas.
At [44:19]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she names demand forecasting and recommendation engines as use cases that can
fit into standard monitoring tools. At
[51:07]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she mentions personalization and loyalty programs as common retail problems
across brands.

[Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) adds the product
ownership version in
[Building Data Products at Scale at 22:08]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }}).
Her METRO recommender discussion uses API-first design and scaling as the
operating frame. At
[30:01]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }}),
she connects production ML hiring to data scientists, machine learning
engineers, and MLOps. At
[34:53]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }}),
she discusses collaborative filtering and Word2Vec variants. That makes the
recommender a [data product]({{ '/wiki/data-products/' | relative_url }}) with
an API, owners, metrics, and production staffing.

Teams may start a recommender as a notebook or a small batch job. They may also
start with a search-ranking tweak. They turn it into shared infrastructure when
several product surfaces need the same events and features.

When teams need shared models and experiments, the recommender connects back to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).
It also connects to [model registry]({{ '/wiki/model-registry/' | relative_url }})
and [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

## Related Pages

Use these pages for the surrounding architecture, evaluation, and operating
details.

- [Search]({{ '/wiki/search/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
