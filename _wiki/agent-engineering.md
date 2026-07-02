---
layout: wiki
title: "Agent Engineering"
summary: "How DataTalks.Club guests define AI agents and engineer them through workflow design, tools, retrieval, evaluation, guardrails, security, and production constraints."
related:
  - AI Engineer Role
  - AI Engineering Roadmap
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Multi-Agent Systems
  - AI Red Teaming
  - Responsible AI and Governance
  - Tools
---

Agent engineering is the practice of building AI systems that can pursue a
goal and act inside a workflow. These systems may use tools, retrieve
information, and keep task state. Agents in these discussions aren't chatbots
with longer prompts; they include on-call assistants, email assistants, coding
agents, and enterprise search assistants, along with multi-agent support systems
and workflow automation.

An agent is defined around autonomy and objectives, tied to LLM reasoning, and
extended with orchestration, tool use, memory, and knowledge stores
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Agent engineering therefore sits next to
[[LLM Production Patterns]],
[[retrieval-augmented-generation|Retrieval-Augmented Generation]],
and [[LLM Evaluation Workflows]].

## Key Agent Episodes

The agent discussions in the podcast cluster around six recurring threads:

- [[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]] with [[person:ranjithakulkarni|Ranjitha Kulkarni]] for autonomy, orchestration, tools, memory, and SRE workflows. The same episode covers agentic RAG, MCP-style tool protocols, and goal-based evaluation.
- [[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]] with [[person:adityagautam|Aditya Gautam]] for enterprise adoption, specialized models, guardrails, and data lineage. It also covers multi-tenant evaluation, human-label alignment, and deployment risk.
- [[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]] with [[person:micheallanham|Micheal Lanham]] for the lineage from game AI and multi-agent systems to LLM agents. It also covers task decomposition, orchestration designs, SDKs, MCP integration, coding agents, and monitoring.
- [[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]] with [[person:hugobowneanderson|Hugo Bowne-Anderson]] for generator-evaluator loops, embedded workflow assistants, and RAG-to-agent progression. Examples include email assistants, agent memory, and small-start evaluation.
- [[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]] with [[person:pauliusztin|Paul Iusztin]] for agents inside the wider AI engineering skill stack.
- [[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]] with [[person:mariasukhareva|Maria Sukhareva]] for security risks that become sharper when an LLM can retrieve data or take actions.

## Agents as Workflow Actors

Across these episodes, an agent is an LLM-backed system that can decide the next
step in a task rather than only return one answer. It may call APIs or run
search. It may also look at logs, draft code, update a document, or route work
to another component.

Beyond prompts, engineers define task decomposition, tool interfaces, and
retrieved context. They also define permissions, evaluation, observability, and
fallback behavior.

There is a strong boundary between
[[retrieval-augmented-generation|RAG]] and agents. Some cases need only
retrieval, while others need an agent, with retrieval treated as one tool an
agent can call
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

The same progression appears in practical LLM work: start with chunking and
embeddings for quick RAG wins, then add tool calls and agent behavior once teams
need them
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Agent engineering also sits inside the
[[AI Engineer Role]] and a broader AI product stack: the full-stack AI engineer
skill set, RAG and knowledge management, and the move from techniques to shipping
AI products
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]]).

## Reliability, Adoption, and Governance

Guests agree that agents need tool use, context, and evaluation. They differ on
the first design constraint. It may be operational reliability, adoption path,
orchestration style, or enterprise governance.

[[person:ranjithakulkarni|Ranjitha Kulkarni]] starts from production workflows,
using on-call automation and SRE workflows as examples that cover logs, metrics,
and remediation. Agents need usable integrations before they can help with
operational work
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

[[person:hugobowneanderson|Hugo Bowne-Anderson]] starts from practical adoption
with a framework that begins with the problem, starts small, then adds data and
evaluation. An email assistant example shows a concrete path from Gmail API
access and RAG to a useful assistant
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

[[person:micheallanham|Micheal Lanham]] starts from workflow design and
multi-agent history, emphasizing minimalism and task decomposition, comparing
sequential flows with manager-agent orchestration, and bringing in the OpenAI
Agent SDK and MCP integration
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

[[person:adityagautam|Aditya Gautam]] starts from enterprise risk, linking
specialized models to agent governance, guardrails, and data lineage, and tying
evaluation to multi-tenancy, scale, and alignment with human labels
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

## Agent Design

Agent design begins with the task boundary. A useful agent needs a concrete job,
not a vague instruction to "be helpful." Planning can be single-step, multi-pass,
or self-reflection
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
A planning agent also needs limits on how long it can plan, which tools it can
call, and when it should stop.

A practical design warning is to start with the smallest workflow that solves
the task, favoring minimalism and task decomposition and distinguishing a
sequential pipeline from manager-agent orchestration
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). That
distinction matters for
[[Software Engineering]]
because a linear workflow is easier to test and debug than an open-ended
multi-agent system.

The product reason to use agents is that value appears when the system acts on
documents, APIs, and workflow state, not only when it chats. Embedded agents fit
Slack-style workflows and proactive assistants
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
That makes agent design a product workflow question as much as a model question.

## Tooling and Integration

Tools are part of the agent's interface with the world, but bad tools create
noisy context and unsafe actions. Good tools expose constrained actions, typed
inputs, traceable outputs, and enforceable permissions.

Prompts, SDKs, and tool wrappers pair with integration abstractions for diverse
tools, and agent marketplaces and MCP-style protocols address making tools
discoverable and callable
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
These are [[Tools]]
questions, but the agent page keeps the workflow-specific part. Tools should
match the decisions the agent is allowed to make.

The OpenAI Agent SDK and MCP integration appear again alongside scratchpads and
internal reasoning servers as a separate integration layer
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). The
agent may need private reasoning state or task state that isn't shown directly to
the user. That state should be observable enough for debugging, but it shouldn't
replace tests.

A production AI view covers a browser extension architecture with a backend AI
integration, plus search-focused assistants and tool selection
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). Those
examples keep agent engineering close to normal application architecture. A tool
call still needs a backend, authentication, latency control, and failure
handling.

## Retrieval, Memory, and Context

Retrieval is one of the main tools agents use. It gives the system access to
documents, logs, and emails. It can also expose code, tickets, and other
external state. Guests don't treat retrieval as automatic. They discuss
chunking, metadata, wrappers, and failure analysis.

Context engineering is the design of effective LLM inputs. The RAG reality check
is that latency, cost, and noisy context can break a system; retrieval backends
often need reworking, along with chunking, metadata, and wrappers so retrieved
information fits the agent's job
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For the broader retrieval architecture, see
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].

Chunking strategies include fixed length and sliding windows, and retrieval-based
memory is distinct from multi-turn conversation memory
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
That distinction is central to agent engineering. A support assistant may need
durable customer facts and ticket history, while a coding agent may need
repository context and task state. A short conversation memory isn't enough for
either system.

RAG and knowledge management connect to the AI engineer skill stack
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]]).
That link matters because many agent failures are knowledge-system failures. If
the source documents lack metadata, ownership, or a refresh cadence, the agent
will act on weak context.

## Evaluation and Testing

Agent evaluation checks whether the system accomplished the goal under realistic
conditions. It can't only compare one final string to a reference answer
because multiple valid tool-call paths may exist.

Agent evaluation uses custom datasets and system benchmarks, mocked tools,
integration tests, and regression tests, and emphasizes goal-based evaluation and
outcome assertions over exact paths
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Those evaluation choices belong with
[[LLM Evaluation Workflows]]
and [[Testing]].

A generator-evaluator loop provides automated quality control, with gold test
sets weighed against cost and representativeness, and failure analysis deciding
whether retrieval needs to change
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Those evaluation habits are useful before a system becomes agentic, then become
more important when the system starts calling tools.

The enterprise version adds evals for multi-tenancy and scale and aligning LLM
judges with human labels
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). Evaluation and
monitoring tools such as Arize Phoenix round it out
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Together, these episodes make evaluation part of daily agent work rather than a
one-time benchmark.

## Production and Governance

Production agents need permission checks, audit logs, lineage records, and
guardrails. They also need monitoring and human review for high-risk actions.
Cost and latency controls matter because tool calls, retrieval, and multi-step
reasoning can multiply runtime.

The strongest governance source covers reliability in legal and healthcare
settings, links guardrails and data lineage to Agent MLOps, and names user
feedback loops along with infrastructure and deployment risks
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

Those controls overlap with security work on prompt overload and knowledge-base
retrieval attacks
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
For agents, the same retrieval risk can become an action risk. That matters when
the system can call tools, write data, send messages, or trigger workflows.
Teams keep agents governed by narrowing tool permissions and tracing the data
used for each answer or action. They also keep human review around high-impact
decisions and test failures repeatedly. Practical agent work therefore draws on
[[AI Red Teaming]],
[[Responsible AI and Governance]],
[[Data Governance]], and
[[Production]].

These discussions place agent engineering beside
[[Responsible AI and Governance]]
and [[Production]].

The operational discipline of monitoring, governing, and deploying agents in
production is covered as
[[Agent Ops]].

Cost and performance mechanics come from prompt evaluation and cost tradeoffs,
with prompt compression and caching treated as model-efficiency tools
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). These
techniques aren't agent-specific, but agents make them more important because
every extra step can add tokens, latency, and failure modes.

Generic agent products miss details that live in each task. Teams need specific
integrations, context, datasets, and evaluation
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
An agent should be designed around a real workflow and measured against that
workflow.

## Related Pages

These pages cover the role, retrieval layer, evaluation work, and production
constraints around agent systems.

- [[AI Engineer Role]]
- [[AI Engineering Roadmap]]
- [[LLM Production Patterns]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
- [[retrieval-augmented-generation|RAG]]
- [[LLM Evaluation Workflows]]
- [[Tools]]
- [[Production]]
- [[Responsible AI and Governance]]
- [[Agent Ops]]
