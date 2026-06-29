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

Privacy engineering for ML means designing data collection, feature access, and
model training around privacy constraints. Teams apply the same constraints to
deployment, logging, and interfaces. The system should create value without
collecting, exposing, or retaining more personal data than the product can
justify. Privacy engineering sits near
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).
It also connects to [Security]({{ '/wiki/security/' | relative_url }}),
[Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

In the season 14-15 archive, guests treat privacy engineering as technical
architecture plus organizational process. They discuss consent UX, data minimization, and
privacy-enhancing technologies. They also cover access reviews, purpose-based
permissions, and localized or self-hosted LLMs. A recurring risk is sending
sensitive text into systems that weren't designed around retention and deletion.

## Link Map

These wiki pages connect privacy engineering to adjacent topics:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})

These interviews anchor the page:

- [Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}) with [Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }})
- [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}) with [Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}) with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})

## Common Definition

Across the archive, privacy engineering translates legal obligations and user
expectations into product requirements. It also connects data architecture and
ML system design. In
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}),
Katharine Jarmul describes looking at the data side and application side of a
system. Privacy engineers identify risks and constraints, then turn them into
requirements that satisfy product goals and privacy needs.

Bart Vandekerckhove gives the platform-governance version in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
Cloud data warehouses and lakes collapse old boundaries between source systems.
Teams then need dataset-level access management and purpose-based requests. They
also need approvals, reviews, and revocation. Masking and visibility into access
matter too.

Meryem Arik adds the LLM deployment focus in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
Privacy is one reason to move from quick API prototypes toward controlled
open-source or self-hosted models for production workloads.

## Guest Perspectives

Katharine focuses on data minimization, consent, and re-identification risk.
She also discusses privacy-enhancing technologies, including differential
privacy and federated learning. The same discussion covers encrypted computation
plus localized model deployment
([Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).

Katharine argues that teams should design privacy into the easiest product path.
They shouldn't leave it to users who may paste personal, proprietary, or
regulated data into convenient interfaces.

Bart focuses on operating practice. In his access-management discussion, he
centers data owners, data engineers, and governance teams. DPOs and CISOs also
appear in the approval flow. He also covers access requests, time-bound access,
and regular reviews. He treats automated tagging and masking as part of the same
governance work
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).

Meryem's production LLM discussion focuses on model control. APIs are fast for
prototyping, but long-term systems often need stable behavior and cost control.
They may also need latency control, fine-tuning, and data privacy
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).

## Data Minimization and Consent UX

Katharine starts from practical product choices, including cookie defaults,
one-click rejection, and consent. She also asks whether a product can still work
when a user shares less data
([Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).
Her business case isn't only compliance. If a small model-performance bump
requires holding sensitive data indefinitely, the company also accepts breach
risk. It also accepts legal, insurance, and customer-trust risk.

For ML teams, this changes the design question. Instead of asking how much user
history to collect for personalization, the team can ask which inferences can
happen in-session. It can also ask which features are necessary, which retention
period is justified, and whether the system can degrade gracefully when consent
is withheld. This connects privacy engineering to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
because the interface and the model pipeline belong to the same risk surface.

## Access Controls for Sensitive ML Data

Bart's access-management episode shows why privacy engineering can't be only a
modeling concern. A churn model may need customer email, product usage, billing,
or support data. Each field can have a different owner and sensitivity level. It
can also have a different approved purpose
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).

Bart recommends catalog discovery and purpose-based access requests. He also
recommends data-owner approval, time-bound access, and automatic revocation.

Bart also warns about privilege creep and role explosion. ML experiments often
start with temporary access, but access granted and never revoked
creates long-term risk. Bart's answer is collaboration between data owners,
engineers, and governance teams.

He also recommends active metadata, automated tagging, and masking. He treats row
filtering and regular reviews as part of the same control set. Together, Bart
treats these controls as part of
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Security]({{ '/wiki/security/' | relative_url }}) inside the ML system, not as
external compliance paperwork.

## Privacy-Enhancing Technologies

Katharine describes privacy-enhancing technologies as architectural and
algorithmic options. They let teams do more advanced data science while reducing
centralization or exposure of sensitive data
([Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).
Katharine names encrypted ML and federated learning as examples. She also names
rigorous anonymity definitions and differential privacy.

Guests don't present these techniques as the first move for every team.
Katharine recommends starting with the simpler organizational conversation. Then
the team can move toward advanced privacy engineering when the system needs it.

Teams need maturity first because a team that hasn't defined sensitive fields
and access owners won't fix privacy by adding a complex privacy-preserving
algorithm. The same applies when retention, consent, or deletion are undefined.
Privacy-enhancing technologies are most useful when they fit into an existing
workflow for data governance and evaluation. They also need production
ownership.

## LLM Privacy and Deployment Choices

LLMs make privacy engineering more visible because users naturally paste
contracts and emails into text boxes. They also paste customer messages and
credentials. Proprietary documents can end up there too.

Katharine's generative-AI discussion shows how retention and deletion become
product decisions. The same is true for consent and incident notification.
Training reuse is another product decision
([Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})).

Her design principle is that the easiest path should be private enough for
ordinary users. Users shouldn't have to manage the whole burden.

Meryem's LLM deployment episode gives the production tradeoff. API models are
useful during prototyping because teams can get demos quickly. Production teams
often move toward open-source or self-hosted models for control and privacy.
They may also need stable model behavior and cost control. Latency control and
fine-tuning can matter too
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).

Teams don't need to self-host every private system immediately. They do need to
include the privacy review in the prototype-to-production decision alongside
latency and evaluation. Retrieval, monitoring, and cost matter too.

## Related Pages

Continue from these related pages:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
