---
layout: wiki
title: "Governance"
summary: "How DataTalks.Club guests connect governance across data, ML, and AI systems through ownership, access, review, release controls, privacy, security, and accountability."
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

DataTalks.Club guests describe governance as practical engineering and product
work, not a standalone compliance checklist. [[person:jessiashdown|Jessi Ashdown]]
and [[person:urigilad|Uri Gilad]] tie cloud governance
to classification and catalogs in
[[podcast:cloud-data-governance|Cloud Data Governance]]
at 14:04 and 15:33. At 23:00, they add the reason for governance before the
policy design.

[[person:bartvandekerckhove|Bart Vandekerckhove]]
grounds the access side in catalogs and dictionaries at 8:58 in
[[podcast:data-governance-data-access-management|Data Governance and Data Access Management]].
He adds lineage in the same chapter. At 27:49 and 32:08, his episode covers
purpose-based requests, reviews, and revocation. At 42:20 and 50:08, it covers
masking and access-as-code.

The same operating model expands when the governed asset changes. Data platforms
need [[data governance]],
[[security]], and
[[privacy engineering for ML]].
ML platforms add [[MLOps]],
[[model-registry|model registries]], and release
controls. AI products add [[responsible-ai-and-governance|responsible AI]],
evaluation, human review, and guardrails for LLM or agent behavior.

## Governed Assets

Podcast guests converge on one broad definition: governance makes useful
systems reviewable without hiding risk. Teams classify assets and assign
owners. They encode repeated rules, preserve metadata and lineage, then revisit
access or model behavior after systems change.

Data governance starts with datasets, tables, derived metrics, and catalogs.
Business glossaries and lineage make the inventory usable. In
[[podcast:cloud-data-governance|Cloud Data Governance]],
Jessi and Uri start from the inventory problem. At 6:40 and 7:47, they argue
that a company can't secure or reuse data confidently if it doesn't know what
data it has.

Retention and deletion depend on the same inventory. At 24:14 and
38:25, they move from taxonomy and classification into retention, freshness, and
purpose-based access.


Bart reaches the same trust goal from a different failure mode. In
[[podcast:data-governance-data-access-management|Data Governance and Data Access Management]],
he describes older centralized governance at 6:52, then focuses on request
paths and approvals. He also covers time-bound permissions, privilege creep,
and revocation. That version is strongest when sensitive data already lives in shared cloud systems
and informal permission handling no longer works.

ML governance adds datasets, features, experiments, and models. It also covers
prediction schemas, artifacts, environments, and monitoring signals.
[[person:simonstiebellehner|Simon Stiebellehner]]
links experiment tracking, [[model-registry|model registries]],
metadata, and lineage in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He also covers artifact logging, GDPR-aware dataset storage, and unified
prediction schemas.
Those controls make a [[ml-platforms|machine learning platform]]
reviewable because reviewers can see which data, code, artifact, and schema
supported a deployed model.

AI product governance adds prompts, retrieved context, and outputs. Guardrail
results, evaluation labels, feedback, and human override points become part of
the record too.
[[person:supreetkaur|Supreet Kaur]] places feature
necessity, PII handling, compliance input, and fairness checks in the same
operating model in
[[podcast:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]].
Her episode also covers interpretability, drift, and human oversight.

[[person:mariasukhareva|Maria Sukhareva]] adds prompt
injection, knowledge-base exfiltration, output validation, and query analysis in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
[[person:adityagautam|Aditya Gautam]] extends the
surface to agent guardrails, lineage, multi-tenant evaluations, and human-label
alignment in [[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]].

## Inventory and Ownership

Governance starts with inventory because teams can't secure or reuse unknown
data. They also can't retain or delete it deliberately. Jessi and Uri describe
taxonomy, classification, catalogs, and lineage in
[[podcast:cloud-data-governance|Cloud Data Governance]].
They also cover retention, freshness, purpose-based access, and minimum viable
governance.

Their discussion links [[data governance]]
to [[self-service-data-platforms|self-service data platforms]].
A governed catalog should expose meaning and policy to data consumers instead of
making them rely on private knowledge.

Ownership turns metadata into accountability. Bart separates data teams from
governance teams at 13:34 in
[[podcast:data-governance-data-access-management|Data Governance and Data Access Management]],
then discusses domain ownership models. [[person:zhamakdehghani|Zhamak Dehghani]]
gives the domain-owned version in
[[podcast:data-mesh-architecture-decentralized-data-products|Data Mesh Implementation]].

At 16:34 and 39:36, she links domain ownership to data product contracts,
service levels, and quality expectations. At 49:25 and 53:02, she names
federated governance, identity, and authorization as shared primitives. She
also includes retention, metadata, and validation across domain-owned data
products.


Those domain boundaries keep governance close to
[[Data Mesh]].

Domains own data products, but shared rules make products interoperable.
Identity and authorization define who can use the product. Retention, metadata,
and validation let decentralized products behave as part of one system.

Quality evidence belongs in the same ownership model. Jessi and Uri discuss
trust signals, source quality, and measurable checks at 34:59 in
[[podcast:cloud-data-governance|Cloud Data Governance]].
Consumers need freshness, schemas, volume, and lineage before they use a
dataset for a metric. Owners and known limits matter when the same data feeds a
model or an operational decision.
Those checks make governance part of
[[Data Quality and Observability]].

## Access, Privacy, and Policy Automation

Access governance decides who can use data and why they need it. It also sets
how long they keep access. Bart's
[[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]
episode is the clearest podcast anchor. At 27:49, he covers access requests and
approvals. He also covers review and revocation.

At 29:36, an analyst requests data for a specific churn-analysis purpose. At
32:08, Bart discusses privilege creep and time-bound access. Temporary debugging
access at 35:35 keeps incident response possible. Masking and filtering at
42:20 limit sensitive-data exposure.


Those controls sit beside [[security]]
because they reduce excess privilege and exfiltration risk without blocking
legitimate analysis. Bart also connects pipelines, Terraform, and IAM at 46:42
and 50:08. He adds alerts, automated tagging, and active metadata in the same
access-as-code discussion.

Access-as-code links
governance to
[[GitOps for Data Teams]]
and [[DataOps]]. Teams can turn repeated
controls into reviewable configuration instead of one-off permission changes.

Automation matters because manual governance becomes a queue. Jessi and Uri
discuss automation for tagging, requests, and reduced manual effort at 48:50 in
[[podcast:cloud-data-governance|Cloud Data Governance]].
They still include data stewards, producers, and decision makers at 33:03, so
automation routes repeated checks without replacing judgment.

Privacy changes the access question. Teams need to ask whether data should be
collected or centralized at all. They also need retention and exposure rules.
[[person:katharinejarmul|Katharine Jarmul]]
connects GDPR and CCPA/CPRA to consent UX in
[[podcast:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]]
at 11:33 and 47:00.

At 22:38, she discusses privacy-risk translation, and at 25:12 she covers
fingerprinting and re-identification.

Privacy-enhancing technologies at 33:08 and federated learning extend the
architecture options. Differential privacy at 40:50 makes the same point:
governance may need an architecture decision when a permission rule isn't
enough.

## ML Release Controls

ML governance adds release evidence. At 4:42 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
Simon defines MLOps as people, practices, and technology. He then ties
self-service compute, experiment tracking, and model registries into the
platform. He also covers orchestration, metadata, and lineage.

Artifact
logging, batch deployment, online deployment, and monitoring complete the
release record. A reviewer can then see which
model ran, which data and artifact supported it, and how predictions should be
monitored.


In regulated organizations, teams make the approval path more explicit.
[[person:nemanjaradojkovic|Nemanja Radojkovic]] connects
finance use cases, legacy systems, and regulatory constraints
in
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]].
He also covers CI/CD, approvals, and release management. On-premises platforms,
dev/test/prod separation, and monitoring add more constraints. Model registries
and minimal viable MLOps complete the practical path.

His discussion at 18:52 and 22:25 shows why release paths differ. A bank, a
startup, and a temporary tactical setup can all be valid while requiring
different evidence and approval points.

[[person:geojolly|Geo Jolly]] frames the same release
surface through platform product work in
[[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy]].
Roadmap choices and stakeholder balance influence whether teams adopt the
governed path. Rollout timing and compliance matter too. Quality assurance,
shadowing, and release checklists also guide adoption. ROI and platform
happiness reports matter too.

Governance fails when the
controlled platform is slow, undocumented, or mismatched to real data science
and engineering work. It becomes the default when teams can request data,
deploy models, communicate releases, and review post-launch behavior through a
usable [[platform engineering]]
surface.

## Responsible AI Review

Responsible AI turns governance toward model impact. At 4:43 in
[[podcast:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]],
Supreet defines the trust problem around AI decisions. At 8:20, she separates
explainable AI from the broader responsible-AI discipline. Before model
training, she includes skewness, missingness, and coverage.

She also covers exploratory bias detection, PII handling, and feature-necessity
review. At 17:20, product teams, subject-matter experts, and compliance input enter the
feature decision.

Supreet keeps fairness and business tradeoffs together. Her episode covers
accuracy versus interpretability and ethics versus profitability. It also
covers human review, drift, feedback loops, and regulated-industry sensitivity.
AutoML risk and professional responsibility remain part of the same discussion.

Those controls connect
[[responsible AI and governance]]
to [[model monitoring]] and
[[machine learning system design]].
Fairness and explainability evidence should influence launch, monitoring, and
override decisions.

Governance also needs evidence that the explanation fits the audience.
[[person:christophmolnar|Christoph Molnar]] treats
interpretability as model debugging and uncertainty evidence in
[[podcast:interpretable-machine-learning|Interpretable Machine Learning]]
at 9:27, 20:27, and 23:44. [[person:tamaraatanasoska|Tamara Atanasoska]]
shows why fairness metrics still require product and domain judgment in
[[podcast:fairness-in-ai-ml-engineering|Fairness in AI/ML Engineering]]
at 21:31, 24:04, and 28:52. Her 31:33 and 37:13 chapters add organizational
responsibility and human review. A fairness dashboard or a SHAP value
becomes governance evidence only when someone
uses it to decide, monitor, or override a system.

## LLM and Agent Controls

Generative AI widens governance from model release to interaction safety and
retrieval exposure. Maria's
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]
episode covers chatbot hacking and prompt injection. It also covers
hallucinations, legal exposure, financial exposure, and knowledge-base
exfiltration.

Those points appear at 9:28, 11:38, 13:20, and 18:01. Output validation and query analysis at
16:15 and 17:00 create the first mitigation layer. Non-LLM classifiers and
human review at 25:34 add controls outside the generative model.

Those examples place LLM governance beside
[[AI red teaming]],
[[LLM production patterns]],
and [[security]]. The controlled asset is
a live interaction with retrieved context, not only a stored model file.

Agents add autonomy and memory, plus tools and multi-step execution.
Aditya's
[[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]
episode discusses reliability in legal and healthcare settings, specialized
models, guardrails, and lineage. It also covers compliance and feedback.
Multi-tenant evaluations and LLM judges appear at 30:26 and 43:30. Deployment
risk appears at 50:18.

In that setting, governance needs permission boundaries and evaluation cases.
It also needs lineage for what the agent saw. Records of tool use and human
review points help people decide when to trust or override the result.

## Adjacent Topics

Use [[Data Governance]] for
datasets and catalogs, plus lineage and ownership. It also covers access and
data quality. Use
[[Privacy Engineering for ML]]
for consent, minimization, PETs, and federated learning. It also covers
differential privacy.
Use [[Responsible AI and Governance]]
for fairness, explainability, human oversight, and post-launch review.

For implementation details, use
[[MLOps vs DataOps]] and
[[Model Registry]] for release
controls. Use
[[self-service-data-platforms|Self-Service Data Platforms]]
and [[GitOps for Data Teams]]
for governed platform work. Use
[[AI Red Teaming]] and
[[LLM Evaluation Workflows]]
for LLM and agent systems.
