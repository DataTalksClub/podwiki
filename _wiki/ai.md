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
  - Data Products
  - Evaluation
  - Governance
  - AI Agents
  - Prompt Engineering
  - Responsible AI and Governance
---

Artificial intelligence is the DataTalks.Club umbrella for systems built from
models and data. They also depend on software and workflow design. These
systems support decisions, generate content, retrieve knowledge, or automate
product work.

In older conversations that often means
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}),
[deep learning]({{ '/wiki/deep-learning/' | relative_url }}), and
[NLP]({{ '/wiki/nlp/' | relative_url }}). In newer conversations it often means
[LLMs]({{ '/wiki/llms/' | relative_url }}),
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}),
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
and [AI agents]({{ '/wiki/ai-agents/' | relative_url }}).

The useful boundary in the podcast isn't "does it call a model?" It's whether
the system changes a workflow and can be evaluated, operated, secured, and
improved. [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) makes that
distinction in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).

At 7:45 he connects modern generative AI work back to statistical rigor. At
36:15 he frames human-centered design as part of AI delivery. At 42:05 he places
agents inside normal software engineering discipline.
Janna Lipenkova's
[Creating Intelligent Products]({{ '/books/20240205-creating-intelligent-products/' | relative_url }})
develops the same product-focused view: it treats AI as an end-to-end product
discipline covering market research, UX, and business model fit, not just model
development.

## AI as Product Engineering

Recent DataTalks.Club guests describe AI as a product and engineering system,
not as a standalone prediction. In
[Paul Iusztin's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts full-stack
engineering and RAG into the same skill stack. He adds knowledge management and
LLMOps as delivery concerns. The 22:29, 29:12, and 42:28 chapters also make
product delivery part of AI work. That makes
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) closer to
shipping a [data product]({{ '/wiki/data-products/' | relative_url }}) than to
only training a model.

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) gives the
role version of the same idea in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
At 19:40 he describes the AI engineer as a generalist who combines product
discovery and backend delivery. The role also includes LLM tooling and enough
judgment to decide what should be automated. His 7:51 and 57:39 chapters make
built projects and skill proof more important than credentials. That's why the
AI page connects to both the
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) and the
[AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }}).

AI product thinking also shows up before the LLM era. In
[Build & Scale Data Products for AI]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }}),
[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) treats AI work as
roadmaps, customer research, and business metrics. MLOps priorities belong in
the same roadmap.

The 23:20 and 31:45 chapters push teams to work backward from
business problems. The 51:11 and 53:27 chapters add success metrics and SLAs.
They also add data quality.

That discussion links AI to
[data product management]({{ '/wiki/data-product-management/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}).

## Machine Learning, LLMs, and Generative AI

[Machine learning]({{ '/wiki/machine-learning/' | relative_url }}) is the
technical base under much of the AI archive. It covers feature work, labels, and
training data. It also covers model validation, deployment, monitoring, and
tradeoffs between accuracy and interpretability. Use the narrower
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
when the discussion is about supervised learning systems, feature pipelines, or
classical production ML.

The newer LLM conversations narrow the problem to language models and generated
outputs. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) separates
classification tasks from generative tasks at 11:44. She compares open-source
and API models at 16:48 and 49:44. From 26:30 through 46:42, she discusses
fine-tuning and retrieval.

Later chapters cover vector databases, latency, cost, and evaluation. Use that
episode to move from general AI into
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}), and
[evaluation]({{ '/wiki/evaluation/' | relative_url }}).

[Generative AI]({{ '/wiki/generative-ai/' | relative_url }}) covers systems that
produce text, code, summaries, or answers. It also covers translations, images,
and plans. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) uses chatbot
failures to show that generated outputs need controls.

The 9:28 chapter covers large-scale chatbot probing, and the 13:20 chapter shows
knowledge-base exfiltration patterns. The 16:15 chapter adds output validation,
query analysis, and layered defenses. Those failure modes connect
[prompt engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
to [security]({{ '/wiki/security/' | relative_url }}) rather than treating a
prompt as only copywriting.

## Retrieval and Knowledge Systems

Many AI products in the podcast become useful only when the model can work with
the right context. [Atita Arora]({{ '/people/atitaarora/' | relative_url }})
explains this search lineage in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).

At 23:00 she connects NLP and personalization to learning-to-rank and LLMs. At
30:38 she frames RAG as retrieval plus generation to reduce hallucinations. At
38:24 and 42:49, she covers chunking and embeddings. She also covers citations
and prompt design.
At 48:09 she adds human-in-the-loop evaluation.

That makes [search]({{ '/wiki/search/' | relative_url }}) and
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) central AI topics.
[RAG]({{ '/wiki/rag/' | relative_url }}) and
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
cover the broader architecture. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) adds the
operational side. At 29:30 and 31:38, RAG systems inherit latency, cost, and
data-quality problems. At 36:11 and 37:39, retrieval can be a tool inside an
agent rather than the whole system.

## Agents and Action-Oriented AI

[AI agents]({{ '/wiki/ai-agents/' | relative_url }}) extend AI systems from
answer generation into planning and tool use. They also add memory and action.

In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) defines
agents through objectives and tools at 11:00 and 12:31. Memory and stores sit
in the same definition. At 21:21 she shifts the discussion toward context
design. At 51:17, 53:20, and
56:02 she argues for custom evaluations and mocked tools. The checks should be
outcome-based rather than exact-path tests.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) places current
agents inside a longer AI lineage in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
He links reinforcement learning and evolutionary algorithms to early NLP and
prompt optimization. Those connections appear across the 8:01, 9:09, 10:00, and
14:09 chapters.

His 20:57 and 23:48 chapters favor minimal task decomposition before manager-agent
orchestration. The 31:31 and 57:39 chapters cover tool integration and
monitoring. For design details, use
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}) and
[multi-agent systems]({{ '/wiki/multi-agent-systems/' | relative_url }}).

## Evaluation, Reliability, and Cost

AI systems need [evaluation]({{ '/wiki/evaluation/' | relative_url }}) because
the output is probabilistic, context-dependent, and tied to user trust.

In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) starts with
data trust and pipeline tests at 9:05, 11:47 and 13:14. He then moves to
prompt engineering and prompt evaluation at 25:13 and 28:16. His 30:00 and
31:45 chapters add prompt compression, prompt caching, and token use. They also
cover latency and model efficiency. A useful AI feature must survive
[production]({{ '/wiki/production/' | relative_url }}) traffic, not only a demo.

LLM and RAG evaluation have their own patterns. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) ties gold-standard
examples and output-driven metrics together at 53:34 and 56:39. Meryem also
separates classification metrics, generative metrics, and human judgment. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) adds retrieval-level
and answer-level checks at 48:09. Those discussions belong with
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}).

## Infrastructure and Model Control

Infrastructure-heavy AI work asks who controls compute, data, and models. It
also asks who owns latency, privacy, and operating cost. In
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }}),
[Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }}) compares
cloud and on-prem economics at 8:25 and 10:00, then connects privacy and
control to decentralization at 21:37. His 30:16, 34:46, and 47:16 chapters add
distributed training and GPU coordination. They also cover PyTorch and NCCL
communication bottlenecks, Kubernetes limits, SLURM, and open-source
orchestration.

That infrastructure view complements Meryem Arik's model-deployment view in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
where open-source models and hosted APIs appear at 16:48 and 49:44. The 23:37,
25:26 and 51:35 chapters add fine-tuning, serving optimization, and latency
tradeoffs. For deeper implementation work, use
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}),
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
and [MLOps]({{ '/wiki/mlops/' | relative_url }}).

## Governance, Security, and Human Oversight

AI needs [governance]({{ '/wiki/governance/' | relative_url }}) when it affects
people, regulated decisions, or private data. Safety-critical workflows need the
same discipline. Material business outcomes do too.

In
[Responsible & Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}),
[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) defines responsible
AI through trust and fairness at 4:43 and 8:20. She also includes
explainability, stakeholder collaboration, and compliance. She moves from
data-level fairness checks at 11:36
and PII handling at 14:39 to cross-functional governance at 27:38. At 35:28 she
adds human-in-the-loop oversight.

For LLM systems, governance also has a security layer. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) connects
prompt injection and data exfiltration across the 11:38 and 13:20 chapters. The
16:15 and 18:01 chapters add hallucinations and controls. At 20:39 and 25:34,
she adds ROI and hybrid human review.

Those risks are why the AI topic links out to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}),
[Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
and [Security]({{ '/wiki/security/' | relative_url }}).

## Related Pages

Use these pages for narrower AI topics and implementation details.

- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) and [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) cover the builder role and skill stack.
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }}), [LLMs]({{ '/wiki/llms/' | relative_url }}), and [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }}) cover model behavior and generated outputs.
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}), [RAG]({{ '/wiki/rag/' | relative_url }}), and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) cover context and retrieval.
- [AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}), and [Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) cover action-oriented AI systems.
- [Data Products]({{ '/wiki/data-products/' | relative_url }}), [MLOps]({{ '/wiki/mlops/' | relative_url }}), and [Production]({{ '/wiki/production/' | relative_url }}) cover delivery and operations.
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }}), [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}), and [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}) cover measurement.
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) and [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}) cover compute, orchestration, and deployment choices.
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}), [Governance]({{ '/wiki/governance/' | relative_url }}), [Security]({{ '/wiki/security/' | relative_url }}), and [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) cover risk controls.
