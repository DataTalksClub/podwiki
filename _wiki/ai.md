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
  - Agent Engineering
  - Prompt Engineering
  - Responsible AI and Governance
---

Artificial intelligence is the DataTalks.Club umbrella for systems built from
models and data. They also depend on software and workflow design. These
systems support decisions, generate content, retrieve knowledge, or automate
product work.

In older conversations that often means
[[machine learning]],
[[deep learning]], and
[[NLP]]. In newer conversations it often means
[[LLMs]],
[[generative AI]],
[[retrieval-augmented-generation|retrieval-augmented generation]],
and [[agent-engineering|AI agents]].

The useful boundary in the podcast isn't "does it call a model?" It's whether
the system changes a workflow and can be evaluated, operated, secured, and
improved. [[person:nasserqadri|Nasser Qadri]] makes that
distinction in
[[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]].

At 7:45 he connects modern generative AI work back to statistical rigor. At
36:15 he frames human-centered design as part of AI delivery. At 42:05 he places
agents inside normal software engineering discipline.
Janna Lipenkova's
[[book:20240205-creating-intelligent-products|Creating Intelligent Products]]
develops the same product-focused view: it treats AI as an end-to-end product
discipline covering market research, UX, and business model fit, not just model
development.
[[book:20220509-artificial-intelligence-with-python|Artificial Intelligence with Python]]
by Prateek Joshi covers the broader toolkit that underlies these product systems, from search and optimization through ML, deep learning, and reinforcement learning.

## AI as Product Engineering

Recent DataTalks.Club guests describe AI as a product and engineering system,
not as a standalone prediction. In
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul Iusztin's AI engineering episode]],
[[person:pauliusztin|Paul Iusztin]] puts full-stack
engineering and RAG into the same skill stack. He adds knowledge management and
LLMOps as delivery concerns. The 22:29, 29:12, and 42:28 chapters also make
product delivery part of AI work. That makes
[[AI engineering]] closer to
shipping a [[data-products|data product]] than to
only training a model.

[[person:ruslanshchuchkin|Ruslan Shchuchkin]] gives the
role version of the same idea in
[[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]].
At 19:40 he describes the AI engineer as a generalist who combines product
discovery and backend delivery. The role also includes LLM tooling and enough
judgment to decide what should be automated. His 7:51 and 57:39 chapters make
built projects and skill proof more important than credentials. That's why the
AI page connects to both the
[[AI Engineer Role]] and the
[[AI Engineering Roadmap]].

AI product thinking also shows up before the LLM era. In
[[podcast:building-and-scaling-ai-data-products-with-mlops|Build & Scale Data Products for AI]],
[[person:gregcoquillo|Greg Coquillo]] treats AI work as
roadmaps, customer research, and business metrics. MLOps priorities belong in
the same roadmap.

The 23:20 and 31:45 chapters push teams to work backward from
business problems. The 51:11 and 53:27 chapters add success metrics and SLAs.
They also add data quality.

That discussion links AI to
[[data product management]],
[[MLOps]], and
[[data engineering]].

## Machine Learning, LLMs, and Generative AI

[[Machine learning]] is the
technical base under much of the AI archive. It covers feature work, labels, and
training data. It also covers model validation, deployment, monitoring, and
tradeoffs between accuracy and interpretability. Use the narrower
[[Machine Learning Engineer Role]]
when the discussion is about supervised learning systems, feature pipelines, or
classical production ML.

The newer LLM conversations narrow the problem to language models and generated
outputs. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
[[person:meryemarik|Meryem Arik]] separates
classification tasks from generative tasks at 11:44. She compares open-source
and API models at 16:48 and 49:44. From 26:30 through 46:42, she discusses
fine-tuning and retrieval.

Later chapters cover vector databases, latency, cost, and evaluation. Use that
episode to move from general AI into
[[LLM production patterns]],
[[vector databases]], and
[[evaluation]].

[[Generative AI]] covers systems that
produce text, code, summaries, or answers. It also covers translations, images,
and plans. In
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]],
[[person:mariasukhareva|Maria Sukhareva]] uses chatbot
failures to show that generated outputs need controls.

The 9:28 chapter covers large-scale chatbot probing, and the 13:20 chapter shows
knowledge-base exfiltration patterns. The 16:15 chapter adds output validation,
query analysis, and layered defenses. Those failure modes connect
[[prompt engineering]]
to [[security]] rather than treating a
prompt as only copywriting.

## Retrieval and Knowledge Systems

Many AI products in the podcast become useful only when the model can work with
the right context. [[person:atitaarora|Atita Arora]]
explains this search lineage in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].

At 23:00 she connects NLP and personalization to learning-to-rank and LLMs. At
30:38 she frames RAG as retrieval plus generation to reduce hallucinations. At
38:24 and 42:49, she covers chunking and embeddings. She also covers citations
and prompt design.
At 48:09 she adds human-in-the-loop evaluation.

That makes [[search]] and
[[embeddings]] central AI topics.
[[retrieval-augmented-generation|RAG]] and
[[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]]
cover the broader architecture. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
[[person:ranjithakulkarni|Ranjitha Kulkarni]] adds the
operational side. At 29:30 and 31:38, RAG systems inherit latency, cost, and
data-quality problems. At 36:11 and 37:39, retrieval can be a tool inside an
agent rather than the whole system.

## Agents and Action-Oriented AI

[[agent-engineering|AI agents]] extend AI systems from
answer generation into planning and tool use. They also add memory and action.

In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
[[person:ranjithakulkarni|Ranjitha Kulkarni]] defines
agents through objectives and tools at 11:00 and 12:31. Memory and stores sit
in the same definition. At 21:21 she shifts the discussion toward context
design. At 51:17, 53:20, and
56:02 she argues for custom evaluations and mocked tools. The checks should be
outcome-based rather than exact-path tests.

[[person:micheallanham|Micheal Lanham]] places current
agents inside a longer AI lineage in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
He links reinforcement learning and evolutionary algorithms to early NLP and
prompt optimization. Those connections appear across the 8:01, 9:09, 10:00, and
14:09 chapters.

His 20:57 and 23:48 chapters favor minimal task decomposition before manager-agent
orchestration. The 31:31 and 57:39 chapters cover tool integration and
monitoring. For design details, use
[[agent engineering]] and
[[multi-agent-systems|multi-agent systems]].

## Evaluation, Reliability, and Cost

AI systems need [[evaluation]] because
the output is probabilistic, context-dependent, and tied to user trust.

In
[[podcast:production-ready-ai-engineering|Production AI Engineering]],
[[person:bartoszmikulski|Bartosz Mikulski]] starts with
data trust and pipeline tests at 9:05, 11:47 and 13:14. He then moves to
prompt engineering and prompt evaluation at 25:13 and 28:16. His 30:00 and
31:45 chapters add prompt compression, prompt caching, and token use. They also
cover latency and model efficiency. A useful AI feature must survive
[[production]] traffic, not only a demo.

LLM and RAG evaluation have their own patterns. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
[[person:meryemarik|Meryem Arik]] ties gold-standard
examples and output-driven metrics together at 53:34 and 56:39. Meryem also
separates classification metrics, generative metrics, and human judgment. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
[[person:atitaarora|Atita Arora]] adds retrieval-level
and answer-level checks at 48:09. Those discussions belong with
[[LLM Evaluation Workflows]],
[[Production Search Evaluation]],
[[Data Quality and Observability]],
and [[data-quality-and-observability|Data Observability]].

## Infrastructure and Model Control

Infrastructure-heavy AI work asks who controls compute, data, and models. It
also asks who owns latency, privacy, and operating cost. In
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]],
[[person:andreycheptsov|Andrey Cheptsov]] compares
cloud and on-prem economics at 8:25 and 10:00, then connects privacy and
control to decentralization at 21:37. His 30:16, 34:46, and 47:16 chapters add
distributed training and GPU coordination. They also cover PyTorch and NCCL
communication bottlenecks, Kubernetes limits, SLURM, and open-source
orchestration.

That infrastructure view complements Meryem Arik's model-deployment view in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
where open-source models and hosted APIs appear at 16:48 and 49:44. The 23:37,
25:26 and 51:35 chapters add fine-tuning, serving optimization, and latency
tradeoffs. For deeper implementation work, use
[[AI Infrastructure]],
[[Machine Learning Infrastructure]],
and [[MLOps]].

## Governance, Security, and Human Oversight

AI needs [[governance]] when it affects
people, regulated decisions, or private data. Safety-critical workflows need the
same discipline. Material business outcomes do too.

In
[[podcast:responsible-explainable-ai-bias-detection|Responsible & Explainable AI]],
[[person:supreetkaur|Supreet Kaur]] defines responsible
AI through trust and fairness at 4:43 and 8:20. She also includes
explainability, stakeholder collaboration, and compliance. She moves from
data-level fairness checks at 11:36
and PII handling at 14:39 to cross-functional governance at 27:38. At 35:28 she
adds human-in-the-loop oversight.

For LLM systems, governance also has a security layer. In
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]],
[[person:mariasukhareva|Maria Sukhareva]] connects
prompt injection and data exfiltration across the 11:38 and 13:20 chapters. The
16:15 and 18:01 chapters add hallucinations and controls. At 20:39 and 25:34,
she adds ROI and hybrid human review.

Those risks are why the AI topic links out to
[[Responsible AI and Governance]],
[[AI Red Teaming]],
[[Privacy Engineering for ML]],
and [[Security]].

## Related Pages

Use these pages for narrower AI topics and implementation details.

- [[AI Engineering]] and [[AI Engineer Role]] cover the builder role and skill stack.
- [[Generative AI]], [[LLMs]], and [[Prompt Engineering]] cover model behavior and generated outputs.
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]], [[retrieval-augmented-generation|RAG]], and [[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]] cover context and retrieval.
- [[agent-engineering|AI Agents]], [[Agent Engineering]], and [[multi-agent-systems|Multi-Agent Systems]] cover action-oriented AI systems.
- [[Data Products]], [[MLOps]], and [[Production]] cover delivery and operations.
- [[Evaluation]], [[LLM Evaluation Workflows]], and [[Production Search Evaluation]] cover measurement.
- [[AI Infrastructure]] and [[Machine Learning Infrastructure]] cover compute, orchestration, and deployment choices.
- [[Responsible AI and Governance]], [[Governance]], [[Security]], and [[AI Red Teaming]] cover risk controls.
