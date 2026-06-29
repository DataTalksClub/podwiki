---
layout: wiki
title: "Data Governance"
summary: "How DataTalks.Club guests frame governance as the people, processes, policies, catalogs, and automation that make data safe and usable."
related:
  - Data Engineering Platforms
  - Data Mesh
  - Data Quality and Observability
  - MLOps and DataOps
  - Responsible AI and Governance
---

## Definition and Scope

Data governance is the operating system for knowing what data exists, who owns
it, what it means, who can use it, how long it should live, and whether it is
fit for a specific use. In the podcast archive, governance is broader than
security or compliance. It includes classification, catalogs, policies, lineage,
quality signals, access workflows, and the human roles that make those controls
usable.

The recurring archive position is pragmatic: governance should make data easier
to use safely, not just harder to access. The best evidence comes from the cloud
data governance episode, then reappears in Data Mesh, DataOps, modern data
engineering, and MLOps platform episodes.

## Contents

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Tradeoffs](#tradeoffs)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

### Governance starts with the "why"

Jessi Ashdown and Uri Gilad repeatedly warn against starting from tools. Teams
should first ask whether the pressure is regulation, privacy, exfiltration risk,
analytics enablement, cost control, or trust. That "why" determines the minimum
useful governance program.

### Catalogs are useful but not sufficient

Catalogs help people find datasets, understand metadata, request access, and
spot unused storage. The archive does not treat catalogs as governance by
themselves. A useful catalog is connected to classifications, policies, lineage,
business definitions, quality signals, and access workflows.

### Policies need automation and human judgment

Retention, freshness, purpose-based access, hashing, and opt-in rules can be
encoded in tools. But the archive keeps humans in the loop for classification
and judgment: a field can be personal, business-critical, or safe only in
context.

### Federated governance needs shared primitives

In the Data Mesh episode, Zhamak Dehghani reframes governance as cross-cutting
policies for autonomous domains. Every team can choose local implementation
details, but shared primitives such as retention policies, privacy levels,
identity, access control, and data product discovery need common handling.

### Quality is part of governance

The governance episode explicitly includes data quality as a governance concern:
whether a source can support a mortgage decision, an oil-rig safety decision, an
ML model, or a business metric depends on source knowledge, measurable checks,
and producer accountability.

## Episode Evidence

| Episode | Evidence |
| --- | --- |
| [Cloud Data Governance](https://datatalks.club/podcast.html), 6:40-18:24 | Defines governance beyond PII and security, then anchors implementation in people, processes, tools, classification, and policies. Source: `../datatalksclub.github.io/_podcast/cloud-data-governance.md`. |
| [Cloud Data Governance](https://datatalks.club/podcast.html), 20:09-30:20 | Argues that even small programs need to know what data they have, but the level of governance should match data sensitivity and business value. |
| [Cloud Data Governance](https://datatalks.club/podcast.html), 34:59-50:36 | Covers quality signals, retention, freshness, purpose-based access, storage-level enforcement, request workflows, automation, and ROI through catalog usage and compliance value. |
| [Data Mesh Implementation](https://datatalks.club/podcast.html), 49:25-53:02 | Defines federated governance as shared policies and automated enforcement across independent data products and platforms. Source: `../datatalksclub.github.io/_podcast/data-mesh-architecture-decentralized-data-products.md`. |
| [Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html), 21:22-24:23 | Connects governance to avoiding data swamps: unclear purpose, low trust, unused data, and no cleanup rules. Source: `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`. |
| [Mastering DataOps](https://datatalks.club/podcast.html), 51:21-53:33 | Treats governance, catalogs, code, models, and visualizations as versioned parts of one data delivery system. Source: `../datatalksclub.github.io/_podcast/dataops-automation-and-reliable-data-pipelines.md`. |

## Tradeoffs

Governance can either enable or block data work. The cloud governance episode
pushes guardrails that make leaders comfortable with broader access. The Data
Mesh episode pushes federated standards because central approval queues do not
scale across autonomous domains.

The strongest tension is minimum viable governance versus future-proofing. The
archive supports starting small, but not ignoring future scale: classify the
highest-value or highest-risk data first, automate what repeats, and expand as
usage proves value.

## Related Pages

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})

## Maintenance Notes

- Best source files for future expansion:
  `../datatalksclub.github.io/_podcast/cloud-data-governance.md`,
  `../datatalksclub.github.io/_podcast/data-mesh-architecture-decentralized-data-products.md`,
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`,
  and `../datatalksclub.github.io/_podcast/dataops-automation-and-reliable-data-pipelines.md`.
- Future updates should add concrete policy examples, not generic governance
  claims. Good candidates: retention, access purpose, data quality thresholds,
  catalog metadata, lineage, and stewardship workflows.
- Keep AI policy, fairness, and model risk details on
  [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
  unless the evidence is specifically about data assets and access.
