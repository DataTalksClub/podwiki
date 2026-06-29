---
layout: wiki
title: "AI"
summary: "How the DataTalks.Club podcast archive frames AI after ChatGPT: generative AI, AI engineering, agents, RAG, LLMOps, infrastructure, evaluation, and governance."
related:
  - LLM Production Patterns
  - Search, RAG, and Knowledge Systems
  - Machine Learning
  - Data Science
  - Data Engineering
  - Responsible AI and Governance
---

## Definition

AI is the archive's broad umbrella for systems that automate or augment tasks
with machine learning, deep learning, language models, agents, retrieval, and
decision logic. In older episodes, AI often overlaps with machine learning and
data science. In newer episodes, especially after ChatGPT, guests usually use
"AI" to mean generative AI. That includes LLM applications, RAG, agents, AI
engineering, LLMOps, and the infrastructure needed to build and run these
systems.

Keep that distinction explicit. The archive doesn't have one timeless definition
of AI. In current episodes, modern AI work combines software engineering, data
engineering, evaluation, domain knowledge, model behavior, infrastructure, and
governance.

## Contents

Use these sections to separate broad AI usage from LLM-era engineering detail.

- [Scope](#scope)
- [Recurring Archive Themes](#recurring-archive-themes)
- [Role and Content Boundaries](#role-and-content-boundaries)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Scope

Use this foundation hub for generative AI, AI engineering, LLM applications,
agents, RAG, context management, evaluation, and production readiness. It also
covers infrastructure and governance.

For LLM-specific production patterns, use
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
For retrieval and RAG architecture, use
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
For classic applied modeling, use [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}).

## Recurring Archive Themes

**The archive now uses AI mostly as generative AI.**

Season 23 role episodes make the vocabulary shift visible. Guests acknowledge
that AI can mean the broad umbrella over machine learning and deep learning, but
they also note that current industry usage usually points to LLMs, ChatGPT-style
systems, and generative AI products.

This matters for wiki maintenance. A page about AI in this repo should usually
route broad modeling claims to [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
and reserve AI-specific synthesis for LLM-era systems unless an episode clearly
uses the broader meaning.

**AI engineering is software engineering around model behavior.**

The newest archive episodes define AI engineering less as model research and
more as building useful systems around models. AI engineers build interfaces,
backends, context flows, RAG pipelines, agents, evaluations, observability, and
deployment paths. They translate product needs into software while accounting
for LLM behavior.

Guests repeatedly say that making API calls is not enough. AI engineering needs
software engineering rigor, context management, evaluation design, stakeholder
communication, and enough domain knowledge to know what "good" means.

**Evaluation is becoming a core AI skill.**

AI episodes borrow heavily from data science and ML evaluation. Guests discuss
precision, recall, accuracy, test sets, agent evaluations, feedback pipelines,
human review, monitoring, and iteration. AI products need a way to compare
outputs against expected behavior, user needs, and business risk.

This is where data scientists have a strong transition path into AI engineering:
they already understand metrics, experiments, data splits, and evaluation
tradeoffs. They may need stronger software engineering practice to ship the
systems.

**RAG, context, and data engineering are central.**

AI systems often fail because they lack the right context, not because the model
is weak. The archive connects RAG, chunking, embeddings, citations, retrieval
quality, metadata, knowledge graphs, and semantic data layers to production AI.

Data engineering therefore remains foundational. Agents and conversational
interfaces need clean data, structured context, documented semantics, and
retrieval pipelines. Putting an LLM on top of messy data doesn't make the data
reliable.

**Agents add orchestration and operational risk.**

Agent episodes describe tools, memory, context windows, orchestration,
manager-agent designs, MCP-style tool integration, and multi-step workflows. The
archive is cautiously practical. Agents can automate useful work, but they also
add more places to fail. Teams need to evaluate tool choice, context
construction, branching behavior, latency, cost, evaluation, and auditability.

Preserve that tension. Agents aren't just a product label. They change how teams
design, test, monitor, and debug AI systems.

**Infrastructure choices depend on cost, control, and scale.**

AI infrastructure episodes add the compute layer. Guests compare cloud with
on-prem setups, GPU utilization, orchestration, distributed training, Kubernetes
limitations, Slurm, open-source tooling, and hybrid setups. The archive doesn't
say every company should build its own infrastructure. It asks whether the
organization has enough scale, privacy need, cost pressure, or control
requirement to justify the operational burden.

**Governance and human oversight remain part of AI.**

Responsible-AI episodes connect AI to fairness, explainability, privacy, PII,
security, red teaming, human oversight, monitoring, and regulatory pressure.
Production AI pages shouldn't separate capability from risk. The more AI
systems act across workflows or influence decisions, the more teams need
auditability, ownership, and human review paths.

## Role and Content Boundaries

**AI versus machine learning.**

Machine learning is a major technical subset of AI. In the current archive,
"AI" often means generative AI and agentic systems, while "machine learning"
covers predictive models, features, labels, baselines, training, evaluation, and
production ML.

Use [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}) when the
topic is classic applied modeling. Use this page when the topic is broad AI
vocabulary, LLM-era engineering, agents, infrastructure, or governance.

**AI versus AI engineering.**

AI is the broad topic. AI engineering is the role and practice of shipping AI
products. The archive's AI-engineering material currently covers LLM
applications, end-to-end product building, backend work, context management,
RAG, agents, evaluation, and production readiness.

The repo may eventually need a separate AI engineer role page. Until then,
summarize the role enough to satisfy linked topic slugs and route deeper work to
future role or roadmap pages.

**AI versus data science and data engineering.**

Data scientists contribute evaluation, experimentation, domain framing, and
model judgment. Data engineers contribute clean data, pipelines, metadata,
retrieval corpora, and platform reliability. AI engineers combine these with
software engineering and product delivery.

The archive repeatedly frames successful AI work as cross-functional rather than
owned by one role.

## Episode Evidence

These episodes give the strongest starting evidence for the topic.

- [Understanding the AI Engineer Role](https://datatalks.club/podcast.html): At
  5:49-7:55, the episode separates broad AI from current generative-AI usage. At
  13:15-15:20, it frames AI engineering as the middle ground between software
  engineering and data science.
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products](https://datatalks.club/podcast.html):
  At 12:09-14:27, the guest describes building software around models,
  infrastructure, scaling, and monitoring. Later sections cover RAG, knowledge
  graphs, agents, LLMOps, and AI evaluations.
- [Inside the AI Engineer Role](https://datatalks.club/podcast.html): At
  8:38-9:20, the guest says AI engineering is more than working with LLMs. It
  includes context management and end-to-end systems. Later sections contrast AI
  engineers with backend engineers and data scientists.
- [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}):
  Connects AI engineering to data pipeline testing, prompt evaluation, prompt
  compression, caching, latency, cost, coding assistants, and production
  readiness.
- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}):
  Grounds RAG in search quality, chunking, embeddings, citations, retrieval
  metrics, and human-in-the-loop evaluation.
- [From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}):
  Places modern LLM agents in a longer AI lineage and covers workflow design,
  orchestration, tool use, local models, and evaluation.
- [Post-ChatGPT AI Infrastructure](https://datatalks.club/podcast.html): Covers
  cloud versus on-prem economics, open-source orchestration, distributed
  training, GPU utilization, and infrastructure ownership after ChatGPT.
- [Responsible AI and Governance](https://datatalks.club/podcast.html): Adds
  fairness, explainability, privacy, PII handling, compliance input, human
  oversight, and monitoring as AI-system requirements.

## Related Pages

Use these pages for adjacent topics and deeper implementation detail.

- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})

## Maintenance Notes

- Highest-value source files for future expansion:
  `../datatalksclub.github.io/_podcast/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.md`,
  `../datatalksclub.github.io/_podcast/s23e05-inside-ai-engineer-role-tools-skills-and-career-path.md`,
  `../datatalksclub.github.io/_podcast/s23e07-understanding-ai-engineer-role.md`,
  `../datatalksclub.github.io/_podcast/production-ready-ai-engineering.md`,
  and `../datatalksclub.github.io/_podcast/ai-infrastructure-hybrid-cloud-on-prem-distributed-training.md`.
- Good future additions: a dedicated AI engineer role page, an AI engineering
  roadmap, an agent evaluation page, and a stronger bridge to security and
  red-teaming episodes.
- Avoid using this page as a generic AI encyclopedia. Keep it anchored in how
  the archive uses "AI", especially the post-ChatGPT shift toward LLM products,
  agents, infrastructure, and evaluation.
