---
layout: article
title: "AI Engineer Roadmap"
keyword: "ai engineer roadmap"
summary: "A practical roadmap for becoming an AI engineer, from software foundations and LLM calls to RAG, evaluation, agents, and production ownership."
search_intent: "People searching for an AI engineer roadmap need a concrete build sequence: what skills to learn, what projects to build, and when to stop studying and ship."
related_wiki:
  - AI Engineering
  - AI Engineer Role
  - LLM Production Patterns
  - RAG
  - Agent Engineering
  - LLM Evaluation Workflows
  - AI Engineering Portfolio Projects
  - Notebook to Production AI Systems
---

An AI engineer roadmap should start with working software, not with model
theory. The job is building product applications around model behavior:
calling models, managing context, evaluating outputs, and operating the
resulting product. In
[AI Engineering Skill Stack]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) describes a
full-stack skill set that spans backend, frontend, database work, then adds
RAG, agents, evaluation, and LLMOps. At 22:29 he lists the engineering
foundations; at 29:12 the stack grows to include knowledge management; at
42:28 the focus shifts to shipping products.

This roadmap differs from a
[Machine Learning Engineer Roadmap]({{ '/roadmaps/machine-learning-engineer-roadmap/' | relative_url }})
because the core artifact is an application that calls a model API, not a
trained model. Use
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) for the
role boundary and
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) for the
discipline overview.

## Start With Product Ownership

AI engineering is applied product work, not prompt-only experimentation.
[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) frames
the role around product discovery, context management, and usable applications
in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
At 7:51, his BranchGPT example combines a web application, context
management, and user behavior into one product. That sets the sequence: build
the application first, then add model intelligence.

[Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }}) shows
the career-break entry path in
[How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }}).
She started with a telecom capstone using ML, then built prototypes with AI
dev tools, and landed a healthcare AI engineer role. Her path confirms the
sequence below: software foundations, then model calls, then a portfolio
project, then evaluation and production skills.

## Stage 1: Software Engineering Foundations

Before touching an LLM, build a small service with persistence, logs, and
tests. AI products still need APIs, databases, authentication, and deployment.
Paul's full-stack skill stack places backend, frontend, and database work
inside AI engineering
([his episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
22:29).

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) makes the same
argument from a different angle in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).
At 7:45, he says AI engineers go beyond API calls and need software
engineering rigor for agents, orchestration, and production systems.

Learn these in order:

- Python with FastAPI or Flask for API services
- a database (Postgres with pgvector is a practical start)
- Docker for containerization and deployment
- Git, CI, and basic cloud deployment

Pair this stage with
[Machine Learning for Software Engineers]({{ '/guides/machine-learning-for-software-engineers/' | relative_url }})
and
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}).

## Stage 2: Add LLM Calls and Structured Outputs

Once you can ship a service, add a model call. Start with a simple chat
endpoint that calls an LLM API and returns structured output. The first
milestone is a working API that a real user can interact with.

[Sandra Kublik]({{ '/people/sandrakublik/' | relative_url }}) describes the
product-thinking side in
[Practical LLM Use Cases and Product Patterns]({{ '/podcasts/practical-llm-use-cases-and-product-patterns/' | relative_url }}).
She covers model choice, architecture trade-offs, and the decision between
proprietary and open-source models based on cost, latency, and data risk.

[Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }}) enters
here: provide examples, context, and clear instructions rather than relying on
zero-shot calls. Use
[LLMs]({{ '/wiki/llms/' | relative_url }}) and
[Generative AI]({{ '/wiki/generative-ai/' | relative_url }}) for concept
depth.

Build:

- one API endpoint that calls an LLM and returns JSON
- one frontend page or CLI that lets a user interact with the model
- one prompt template with examples and output formatting

## Stage 3: Build Evaluation Before More Architecture

The biggest mistake AI engineers make is adding retrieval and agents before
they can measure whether outputs are good. Build a test set and an evaluation
harness early.

[Long-Context LLM Evaluation]({{ '/wiki/long-context-llm-evaluation/' | relative_url }})
and
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
cover the testing discipline. In
[Applied LLM Research and Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}),
guest research on context window performance shows a measurable drop around
32k-64k tokens, which is why chunking and retrieval beat stuffing long contexts.

[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
adds the evaluator-optimizer pattern: use gold test sets, categorize failures,
and prioritize retrieval fixes based on error analysis rather than guessing.

Build:

- a gold test set of 20-50 examples with expected outputs
- an automated scoring script that runs after each change
- a failure log that categorizes errors by type

## Stage 4: Add Retrieval When Knowledge Is the Bottleneck

When the model needs domain-specific knowledge it wasn't trained on, add
retrieval-augmented generation. Do not add RAG before you have evaluation in
place, because you won't know if retrieval helps or hurts.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) explains the
retrieval-over-retraining tradeoff in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
She argues retrieval beats continuous retraining for keeping answers current.
The episode also covers vector databases, embedding strategies, and the
indexing-vs-query-time encoding split.

[RAG]({{ '/wiki/rag/' | relative_url }}),
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) give the
concept depth. Use
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
for the architecture overview and
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
for project ideas.

Build:

- one RAG pipeline that chunks documents, embeds them, and retrieves relevant passages
- one evaluation pass comparing RAG answers to baseline answers
- one citation feature that links answers to source passages

## Stage 5: Add Agents for Tool-Using Work

Agents make sense when the system needs to call external tools, make
multi-step decisions, or act on the user's behalf. Do not add agents when a
single LLM call with good context solves the problem.

[Building Agentic AI Engineering]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
covers the full agent stack: orchestration, tools, memory, planning
strategies, and the code-agent-vs-natural-language-agent tradeoff. The episode
also covers when retrieval is enough and when agents are needed.

[From Game AI to Modern AI Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }})
adds agent workflow design, the minimalism principle, and task decomposition.
The episode covers OpenAI Agent SDK, MCP integration, and sequential thinking
servers.

Use
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) for
concept depth.

Build:

- one agent that calls an external API (search, database, or tool)
- one multi-step workflow that uses planning and self-reflection
- one evaluation pass with outcome-based assertions

## Stage 6: Operate the System in Production

Production AI engineering adds monitoring, cost control, security, and
incident response. The system must fail in observable ways and recover.

[Production-Ready AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})
covers data trust and testing for AI pipelines, prompt caching and token
optimization, and open-source model deployment experience. The episode bridges
data engineering and AI engineering by showing how preprocessing and data
quality feed model quality.

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) introduces
"Agent Ops" in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).
At the "Orchestration and the Rise of Agent Ops" section, he argues that
orchestration, monitoring, and operational discipline will define the next
phase of AI engineering.

[Generative AI Chatbots in Production Security]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
covers the security side: prompt injection, data exfiltration, output
validation, non-LLM classifiers as defenses, and human-in-the-loop review.

Use
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}), and
[Prompt Injection and Chatbot Risk Management]({{ '/wiki/prompt-injection-and-chatbot-risk-management/' | relative_url }})
for production safety. Use
[AI Infrastructure Cost and Ownership]({{ '/wiki/ai-infrastructure-cost-and-ownership/' | relative_url }})
for cost discipline.

Build:

- one monitoring dashboard for token usage, latency, and error rates
- one cost alerting mechanism
- one incident response runbook for hallucination or failure scenarios

## Portfolio Project Sequence

Your portfolio should show the full path, not isolated demos. Aim for one
project that covers stages 2 through 4 at minimum:

1. An LLM-backed API service with structured output and tests
2. A RAG application with evaluation and citations
3. An agent that uses tools and has outcome-based tests

Use
[AI Engineering Portfolio Projects]({{ '/wiki/ai-engineering-portfolio-projects/' | relative_url }})
for detailed project ideas. Pair with the
[LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }})
for the deeper production build path.

## When to Stop Studying and Build

[Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }}) is the
clearest signal that the path works. She went from a career break to an AI
engineer role by building a capstone project, prototyping with AI dev tools,
and interviewing with a PDF Q&A assistant as her portfolio artifact
([How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }}),
6:43 and 10:43).

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) adds the
side-project philosophy: source inspiration from daily life, build small
things, and let project work teach the business side
([Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})).

Stop studying when you can build, evaluate, and explain one project
end-to-end. The certificate or course completion matters less than a deployed
system with tests and monitoring.

## Related Pages

- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
- [AI Engineering Roadmap (Wiki)]({{ '/wiki/ai-engineering-roadmap/' | relative_url }})
- [LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }})
- [AI Engineering Portfolio Projects]({{ '/wiki/ai-engineering-portfolio-projects/' | relative_url }})
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
- [Nontraditional Paths to AI Engineering]({{ '/wiki/nontraditional-paths-to-ai-engineering/' | relative_url }})
- [Machine Learning Engineer Roadmap]({{ '/roadmaps/machine-learning-engineer-roadmap/' | relative_url }})
- [LLM System Design Interview]({{ '/guides/llm-system-design-interview/' | relative_url }})
