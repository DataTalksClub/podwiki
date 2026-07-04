---
layout: wiki
title: "Governance"
summary: "Governance ties ownership, access, review, release controls, privacy, security, and accountability across data, ML, and AI systems."
related:
  - Data Governance
  - Responsible AI and Governance
  - MLOps
  - DataOps
  - Model Registry
  - Security
---

Governance is the operating model for accountable choices in data, ML, and AI
systems. It names owners and usage rights. It sets review rules and records
evidence after access, data, or model changes.

Governance is practical engineering and product work, not a standalone
compliance checklist. Cloud governance connects classification and catalogs,
with the reason for governance established before policy design.[[cite:cloud-data-governance=>Cloud Data Governance]]

The access side starts with catalogs, dictionaries, and lineage, then extends
to purpose-based requests and reviews. It also covers revocation, masking, and
access-as-code.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

The same operating model expands when the governed asset changes. Data platforms
need [[data governance]],
[[security]], and
[[privacy engineering for ML]].
ML platforms add [[MLOps]],
[[model-registry=>model registries]], and release
controls. AI products add [[responsible-ai-and-governance=>responsible AI]],
evaluation, human review, and guardrails for LLM or agent behavior.

## Governed Assets

One broad definition recurs: governance makes useful systems reviewable without
hiding risk. Teams classify assets and assign owners. They encode repeated
rules, preserve metadata and lineage, then revisit access or model behavior
after systems change.

Data governance starts with datasets, tables, derived metrics, and catalogs.
Business glossaries and lineage make the inventory usable. A company can't
secure or reuse data confidently without knowing what data it has.[[cite:cloud-data-governance=>Cloud Data Governance]]

Retention and deletion depend on the same inventory, moving from taxonomy and
classification into retention, freshness, and purpose-based access.[[cite:cloud-data-governance=>Cloud Data Governance]]

A different failure mode reaches the same trust goal. Older centralized
governance gives way to request paths and approvals. Time-bound permissions
counter privilege creep. Revocation becomes an operating control.[[cite:data-governance-data-access-management=>Access]]
That approach is strongest when sensitive data already lives in shared cloud
systems and informal permission handling no longer works.

ML governance tracks training inputs, release artifacts, and monitoring
signals. Experiment tracking links [[model-registry=>model registries]] with
metadata and lineage. Artifact logs complete the record alongside GDPR-aware
dataset storage and prediction schemas.[[cite:building-production-ml-platform-and-mlops-team=>ML Platforms]]

A [[ml-platforms=>machine learning platform]] becomes reviewable when reviewers
can trace the deployed model back to its data, code, artifact, and schema.

AI product governance adds prompts, retrieved context, and outputs. It also
covers guardrail results, evaluation labels, feedback, and human override
points. Feature necessity, PII handling, and compliance input fit the same
operating model. Fairness checks sit beside interpretability, drift, and human
oversight.[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

Prompt injection and knowledge-base exfiltration extend the surface. Output
validation and query analysis add mitigation evidence.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]
Agent guardrails and lineage do the same. Multi-tenant evaluations and
human-label alignment also become governance evidence.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Inventory and Ownership

Governance starts with inventory because unknown data can't be secured, reused,
retained, or deleted deliberately. Taxonomy, classification, catalogs, and
lineage come first. Retention, freshness, purpose-based access, and minimum
viable governance follow.[[cite:cloud-data-governance=>Cloud Data Governance]]

[[data governance]] connects to
[[self-service-data-platforms=>self-service data platforms]].
A governed catalog should expose meaning and policy to data consumers instead
of making them rely on private knowledge.

Ownership turns metadata into accountability. Data teams separate from
governance teams, and domain ownership models follow.[[cite:data-governance-data-access-management=>Data Access]]
In data mesh, domains own products. Identity and authorization remain shared
governance primitives. Retention, metadata, and validation remain shared
too.[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh]]

Domain ownership links to data product contracts, service levels, and quality
expectations. Teams make federated governance, identity, and authorization shared
primitives. Retention, metadata, and validation then apply across domain-owned
data products.[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]]

Those domain boundaries keep governance close to
[[Data Mesh]].

Domains own data products, but shared rules make products interoperable.
Identity and authorization define who can use the product. Retention, metadata,
and validation let decentralized products behave as part of one system.

Trust signals and measurable checks belong in the same ownership model.[[cite:cloud-data-governance=>Cloud]]
Consumers need freshness and lineage before using a dataset for a metric.
They also need schemas and volume. When the same data feeds a model or an
operational decision, owners and known limits also matter.
Those checks make governance part of
[[Data Quality and Observability]].

## Access, Privacy, and Policy Automation

Access governance decides who can use data, why they need it, and how long they
keep access. Access requests, approvals, review, and revocation are the core
controls.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

An analyst requests data for a specific churn-analysis purpose, and time-bound
access counters privilege creep. Temporary debugging access keeps incident
response possible while masking and filtering limit sensitive-data exposure.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Those controls sit beside [[security]]
because they reduce excess privilege and exfiltration risk without blocking
legitimate analysis. Pipelines, Terraform, and IAM connect to alerts, while
automated tagging and active metadata make the access-as-code approach
reviewable.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

Access-as-code links
governance to
[[GitOps for Data Teams]]
and [[DataOps]]. Teams can turn repeated
controls into reviewable configuration instead of one-off permission changes.

Automation matters because manual governance becomes a queue, so automation
handles tagging, requests, and manual-effort reduction. Data stewards,
producers, and decision makers stay in the loop, so repeated checks move
without replacing judgment.[[cite:cloud-data-governance=>Cloud Data Governance]]

Privacy changes the access question. Teams must decide whether data should be
collected or centralized at all. They also need retention and exposure rules.
GDPR and CCPA/CPRA connect to consent UX.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Engineering, GDPR, and Machine Learning]]

Privacy-risk translation and fingerprinting come first because re-identification
remains a privacy concern.[[cite:data-privacy-engineering-gdpr-machine-learning=>Privacy ML]]

Privacy-enhancing technologies and federated learning extend the architecture
options, and differential privacy makes the same point. Governance may need an
architecture decision when a permission rule isn't enough.[[cite:data-privacy-engineering-gdpr-machine-learning=>Privacy ML]]

## ML Release Controls

ML governance adds release evidence through MLOps, which spans people,
practices, and technology. It ties self-service compute, experiment tracking,
and model registries into the platform. Orchestration, metadata, and lineage
complete that platform record.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Artifact
logging, batch deployment, online deployment, and monitoring complete the
release record. A reviewer can then see which
model ran, which data and artifact supported it, and how predictions should be
monitored.

In regulated organizations, teams make the approval path more explicit. Finance
use cases and legacy systems combine with regulatory constraints. CI/CD,
approvals, and release management become part of the same path.[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]
On-premises platforms and dev/test/prod separation add more constraints.
Monitoring, model registries, and minimal viable MLOps complete the practical
path.

Release paths differ across banks, startups, and temporary tactical setups.
Each one still needs evidence and approval points.[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]

Platform product work also shapes releases.[[cite:ml-product-manager-and-mlops-platform-strategy=>MLOps Platform Strategy]]
Roadmap choices and stakeholder balance influence whether teams adopt the
governed path. Rollout timing, compliance, quality assurance, and shadowing
also affect adoption. Release checklists, ROI, and platform happiness reports
keep the path accountable.

Governance fails when the
controlled platform is slow, undocumented, or mismatched to real data science
and engineering work. It becomes the default when teams can request data,
deploy models, communicate releases, and review post-launch behavior through a
usable [[platform engineering]]
surface.

## Responsible AI Review

Responsible AI turns governance toward model impact, where the trust problem
centers on AI decisions. Explainable AI is distinct from the broader
responsible-AI discipline. Pre-training review covers skewness, missingness,
and coverage.[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

Exploratory bias detection, PII handling, and feature-necessity review follow.
Product teams, subject-matter experts, and compliance input enter the feature
decision.[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

Fairness and business tradeoffs stay together. Accuracy versus interpretability
and ethics versus profitability are product decisions. Human review and drift
stay in scope too. Feedback loops, regulated-industry sensitivity, AutoML risk,
and professional responsibility complete the review surface.[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

Those controls connect
[[responsible AI and governance]]
to [[model monitoring]] and
[[machine learning system design]].
Fairness and explainability evidence should influence launch, monitoring, and
override decisions.

Governance also needs audience-fit evidence, and interpretability supports
debugging and uncertainty review.[[cite:interpretable-machine-learning=>Interpretability]]

Fairness metrics still require product and domain judgment. Human review stays
part of the decision.[[cite:fairness-in-ai-ml-engineering=>Fairness]]
A fairness dashboard or a SHAP value becomes evidence only when someone uses it
for a decision. Monitoring and override decisions matter too.

## LLM and Agent Controls

Generative AI widens governance from model release to interaction safety and
retrieval exposure. Chatbot hacking, prompt injection, and hallucinations are
part of the risk surface. Legal exposure, financial exposure, and knowledge-base
exfiltration add more failure modes.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Output validation and query analysis create the first mitigation layer.
Non-LLM classifiers and human review add controls outside the generative model.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Those examples place LLM governance beside
[[AI red teaming]],
[[LLM production patterns]],
and [[security]]. The controlled asset is
a live interaction with retrieved context, not only a stored model file.

Agents add autonomy, memory, tools, and multi-step execution. Reliability in
legal and healthcare settings brings specialized models, guardrails, lineage,
and compliance into scope. Feedback, multi-tenant evaluations, LLM judges, and
deployment risk matter too.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

In that setting, governance needs permission boundaries and evaluation cases.
It also needs lineage for what the agent saw. Records of tool use and human
review points help people decide when to trust or override the result.

## Related Pages

Governance connects to these narrower pages:

- [[Data Governance]] covers datasets, catalogs, lineage, ownership, access, and
  data quality.
- [[Privacy Engineering for ML]] covers consent, minimization, PETs, federated
  learning, and differential privacy.
- [[Responsible AI and Governance]] covers fairness, explainability, human
  oversight, and post-launch review.
- [[MLOps vs DataOps]] and [[Model Registry]] cover release controls.
- [[self-service-data-platforms=>Self-Service Data Platforms]] and
  [[GitOps for Data Teams]] cover governed platform work.
- [[AI Red Teaming]] and [[LLM Evaluation Workflows]] cover LLM and agent
  systems.
