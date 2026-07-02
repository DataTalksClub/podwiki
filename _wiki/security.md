---
layout: wiki
title: "Security"
summary: "Security in data and AI systems: LLM abuse, data exfiltration, access control, privacy, release approval, and secure ML artifacts."
related:
  - AI Red Teaming
  - Responsible AI and Governance
  - Data Governance
  - LLM Production Patterns
  - Production
---

Security prevents unauthorized access and data leakage. It also reduces misuse,
unsafe model behavior, and unreviewed changes in systems that handle data or
make decisions. DataTalks.Club podcast discussions repeatedly touch
[[data governance]] and
[[privacy-engineering-for-ml|privacy engineering]].
They also touch [[MLOps]] and
[[LLM production patterns]].

The recurring concerns are who can read data, who can change a model, and what
can influence an answer. Security also asks how a system might expose private
information.

The clearest LLM-specific account comes from a large chatbot hacking exercise
covering hallucinated commitments, prompt injection, and knowledge-base
exfiltration
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
Those examples put chatbot security in the full system around the model, not only
in prompt wording.

## Data Access and Permission Review

Data security starts with knowing who can use each dataset. Teams also need the
reason for access and the time when access should expire. Access controls should
be added early when sensitive data appears, and security ties to access requests,
approval reviews, revocation, time-bound access, and privilege creep
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]).

This access model depends on [[data governance]]
and ownership rather than blanket permissions, plus policy-aware tooling. Cloud
consolidation and "Chinese wall" constraints connect to access management, and a
churn-analysis example shows why access requests should state purpose and scope
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]).

Role explosion, access reviews, alerts, Terraform, and IAM patterns make
permission changes visible
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]).
The same concerns affect [[Data Mesh]]
when domains share data but retain accountability for sensitive fields.

Security also includes temporary access for urgent work, such as debugging access
in production
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]).
The team needs a fast way to investigate incidents, but the access should stay
scoped, reviewed, and removed after the investigation.

Privacy and security stakeholders belong in the access decision, and sensitive
data in data mesh links to masking, filtering, and federated governance
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]).
Those examples tie security to
[[governance]]. A data owner, a
security team, and a data protection officer may each ask for different evidence
before granting access.

## LLM Abuse and Retrieval Leakage

LLM security adds risks that ordinary data access controls don't catch. A chatbot
hacking exercise includes prompt injection and attempts to reveal hidden
instructions, extract private knowledge-base records, or make the assistant
produce unsafe answers, along with data exfiltration through overloaded prompts
and [[retrieval-augmented-generation|retrieval-augmented generation]]
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Teams need layered controls around chatbots, copilots, and RAG systems
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
Query analysis can block or redirect risky inputs before retrieval. Output
validation and non-LLM classifiers can catch failures after the model responds.
Logging and human review add another layer.

The model can't be the only enforcement point. User input and retrieved passages
sit inside the attack surface. Tool calls and the answer renderer do too. For
adjacent production patterns, see
[[LLM Production Patterns]]
and [[AI Red Teaming]].

## Privacy Risk Beyond Access Control

Privacy overlaps with security but doesn't collapse into it. A system can have
strong access controls and still expose people through profiling,
fingerprinting, or re-identification.

Privacy has legal, social, and technical perspectives, along with translation
work between legal and technical teams
([[podcast:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy engineering episode]]).
Browser history and profiling, fingerprinting, and re-identification are all
concerns.

Session-based and ephemeral personalization treats privacy engineering as an
architectural choice, and privacy-enhancing technologies, encrypted ML, federated
learning, and differential privacy extend it
([[podcast:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy engineering episode]]).

Anonymization pitfalls, consent, and data minimization round out the topic
([[podcast:data-privacy-engineering-gdpr-machine-learning|Katharine's privacy engineering episode]]).
These concerns belong with
[[Privacy Engineering for ML]].
Teams may need to avoid centralizing data rather than collecting it first and
locking it down later.

## Model Artifacts and Software Supply Chain

ML security includes the model file, feature code, dependencies, and loading
format. Secure model persistence and pickle deserialization risk place model
files, feature pipelines, and serialized objects inside the attack surface
([[podcast:fairness-in-ai-ml-engineering|Fairness in AI/ML Engineering]]).

That supply-chain risk links [[machine learning]]
security to [[software engineering]].
Teams need dependency review, artifact provenance, safer loading formats, and
release approval for models as well as application code. The same model can be
accurate in evaluation and unsafe to load if the serialized artifact can run
untrusted code.

## Regulated Deployment and Trust

Production security means controls survive deployment, staffing changes, and
model updates. Regulatory and legacy constraints, release management, approvals,
and DevOps work all tie to ML deployment and trust
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]). This fits
finance and other regulated settings where teams need auditable controls, change
review, and rollback paths before a model reaches users.

Production controls also need monitoring and incident routes. Temporary debugging
access covers scoped access during urgent investigation
([[podcast:data-governance-data-access-management|Data Governance and Data Access Management]]),
and chatbot security adds output monitoring and human review for LLM systems
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Hallucinations link to user trust and adoption risk, and hybrid review supports
accuracy and harm reduction
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
For broader deployment design, see
[[Production]] and
[[MLOps]].

## Red Teaming and Human Review

[[AI red teaming]] tests an AI
system before real users exploit or accidentally trigger the same failures. A
chatbot hacking exercise found failures that ordinary product demos would miss:
prompt injection, hidden-instruction leakage, knowledge-base exfiltration, unsafe
answers, and hallucinated commitments
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
A model can create business risk by promising something the company didn't intend
to offer.

Red-team findings should become deployed controls: classifier rules, retrieval
filters, query checks, output checks, and monitoring signals, plus
human-in-the-loop review when automation alone can't handle the risk
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
Human review keeps red teaming connected to
[[responsible AI and governance]]
rather than leaving it as a one-time exercise.

## Related Security Topics

Security in the podcast archive sits next to these policy, privacy, evaluation,
and deployment topics:

- [[Data Governance]]
- [[Governance]]
- [[Privacy Engineering for ML]]
- [[Responsible AI and Governance]]
- [[AI Red Teaming]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[LLM Production Patterns]]
- [[Production]]
- [[MLOps]]
