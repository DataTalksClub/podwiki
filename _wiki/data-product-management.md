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

The topic sits next to [[Data Products]],
which covers the artifact, and
[[Data Product Adoption]],
which covers whether people trust and use the work. It also overlaps with
[[Product Analytics]],
[[a-b-testing|A/B Testing]], and
[[Experimentation and Causal Inference]]
when a data product changes customer behavior. Internal technical products put
the role near [[MLOps]],
[[Data Engineering Platforms]],
[[self-service-data-platforms|Self-Service Data Platforms]],
and [[Data Mesh]].

[[person:saramenefee|Sara Menefee]] gives the clearest
transition example in
[[Product Designer to Data Product Manager]].
She frames data product management as regular product work with data-specific
literacy.

Product teams still do customer discovery and hypothesis formation before
planning with engineering. Launch work requires SQL and data quality judgment,
plus PII awareness, compliance literacy, and documentation habits
([[podcast:product-designer-to-data-product-manager|7:04-26:33]]).

[[person:gregcoquillo|Greg Coquillo]] gives the roadmap
version in
[[podcast:building-and-scaling-ai-data-products-with-mlops|Building and Scaling AI Data Products with MLOps]].
Customer needs and pain points come first. Roadmap tradeoffs and measurable
business value come next
([[podcast:building-and-scaling-ai-data-products-with-mlops|6:41-14:03]]).

## Problem-First Product Work

Data product management starts before anyone picks a technical solution.
Menefee's transition episode puts user research and customer development before
engineering. The team talks to users, learns what they're responsible for, and
forms a hypothesis about the problem before planning delivery
([[podcast:product-designer-to-data-product-manager|4:58-16:26 and 7:04-15:10]]).

Coquillo applies the same rule to AI products. His team maps the customer
journey and learns the domain. They interview stakeholders, review
documentation, use the Five Whys, and test hypotheses before making roadmap
commitments
([[podcast:building-and-scaling-ai-data-products-with-mlops|14:03-35:34]]).

His manufacturing example shows a multi-team internal product. The team built
curated pipelines and dashboards that helped sales build contracts faster.
Marketing and finance used the same product. Supply chain and program teams
used it too.

It combined routing and capacity data with demand signals, plus pricing,
competitor, and marketing data
([[podcast:building-and-scaling-ai-data-products-with-mlops|4:24-7:13]]).

[[person:caitlinmoorman|Caitlin Moorman]] extends
discovery into adoption in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].
Poor usage may mean people don't know the data product exists, don't understand
it, or don't trust it. They may also miss how it fits the decision they need to
make
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|24:13-34:00]]).
For data product managers, user research belongs inside
[[Data Product Adoption]],
not only before kickoff.

[[person:annahannemann|Anna Hannemann]] ties problem
framing to [[Data Strategy]] in
[[podcast:building-data-products-product-owner-vs-product-manager|Product Owners in Data Science]].
Her operations examples show that the right product choice may be a manual
cleanup, an MVP, or staged investment rather than a model
([[podcast:building-data-products-product-owner-vs-product-manager|44:48-53:09]]).

## Role Boundaries

Data product management sits beside
[[Analytics Engineering]],
[[Data Engineering]],
[[Data Science]], and product
analytics. The PM decides which user problem matters, which interface should
exist, which adoption path is credible, and which metric proves the work
changed a decision.

Menefee shows that boundary through discovery, planning, and launch. Data
quality and documentation also belong in the role
([[podcast:product-designer-to-data-product-manager|7:04-28:30]]).

[[person:geojolly|Geo Jolly]] shows it through
[[ML Product Manager Role]]
work. The PM defines the problem, balances stakeholders, manages rollout, and
measures platform impact. Technical leads design the solution
([[podcast:ml-product-manager-and-mlops-platform-strategy|16:44-29:08]]).
Jolly warns against starting from a favorite solution before the team validates
the user problem
([[podcast:ml-product-manager-and-mlops-platform-strategy|16:44-21:06]]).

Coquillo makes the same split from the data-team side. Data professionals bring
technical input and T-shirt sizing into roadmap work, while the team still works
backward from the business problem
([[podcast:building-and-scaling-ai-data-products-with-mlops|26:25-35:34]]).
He also describes teams without a dedicated PM. They still need to identify the
customer and validate the work. They also need to align their mental models so
they make product decisions instead of only technical decisions
([[podcast:building-and-scaling-ai-data-products-with-mlops|55:32-58:42]]).

Hannemann draws the clearest title boundary. A product owner often protects
delivery teams and makes tactical release tradeoffs. A product manager may own
broader strategy. A domain owner may align data science work across product and
business areas
([[podcast:building-data-products-product-owner-vs-product-manager|15:11-22:08]]).
The dedicated comparisons are
[[Data Product Owner vs Data Product Manager]]
and
[[Product Owner vs Product Manager]].

## Centers of Gravity

Menefee centers the role on discovery, empathy, data literacy, and execution.
Her data product manager asks how people make decisions. The role stays close
enough to SQL and data quality to make delivery credible. It treats PII,
compliance, and documentation as part of the job
([[podcast:product-designer-to-data-product-manager|19:38-26:33 and 46:01-56:08]]).

Coquillo centers the role on roadmap discipline for AI and MLOps work. His
roadmap ranks opportunities by impact, effort, and cost. It then moves from
problems to solutions to metrics. SMART goals and pipeline failures are success
measures, not afterthoughts. SLAs and data quality matter too
([[podcast:building-and-scaling-ai-data-products-with-mlops|41:44-55:32]]).

Jolly centers the role on internal platform adoption. He treats data
scientists, analysts, and other platform users as customers. Feedback loops,
productivity costs, backlog prioritization, and observability KPIs help him
manage the platform as a product. Release governance and rollout timing matter
too
([[podcast:ml-product-manager-and-mlops-platform-strategy|11:24-37:48]]).
That platform version sits close to
[[Model Monitoring]] and
[[self-service-data-platforms|Self-Service Data Platforms]].

[[person:ioannismesionis|Ioannis Mesionis]] shows the
same product boundary inside a lead data scientist role in
[[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]].
Intake, Definition of Done, KPIs, and feasibility checks structure the work.
Pilots, demos, and stakeholder communication turn data science work into a
managed product lifecycle
([[podcast:building-data-products-lead-data-scientist|14:00-38:17]]).

## Roadmaps and Tradeoffs

Roadmaps in data product management are evidence and tradeoff documents, not
lists of possible models. Coquillo asks for technical input and T-shirt sizing.
He uses problem-first feature design and ranks longer-term MLOps investments by
impact, effort, and cost
([[podcast:building-and-scaling-ai-data-products-with-mlops|28:53-47:18]]).

Jolly adds the internal platform version. Backlog grooming and engineering
partnership have to balance adoption and quality. User feedback, governance,
and stakeholder value matter too
([[podcast:ml-product-manager-and-mlops-platform-strategy|15:19-23:28 and 31:28-37:48]]).

The [[Data Product Manager Roadmap]]
uses these responsibilities as a learning path, while the
[[Data Product Manager]]
guide focuses on the role. It covers discovery, metrics, technical literacy,
and roadmaps. It also covers adoption and portfolio evidence.

## Metrics and Experiments

Data product managers need measurable success criteria. Coquillo's template
moves from problems to solutions to metrics, then adds SMART goals and
operational measures such as pipeline failures, SLAs, and data quality
([[podcast:building-and-scaling-ai-data-products-with-mlops|47:18-55:32]]).

Mesionis makes metrics part of the Definition of Done. His teams define KPIs,
success criteria, fail-fast checks, and feasibility. They then use baseline
comparisons, pilots, and A/B tests before treating the product as complete
([[podcast:building-data-products-lead-data-scientist|17:37-27:25]]).
The broader lifecycle includes rollout, monitoring, demos, and stakeholder
feedback
([[podcast:building-data-products-lead-data-scientist|14:00-41:33]]).

When a data product changes a customer or product workflow, success often needs
[[Product Analytics]],
[[a-b-testing|A/B Testing]], and causal thinking.
In Moorman's A/B testing reporting example, decision-makers need interpretation
and a usable choice, not only statistical output
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|28:42-32:25]]).

[[person:vinvashishta|Vin Vashishta]] adds the
executive metric layer for ML products in
[[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]].
He translates model work into revenue, cost savings, ARR, and MRR. ROI and
usage belong in the same executive view. Task time, decision quality, and
pricing impact matter there too
([[podcast:make-money-with-machine-learning-roles-skills|12:07-20:15 and 1:15:14-1:18:12]]).

## Adoption and Operating Ownership

Adoption belongs inside the product boundary because unused data outputs are
unfinished products. Moorman recommends starting from the decision and designing
for personas. She embeds metrics in meetings, prototypes quickly, and scopes
narrow wins that create advocates
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|32:25-47:30]]).
She also argues that adoption depends on discoverability, interpretability,
trust, and data quality. The meeting or workflow where the decision is made
matters too
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|24:13-40:53]]).

Menefee adds documentation-first adoption work. PRDs, customer notes, and
knowledge bases teach people how to trust new data tools, while pairing and
Slack support adoption in daily work
([[podcast:product-designer-to-data-product-manager|46:01-56:08]]).

Jolly adds release governance and rollout strategy for ML products. Validation
and quality assurance matter for internal platform users. Platform stability and
rollout timing matter too
([[podcast:ml-product-manager-and-mlops-platform-strategy|31:28-37:48 and 57:20-59:52]]).
Mesionis keeps monitoring and MLOps capability in the same operating model as
demos and stakeholder feedback
([[podcast:building-data-products-lead-data-scientist|27:25-41:33]]).

This operating ownership puts data product management near
[[Data Quality and Observability]],
[[data-quality-and-observability|Data Observability]],
[[Model Monitoring]], and
[[Production]]. The product manager
doesn't replace the people who build those systems. They keep the product
accountable to users, decisions, metrics, and trust after launch.
