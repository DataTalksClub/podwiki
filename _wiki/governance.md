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
work, not a standalone compliance checklist. [Jessi Ashdown](https://datatalks.club/people/jessiashdown.html)
and [Uri Gilad](https://datatalks.club/people/urigilad.html) tie cloud governance
to classification and catalogs in
[Cloud Data Governance](https://datatalks.club/podcast/cloud-data-governance.html)
at 14:04 and 15:33. At 23:00, they add the reason for governance before the
policy design.

[Bart Vandekerckhove](https://datatalks.club/people/bartvandekerckhove.html)
grounds the access side in catalogs and dictionaries at 8:58 in
[Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html).
He adds lineage in the same chapter. At 27:49 and 32:08, his episode covers
purpose-based requests, reviews, and revocation. At 42:20 and 50:08, it covers
masking and access-as-code.

The same operating model expands when the governed asset changes. Data platforms
need [data governance]({{ '/wiki/data-governance/' | relative_url }}),
[security]({{ '/wiki/security/' | relative_url }}), and
[privacy engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).
ML platforms add [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[model registries]({{ '/wiki/model-registry/' | relative_url }}), and release
controls. AI products add [responsible AI]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
evaluation, human review, and guardrails for LLM or agent behavior.

## Governed Assets

Podcast guests converge on one broad definition: governance makes useful
systems reviewable without hiding risk. Teams classify assets and assign
owners. They encode repeated rules, preserve metadata and lineage, then revisit
access or model behavior after systems change.

Data governance starts with datasets, tables, derived metrics, and catalogs.
Business glossaries and lineage make the inventory usable. In
[Cloud Data Governance](https://datatalks.club/podcast/cloud-data-governance.html),
Jessi and Uri start from the inventory problem. At 6:40 and 7:47, they argue
that a company can't secure or reuse data confidently if it doesn't know what
data it has.

Retention and deletion depend on the same inventory. At 24:14 and
38:25, they move from taxonomy and classification into retention, freshness, and
purpose-based access.


Bart reaches the same trust goal from a different failure mode. In
[Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html),
he describes older centralized governance at 6:52, then focuses on request
paths and approvals. He also covers time-bound permissions, privilege creep,
and revocation. That version is strongest when sensitive data already lives in shared cloud systems
and informal permission handling no longer works.

ML governance adds datasets, features, experiments, and models. It also covers
prediction schemas, artifacts, environments, and monitoring signals.
[Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
links experiment tracking, [model registries]({{ '/wiki/model-registry/' | relative_url }}),
metadata, and lineage in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
He also covers artifact logging, GDPR-aware dataset storage, and unified
prediction schemas.
Those controls make a [machine learning platform]({{ '/wiki/ml-platforms/' | relative_url }})
reviewable because reviewers can see which data, code, artifact, and schema
supported a deployed model.

AI product governance adds prompts, retrieved context, and outputs. Guardrail
results, evaluation labels, feedback, and human override points become part of
the record too.
[Supreet Kaur](https://datatalks.club/people/supreetkaur.html) places feature
necessity, PII handling, compliance input, and fairness checks in the same
operating model in
[Responsible and Explainable AI](https://datatalks.club/podcast/responsible-explainable-ai-bias-detection.html).
Her episode also covers interpretability, drift, and human oversight.

[Maria Sukhareva](https://datatalks.club/people/mariasukhareva.html) adds prompt
injection, knowledge-base exfiltration, output validation, and query analysis in
[Hardening Generative AI Chatbots](https://datatalks.club/podcast/generative-ai-chatbots-in-production-security.html).
[Aditya Gautam](https://datatalks.club/people/adityagautam.html) extends the
surface to agent guardrails, lineage, multi-tenant evaluations, and human-label
alignment in [The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html).

## Inventory and Ownership

Governance starts with inventory because teams can't secure or reuse unknown
data. They also can't retain or delete it deliberately. Jessi and Uri describe
taxonomy, classification, catalogs, and lineage in
[Cloud Data Governance](https://datatalks.club/podcast/cloud-data-governance.html).
They also cover retention, freshness, purpose-based access, and minimum viable
governance.

Their discussion links [data governance]({{ '/wiki/data-governance/' | relative_url }})
to [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).
A governed catalog should expose meaning and policy to data consumers instead of
making them rely on private knowledge.

Ownership turns metadata into accountability. Bart separates data teams from
governance teams at 13:34 in
[Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html),
then discusses domain ownership models. [Zhamak Dehghani](https://datatalks.club/people/zhamakdehghani.html)
gives the domain-owned version in
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html).

At 16:34 and 39:36, she links domain ownership to data product contracts,
service levels, and quality expectations. At 49:25 and 53:02, she names
federated governance, identity, and authorization as shared primitives. She
also includes retention, metadata, and validation across domain-owned data
products.


Those domain boundaries keep governance close to
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}).

Domains own data products, but shared rules make products interoperable.
Identity and authorization define who can use the product. Retention, metadata,
and validation let decentralized products behave as part of one system.

Quality evidence belongs in the same ownership model. Jessi and Uri discuss
trust signals, source quality, and measurable checks at 34:59 in
[Cloud Data Governance](https://datatalks.club/podcast/cloud-data-governance.html).
Consumers need freshness, schemas, volume, and lineage before they use a
dataset for a metric. Owners and known limits matter when the same data feeds a
model or an operational decision.
Those checks make governance part of
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

## Access, Privacy, and Policy Automation

Access governance decides who can use data and why they need it. It also sets
how long they keep access. Bart's
[Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html)
episode is the clearest podcast anchor. At 27:49, he covers access requests and
approvals. He also covers review and revocation.

At 29:36, an analyst requests data for a specific churn-analysis purpose. At
32:08, Bart discusses privilege creep and time-bound access. Temporary debugging
access at 35:35 keeps incident response possible. Masking and filtering at
42:20 limit sensitive-data exposure.


Those controls sit beside [security]({{ '/wiki/security/' | relative_url }})
because they reduce excess privilege and exfiltration risk without blocking
legitimate analysis. Bart also connects pipelines, Terraform, and IAM at 46:42
and 50:08. He adds alerts, automated tagging, and active metadata in the same
access-as-code discussion.

Access-as-code links
governance to
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). Teams can turn repeated
controls into reviewable configuration instead of one-off permission changes.

Automation matters because manual governance becomes a queue. Jessi and Uri
discuss automation for tagging, requests, and reduced manual effort at 48:50 in
[Cloud Data Governance](https://datatalks.club/podcast/cloud-data-governance.html).
They still include data stewards, producers, and decision makers at 33:03, so
automation routes repeated checks without replacing judgment.

Privacy changes the access question. Teams need to ask whether data should be
collected or centralized at all. They also need retention and exposure rules.
[Katharine Jarmul](https://datatalks.club/people/katharinejarmul.html)
connects GDPR and CCPA/CPRA to consent UX in
[Data Privacy Engineering, GDPR, and Machine Learning](https://datatalks.club/podcast/data-privacy-engineering-gdpr-machine-learning.html)
at 11:33 and 47:00.

At 22:38, she discusses privacy-risk translation, and at 25:12 she covers
fingerprinting and re-identification.

Privacy-enhancing technologies at 33:08 and federated learning extend the
architecture options. Differential privacy at 40:50 makes the same point:
governance may need an architecture decision when a permission rule isn't
enough.

## ML Release Controls

ML governance adds release evidence. At 4:42 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
Simon defines MLOps as people, practices, and technology. He then ties
self-service compute, experiment tracking, and model registries into the
platform. He also covers orchestration, metadata, and lineage.

Artifact
logging, batch deployment, online deployment, and monitoring complete the
release record. A reviewer can then see which
model ran, which data and artifact supported it, and how predictions should be
monitored.


In regulated organizations, teams make the approval path more explicit.
[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) connects
finance use cases, legacy systems, and regulatory constraints
in
[MLOps in Finance](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html).
He also covers CI/CD, approvals, and release management. On-premises platforms,
dev/test/prod separation, and monitoring add more constraints. Model registries
and minimal viable MLOps complete the practical path.

His discussion at 18:52 and 22:25 shows why release paths differ. A bank, a
startup, and a temporary tactical setup can all be valid while requiring
different evidence and approval points.

[Geo Jolly](https://datatalks.club/people/geojolly.html) frames the same release
surface through platform product work in
[ML Product Manager and MLOps Platform Strategy](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html).
Roadmap choices and stakeholder balance influence whether teams adopt the
governed path. Rollout timing and compliance matter too. Quality assurance,
shadowing, and release checklists also guide adoption. ROI and platform
happiness reports matter too.

Governance fails when the
controlled platform is slow, undocumented, or mismatched to real data science
and engineering work. It becomes the default when teams can request data,
deploy models, communicate releases, and review post-launch behavior through a
usable [platform engineering]({{ '/wiki/platform-engineering/' | relative_url }})
surface.

## Responsible AI Review

Responsible AI turns governance toward model impact. At 4:43 in
[Responsible and Explainable AI](https://datatalks.club/podcast/responsible-explainable-ai-bias-detection.html),
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
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
to [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
Fairness and explainability evidence should influence launch, monitoring, and
override decisions.

Governance also needs evidence that the explanation fits the audience.
[Christoph Molnar](https://datatalks.club/people/christophmolnar.html) treats
interpretability as model debugging and uncertainty evidence in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html)
at 9:27, 20:27, and 23:44. [Tamara Atanasoska](https://datatalks.club/people/tamaraatanasoska.html)
shows why fairness metrics still require product and domain judgment in
[Fairness in AI/ML Engineering](https://datatalks.club/podcast/fairness-in-ai-ml-engineering.html)
at 21:31, 24:04, and 28:52. Her 31:33 and 37:13 chapters add organizational
responsibility and human review. A fairness dashboard or a SHAP value
becomes governance evidence only when someone
uses it to decide, monitor, or override a system.

## LLM and Agent Controls

Generative AI widens governance from model release to interaction safety and
retrieval exposure. Maria's
[Hardening Generative AI Chatbots](https://datatalks.club/podcast/generative-ai-chatbots-in-production-security.html)
episode covers chatbot hacking and prompt injection. It also covers
hallucinations, legal exposure, financial exposure, and knowledge-base
exfiltration.

Those points appear at 9:28, 11:38, 13:20, and 18:01. Output validation and query analysis at
16:15 and 17:00 create the first mitigation layer. Non-LLM classifiers and
human review at 25:34 add controls outside the generative model.

Those examples place LLM governance beside
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}),
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and [security]({{ '/wiki/security/' | relative_url }}). The controlled asset is
a live interaction with retrieved context, not only a stored model file.

Agents add autonomy and memory, plus tools and multi-step execution.
Aditya's
[The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)
episode discusses reliability in legal and healthcare settings, specialized
models, guardrails, and lineage. It also covers compliance and feedback.
Multi-tenant evaluations and LLM judges appear at 30:26 and 43:30. Deployment
risk appears at 50:18.

In that setting, governance needs permission boundaries and evaluation cases.
It also needs lineage for what the agent saw. Records of tool use and human
review points help people decide when to trust or override the result.

## Adjacent Topics

Use [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) for
datasets and catalogs, plus lineage and ownership. It also covers access and
data quality. Use
[Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
for consent, minimization, PETs, and federated learning. It also covers
differential privacy.
Use [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
for fairness, explainability, human oversight, and post-launch review.

For implementation details, use
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}) and
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}) for release
controls. Use
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
for governed platform work. Use
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) and
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for LLM and agent systems.
