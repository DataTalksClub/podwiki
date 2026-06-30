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

Governance is the operating model for accountable choices in data systems, ML
systems and AI systems. It names owners and policies. It also defines approval
paths and the evidence teams keep when a system changes.

In the DataTalks.Club archive, governance connects
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[security]({{ '/wiki/security/' | relative_url }}). It also connects
[privacy engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[responsible AI]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
rather than living as a separate compliance checklist.

The archive grounds that definition in operational examples.
[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
defines data governance through trust and catalogs in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
His episode also covers purpose-based access, reviews, revocation, and masking.
Access-as-code is part of the same operating model.

[Jessi Ashdown]({{ '/people/jessiashdown/' | relative_url }}) and
[Uri Gilad]({{ '/people/urigilad/' | relative_url }}) broaden the same idea in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
They connect governance to cloud classification, catalogs, and policies. Request
workflows, automation, and ROI are part of the same discussion.

ML and AI episodes add model artifacts and release controls.
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
grounds the platform side.
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
adds fairness review and human oversight.
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
adds prompt-injection defenses.
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
adds agent lineage.

## Common Definition

Across the archive, governance means making data and AI systems usable while
keeping risk visible and reviewable. Teams classify important assets, assign
owners, and encode repeated policies. They preserve metadata and lineage, keep
human review for judgment calls, and revisit access after systems change.

Teams revisit quality plus model behavior. Jessi and Uri call data
governance a mix of people and process, tooling and cataloging, and
classification in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})
at 14:04 and 15:33. At 23:00, they argue that the program should start with
the reason for governance.

Bart's access-management discussion takes a narrower operational path. In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he separates catalogs, dictionaries, and lineage at 8:58. He then moves to
ownership and access controls.

Request approval, review, revocation, and masking set the enforcement path.
Filtering works with role inheritance, alerts and access-as-code. Governance
becomes real when someone can ask for data for a stated purpose. An accountable
owner can approve or deny it, and the organization can later prove or remove
that access.

For ML and AI, the governed asset isn't only a table. It includes datasets and
features. It also includes experiments and models, prompts and outputs,
monitoring signals, and release decisions.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
connects [model registries]({{ '/wiki/model-registry/' | relative_url }}),
metadata, lineage, and artifact logging in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He also covers prediction schemas and GDPR-aware dataset storage.

[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) extends the same
operating model to feature necessity, PII handling, compliance input, and
fairness in
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}).
Her episode also brings in interpretability, drift, and human oversight.

## Guest Differences

The guests differ less on whether governance matters and more on which failure
mode should drive the operating model. Jessi and Uri start from the inventory
problem. At 6:40 and 7:47 in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}),
they frame governance as knowing what data exists and what it means. Teams also
need to know how sensitive the data is before they secure or reuse it. The same
knowledge supports retention and deletion.

Bart starts from access friction and privilege creep. His
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode moves from older centralized governance at 6:52 to request workflows,
time-bound permissions, and revocation. It also covers temporary debugging
access, masking, and filtering. Role inheritance and access-as-code round out
the model. His version is strongest when sensitive data already sits in shared
cloud systems and informal permission handling no longer works.

[Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }}) starts from
organizational scale in
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}).
She links domain ownership and data product contracts to shared identity and
authorization primitives. She also covers retention and metadata. The same
discussion includes automated checks and federated governance.

Those points appear at 16:34 and 39:36, then again at 49:25 and 53:02. That
boundary keeps governance close to
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}). Domains own data
products, but shared rules still make products interoperable.

[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) draws the
boundary around privacy risk in
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}).
Her discussion of legal and technical translation links governance to consent,
fingerprinting, and re-identification. Privacy-enhancing technologies,
federated learning, and differential privacy make governance an architecture
decision, not only an access decision.

The ML platform guests start from release context. Simon treats governance as
part of reproducible ML platforms in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) shows
how finance settings add legacy systems and approvals in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).
He also covers release management, dev/test/prod separation, monitoring, and
minimal viable MLOps.

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) frames governance through
platform product work in
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }}).
His version centers roadmap choices, stakeholder balance, and adoption. Rollout
timing, compliance, and release checklists define the release side.

AI-system guests add new failure modes.
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }})
starts from chatbot safety, prompt injection, and knowledge-base exfiltration in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
She also covers output validation and query analysis. Non-LLM classifiers,
human review, and ROI round out the discussion.

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) extends the
problem to agents with guardrails and data lineage in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}).
He also covers feedback loops, multi-tenant evaluations, and deployment risk.

## Ownership, Inventory, and Data Products

Governance starts with inventory because unknown data can't be secured or
reused deliberately. Teams also can't retain or delete it with confidence. Jessi
and Uri make that point in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }})
through taxonomy, classification, catalogs and business glossaries. They make the
inventory usable.

They also cover lineage and retention. Freshness,
purpose-based access, and minimum viable governance complete the operating
model.

Their discussion connects
[data governance]({{ '/wiki/data-governance/' | relative_url }})
to [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
because a governed catalog should make both meaning and policy visible to data
consumers.

Ownership turns metadata into accountability. Bart separates data teams from
governance teams in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
at 13:34. He also discusses domain ownership models. Zhamak's
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})
episode gives the domain-owned version.

Data product contracts, service levels, and quality expectations become shared
controls. Identity and authorization define who can use the product. Retention,
metadata, and validation let decentralized products still behave as part of one
system.

Quality is part of that ownership model. Jessi and Uri discuss trust signals,
source quality, and measurable checks at 34:59 in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).

Those checks connect governance to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
because consumers need evidence about freshness and lineage. Owners, schemas,
and known limits matter too. That evidence helps them decide whether a dataset
can support a metric, a model, or an operational decision.

## Access, Privacy, and Policy Automation

Access governance decides who can use data, why they need it, and how long they
keep it.

Bart's
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode is the clearest archive anchor. He covers purpose-based requests,
approvals, periodic reviews, and revocation. He also covers production-debugging
access, masking, and filtering. Role inheritance, alerts, and access-as-code
finish the control set. That makes governance
adjacent to [security]({{ '/wiki/security/' | relative_url }}) because the
controls reduce excess privilege and exfiltration risk without blocking
legitimate analysis.


Automation matters because manual governance turns into a queue. Jessi and Uri
discuss automation for tagging, requests, and lower manual effort at 48:50 in
[Cloud Data Governance]({{ '/podcasts/cloud-data-governance/' | relative_url }}).
Bart adds active metadata and automated tagging in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
He also connects pipelines, Terraform, IAM, and access-as-code to the same
control model.

Those patterns connect governance to
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). Teams turn repeated controls into
reviewable workflows and auditable configuration.

Privacy changes the question from "who can access this data?" to "should this
data be collected at all?" Teams also ask whether data should be centralized,
retained, or exposed.

Katharine's
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
episode links GDPR and CCPA/CPRA to consent UX. It also covers privacy-risk
translation, fingerprinting, and re-identification. Privacy-enhancing
technologies, federated learning, and differential privacy add architectural
options.

The episode also raises generative-AI retention concerns. That
makes [privacy engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
a governance practice because policy may need to change the architecture, not
just the permission rule.


## ML Release Controls and Reproducibility

ML governance adds model artifacts and environments to the governed surface. It
also adds experiments and deployment paths. Simon defines MLOps as people,
processes, and technology at 4:42 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

He then connects self-service compute, experiment tracking, and model
registries. Batch and online deployment also enter the governance surface.
Orchestration, metadata, and lineage make the workflow traceable. Artifact
logging, GDPR-aware dataset storage, and unified prediction schemas complete the
review path.

Those practices make an [ML platform]({{ '/wiki/ml-platforms/' | relative_url }}) a governance
surface. Reviewers can tell which model ran, which data and artifact supported
it, and how predictions should be monitored.

In regulated organizations, release governance becomes more explicit.
Nemanja's
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
episode connects finance use cases, legacy constraints, CI/CD, and approvals.
It also covers release management, on-premises platforms, dev/test/prod
separation, and monitoring. Model registries and minimal viable MLOps complete
the practical path. Controls should fit the organization's existing risk model
and infrastructure.

A startup's release path, a bank's release path, and a temporary tactical setup
can all be valid, but the evidence and approval points differ.

## Responsible AI, Fairness, and Human Review

Responsible AI turns governance toward model impact. Supreet's
[Responsible and Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
episode defines the trust problem at 4:43 and separates explainable AI from the
broader governance mindset at 8:20.

Before model training, her controls include skewness, missingness, coverage and
exploratory bias detection. PII handling also matters, and feature-necessity
reviews bring in product teams, subject matter, and compliance input.

Supreet also links governance to business tradeoffs and oversight. Her episode
covers accuracy versus interpretability and ethics versus profitability. It also
covers human review, drift, and feedback loops. Regulated-industry sensitivity
and AutoML risks appear in the same discussion. Professional responsibility is
part of it too.

That connects to
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
and [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).
It also connects to
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
because fairness and explainability evidence should enter launch and monitoring
decisions.

## LLM and Agent Governance

Generative AI widens governance from model release to interaction safety and
retrieval exposure. Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode covers chatbot hacking, prompt injection, hallucinations, and legal
exposure. It also covers financial exposure and knowledge-base exfiltration.

Output validation and query analysis are the first mitigation layer. Non-LLM
classifiers and human review round out the operating view. Translation quality
control and ROI remain part of the adoption question.

Those examples connect governance to
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
They also connect to [security]({{ '/wiki/security/' | relative_url }}) because
the controlled asset is now a live interaction, not only a stored model.

Agents add autonomy and memory, plus tools and multi-step execution.
Aditya's
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
episode discusses reliability in legal and healthcare settings. It also covers
specialized models plus agent governance. Guardrails, data lineage, and user
feedback define the operating loop.

Multi-tenant evaluations and LLM judges
aligned with human labels complete the picture. Deployment risks remain part of
the same governance surface.

In that setting, governance needs
evaluation workflows and permission boundaries. It also needs lineage and
feedback loops that can explain what the agent saw. Those loops should also
show which tools it used and why a human should trust or override the result.

## Adoption and Platform Governance

Governance works only if teams use the governed path. Geo's
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
episode treats internal ML platform users as customers. That shifts governance
from "what policy exists?" to "will teams adopt the controlled workflow?"

His
discussion of ROI and usability costs makes platform adoption part of
governance. Stakeholder balance and user research matter for the same reason.

Rollout timing, compliance, and platform happiness reports influence the operating
model. Quality assurance, shadowing, and release checklists define the release
path.

This product view connects governance to
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}).
If the governed platform is slow, undocumented, or mismatched to real data
science and engineering workflows, teams bypass it. If it's usable and
reviewable, governance becomes the default path for data requests and model
deployment. It can also include release communication and post-launch review.

## Related Pages

Use these pages for adjacent data, ML, platform and security topics. The final
links cover responsible-AI and LLM operations.

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
