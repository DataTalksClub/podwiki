---
layout: wiki
title: "Multi-Agent Systems"
summary: "How DataTalks.Club guests frame multi-agent systems: coordination patterns, tool boundaries, memory, evaluation, and governance."
related:
  - Agent Engineering
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Responsible AI and Governance
  - Evolutionary Algorithms
---

Multi-agent systems split an [[agent-engineering|AI agent]]
task across more than one specialized agent. Teams make that split as an
engineering choice, not as the default structure of agentic software.
The design question is whether a task needs a sequential handoff or a manager
agent. Some tasks need direct collaboration between agents. In many cases,
[[agent engineering]] with
bounded tools and tests is enough.

The most explicit taxonomy contrasts sequential agent flows, manager-agent
orchestration, and direct collaboration
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Agent tools, memory, and evaluation define the production boundaries
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Memory or agents shouldn't be added before the product needs them
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Production agents are framed through governance and evaluation
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

## Coordination Patterns

Sequential flows move work through an assembly line of agents. One handles
requirements, another plans, and another executes. Each passes output to the
next ([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Teams can review this more easily because work moves through a known order.

Manager-agent orchestration adds a front-facing agent that calls other agents
as needed. The orchestrator reviews outputs and gives feedback. It checks
whether the work still meets the requirements
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). Teams
use manager-agent orchestration when the user should see one interaction.
Behind that interface, the system may still need separate planning and building
agents, plus review or repair agents.

Peer collaboration lets agents exchange outputs directly through a shared
message channel. It's powerful but expensive and weak for real-time responses
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Reserve it for complex problems where the input and desired output are clear,
but the path between them is detailed. Coding work is a concrete example. A
designer can work beside front-end and back-end developers while they share
feedback
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Flow, Orchestration, and Collaboration

These designs differ in how agents communicate. Sequential flows use handoffs
between agents, orchestration puts routing and review with a manager agent, and
collaboration lets agents share intermediate outputs with each other.

Minimalism helps when teams break work into tasks for individual agents. No
single large agent should have too many tools and instructions
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
A multi-agent system multiplies prompts, tool calls, state, and possible failure
paths. A requirements-plan-execution sequence often goes far enough before a
team adds a manager agent or peer collaboration.

Manager-agent orchestration becomes useful when the system has to choose between
workflows, retry a failed step, or compare output to requirements. An
orchestration agent can review the output and choose whether to rerun or
continue. It can also switch between parallel development tasks when needed
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). This
keeps the coordination logic in one place instead of letting every agent
negotiate with every other agent.

Directly collaborating agents share outputs that become inputs for other agents.
That exchange lets them refine a solution together. This style resembles
[[evolutionary algorithms]]
because collaboration can resemble candidate search. Agents first generate
candidate outputs, then exchange them for judgment and improvement
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

The comparison is limited because not every multi-agent system is an
evolutionary algorithm.

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

Current multi-agent tooling includes the OpenAI Agents SDK and handoffs. It also
includes guardrails and MCP-style integrations
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Reasoning scratchpads are separate from inter-agent communication. Agents may
use a sequential-thinking server to plan. They usually pass results to other
agents rather than expose every reasoning step
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Memory and Context

Multi-agent systems need an explicit memory boundary because each agent may see
a different slice of context. Context engineering means choosing what to send to
the LLM. It doesn't stuff every document, log line, or metric into the prompt
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For manager-agent orchestration, the manager often needs requirements and
state. It may also need summaries, while the worker agent needs task-specific
inputs and tool results.

[[retrieval-augmented-generation=>RAG]] is one tool an agent can choose, not the
whole system. Agents move beyond a fixed retrieval workflow by deciding when to
use search, tables, MongoDB queries, or other tools
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Retrieval can serve a single worker or the manager, and it can also serve a
shared workspace. The team still has to define who may read and write each
piece of state.

Many systems don't need memory at all. Teams should add tools or memory only
when the product needs them. They should also distinguish retrieval-based memory
from active conversation memory
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
In a multi-agent system, that caution prevents teams from adding a memory agent
too early. It also keeps a shared scratchpad or long-term profile store out of
the design until the task requires one.

## Evaluation

Multi-agent evaluation checks goal completion, tool choice, and workflow
boundaries. Agent evaluation has to cover the answer and tool calls. It also
covers parameters and other behavior, not only a final response
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Software-style tests apply here.

Those tests mock tools, cover integrations, rerun regressions, and assert
outcomes. A calendar example evaluates whether the system created the right
invite, not whether it followed one exact path.

Monitoring creates the same demand for traces and measurements, so teams measure
agent consistency and output variance. They monitor LLM communication and
prompts with tools such as Arize Phoenix
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
In a manager-agent system, traces need to show which agent acted and which tool
it called. They also need to show what the agent passed on, and where a rerun or
review happened.

This extends to multi-tenant and regulated settings. For a multi-agent workflow
serving separate customers, teams need customer-specific golden datasets and LLM
judges aligned to human labels. They also need red-team stress testing and human
review for critical actions such as high-value refunds
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). In multi-agent
systems, those requirements belong with
[[LLM Evaluation Workflows]]
and [[AI Red Teaming]].

## Guardrails and Governance

Multi-agent systems create a governance problem because data and actions can
move through several agents before the user sees an answer. Companies need to
know what each agent is doing and how user data is processed. They also need to
know where data has gone, and what offline workflows touched it
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). That visibility
connects to retention, data lineage, auditability, and compliance.

Guardrails also have to sit near the tool boundary. A refund example puts
high-value Stripe actions behind human review, even when the agent handles
lower-risk cases
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). In a
manager-agent design, the manager can enforce that policy by routing edge cases
to a human queue instead of passing them to another agent.

Human review remains part of production evaluation because deploying an agent
without human-in-the-loop data isn't advisable. The team needs a ground truth for
the LLM judge and a way to detect drift
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). That makes
multi-agent governance part of
[[Responsible AI and Governance]]
rather than a separate prompt-engineering concern.

The broader production discipline of deploying, monitoring, and governing
agents is covered as
[[Agent Ops]].

## Use Cases and Limits

Add agents only when the workflow demands them. A working RAG system shouldn't
gain agentic complexity unless users need broader actions. Tool calls or
corpus-level operations can justify the extra machinery when the fixed path can't
answer
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Start with the problem, then a small LLM system, with data and evaluation next
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A similar boundary separates RAG and agents. RAG works when the task is simple
question answering over a large search space. Agents become useful when context
changes or planning is dynamic. They also help when data comes from multiple
sources, or when the task needs multiple API integrations
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Use multi-agent systems when one agent's planning and tool use become too broad
to test or reason about as a single role. Memory can create the same pressure.

That decision sits inside normal product engineering. A vertical finance agent
is a full product with a TypeScript UI and FastAPI backend. It uses RAG and
agents alongside AWS infrastructure and data pipelines, with evaluation part of
the same product work
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's AI engineering episode]]).

Durable workflow tools can provide queues and retries for the agentic world
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's AI engineering episode]]).
That keeps multi-agent design close to
[[AI Engineer Role]] work.
Teams still own data and interfaces, tests and traces, permissions, and the
user-facing product.
