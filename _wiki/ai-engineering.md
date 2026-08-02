---
layout: wiki
title: "AI Engineering"
summary: "AI engineering is the discipline of shipping LLM applications, RAG systems, agents, evaluations, and production AI products."
related:
  - AI Engineer Role
  - AI Engineering Roadmap
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - Agent Engineering
  - LLM Evaluation Workflows
  - Notebook to Production AI Systems
  - Multimodal LLMs
  - AI Infrastructure
  - MLOps
---

AI engineering turns foundation models into usable software. It's product
engineering around models rather than prompt writing alone. The discipline owns
the application layer and model behavior. It also owns context, evaluation, and
operations around AI products.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]
For the learning sequence, use [[AI Engineering Roadmap]].

Prompting lets more people act as new AI experts. They can explore, prototype,
and contribute without first training a model. Maria Sukhareva treats that
democratization as useful experimentation. It doesn't replace production
judgment.[[cite:generative-ai-chatbots-in-production-security@05:42=>Prompting and AI Experts]]
Production AI engineering still depends on system design and evaluation.
Operations matter too, and engineers need to know when a prompt is only one
component of the product.

Production AI connects data pipeline tests and prompt evaluation with compression
and caching.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
End-to-end ownership spans product-driven AI, requirements, and feedback loops.
It also includes the move away from notebooks. Use
[[Notebook to Production Workflow]] for the practical handoff path.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>Notebook to Production]]

## Application Ownership

AI engineers own the application layer around model behavior, and that ownership
has four parts.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]

- Product software and database design.
- RAG and agents.
- Evaluation.
- Deployment.

AI engineering therefore sits near
[[software engineering]],
[[machine-learning-engineer-role=>machine learning engineering]],
and [[data-engineer-role=>data engineering]].

AI engineers increasingly build with
[[ai-coding-tools=>AI coding tools]]. Cursor and Claude Code change product code
maintenance.[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>AI Engineer Role]]

AI engineering is broader than [[llm-tools=>LLM Tools for Real Products]] or a
framework choice. Engineers choose where to put knowledge, which model behavior
to trust, and how to look at failures. They also operate the feature after
launch. The [[book:20241104-llm-engineer-s-handbook=>LLM Engineer's Handbook]]
covers a similar production stack, from RAG ingestion to LLMOps and deployment.
Production AI engineering connects directly to [[LLM Production Patterns]],
[[AI Infrastructure]], and [[MLOps Architecture]].

For the title-specific role boundary, see [[AI Engineer Role]].

## Role Boundaries

AI engineering can look like product building or like an extension of data
science, depending on the team. In product-centered projects such as BranchGPT,
teams treat the AI system as a web application. Context management, user
behavior, and product discovery sit beside technical delivery.[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]]

Some teams keep the boundary closer to data science and domain expertise.
Generative AI evaluation still draws on statistical rigor and research mindsets.
Engineering teams also need speed and orchestration. Latency control matters in
the same role boundary.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

AI engineering crosses role boundaries and overlaps older
[[data-scientist-role=>data scientist]] and
[[machine-learning-engineer-role=>ML engineer]] responsibilities.
Paul Iusztin frames the distinction as a shift from analysis or modeling alone
to end-to-end product ownership. The AI engineer builds the surrounding
software and data path. Evaluation, deployment, and user-facing product
behavior belong there too.
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@15:13=>AI Engineering Skill Stack]]

At senior scope, that boundary becomes a
[[staff-ai-engineer=>staff AI engineer]] problem. Roadmap and architecture
decisions have to stay connected to cross-team production AI delivery.
[[cite:from-academia-to-staff-ai-engineer-interviews-and-career-growth=>Staff AI Engineer Transition]]

## Core System Pieces

AI engineers repeatedly work with the application and model layers, handling
context and evaluation beside data pipelines. Deployment and operations are part
of the same work. RAG and knowledge management sit in the shipping stack with
agents, evaluation, and LLMOps.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]

Data-pipeline tests come before prompt mechanics. Prompt compression and caching
come later.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
Orchestration, latency, and fine-tuning round out the model-layer concerns.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Notebook-to-production discussions add product and deployment concerns.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>Notebook to Production]]

- Product-driven AI and end-to-end ownership.
- Business-to-ML requirements and feedback loops.
- Image description architecture and a serving stack with FastAPI, UV, and Arize.

Image-description systems bring [[multimodal-llms=>multimodal LLMs]] into
production AI engineering. Model behavior matters alongside serving,
monitoring, and user-facing product design.

For the handoff path, see [[Notebook to Production Workflow]].
For the broader system view, see [[Notebook to Production AI Systems]] and
[[machine learning system design]]. Use
[[llm-system-design-interview=>LLM system design interview]] for LLM-specific
system prompts and retrieval. It also covers safety, cost, and operations.

## Context, RAG, and Knowledge Systems

Models sometimes need private or changing knowledge, so RAG and knowledge
management are central.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]

BranchGPT treats context management as product work.[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>AI Engineer Role]]
That work belongs under [[Context Engineering]].

For deeper retrieval and knowledge-system work, start with
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].
Then compare [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
and [[Graph RAG vs Vector RAG]].
Use retrieval when a product needs grounded, changing, or auditable knowledge.
Evaluate retrieval and generation together rather than treating the prompt as
the whole system.

## Evaluation and Reliability

AI engineers need evaluation before they can call a feature production-ready, and
evaluation is one pillar.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]

Older data-science discipline still shapes generative AI through statistical
rigor and a balance of research mindsets with engineering speed.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Teams make reliability concrete through tests and examples while tracking cost
and latency. The production discussion covers data trust, snapshot and integration
testing, and prompt evaluation. It also covers prompt compression and prompt
caching.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
For evaluation workflows, see
[[LLM Evaluation Workflows]]
and [[Evaluation]]. For prompt and
production work, see [[Prompt Engineering]]
and [[LLM Production Patterns]].

Feedback loops and monitoring extend evaluation across the product lifecycle.
They cover explicit and implicit feedback. Modern tools support that production
work.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>Notebook to Production]]
That makes evaluation an ongoing operating practice, not a final checklist
before launch.

## Agents and Tool Use

AI engineering includes agent engineering for planning and tool use, with agent
rigor as a concern. Orchestration also matters.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Agents are software systems, not magic prompts. An AI engineer has to define
tool contracts and permissions. They also need retries, traces, latency limits,
and outcome tests. Use [[Agent Engineering]] and
[[multi-agent-systems=>Multi-Agent Systems]] for
deeper agent-specific work.

Use [[game-ai-to-llm-agents=>Game AI to LLM Agents]] when the design question is
how older state, action, feedback, and simulation ideas transfer into LLM
agents. The same bridge keeps
[[evolutionary-algorithms=>evolutionary algorithms]] nearby when the system tests
candidate prompts, actions, or designs against feedback. Running agents in
production adds monitoring, governance, and
evaluation concerns covered under [[Agent Ops]].
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Data Pipelines and Deployment

Production AI still depends on data engineering because data trust and pipeline
tests feed AI work. Testing tools, Spark choices, preprocessing, and
fine-tuning examples matter too. Data engineers prepare and clean the examples
that make specialized AI systems viable.
[[cite:production-ready-ai-engineering@18:38=>Production AI]]
For adjacent data work, see [[Data Pipelines]],
[[Data Engineering]], and
[[How to Build Data Pipelines]].

Teams handle deployment through end-to-end AI systems where ownership and
requirements define the work. System architecture connects production code with
serving and monitoring. Use [[Notebook to Production Workflow]] for the release
sequence.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>Notebook to Production]]
The same operational work runs through [[MLOps]],
[[MLOps Engineer]], and
[[AI Infrastructure]].

## Career and Project Signals

Hiring discussions value project evidence more than credentials alone. Project
work shows AI engineering judgment.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>Skill Stack]]
The same argument runs through side projects and local community work.
Daily-life project ideas count too. The episode also covers hiring signals and
using AI to learn.
[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]]

Career-break and domain-first candidates need the same proof standard.
[[nontraditional-paths-to-ai-engineering=>nontraditional paths to AI engineering]]
connects older context and side projects. Current AI product artifacts matter
more than biography alone.
[[cite:s23e04-how-to-become-ai-engineer-after-career-break=>AI Engineer After a Career Break]]
Use [[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
for those daily workflows.

At the concept level, the useful signal is ownership across product surface and
context strategy. A reviewer should also see evaluation cases, deployment notes,
monitoring, and cost or latency tradeoffs. Use
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]] for
concrete project shapes and review criteria.

Software engineers moving into this path can use
[[software-engineer-to-machine-learning=>software engineer to machine learning]]
for the named transition. Use
[[machine-learning-for-software-engineers=>machine learning for software engineers]]
to separate reusable strengths from missing ML data and evaluation habits.

Use [[AI Engineering Roadmap]] for the staged learning path. Use
[[RAG Portfolio Projects]] for retrieval-heavy examples and
[[Open Source Portfolio Evidence]] for public proof outside a dedicated AI
product.
