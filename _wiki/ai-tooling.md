---
layout: wiki
title: "AI Tooling"
summary: "How DataTalks.Club podcast guests choose and operate AI tooling for model APIs, open-source LLMs, RAG, prompts, agents, evaluation, and deployment."
related:
  - Tools
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Retrieval-Augmented Generation
  - Agent Engineering
  - MLOps Tools
  - AI Engineering
---

AI tooling covers the tools around model access and deployment. It also covers
retrieval and prompts, agent frameworks, evaluation, and observability. In
DataTalks.Club podcast discussions, guests rarely treat a model API as the
whole product.
They describe AI tools as a stack around data and context. The stack also
includes actions, tests, traces, and production ownership.

For the whole role, use the
[[AI Engineer Role]]. Use
[[LLM Tools]] for practical stack
selection around model APIs, RAG, and evaluation. It also covers agents,
observability, and cost.
Use
[[LLM Production Patterns]]
for production architecture and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
for retrieval systems. Use
[[Agent Engineering]] for
tool-using agents and [[LLM Evaluation Workflows]]
for evaluation design.

## Tooling Stack Map

AI tooling starts with [[LLMs]] and general
[[Tools]], but the podcast discussions place
most of the engineering work around the model boundary. Teams structure model
inputs with [[Prompt Engineering]]
and attach outside knowledge with
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].
[[Vector Databases]] and
[[Embeddings]] support that retrieval
layer. Agent frameworks, evaluation tools, monitoring, and deployment systems
then turn the model call into an owned product.

[[person:pauliusztin=>Paul Iusztin]] presents that full
stack in his AI engineering discussion
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].
[[person:bartoszmikulski=>Bartosz Mikulski]] connects it
to production data workflows
[[cite:production-ready-ai-engineering|Production AI Engineering]].
[[person:meryemarik=>Meryem Arik]] anchors model
serving and retrieval choices in deployment work
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

[[person:hugobowneanderson=>Hugo Bowne-Anderson]] focuses
on iterative testing
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
[[person:ranjithakulkarni=>Ranjitha Kulkarni]]
extends AI tooling to agents
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
[[person:vincentwarmerdam=>Vincent Warmerdam]]
uses open-source ML tooling to show how maintainers, documentation, plugins,
and business models affect the tools teams rely on
[[cite:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].

## Tools Around the Model

Guests define AI tooling as services and libraries around the
model. Those tools give an LLM useful context and controlled actions. They also
make behavior measurable.

[[person:pauliusztin=>Paul Iusztin]] places RAG and
knowledge management in the same AI product stack as agents, evaluation, and
LLMOps
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].
That framing links AI tooling to
[[AI Engineering]], but the tools
matter because they package the system around the model.

[[person:hugobowneanderson=>Hugo Bowne-Anderson]]
describes the same tooling loop from a build perspective. He starts with
prompting practices and generator-evaluator checks. He introduces gold test
sets, then brings in failure analysis, logs, and traces
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
Tools are useful when they shorten that loop.

## Build, Buy, and Framework Boundaries

Guests differ on how much of the stack teams should buy, borrow, or build.
[[person:meryemarik=>Meryem Arik]] compares API models
with open-source models. Her discussion emphasizes control and privacy. It also
covers fine-tuning, API drift, latency, and hardware cost
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

[[person:bartoszmikulski=>Bartosz Mikulski]] looks at
tool choice through production data workflows. He compares open-source model
and assistant tools, then covers coding-assistant workflows
[[cite:production-ready-ai-engineering|Production AI Engineering]]. Those
assistant workflows are covered in depth as [[AI Coding Tools]].

[[person:ranjithakulkarni=>Ranjitha Kulkarni]] draws a different boundary for
agent frameworks by discussing prompt-level implementations, SDKs, and tool
wrappers. She then compares building from scratch with libraries such as
LangChain, the OpenAI Agents SDK, and smaller agent frameworks
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Teams choose based on control over tool interfaces, state, tests, and failure
handling more than novelty.

## Model APIs and Open-Source Models

Model tooling begins with the API-versus-open-source choice. Meryem reviews the
open-source landscape and explains why teams might choose open-source models
for privacy, control, or fine-tuning. She also warns that API providers can
change model behavior
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
Teams then need evaluation and release checks as part of the tooling decision.

The same episode separates prototyping from production. Meryem describes when
GPT-style APIs are useful for prototyping and when open-source models become
attractive. Latency and cost move the choice from model quality into deployment
engineering
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At that point, model tooling becomes
[[MLOps]] and
[[MLOps Tools]], not only to prompt
design.

## RAG and Vector Search Tooling

RAG tools appear when teams need fresh or private knowledge without retraining
the model. Meryem makes this boundary explicit in her LLM deployment discussion
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

Retrieval handles changing knowledge, while fine-tuning is better suited to
specialized behavior, domain adaptation, or tone. She covers grounding answers
with indexed documents, retrieval-augmented responses, embeddings, and vector
databases
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
That distinction is the same decision boundary covered in
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].


Hugo turns RAG tooling into an iteration cycle. He recommends quick business
wins with chunking and embeddings, then compares fixed-length chunks, sliding
windows, and context rot
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
Those choices sit next to [[Vector Databases]]
and [[Embeddings]]. They also connect to
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

Ranjitha adds the production caution. Her agentic AI discussion covers RAG
latency, cost, garbage-in/garbage-out failure modes, and backend changes that
make retrieved material more useful to the LLM. Retrieval can also become a
tool an agent calls rather than the whole architecture
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].

## Prompt and Context Tooling

Prompt tools are most useful when they make inputs structured, reusable, and
testable. Bartosz introduces in-context learning and examples, then links
prompt formatting to cost-aware evaluation. He treats prompt compression and
prompt caching as engineering tools for reducing tokens, latency, and repeated
work
[[cite:production-ready-ai-engineering|Production AI Engineering]].

Hugo covers a complementary workflow in practical LLM engineering. He discusses
role prompts, structured outputs, and timestamps, then builds transcript
workflows with Gemini and Descript. He also uses Loom, automation, and GitHub
Actions
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
Prompt engineering often belongs inside a larger pipeline, not a one-off chat
session.

Ranjitha uses the term context engineering in her agentic AI discussion. She
focuses on designing effective LLM inputs and adds chunking, metadata, and
wrappers
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
That makes context tooling a bridge between
[[Prompt Engineering]],
[[retrieval-augmented-generation=>RAG]], and
[[Agent Engineering]].

## Agent Frameworks and Tool Protocols

Agent tooling shows up when a system must plan, call tools, and update state
inside a workflow. Ranjitha defines agents around autonomy and objectives, then
adds tools, memory, and knowledge stores. She compares single-step planning,
multi-pass execution, and self-reflection
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].

Ranjitha makes the tooling boundary practical by discussing code agents versus
natural-language agents. She covers SRE workflows that use logs, metrics, and
remediation. She also adds integration abstractions and references agent
marketplaces and tool protocols such as MCP
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].

Hugo reaches a similar boundary in practical LLM engineering. Teams move from
RAG into tool calls only when the workflow needs actions
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].

## Evaluation and Observability Tooling

Evaluation tools make AI systems easier to change without guessing. Hugo's
practical LLM engineering episode gives the clearest loop. Hugo covers
generator-evaluator checks and representative gold tests. He also adds failure
categories, logs, and traces
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
That loop connects AI tooling directly to
[[Evaluation]],
[[LLM Evaluation Workflows]],
and [[Model Monitoring]].

Ranjitha extends that loop to agents. Her agentic AI discussion covers custom
datasets and system benchmarks before moving to mocked tools, integration
tests, and regression tests. She also argues for outcome-based checks because
an agent may solve the same goal through different paths
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Paul also places evaluation inside the AI engineering skill stack
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].

## Deployment and Operational Tooling

Deployment tooling matters because LLM systems inherit classic production
constraints. Teams still have to manage data quality and latency. They also
need cost control, testing, and recovery. Bartosz makes this link in
production-ready AI engineering
[[cite:production-ready-ai-engineering|Production AI Engineering]].

Bartosz covers data trust, pipeline tests, and tools such as Great Expectations
and Soda. He also covers preprocessing and fine-tuning data for AI systems
[[cite:production-ready-ai-engineering|Production AI Engineering]].

Meryem covers the serving side in LLM production by describing TitanML's
training, optimization, and serving stack. She then covers model size,
compression, and inference optimization
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
These episodes place AI tooling next to [[Machine Learning System Design]]
and [[MLOps Tools]], especially when
teams move past demos.

## Open-Source Tool Sustainability

Open-source AI tooling depends on maintainers, governance, documentation, and
business models. [[person:vincentwarmerdam|Vincent Warmerdam]]
uses scikit-learn and related tools as the example in open-source ML tooling.
He discusses governance and NumFOCUS, then distinguishes core scikit-learn
features from plugin ecosystems. He treats maintainer transitions and
motivation as part of tool quality
[[cite:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].

The same episode shows why tool ecosystems need more than code. Vincent covers
documentation, interactive content, and videos
[[cite:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].

He then walks through Skrub's table vectorizer and pragmatic tabular defaults
before covering funding, training, consulting, and partnerships as
sustainability mechanisms
[[cite:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].
That makes [[Open Source and Developer Relations]] part of the AI tooling story.

## Neighboring Tooling Areas

AI tooling overlaps with several adjacent system concerns:

- [[LLM Production Patterns]] for model, RAG, agent, and deployment patterns.
- [[LLM Evaluation Workflows]] for gold sets, failure analysis, judges, and agent tests.
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for retrieval architecture and vector search.
- [[Agent Engineering]] for tool-using workflows and agent evaluation.
- [[MLOps Tools]] for the broader machine learning operations toolkit.
