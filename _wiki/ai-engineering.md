---
layout: wiki
title: "AI Engineering"
summary: "Podcast-grounded guide to AI engineering as the discipline of shipping LLM applications, RAG systems, agents, evaluations, and production AI products."
related:
  - AI Engineer Role
  - AI Engineering Roadmap
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - Agent Engineering
  - LLM Evaluation Workflows
  - Notebook to Production AI Systems
  - AI Infrastructure
  - MLOps
---

AI engineering turns foundation models into usable software. It's product
engineering around models rather than prompt writing alone. One skill stack
covers full-stack product work and
[[retrieval-augmented-generation=>RAG]]. It also covers agents, evaluation, and
LLMOps
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).

Maria Sukhareva frames generative AI democratization as prompting that lets many
more people act as new AI experts
[[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
That lower barrier matters, but production AI engineering still depends on
engineering judgment across system design, evaluation, and operations. It also
requires knowing when a prompt is only one component of the product.

It's also a production discipline. Production AI connects to data pipeline tests
and prompt evaluation, then compression and caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
End-to-end ownership spans product-driven AI, requirements, feedback loops, and
the move away from notebooks
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

## Application Ownership

AI engineers own the application layer around model behavior as full-stack
builders. They need frontend and backend skill plus database design. They also
need RAG, agents, evaluation, and deployment to ship a working product
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
That puts AI engineering near
[[software engineering]],
[[machine-learning-engineer-role=>machine learning engineering]],
and [[data-engineer-role|data engineering]].
AI engineers increasingly build with
[[AI Coding Tools]] like Cursor
and Claude Code, which change how product code is written and maintained.

The same ownership takes a product-builder flavor in AI projects such as
BranchGPT. In that example, teams treat the project as a web application with
context management and user behavior. Product discovery sits beside technical
delivery
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).
For role boundaries, see [[AI Engineer Role]]
and [[AI Engineering Roadmap]].

The boundary can also stay closer to data science and domain expertise. The
discussion covers generative AI evaluation grounded in statistical rigor and
research mindsets contrasted with engineering speed. It also compares AI roles
across big tech and startups, with orchestration and latency concerns
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).
That shows why AI engineering crosses role boundaries rather than replacing
every older [[data-scientist-role|data scientist]]
or [[machine-learning-engineer-role|ML engineer]]
responsibility.

## Core System Pieces

AI engineers repeatedly work with the application and model layers, handling
context and evaluation beside data pipelines, deployment, and operations. RAG
and knowledge management group with agents, evaluation, and LLMOps in the
shipping stack
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).

Data-pipeline tests come before prompt mechanics, then prompt compression and
caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
Orchestration, latency, and fine-tuning round out the model-layer concerns
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

AI engineering is broader than [[LLM tools]]
or a framework choice. The engineer has to choose where to put knowledge and
which model behavior to trust, look at failures, and operate the feature after
launch. The [[book:20241104-llm-engineer-s-handbook|LLM Engineer's Handbook]] by
Paul Iusztin and Maxime Labonne covers the same production stack, from RAG
ingestion to LLMOps and deployment. For related production work, see
[[LLM Production Patterns]],
[[AI Infrastructure]], and
[[MLOps Architecture]].

The notebook-to-production view adds product and deployment concerns such as
product-driven AI, end-to-end ownership, and business-to-ML requirements. It
also covers feedback loops and image description architecture, plus a modern
stack with FastAPI, UV, and Arize
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
For those topics, see
[[Notebook to Production AI Systems]],
[[machine learning system design]],
and [[machine learning for software engineers]].

## Context, RAG, and Knowledge Systems

AI engineering starts to differ from ordinary application development when the
model needs private or changing knowledge. RAG and knowledge management are core
technical pillars for shipping AI products
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
The BranchGPT example shows context management as part of the product rather
than a hidden implementation detail
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).
That work belongs under [[Context Engineering]].

For deeper retrieval and knowledge-system work, start with
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].
Then compare [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
and [[Graph RAG vs Vector RAG]].
Use retrieval when a product needs grounded, changing, or auditable knowledge.
Evaluate retrieval and generation together rather than treating the prompt as
the whole system.

## Evaluation and Reliability

AI engineers need evaluation before they can call a feature production-ready.
Evaluation is one of the technical pillars for shipping AI products
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
Older data-science discipline still shapes generative AI through statistical
rigor and a balance of research mindsets with engineering speed
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Reliability becomes concrete through tests and examples while tracking cost and
latency. The production discussion covers data trust, snapshot and integration
testing, and prompt evaluation. It also covers prompt compression and prompt
caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
For evaluation workflows, see
[[LLM Evaluation Workflows]]
and [[Evaluation]]. For prompt and
production work, see [[Prompt Engineering]]
and [[LLM Production Patterns]].

Feedback loops and monitoring extend evaluation from an end-to-end product view.
They cover explicit and implicit feedback plus modern tools for production AI
systems
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
That makes evaluation an ongoing operating practice, not a final checklist
before launch.

## Agents and Tool Use

AI engineering includes agent engineering for planning and tool use, with agent
rigor and orchestration as concerns
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Agents are software systems, not magic prompts. An AI engineer has to define
tool contracts and permissions. They also need retries, traces, latency limits,
and outcome tests. Use
[[Agent Engineering]],
[[agent-engineering=>AI Agents]], and
[[multi-agent-systems=>Multi-Agent Systems]] for
deeper agent-specific work. Running agents in production adds monitoring,
governance, and evaluation concerns covered under
[[Agent Ops]].

## Data Pipelines and Deployment

Production AI still depends on data engineering. Data trust, data pipeline
tests, and testing tools all feed AI work. Spark choices, preprocessing, and
fine-tuning data do too
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
For adjacent data work, see [[Data Pipelines]],
[[Data Engineering]], and
[[How to Build Data Pipelines]].

The deployment side runs through end-to-end AI systems, covering ownership,
requirements, and system architecture. It also covers production code and a
modern serving and monitoring stack
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
The same operational work runs through [[MLOps]],
[[MLOps Engineer]], and
[[AI Infrastructure]].

## Career and Learning Signals

Project evidence matters more than credentials alone because AI engineering
learning ties to shipped projects and portfolio work
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
The same argument runs through side projects and local community work. It also
covers daily-life project ideas, hiring signals, and using AI to learn
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

For a learner, a strong AI engineering portfolio should show more than a chatbot
demo. It should show a product problem and a user interface or API, plus context
strategy, evaluation cases, and deployment notes. Add monitoring or feedback and
a tradeoff around latency or cost. Data quality and model choice are also useful
tradeoffs.

Use [[AI Engineering Roadmap]],
[[RAG Portfolio Projects]],
and [[Open Source Portfolio Evidence]]
for project sequencing. The
[[ai-engineering-roadmap=>AI Engineer Roadmap]]
turns that sequencing into concrete build stages with portfolio milestones.
</content>
