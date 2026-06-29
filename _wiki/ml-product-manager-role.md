---
layout: wiki
title: "ML Product Manager Role"
summary: "How the podcast archive defines the technical product manager role for ML platforms and ML-enabled data products."
related:
  - Data Product Management
  - ML Platforms
  - MLOps
  - Platform Adoption
  - Data Teams
---

The ML product manager role sits between product management, machine learning,
and platform delivery. In the DataTalks.Club archive, guests describe the role
as more than writing tickets for model teams. ML product managers define user
problems, translate between stakeholders and engineers, manage roadmaps, and
guide adoption. They also decide how technical platform work connects to
business outcomes.

Use this page for the role. Use [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
for the broader product discipline, [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
for shared systems, and [MLOps]({{ '/wiki/mlops/' | relative_url }}) for the
operating practices around model delivery.

## Link Map

The role connects to these wiki pages:

- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
- [Data Teams]({{ '/wiki/data-teams/' | relative_url }})

These podcast discussions anchor the page:

- [ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
  with [Geo Jolly]({{ '/people/geojolly/' | relative_url }}) is the core role
  episode. It covers ML platform strategy at 8:41 and PM responsibilities at
  9:50. It also covers internal platform users at 11:24, adoption at 35:18,
  and release governance at 31:28.
- [Building and Scaling AI Data Products with MLOps]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})
  with [Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) expands
  the role from platform ownership into customer research and product sense. It
  also covers roadmaps, SMART goals, data quality, and MLOps prioritization.
- [Product Designer to Data Product Manager]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})
  with [Sara Menefee]({{ '/people/saramenefee/' | relative_url }}) shows how
  customer discovery, data literacy, and SQL affect data-focused product work.
  She also connects PII/compliance awareness with stakeholder education.

## Common Definition

Across these episodes, guests treat models, data pipelines, and ML platforms as
products with users. An ML product manager is the technical PM for that work.
Geo Jolly describes an internal ML platform with more than one hundred users. He
frames data scientists, business data engineers, and other internal teams as
customers whose requirements must be prioritized
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Greg Coquillo makes the same move for AI data products. Even internal teams need
customer research, problem framing, product sense, and success metrics. They
also need roadmaps that rank work by impact, effort, and cost
([episode]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

The archive also converges on technical literacy. ML product managers don't
replace engineers or data scientists, but they need enough understanding of
models and data infrastructure. They also need context on cloud concepts,
quality checks, and lifecycle work. That knowledge makes roadmap decisions
credible.

Sara Menefee's transition story adds that a data-focused PM needs practical data
curiosity, SQL, and documentation habits. They also need a working view of how
data moves from sources through warehouses into applications
([episode]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

## Guest Emphases

Geo's episode centers on platform work. The ML PM owns a roadmap for shared
capabilities while coordinating with backend and systems engineers. They manage
rollout through adoption plans, observability metrics, and governance checks
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Greg's episode covers a broader role. Data product managers can work on
ML-enabled business products, internal data platforms, or operational workflows.
He puts more weight on customer interviews, the Five Whys, and SMART goals. He
also stresses working backwards from a business problem
([episode]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Sara's episode emphasizes product craft from design, including customer
discovery, case study structure, and empathy. She also covers education for
teams that don't yet understand data quality or compliance implications
([episode]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

The disagreement isn't about whether the role is technical. The PM can create
value through platform adoption, business-product strategy, or organization-wide
translation.

## Internal Users and Adoption

Internal users still behave like customers. Geo argues that a platform PM must understand which teams will adopt a
capability, when they can absorb it, and how rollout timing affects value. He
calls this a form of "time to stakeholders" for internal platforms
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That connects directly to [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}):
the PM's job isn't complete when a platform feature ships. It's complete when
data scientists and related teams can use it productively.

Geo also describes embedded data scientists as power users and internal
advocates for the ML platform. They test capabilities, guide other users, and
help the platform team produce tutorials and examples
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
That role differs from a public go-to-market launch, but the product management
work is similar. The PM segments users, gathers feedback, lowers friction, and
keeps communicating value.

## Roadmaps and Backlog Decisions

ML PM work is partly a filtering function. Geo describes how PMs balance
requirements from different stakeholders and write specifications. They groom a
backlog with engineers and resist solution bias until the problem and metrics
are clear
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Greg's roadmap template starts with problems, possible solutions, and metrics.
It then adds impact, effort, cost, and horizon. He also distinguishes technical
roadmaps from scaling roadmaps. That distinction matters when manual work must
become reliable ML or MLOps workflows
([episode]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

This is why the role belongs near both [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). The PM isn't merely asking
whether a model can be built. They decide whether the next investment should be
model work, platform capability, or data quality. The answer may also be
operational automation or stakeholder alignment.

## Technical Literacy Without Replacing Engineering

The archive separates technical credibility from technical ownership. Geo says
platform-specific PMs need enough knowledge of model
architectures and data infrastructure. They also need enough context on cloud
platforms and CI/CD. Kubernetes and systems work also matter when PMs
communicate with engineers
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

At the same time, he separates the PM role from data science lead or staff
engineering roles. Those roles may own a workstream. The PM drives the
cross-team roadmap and customer-facing problem definition.

Sara's episode makes the same point from a transition path. A designer moving
into data product management doesn't need to become a full data engineer, but
needs SQL and data lifecycle knowledge. They also need documentation fluency and
enough compliance awareness to ask better product questions
([episode]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).
The practical bar isn't academic ML depth. It's the ability to make product
tradeoffs without losing the technical consequences.

## Quality, Governance, and Measurement

ML product managers inherit operational responsibility because ML products fail
in production, not only in notebooks. Geo discusses observability metrics for
platform impact, model validation, shadowing, and release checklists. He also
covers approvals from governance groups when the product or domain requires
them
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).
Greg adds internal-platform success metrics such as SMART goals, pipeline
failures, service-level expectations, and data quality measures
([episode]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

Sara adds an upstream product lens. A data PM has to account for data quality,
PII, compliance, and stakeholder education. Those issues appear before a data
product becomes a reliable workflow
([episode]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Together, the episodes frame quality as a product concern, not only an
engineering concern. That makes the role adjacent to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
It also connects to [Governance]({{ '/wiki/governance/' | relative_url }}).

## Transition Paths

The role can be entered from several directions, but each path has a gap to
close. Geo moved from data science toward product management and recommends
building roadmap, backlog, communication, and prioritization skills. He pairs
those skills with ML basics
([episode]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Sara shows a product-design path where user research and case study framing are
assets. SQL, data lifecycle understanding, and technical documentation become
the missing pieces
([episode]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).
Greg's episode is useful for data professionals who lack a formal PM. He argues
that teams can still identify customers, validate needs, and practice product
thinking from their current role
([episode]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})).

## Related Pages

These pages cover the adjacent roles, systems, and operating practices:

- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
- [Data Teams]({{ '/wiki/data-teams/' | relative_url }})
