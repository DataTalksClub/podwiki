---
layout: wiki
title: "Data Product Management"
summary: "How DataTalks.Club podcast guests define data product management: user discovery, role boundaries, roadmaps, adoption, metrics, ownership, and operating discipline for data products."
related:
  - Data Products
  - Data Product Adoption
  - Product Analytics
  - Data Engineering Platforms
  - MLOps
  - Data Mesh
---

Data product management applies product management to data capabilities such as
dashboards, metrics, and event streams. It also covers models, ML platforms, and
the operating systems around them. In the DataTalks.Club archive, the role is
defined less by the title than by the decision boundary it owns. A data product
manager clarifies the user problem and chooses the outcome. They manage the
roadmap, coordinate delivery, and prove that the product changes a decision or
workflow.

The concept sits next to [Data Products]({{ '/wiki/data-products/' | relative_url }}),
which covers the artifact.
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
covers the last-mile problem of getting people to trust and use the work. Data
product management also overlaps with
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) when a data product
changes user behavior. It overlaps with
[MLOps]({{ '/wiki/mlops/' | relative_url }}) or
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
when the product is an internal technical platform.

[Sara Menefee]({{ '/people/saramenefee/' | relative_url }}) gives the clearest
transition example in
[Product Designer to Data Product Manager]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}).
She frames data product management as regular product work with data-specific
literacy. That work includes customer discovery and hypothesis formation.
Planning, engineering partnership, and launch come next. It also requires SQL
and data quality judgment.

PII, compliance, and documentation literacy matter too
([7:04-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) gives the roadmap
version in
[Building and Scaling AI Data Products with MLOps]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }}).
In his version, product work starts from customer needs and pain points. Roadmap
tradeoffs and measurable business value come next
([6:41-14:03]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

## Archive Consensus

Across the archive, data product management starts before a technical solution
is chosen. Menefee starts with product discovery. The team talks to users,
understands what they're responsible for, and forms a hypothesis about the
problem. Planning and engineering follow
([7:04-15:10]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo uses the same problem-first rule for AI products. Customer journey
mapping and domain knowledge come before roadmap commitments. So do interviews,
documentation review, the Five Whys, and hypothesis testing
([14:03-26:25]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

The common role boundary is ownership of the why and the what. The PM doesn't
own every technical detail. [Geo Jolly]({{ '/people/geojolly/' | relative_url }})
describes an ML platform PM who defines the problem and the target outcome.
Technical leads design the solution. He warns against starting from a favorite
solution before the team validates the user problem
([16:44-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Coquillo gives the same split from the data-team side. Data professionals bring
technical input and T-shirt sizing into the roadmap. The team still works
backward from the business problem
([26:25-35:34]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

The product isn't complete when a table, dashboard, model, or platform feature
ships. [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) argues
in
[Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
that adoption depends on discoverability and interpretability. Trust, data
quality, and the meeting or workflow where the decision is made also matter
([24:13-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Ioannis Mesionis]({{ '/people/ioannismesionis/' | relative_url }}) turns that
into an operating model in
[Building Data Products at Scale]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }}).
The lifecycle includes intake, Definition of Done, KPIs, and feasibility checks.
Pilots and A/B tests come before production. Rollout, monitoring, demos, and
stakeholder feedback also belong there
([14:00-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

## Guest Differences

Guests differ most in the center of gravity they give the role. Menefee centers
it on discovery, empathy, data literacy, and execution. Her data product manager
asks how users make decisions. The role also stays close enough to data quality,
SQL, and PII to make delivery credible. Compliance and documentation matter too
([19:38-26:33 and 46:01-56:08]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo centers the role on roadmap discipline for AI and MLOps work. His
roadmap ranks opportunities by impact, effort, and cost. It then moves from
problems to solutions to metrics. Success metrics include SMART goals and
operational measures. Pipeline failures, SLAs, and data quality belong there too
([41:44-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Jolly centers the role on internal platform adoption. He treats data scientists,
analysts, and other platform users as customers. Product management includes
feedback loops, productivity costs, and backlog prioritization. Observability
KPIs, release governance, and rollout timing are part of the same work
([11:24-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That version sits close to the
[ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).

[Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) draws the
clearest title boundary in
[Product Owners in Data Science]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }}).
A product owner often protects delivery teams and makes tactical release
tradeoffs. A product manager may own broader strategy. A domain owner may align
data science work across product and business areas
([15:11-22:08]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
Use
[Data Product Owner vs Data Product Manager]({{ '/comparisons/data-product-owner-vs-data-product-manager/' | relative_url }})
and
[Product Owner vs Product Manager]({{ '/comparisons/product-owner-vs-product-manager/' | relative_url }})
for the dedicated role comparisons.

## Role Boundaries

Data product management is adjacent to data science and data engineering. It
also touches analytics engineering and product analytics. The role boundary is
product judgment. The PM decides which user problem matters, which interface
should exist, and which adoption path is credible. They also decide which metric
proves the work mattered.

Menefee shows that boundary through discovery and planning. Launch, data
quality, and documentation also belong in the role
([7:04-28:30]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Jolly shows it through platform PM work. The PM defines the problem, balances
stakeholders, manages rollout, and measures platform impact. Engineers own
implementation details
([16:44-29:08]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
builds trusted models, transformations, tests, and BI-ready data products.
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) builds and
operates pipelines, while
[Data Science]({{ '/wiki/data-science/' | relative_url }}) develops models and
analytical methods. Data product management decides whether those capabilities
solve the right problem, whether users can use them, and whether the team can
measure the result.

The role can exist without the exact title, and Coquillo describes teams
operating without a PM. They still need to identify the customer and validate
the work. They also need to align mental models so the team makes product
decisions instead of only technical decisions
([55:32-58:42]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
Mesionis shows the same structure inside a lead data scientist role through
intake, Definition of Done, and pilots. Demos and stakeholder communication
serve the same function
([14:00-38:17]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

## Discovery and Problem Framing

Discovery is the first practical skill in the archive. Menefee's transition
episode puts user research and customer development before engineering.
Hypothesis formation and PM-designer collaboration come before engineering too
([4:58-16:26]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo adds a business-partner version. The team maps the customer journey
and learns the domain. It interviews stakeholders, reads existing documentation,
asks why repeatedly, and works backward from the business problem
([14:03-35:34]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Moorman extends discovery into adoption. Poor usage may mean users don't know
the data product exists. They may not understand it, trust it, or see how it
fits the decision they need to make
([24:13-34:00]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).
That makes user research part of
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
not only a pre-project ritual.

This is also where data product management connects to
[Data Strategy]({{ '/wiki/data-strategy/' | relative_url }}). Hannemann's
operations examples show that the best product decision may be a manual cleanup,
an MVP, or staged investment. The answer doesn't have to be a model
([44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
The product manager chooses the smallest credible path to learning and impact.

## Roadmaps and Tradeoffs

Roadmaps in data product management are evidence and tradeoff documents, not
lists of possible models. Coquillo's roadmap approach asks for technical input
and T-shirt sizing. It uses problem-first feature design and ranks longer-term
MLOps investments by impact, effort, and cost
([28:53-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Jolly adds the internal platform version. Backlog grooming, engineering
partnership, and user feedback must balance adoption and quality. Governance and
stakeholder value matter too
([15:19-23:28 and 31:28-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

For a learning path through these responsibilities, use the
[Data Product Manager Roadmap]({{ '/roadmaps/data-product-manager-roadmap/' | relative_url }}).
For a role-focused description, use the
[Data Product Manager Guide]({{ '/guides/data-product-manager/' | relative_url }})
and
[Data Product Manager Role]({{ '/guides/data-product-manager-role/' | relative_url }}).
Those pages build on the same archive structure. They cover discovery, metrics,
technical literacy, and roadmaps. Adoption and portfolio evidence belong there
too.

## Metrics, Experiments, and Success Criteria

The archive repeatedly ties data product management to measurable success.
Coquillo's template moves from problems to solutions to metrics, then adds
SMART goals and operational measures. Those measures include pipeline failures,
SLAs, and data quality
([47:18-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Mesionis makes metrics part of the Definition of Done. The team defines KPIs,
success criteria, fail-fast checks, and feasibility. Baseline comparisons,
pilots, and A/B tests happen before the product is complete. Rollout and
feedback loops happen there too
([17:37-27:25]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

When the product changes a customer or product workflow, success often needs
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
Moorman's A/B testing reporting example makes the product point clear:
decision-makers need interpretation and a usable choice, not only statistical
output
([28:42-32:25]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Vin Vashishta]({{ '/people/vinvashishta/' | relative_url }}) adds the
executive metric layer for ML products in
[Monetizing Machine Learning]({{ '/podcasts/make-money-with-machine-learning-roles-skills/' | relative_url }}).
He translates model work into revenue, cost savings, ARR, and MRR. He also ties
ML products to ROI, usage, task time, and decision quality. Pricing impact
belongs in the same executive view
([12:07-20:15 and 1:15:14-1:18:12]({{ '/podcasts/make-money-with-machine-learning-roles-skills/' | relative_url }})).

## Adoption and Operating Ownership

Adoption is part of the product boundary because the archive treats unused data
outputs as unfinished products. Moorman recommends starting from the decision
and designing for personas. She also recommends embedding metrics in meetings,
prototyping quickly, and scoping narrow wins. Those narrow wins build advocacy
([32:25-47:30]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Menefee adds documentation-first adoption work. PRDs, customer notes, and
knowledge bases teach users how to trust new data tools. Pairing and Slack help
support adoption in daily work
([46:01-56:08]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Jolly adds release governance and rollout strategy for ML products. Validation,
quality assurance, and platform stability belong there too
([31:28-37:48 and 57:20-59:52]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
Mesionis keeps demos and stakeholder feedback inside the same operating model.
Monitoring and MLOps capability stay there too
([27:25-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

That operating boundary connects data product management to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}). The product manager
doesn't replace the people who build those systems. They keep the product
accountable to users, decisions, metrics, and trust after launch.

## Related Pages

These pages cover adjacent artifacts, roles, and operating systems:

- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Product Manager Roadmap]({{ '/roadmaps/data-product-manager-roadmap/' | relative_url }})
- [Data Product Manager Guide]({{ '/guides/data-product-manager/' | relative_url }})
- [Data Product Manager Role]({{ '/guides/data-product-manager-role/' | relative_url }})
- [Data Product Owner vs Data Product Manager]({{ '/comparisons/data-product-owner-vs-data-product-manager/' | relative_url }})
- [Product Owner vs Product Manager]({{ '/comparisons/product-owner-vs-product-manager/' | relative_url }})
- [ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }})
