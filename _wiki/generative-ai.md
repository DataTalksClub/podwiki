---
layout: wiki
title: "Generative AI"
summary: "How the podcast archive covers generative AI as applied language, chatbot, agent, coding, and content-generation systems."
related:
  - LLMs
  - LLM Production Patterns
  - NLP
  - Agent Engineering
  - Responsible AI and Governance
---

## Definition and Scope

Generative AI systems create outputs from prompts and context. In the podcast
archive, guests mostly discuss generative AI through LLM applications such as
chatbots, retrieval-backed assistants, coding tools, workflow automation,
translation support, and agent systems.

Use [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for production engineering and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
for risk, trust, and oversight.

## Contents

Use these links to jump between the main generative AI sections.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Generative AI needs guardrails around trust. Maria Sukhareva's
chatbot-security episode is the archive's clearest warning. Generative chatbots
can hallucinate, expose sensitive information, and create legal or financial
risk. Teams mitigate those risks with query analysis, output validation,
non-LLM classifiers, human review, and narrow task design.

Generative AI is often an assistant, not the final authority. Several
episodes position AI as a drafting, summarization, moderation, translation,
coding, or research assistant. Human review remains important when errors
affect users, money, safety, compliance, brand voice, or trust.

Production value comes from workflow integration. Generative AI becomes
useful when teams integrate it into an existing workflow. The archive includes
review analysis, transcript processing, browser extensions, email assistants,
Slack assistants, coding environments, and game-development tools. Prompt
quality matters, but guests also name data pipelines, APIs, logging, caching,
evaluation, and cost.

Hype can hide simpler systems. Guests repeatedly warn that generative AI
shouldn't replace reliable deterministic code, search, classical ML, or non-LLM
classifiers when those fit the task better. The practical question isn't whether
a model can generate an answer. The question is whether the whole system can
produce a useful, reviewable, and safe result.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Hardening Generative AI Chatbots](https://datatalks.club/podcast.html): The
  5:42 and 9:28 clips cover democratized prompting and a chatbot hacking
  exercise. The 11:38 clip covers hallucinations and legal or financial exposure.
  The 16:15 and 25:34 clips recommend layered defenses and human review.
- [Production AI Engineering](https://datatalks.club/podcast.html): The 21:46
  clip covers invisible AI inside workflows such as augmented generation and
  review analysis. The 28:16 and 31:45 clips connect prompt evaluation, quality,
  cost, caching, and latency. The 42:05 clip discusses coding assistants.
- [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html): The
  9:28 clip covers everyday generative use cases. The 13:56 clip uses
  generator-evaluator quality control. The 33:14 and 40:12 clips move from chat
  to embedded agents, actions, documents, and automation.
- [From Game AI to Modern AI Agents](https://datatalks.club/podcast.html): At
  38:57, covers generative AI in games through procedural content and
  replayability. At 41:42, discusses technical limits in agent-built game
  implementations.
- [Deploying LLMs in Production](https://datatalks.club/podcast.html): At 11:44,
  compares model choices for classification and generative tasks. At 26:30,
  covers fine-tuning for domain adaptation and tone.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})

## Maintenance Notes

Future updates should separate model capability from risk and workflow evidence.

- Keep broad AI governance claims on
  [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).
- Add a podcast summary for `generative-ai-chatbots-in-production-security.md`
  before expanding the security section.
- When adding examples, separate model capability from workflow integration,
  evaluation, and risk controls.
