---
layout: article
title: "What Does a Data Product Manager Do?"
keyword: "data product management"
summary: "A practical explanation of the data product manager role, based on podcast discussions about discovery, metrics, roadmaps, ownership, and data product adoption."
related_wiki:
  - Data Product Management
  - Data Products
  - Data Product Adoption
  - Product Analytics
  - Metrics
  - ML Product Manager Role
---

Data product management applies product management to dashboards and data
platforms. It also applies to ML systems and recommender systems. Metric layers
and other [data products]({{ '/wiki/data-products/' | relative_url }}) belong in
the same family.

A data product manager doesn't just collect stakeholder requests and hand them to
engineers. They turn data work into a product with users, tradeoffs, and success
metrics. They also own release plans and an adoption path.

Podcast guests repeatedly start data product management from a user problem.
[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) describes
internal data products as services for sales, marketing, finance, and supply
chain teams. In his manufacturing example, curated pipelines and
dashboards helped sales teams build contracts faster. Those contracts depended
on routing, capacity, demand, and pricing data. They also needed competitor and
marketing data
([4:24-7:13]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

That's why [data product management]({{ '/wiki/data-product-management/' | relative_url }}) sits between business context, data infrastructure, product
judgment, and user adoption.

## Data Product Manager Role: What It Owns

A data product manager owns the problem framing and product direction for a data
capability. [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) says
internal data product management still follows the same product principle as
external product management. Teams start with customer needs and identify pain
points. Then they work backward to a solution and build a roadmap that creates value
([7:13-11:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
The "customer" may be an internal sales team or a finance team.

It may also be a data scientist using an ML platform, or a product manager
reading an experiment report.

That ownership usually includes five jobs:

- identify the users and decisions the data product should support
- define the problem, expected outcome, and product success metrics
- prioritize roadmap items by impact, effort, cost, risk, and timing
- coordinate with data scientists, data engineers, ML engineers, designers, and
  business stakeholders
- drive rollout, feedback, quality, and [data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }})

This role isn't the same as "the person who writes tickets." [Geo Jolly]({{ '/people/geojolly/' | relative_url }}) describes the technical PM for an internal
ML platform as the person who gathers feedback from data science leads and
reviews platform gaps. The PM also writes specifications, maintains the roadmap,
and balances custom requests against long-term platform improvement
([9:50-16:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That makes the role close to the [ML product manager role]({{ '/wiki/ml-product-manager-role/' | relative_url }}) when the product is an
internal [MLOps]({{ '/wiki/mlops/' | relative_url }}) or platform capability.

## Discovery Starts Before the Dataset

Teams shouldn't choose a model, dashboard, or data pipeline before discovery.
[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) recommends
customer journey mapping, business-partner interviews, workflow documentation,
and the Five Whys before the team commits to a solution
([14:03-26:25]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
In that discussion, a churn problem isn't automatically a churn model. The team
first asks what changed in the customer journey, which business goal moved, and
which hypotheses the data can confirm or reject.

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) makes the
same point from the adoption side. For last-mile data delivery, she argues that
teams should start with the decision they want to enable. They can then work
backward to the data sources, transformations, dashboard design, and meeting
rituals needed for that decision
([34:00-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

For example, an A/B testing reporting product isn't just a dashboard. It has to
help a product manager decide whether to roll out a feature. It also has to show
business impact and guardrail metrics.

[Liesbeth Dingemans]({{ '/people/liesbethdingemans/' | relative_url }}) adds a
design lens for AI products, framing design as a user-centered product
process. She also asks teams to treat the algorithm as a stakeholder when the
interface needs better signals ([5:07-10:04]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }})).
For a data product manager, that means discovery covers both human users and the
data-generating behavior the product needs.

## Roadmaps Are Product Decisions, Not Wish Lists

When a data product manager turns discovery into a roadmap, [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) separates that roadmap from a project
plan. He defines the roadmap as the future transformation of a product, system, or
department, and he expects it to adapt as customer needs change
([41:44-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

His practical roadmap template records the problem and its driver. It then adds
possible solutions, justification, and affected stakeholders. It also captures
impact, effort, SMART goals, and priority
([47:18-51:11]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Data product managers need that structure because data products compete for
scarce engineering, data, and stakeholder attention. The next step may be
pipeline reliability or an ML feature. It may also be better documentation, an
API, or a manual operational fix.
[Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) shows this in
her recommender systems work at METRO.

The team moved from manual newsletter support toward API-first recommenders, ML
flow, and Datadog monitoring. It also built product surfaces such as
frequently-bought-together and alternative recommendations
([22:08-30:01]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

Roadmap work also requires technical realism. [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) says data professionals contribute
T-shirt sizing, infrastructure constraints, and delivery estimates when product
managers prioritize features ([28:53-35:34]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
[Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) makes the same
case for technical literacy in data product leadership. A product owner with a
data and tech background can better advocate when the team needs more time,
better data, or infrastructure changes ([12:49-15:11]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

## Metrics Decide Whether the Product Worked

The data product manager role is accountable for success criteria, not only
shipment. [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) calls
success metrics product management 101. For internal platforms, he names
pipeline latency and service-level agreements. He also names data quality
complaints, engagement, and churn ([51:11-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
Those examples connect directly to [metrics]({{ '/wiki/metrics/' | relative_url }}).

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) gives the platform
version. For an internal ML platform, the PM may define an outcome such as
reducing model training time by a target percentage. The PM then works with
engineers to decide how to achieve it. He also notes that platform impact can be
hard to measure, so teams need observability metrics and regular feedback from users
([16:44-18:25 and 55:44-57:20]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Customer-facing products often need experimentation.
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) explains that A/B
testing establishes a causal link between a product change and its impact by
randomizing users. Teams then track outcomes and control noise
([8:13-13:25]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

In his subscription-versus-points example, the rollout decision depends on a revenue
metric, not just a team's intuition about the feature
([14:27-18:06]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).
That's why data product management often overlaps with [product analytics]({{ '/wiki/product-analytics/' | relative_url }}).
It also overlaps with [experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).

## Adoption Is Part of the Role

A data product isn't finished when the table, dashboard, model, or platform
feature exists. [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
describes the last mile as the gap between making data available and getting it
used in real decisions. Teams have to make the product easy to find, interpret,
and trust. It also needs to be easy enough to use that the benefit outweighs the
cost ([13:24-24:13]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) gives a concrete internal
platform example. Even though his ML platform served internal users, he treated
more than 100 data scientists and analysts as customers. He also included
business data engineers. Without product direction, he warns, internal platforms
accumulate tools and libraries. They also add UIs until users don't know where
to start
([11:24-13:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

His team used surveys and follow-up sessions. It also used a Happiness Report to
turn user feedback about documentation, stability, and usability into objectives
([55:44-57:20]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Adoption work also shows up in business communication. [Loris Marini]({{ '/people/lorismarini/' | relative_url }}) describes a SaaS reporting problem
where users had too much real-time campaign information and not enough guidance
on what to do next. His team worked on making reporting more actionable, moving
from raw information toward diagnostic and prescriptive support ([4:51-8:30]({{ '/podcasts/data-professionals-business-skills-in-saas/' | relative_url }})).
The data product has to fit the user's decision, not just expose more data.

## Product Manager, Product Owner, and Data Team Boundaries

Title boundaries vary by company. [Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) says the distinction between product
owner and product manager is often unclear across organizations. In her view, a
product owner is closer to the CEO of the product. A product manager may have
less decision power and listen more to tech leads and teams
([15:11-21:45]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

The team needs someone with authority to decide whether the product is good
enough to ship. They also need someone who can decide whether the team needs two
more weeks and which constraints matter.

Data product managers also don't replace data engineers, data scientists, ML
engineers, or analytics engineers. [Geo Jolly]({{ '/people/geojolly/' | relative_url }}) says the PM defines the problem and
desired outcome while the engineering team defines the solution
([15:19-16:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
This split keeps product work connected to technical reality without turning the
roadmap into a list of preferred tools. When the product is internal
infrastructure, the role also connects to [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

## Building the Skill Set

The data product manager role rewards people who can move between business
questions and technical delivery. Start discovery by identifying the
customer and mapping the decision. Then interview domain experts and write down
the pain points before proposing a solution. [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) recommends this even for teams
without a formal PM, because it prevents people from solving problems that do
not exist ([55:32-58:42]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Then practice roadmap and measurement work. For each candidate data product,
write the problem and user. Then add the business value, technical constraints,
and effort. Add the rollout plan, success metric, and adoption risk too.

That exercise matches how [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) frames
roadmaps. It also matches how [Geo Jolly]({{ '/people/geojolly/' | relative_url }})
frames internal platform prioritization and how [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
frames last-mile adoption.

For readers comparing this role with adjacent paths, use the broader wiki page
on [data product management]({{ '/wiki/data-product-management/' | relative_url }}).
The role-specific page on [ML product managers]({{ '/wiki/ml-product-manager-role/' | relative_url }})
covers platform-heavy PM work. The adoption-focused page on
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
covers last-mile usage.
