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
retain it, and which controls apply in production. In the DataTalks.Club
archive, it sits between [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
and [Security]({{ '/wiki/security/' | relative_url }}). It also connects to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

This topic is centered on ML and AI systems, not privacy law in the abstract.
[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) gives the
most direct archive definition in
[her privacy engineering episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}).

She joins the legal and social sides of privacy with the technical side. Then
she translates risk into product and architecture requirements. The rest of the
archive adds the operating machinery. That machinery includes access governance
and masking. It also includes data quality checks, LLM deployment choices, and
security testing.


## Common Definition

Across the archive, privacy engineering isn't a late compliance review. It's
a design constraint across the full data lifecycle. A team should know why it
collects data and whether the use case still works with less data. It should
also know which fields are sensitive, who can access them, and how the model or
application prevents unintended exposure.

Katharine's episode connects minimization to consent. At 11:33 and 14:35, she
discusses GDPR, CCPA, and CPRA. She also covers cookie-consent defaults. At
22:38, she frames privacy engineering as translation between legal and
technical views. At 30:15 and 47:00, privacy becomes normal product design.

Teams can use session-based inference and ask whether data collection is
necessary. They can also make the private path easy for users
([Katharine's privacy episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).

[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }}) gives
the governance version in
[his access-governance episode]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).

At 11:20, he connects modern cloud data consolidation to access management. At
27:49 and 32:08, the controls become operational. Teams need purpose-based
access requests, approval, reviews, and revocation. Time-bound access matters
too.

For ML teams, those controls decide which training data can be used. They also
decide which features, logs, and debugging records can be used.


[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) links privacy to
responsible AI in
[her responsible-AI episode]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}).
At 14:39 and 17:20, PII handling and masking become product decisions. Feature
necessity becomes a subject-matter and compliance decision too. That places
privacy engineering next
to [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

The review should cover both model accuracy and whether the data inputs are
justified.

## Guest Differences

The guests mostly agree on the goal. Useful AI systems shouldn't create
avoidable privacy, security, or compliance risk. The difference is their
starting point.

Katharine starts from privacy risk through regulation and consent UX examples.
Her episode also covers browser fingerprinting. Re-identification,
privacy-enhancing technologies, and differential privacy follow
([Katharine's privacy episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
at 16:24 and 25:12 and at 33:08 and 40:50).

The failure mode is collecting or centralizing sensitive data because it's
convenient. The team may then discover later that deletion, retention, or user
expectations were never designed into the system.

Bart starts from access operations. Cloud warehouses and lakehouses make more
data visible to more teams. Without purpose-based requests and owners, privacy
depends on informal permission habits. Masking and filtering make those habits
explicit. Reviews and revocation do too
([Bart's access-governance episode]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
25:05 and 27:49, plus 42:20 and 46:42).

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) starts from LLM
deployment. In
[her LLM deployment episode]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
the 16:48 chapter compares open-source and API models around control, privacy,
and fine-tuning. At 18:46, hidden API model changes become a production risk.
For her, privacy is one reason a team may move from a quick hosted-model
prototype to a more controlled deployment path.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) starts from
product security. In
[her chatbot-security episode]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 13:20 chapter shows how prompt injection and retrieval can expose hidden
knowledge-base content. Her mitigation path uses layered defenses, output
validation, query analysis, and non-LLM classifiers at 16:15 and 17:00. This
connects privacy engineering to [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
and [Security]({{ '/wiki/security/' | relative_url }}).

## Data Minimization and Consent

Data minimization is the archive's strongest privacy-engineering habit. The
team should first ask whether the product can work with less data. Shorter
retention, local inference, or a less identifying representation may be enough.
Katharine's
session-based personalization example at 30:15 shows the design. Teams can
infer intent from the current session where possible instead of accumulating
permanent user histories
([Katharine's privacy episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).

This changes the modeling conversation. A personalization model or churn model
may improve when it sees more user history. A fraud model or support assistant
may improve too. The improvement still has to be weighed against breach impact,
deletion requirements, customer trust, and insurance or regulatory exposure.
Katharine ties that business case to risk management and customer trust at
35:09 in the same episode.

Consent belongs in the same product design. At 14:35, Katharine discusses
one-click rejection and user behavior around cookie banners. For ML teams,
privacy shouldn't depend on users understanding every later model use. Teams
should offer a reasonable low-data path. They should avoid turning consent into
a forced trade for basic functionality.

## Access Governance for ML Data

Privacy engineering fails if sensitive data becomes the default input to every
notebook, feature store, and production job. Bart's access-management episode
shows the practical controls. A team should connect catalogs and lineage to
ownership. It should then require access requests that name the purpose and
duration
([Bart's access-governance episode]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
8:58, 13:34, 27:49).

For ML systems, access rules should cover raw sources and feature tables. They
should also cover labels, experiment datasets, and model-debugging samples.
Embeddings, retrieval indexes, logs, and annotation queues need coverage too.
The same customer email can appear in several derived forms. A support message
can too, so privacy reviews need
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
signals, not only a policy document.

Bart's privilege-creep discussion at 32:08 is especially relevant to model
experimentation. Temporary access granted for a prototype can persist after the
model is abandoned. Time-bound access, revocation, review workflows, and
access-as-code reduce that drift. Masking and filtering at 42:20 and active
metadata at 46:42 make those controls easier to reuse. The same controls can
cover analytics, training, and operations.

## Privacy-Enhancing Technologies

Katharine describes privacy-enhancing technologies as architectural choices,
not magic add-ons. At 33:08 in
[her privacy episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}),
she discusses encrypted ML, federated learning, and privacy-aware architecture.
At 40:50, she introduces differential privacy as a formal way to reason about
privacy loss.

The archive doesn't imply that every team should begin with advanced PETs.
Katharine recommends clarifying what data is sensitive and what the product
needs. Teams should then decide who owns the risk. Techniques such as federated
learning, encrypted computation, differential privacy, or localized deployment
fit only when the use case still requires learning from sensitive patterns.

That matters because privacy-enhancing technologies need governance around
them. A federated-learning design still needs participant consent, update
controls, evaluation, and incident handling. Differential privacy still needs a
privacy budget and a decision about utility loss. Teams still need to own
encrypted computation in production. The technical technique works only when it's
embedded in [MLOps]({{ '/wiki/mlops/' | relative_url }}), governance, and
security practice.

## Regulated and High-Impact Deployment

High-impact deployment changes privacy engineering from a model-building concern
into a cross-functional approval process. Supreet's
[responsible-AI episode]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
episode is useful here because it treats feature necessity, PII handling,
fairness, and compliance as connected decisions. Human oversight belongs in
that same review. At 17:20, product owners should help decide whether to use a
feature. Subject-matter experts and compliance stakeholders belong in that
decision too.

Bart adds the access-control operating model for regulated data. In his
episode, data owners and governance teams appear in the approval flow. DPOs and
security teams appear too, along with engineers. The important approach is
separation of concerns. Privacy and security may need to approve the same
dataset. Domain owners may need to approve it for different reasons

([Bart's access-governance episode]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
35:35, 37:19).

For production ML, the approval record should state which sensitive fields are
used and why they're necessary. It should state whether those fields are
masked, transformed, or excluded. It should also state who approved access, how
long access lasts, what gets logged in production, and how the team handles
deletion or incident-response requests. Those checks connect privacy
engineering to [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[Security]({{ '/wiki/security/' | relative_url }}), and [MLOps]({{ '/wiki/mlops/' | relative_url }}).

## LLM Privacy and Security Tradeoffs

LLMs make privacy engineering visible because the interface invites free-form
text. Users may paste contracts, credentials, or customer messages into the same
box. They may paste medical details, code, or proprietary documents too.

Katharine's generative-AI discussion turns retention and deletion into product
requirements. Training reuse and consent belong there. Incident notification
does too
([Katharine's privacy episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).

Meryem's production LLM episode adds the infrastructure tradeoff. API models
are fast for prototyping, while open-source or self-hosted models can give
teams more control over privacy and fine-tuning. They can also give teams more
control over latency and cost
([Meryem's LLM deployment episode]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
16:48). API drift at 18:46 adds another operational risk. When a provider
changes model behavior, the privacy review and the evaluation results may no
longer describe the system that's running.

Retrieval systems add a second exposure path. A model might not store the
private data, but a vector index can still leak it. A document chunk, prompt
template, or log can leak it too. Maria's chatbot-security episode shows this
through knowledge-base exfiltration at 13:20. She then argues for layered
defenses at 16:15 and 17:00
([Maria's chatbot-security episode]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

That places LLM privacy next to
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[LLMs]({{ '/wiki/llms/' | relative_url }}), and
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}).

The archive's practical production rule is to include privacy in the
prototype-to-production decision. Teams should decide where prompts are stored,
whether user inputs can train future models, and how retrieval permissions are
enforced. They should also decide what appears in logs and what tests catch
prompt injection or data exfiltration. Cost and latency belong in the same
review as evaluation and privacy on
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
systems.

## Related Pages

Use these adjacent pages for governance, security, LLM deployment, and ML
operations context:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
