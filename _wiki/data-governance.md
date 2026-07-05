---
layout: wiki
title: "Data Governance"
summary: "How DataTalks.Club guests define data governance through inventory, ownership, catalogs, access controls, quality signals, privacy rules, and policy automation."
related:
  - Governance
  - Data Mesh
  - Data Quality and Observability
  - DataOps
  - Business Intelligence
  - Security
---

Data governance helps a team identify what data exists and who owns it. It also
clarifies who can use the data, what it means, and whether it's fit for a
decision.
DataTalks.Club episodes connect governance to
[[data engineering platforms]] and [[data-quality-and-observability=>data quality]].
They also connect it to [[privacy-engineering-for-ml=>privacy engineering]],
[[security]], and the operating model around [[DataOps]].

Governance is more than PII controls or access monitoring. Jessi Ashdown and
Uri Gilad frame it as people, processes, and tools for making data usable with
controlled risk. A company needs inventory before it can use or secure its
data. The same inventory tells the company what to retain or
remove.[[cite:cloud-data-governance@6:40=>Cloud Data Governance]][[cite:cloud-data-governance@14:04=>Cloud Data Governance]]

The [[chief-data-officer-role=>Chief Data Officer role]] puts that governance
work inside a wider data strategy. Marco De Sa describes governance as one CDO
pillar. It sits beside infrastructure and analytics. It also sits beside
accessibility, machine learning, and future product data needs
[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]].

The access-management framing adds that governance creates trust in data for
analysts, data scientists, and customers.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

The book [[book:20210524-data-governance-the-definitive-guide=>Data Governance
Definitive Guide]] expands the same foundations into catalogs,
classification, access controls, and policy automation. Andrew Jones's
[[book:20230807-driving-data-quality-with-data-contracts=>Driving Data Quality
with Data Contracts]] connects governance to producer-consumer agreements. Teams
define schema and quality expectations before a pipeline runs.

## Usable Data With Controlled Risk

Teams classify data and assign ownership. They document meaning and expose
lineage, while access rules and usage reviews control use. Quality measures show
whether data remains fit for use.
People can then find the right data
and judge whether it supports a decision without creating avoidable privacy or
security risk. It also limits compliance risk.[[cite:cloud-data-governance=>Cloud Data Governance]][[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Jessi Ashdown and Uri Gilad first ask why a team needs governance. They then
turn to classification, policy, regulation, and privacy. They cite cloud
adoption, GDPR, and the Cambridge Analytica fallout as catalysts for governance
programs. Exfiltration risk,
analytics enablement, and cost control can matter too. Trust matters across all
of them. Those reasons put governance inside [[data strategy]] because the right
controls depend on why the data matters.[[cite:cloud-data-governance@8:57=>Cloud Data Governance]][[cite:cloud-data-governance@23:00=>Cloud Data Governance]]

The ML platform version adds reproducibility and regulatory limits. Fintech
platform teams need datasets, logs, metadata, and lineage for monitoring and
later analysis. GDPR and regulatory constraints still limit what they can log or
persist. A run record may keep metadata, pointers, or queries rather than copy
every dataset into tool-managed storage. Teams therefore need governance inside
[[MLOps]] platform design. They can make data usable without collecting
everything and without turning retention or deletion into an artifact-store
problem.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

## ML Platform Logging

Teams govern ML platforms partly through the data context they record during
training and evaluation. They also record context during serving. Some tools
store query metadata or pointers. Others copy the full dataset used in a run.

Copying every dataset can make reproducibility look simple. It also multiplies
storage, retention, and deletion work when the data includes personal
information
[[cite:building-production-ml-platform-and-mlops-team@44:05=>Building Production ML Platforms]].

GDPR makes that choice operational. If a person asks to be deleted, the team
has to know where their data exists. It may exist only in the governed
warehouse, or it may also exist in many logged training artifacts. Metadata,
lineage, and controlled data references can preserve auditability without
duplicating every row into the MLOps tool
[[cite:building-production-ml-platform-and-mlops-team@45:50=>Building Production ML Platforms]].

Fintech and fraud teams may need to show why a decision happened. Their
platform therefore has to connect model metadata and data references. It also
has to connect audit history and monitoring logs without weakening the privacy
controls around the original datasets
[[cite:building-production-ml-platform-and-mlops-team@39:54=>Building Production ML Platforms]].

## Starting Points

Guests converge on trust, but they start from different failure modes. Jessi
Ashdown and Uri Gilad start with inventory. Teams first need location,
sensitivity, and policy context for each dataset.[[cite:cloud-data-governance=>Cloud Data Governance]]
Bart Vandekerckhove focuses on access friction and privilege creep. Teams need
purpose-based requests, approvers, time-bound access, and revocation.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Zhamak Dehghani puts governance at the domain-ownership boundary. In [[Data Mesh]],
domains own data products, but federated governance still supplies shared policies and
automated enforcement. The shared primitives cover identity and authorization. They
also cover metadata, retention, and validation.[[cite:data-mesh-architecture-decentralized-data-products@49:25=>Data Mesh Implementation]][[cite:data-mesh-architecture-decentralized-data-products@53:02=>Data Mesh Implementation]]
[[Data Mesh vs Centralized Data Platform]] covers the ownership boundary behind
that governance choice.

Katharine Jarmul centers privacy risk. Governance has to cover the translation
between legal and technical teams, plus consent, data
minimization, and workflow practices. This matters when a team has to decide
whether data should be collected or centralized at all.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Engineering, GDPR, and Machine Learning]]

## Inventory, Classification, and Policy

Teams can't govern unknown data. Inventory work records what data exists before
the team can secure and analyze it. The team can then decide what to retain or
delete. Catalogs expose datasets and metadata. They also record owners,
descriptions, and discovery paths.[[cite:cloud-data-governance=>Cloud Data Governance]]

Classification turns inventory into decisions. Taxonomies and meaningful data
classes connect retention, freshness, and purpose-based access. A customer
identifier and an aggregated metric may need different retention rules. A
temporary debugging table may need a different access path and review
expectation.[[cite:cloud-data-governance@15:33=>Cloud Data Governance]][[cite:cloud-data-governance@24:14=>Cloud Data Governance]]

Policy should match the reason for governance. Low-risk or low-value data may
need minimal governance, while higher-risk data may need stricter classification,
review, and access controls. Smaller [[data engineering]] teams can start with a
minimum viable governance strategy and classify the highest-risk or
highest-value datasets first.[[cite:cloud-data-governance@19:40=>Cloud Data Governance]][[cite:cloud-data-governance@53:21=>Cloud Data Governance]]

## Catalogs, Lineage, and Ownership

A catalog helps people find data, but it isn't the whole governance program. A
useful catalog includes technical metadata, lineage, and a business glossary.
Those details help people understand data. They don't decide who should get
access, who should approve it, or when access should
expire.[[cite:cloud-data-governance@27:48=>Cloud Data Governance]][[cite:cloud-data-governance@54:37=>Cloud Data Governance]][[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Ownership connects discovery to accountability. Multiple teams can share
responsibility, but one team still answers questions and approves changes. That
team also fixes broken assumptions.
Cloud governance assigns data stewards, producers, and decision makers to
explicit human roles. Those people each own a different part of the policy and
access path. That keeps [[data teams]] from treating governance as only a catalog
feature.[[cite:cloud-data-governance@33:03=>Cloud Data Governance]]

Teams use data observability to make the accountability model operational
through RACI. Data engineering teams may be responsible for fixing a failed
pipeline, while a data leader or domain owner may be accountable. Analysts may
need to be informed, and data scientists or other consumers may be consulted on
SLA needs
[[cite:data-quality-data-observability-data-reliability@29:00=>Data Observability Explained]].
With those roles named, teams can treat governance as a response path for
[[data-observability-for-data-engineering=>data observability in data engineering]],
not only as a catalog field.
Data Mesh makes that boundary explicit. It ties data product ownership to
business domains, quality expectations, and service levels.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]][[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]]

This is where governance connects to [[Data Products]] and [[Business
Intelligence]]. Dashboards, metrics, and AI-assisted answers can expose governed
data to many more users, so ownership and lineage must be clear before people
trust the output.

## Access Management

Access governance decides who can use data, why they can use it, and how long
that access lasts. The access path runs from request to approval, review, and
revocation. Sensitive data needs this control early, especially when cloud
consolidation puts many datasets behind shared systems.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

A purpose-based request turns access into a governance decision. Analysts can
discover data through a catalog and request access for a specific use. The team
can limit privilege creep with time-bound access, reviews, and revocation.
Those controls connect governance to [[security]] because the team has to reduce
excess permissions without blocking legitimate analysis.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Production debugging needs a different path. Governance should leave a fast,
reviewable way to grant temporary access during an incident, then remove it when
the investigation ends. This is where governance meets [[GitOps for Data Teams]]:
access-as-code makes permission changes reviewable, auditable, and easier to
roll back.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

## Automation and DataOps

Governance breaks down when every decision becomes a manual queue. Teams can
automate repeated controls such as ownership tags, sensitive-data labels, and
retention classes. Access review reminders and revocation rules fit too. Cloud
governance episodes discuss automated tagging, access requests, and enforcement
through both catalog interfaces and storage control planes.[[cite:cloud-data-governance@45:04=>Cloud Data Governance]][[cite:cloud-data-governance@48:50=>Cloud Data Governance]]

Tooling choices such as Dataplex or Collibra matter only when they support that
operating model. The governance ROI question is whether catalogs, access
workflows, and automation reduce risk or duplicated effort enough to justify the
program.[[cite:cloud-data-governance@47:35=>Cloud Data Governance]][[cite:cloud-data-governance@50:19=>Cloud Data Governance]]

In DataOps, teams use active metadata and automated tagging. Pipelines and
access-as-code keep common controls close to data systems. Teams can implement
them with tools such as Terraform and IAM.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Automation doesn't remove judgment because different reviewers care about
different risks. Data stewards, producers, and decision makers may need one
review. Privacy teams, security teams, and domain owners may need another.
Metadata can route the decision, but it can't replace
the decision.[[cite:cloud-data-governance=>Cloud Data Governance]][[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

## Quality, Privacy, and AI Boundaries

Data quality is part of governance because bad data can make a governed system
unsafe or useless. Consumers need trust signals and source quality. They also
need freshness, schema, and volume. Lineage and ownership help them judge
whether data can support a metric, a model, or an operational decision. That
links data governance to [[Data Quality
and Observability]].[[cite:cloud-data-governance=>Cloud Data Governance]]

Privacy changes the governance question because access isn't the only risk.
The team also asks whether the data should be collected or centralized at all.
Fingerprinting and re-identification risk show why a permission rule may not be
enough. Privacy-enhancing technologies can require a different
architecture.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Engineering, GDPR, and Machine Learning]]

Model governance adds another boundary. When teams use governed data to make or
automate decisions about people, they need feature-necessity review and PII
handling. They also need fairness checks and human oversight. [[Responsible AI and Governance]]
covers that overlap in more detail.[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

## Related Pages

These pages cover adjacent governance concepts:

- [[Governance]]
- [[Data Mesh]]
- [[Data Mesh vs Centralized Data Platform]]
- [[Data Products]]
- [[Data Quality and Observability]]
- [[DataOps]]
- [[Security]]
- [[Privacy Engineering for ML]]
- [[Responsible AI and Governance]]
