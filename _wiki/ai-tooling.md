---
layout: wiki
title: "AI Tooling"
summary: "How DataTalks.Club podcast guests choose and operate AI tooling for model APIs, open-source LLMs, RAG, prompts, agents, evaluation, observability, and deployment."
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
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
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
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].
[[Vector Databases]] and
[[Embeddings]] support that retrieval
layer. Agent frameworks, evaluation tools, monitoring, and deployment systems
then turn the model call into an owned product.

[[person:pauliusztin|Paul Iusztin]] presents that full
stack in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]].
[[person:bartoszmikulski|Bartosz Mikulski]] connects it
to production data workflows in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
[[person:meryemarik|Meryem Arik]] anchors model
serving and retrieval choices in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

[[person:hugobowneanderson|Hugo Bowne-Anderson]] focuses
on iterative testing in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
[[person:ranjithakulkarni|Ranjitha Kulkarni]]
extends AI tooling to agents in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
[[person:vincentwarmerdam|Vincent Warmerdam]]
uses [[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]
to show how maintainers, documentation, plugins, and business models affect the
tools teams rely on.

## Tools Around the Model

Guests define AI tooling as services and libraries around the
model. Those tools give an LLM useful context and controlled actions. They also
make behavior measurable.

[[person:pauliusztin|Paul Iusztin]] places RAG and
knowledge management in the same AI product stack as agents, evaluation, and
LLMOps. He covers that stack in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]]
at 29:12 and 42:28. That framing links AI tooling to
[[AI Engineering]], but the tools
matter because they package the system around the model.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
describes the same tooling loop from a build perspective in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
He starts with prompting practices at 11:11 and adds generator-evaluator checks
at 13:56. He introduces gold test sets at 23:00, then brings in failure
analysis, logs, and traces at 26:43-27:38. Tools are useful when they shorten
that loop.

## Build, Buy, and Framework Boundaries

Guests differ on how much of the stack teams should buy, borrow, or build.
[[person:meryemarik|Meryem Arik]] compares API models
with open-source models in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
at 16:48 and 49:44. Her discussion emphasizes control and privacy. It also
covers fine-tuning, API drift, latency, and hardware cost.

[[person:bartoszmikulski|Bartosz Mikulski]] looks at
tool choice through production data workflows in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His 33:42 chapter compares open-source model and assistant tools. The 42:05 and
44:38 chapters cover coding-assistant workflows, which are covered in depth as
[[AI Coding Tools]].

[[person:ranjithakulkarni|Ranjitha Kulkarni]] draws a
different boundary for agent frameworks. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
she discusses prompt-level implementations, SDKs, and tool wrappers at 18:23.
At 44:08-46:00 she compares building from scratch with libraries such as
LangChain, the OpenAI Agents SDK, and smaller agent frameworks. Teams choose
based on control over tool interfaces, state, tests, and failure handling more
than novelty.

## Model APIs and Open-Source Models

Model tooling begins with the API-versus-open-source choice. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
Meryem reviews the open-source landscape at 13:45. At 16:48, she explains why
teams might choose open-source models for privacy, control, or fine-tuning. She
also warns at 18:46 that API providers can change model behavior. Teams then
need evaluation and release checks as part of the tooling decision.

The same episode separates prototyping from production. At 49:44, Meryem
describes when GPT-style APIs are useful for prototyping and when open-source
models become attractive. At 51:35, latency and cost move the choice from model
quality into deployment engineering. At that point, model tooling becomes
[[MLOps]] and
[[MLOps Tools]], not only to prompt
design.

## RAG and Vector Search Tooling

RAG tools appear when teams need fresh or private knowledge without retraining
the model. Meryem makes this boundary explicit at 40:46 in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

Retrieval handles changing knowledge, while fine-tuning is better suited to
specialized behavior, domain adaptation, or tone. At 42:02-48:01 she covers
grounding answers with indexed documents and retrieval-augmented responses. She
also covers embeddings and vector databases. That distinction is the same
decision boundary covered in
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]].


Hugo turns RAG tooling into an iteration cycle in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 44:26 he recommends quick business wins with chunking and embeddings. At
48:20 he compares fixed-length chunks, sliding windows, and context rot. Those
choices sit next to [[Vector Databases]]
and [[Embeddings]]. They also connect to
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].

Ranjitha adds the production caution. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
her 29:30 chapter covers RAG latency, cost, and garbage-in/garbage-out failure
modes. At 31:38 and 32:48, she describes backend and context changes that make
retrieved material more useful to the LLM. At 36:11, retrieval becomes a tool an
agent can call rather than the whole architecture.

## Prompt and Context Tooling

Prompt tools are most useful when they make inputs structured, reusable, and
testable. In [[podcast:production-ready-ai-engineering|Production AI Engineering]],
Bartosz introduces in-context learning and examples at 25:13. At 28:16 he
links prompt formatting and examples to cost-aware evaluation. At 30:00-31:45, prompt
compression and prompt caching become engineering tools for reducing tokens,
latency, and repeated work.

Hugo covers a complementary workflow in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 11:11, he discusses role prompts, structured outputs, and timestamps. At
12:22-17:38, he builds transcript workflows with Gemini and Descript. He also
uses Loom, automation, and GitHub Actions. Prompt engineering often belongs
inside a larger pipeline, not a one-off chat session.

Ranjitha uses the term context engineering in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 21:21 she focuses on designing effective LLM inputs. At 32:48 she adds
chunking, metadata, and wrappers. That makes context tooling a bridge between
[[Prompt Engineering]],
[[retrieval-augmented-generation|RAG]], and
[[Agent Engineering]].

## Agent Frameworks and Tool Protocols

Agent tooling shows up when a system must plan, call tools, and update state
inside a workflow. Ranjitha defines agents around autonomy and objectives at
11:00 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 12:31, she adds tools, memory, and knowledge stores. At 15:10, she compares
single-step planning, multi-pass execution, and self-reflection.

Ranjitha makes the tooling boundary practical by discussing code agents versus
natural-language agents at 19:58. At 22:50, she covers SRE workflows that use
logs, metrics, and remediation. At 24:59, she adds integration abstractions.
Later, at 48:00, she references agent marketplaces and tool protocols such as
MCP.

Hugo reaches a similar boundary in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 50:19, teams move from RAG into tool calls only when the workflow needs
actions.

## Evaluation and Observability Tooling

Evaluation tools make AI systems easier to change without guessing. Hugo's
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
episode gives the clearest loop. Hugo covers generator-evaluator checks at
13:56, representative gold tests at 23:00, and failure categories at 26:43. He
adds logs and traces at 27:38. That loop connects AI tooling directly to
[[Evaluation]],
[[LLM Evaluation Workflows]],
and [[Model Monitoring]].

Ranjitha extends that loop to agents. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
she discusses custom datasets and system benchmarks at 51:17. At 53:20, she
adds mocked tools, integration tests, and regression tests. At 56:02, she argues
for outcome-based checks because an agent may solve the same goal through
different paths. Paul also places evaluation inside the AI engineering skill
stack in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]]
at 42:28.

## Deployment and Operational Tooling

Deployment tooling matters because LLM systems inherit classic production
constraints. Teams still have to manage data quality and latency. They also
need cost control, testing, and recovery. Bartosz makes this link in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].

At 9:05-13:14 he covers data trust, pipeline tests, and tools such as Great
Expectations and Soda. At 18:38, data engineering appears again as
preprocessing and fine-tuning data for AI systems.

Meryem covers the serving side in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 23:37 she describes TitanML's train, optimization, and serving stack. At
25:26 she covers model size, compression, and inference optimization. These
episodes place AI tooling next to [[Machine Learning System Design]]
and [[MLOps Tools]], especially when
teams move past demos.

## Open-Source Tool Sustainability

Open-source AI tooling depends on maintainers, governance, documentation, and
business models. [[person:vincentwarmerdam|Vincent Warmerdam]]
uses scikit-learn and related tools as the example in
[[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].
At 10:28 he discusses governance and NumFOCUS. At 14:01 he distinguishes core
scikit-learn features from plugin ecosystems. At 18:11 and 21:51, maintainer
transitions and motivation become part of tool quality.

The same episode shows why tool ecosystems need more than code. Vincent covers
documentation, interactive content, and videos at 42:20.

He then walks through Skrub's table vectorizer and pragmatic tabular defaults
at 48:31. At 53:47 and 56:19, he covers funding and training. He also covers
consulting and partnerships as sustainability mechanisms. That makes [[Open Source and Developer Relations]]
part of the AI tooling story.

## Neighboring Tooling Areas

AI tooling overlaps with several adjacent system concerns:

- [[LLM Production Patterns]] for model, RAG, agent, and deployment patterns.
- [[LLM Evaluation Workflows]] for gold sets, failure analysis, judges, and agent tests.
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]] for retrieval architecture and vector search.
- [[Agent Engineering]] for tool-using workflows and agent evaluation.
- [[MLOps Tools]] for the broader machine learning operations toolkit.
