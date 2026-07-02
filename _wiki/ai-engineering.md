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

AI engineering turns foundation models into usable software. It is product
engineering around models rather than prompt writing alone: one skill stack
covers full-stack product work,
[[retrieval-augmented-generation|RAG]],
agents, evaluation, and LLMOps
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).

It is also a production discipline. Production AI connects to data pipeline tests
and prompt evaluation, then compression and caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
End-to-end ownership spans product-driven AI, requirements, feedback loops, and
the move away from notebooks
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

## Application Ownership

AI engineers own the application layer around model behavior, a full-stack
builder path: frontend and backend skill plus database design, RAG, agents,
evaluation, and deployment are all needed to ship a working product
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
That puts AI engineering near
[[software engineering]],
[[machine-learning-engineer-role|machine learning engineering]],
and [[data-engineer-role|data engineering]].
AI engineers increasingly build with
[[AI Coding Tools]] like Cursor
and Claude Code, which change how product code is written and maintained.

The same ownership takes a product-builder flavor when an AI project such as
BranchGPT is treated as a web application with context management and user
behavior, placing product discovery beside technical delivery
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).
For role boundaries, see [[AI Engineer Role]]
and [[AI Engineering Roadmap]].

The boundary can also stay closer to data science and domain expertise:
generative AI evaluation grounded in statistical rigor, research mindsets
contrasted with engineering speed, AI roles compared across big tech and
startups, plus orchestration and latency concerns
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

The notebook-to-production view adds product and deployment concerns:
product-driven AI, end-to-end ownership, business-to-ML requirements, feedback
loops, and image description architecture, plus a modern stack with FastAPI, UV,
and Arize
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
That context management work is the practice of
[[Context Engineering]].

For deeper retrieval and knowledge-system work, start with
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].
Then compare [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
and [[Graph RAG vs Vector RAG]].
Use retrieval when a product needs grounded, changing, or auditable knowledge,
and evaluate retrieval and generation together rather than treating the prompt
as the whole system.

## Evaluation and Reliability

AI engineers need evaluation before they can call a feature production-ready.
Evaluation is one of the technical pillars for shipping AI products
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
Older data-science discipline carries into generative AI through statistical
rigor and a balance of research mindsets with engineering speed
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Reliability becomes concrete through tests and examples while tracking cost and
latency: data trust, snapshot and integration testing, prompt evaluation, prompt
compression, and prompt caching
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
For evaluation workflows, see
[[LLM Evaluation Workflows]]
and [[Evaluation]]. For prompt and
production work, see [[Prompt Engineering]]
and [[LLM Production Patterns]].

Feedback loops and monitoring extend evaluation from an end-to-end product view,
covering explicit and implicit feedback plus modern tools for production AI
systems
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
That makes evaluation an ongoing operating practice, not a final checklist
before launch.

## Agents and Tool Use

AI engineering includes agent engineering for planning and tool use, with agent
rigor and orchestration as concerns
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Agents are software systems, not magic prompts. An AI engineer has to define
tool contracts and permissions, plus retries, traces, latency limits, and
outcome tests. Use
[[Agent Engineering]],
[[agent-engineering|AI Agents]], and
[[multi-agent-systems|Multi-Agent Systems]] for
deeper agent-specific work. Running agents in production adds monitoring,
governance, and evaluation concerns covered under
[[Agent Ops]].

## Data Pipelines and Deployment

Production AI still depends on data engineering: data trust, data pipeline
tests, testing tools, Spark choices, and preprocessing and fine-tuning data all
feed AI work
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).
For adjacent data work, see [[Data Pipelines]],
[[Data Engineering]], and
[[How to Build Data Pipelines]].

The deployment side runs through end-to-end AI systems: ownership, requirements,
system architecture, production code, and a modern serving and monitoring stack
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
The same operational work runs through [[MLOps]],
[[MLOps Engineer]], and
[[AI Infrastructure]].

## Career and Learning Signals

Project evidence matters more than credentials alone. AI engineering learning
ties to shipped projects and portfolio work
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
The same argument runs through side projects and local community work,
daily-life project ideas, hiring signals, and using AI to learn
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

For a learner, a strong AI engineering portfolio should show more than a chatbot
demo. It should show a product problem and a user interface or API, plus context
strategy, evaluation cases, and deployment notes. Add monitoring or feedback and
a tradeoff around latency or cost; data quality and model choice are also useful
tradeoffs.

Use [[AI Engineering Roadmap]],
[[RAG Portfolio Projects]],
and [[Open Source Portfolio Evidence]]
for project sequencing. The
[[ai-engineering-roadmap|AI Engineer Roadmap]]
turns that sequencing into concrete build stages with portfolio milestones.
</content>
