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

Data governance lets a team answer basic questions about its data. The team
needs to know what data exists, who owns it, who can use it, and what it means.
It also needs to know whether the data is fit for use. In the DataTalks.Club
podcast discussions, guests don't treat governance as only
security or compliance. They connect it to [[data engineering platforms]],
[[data-quality-and-observability=>data quality]],
[[privacy-engineering-for-ml=>privacy engineering]],
and the operating model around [[DataOps]].

[[book:20210524-data-governance-the-definitive-guide=>Data Governance book]]
by Evren Eryurek, Uri Gilad, and Jessi Ashdown expands on these governance
foundations. It covers catalogs, classification, access controls, and policy
automation.

[[person:jessiashdown=>Jessi Ashdown]] and
[[person:urigilad=>Uri Gilad]] make the broadest
definition in
[[cite:cloud-data-governance|Cloud Data Governance]]. They define governance
beyond PII, credit card numbers, and access monitoring. Jessi adds the practical
reason. A company that doesn't know what data it has can't decide how to use,
secure, retain, or remove that data.

[[person:bartvandekerckhove=>Bart Vandekerckhove]] gives
the access-management version. In
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]],
he defines governance as the activities that create trust in data. That trust
matters for analysts, data scientists, and customers. In that framing, teams
govern data through operating practice, not through documentation alone.

Andrew Jones's
[[book:20230807-driving-data-quality-with-data-contracts=>Driving Data Quality with Data Contracts]]
develops that operating-practice idea. Before the pipeline runs, producers and
consumers agree on the schema plus quality obligations.
The same trust boundary applies to
[[Business Intelligence]],
where dashboards, metrics, and AI-assisted answers can expose governed data to
many more users.

## Usable Data With Controlled Risk

Across these episodes, data governance means making data usable and safe at the
same time. Teams classify data, assign ownership, and document meaning. They
expose lineage, design access rules, review usage, and measure quality. People
can then find the right data and judge whether it supports a decision without
creating avoidable privacy, security, or compliance risk.

In [[cite:cloud-data-governance|Cloud Data Governance]], Jessi and Uri describe
governance as people, procedures, and tools. They move from that definition into
classification and policy, then say the team should start with the reason for
governance.

Regulation and privacy are common reasons to govern data. Exfiltration risk,
analytics enablement, trust, and cost control can matter too. Those reasons put
governance inside
[[data strategy]]
because the right controls depend on why the data matters.

Simon Stiebellehner gives the ML platform version in fintech. Platform teams
need reproducible datasets, logs, metadata, and lineage for monitoring and later
analysis. GDPR and regulatory constraints still limit what they can log or
persist
[[cite:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Governance therefore belongs in [[MLOps]] platform design. Teams make data
usable while controlling privacy and compliance risk instead of collecting
everything.

Bart's episode agrees with the trust goal and then describes the operating work.
In [[cite:data-governance-data-access-management|Data Governance and Data Access Management]],
he separates catalogs, dictionaries, and lineage. He then moves into access
controls and ownership models.

Bart covers the access path from request to approval, review, and revocation.
For him, governance becomes real when people can request access for a stated
purpose and the team can later review or remove that access.

## Inventory, Access, Domain, and Privacy Starting Points

The podcast discussions converge on trust, but each guest reaches it from a
different data governance failure mode.

Jessi Ashdown and Uri Gilad start with the inventory problem. Their cloud
governance episode asks what data exists and where it lives. It also asks how
sensitive the data is and which policies should apply
[[cite:cloud-data-governance|Cloud Data Governance]]. Their version is useful
when a team has many datasets, cloud storage systems, and consumers who need
self-service access.

Bart Vandekerckhove starts with access friction and privilege creep. In
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]],
he describes older governance as centralized and top-down, then pushes toward
scalable access management.

Teams need purpose-based requests and approvers, plus time-bound access and
revocation. Masking, filtering, reviews, and access-as-code belong in the same
control set.

His version is useful when a team already has sensitive data in shared cloud
systems and informal permission handling no longer works.

[[person:zhamakdehghani=>Zhamak Dehghani]] starts from a
different organizational problem in
[[cite:data-mesh-architecture-decentralized-data-products|Data Mesh Implementation]].
She describes federated governance as shared policies with automated enforcement
across domain-owned data products. That places governance close to [[Data Mesh]].
Domains can own data products, but shared primitives still cover identity and
authorization. They also cover metadata, retention, and validation.

Use
[[Data Mesh vs Centralized Data Platform]]
for the ownership boundary behind that governance choice.

[[person:katharinejarmul=>Katharine Jarmul]] moves the
boundary toward privacy risk in
[[cite:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]].
She discusses the translation work between legal and technical teams and
connects privacy to consent, data minimization, and workflow practices. Her
privacy framing matters when a team uses governance to decide whether data
should be collected or centralized at all.

## Inventory, Classification, and Policy

Governance starts with inventory because teams can't govern unknown data.
Jessi Ashdown says this directly in
[[cite:cloud-data-governance|Cloud Data Governance]]. The team needs to know
what data exists before it can secure, analyze, retain, or delete it. That
inventory work relies on catalogs because catalogs expose datasets and metadata.
They also expose owners, descriptions, and discovery paths.

Classification turns inventory into decisions. Jessi and Uri discuss taxonomy
plus meaningful data classes, then connect classification to retention,
freshness, and purpose-based access [[cite:cloud-data-governance|Cloud Data Governance]].
A customer identifier and an aggregated metric may need different retention
rules. A temporary debugging table may need a different access path and review
expectation.

The policy should match the reason for governance. Jessi and Uri leave room for
minimal governance when the data is low risk or low value. They also describe a
minimum viable governance strategy that can grow later
[[cite:cloud-data-governance|Cloud Data Governance]].
That matters for smaller [[data engineering]] teams. They can classify the
highest-risk or highest-value datasets first instead of cataloging every field
before anyone gets value.

## Catalogs, Lineage, and Ownership

Catalogs help people find data, but these guests don't treat a catalog as the
whole governance program. Jessi and Uri compare governance tools with
spreadsheets and list the catalog contents that matter
[[cite:cloud-data-governance|Cloud Data Governance]]. Technical metadata,
lineage, and a business glossary all belong in the catalog.

They make the boundary explicit because governance extends beyond the catalog.

Bart Vandekerckhove gives the same boundary from the access side. In
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]],
he separates data catalogs, data dictionaries, and lineage. Those tools help
people understand data, but they don't decide who should get access, who should
approve it, or when access should expire.

Ownership connects discovery to accountability. Bart discusses data teams,
governance teams, and Data Mesh ownership
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]].
Zhamak Dehghani adds the domain version in
[[cite:data-mesh-architecture-decentralized-data-products|Data Mesh Implementation]].
She connects data ownership to business domains and ties data product contracts
to quality and service levels. A useful catalog should therefore name the team
that can answer questions, approve changes, and fix broken assumptions.

## Access Management

Access governance decides who can use data, and it records the purpose plus
duration. Bart's
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]]
episode is the clearest podcast example for this. He connects cloud
consolidation and "Chinese wall" constraints to access management and argues
that sensitive data needs access controls early.

Bart names the core access path: teams request and approve access, then review
and revoke it later.

A purpose-based access request turns the request into a governance decision. In
Bart's
churn example, the analyst discovers data through a catalog and requests access
for a specific use. Bart also discusses privilege creep, time-bound access, and
revocation [[cite:data-governance-data-access-management|Data Governance and Data Access Management]].
Those controls connect governance to [[security]] because the team must reduce
excess permissions without blocking legitimate analysis.

Production debugging needs a different access path, and Bart covers temporary
debugging access [[cite:data-governance-data-access-management|Data Governance and Data Access Management]].
Governance shouldn't make incident response impossible. The team needs a fast,
reviewable way to grant temporary access during an incident, then remove it when
the investigation ends. This is also where governance meets [[GitOps for Data Teams]].
Access-as-code makes permission changes reviewable, auditable, and easier to
roll back.

## Automation and DataOps

Governance breaks down when every decision becomes a manual queue. These
episodes therefore connect governance to automation and
[[DataOps]].
In
[[cite:cloud-data-governance|Cloud Data Governance]],
Jessi and Uri discuss automation for tagging, requests, and reducing manual
effort. They compare enforcement through catalog interfaces with enforcement at
the storage control plane.

Bart makes the automation path more explicit. In
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]],
he connects governance in DataOps to active metadata, automated tagging, and
pipelines. He also discusses access-as-code through Terraform, IAM, and early
patterns.

Automation works best for repeated controls. Useful targets include ownership
tags, sensitive-data labels, and retention classes. Access review reminders and
revocation rules also fit.

Automation doesn't remove judgment because Jessi and Uri still put data
stewards, producers, and decision makers in the review
[[cite:cloud-data-governance|Cloud Data Governance]]. Bart also separates
privacy and security stakeholders
[[cite:data-governance-data-access-management|Data Governance and Data Access Management]].
A data protection officer, a security team, and a domain owner may all care
about the same dataset for different reasons. A data engineer may care about it
for a fourth reason, so metadata can route the decision without replacing it.

## Quality, Privacy, and AI Boundaries

Data quality is part of governance because bad data can make a governed system
unsafe or useless. Jessi and Uri discuss trust signals, source quality, and
measurable checks in [[cite:cloud-data-governance|Cloud Data Governance]]. That
links data governance to [[Data Quality and Observability]].

Freshness, schema, and volume help consumers judge the data, along with lineage
and ownership. Consumers need to know whether the data can support a metric, a
model, or an operational decision.

Privacy changes the governance question. The team isn't only asking who can
access the data. It also asks whether it should collect or centralize the data
at all.

Katharine Jarmul's
[[cite:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]]
episode covers GDPR and related privacy regulation awareness.

She discusses fingerprinting and re-identification risk and covers
privacy-enhancing technologies, federated learning, and differential privacy.
Those choices belong next to governance because policy may need an architecture.
A permission rule isn't enough.

[[person:supreetkaur=>Supreet Kaur]] extends governance
into model decisions in
[[cite:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]].
Her episode covers feature necessity, PII handling, fairness checks, and human
oversight. That belongs on
[[Responsible AI and Governance]],
but it also matters here. Teams still need to review governed data when they use it to
make or automate decisions about people.

## Related Data Governance Topics

Use these pages for adjacent governance concepts:

- [[Governance]]
- [[Data Mesh]]
- [[Data Mesh vs Centralized Data Platform]]
- [[Data Products]]
- [[Data Quality and Observability]]
- [[DataOps]]
- [[Security]]
- [[Privacy Engineering for ML]]
- [[Responsible AI and Governance]]
