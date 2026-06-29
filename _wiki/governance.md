---
layout: wiki
title: "Governance"
summary: "Archive-backed bridge for governance across data, ML, and AI: ownership, access, review, release controls, compliance, and accountability."
related:
  - Data Governance
  - Responsible AI and Governance
  - MLOps and DataOps
  - Model Registry
  - Security
---

Governance is how data and ML teams turn risk into accountable choices. It
names owners and policies, defines approvals and evidence, and sets review
loops plus release controls. In the podcast archive, governance isn't a
separate compliance layer.

It connects these topics:

- [data governance]({{ '/wiki/data-governance/' | relative_url }})
- [security]({{ '/wiki/security/' | relative_url }})
- [privacy engineering]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [responsible AI]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})

The strongest archive discussions are operational.
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
moves from trust in data to access workflows and reviews. It then covers
masking, role inheritance, and access-as-code.

[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})
connects cloud classification and catalogs with policy. It also covers request
workflows, automation, and ROI.

[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
extends governance into feature necessity and PII handling. It also covers
explainability, fairness, and human oversight.

## Link Map

The closest wiki pages are:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

The most useful podcast anchors are:

- [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
  with [Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
- [Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})
  with [Jessi Ashdown]({{ '/people/jessiashdown/' | relative_url }})
  and [Uri Gilad]({{ '/people/urigilad/' | relative_url }})
- [Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
  with [Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }})
- [Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
  with [Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }})
- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
- [MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
  with [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
- [ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
  with [Geo Jolly]({{ '/people/geojolly/' | relative_url }})

## Common Definition

The archive treats governance as a set of named decisions, not as one tool.

The repeatable moves are:

- classify important data and model artifacts
- assign owners and approvers
- encode policy where it repeats
- keep people in the loop for judgment calls
- preserve metadata and lineage for later explanation
- revisit access, quality, and model behavior after systems change

In
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}),
classification and catalogs sit beside policy, request workflows, and ROI.
Governance starts with the reason for control. It then picks the minimum process
that still protects the data and makes reuse possible.

The access-management version is more concrete. Bart's
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode treats operational controls as governance machinery.

Those controls include:

- requests and approvals
- periodic reviews and revocation
- temporary debugging access
- masking and filtering
- role inheritance and alerts
- active metadata and access-as-code

That makes governance close to
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}):
rules become reviewable workflows and automatable controls.

ML and AI episodes add model artifacts and release gates. They also add
explainability, drift, and stakeholder review.

Simon Stiebellehner connects
[model registries]({{ '/wiki/model-registry/' | relative_url }}) to metadata,
lineage, reproducibility, and artifact logging in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He also discusses GDPR-sensitive dataset storage. Supreet Kaur adds feature
necessity and PII handling in
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}).
Her episode also covers product input and compliance input. It connects those
reviews to interpretability tradeoffs, human oversight, and drift checks.

## Disagreements and Boundaries

Guests start from different failure modes. Jessi Ashdown and Uri Gilad begin
with business purpose such as regulation and privacy. Their starting points also
include trust, exfiltration risk, democratized access, and cost
([Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})).
Bart Vandekerckhove begins with access operations. Sensitive data, consolidated
cloud storage, data mesh, and privilege creep make request and revocation
workflows necessary early
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).

The ML platform guests focus on release context. Nemanja Radojkovic describes
finance settings with legacy systems and slow change. Approvals, on-premises
platforms, and existing DevOps controls also matter
([MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Geo Jolly frames governance through platform product work that includes roadmap
choices and stakeholder communication. It also includes rollout timing,
compliance, and release checklists
([ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Katharine Jarmul and Supreet Kaur draw the boundary around user harm and privacy
risk. Katharine pushes governance toward consent, data minimization, and
re-identification risk. She also covers PETs and federated learning, plus
differential privacy and localized model deployment
([Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).
Supreet focuses on fairness checks, explainability, compliance participation,
and human-in-the-loop decisions when automated systems affect people
([Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})).

## Access And Ownership

Access governance starts with knowing who can use which data and why.
In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
Bart traces the workflow from catalogs and lineage into purpose-based requests
and approvers. Reviews and revocation are part of that loop. Temporary
production-debugging grants are part of the same operating model.

His examples connect
[data governance]({{ '/wiki/data-governance/' | relative_url }}) to
[security]({{ '/wiki/security/' | relative_url }}) because the stakeholders see
different risks. Privacy teams care about lawful processing and sensitive
attributes. Security teams care about exfiltration, least privilege, and
operational controls.

Access isn't a one-time permission. Role inheritance can reduce repeated
approvals, but Bart also warns about role explosion and privilege creep. Reviews
and alerts are part of the control loop
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).
Access-as-code and Terraform-style IAM make governance auditable. Active
metadata and automated tagging reduce manual queues.

## Cloud Governance And Data Products

Cloud governance broadens access control into data product usability. Jessi
Ashdown and Uri Gilad cover classification, taxonomy, catalog metadata, and
business glossaries. They also discuss lineage and retention. Freshness,
purpose-based access, request workflows, and measurable ROI round out the model
([Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})).
Their episode treats governance as enablement: guardrails make self-service
access safer, and catalog interfaces make policy visible to data consumers.

That view connects governance to
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
Quality signals and source context determine whether a dataset can support a
metric, model, or operational decision. Measurable checks make that judgment
repeatable
([Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})).
Minimum viable governance is acceptable here. It still has to classify
high-value or high-risk data first and leave room for automation as usage grows.

## Privacy And Responsible AI Review

Privacy episodes make governance more than access approval. Katharine Jarmul's
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
episode covers GDPR, CCPA and CPRA awareness. It also covers consent UX,
opt-out defaults, and privacy risk translation. Fingerprinting,
re-identification, and data minimization are part of the same discussion.

PETs and federated learning extend that discussion alongside differential
privacy and generative AI retention concerns. For
[Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
the governance decision isn't only whether data can be used. Teams also decide
whether the architecture should avoid collecting or centralizing it.

Responsible AI adds product and domain review. Supreet Kaur's
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
episode turns governance into a cross-functional check on feature necessity and
PII handling. It also covers bias detection, missingness, and coverage.
Explainability tools and profitability-versus-fairness decisions are part of
that review.

Human oversight and interpretability tradeoffs are part of the same review.
Drift and feedback loops are too. This is the bridge between
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
and production monitoring.

## ML Platform Release Governance

ML platform governance focuses on reproducibility, release controls, and
operability. Simon Stiebellehner describes MLOps as people, processes, and
technology. He grounds governance in experiment tracking, model registries,
batch and online deployment, and orchestration.

He also discusses thin cloud abstractions, metadata, and lineage. Artifact
logging, unified prediction schemas, and GDPR-aware dataset storage complete the
governance picture
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Those practices turn [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
into governance infrastructure. They make it possible to know which model ran,
which artifact supported it, and how it should be monitored.

Finance shows why release governance can't be copied blindly from startups.
Nemanja Radojkovic's
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
episode links CI/CD, deployment, model governance, and regulatory expectations.
Legacy systems are part of that context, and the episode also covers approvals
and release management.

On-premises platforms, dev/test/prod separation and monitoring matter too, while
minimum viable MLOps gives teams a smaller starting point. Useful
[MLOps]({{ '/wiki/mlops/' | relative_url }}) controls fit the risk and
infrastructure that already govern the organization.

## Governance As Platform Product Work

Governance also has a product-management side. Geo Jolly's
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
episode treats internal ML platform users as customers. That shifts governance
questions from "what policy exists?" to "will teams adopt the controlled path?"

Roadmaps and stakeholder balance become part of governance alongside ROI, user
research and backlog prioritization.

Rollout timing and compliance matter as well, along with release checklists,
platform happiness reports and quality assurance.

This product view is useful for
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}).
If the governed platform is too painful, teams bypass it. If it's usable,
documented, and aligned with real workflows, governance becomes the default
path. Teams then use it for deployment, data requests, and release communication
([ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

## Related Pages

Use these pages for the adjacent data, ML, and responsible-AI topics:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
