---
layout: wiki
title: "Security"
summary: "Archive-backed bridge for security in data and AI systems: LLM abuse, data exfiltration, access control, privacy, and secure ML artifacts."
related:
  - AI Red Teaming
  - Responsible AI and Governance
  - Data Governance
  - LLM Production Patterns
  - Production
---

Security prevents unauthorized access, data leakage, misuse, and unsafe model
behavior. It also keeps unreviewed changes out of systems that handle data or
make decisions. In the DataTalks.Club archive, guests don't describe security
as one control. They connect it to [data governance]({{ '/wiki/data-governance/' | relative_url }}),
[privacy engineering]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) gives the
clearest LLM-specific framing in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 9:28, her episode moves into a large chatbot hacking exercise. At 11:38 and
13:20, she covers hallucinated commitments, prompt injection, and knowledge-base
exfiltration. That makes chatbot security a system design problem, not only a
prompt-writing problem.

[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }}) gives
the access-control framing in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
At 25:05, he argues that teams should add access controls early when sensitive
data appears. At 27:49 and 32:08, he ties security to access requests and
approval reviews. He also covers revocation, time-bound access, and privilege
creep.

## Common Definition

The common archive definition is practical. Security keeps useful systems from
exposing data, making unsafe commitments, or changing without review.

For data teams, that means access management and catalog-aware controls. It also means
purpose-based requests and revocation. For ML teams, it also means secure
artifacts and trusted dependencies, plus release approvals and monitoring. For
LLM teams, it adds prompt injection and retrieval leakage. It also adds output
validation and human review.

Security crosses several pages because [Governance]({{ '/wiki/governance/' | relative_url }})
explains policy decisions and [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
covers ownership and lineage. Data governance also covers classification and
access-as-code.
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) then covers
adversarial testing, while [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
covers safety and accountability when systems affect people.

## Guest Differences

Guests agree that security needs controls around data and behavior, but they
start from different risks.

Maria starts from user-facing LLM abuse. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 16:15 and 17:00 chapters cover output validation and query analysis. They
also cover layered defenses and non-LLM classifiers. Her view fits chatbots,
copilots, and [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
systems where a malicious or curious user can manipulate the input.

Bart starts from data access. In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
the 29:36 chapter uses a churn-analysis example to show purpose-based access
requests. The 35:35 chapter covers temporary production debugging access. His
view fits shared data platforms, [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}),
and teams where permissions accumulate faster than people review them.

[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) starts from
privacy harm in
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}).
At 25:12, she discusses browser history, profiling, and fingerprinting. She
also covers re-identification. At 33:08 and 40:50, she covers
privacy-enhancing technologies, federated learning, and differential privacy.
Her view matters when a system can be technically secure and still collect or
infer too much about people.

[Tamara Atanasoska]({{ '/people/tamaraatanasoska/' | relative_url }}) adds
software supply-chain risk for ML. In
[Fairness in AI/ML Engineering]({{ '/podcasts/fairness-in-ai-ml-engineering/' | relative_url }}),
the 46:20 and 47:16 chapters cover secure model persistence and pickle
deserialization risk. That places model files, feature pipelines, and serialized
objects inside the attack surface.

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) starts
from regulated deployment in
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}).
At 18:52 and 22:25, he discusses legacy systems and governance. He also covers
release management and approvals, then connects security to trust. His view
fits finance and other regulated settings where deployment security includes
auditable controls and change management.

## Data, AI, and LLM Security

Data security starts with knowing who can use each dataset. The team also needs
to know the purpose and duration of that access. Bart's
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode connects that to catalogs, access controls, and access-as-code. At
11:20, he links cloud consolidation and "Chinese wall" constraints to access
management.

At 44:55 and 50:08, he discusses role explosion, reviews, and
alerts. He also covers Terraform and IAM patterns. Those controls make
permission changes visible and reviewable.

AI security adds the model and its surrounding pipeline. Tamara's
[Fairness in AI/ML Engineering]({{ '/podcasts/fairness-in-ai-ml-engineering/' | relative_url }})
episode isn't only about fairness. The 46:20 to 47:16 section explains why
model persistence can become dangerous when teams rely on unsafe serialization.
That connects [machine learning]({{ '/wiki/machine-learning/' | relative_url }})
security to normal [software engineering]({{ '/wiki/software-engineering/' | relative_url }})
practices such as dependency review, artifact provenance, and safer loading
formats.

LLM security adds prompt and retrieval attacks. Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode covers data exfiltration through overloaded prompts and knowledge-base
retrieval at 13:20.

At 16:15 and 17:00, Maria shows why teams need retrieval constraints and query
analysis. They also need output validation, classifiers, and logging. The model
can't be the only enforcement point because the input and retrieved passages are
part of the system.

## Red Teaming

[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) is the security
practice of attacking an AI system before real users do the same thing
accidentally or on purpose. Maria's episode anchors this page because the 9:28
chatbot hacking exercise found failures that ordinary product demos miss. The
tests include prompt injection and attempts to reveal hidden instructions. They
also include attempts to extract private knowledge-base records or make the
assistant produce unsafe answers.

Red teaming should feed production controls. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 18:01 chapter connects hallucinations with user trust and adoption risk.
The 25:34 chapter covers human-in-the-loop review.

A red-team finding therefore shouldn't end as a note in a report. It should become a classifier rule,
retrieval filter, output check, or monitoring signal. Some findings should also
become a human review path inside the deployed system.

## Privacy and Governance

Privacy overlaps with security but doesn't collapse into it. A system can have
strong access controls and still expose people through profiling or
re-identification. Katharine's
[Data Privacy Engineering, GDPR, and Machine Learning]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }})
episode makes that distinction. At 16:24, she defines privacy through legal,
social, and technical perspectives. At 22:38, she describes the translation
work between legal and technical teams.

[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) shows how
privacy engineering changes architecture through session-based and ephemeral
personalization at 30:15. At 33:08, she discusses encrypted ML, federated
learning, and architecture choices.

At 45:08 and 47:00, she covers anonymization pitfalls and consent. She also
covers data minimization and workflow practices. These choices connect to
[Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
because the team may need to avoid centralizing data rather than merely locking
it down after collection.

Governance turns privacy and security decisions into repeatable work. Bart's
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
episode covers privacy and security stakeholders at 37:19. It also connects
data mesh and sensitive data to masking, filtering, and federated governance at
42:20. In practice, a data protection officer and a security team may need
different evidence before granting access. A data owner may need different
evidence again.

## Production Controls

Production security means controls survive deployment, staffing changes, and
model updates. Nemanja's
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
episode makes this concrete for finance.

At 18:52, he discusses regulatory and
legacy constraints. At 22:25 and 23:39, he connects release management,
approvals, and DevOps processes to ML deployment. He also connects those
controls to trust. Security therefore includes how teams review, approve, and
roll back model changes.

Production controls also need monitoring and incident paths. Bart's temporary
debugging-access chapter at 35:35 shows one practical compromise. Teams need a
fast way to investigate production issues, but that access should be scoped,
reviewed, and removed. Maria's chatbot episode adds output monitoring and human
review for LLM systems. The 25:34 chapter covers hybrid review to improve
accuracy and reduce harm.

For broader production design, use [Production]({{ '/wiki/production/' | relative_url }})
and [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
Security controls should sit next to deployment, testing, and observability.
They should also sit next to evaluation and rollback. Teams miss the failure
modes in these episodes when they treat security as a separate checklist after
the system ships.

## Related Pages

These pages cover the neighboring concepts that security depends on:

- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
