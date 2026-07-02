---
layout: wiki
title: "Privacy Engineering for ML"
summary: "How DataTalks.Club guests describe privacy engineering, access governance, privacy-enhancing technologies, and production LLM privacy tradeoffs."
related:
  - Data Governance
  - Responsible AI and Governance
  - Security
  - LLM Production Patterns
  - LLMs
  - Machine Learning
---

Privacy engineering for ML is the work of turning privacy obligations into
system design. It asks what data a product should collect and what data a model
should see. It also asks who may access that data, how long the team should
retain it, and which controls apply in production. In these podcast
discussions, it sits between [[Data Governance]]
and [[Security]]. It also connects to
[[Responsible AI and Governance]],
[[Machine Learning]], and
[[LLM Production Patterns]].

This topic is centered on ML and AI systems, not privacy law in the abstract.
[[person:katharinejarmul|Katharine Jarmul]] gives the
clearest definition in
[[podcast:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]].
At 22:38, she describes privacy engineering as translation between legal,
social, and technical views. At 30:15 and 47:00, privacy becomes part of normal
product and architecture work rather than a late compliance check.
Mario Lazo and Justin Ryan's
[[book:20240715-ai-data-privacy-and-protection|AI Data Privacy and Protection]]
provides a structured reference for the same legal-to-technical translation:
data classification, access controls, and privacy-by-design patterns for AI
systems.

Across these episodes, guests converge on a practical rule. Useful AI systems
shouldn't create avoidable privacy, security, or compliance risk.
[[person:bartvandekerckhove|Bart Vandekerckhove]]
adds the operating layer in
[[podcast:data-governance-data-access-management|Data Governance and Data Access Management]],
where access requests and reviews turn privacy rules into daily controls.
Masking and revocation do the same.

[[person:supreetkaur|Supreet Kaur]]
ties PII handling to [[Responsible AI and Governance]]
in
[[podcast:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]].
[[person:meryemarik|Meryem Arik]] and
[[person:mariasukhareva|Maria Sukhareva]] extend the
same topic into [[LLMs]],
[[retrieval-augmented-generation|Retrieval-Augmented Generation]],
and [[AI Red Teaming]].

## Privacy as System Design

Privacy engineering starts before model training. A team should know why it
collects each field and whether the use case still works with less data. The
team should identify sensitive fields, access rules, and safeguards against
unintended exposure.

Katharine grounds that work in regulation and user
experience. At 11:33 and 14:35 in
[[podcast:data-privacy-engineering-gdpr-machine-learning|her privacy episode]],
she discusses GDPR, CCPA, and CPRA. She also covers cookie-consent defaults
and one-click rejection.

Katharine also covers browser fingerprinting at 16:24 and re-identification at
25:12. Those examples matter for [[Machine Learning]]
systems. Training data and feature tables can preserve identity even after the
obvious personal fields are removed. Event logs, embeddings, and retrieval
indexes can do the same.

Teams fail when they collect or centralize sensitive
data because it's easier for experimentation. Later, they discover that
deletion, retention, and user expectations were never designed into the system.

## Data Minimization and Consent

In these discussions, teams start privacy engineering by minimizing data. The
team should first ask whether the product can work with less data. Shorter
retention, local inference, or a less identifying representation may be enough.
Katharine's session-based personalization example at 30:15 shows the design.
Teams can infer intent from the current session where possible instead of
accumulating permanent user histories
([[podcast:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]]).

A personalization model or churn model may improve when it sees more user
history. A fraud model or support assistant may improve too. The improvement
still has to be weighed against breach impact, deletion requirements, customer
trust, and insurance or regulatory exposure. Katharine ties that business case
to risk management and customer trust at 35:09 in the same episode.

Consent belongs in the same product design. At 14:35, Katharine discusses
one-click rejection and user behavior around cookie banners. For ML teams,
privacy shouldn't depend on users understanding every later model use. Teams
should offer a reasonable low-data path. They should avoid turning consent into
a forced trade for basic functionality.

## Access Governance for ML Data

Privacy engineering fails when sensitive data becomes the default across
notebooks, feature stores, and production jobs.

[[podcast:data-governance-data-access-management|Bart's access-governance episode]]
shows the practical controls at 8:58 / 11:20 / 13:34 / 27:49. At 11:20, he
links modern cloud data consolidation to access management. At 8:58 and 13:34,
he explains how catalogs and lineage connect datasets to owners. At 27:49,
purpose-based access requests make teams state why they need the data and how
long they need it.

For ML systems, access rules should cover raw sources and feature tables. They
should also cover labels, experiment datasets, and model-debugging samples.
Embeddings, retrieval indexes, logs, and annotation queues need coverage too.
The same customer email can appear in several derived forms. A support message
can too, so privacy reviews need
[[Data Governance]] and
[[Data Quality and Observability]]
signals, not only a policy document.

Bart's privilege-creep discussion at 32:08 is especially relevant to model
experimentation. Temporary access granted for a prototype can persist after the
model is abandoned. At 25:05 and 27:49, he describes approval flows and
purpose-based requests. Time-bound access, revocation, reviews, and
access-as-code reduce drift. Masking and filtering at 42:20 and active metadata
at 46:42 make those controls reusable across analytics, training, and
operations.

## PII Handling in Responsible AI

Supreet treats privacy as part of responsible AI review, not as a separate
legal checklist. At 14:39 in
[[podcast:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]],
PII handling and masking become product choices. At 17:20, feature necessity
becomes a subject-matter and compliance decision. Product owners, domain
experts, and compliance stakeholders should decide whether a sensitive feature
belongs in the model.

For production ML, teams should review both model quality and whether the
inputs are justified. A model can be accurate and still use data it doesn't
need. A feature can be predictive and still create privacy, fairness, or
regulatory risk. Supreet's framing links privacy engineering to
[[Responsible AI and Governance]].
Teams also need [[Data Quality and Observability]]
and [[MLOps]] because the review depends on
evidence about the data, the model behavior, and the approval record.

## Privacy-Enhancing Technologies

Katharine describes privacy-enhancing technologies as architectural choices,
not magic add-ons. At 33:08 in
[[podcast:data-privacy-engineering-gdpr-machine-learning|her privacy episode]],
she discusses encrypted ML, federated learning, and privacy-aware architecture.
At 40:50, she introduces differential privacy as a formal way to reason about
privacy loss.

She doesn't imply that every team should begin with advanced PETs. She
recommends clarifying what data is sensitive and what the product needs. Teams
should then decide who owns the risk. Techniques such as federated learning,
encrypted computation, differential privacy, or localized deployment fit when
the use case still requires learning from sensitive patterns.

Privacy-enhancing technologies still need governance around them. A
federated-learning design still needs participant consent, update controls,
evaluation, and incident handling. Differential privacy still needs a privacy
budget and a decision about utility loss. Teams still need to own encrypted
computation in production. The technical technique works only when it's
embedded in [[MLOps]], governance, and
security practice.

## Regulated and High-Impact Deployment

High-impact deployment changes privacy engineering from a model-building
concern into cross-functional approval. Supreet's
[[podcast:responsible-explainable-ai-bias-detection|responsible-AI episode]]
is useful here because it treats feature necessity, PII handling, fairness, and
compliance as connected decisions. Human oversight belongs in that same review.
At 17:20, product owners should help decide whether to use a feature.
Subject-matter experts and compliance stakeholders belong in that decision too.

Bart adds the access-control operating model for regulated data. In his
episode, data owners and governance teams appear in the approval flow. DPOs and
security teams appear too, along with engineers. Separation of concerns matters.

Privacy and security may need to approve the same dataset. Domain owners may
need to approve it for different reasons
([[podcast:data-governance-data-access-management|Bart's access-governance episode]],
35:35, 37:19).

For production ML, the approval record should state which sensitive fields are
used and why they're necessary. It should state whether those fields are
masked, transformed, or excluded. It should also state who approved access, how
long access lasts, what gets logged in production, and how the team handles
deletion or incident-response requests. Those checks link privacy engineering
to [[Responsible AI and Governance]],
[[Security]], and
[[MLOps]].

## LLM Privacy and Security Tradeoffs

LLMs make privacy engineering visible because the interface accepts free-form
text. Users may paste contracts, credentials, or customer messages into the same
box. They may paste medical details, code, or proprietary documents too.

Katharine's generative-AI discussion turns retention and deletion into product
requirements. Training reuse and consent belong there. Incident notification
does too
([[podcast:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]]).

Meryem's production LLM episode adds the infrastructure tradeoff. API models
are fast for prototyping, while open-source or self-hosted models can give
teams more control over privacy and fine-tuning. They can also give teams more
control over latency and cost
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Meryem's LLM deployment episode]],
16:48). API drift at 18:46 adds another operational risk. When a provider
changes model behavior, the privacy review and the evaluation results may no
longer describe the system that's running.

Retrieval systems add a second exposure path. A model might not store the
private data, but a vector index can still leak it. A document chunk, prompt
template, or log can leak it too. Maria's chatbot-security episode shows this
through knowledge-base exfiltration at 13:20. She then argues for layered
defenses at 16:15 and 17:00
([[podcast:generative-ai-chatbots-in-production-security|Maria's chatbot-security episode]]).

The guests share the same production rule: include privacy in the
prototype-to-production decision. Teams should decide where prompts are stored,
whether user inputs can train future models, and how retrieval permissions are
enforced. They should also decide what appears in logs and what tests catch
prompt injection or data exfiltration. Cost and latency belong in the same
review as evaluation and privacy on
[[LLM Production Patterns]]
systems.
