---
layout: wiki
title: "AI"
summary: "How DataTalks.Club podcast guests define AI across machine learning, generative AI, agents, production systems, evaluation, infrastructure, and governance."
related:
  - Generative AI
  - LLMs
  - AI Engineering
  - AI Engineer Role
  - Machine Learning
  - Responsible AI and Governance
---

## Definition

Artificial intelligence covers systems that automate or support decisions that
would otherwise need human judgment. It includes recommendation, generation,
search, and planning.

DataTalks.Club guests use AI for
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}),
[deep learning]({{ '/wiki/deep-learning/' | relative_url }}), and
[NLP]({{ '/wiki/nlp/' | relative_url }}). Recent episodes also use AI for
[LLMs]({{ '/wiki/llms/' | relative_url }}) and
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}). They also use AI
for [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[production systems]({{ '/wiki/production/' | relative_url }}).

In [Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}),
[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) separates the broad
AI umbrella from the current industry habit of using AI to mean generative-AI
products. He also ties current AI work to statistical evaluation and agents.

In
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) gives a longer
lineage. Game AI and reinforcement learning sit inside the same historical
family as modern LLM agents. So do evolutionary algorithms and NLP. Engineers
build and evaluate each one differently.

## Common Definition

Across recent episodes, guests treat AI as a system-level discipline rather
than a single model call. A useful AI product combines model behavior with
software, data, context, and evaluation. It also needs user experience,
security, and operations.

In [Paul Iusztin's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) frames modern AI
engineering as full-stack product work. The 22:29, 29:12, and 42:28 chapters
put RAG and knowledge management in the same skill stack as agents. They also
include LLMOps and product engineering. Shipping discipline sits alongside both.

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) makes the
same point from a role perspective in [Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
At 19:40, the AI engineer combines product discovery with backend work. The role
also includes LLM tooling and delivery habits. That role framing links AI to
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}),
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}), and
[AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }}).

The common definition is pragmatic. AI is useful when it changes a workflow or
decision, not when a team merely adds a model endpoint. In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) connects AI
work to data trust, pipeline tests, and prompt evaluation from 9:05 through
28:16. The 30:00 and 31:45 chapters add prompt compression, caching, latency,
and cost. That puts AI close to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}).

## Guest Differences

Guests disagree less about whether AI matters and more about where the hard
part sits. [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) stresses
statistical rigor and human-centered design in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}),
especially at 7:45 and 36:15. In his framing, teams need to ask what the system
should optimize, how people use it, and how they know whether an answer is
good.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts more weight on
the builder's skill stack in [his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
His 22:29 and 42:28 chapters cover full-stack engineering, product delivery,
and technical pillars for shipping AI products. [Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }})
adds hiring and project evidence in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
The 7:51 and 57:39 chapters make side projects and skill proof more important
than credentials.

[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) shifts the
center toward infrastructure in [Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}).
The 8:25 and 21:37 chapters frame AI through cloud economics, privacy, and
control. The 30:16 and 47:16 chapters add distributed training, GPU
coordination, Kubernetes limits, and open-source orchestration. For
infrastructure-heavy teams, the question isn't only "which model?" It's also
who controls compute, who pays for it, and who operates it.

## AI, Machine Learning, and Generative AI

[Machine learning]({{ '/wiki/machine-learning/' | relative_url }}) is a major
technical subset of AI. In older DataTalks.Club episodes, AI often means
predictive modeling, features, and labels. It also means training data, model
evaluation and deployment. Use [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
or [Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
when the discussion centers on supervised learning, model validation, feature
pipelines, or classical ML system design.

Recent AI episodes often mean [generative AI]({{ '/wiki/generative-ai/' | relative_url }})
and [LLMs]({{ '/wiki/llms/' | relative_url }}). In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) separates API-based
LLM use and open-source models. She also covers fine-tuning, retrieval, vector
databases, and deployment choices. Use that episode for LLM-specific design
decisions. This topic is the broader AI map.

[Generative AI]({{ '/wiki/generative-ai/' | relative_url }}) covers systems
that produce text, code, and images. It also covers summaries, answers, and
plans.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }})
uses chatbot failures in [Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
to show why generated outputs need guardrails. The 9:28, 13:20, and 16:15
chapters cover prompt injection and data exfiltration. They also cover output
validation and layered defenses. That makes generative AI part of
[security]({{ '/wiki/security/' | relative_url }}) as well as product design.

## Agents

Agents extend AI systems from answer generation into action. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) defines
agents through objectives, tools, and memory. She also covers knowledge stores,
planning, and evaluation.

The 11:00 and 12:31 chapters cover objectives, tools, and memory. The 21:21
chapter adds context design. The 36:11 and 51:17 chapters connect agents
to [RAG]({{ '/wiki/rag/' | relative_url }}), test datasets, and outcome-based
checks.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) adds a design
history in [From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 20:57 and 23:48, he discusses task decomposition, sequential flows, and
manager-agent orchestration. At 31:31 and 57:39, he adds MCP-style tool
integration and monitoring. Use [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) for
the narrower designs.

## Production Systems

Production AI work starts when the team asks how the system behaves after the
demo. [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) makes
that practical in [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
Pipeline tests and prompt evaluation show up before the conversation reaches
coding assistants. So do prompt compression, caching, and latency. Those production
concerns connect
AI to [Production]({{ '/wiki/production/' | relative_url }}),
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}).

Retrieval changes production architecture, and
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
shows why. In that episode,
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) grounds RAG in search
quality, embeddings, and chunking. She also covers citations and evaluation.

In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) warns at
29:30 and 31:38 that RAG inherits latency and cost problems. It also inherits
data-quality problems.
Use [Search]({{ '/wiki/search/' | relative_url }}),
[Search and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}),
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) for those
implementation details.

Infrastructure choices depend on cost, control, scale, and privacy. In
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) compares
cloud, on-prem, and open-source orchestration. He also covers distributed
training and GPU coordination. That discussion anchors
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}),
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
and [MLOps]({{ '/wiki/mlops/' | relative_url }}).

## Governance and Security

AI systems need governance when they affect users or regulated decisions. They
also need governance when they use private data or operational workflows. In
[Responsible & Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}),
[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) defines responsible
AI through trust, fairness, and explainability. She also adds SME input and
compliance.

The 27:38 and 35:28 chapters add monitoring and human oversight. These chapters
connect AI governance to product choices, not only post-hoc documentation.

Security becomes sharper for LLM and chatbot systems. [Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }})
shows in [Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
that prompt injection and knowledge-base leakage need specific defenses.
Hallucinations and unsafe automation also need human review. That discussion
belongs with [Security]({{ '/wiki/security/' | relative_url }}),
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}),
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
and [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).

## Related Pages

Use these pages for narrower AI topics and article-style guides.

- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }}) covers LLM-era AI products and generated outputs.
- [LLMs]({{ '/wiki/llms/' | relative_url }}) covers model choice, prompting, retrieval, fine-tuning, and deployment.
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) and [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) cover the builder role.
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) and [AI Agents]({{ '/wiki/ai-agents/' | relative_url }}) cover tool-using and action-oriented systems.
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) cover context and retrieval.
- [Production]({{ '/wiki/production/' | relative_url }}) and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) cover reliability after a prototype works.
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) covers compute, orchestration, and deployment choices.
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}), [Security]({{ '/wiki/security/' | relative_url }}), and [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) cover risk controls.
- [LLM Tools]({{ '/guides/llm-tools/' | relative_url }}) and [LLM System Design Interview]({{ '/guides/llm-system-design-interview/' | relative_url }}) turn these topics into article-style guides.
