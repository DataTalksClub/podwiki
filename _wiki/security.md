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

## Definition and Scope

Security is the practice of preventing unauthorized access, leakage, misuse, and
unsafe behavior in data and AI systems. In the podcast archive, security appears
across data access management, privacy engineering, and LLM prompt injection. It
also includes knowledge-base exfiltration, secure model persistence, and release
controls in regulated environments.

Use this page as the cross-cutting security bridge. Use
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) when the evidence
is specifically about adversarial testing. Use
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) when the topic
is ownership, catalogs, or access workflows. Put policy and lineage evidence
there too.

## Contents

Use these sections to move through the page.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

LLM security needs system design, not only prompt wording. The chatbot-security
episode shows that users can manipulate prompts and exfiltrate knowledge-base
content. They can also trigger hallucinated commitments. Safer designs layer
query analysis, retrieval constraints, and output validation. They also use
classifiers, logging, and human review.

Data security is access management. Governance episodes treat data catalogs and
access-as-code as security primitives. They also cover access requests,
approvals, revocation, and temporary production access. The recurring risk is
privilege creep: access granted for one task remains after the task is done.

Privacy and security overlap without being identical because the privacy episode
covers re-identification and profiling. It also covers consent, retention,
differential privacy, and federated learning. Those practices reduce harm even
when ordinary infrastructure security is working.

ML artifacts can create security risk. The fairness episode includes secure
model persistence and pickle deserialization risk. That belongs here because
models, feature pipelines, and serialized objects can become part of the attack
surface.

## Episode Evidence

These episodes give the strongest security evidence.

- [Hardening Generative AI Chatbots](https://datatalks.club/podcast.html)
  (11:38-17:16) covers chatbot failures, prompt injection, and
  knowledge-base exfiltration. It then covers output validation, query analysis,
  layered defenses, and non-LLM classifiers.
- [Data Governance and Data Access Management](https://datatalks.club/podcast.html)
  (25:05-33:22) covers access controls for sensitive data, request and
  approval workflows, privilege creep, and time-bound access. Bart also covers
  revocation and temporary debugging access.
- [Practical Data Privacy](https://datatalks.club/podcast.html) (25:12-61:15)
  covers profiling risk, re-identification risk, and privacy-enhancing
  technologies. It also covers differential privacy, anonymization pitfalls, and
  data minimization. Later sections cover retention and localized model
  deployment.
- [Fairness in AI and ML Engineering](https://datatalks.club/podcast.html)
  (46:20-50:54) discusses secure model persistence and deserialization risk,
  including why unsafe pickle workflows matter for ML systems.
- [MLOps in Finance](https://datatalks.club/podcast.html) (18:52-23:39)
  connects security with regulation, release management, and approvals while
  also covering legacy platforms and trust-building in finance.

## Related Pages

Use these pages for adjacent governance, production, and LLM topics.

- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})

## Maintenance Notes

Best source files for future expansion:

- `../datatalksclub.github.io/_podcast/generative-ai-chatbots-in-production-security.md`
- `../datatalksclub.github.io/_podcast/data-governance-data-access-management.md`
- `../datatalksclub.github.io/_podcast/data-privacy-engineering-gdpr-machine-learning.md`
- `../datatalksclub.github.io/_podcast/fairness-in-ai-ml-engineering.md`
- `../datatalksclub.github.io/_podcast/mlops-and-ml-engineering-in-finance.md`

When adding evidence, name the protected asset and the threat model. Also name
the control and the operating owner. Keep broad governance principles on
[Governance]({{ '/wiki/governance/' | relative_url }}) unless the episode
describes a concrete security control.
