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

Artificial intelligence covers systems built from models and data, which also
depend on software and workflow design. These systems support decisions,
generate content, retrieve knowledge, or automate product work.

In older conversations that often means
[[machine learning]],
[[deep learning]], and
[[NLP]]. In newer conversations it often means
[[LLMs]],
[[generative AI]],
[[retrieval-augmented-generation|retrieval-augmented generation]],
and [[agent-engineering|AI agents]].

The useful boundary isn't "does it call a model?" It's whether the system
changes a workflow and can be evaluated, operated, secured, and improved. Modern
generative AI work connects back to statistical rigor, human-centered design is
part of AI delivery, and agents sit inside normal software engineering
discipline
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).
Janna Lipenkova's
[[book:20240205-creating-intelligent-products|Creating Intelligent Products]]
develops the same product-focused view: it treats AI as an end-to-end product
discipline covering market research, UX, and business model fit, not just model
development.
[[book:20220509-artificial-intelligence-with-python|Artificial Intelligence with Python]]
by Prateek Joshi covers the broader toolkit that underlies these product systems, from search and optimization through ML, deep learning, and reinforcement learning.

## AI as Product Engineering

Recent guests describe AI as a product and engineering system, not a standalone
prediction. [[person:pauliusztin|Paul Iusztin]] puts
full-stack engineering and RAG into the same skill stack, with knowledge
management and LLMOps as delivery concerns and product delivery as part of AI
work
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
That makes
[[AI engineering]] closer to
shipping a [[data-products|data product]] than to
only training a model.

[[person:ruslanshchuchkin|Ruslan Shchuchkin]] gives the
role version of the same idea: the AI engineer is a generalist who combines
product discovery, backend delivery, LLM tooling, and enough judgment to decide
what should be automated, with built projects and skill proof mattering more
than credentials
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).
That's why the AI page connects to both the
[[AI Engineer Role]] and the
[[AI Engineering Roadmap]].

AI product thinking also shows up before the LLM era.
[[person:gregcoquillo|Greg Coquillo]] treats AI work as
roadmaps, customer research, business metrics, and MLOps priorities, pushing
teams to work backward from business problems and add success metrics, SLAs, and
data quality
([[podcast:building-and-scaling-ai-data-products-with-mlops|Build & Scale Data Products for AI]]).

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
outputs. [[person:meryemarik|Meryem Arik]] separates
classification tasks from generative tasks, compares open-source and API models,
and covers fine-tuning, retrieval, vector databases, latency, cost, and
evaluation
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Use that episode to move from general AI into
[[LLM production patterns]],
[[vector databases]], and
[[evaluation]].

[[Generative AI]] covers systems that
produce text, code, summaries, answers, translations, images, or plans.
[[person:mariasukhareva|Maria Sukhareva]] uses chatbot
failures to show that generated outputs need controls, covering large-scale
chatbot probing, knowledge-base exfiltration patterns, output validation, query
analysis, and layered defenses
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
Those failure modes connect
[[prompt engineering]]
to [[security]] rather than treating a
prompt as only copywriting.

## Retrieval and Knowledge Systems

Many AI products become useful only when the model can work with the right
context. [[person:atitaarora|Atita Arora]] traces the
search lineage from NLP and personalization to learning-to-rank and LLMs, frames
RAG as retrieval plus generation to reduce hallucinations, and covers chunking,
embeddings, citations, prompt design, and human-in-the-loop evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

That makes [[search]] and
[[embeddings]] central AI topics, and
[[retrieval-augmented-generation|RAG]]
covers the broader architecture. [[person:ranjithakulkarni|Ranjitha Kulkarni]]
adds the operational side: RAG systems inherit latency, cost, and data-quality
problems, and retrieval can be a tool inside an agent rather than the whole
system
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

## Agents and Action-Oriented AI

[[agent-engineering|AI agents]] extend AI systems from
answer generation into planning and tool use. They also add memory and action.

[[person:ranjithakulkarni|Ranjitha Kulkarni]] defines
agents through objectives, tools, memory, and stores, then moves toward context
design and argues for custom evaluations and mocked tools, with checks that are
outcome-based rather than exact-path tests
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

[[person:micheallanham|Micheal Lanham]] places current
agents inside a longer AI lineage, linking reinforcement learning and
evolutionary algorithms to early NLP and prompt optimization. He favors minimal
task decomposition before manager-agent orchestration, and covers tool
integration and monitoring
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
For design details, use
[[agent engineering]] and
[[multi-agent-systems|multi-agent systems]].

## Evaluation, Reliability, and Cost

AI systems need [[evaluation]] because
the output is probabilistic, context-dependent, and tied to user trust.

[[person:bartoszmikulski|Bartosz Mikulski]] starts with
data trust and pipeline tests, then moves to prompt engineering and prompt
evaluation, and adds prompt compression, prompt caching, token use, latency, and
model efficiency
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
A useful AI feature must survive
[[production]] traffic, not only a demo.

LLM and RAG evaluation have their own patterns.
[[person:meryemarik|Meryem Arik]] ties gold-standard
examples and output-driven metrics together and separates classification
metrics, generative metrics, and human judgment
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
[[person:atitaarora|Atita Arora]] adds retrieval-level
and answer-level checks
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Those discussions belong with
[[LLM Evaluation Workflows]],
[[Production Search Evaluation]],
[[Data Quality and Observability]],
and [[data-quality-and-observability|Data Observability]].

## Infrastructure and Model Control

Infrastructure-heavy AI work asks who controls compute, data, and models, and
who owns latency, privacy, and operating cost.
[[person:andreycheptsov|Andrey Cheptsov]] compares
cloud and on-prem economics, connects privacy and control to decentralization,
and adds distributed training and GPU coordination, including PyTorch and NCCL
communication bottlenecks, Kubernetes limits, SLURM, and open-source
orchestration
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure]]).

That infrastructure view complements the model-deployment view in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
where open-source models and hosted APIs sit alongside fine-tuning, serving
optimization, and latency tradeoffs. For deeper implementation work, use
[[AI Infrastructure]],
[[Machine Learning Infrastructure]],
and [[MLOps]].

## Governance, Security, and Human Oversight

AI needs [[governance]] when it affects
people, regulated decisions, or private data. Safety-critical workflows need the
same discipline. Material business outcomes do too.

[[person:supreetkaur|Supreet Kaur]] defines responsible
AI through trust and fairness, and includes explainability, stakeholder
collaboration, and compliance. The work runs from data-level fairness checks and
PII handling to cross-functional governance and human-in-the-loop oversight
([[podcast:responsible-explainable-ai-bias-detection|Responsible & Explainable AI]]).

For LLM systems, governance also has a security layer.
[[person:mariasukhareva|Maria Sukhareva]] connects
prompt injection and data exfiltration, adds hallucinations and controls, and
covers ROI and hybrid human review
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Those risks are why the AI topic links out to
[[Responsible AI and Governance]],
[[AI Red Teaming]],
[[Privacy Engineering for ML]],
and [[Security]].

## Related Pages

Use these pages for narrower AI topics and implementation details.

- [[AI Engineering]] and [[AI Engineer Role]] cover the builder role and skill stack.
- [[Generative AI]], [[LLMs]], and [[Prompt Engineering]] cover model behavior and generated outputs.
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]] and [[retrieval-augmented-generation|RAG]] cover context and retrieval.
- [[agent-engineering|AI Agents]], [[Agent Engineering]], and [[multi-agent-systems|Multi-Agent Systems]] cover action-oriented AI systems.
- [[Data Products]], [[MLOps]], and [[Production]] cover delivery and operations.
- [[Evaluation]], [[LLM Evaluation Workflows]], and [[Production Search Evaluation]] cover measurement.
- [[AI Infrastructure]] and [[Machine Learning Infrastructure]] cover compute, orchestration, and deployment choices.
- [[Responsible AI and Governance]], [[Governance]], [[Security]], and [[AI Red Teaming]] cover risk controls.
