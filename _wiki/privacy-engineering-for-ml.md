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
  - Synthetic Data
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
[[person:katharinejarmul=>Katharine Jarmul]] gives the
clearest definition. Privacy engineering translates between legal, social, and
technical views. It turns privacy into normal product and architecture work
rather than a late compliance check [[cite:data-privacy-engineering-gdpr-machine-learning|Data Privacy Engineering, GDPR, and Machine Learning]].

Mario Lazo and Justin Ryan's
[[book:20240715-ai-data-privacy-and-protection=>AI Data Privacy and Protection]]
provides a structured reference for the same legal-to-technical translation. It
covers data classification, access controls, and privacy-by-design patterns for
AI systems.

Across these episodes, guests converge on a practical rule. Useful AI systems
shouldn't create avoidable privacy, security, or compliance risk.
[[person:bartvandekerckhove=>Bart Vandekerckhove]]
adds the operating layer. Access requests, reviews, masking, and revocation
turn privacy rules into daily controls [[cite:data-governance-data-access-management|Data Governance and Data Access Management]].

[[person:supreetkaur=>Supreet Kaur]]
ties PII handling to [[Responsible AI and Governance]] [[cite:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]].
[[person:meryemarik=>Meryem Arik]] and
[[person:mariasukhareva=>Maria Sukhareva]] extend the
same topic into [[LLMs]],
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
and [[AI Red Teaming]].

## Privacy as System Design

Privacy engineering starts before model training. A team should know why it
collects each field and whether the use case still works with less data. The
team should identify sensitive fields, access rules, and safeguards against
unintended exposure.

Katharine grounds that work in regulation and user experience. Her privacy
episode connects GDPR, CCPA, and CPRA to product design. She also connects
cookie-consent defaults and one-click rejection to the same design work [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

Katharine also uses browser fingerprinting and re-identification to show why
privacy engineering matters for [[Machine Learning]] systems. Training data and
feature tables can preserve identity even after the obvious personal fields are
removed. Event logs, embeddings, and retrieval indexes can do the same [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

Teams fail when they collect or centralize sensitive
data because it's easier for experimentation. Later, they discover that
deletion, retention, and user expectations were never designed into the system.

## Data Minimization and Consent

In these discussions, teams start privacy engineering by minimizing data. The
team should first ask whether the product can work with less data. Shorter
retention, local inference, or a less identifying representation may be enough.
Katharine's session-based personalization example shows the design. Teams can
infer intent from the current session where possible instead of accumulating
permanent user histories [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

A personalization model or churn model may improve when it sees more user
history. A fraud model or support assistant may improve too. The improvement
still has to be weighed against breach impact, deletion requirements, customer
trust, and insurance or regulatory exposure. Katharine ties that business case
to risk management and customer trust [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

Consent belongs in the same product design. Katharine discusses one-click
rejection and user behavior around cookie banners. For ML teams, privacy
shouldn't depend on users understanding every later model use. Teams should
offer a reasonable low-data path. They should avoid turning consent into a
forced trade for basic functionality [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

## Access Governance for ML Data

Privacy engineering fails when sensitive data becomes the default across
notebooks, feature stores, and production jobs.

Bart's access-governance episode shows the practical controls. He links modern
cloud data consolidation to access management and explains how catalogs and
lineage connect datasets to owners. Teams use purpose-based access requests to
state why they need the data and how long they need it [[cite:data-governance-data-access-management|Bart's access-governance episode]].

For ML systems, access rules should cover raw sources and feature tables. They
should also cover labels, experiment datasets, and model-debugging samples.
Embeddings, retrieval indexes, logs, and annotation queues need coverage too.
The same customer email can appear in several derived forms. A support message
can too, so privacy reviews need
[[Data Governance]] and
[[Data Quality and Observability]]
signals, not only a policy document.

Bart's privilege-creep discussion is especially relevant to model
experimentation. Temporary access granted for a prototype can persist after the
model is abandoned [[cite:data-governance-data-access-management|Bart's access-governance episode]].

Approval flows and purpose-based requests reduce drift. Time-bound access does
too, as do revocation, reviews, and access-as-code.
Masking and filtering make those controls reusable across analytics and
training. Active metadata extends that reuse to operations [[cite:data-governance-data-access-management|Bart's access-governance episode]].

## PII Handling in Responsible AI

Supreet treats privacy as part of responsible AI review, not as a separate
legal checklist. PII handling and masking become product choices, while feature
necessity becomes a subject-matter and compliance decision. Product owners,
domain experts, and compliance stakeholders should decide whether a sensitive
feature belongs in the model [[cite:responsible-explainable-ai-bias-detection|Responsible and Explainable AI]].

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
not magic add-ons. Her privacy episode discusses encrypted ML, federated
learning, privacy-aware architecture, and differential privacy as a formal way
to reason about privacy loss [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

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
concern into cross-functional approval. Supreet's responsible-AI episode is
useful here because it treats feature necessity, PII handling, fairness, and
compliance as connected decisions. Human oversight belongs in that same review.
Product owners, subject-matter experts, and compliance stakeholders should help
decide whether to use a sensitive feature [[cite:responsible-explainable-ai-bias-detection|Supreet's responsible-AI episode]].

Sabina Firtala describes the same privacy engineering work inside a frontline
scoring system. The tool combines case-management data with public records and
surveys to support risk triage. In that setting, teams need to justify which
fields enter the model and minimize unnecessary data. They also need access
controls for sensitive public and social-service records. Legal compliance and
governance have to stay tied to the scoring workflow [[cite:building-domestic-risk-assessment-tool|Building a Domestic Risk Assessment Tool]].

Bart adds the access-control operating model for regulated data. In his
episode, data owners and governance teams appear in the approval flow. DPOs and
security teams appear too, along with engineers. Separation of concerns matters.

Stefan Gudmundsson's digital-therapeutics example adds the healthcare version
of that review. When an ML product works with sensitive health context,
de-identification is necessary but not sufficient. Activity, heart-rate
variability, and mental-health signals all need explicit consent and privacy
boundaries. Teams also need HIPAA/GDPR expectations and empathy for users who
may be sharing vulnerable information [[cite:ai-in-healthcare-and-digital-therapeutics|AI in Healthcare and Digital Therapeutics]].

Privacy and security may need to approve the same dataset. Domain owners may
need to approve it for different reasons [[cite:data-governance-data-access-management|Bart's access-governance episode]].

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
does too [[cite:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy episode]].

Meryem's production LLM episode adds the infrastructure tradeoff. API models
are fast for prototyping, while open-source or self-hosted models can give
teams more control over privacy and fine-tuning. They can also give teams more
control over latency and cost [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Meryem's LLM deployment episode]].
API drift adds another operational risk. When a provider changes model
behavior, the privacy review and the evaluation results may no longer describe
the system that's running [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Meryem's LLM deployment episode]].

Retrieval systems add a second exposure path. A model might not store the
private data, but a vector index can still leak it. A document chunk, prompt
template, or log can leak it too. Maria's chatbot-security episode shows this
through knowledge-base exfiltration, then argues for layered defenses [[cite:generative-ai-chatbots-in-production-security|Maria's chatbot-security episode]].

The guests share the same production rule: include privacy in the
prototype-to-production decision. Teams should decide where prompts are stored,
whether user inputs can train future models, and how retrieval permissions are
enforced. They should also decide what appears in logs and what tests catch
prompt injection or data exfiltration. Cost and latency belong in the same
review as evaluation and privacy on
[[LLM Production Patterns]]
systems.
