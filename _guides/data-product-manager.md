---
layout: article
title: "Data Product Manager"
keyword: "data product manager"
summary: "A podcast-grounded definition of the data product manager role: who they serve, what they own, and how they turn data work into adopted products."
search_intent: "Define what a data product manager is, when a team needs one, and how the role differs from analytics, data science, and product owner work."
related_wiki:
  - Data Product Management
  - Data Product Adoption
  - Data Products
  - Product Analytics
  - Experimentation and Causal Inference
---

A data product manager is a product manager who makes data, analytics, or
machine learning useful to a real group of users. They don't only ask whether a
dashboard, model, metric layer, or platform feature can be built. They ask who
will use it, which decision it supports, how people will trust it, and how the
team will know it worked.

DataTalks.Club guests ground that definition in product work, not only data
delivery. [Sara Menefee]({{ '/people/saramenefee/' | relative_url }}) starts
data product management with customer discovery and hypotheses about user
problems
([7:04-11:38]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) gives the internal
platform version. The product manager defines the problem and desired outcome,
while engineers and technical leads design the solution
([16:44-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) adds the
adoption test. Data has to reach the meeting, workflow, or person making the
decision
([8:48-26:36]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Those interviews match the reference definition of
[data product management]({{ '/wiki/data-product-management/' | relative_url }}):
the work starts with user discovery and ends only when the data product changes
decisions. It also connects to related pages on
[data products]({{ '/wiki/data-products/' | relative_url }}),
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), and
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).

## The Short Definition

A data product manager owns the product judgment around a data capability.
Menefee's episode on moving from product design into data product management
starts the role with customer discovery and hypothesis formation. She then adds
market and tooling research before the team commits to a solution
([7:04-11:38]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

That makes the role different from a general request intake function. The data
product manager has to understand the user problem and the data lifecycle. They
also have to understand the delivery path from source systems through
transformations and warehouses. They also need the context for applications,
dashboards, or APIs.

Menefee treats data quality, PII, compliance, and SQL as part of the role's
working context. Documentation literacy belongs there too. These aren't optional
polish
([19:38-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

## Core Responsibilities

A data product manager usually owns four questions.

- Who uses or consumes the data product?
- What decision, workflow, or behavior should change?
- What metric proves that the product is working?
- What tradeoff should the team accept on scope, quality, speed, cost, or risk?

Jolly's ML product management interview gives a platform version of this
work. At Glovo, he describes leading an internal machine learning platform used
by data scientists and analysts. His product work includes roadmap direction and
specifications. He also gathers feedback from data science leads, prioritizes
the backlog, and communicates with stakeholders
([6:28-16:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Jolly's strongest distinction is that the product manager defines the problem
and desired outcome while engineers and technical leads design the solution. He
warns against jumping straight to a favorite technical approach before
validating the problem
([16:44-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

## Data Products Need Adoption Work

A team hasn't finished the product work if it only ships the data output.
Moorman's last-mile data delivery episode frames the missing work as the
gap between making data available and getting teams to change decisions with it.
People have to find the data, understand it, trust it, and bring it into the
meeting or workflow where the decision happens
([8:48-26:36]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Moorman's advice is product management in a data setting: treat poor adoption as
a user research problem. Ask whether people know the product exists and know how
to use it. Then ask whether it solves the problem they actually have. For
analytics and A/B testing tools, she recommends starting from the decision a
product manager needs to make. Then work backward to the data sources,
transformation jobs, joins, and dashboard design
([26:21-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

This is why a data product manager needs fluency in
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
when the data product supports product decisions. The manager doesn't need to
be the statistician for every test, but they need enough judgment to connect
metrics, guardrails, and rollout decisions.

## Product Manager, Product Owner, And Domain Owner

Guests don't use one universal title for this work. In [Anna
Hannemann]({{ '/people/annahannemann/' | relative_url }})'s episode on product
owners in data science, companies draw different boundaries between product
owner, product manager, and domain owner. Hannemann describes the role as
sitting between stakeholders and data scientists or developers. The product
owner translates requirements, shields the team from unrealistic expectations,
and decides whether quality is good enough to go live
([15:11-21:45]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

Her examples are deliberately business-led. Operations teams bring problems,
and the data product leader chooses among a model, manual work, and an MVP.
Sometimes they choose a larger investment. In one case, fixing 200 bad rows
manually was better than turning machine learning into a hammer for every
problem. In another, portfolio-style questions helped stage data product
investments across several use cases
([44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

## Need Signals

You probably need a data product manager when data work has real users and
competing priorities. Use decisions as the signal, not headcount or tooling
maturity. Menefee puts user discovery and success metrics
inside the data PM role
([7:04-15:10]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).
Jolly puts problem definition, roadmap direction, and outcome ownership in the
PM role for an internal ML platform
([6:28-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Hannemann shows the release-risk version. A product owner may decide whether a
model is good enough to go live and explain that quality to stakeholders
([15:11-21:45]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
Moorman adds the adoption version. Someone has to make the data findable,
understandable, trusted, and useful at the decision point
([20:02-28:10]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

That can mean a customer-facing recommendation system, an internal MLOps
platform, or an experimentation dashboard. It can also mean a governed metric
layer or a decision-support workflow. In each case, someone has to own the
product judgment. Without that owner, the team can build technically correct
dashboards, models, or tables that nobody uses
([8:48-26:36]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Use [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
for the broader reference page. Use
[Product Owner vs Product Manager]({{ '/comparisons/product-owner-vs-product-manager/' | relative_url }})
for the title boundary. Use
[Data Product Manager vs Product Manager]({{ '/comparisons/data-product-manager-vs-product-manager/' | relative_url }})
for the closest role comparison.

[Product Designer to Data Product Manager]({{ '/wiki/product-designer-to-data-product-manager/' | relative_url }})
covers the design-to-data transition.
[Data Product Manager Roadmap]({{ '/roadmaps/data-product-manager-roadmap/' | relative_url }})
covers the learning path.
[Data Product Owner vs Data Product Manager]({{ '/comparisons/data-product-owner-vs-data-product-manager/' | relative_url }})
covers the data-specific owner boundary.
