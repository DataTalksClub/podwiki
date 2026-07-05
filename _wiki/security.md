---
layout: wiki
title: "Security"
summary: "Security in data and AI systems: LLM abuse, data exfiltration, access control, privacy, release approval, and secure ML artifacts."
related:
  - AI Red Teaming
  - Responsible AI and Governance
  - Data Governance
  - LLM Production Patterns
  - ai-infrastructure-cost-and-ownership
  - Production
---

Security in data and AI systems prevents unauthorized access, data leakage,
unsafe model behavior, and unreviewed changes to systems that handle data or
make decisions. The topic sits next to [[data governance]],
[[privacy-engineering-for-ml=>privacy engineering]], [[MLOps]], and
[[LLM production patterns]].

Security decisions ask who can read data and who can change a model. They also
ask what can influence an answer. LLM systems add prompt injection and
hidden-instruction leakage. They also add knowledge-base exfiltration, unsafe
answers, and hallucinated commitments.[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]
Security therefore covers the model and retrieval path. It also covers access,
approval, logging, and review paths.

## Data Access and Permission Review

Data security starts with knowing who can use each dataset. Teams also need the
reason for access and the time when access expires. Access controls should start
early when sensitive data appears. Access-management work covers requests and
approvals. It also covers reviews, revocation, time limits, and privilege
creep.[[cite:data-governance-data-access-management=>Data Access Management]]

Effective access management depends on [[data governance]] and ownership rather
than blanket permissions. Cloud consolidation and
"Chinese wall" constraints connect access management to policy-aware tooling. A
churn-analysis example shows why access requests should state purpose and
limits.[[cite:data-governance-data-access-management=>Data Access Management]]

Role design and access reviews make permission changes visible. Alerts and
infrastructure-as-code support that visibility.[[cite:data-governance-data-access-management=>Data Access Management]]
The same concerns affect [[Data Mesh]] when domains share data but retain
accountability for sensitive fields.

Urgent production debugging can require temporary access.[[cite:data-governance-data-access-management=>Data Access Management]]
During incidents, teams may need fast investigation. Temporary access should stay
scoped, reviewed, and removed afterward.

Privacy and security stakeholders belong in the access decision. Sensitive data
in data mesh links to masking, filtering, and federated governance.[[cite:data-governance-data-access-management=>Data Access Management]]
Access decisions tie security to [[governance]]. A data owner, a security team,
and a data protection officer may each ask for different evidence.

## LLM Abuse and Retrieval Leakage

LLM security adds risks that ordinary data access controls don't catch.
Attackers can use overloaded prompts and
[[retrieval-augmented-generation=>retrieval-augmented generation]] as
exfiltration paths. Chatbot abuse also includes hidden-instruction leakage,
private knowledge-base extraction, unsafe answers, and hallucinated commitments.
[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]

Security controls can't rely on the model as the only enforcement point. User
input and retrieved passages sit inside the attack surface. Tool calls and the
answer renderer do too. For adjacent production patterns, see
[[LLM Production Patterns]] and [[AI Red Teaming]]. For the chatbot-specific risk
model, see [[Prompt Injection and Chatbot Risk Management]]. It covers prompt
injection and retrieval leakage along with hallucinated commitments and layered
defenses.[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]

## Privacy Risk Beyond Access Control

Privacy overlaps with security but doesn't collapse into it. A system can have
strong access controls and still expose people through profiling,
fingerprinting, or re-identification.

Privacy includes legal, social, and technical perspectives. It also requires
translation work between legal and technical teams.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Playbook]]
Browser history, profiling, fingerprinting, and re-identification are all
privacy concerns.

Teams can use session-based and ephemeral personalization as privacy engineering
choices. Privacy-enhancing technologies, encrypted ML, federated learning, and
differential privacy extend that design space.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Playbook]]

Anonymization pitfalls, consent, and data minimization round out the topic.[[cite:data-privacy-engineering-gdpr-machine-learning=>Data Privacy Playbook]]
For more detail, see [[Privacy Engineering for ML]]. Some systems may need to
avoid centralizing data rather than collecting it first and locking it down
later.

## Model Artifacts and Software Supply Chain

ML security includes the model file, feature code, dependencies, and loading
format. Secure model persistence and pickle deserialization risk place model
files inside the attack surface. Feature pipelines and serialized objects belong
there too.[[cite:fairness-in-ai-ml-engineering@47:16=>Fairness in AI/ML]]
The skops discussion gives a concrete mitigation path for scikit-learn-style
models. Teams should avoid treating an arbitrary pickle as a trusted artifact.
Safer persistence and sharing workflows matter when models move between people
or platforms
[[cite:fairness-in-ai-ml-engineering@46:20=>Fairness in AI/ML]].

Tamara Atanasoska's point is practical: a model hub or shared artifact store is
part of the security boundary. `skops` gives teams more control over which
objects can load, while a plain pickle can execute untrusted types during
deserialization. That makes model loading a [[scikit-learn=>scikit-learn]]
security concern, not only a convenience choice for notebooks
[[cite:fairness-in-ai-ml-engineering@47:16=>Fairness in AI/ML]].

That supply-chain risk links [[machine learning]]
security to [[software engineering]]. Teams need dependency review, artifact
provenance, safer loading formats, and release approval for models as well as
application code. The same model can be accurate in evaluation and unsafe to load
if the serialized artifact can run untrusted code.

## Regulated Deployment and Trust

Production controls must survive deployment and model updates in regulated
finance.[[cite:mlops-and-ml-engineering-in-finance=>MLOps]]
Teams use release management and approvals to build trust. DevOps work supports
the same trust.
Finance and other regulated settings need auditable controls and change review.
They also need rollback paths before a model reaches users.

Security or privacy constraints can affect where AI systems run. In those cases,
[[ai-infrastructure-cost-and-ownership=>infrastructure ownership]] becomes part
of the control model rather than only a cost decision
[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]].

Production controls need monitoring and incident routes. Temporary debugging
access helps during urgent investigations.[[cite:data-governance-data-access-management=>Data Access Management]]
It shouldn't leave broad access in place.
Chatbot security adds output monitoring and human review for LLM systems.[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]

Hallucinations affect user trust and adoption. They can also create legal or
financial exposure when a customer-facing bot invents a discount, service, or
deal. Hybrid review supports accuracy and harm reduction. A person can approve
or correct risky answers before they leave the organization.[[cite:generative-ai-chatbots-in-production-security@11:38=>Chatbot Incidents]]
[[cite:generative-ai-chatbots-in-production-security@25:34=>Human Review]]
For broader deployment design, see [[Production]] and [[MLOps]].

## Red Teaming and Human Review

[[AI red teaming]] tests an AI system before real users trigger the same
failures. Chatbot hacking found prompt injection and hidden-instruction leakage.
It also found knowledge-base exfiltration, unsafe answers, and hallucinated
commitments.
[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]

Security owns the accountability boundary after those findings appear, including
approvals, monitoring, and access review. Incident routes and human review cover
residual risk. The detailed chatbot controls belong in
[[Prompt Injection and Chatbot Risk Management]], while [[AI Red Teaming]] owns
the adversarial test design and regression-test workflow.

## Related Pages

Security sits next to these policy, privacy, evaluation, and deployment topics:

- [[Data Governance]]
- [[Governance]]
- [[Privacy Engineering for ML]]
- [[Responsible AI and Governance]]
- [[AI Red Teaming]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[LLM Production Patterns]]
- [[Production]]
- [[MLOps]]
