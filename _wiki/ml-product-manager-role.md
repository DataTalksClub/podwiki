---
layout: wiki
title: "ML Product Manager Role"
summary: "How DataTalks.Club guests define the technical product manager role for ML platforms and ML-enabled data products."
related:
  - Data Product Management
  - ML Platforms
  - MLOps
  - Platform Adoption
  - Data Teams
---

An ML product manager owns product judgment for machine-learning systems,
ML-enabled data products, or shared ML platforms. DataTalks.Club guests don't treat
the role as a backlog secretary for data scientists. It's the
person who turns a business or user problem into a roadmap. They align
technical and non-technical stakeholders and keep model, data, and platform
work tied to measurable outcomes.

The role is narrower than
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
when the product doesn't involve ML. It's broader than
[MLOps]({{ '/wiki/mlops/' | relative_url }}) when the work includes discovery,
prioritization, rollout, and adoption. The role often sits on top of
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
[Data Products]({{ '/wiki/data-products/' | relative_url }}). Internal data
scientists, ML engineers, analysts, or business teams may be the users.

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) gives the clearest role
definition in
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }}).
He describes a technical PM responsible for ML platform strategy, stakeholder
requirements, roadmap decisions, and adoption. Observability and release
governance also sit in that role.

[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) broadens the role
in
[Building and Scaling AI Data Products with MLOps]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})
by treating AI data products as customer-facing or internal products. Those
products need research, prioritization, SMART goals, and operational metrics.

[Sara Menefee]({{ '/people/saramenefee/' | relative_url }}) adds the
data-product transition path in
[Product Designer to Data Product Manager]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}).
The PM still practices discovery and launch discipline. They also need SQL,
data quality judgment, documentation habits, and enough lifecycle knowledge to
ask better technical questions.

## Product Ownership for ML Work

Across these episodes, guests converge on one definition. An ML product manager
is a product manager for model-backed or ML-platform work. They own the user
problem, prioritization logic, and measurement plan. Engineers and data
scientists still own technical implementation, but the PM decides which problem
matters and how the organization will know the solution worked.

Geo's platform example makes the internal-user version explicit. His ML platform
served more than one hundred users, including data scientists and business data
engineers. He treats those internal users as customers. Their requirements,
adoption constraints, and productivity costs belong in the roadmap
([ML platform users and adoption constraints at 11:24-18:25]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That makes the role close to
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}):
the product is successful only when teams can actually use it.

Greg gives the AI data-product version. He starts with customer needs and
domain knowledge before committing to a roadmap. Interviews and documentation
review help define the problem. So does the Five Whys.

His roadmap then moves from problems to possible solutions to metrics. Impact,
effort, and cost help choose what comes next
([AI data product discovery and roadmap metrics at 14:03-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

ML product management therefore sits close to
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
because the product may be a model or dashboard. It may also be a workflow,
platform capability, or data-quality improvement.

Sara's episode shows why the product part can't be skipped. A data-focused PM
still does customer discovery and forms hypotheses. They plan with engineering
and launch. Data quality, PII, and compliance make those steps credible. SQL
and data lifecycle knowledge matter too
([data product manager discovery and technical fluency at 7:04-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

## Platform PM, AI Product PM, and Data PM Variants

Guests differ less on the need for technical literacy and more on the
center of gravity. Geo centers the role on internal ML platforms. His ML product
manager writes specs and balances stakeholder requirements. They also groom the
backlog with engineering, resist solution bias, and manage rollout governance
([ML platform roadmap and release governance at 9:50-21:06 and 31:28-35:18]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That platform-centered version looks like product management for
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}), deployment
paths, and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

Greg centers the role on business-value roadmaps for AI and data products.
Customer research and product sense get more weight. So do manual-workflow
discovery, MLOps prioritization, and SMART goals. SLAs, data quality, and
pipeline failures also matter
([AI data product research prioritization and metrics at 23:20-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
In that version, the ML product manager may look like a
[data product manager]({{ '/wiki/data-product-manager/' | relative_url }})
who works on AI capabilities.

Sara centers the role on product craft and transition skills. Her version is
less platform-specific. It's more about becoming fluent enough in data to guide
discovery and launch work. That fluency also supports documentation and
stakeholder education
([data PM fluency documentation and stakeholder education at 19:38-28:30 and 51:55-58:24]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).
This is useful for teams where the ML PM title doesn't exist, but a product
manager still has to make data and ML tradeoffs.

## Data Product Manager Boundary

The boundary with a data product manager is scope, not craft. Both roles use
discovery, prioritization, and roadmaps. Both also rely on metrics and adoption
work.

A data product manager can own dashboards, datasets, and events. They may also
own analytical workflows or data platforms. An ML product manager owns the
subset where machine learning changes the product surface, operating risk, or
platform dependency.

Greg's discussion sits on the boundary. He uses the data product manager frame
for AI products because the work still starts with customers and business
problems. The roadmap can still include MLOps, scaling strategies, and
unscalable manual workflows that should become model-assisted workflows
([AI data product roadmap tradeoffs at 35:34-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
That's why this role belongs next to both
[Data Products]({{ '/wiki/data-products/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}).

Sara shows the broader data PM skill floor. Data quality, PII, SQL, and
documentation matter even before a team introduces a model. Lifecycle awareness
matters too
([data PM skill floor and data lifecycle at 19:38-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Geo's episode adds the ML-specific layer through model architectures and data
infrastructure. Cloud concepts, CI/CD, and Kubernetes become relevant too.
For an ML platform or model-backed capability, validation matters. Shadowing and
release checklists matter too
([ML PM technical knowledge and validation at 23:28-25:31 and 57:20]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Use the ML product manager label when the PM must reason about model lifecycle,
platform adoption, or ML quality gates. The label also fits tradeoffs among
model work, platform work, and data-quality work. Use the data product manager
label when the product is primarily a data capability and ML is optional or
downstream.

## ML Engineer Boundary

The boundary with a
[Machine Learning Engineer]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
is ownership of the solution path. The ML product manager defines the user
problem, desired outcome, and roadmap priority. They also define the rollout
plan and measurement system.

The ML engineer turns model work into reliable software. That can mean training
and inference code, services or batch jobs, and deployment paths. It can also
mean monitoring hooks and operational behavior.

Geo draws this line when he separates the technical ML product manager from data
science lead or staff engineering work. The PM coordinates cross-team
requirements, adoption, and roadmap tradeoffs. Engineers own backend systems,
systems engineering, CI/CD, and Kubernetes. They also own platform
implementation details
([ML PM and engineering ownership boundaries at 28:37-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

That boundary still requires technical credibility. Geo argues that ML platform
PMs need enough familiarity with model architectures and data infrastructure.
Cloud concepts and tooling also help them communicate with engineers and avoid
naive roadmap decisions
([ML platform technical credibility at 23:28-25:31]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
The PM doesn't replace the ML engineer. They should still understand enough of
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[Production]({{ '/wiki/production/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
to make tradeoffs visible.

## Product Manager Boundary

An ML product manager is still a product manager. Geo and Greg show that the
distinction isn't that ordinary product managers own users while ML product
managers own technology. They both start from the user problem and the business
outcome. ML changes the feasibility, reliability, measurement, and adoption
questions the PM has to manage.

For a conventional product manager, the hardest question may be which customer
problem to solve or which feature to launch. For an ML product manager, the same
question can depend on data availability, model quality, and serving
constraints. Platform readiness, governance approvals, and user trust can also
influence the decision.
Geo's release-governance and adoption sections make those extra constraints
visible
([ML platform release governance and adoption at 31:28-37:48]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Greg's roadmap template also keeps the product-manager boundary clear. The PM
starts with the business problem, not with "build a model." They consider
customer pain, impact, and effort. Cost and metric belong in the same decision.
A model, pipeline, platform investment, or manual workflow improvement may be
the right next step
([AI data product roadmap decisions at 31:45-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

[Data Product Manager vs Product Manager]({{ '/wiki/data-product-manager-vs-product-manager/' | relative_url }})
and
[Product Owner vs Product Manager]({{ '/wiki/product-owner-vs-product-manager/' | relative_url }})
separate the title boundaries.

## Roadmaps and Backlog Decisions

ML product managers turn technical possibilities into a sequence the team can
execute. Geo describes roadmap ownership, specs, and stakeholder balancing. He
also covers backlog grooming with engineers and problem breakdown through
workshops and interviews
([ML platform roadmap ownership and problem breakdown at 9:50-21:06]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
A PM should avoid jumping from a stakeholder request directly to a technical
solution.

Greg turns the same idea into a roadmap structure built around problems and
possible solutions. Metrics and impact come next. He also adds effort, cost,
and time horizon before the team compares options. A technical roadmap may
standardize the platform. A scaling roadmap may turn manual operational work
into a reliable data or ML workflow
([AI data product scaling roadmap at 35:34-47:18]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Roadmap quality depends on the engineers, data scientists, analysts, and
business owners in
[Data Teams]({{ '/wiki/data-teams/' | relative_url }}). Each group affects
what's feasible and useful. Governance stakeholders may also influence the
roadmap. The PM's job is to make those constraints explicit without letting one
stakeholder dictate the whole product direction.

## Adoption, Quality, and Governance

ML product work isn't finished when a model or platform feature ships. Geo
frames adoption as a product problem for internal platforms. The PM has to know
which teams will adopt the capability and when rollout timing creates value.
They also need to understand how users experience the platform
([ML platform adoption and user experience at 35:18-40:14]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
In Geo's example, embedded data scientists can act as power users, internal
advocates, and demo partners for the platform.

Quality and governance are also product concerns. Geo discusses observability
metrics for platform impact and governance approvals. Model validation belongs
in the same release conversation. So do shadowing and release checklists
([ML platform observability governance and release checks at 18:25 and 31:28-57:20]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Greg adds SMART goals and service-level expectations. Pipeline failures and data
quality measures also matter for internal data platforms
([AI data product SMART goals and data quality metrics at 51:11-55:32]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
Sara adds compliance and documentation. She also puts PII and stakeholder
education upstream in product-management responsibilities
([data PM compliance education and documentation at 19:38-24:30 and 51:55-56:08]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Together, the episodes treat quality as a product boundary, not only an
engineering checklist. The ML PM should know when the product risk is model
drift, data freshness, or governance approval. User misunderstanding and lack
of trust can be product risks too. That's why the role links naturally to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).

## Transition Paths

People enter the role from data science, product design, product management, or
technical program work. Each path leaves a different gap. Geo moved from web
development through data science into product management. He recommends building
communication, prioritization, and roadmap literacy. Backlog and ML-platform
literacy matter too
([Geo Jolly's path into ML product management at 1:56-6:28 and 44:56-59:52]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Sara shows the product-design path. User research and empathy transfer well from
design work, as does case-study framing. SQL and data lifecycle knowledge need
deliberate practice. Documentation fluency and data-quality judgment need
practice too
([product designer to data product manager transition at 28:30-39:04]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Greg's episode is useful for data professionals without a formal PM title. They
can still identify customers and validate needs. They can also align mental
models inside the team
([AI data PM practice without the title at 55:32-58:42]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).
