---
layout: wiki
title: "Data Governance"
summary: "How DataTalks.Club guests frame governance as the people, policies, catalogs, and automation that make data safe and usable."
related:
  - Data Engineering Platforms
  - Data Mesh
  - Data Quality and Observability
  - MLOps and DataOps
  - Responsible AI and Governance
---

## Definition and Scope

Data governance tracks data inventory and ownership. It also defines meaning,
access, retention, and fitness for use. In the podcast archive, governance is
broader than security or compliance. It includes classification, catalogs,
policies, lineage, quality signals, access workflows, and human stewardship.

The recurring archive position is pragmatic: governance should make data easier
to use safely, not just harder to access. The best evidence comes from the cloud
data governance episode. The same ideas reappear in Data Mesh, DataOps, modern
data engineering, and MLOps platform episodes.


## Recurring Archive Themes

Governance starts with the "why". Jessi Ashdown and Uri Gilad repeatedly warn
against starting from tools. Teams should first ask whether pressure comes from
regulation or privacy. Other drivers include exfiltration risk, analytics
enablement, cost control, and trust.

Catalogs are useful but not sufficient. Catalogs help people find datasets and
understand metadata. They also support access requests and expose unused
storage. The archive doesn't treat catalogs as governance by themselves. A
useful catalog connects policies, lineage, business definitions, and quality
signals.

Policies need automation and human judgment. Teams can encode retention,
freshness, purpose-based access, and hashing in tools. Opt-in rules can be
encoded too. The archive still keeps humans in the loop for classification and
judgment. A field can be personal, business-critical, or safe only in context.

Governance works best with shared primitives. In the Data Mesh episode, Zhamak
Dehghani reframes governance as cross-cutting policies for autonomous domains.
Teams can choose local implementation details. Retention, privacy levels, and
identity still need common handling. Access control and product discovery do
too.

Quality is part of governance. The governance episode includes data quality
as a governance concern. Source quality determines whether data can support a
mortgage decision, oil-rig safety decision, ML model, or business metric.

## Episode Evidence

These episodes give the strongest evidence:

- [Cloud Data Governance](https://datatalks.club/podcast.html), 6:40-18:24:
  defines governance beyond PII and security. It anchors implementation in
  people, processes, and tools. It also covers classification and policies.
  Source:
  `../datatalksclub.github.io/_podcast/cloud-data-governance.md`.
- [Cloud Data Governance](https://datatalks.club/podcast.html), 20:09-30:20:
  argues that even small programs need to know what data they have. The right
  level of governance depends on data sensitivity and business value.
- [Cloud Data Governance](https://datatalks.club/podcast.html), 34:59-50:36:
  covers quality signals, retention, and freshness. It also covers
  purpose-based access, storage-level enforcement, request workflows,
  automation, and ROI.
- [Data Mesh Implementation](https://datatalks.club/podcast.html), 49:25-53:02:
  defines federated governance as shared policies and automated enforcement
  across independent data products and platforms. Source:
  `../datatalksclub.github.io/_podcast/data-mesh-architecture-decentralized-data-products.md`.
- [Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html),
  21:22-24:23: connects governance to avoiding data swamps. Those swamps have
  unclear purpose, low trust, unused data, and no cleanup rules. Source:
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`.
- [Mastering DataOps](https://datatalks.club/podcast.html), 51:21-53:33:
  treats governance and catalogs as versioned work. Code, models, and
  visualizations belong in the same delivery system. Source:
  `../datatalksclub.github.io/_podcast/dataops-automation-and-reliable-data-pipelines.md`.

## Tradeoffs

Governance can either enable or block data work. The cloud governance episode
pushes guardrails that make leaders comfortable with broader access. The Data
Mesh episode pushes federated standards because central approval queues don't
scale across autonomous domains.

The strongest tension is minimum viable governance versus future-proofing. The
archive supports starting small, but not ignoring future scale. Classify the
highest-value or highest-risk data first, automate what repeats, and expand as
usage proves value.

## Related Pages

Useful adjacent pages:

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
