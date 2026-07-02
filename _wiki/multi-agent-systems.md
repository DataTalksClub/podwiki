---
layout: wiki
title: "Multi-Agent Systems"
summary: "How DataTalks.Club guests discuss multi-agent systems through sequential flows, manager-agent orchestration, peer collaboration, tool use, memory, evaluation, and guardrails."
related:
  - Agent Engineering
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Responsible AI and Governance
  - Evolutionary Algorithms
---

Multi-agent systems split an [[agent-engineering|AI agent]]
task across more than one specialized agent. That split is an engineering
choice, not the default structure of agentic software.
The design question is whether a task needs a sequential handoff or a manager
agent; some tasks need direct collaboration between agents. In many cases,
[[agent engineering]] with
bounded tools and tests is enough.

The most explicit taxonomy contrasts sequential agent flows, manager-agent
orchestration, and direct collaboration
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Agent tools, memory, and evaluation define the production boundaries
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Memory or agents should not be added before the product needs them
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Production agents are framed through governance and evaluation
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

## Coordination Patterns

A sequential flow is an assembly line of agents: one handles requirements,
another plans, and another executes, each passing its output to the next
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). Teams
can review this more easily because work moves through a known order.

Manager-agent orchestration adds a front-facing agent that calls other agents
as needed. The orchestrator looks at outputs, gives feedback, and checks whether
the work still meets the requirements
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). Teams
use manager-agent orchestration when the user should see one interaction, but
the system needs separate planning and building agents, and possibly review or
repair agents behind it.

Peer collaboration lets agents exchange outputs directly through a shared
message channel. It is powerful but expensive and weak for real-time responses
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]), and is
best reserved for complex problems where the input and desired output are clear
but the path between them is detailed. Coding work is a concrete example: a
designer, front-end developer, and back-end developer can work in parallel while
they share feedback
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Flow, Orchestration, and Collaboration

These designs differ in how agents communicate. Sequential flows use handoffs
between agents, orchestration puts routing and review with a manager agent, and
collaboration lets agents share intermediate outputs with each other.

Minimalism helps: break the work into tasks for individual agents so that no
single large agent carries too many tools and instructions
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). This
matters because a multi-agent system multiplies prompts, tool calls, state, and
possible failure paths. A sequential requirements-plan-execution flow is often
enough before a team adds a manager agent or peer collaboration.

Manager-agent orchestration becomes useful when the system has to choose
between workflows, retry a failed step, or compare output to requirements. An
orchestration agent can review the output and choose whether to rerun or
continue, and can switch between parallel development tasks when needed
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). This
keeps the coordination logic in one place instead of letting every agent
negotiate with every other agent.

Agents in direct collaboration share outputs that become inputs for other
agents, refining a solution together. This style resembles
[[evolutionary algorithms]]
because collaboration can resemble candidate search: agents first generate
candidate outputs and then exchange them for judgment and improvement
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). The
comparison is limited; not every multi-agent system is an evolutionary
algorithm.

## Tools and Shared State

Modern agents orchestrate calls to LLMs and tools, plus knowledge stores and
memory
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Multi-agent systems inherit that same machinery, then add a coordination layer
between agents.

Tool boundaries matter more when several agents can act. An SRE example has an
agentic system move across logs and metrics, reaching source code, Kubernetes,
and remediation options
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Teams abstract over different observability and deployment tools but still need
domain knowledge for each source's quirks
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
In a multi-agent design, teams define which agent can call which
[[tools]], and what each call returns to the rest of the system.

Current multi-agent tooling includes the OpenAI Agents SDK and handoffs, along
with guardrails and MCP-style integrations
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Reasoning scratchpads are separate from inter-agent communication: agents may
use a sequential-thinking server to plan, but they usually pass results to other
agents rather than expose every reasoning step
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Memory and Context

Multi-agent systems need an explicit memory boundary because each agent may see
a different slice of context. Context engineering means choosing what to send to
the LLM instead of stuffing every document, log line, or metric into the prompt
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For manager-agent orchestration, the manager often needs requirements and
state. It may also need summaries, while the worker agent needs task-specific
inputs and tool results.

[[retrieval-augmented-generation|RAG]] is one tool an agent can choose, not the
whole system. Agents move beyond a fixed retrieval workflow by deciding when to
use search, tables, MongoDB queries, or other tools
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Retrieval can serve a single worker or the manager, and it can also serve a
shared workspace. The team still has to define who may read and write each
piece of state.

Many systems don't need memory at all: add tools or memory only as needed,
distinguishing retrieval-based memory from active conversation memory
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
In a multi-agent system, that caution prevents teams from adding a memory agent
too early, or a shared scratchpad or long-term profile store before the task
requires one.

## Evaluation

Multi-agent evaluation checks whether the system reached the goal, used the
right tools, and stayed inside the allowed workflow. Agent evaluation has to
cover the answer, tool calls, parameters, and other behavior, not only a final
response
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Software-style tests apply here.

Those tests mock tools, cover integrations, rerun regressions, and assert
outcomes. A calendar example evaluates whether the system created the right
invite, not whether it followed one exact path.

The same point applies from the monitoring side: measure agent performance for
consistency, understand variance in outputs, and monitor LLM communication and
prompts with tools such as Arize Phoenix
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). In a
manager-agent system, traces need to show which agent acted, which tool it
called, what it passed on, and where a rerun or review happened.

This extends to multi-tenant and regulated settings. For a multi-agent workflow
serving separate customers, teams need customer-specific golden datasets, LLM
judges aligned to human labels, red-team stress testing, and human review for
critical actions such as high-value refunds
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). In multi-agent
systems, those requirements belong with
[[LLM Evaluation Workflows]]
and [[AI Red Teaming]].

## Guardrails and Governance

Multi-agent systems create a governance problem because data and actions can
move through several agents before the user sees an answer. Companies need to
know what each agent is doing, how user data is processed, where data has gone,
and what offline workflows touched it
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). That visibility
connects to retention, data lineage, auditability, and compliance.

Guardrails also have to sit near the tool boundary. A refund example puts
high-value Stripe actions behind human review, even when the agent handles
lower-risk cases
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). In a
manager-agent design, the manager can enforce that policy by routing edge cases
to a human queue instead of passing them to another agent.

Human review remains part of production evaluation. Deploying an agent without
human-in-the-loop data is not advisable: the team needs a ground truth for the
LLM judge and a way to detect drift
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). That makes
multi-agent governance part of
[[Responsible AI and Governance]]
rather than a separate prompt-engineering concern.

The broader production discipline of deploying, monitoring, and governing
agents is covered as
[[Agent Ops]].

## Use Cases and Limits

Add agents only when the workflow demands them. A working RAG system shouldn't
gain agentic complexity unless users need broader actions; tool calls or
corpus-level operations can justify the extra machinery when the fixed path
can't answer
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Start with the problem, then a small LLM system, with data and evaluation next
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A similar boundary separates RAG and agents. RAG works when the task is simple
question answering over a large search space. Agents become useful when context
changes, planning is dynamic, data comes from multiple sources, or the task
needs multiple API integrations
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Use multi-agent systems when one agent's planning and tool use become too broad
to test or reason about as a single role. Memory can create the same pressure.

That decision sits inside normal product engineering. A vertical finance agent
is a full product with a TypeScript UI and FastAPI backend, using RAG and agents
alongside AWS infrastructure and data pipelines, with evaluation part of the same
product work
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's AI engineering episode]]).

Durable workflow tools can provide queues and retries for the agentic world
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's AI engineering episode]]).
That keeps multi-agent design close to
[[AI Engineer Role]] work.
Teams still own data and interfaces, tests and traces, permissions, and the
user-facing product.
