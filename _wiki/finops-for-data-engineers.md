---
layout: wiki
title: "FinOps for Data Engineers"
summary: "How data engineers use cloud cost data, tagging, usage models, and platform design to make data infrastructure spend visible and controllable."
related:
  - Data Engineering
  - Data Engineer Role
  - Modern Data Stack
  - Data Engineering Platforms
  - Data Engineering Tools
  - Data Warehouse
  - DataOps
  - Orchestration
  - Data Quality and Observability
  - Data Governance
  - Platform Engineering
  - Metrics
  - Leadership
---

FinOps for data engineers is the practice of making cloud spend visible,
explainable, and actionable inside data platforms. It isn't only a finance
reporting task. Data engineers design the pipelines and warehouses that create
the cost signal. They also own orchestration jobs, storage choices, and
dashboards.

[Eddy Zulkifly]({{ '/people/eddyzulkifly/' | relative_url }}) gives the
archive's clearest definition in
[FinOps for Data Engineers]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}).
He describes his staff data engineering work as both technical and strategic.
He builds pipelines and data quality checks, then defines unit economics and
business metrics for cloud cost decisions
([48:01]({{ '/podcasts/finops-for-data-engineers/' | relative_url }})).
That places FinOps next to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
decisions.

## Common Definition

The archive defines FinOps as cloud cost management through data engineering
work. Finance teams care about spend. Data engineers provide usage data,
tagging, and capacity plans. They also provide cloud architecture and reporting.

At
[31:40]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
Zulkifly explains the SaaS version of the problem. Servers, data centers,
regional storage, and backups all affect cost. Security requirements and
customer data isolation do too. At
[34:15]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
he connects FinOps to vendor negotiations and reserved capacity. The team needs
enough usage history to know what it can commit to before it negotiates with a
cloud provider.

The boundary becomes explicit at
[41:55]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}):
FinOps is about using cloud platforms in a cost-effective way. That includes
serverless choices, container deployment, storage tiers, and whether a team pays
for fixed capacity or usage-based services.

Other guests use the same cost lens without always using the FinOps label.
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) treats
cost awareness as senior data engineering judgment in
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).
He argues against overbuilt real-time platforms when batch or managed systems
fit the business better
([25:33-38:01]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }})).
[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) gives the AI
infrastructure version in
[AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
where cloud and on-prem GPUs become architecture choices. Teams also have to
account for distributed training and total cost of ownership.

## Data Platform Fit

FinOps matters in data platforms because cloud warehouses and managed tools can
hide cost inside normal workflow. A pipeline run or dashboard refresh may look
small alone. A transformation job, notebook, or reverse ETL sync may look small
too. Teams see the cost only when they connect usage to product areas and
teams. Business metrics make the same usage easier to interpret.

Zulkifly uses a digital warehouse analogy. In
[FinOps for Data Engineers at 22:36]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
he maps ingestion and BigQuery storage to the movement of goods through a
physical warehouse. He adds orchestrated SQL transformations and BI
consumption as warehouse operations. The analogy
continues at
[24:34]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}):
digital warehouses change faster than physical warehouses, so teams need
monitoring and tests to keep the system reliable.

That makes FinOps adjacent to [orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [data governance]({{ '/wiki/data-governance/' | relative_url }}). The same
data platform that explains freshness, lineage, and ownership can also explain
spend.

## Cost Models

Data teams need cost models before they can optimize. Zulkifly describes the
inputs at
[36:11]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}):
virtual machines create major cost. Sizing depends on expected runtime, RAM,
and storage. Operating systems, licenses, and cloud-provider discounts affect
the same decision. At
[37:53]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
he describes comparing AWS, Azure, and Google Cloud with the same requirement
set.

The cost model isn't separate from the business model. At
[27:50]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
Zulkifly describes metric trees for a FinOps team. The team identifies cost
drivers inside the data warehouse and cloud platform. It then turns vague
business requirements into data specs, metric definitions, pipeline
frequencies, and assumptions. This is where FinOps overlaps with
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
and [data product management]({{ '/wiki/data-product-management/' | relative_url }}):
the metric has to explain a decision.

In AI and ML platforms, the same modeling habit moves from warehouses to compute.
[AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})
connects cost of ownership to GPU needs, distributed training, cloud usage, and
on-prem tradeoffs. That belongs on
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) in detail,
but it reinforces the FinOps habit. Engineers need usage forecasts and
architecture options before they can make a cost decision.

## Tagging and Accountability

Cost tagging turns cloud usage into a management system. At
[40:18]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
Zulkifly explains that teams using cloud resources need accountability for the
costs they create. Tags connect virtual machines or other resources to teams,
departments, services, or product areas. Regular cost review then becomes
possible.

Tagging also creates a data engineering problem.
At [44:41]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
Zulkifly links FinOps work to ingestion and transformation. He also includes
warehousing and visualization. He mentions Open Usage Cost Specifications for reporting
across AWS, Azure, and Google Cloud. Without that
standardization, the team can end up reconciling different cloud-provider terms
instead of comparing costs cleanly.

## DataOps Boundary

FinOps and [DataOps]({{ '/wiki/dataops/' | relative_url }}) are related, but
they solve different operating problems. DataOps focuses on reliable data
delivery. FinOps focuses on cloud cost visibility and optimization. They meet
when a pipeline change affects downstream reporting, compute spend, or platform
capacity.

At
[46:17]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
the episode compares FinOps with DevOps, MLOps, and DataOps as operating
disciplines. Zulkifly agrees that FinOps mirrors some DataOps practices. CI/CD, dataset
validation, and downstream-dashboard checks help teams see whether a data change
also changes cost behavior.

That boundary is why FinOps belongs beside
[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
and [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}),
not inside them. A platform can be reliable and still too expensive. It can
also be cheap because it under-serves the business. The FinOps work is to make
that tradeoff visible.

## Engineering Responsibilities

Data engineers contribute to FinOps through usage data, metric definitions, and
architecture choices:

- They build the usage data pipeline.
- They maintain definitions for cost metrics and unit economics.
- They help platform and infrastructure teams choose architectures that fit
  usage.

In Zulkifly's role, this work includes pipeline deployment and bug fixing. It
also includes data quality maintenance, metric definitions, and data products
for FinOps users
([48:01]({{ '/podcasts/finops-for-data-engineers/' | relative_url }})).
At
[49:37]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
he describes collaboration with engineers, product owners, and infrastructure
teams. That makes FinOps a cross-functional operating concern, not a solo data
engineering dashboard.

The episode also gives a career signal. Zulkifly's path from analyst work
to data engineering shows why business context can become an engineering
advantage. The cloud skills matter, but so do metric trees, stakeholder
alignment, and translation. Data engineers need to turn cost questions into
reliable data systems
([6:20-8:18]({{ '/podcasts/finops-for-data-engineers/' | relative_url }}),
[27:50-29:16]({{ '/podcasts/finops-for-data-engineers/' | relative_url }})).

## Related Pages

Use these pages for adjacent platform, role, and governance context:

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Warehouse]({{ '/wiki/data-warehouse/' | relative_url }})
- [Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [Leadership]({{ '/wiki/leadership/' | relative_url }})
