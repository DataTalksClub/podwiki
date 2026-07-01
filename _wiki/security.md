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
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[privacy engineering]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).
They also touch [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

The recurring concerns are who can read data, who can change a model, and what
can influence an answer. Security also asks how a system might expose private
information.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) gives the
clearest LLM-specific account in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 9:28, she moves into a large chatbot hacking exercise. At 11:38 and 13:20,
she covers hallucinated commitments, prompt injection, and knowledge-base
exfiltration. Those examples put chatbot security in the full system around the
model, not only in prompt wording.

## Data Access and Permission Review

Data security starts with knowing who can use each dataset. Teams also need the
reason for access and the time when access should expire. In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
argues at 25:05 that teams should add access controls early when sensitive data
appears. At 27:49 and 32:08, he ties security to access requests, approval
reviews, and revocation. He also covers time-bound access and privilege creep.

Bart's access model depends on [data governance]({{ '/wiki/data-governance/' | relative_url }})
and ownership rather than blanket permissions. It also depends on policy-aware
tooling. At 11:20, he links cloud consolidation and "Chinese wall" constraints
to access management. At 29:36, he uses a churn-analysis example to show why
access requests should state purpose and scope.

At 44:55 and 50:08, Bart discusses role explosion and access reviews. He also
covers alerts, Terraform, and IAM patterns. Those patterns make permission
changes visible. The same concerns affect [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
when domains share data but retain accountability for sensitive fields.

Security also includes temporary access for urgent work, which Bart covers at
35:35 through debugging access in production. The team needs a fast way to
investigate incidents, but the access should stay scoped, reviewed, and removed
after the investigation.

At 37:19, Bart brings privacy and security stakeholders into the access
decision. At 42:20, he links sensitive data in data mesh to masking, filtering,
and federated governance. Those examples tie security to
[governance]({{ '/wiki/governance/' | relative_url }}). A data owner, a
security team, and a data protection officer may each ask for different evidence
before granting access.

## LLM Abuse and Retrieval Leakage

LLM security adds risks that ordinary data access controls don't catch. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
Maria's chatbot hacking exercise at 9:28 includes prompt injection and attempts
to reveal hidden instructions. It also includes attempts to extract private
knowledge-base records or make the assistant produce unsafe answers. At 13:20,
she focuses on data exfiltration through overloaded prompts and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).

Maria's 16:15 and 17:00 chapters show why teams need layered controls around
chatbots, copilots, and RAG systems. Query analysis can block or redirect risky
inputs before retrieval. Output validation and non-LLM classifiers can catch
failures after the model responds. Logging and human review add another layer.

The model can't be the only enforcement point. User input and retrieved passages
sit inside the attack surface. Tool calls and the answer renderer do too. For
adjacent production patterns, see
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}).

## Privacy Risk Beyond Access Control

Privacy overlaps with security but doesn't collapse into it. A system can have
strong access controls and still expose people through profiling,
fingerprinting, or re-identification.

In [Katharine's privacy engineering episode]({{ '/podcasts/data-privacy-engineering-gdpr-machine-learning/' | relative_url }}),
[Katharine Jarmul]({{ '/people/katharinejarmul/' | relative_url }}) defines
privacy through legal, social, and technical perspectives at 16:24. At 22:38,
she describes the translation work between legal and technical teams. At 25:12,
she discusses browser history and profiling. She also covers fingerprinting and
re-identification.

At 30:15, Katharine discusses session-based and ephemeral personalization, which
treats privacy engineering as an architectural choice. At 33:08 and 40:50, she
covers privacy-enhancing technologies and encrypted ML. She also discusses
federated learning and differential privacy.

At 45:08 and 47:00, Katharine covers anonymization pitfalls, consent, and data
minimization. These concerns belong with
[Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).
Teams may need to avoid centralizing data rather than collecting it first and
locking it down later.

## Model Artifacts and Software Supply Chain

ML security includes the model file, feature code, dependencies, and loading
format. In
[Fairness in AI/ML Engineering]({{ '/podcasts/fairness-in-ai-ml-engineering/' | relative_url }}),
[Tamara Atanasoska]({{ '/people/tamaraatanasoska/' | relative_url }}) discusses
secure model persistence and pickle deserialization risk at 46:20 and 47:16.
Her warning places model files, feature pipelines, and serialized objects inside
the attack surface.

That supply-chain risk links [machine learning]({{ '/wiki/machine-learning/' | relative_url }})
security to [software engineering]({{ '/wiki/software-engineering/' | relative_url }}).
Teams need dependency review, artifact provenance, safer loading formats, and
release approval for models as well as application code. The same model can be
accurate in evaluation and unsafe to load if the serialized artifact can run
untrusted code.

## Regulated Deployment and Trust

Production security means controls survive deployment, staffing changes, and
model updates. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
discusses regulatory and legacy constraints at 18:52. At 22:25 and 23:39, he
ties release management, approvals, and DevOps work to ML deployment and trust.
His account fits finance and other regulated settings where teams need
auditable controls, change review, and rollback paths before a model reaches
users.

Production controls also need monitoring and incident routes. Bart's temporary
debugging-access example at 35:35 covers scoped access during urgent
investigation. Maria's chatbot security episode adds output monitoring and
human review for LLM systems.

At 18:01, Maria links hallucinations to user trust and adoption risk. At 25:34,
she covers hybrid review for accuracy and harm reduction. For broader deployment
design, see
[Production]({{ '/wiki/production/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}).

## Red Teaming and Human Review

[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) tests an AI
system before real users exploit or accidentally trigger the same failures.
Maria's 9:28 chatbot hacking exercise found failures that ordinary product demos
would miss. The failures included prompt injection, hidden-instruction leakage,
and knowledge-base exfiltration. They also included unsafe answers and
hallucinated commitments. Her 11:38 chapter shows why a model can create
business risk by promising something the company didn't intend to offer.

Red-team findings should become deployed controls. Maria's 16:15 and 17:00
chapters cover classifier rules, retrieval filters, and query checks. They also
cover output checks and monitoring signals. Her 25:34 chapter adds
human-in-the-loop review when automation alone can't handle the risk. Human
review keeps red teaming connected to
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
rather than leaving it as a one-time exercise.

## Related Security Topics

Security in the podcast archive sits next to these policy, privacy, evaluation,
and deployment topics:

- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
