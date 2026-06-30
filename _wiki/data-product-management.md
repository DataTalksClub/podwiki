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

Data product management is product management applied to data capabilities such
as dashboards and ML systems. It also covers metric layers, event streams, and
MLOps platforms. In the DataTalks.Club archive, the role is defined less by the
title than by the boundary it owns. The data product manager clarifies the user
problem and chooses the outcome. They also plan the roadmap, coordinate
delivery, and prove that the data product changes a decision or workflow.

[Sara Menefee]({{ '/people/saramenefee/' | relative_url }})
anchors the discovery side in her episode on moving from design into
[data product management]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}).
[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) anchors the
roadmap and metrics side in
[Build & Scale Data Products for AI]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }}).

This topic covers the concept and role boundary. Use
[Data Products]({{ '/wiki/data-products/' | relative_url }}) for the artifact,
and use [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
for the last-mile adoption problem. Use
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) for usage
and experimentation work. Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
or [MLOps]({{ '/wiki/mlops/' | relative_url }}) when the product is an internal
technical platform.

## Definition

A data product manager owns the product judgment around a data capability. That
means deciding which user problem matters and what interface should exist. They
also decide which metric proves success and which constraints apply.

Menefee describes the role as normal product
management with data-specific context. Customer discovery and hypothesis
formation come first. Planning and engineering partnership follow. Launch and
data quality also belong in the role. So do PII, compliance, SQL, and
documentation literacy
([7:04-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

The archive also treats data product management as a coordination role across
business and technical teams. [Geo
Jolly]({{ '/people/geojolly/' | relative_url }}) describes a technical product
manager for an internal ML platform. That PM owns roadmap direction,
specifications, and backlog prioritization. User feedback and stakeholder
communication also sit with the PM
([6:28-16:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
[Anna Hannemann]({{ '/people/annahannemann/' | relative_url }}) gives the
domain-owner version.

The product leader sits between stakeholders and technical teams. They decide
whether a recommender, markdown model, MVP, or manual fix is the right response
([15:11-21:45 and 44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

## Link Map

Start with these podcast discussions:

- [Sara Menefee on transitioning from product design to data product management]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})
  covers customer discovery plus execution details for quality and
  documentation.
- [Greg Coquillo on building and scaling AI data products]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})
  covers research methods and problem-first roadmaps for AI product work.
- [Geo Jolly on ML product management and MLOps platform strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
  frames internal platform users as customers. He ties PM work to roadmaps,
  observability KPIs, release governance, and rollout timing. Adoption and
  technical literacy are part of the same role.
- [Anna Hannemann on product owners, product managers, and domain ownership]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})
  separates role titles through recommenders and production ML examples.
- [Ioannis Mesionis on data product intake and A/B testing]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})
  gives an operating model for intake, KPIs, pilots and monitoring.
- [Caitlin Moorman on last-mile data delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
  keeps the role focused on adoption. Users must discover the data product,
  understand it, trust it, and use it in a real decision.
- [Zhamak Dehghani on Data Mesh]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})
  defines domain-owned products through contracts, guarantees, platforms, and
  governance.
- [Vin Vashishta on monetizing machine learning]({{ '/podcasts/make-money-with-machine-learning-roles-skills/' | relative_url }})
  adds the revenue boundary through ARR, ROI, and adoption metrics.

Guest pages:

- [Sara Menefee]({{ '/people/saramenefee/' | relative_url }})
- [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }})
- [Geo Jolly]({{ '/people/geojolly/' | relative_url }})
- [Anna Hannemann]({{ '/people/annahannemann/' | relative_url }})
- [Ioannis Mesionis]({{ '/people/ioannismesionis/' | relative_url }})
- [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
- [Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }})
- [Vin Vashishta]({{ '/people/vinvashishta/' | relative_url }})

Adjacent wiki and article pages:

- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Product Manager]({{ '/guides/data-product-manager/' | relative_url }})
- [Data Product Manager Role]({{ '/guides/data-product-manager-role/' | relative_url }})
- [Product Owner vs Product Manager]({{ '/comparisons/product-owner-vs-product-manager/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})

## Common Definition

Across the archive, data product management starts before a technical solution
is chosen. Menefee starts with product discovery. The team talks to users,
forms a hypothesis about their problem, and validates the problem before moving
into planning and engineering
([7:04-15:10]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo uses the same problem-first rule for AI products. Customer journey
mapping and domain knowledge come before roadmap commitments. Interviews,
documentation, the Five Whys, and hypothesis testing come before them too
([14:03-26:25]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

The common role boundary is ownership of the why and the what. The PM doesn't
own every technical detail. Jolly says the PM should define the problem and
target outcome. Technical leads design the solution.
He warns against starting from a favorite solution before validating the user
problem
([16:44-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Coquillo gives a similar split. Data professionals contribute technical input
and T-shirt sizing to roadmaps. The team still works backward from the business
problem
([26:25-35:34]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

The product isn't complete when the table, dashboard, model, or platform
feature ships. Moorman's last-mile episode says adoption depends on
discoverability, interpretability, trust, and data quality. It also depends on
the meeting or workflow where the decision is made
([24:13-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Mesionis turns that into an operating model. Intake and Definition of Done come
first, then KPI work adds feasibility checks. Pilots, A/B tests, rollout, and
monitoring are part of the same lifecycle
([14:00-28:18 and 35:38-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

## Guest Differences

Guests differ most in the center of gravity they give the role. Menefee centers
it on discovery, empathy, data literacy, and execution. Her data product
manager asks how users make decisions. The role also requires PII judgment,
enough SQL to look at data, and adoption documentation
([19:38-26:33 and 46:01-56:08]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo centers the role on roadmap discipline for AI and MLOps work. His
roadmap framing ranks product opportunities by impact, effort, and cost. His
template moves from problems to solutions to metrics. His success metrics
include SMART goals, operational metrics, and pipeline failures. They also
include SLAs and data quality
([41:44-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Jolly centers the role on internal platform adoption. He treats data
scientists and analysts as customers of an ML platform. He ties product
management to user feedback, productivity costs, and backlog prioritization.
Observability KPIs, release governance, and rollout timing also sit in the role
([11:24-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That version sits close to [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).

Hannemann draws the clearest title boundary. In her examples, a product owner
often protects and guides delivery teams. A product manager may own broader
strategy. A domain owner aligns data science work across business areas
([15:11-22:08]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
Use
[Product Owner vs Product Manager]({{ '/comparisons/product-owner-vs-product-manager/' | relative_url }})
for the dedicated comparison.

Her practical examples also keep ML from becoming the default answer. An
operations problem may call for a manual cleanup, an MVP, or staged portfolio
investment instead of a model
([44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).

Dehghani differs by treating the product boundary as an architecture and
governance unit. In [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}), data
product management includes consumer-first guarantees and metadata. It also
includes discoverability, quality, and SLAs. Ownership decisions, platform
abstractions, and federated governance complete the role
([31:05-53:02]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})).

Vashishta differs by making monetization explicit for ML products. He translates
model work into revenue, cost savings, ARR, and MRR. Researchable use cases are part of the same translation. He
also covers gated investment decisions, architecture cost, and ROI. Usage,
task time, decision quality, and pricing impact are adoption metrics
([12:07-20:15 and 43:28-52:33 and 1:15:14-1:18:12]({{ '/podcasts/make-money-with-machine-learning-roles-skills/' | relative_url }})).

## Role Boundaries

Data product management is adjacent to data science and data engineering. It's
also adjacent to analytics engineering and product analytics. The role boundary
is different.

[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
builds trusted models, transformations, tests and BI-ready data
products.

[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) builds and
operates pipelines, while [Data Science]({{ '/wiki/data-science/' | relative_url }})
develops models and analytical methods.

The data product manager decides which user problem matters. They also decide
which adoption path and success metric justify the work, as shown by Menefee's
lifecycle discussion
([7:04-28:30]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}))
and Jolly's platform PM discussion
([16:44-29:08]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).


The product owner boundary is context-dependent. Hannemann describes product
owners as close to delivery teams and stakeholder translation. Product managers
may own broader strategy and portfolio responsibility
([15:11-20:00]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
In a data mesh organization, Dehghani's product owner is closer to a domain
accountability role. The owner negotiates consumer expectations and decides
which quality, SLA, and ownership guarantees the data product can make
([34:36-41:58]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})).

The role can exist without the exact title. Coquillo explicitly discusses
operating without a PM, where the team still needs to identify the customer and
validate the work. It also has to align mental models so it makes product
decisions rather than only technical decisions
([55:32-58:42]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Mesionis shows the same structure in a lead data scientist role. It appears in
intake, Definition of Done, and success criteria. It also appears in pilots and
stakeholder demos
([14:00-38:17]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

## Discovery And Problem Framing

Discovery is the first practical skill in the archive. Menefee's transition
episode puts user research and customer development before planning.
Hypothesis formation and PM-designer collaboration also come before engineering
([4:58-16:26]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Coquillo adds a more structured business-partner version. Customer journey
mapping and domain knowledge appear in his process. Interviews, documentation,
the Five Whys, and working backward from business problems appear too
([14:03-35:34]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Data teams can otherwise build the wrong thing well, so Moorman diagnoses poor
adoption as a product problem. Users may not know the data product exists, or
they may not understand it. They may also lack trust or a clear decision fit
([24:13-34:00]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).
That makes discovery part of [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
not only a pre-project ritual.

## Roadmaps, Prioritization, And Tradeoffs

Roadmaps in data product management are evidence and tradeoff documents, not
lists of possible models. Coquillo's roadmap approach asks for technical input
and T-shirt sizing. It also uses problem-first feature design. MLOps scaling
priorities and impact-effort-cost prioritization set the longer horizon
([28:53-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Jolly adds the internal platform version. It combines backlog grooming with
engineering and continuous feedback from platform users. The roadmap balances
adoption, quality, governance, and stakeholder value
([15:19-23:28 and 31:28-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

The tradeoff isn't always model versus no model. Hannemann's operations
examples show that product leadership may choose a manual fix for bad rows. It
may also choose an MVP or a staged investment across several data product
opportunities
([44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
That boundary connects data product management to
[Data Strategy]({{ '/wiki/data-strategy/' | relative_url }}) and
[Data Products]({{ '/wiki/data-products/' | relative_url }}), because the
manager chooses the smallest credible path to learning and impact.

## Metrics, Experiments, And Success Criteria

The archive repeatedly ties data product management to measurable success.
Coquillo's template moves from problems to solutions to metrics, then adds
SMART goals. It also adds operational measures such as pipeline failures, SLAs,
and data quality
([47:18-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Mesionis makes metrics part of the Definition of Done. The team defines KPIs,
success criteria, fail-fast checks, and feasibility.

Pilots and A/B tests happen before the product is done. Baseline comparisons,
rollout, and feedback loops happen there too
([17:37-27:25]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

When the product changes a customer or product workflow, success often needs
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}). It may also need
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
Moorman's A/B testing reporting example says decision-makers need simpler
interpretation, not only statistical output
([28:42-32:25]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Vashishta adds the executive metric layer for ML products, including ARR and
MRR as revenue measures. Usage, task time, decision quality, and pricing impact
belong there too
([12:07-20:15 and 1:15:14-1:18:12]({{ '/podcasts/make-money-with-machine-learning-roles-skills/' | relative_url }})).

## Adoption And Operating Ownership

Adoption is part of the product boundary because the archive treats unused data
outputs as unfinished products. Moorman recommends starting from the decision
and designing for personas. She also recommends embedding metrics in meetings,
prototyping quickly, and scoping narrow wins that build advocacy
([32:25-47:30]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Menefee adds documentation-first adoption work. PRDs, customer notes, knowledge
bases, and pairing help users learn. Slack help also supports trust in new data
tools
([46:01-56:08]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Operating ownership matters after launch. Jolly's ML platform example includes
release governance, rollout strategy, and adoption. It also includes model
validation, quality assurance, and platform stability
([31:28-37:48 and 1:48:17-1:56:09]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Mesionis similarly keeps demos and stakeholder feedback inside the product
operating model. Monitoring and MLOps capabilities stay there too
([27:25-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).
That connects data product management to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}).

## Related Pages

Use these pages for the adjacent artifacts, roles, and operating systems:

- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Product Designer to Data Product Manager]({{ '/wiki/product-designer-to-data-product-manager/' | relative_url }})
- [Data Product Manager]({{ '/guides/data-product-manager/' | relative_url }})
- [Data Product Manager Role]({{ '/guides/data-product-manager-role/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
