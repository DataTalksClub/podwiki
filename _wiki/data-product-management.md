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
dashboards, metrics, and event streams. It also covers models and ML platforms.
The DataTalks.Club discussions define the role by the decision boundary it
owns. A data product manager clarifies the user problem, chooses the outcome,
and shapes the roadmap. They coordinate delivery and prove that the product
changes a decision or workflow.

The topic sits next to [Data Products]({{ '/wiki/data-products/' | relative_url }}),
which covers the artifact, and
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
which covers whether people trust and use the work. It also overlaps with
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
when a data product changes customer behavior. Internal technical products put
the role near [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}).

[Sara Menefee](https://datatalks.club/people/saramenefee.html) gives the clearest
transition example in
[Product Designer to Data Product Manager]({{ '/wiki/product-designer-to-data-product-manager/' | relative_url }}).
She frames data product management as regular product work with data-specific
literacy.

Product teams still do customer discovery and hypothesis formation before
planning with engineering. Launch work requires SQL and data quality judgment,
plus PII awareness, compliance literacy, and documentation habits
([7:04-26:33](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).

[Greg Coquillo](https://datatalks.club/people/gregcoquillo.html) gives the roadmap
version in
[Building and Scaling AI Data Products with MLOps](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html).
Customer needs and pain points come first. Roadmap tradeoffs and measurable
business value come next
([6:41-14:03](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

## Problem-First Product Work

Data product management starts before anyone picks a technical solution.
Menefee's transition episode puts user research and customer development before
engineering. The team talks to users, learns what they're responsible for, and
forms a hypothesis about the problem before planning delivery
([4:58-16:26 and 7:04-15:10](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).

Coquillo applies the same rule to AI products. His team maps the customer
journey and learns the domain. They interview stakeholders, review
documentation, use the Five Whys, and test hypotheses before making roadmap
commitments
([14:03-35:34](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

His manufacturing example shows a multi-team internal product. The team built
curated pipelines and dashboards that helped sales build contracts faster.
Marketing and finance used the same product. Supply chain and program teams
used it too.

It combined routing and capacity data with demand signals, plus pricing,
competitor, and marketing data
([4:24-7:13](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

[Caitlin Moorman](https://datatalks.club/people/caitlinmoorman.html) extends
discovery into adoption in
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html).
Poor usage may mean people don't know the data product exists, don't understand
it, or don't trust it. They may also miss how it fits the decision they need to
make
([24:13-34:00](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).
For data product managers, user research belongs inside
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
not only before kickoff.

[Anna Hannemann](https://datatalks.club/people/annahannemann.html) ties problem
framing to [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }}) in
[Product Owners in Data Science](https://datatalks.club/podcast/building-data-products-product-owner-vs-product-manager.html).
Her operations examples show that the right product choice may be a manual
cleanup, an MVP, or staged investment rather than a model
([44:48-53:09](https://datatalks.club/podcast/building-data-products-product-owner-vs-product-manager.html)).

## Role Boundaries

Data product management sits beside
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[Data Science]({{ '/wiki/data-science/' | relative_url }}), and product
analytics. The PM decides which user problem matters, which interface should
exist, which adoption path is credible, and which metric proves the work
changed a decision.

Menefee shows that boundary through discovery, planning, and launch. Data
quality and documentation also belong in the role
([7:04-28:30](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).

[Geo Jolly](https://datatalks.club/people/geojolly.html) shows it through
[ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }})
work. The PM defines the problem, balances stakeholders, manages rollout, and
measures platform impact. Technical leads design the solution
([16:44-29:08](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html)).
Jolly warns against starting from a favorite solution before the team validates
the user problem
([16:44-21:06](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html)).

Coquillo makes the same split from the data-team side. Data professionals bring
technical input and T-shirt sizing into roadmap work, while the team still works
backward from the business problem
([26:25-35:34](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).
He also describes teams without a dedicated PM. They still need to identify the
customer and validate the work. They also need to align their mental models so
they make product decisions instead of only technical decisions
([55:32-58:42](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

Hannemann draws the clearest title boundary. A product owner often protects
delivery teams and makes tactical release tradeoffs. A product manager may own
broader strategy. A domain owner may align data science work across product and
business areas
([15:11-22:08](https://datatalks.club/podcast/building-data-products-product-owner-vs-product-manager.html)).
The dedicated comparisons are
[Data Product Owner vs Data Product Manager]({{ '/wiki/data-product-owner-vs-data-product-manager/' | relative_url }})
and
[Product Owner vs Product Manager]({{ '/wiki/product-owner-vs-product-manager/' | relative_url }}).

## Centers of Gravity

Menefee centers the role on discovery, empathy, data literacy, and execution.
Her data product manager asks how people make decisions. The role stays close
enough to SQL and data quality to make delivery credible. It treats PII,
compliance, and documentation as part of the job
([19:38-26:33 and 46:01-56:08](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).

Coquillo centers the role on roadmap discipline for AI and MLOps work. His
roadmap ranks opportunities by impact, effort, and cost. It then moves from
problems to solutions to metrics. SMART goals and pipeline failures are success
measures, not afterthoughts. SLAs and data quality matter too
([41:44-55:32](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

Jolly centers the role on internal platform adoption. He treats data
scientists, analysts, and other platform users as customers. Feedback loops,
productivity costs, backlog prioritization, and observability KPIs help him
manage the platform as a product. Release governance and rollout timing matter
too
([11:24-37:48](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html)).
That platform version sits close to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).

[Ioannis Mesionis](https://datatalks.club/people/ioannismesionis.html) shows the
same product boundary inside a lead data scientist role in
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html).
Intake, Definition of Done, KPIs, and feasibility checks structure the work.
Pilots, demos, and stakeholder communication turn data science work into a
managed product lifecycle
([14:00-38:17](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html)).

## Roadmaps and Tradeoffs

Roadmaps in data product management are evidence and tradeoff documents, not
lists of possible models. Coquillo asks for technical input and T-shirt sizing.
He uses problem-first feature design and ranks longer-term MLOps investments by
impact, effort, and cost
([28:53-47:18](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

Jolly adds the internal platform version. Backlog grooming and engineering
partnership have to balance adoption and quality. User feedback, governance,
and stakeholder value matter too
([15:19-23:28 and 31:28-37:48](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html)).

The [Data Product Manager Roadmap]({{ '/wiki/data-product-manager-roadmap/' | relative_url }})
uses these responsibilities as a learning path, while the
[Data Product Manager]({{ '/wiki/data-product-manager/' | relative_url }})
guide focuses on the role. It covers discovery, metrics, technical literacy,
and roadmaps. It also covers adoption and portfolio evidence.

## Metrics and Experiments

Data product managers need measurable success criteria. Coquillo's template
moves from problems to solutions to metrics, then adds SMART goals and
operational measures such as pipeline failures, SLAs, and data quality
([47:18-55:32](https://datatalks.club/podcast/building-and-scaling-ai-data-products-with-mlops.html)).

Mesionis makes metrics part of the Definition of Done. His teams define KPIs,
success criteria, fail-fast checks, and feasibility. They then use baseline
comparisons, pilots, and A/B tests before treating the product as complete
([17:37-27:25](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html)).
The broader lifecycle includes rollout, monitoring, demos, and stakeholder
feedback
([14:00-41:33](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html)).

When a data product changes a customer or product workflow, success often needs
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}), and causal thinking.
In Moorman's A/B testing reporting example, decision-makers need interpretation
and a usable choice, not only statistical output
([28:42-32:25](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).

[Vin Vashishta](https://datatalks.club/people/vinvashishta.html) adds the
executive metric layer for ML products in
[Monetizing Machine Learning](https://datatalks.club/podcast/make-money-with-machine-learning-roles-skills.html).
He translates model work into revenue, cost savings, ARR, and MRR. ROI and
usage belong in the same executive view. Task time, decision quality, and
pricing impact matter there too
([12:07-20:15 and 1:15:14-1:18:12](https://datatalks.club/podcast/make-money-with-machine-learning-roles-skills.html)).

## Adoption and Operating Ownership

Adoption belongs inside the product boundary because unused data outputs are
unfinished products. Moorman recommends starting from the decision and designing
for personas. She embeds metrics in meetings, prototypes quickly, and scopes
narrow wins that create advocates
([32:25-47:30](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).
She also argues that adoption depends on discoverability, interpretability,
trust, and data quality. The meeting or workflow where the decision is made
matters too
([24:13-40:53](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).

Menefee adds documentation-first adoption work. PRDs, customer notes, and
knowledge bases teach people how to trust new data tools, while pairing and
Slack support adoption in daily work
([46:01-56:08](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).

Jolly adds release governance and rollout strategy for ML products. Validation
and quality assurance matter for internal platform users. Platform stability and
rollout timing matter too
([31:28-37:48 and 57:20-59:52](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html)).
Mesionis keeps monitoring and MLOps capability in the same operating model as
demos and stakeholder feedback
([27:25-41:33](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html)).

This operating ownership puts data product management near
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}). The product manager
doesn't replace the people who build those systems. They keep the product
accountable to users, decisions, metrics, and trust after launch.
