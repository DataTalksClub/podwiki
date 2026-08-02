---
layout: wiki
title: "Governance"
summary: "Governance ties decision rights, risk review, compliance, release controls, and accountability across data, product, ML, and AI systems."
related:
  - Data Governance
  - Responsible AI and Governance
  - MLOps
  - DataOps
  - Model Registry
  - Security
---

Governance is the operating model for accountable choices across data,
product, ML, and AI systems. It names who can decide, who reviews risk, what
evidence must be kept, and when a change needs escalation or human override.

[[Data Governance]] owns catalog and ownership work, plus lineage, access
policy, and contracts. Quality signals, metric definitions, and analytics or ML
data responsibilities belong there too.

The organizational and product layer around those mechanics focuses on decision
rights and risk review. It also covers compliance paths, release controls, and
governance evidence across systems.

Governance is practical engineering and product work, not a standalone
compliance checklist. In the cloud data governance discussion, dataset policies
start with the reason for governance before policy design. The same rule holds
for ML releases, AI product behavior, and platform operating models. Teams need
to know which risk they're controlling before they choose the review path or
tooling.[[cite:cloud-data-governance=>Cloud Data Governance]]

At company scope, the [[chief-data-officer-role=>Chief Data Officer role]]
connects those governed assets to strategy and organization design. Marco De Sa
frames the CDO mandate around data strategy, governance, AI direction, and team
design. It isn't a compliance office alone.
[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]]

## Decision Rights Across Systems

A governed system needs a named decision owner, reviewer set, and evidence
trail. This is true for datasets and platform capabilities. It's also true for
model releases and AI interactions. The governance question is who owns the
decision, which reviewers must be involved, and what evidence proves the
decision was made deliberately.

Data platforms expose this boundary first. In [[Data Mesh]], domains own data
products while shared governance supplies identity and authorization. The shared
layer also supplies retention, metadata, and validation primitives. The
shared layer belongs to organization design as much as architecture. Domain teams get
product ownership. The [[product-owner-vs-product-manager=>Product Owner vs Product Manager]]
boundary is visible while the company keeps shared rules for interoperability
and risk.[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]]

Platform product work adds another decision layer. MLOps platform strategy
episodes connect governance to roadmap choices and stakeholder balance. They
cover rollout timing, compliance, quality assurance, and shadowing. Release
checklists and ROI keep the path accountable. Platform happiness
reports do too.[[cite:ml-product-manager-and-mlops-platform-strategy=>MLOps Platform Strategy]]

Governance fails when the controlled path is too slow or mismatched to real data
science and engineering work. It becomes useful when teams can request data,
deploy models, communicate releases, and review post-launch behavior through a
usable [[platform engineering]] surface.

## Risk and Compliance Boundaries

Governance turns legal and security risk into reviewable engineering work. It
does the same for privacy and product risk. Operational risk fits too. Dataset
policy may start from GDPR or cloud consolidation. It may also start from
exfiltration risk or analytics enablement.

The broader move is the same. Define the risk, name the accountable reviewers,
and keep evidence that later teams can look at.[[cite:cloud-data-governance=>Cloud Data Governance]]

Privacy changes the review boundary because permission isn't the only question.
Teams may need to decide whether data should be collected or centralized at all.
Consent and minimization guide that decision. Fingerprinting and
re-identification risk may require architecture work. Privacy-enhancing
technologies can do the same.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Engineering, GDPR, and Machine Learning]]

The data-specific controls belong in [[Data Governance]] and [[Privacy
Engineering for ML]]. Cross-functional decision paths still need product and
legal reviewers. They also need privacy, security, and engineering reviewers.

ML in regulated organizations adds explicit approval and audit paths. Finance
use cases combine legacy systems and regulatory constraints. CI/CD, approvals,
and release management sit inside the same governed path.[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]
Finance decision-support products also have to keep compliance inside the
product experience. Explainability and auditability matter too when ERP and CRM
context supports forecast or cash-flow decisions.
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]]

## Governance Evidence

Governance evidence changes with the asset. Data governance keeps catalogs and
lineage in view, while owners and quality signals stay visible. Access approvals
and retention rules stay visible too.
[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]
ML governance adds training inputs and experiment metadata. It also adds release
artifacts, prediction schemas, monitoring signals, and model registry records.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

AI product governance adds prompts, retrieved context, and outputs. Guardrail
results, evaluation labels, feedback, and human override points complete the
record.
[[cite:responsible-explainable-ai-bias-detection=>Responsible and Explainable AI]]

This evidence is valuable only when it informs a decision. A catalog entry,
fairness dashboard, or SHAP value becomes governance evidence when a reviewer
uses it. An LLM evaluation result works the same way.

The reviewer may approve or block the system, and may also monitor or redesign
it. That puts governance close to [[MLOps]] and [[Model Registry]]. It also links
to [[Responsible AI and Governance]], [[LLM Evaluation Workflows]], and
[[security]].

## ML Release Controls

ML governance adds release evidence through MLOps, which spans people,
practices, and technology. Self-service compute and experiment tracking form the
platform record. Model registries and orchestration add the next layer, and
metadata and lineage complete it.
Artifact logging and deployment records complete the release trail. Monitoring
then lets a reviewer see which model ran, which data and artifact supported it,
and how predictions should be watched.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

On-premises platforms and dev/test/prod separation add more constraints.
Monitoring, model registries, and minimal viable MLOps complete the practical
path.

Release paths differ across banks, startups, and temporary tactical setups.
Each one still needs evidence and approval points.[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]

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

Fairness metrics still require product and domain judgment, so human review
stays part of the decision.[[cite:fairness-in-ai-ml-engineering=>Fairness]]

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
