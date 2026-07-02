---
layout: wiki
title: "Data Engineering Platforms"
summary: "How DataTalks.Club guests define data engineering platforms: shared ingestion, storage, orchestration, modeling, governance, self-service, reliability, adoption, and cost control."
related:
  - Data Engineering
  - DataOps Platforms
  - Self-Service Data Platforms
  - DataOps
  - Modern Data Stack
  - Data Products
  - Data Governance
  - Data Quality and Observability
---

Data engineering platforms are the shared systems and team practices that move
data from source systems into reliable analytical uses. They also support
machine learning and operational workflows. DataTalks.Club guests describe the
platform as broader than a warehouse or scheduler. It combines ingestion,
storage, compute, and workflow coordination. Access, monitoring, governance,
and support practices belong there too.

[[person:larsalbertsson|Lars Albertsson]] starts from
storage, compute, and workflow engines in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
He then connects those primitives to reproducibility and self-service.
[[person:nataliekwong|Natalie Kwong]] maps the modern
stack version through extraction, loading, transformation, and orchestration in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]].
She also brings CDC and reverse data flows into the same discussion.

The platform question is which capabilities belong in the shared foundation,
where teams draw ownership boundaries, and how adoption changes the
architecture. Use
[[Data Engineering]] for the
broader discipline. Use [[DataOps]] and
[[DataOps Platforms]] for the
operating model. Use
[[self-service-data-platforms|Self-Service Data Platforms]]
for the enablement subset.

## Shared Platform Foundation

A data engineering platform gives teams a reusable foundation for producing and
consuming data. [[person:larsalbertsson|Lars Albertsson]]
breaks the foundation into storage, compute, and workflow engines. He connects
those primitives to self-service analytics, reproducible pipelines, and lineage
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
16:42-35:57 and 50:13-1:04:18).

[[person:nataliekwong|Natalie Kwong]]
describes the same platform from the modern-stack side. Extraction and loading
come before warehouse transformation. Natalie also covers data marts and lakes.
She then places orchestration and CDC in the same platform map. Schema
evolution and reverse flows appear there too
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
3:46-49:32).

[[person:mehdiouazza|Mehdi OUAZZA]] treats the
platform as an organizational product for self-service and onboarding during
hypergrowth. Teams reuse Airflow conventions and playbooks. In streaming work,
they also reuse Kafka schemas and schema registries. Contracts make the
interface explicit
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]],
12:30-23:26).

[[person:caitlinmoorman|Caitlin Moorman]]
adds that a modern stack isn't valuable unless the last mile makes data
trusted and discoverable. It must also be interpretable and tied to decisions
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]],
8:48-34:00).

In practice, a data engineering platform is the shared technical and social
layer that moves data from source systems into governed, observable, usable
data products. The topic sits between [[Data Pipelines]],
[[DataOps]], [[Data Products]],
and [[Data Governance]].

## Ownership and Tooling Tradeoffs

Platform designs differ most on where ownership should sit. [Zhamak
Dehghani](https://datatalks.club/people/zhamakdehghani.html) argues for
domain-owned data products with contracts and quality guarantees. Her platform
boundary also includes metadata and identity. Authorization, self-serve
abstractions, and federated governance sit in the same design
([[podcast:data-mesh-architecture-decentralized-data-products|Data Mesh Implementation]],
13:20-53:02).

[[person:larsalbertsson|Lars Albertsson]]
is more cautious about splitting responsibilities too early. His DataOps
discussion asks when decentralization creates governance risks and
reproducibility risks
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
57:46-1:04:18). Use
[[Data Mesh vs Centralized Data Platform]]
for that ownership comparison.

Teams also need to decide how much infrastructure to buy or build.
[[person:nataliekwong|Natalie Kwong]] explains the
best-of-breed modern analytics stack through connectors, dbt, and warehouses.
She also places Airflow and reverse ETL in the stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
30:59-35:42).

[[person:adrianbrudaru|Adrian Brudaru]] pushes back
from a newer open-source and cost-aware view. He discusses Iceberg and DuckDB.
He also discusses catalogs and SQLMesh. Simpler orchestration can fit when the
requirements support it
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
14:32-35:37 and 44:42-51:19).

[[person:slawomirtulski|Slawomir Tulski]]
adds the career and hiring version of the same warning. Teams should avoid
over-engineered platforms and avoid treating real-time tools as proof of
maturity
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
25:33-38:01).

The practical synthesis isn't a binary choice. The platform decision depends on
ownership and latency, but it also depends on cost, governance, and adoption.
Those requirements appear in specific episodes rather than in tool labels
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]],
52:55 and
[[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
31:40-48:01).

## Platform Capabilities

A platform normally starts with reliable movement from sources into a durable
analytical store. [[person:nataliekwong|Natalie Kwong]]
uses ETL and ELT to explain the boundary. Extraction and loading bring source
data into a warehouse or lake. Transformations produce modeled layers,
downstream data marts, and other outputs
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
3:46-18:47). The same platform boundary explains why
[[ELT]],
[[Data Warehouse]], and
[[Data Lake]] decisions affect shared
data engineering work.

Storage choices become platform choices when multiple consumers depend on the
same data. [[person:larsalbertsson|Lars Albertsson]]
contrasts raw data lakes with warehouse use cases. He also discusses object
storage, governance, and aggregates. Lakehouse architecture appears in the same
discussion
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
21:29-30:34 and 1:07:52).

[[book:20210308-designing-data-intensive-applications|Designing Data-Intensive Applications]]
by Martin Kleppmann grounds these same storage and platform tradeoffs in the
underlying distributed-systems principles.

[[person:adrianbrudaru|Adrian Brudaru]]
updates that discussion with Iceberg and Delta Lake. He also covers catalogs,
metadata, and lineage. Headless table formats are part of the same update
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
18:17-30:31 and 49:42). Use
[[Data Warehouse vs Data Lakehouse]]
and [[Apache Iceberg]] for those
storage patterns.

Orchestration becomes a platform capability when it coordinates clear
responsibilities. [[person:nataliekwong|Natalie Kwong]]
places Airflow at the scheduling layer beside Airbyte-style ingestion and
dbt-style transformation
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
30:59-33:45). [[person:adrianbrudaru|Adrian Brudaru]]
later compares Airflow, Prefect, Dagster, and GitHub Actions. He treats
them as workflow choices, not as universal platform requirements
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
35:37). Use [[Orchestration]] and
[[Apache Airflow]] for the
tool-specific boundary.

## Self-Service, Contracts, and Data Products

Self-service is the clearest recurring platform outcome. [Mehdi
OUAZZA](https://datatalks.club/people/mehdiouazza.html) describes a platform that
helps other teams onboard and build with less bespoke support. He pairs that
with Airflow conventions and playbooks. For streaming work, he adds Kafka
schemas and schema registries. Data contracts make the interface explicit
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]],
12:30-23:26).

This is why self-service belongs with
[[self-service-data-platforms|Self-Service Data Platforms]]
and [[Data Governance]], not only
with tool installation.

[[person:zhamakdehghani|Zhamak Dehghani]] makes the
interface more explicit by calling data a product. In her episode, useful data
products need consumer-first guarantees and ownership decisions. They also need
quality, SLAs, contracts, and metadata. Identity, authorization, and automated
governance are part of the same interface
([[podcast:data-mesh-architecture-decentralized-data-products|Data Mesh Implementation]],
31:05-53:02).

A centralized platform can publish those guarantees. A Data Mesh
approach asks domains to own them on top of shared platform
capabilities
([[Data Mesh vs Centralized Data Platform]]).

[[person:caitlinmoorman|Caitlin Moorman]] provides the
adoption test for data products. A platform output isn't finished when a table
or dashboard exists. Users still need trust and discoverability. They also need
interpretability, personas, and simple abstractions. The platform output should
support better decisions
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]],
24:13-41:18).

Use [[Data Product Adoption]]
when the main question is whether people use the platform output.

## Reliability, Observability, and DataOps

Guests treat reliability as a platform responsibility because many data
failures are silent. [[person:barrmoses|Barr Moses]]
distinguishes data observability from application monitoring and names the
signals a data platform should expose. Those signals include freshness, volume,
distribution, and schema. She also covers lineage and ownership. SLAs,
root-cause context, and runbooks complete the operating view
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
9:49-43:00 and 47:00-1:00:27).

Use
[[Data Quality and Observability]]
for the monitoring layer.

[[person:larsalbertsson|Lars Albertsson]] ties
reliability back to platform design through immutable pipelines and
reproducibility. He also covers workflow engines, schema automation, and
quality practices
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
16:42-20:12 and 46:52). [[person:christopherbergh|Christopher Bergh]]
adds the delivery loop of tests, CI/CD, and observability in the DataOps
episodes. He also links DataOps to deployment confidence and recovery
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
15:52-54:05). [[DataOps]] covers that
delivery discipline in more detail.

[[person:16rahuljain|Rahul Jain]] shows what reliability
looks like from platform leadership. His platform work includes quality
metrics, reconciliation, and GDPR strategies. It also includes dynamic masking,
role-based access control, and data lineage. He closes with an end-to-end
pipeline view from ingestion through exposure and monitoring
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership and Modern Data Platforms]],
25:04-30:50 and 57:29). Platform reliability therefore includes
[[Data Governance]] controls as
well as observability.

## Batch, Streaming, and Latency

The platform should match latency to the business problem. [Mehdi
OUAZZA](https://datatalks.club/people/mehdiouazza.html) covers Kafka and schemas
in a scale-up context. Schema registries and contracts support event streaming
across teams
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]],
23:26). [[person:larsalbertsson|Lars Albertsson]] then
frames batch versus streaming as a latency and predictability tradeoff rather
than a maturity ladder
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]],
41:53-45:11).

[[person:adrianbrudaru|Adrian Brudaru]] repeats that
warning in a newer episode. He places streaming beside micro-batching and
Kafka, and he also names SQS with Flink for specific requirements
([[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
51:19). [[person:slawomirtulski|Slawomir Tulski]]
explicitly warns against the real-time myth and against over-engineered modern
data stacks
([[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
30:56-38:01). Use [[Batch vs Streaming]]
and [[Streaming]] when latency is the
main design question.

## Cost, Ownership, and Maturity

Platform cost is a design concern, not a finance afterthought. Use
[[FinOps for Data Engineers]]
for the cloud-cost, tagging, reporting, and capacity-planning layer.

[[person:eddyzulkifly|Eddy Zulkifly]] compares data
platforms to digital warehouses. He connects the modern stack to ELT, dbt,
BigQuery, and orchestration. He then links platform work to monitoring, tests,
and cost tagging
([[podcast:finops-for-data-engineers|FinOps for Data Engineers]],
21:57-48:01).

Reservations and cloud cost modeling complete the FinOps view, while standard
reporting and accountability matter too. That makes cost part of platform
ownership alongside reliability and governance.

[[person:adrianbrudaru|Adrian Brudaru]] argues for
requirements-led architecture in
[[podcast:trends-in-modern-data-engineering|Modern Data Engineering Trends]],
27:40-44:42. [[person:slawomirtulski|Slawomir Tulski]]
makes the same point in
[[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]],
25:33-38:01.

Iceberg and DuckDB can be right in context, and cloud warehouses can be right
too. Kafka and Spark can also be right when the requirements call for them.
GitHub Actions and catalogs belong in the decision. Adrian and Slawomir warn
against adopting a large platform because the tooling is popular.

Use [[DuckDB]],
[[Apache Iceberg]], and
[[Data Engineering Portfolio Projects]]
for smaller proof-oriented platform designs.

Platform maturity affects staffing because [[person:mehdiouazza|Mehdi OUAZZA]]
argues that scale-up platform work benefits from senior engineers and niche
technology experience. He also notes that teams often split time between
platform engineering and use-case pipelines
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]],
20:13 and 52:55). [[person:16rahuljain|Rahul Jain]]
adds that platform leaders need stakeholder prioritization and technical
credibility. They also need quality standards and business impact
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership and Modern Data Platforms]],
4:52-16:32 and 33:39-41:00).

## Related Pages

Use these pages for adjacent platform, governance, and delivery topics.

- [[Data Engineering]]
- [[self-service-data-platforms|Self-Service Data Platforms]]
- [[DataOps]]
- [[Modern Data Stack]]
- [[FinOps for Data Engineers]]
- [[Data Pipelines]]
- [[Data Products]]
- [[Data Product Adoption]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[Batch vs Streaming]]
- [[Data Warehouse vs Data Lakehouse]]
- [[Data Mesh vs Centralized Data Platform]]
