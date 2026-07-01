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
security or compliance. They connect it to [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[privacy engineering]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
and the operating model around [DataOps]({{ '/wiki/dataops/' | relative_url }}).

[Jessi Ashdown]({{ '/people/jessiashdown/' | relative_url }}) and
[Uri Gilad]({{ '/people/urigilad/' | relative_url }}) make the broadest
definition in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
At 6:40, they define governance beyond PII and credit card numbers. It's also
more than monitoring access. At 7:47, Jessi adds the practical reason. A company
that doesn't know what data it has can't decide how to use, secure, retain or
remove that data.

[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }}) gives
the access-management version in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
At 5:20, he defines governance as the activities that create trust in data for
analysts, data scientists, and customers. In that framing, teams govern data
through operating practice, not through documentation alone.
The same trust boundary applies to
[Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }}),
where dashboards, metrics, and AI-assisted answers can expose governed data to
many more users.

## Usable Data With Controlled Risk

Across these episodes, data governance means making data usable and safe at the
same time. Teams classify data, assign ownership, and document meaning. They
expose lineage, design access rules, review usage, and measure quality. People
can then find the right data and judge whether it supports a decision without
creating avoidable privacy, security, or compliance risk.

In [Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}),
Jessi and Uri describe governance as people, processes, and tools at 14:04.
At 15:33, they move from that definition into classification and policy. At
23:00, they say the team should start with the reason for governance.

Regulation and privacy are common reasons to govern data. Exfiltration risk,
analytics enablement, trust, and cost control can matter too. That connects
governance to
[data strategy]({{ '/wiki/data-strategy/' | relative_url }})
because the right controls depend on why the data matters.

Bart's episode agrees with the trust goal and then describes the operating work.
In [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he separates catalogs, dictionaries, and lineage at 8:58. He then moves into
access controls at 11:20 and ownership models at 13:34.

At 27:49, Bart covers the access path from request to approval, review, and
revocation. For him, governance becomes real when people can request access for
a stated purpose and the team can later review or remove that access.

## Inventory, Access, Domain, and Privacy Starting Points

The podcast discussions converge on trust, but each guest reaches it from a
different data governance failure mode.

Jessi Ashdown and Uri Gilad start with the inventory problem. Their cloud
governance episode asks what data exists and where it lives. It also asks how
sensitive the data is and which policies should apply
([Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}),
6:40, 15:33, 24:14). Their version is useful when a team has many datasets,
cloud storage systems, and consumers who need self-service access.

Bart Vandekerckhove starts with access friction and privilege creep. In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he describes older governance as centralized and top-down at 6:52. He then
pushes toward scalable access management.

Teams need purpose-based requests and approvers, plus time-bound access and
revocation. Masking, filtering, reviews, and access-as-code belong in the same
control set.

His version is useful when a team already has sensitive data in shared cloud
systems and informal permission handling no longer works.

[Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }}) starts from a
different organizational problem in
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}).
At 49:25, she describes federated governance as shared policies with automated
enforcement across domain-owned data products. That places governance close to
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}). Domains can own data
products, but shared primitives still cover identity and authorization. They
also cover metadata, retention, and validation.

Use
[Data Mesh vs Centralized Data Platform]({{ '/comparisons/data-mesh-vs-centralized-data-platform/' | relative_url }})
for the ownership boundary behind that governance choice.

[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) moves the
boundary toward privacy risk in
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}).
At 22:38, she discusses the translation work between legal and technical teams.
At 47:00, she connects privacy to consent, data minimization, and workflow
practices. Her privacy framing matters when a team uses governance to decide
whether data should be collected or centralized at all.

## Inventory, Classification, and Policy

Governance starts with inventory because teams can't govern unknown data.
Jessi Ashdown says this directly in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})
at 7:47. The team needs to know what data exists before it can secure, analyze,
retain, or delete it. That inventory work relies on catalogs because catalogs
expose datasets and metadata. They also expose owners, descriptions, and
discovery paths.

Classification turns inventory into decisions. At 24:14 in the same episode,
Jessi and Uri discuss taxonomy plus meaningful data classes. At 38:25, they
connect classification to retention, freshness, and purpose-based access. A
customer identifier and an aggregated metric may need different retention rules.
A temporary debugging table may need a different access path and review
expectation.

The policy should match the reason for governance. At 19:40, Jessi and Uri
leave room for minimal governance when the data is low risk or low value. At
53:21, they describe a minimum viable governance strategy that can grow later.
That matters for smaller [data engineering]({{ '/wiki/data-engineering/' | relative_url }})
teams. They can classify the highest-risk or highest-value datasets first
instead of cataloging every field before anyone gets value.

## Catalogs, Lineage, and Ownership

Catalogs help people find data, but these guests don't treat a catalog as the
whole governance program. Jessi and Uri compare tools with spreadsheets at 27:48
in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
At 54:37, they list the catalog contents that matter. Technical metadata,
lineage, and a business glossary all belong there.

At 57:46, they make the boundary explicit because governance extends beyond the
catalog.

Bart Vandekerckhove gives the same boundary from the access side. At 8:58 in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he separates data catalogs, data dictionaries, and lineage. Those tools help
people understand data, but they don't decide who should get access, who should
approve it, or when access should expire.

Ownership connects discovery to accountability. Bart discusses data teams,
governance teams, and Data Mesh ownership at 13:34. Zhamak Dehghani
adds the domain version in
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}):
at 16:34, she connects data ownership to business domains. At 39:36, she
ties data product contracts to quality, service levels, and ownership
decisions. A useful catalog should therefore name the team that can answer
questions, approve changes, and fix broken assumptions.

## Access Management

Access governance decides who can use data, and it records the purpose plus
duration. Bart's
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode is the clearest podcast example for this. At 11:20, he connects cloud
consolidation and "Chinese wall" constraints to access management. At 25:05, he
argues that sensitive data needs access controls early.

At 27:49, Bart names the core process: teams request and approve access, then
review and revoke it later.

A purpose-based access request turns the request into a governance decision. In
Bart's
churn example at 29:36, the analyst discovers data through a catalog and
requests access for a specific use. At 32:08, Bart discusses privilege creep,
time-bound access, and revocation. Those controls connect governance to
[security]({{ '/wiki/security/' | relative_url }}) because the team must reduce
excess permissions without blocking legitimate analysis.

Production debugging needs a different access path, and Bart covers temporary
debugging access at 35:35. Governance shouldn't make incident response
impossible. The team needs a fast, reviewable way to grant temporary access
during an incident, then remove it when the investigation ends. This is also
where governance meets
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}).
Access-as-code makes permission changes reviewable, auditable, and easier to
roll back.

## Automation and DataOps

Governance breaks down when every decision becomes a manual queue. These
episodes therefore connect governance to automation and
[DataOps]({{ '/wiki/dataops/' | relative_url }}).
In
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}),
Jessi and Uri discuss automation at 48:50 for tagging, requests, and reducing
manual effort. At 45:04, they compare enforcement through catalog interfaces
with enforcement at the storage control plane.

Bart makes the automation path more explicit. At 46:42 in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he connects governance in DataOps to active metadata, automated tagging, and
pipelines. At 50:08, he discusses access-as-code through Terraform, IAM, and
early patterns.

Automation works best for repeated controls. Useful targets include ownership
tags, sensitive-data labels, and retention classes. Access review reminders and
revocation rules also fit.

Automation doesn't remove judgment because Jessi and Uri still put data
stewards, producers, and decision makers in the process at 33:03 of
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
Bart also separates privacy and security stakeholders at 37:19. A data
protection officer, a security team, and a domain owner may all care about the
same dataset for different reasons. A data engineer may care about it for a
fourth reason, so metadata can route the decision without replacing it.

## Quality, Privacy, and AI Boundaries

Data quality is part of governance because bad data can make a governed system
unsafe or useless. Jessi and Uri discuss trust signals, source quality, and
measurable checks at 34:59 in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
That links data governance to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

Freshness, schema, and volume help consumers judge the data, along with lineage
and ownership. Consumers need to know whether the data can support a metric, a
model, or an operational decision.

Privacy changes the governance question. The team isn't only asking who can
access the data. It also asks whether it should collect or centralize the data
at all.

Katharine Jarmul's
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
episode covers GDPR and related privacy regulation awareness at 11:33.

At 25:12, she discusses
fingerprinting and re-identification risk. At 33:08 and 40:50, she covers
privacy-enhancing technologies, federated learning, and differential privacy.
Those choices belong next to governance because policy may need an architecture.
A permission rule isn't enough.

[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) extends governance
into model decisions in
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}).
Her episode covers feature necessity, PII handling, fairness checks, and human
oversight. That belongs on
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
but it also matters here. Teams still need to review governed data when they use it to
make or automate decisions about people.

## Related Data Governance Topics

Use these pages for adjacent governance concepts:

- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Mesh vs Centralized Data Platform]({{ '/comparisons/data-mesh-vs-centralized-data-platform/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
