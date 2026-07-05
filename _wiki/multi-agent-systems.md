---
layout: wiki
title: "Multi-Agent Systems"
summary: "Multi-agent systems through coordination patterns, tool boundaries, memory, evaluation, and governance."
related:
  - Agent Engineering
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Responsible AI and Governance
  - Evolutionary Algorithms
---

Teams use multi-agent systems when one [[agent-engineering=>AI agent]] role is
too broad to test or reason about. Splitting the task is an engineering choice,
not the default structure for agentic software. A task may need a sequential
handoff, a manager-agent layer, or direct collaboration between agents. In many
cases, [[agent-engineering=>agent engineering]] with bounded tools and tests is
enough.

The clearest podcast taxonomy starts with sequential agent flows, then adds
manager-agent orchestration and direct collaboration. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
[[game-ai-to-llm-agents=>Game AI to LLM Agents]] follows that taxonomy back to
game-AI ideas about state, actions, feedback, and constrained environments. That
lineage overlaps with [[reinforcement-learning]] when agents learn policies
from rewards. In this page's examples, LLM multi-agent systems coordinate tools
and roles without training a policy through trial and error.

Production boundaries come from the same concerns as other
[[llm-production-patterns=>LLM production patterns]]. Teams still need tool
permissions and memory boundaries. They also need evaluation, observability,
and governance. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Agent Boundaries

A multi-agent system coordinates LLM-backed roles around one task. The
coordination boundary between roles matters more than the number of prompts in
a chain.

Sequential flows put requirements, planning, execution, and review in a known
order. Manager-agent orchestration adds a
front-facing agent that routes work, checks outputs, and asks worker agents to
revise or continue. Peer collaboration lets agents exchange intermediate
outputs through a shared message channel. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Use this topic for the point where one agent splits into coordinated roles. It
isn't a general replacement for [[retrieval-augmented-generation=>RAG]],
[[llm-evaluation-workflows=>LLM evaluation]], or [[agent-ops=>Agent Ops]].

## Design Tradeoffs

Teams differ on where to add agency. A minimalist design keeps tasks small and
narrows each agent's instructions and tools. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
A product-first design adds tools or memory only after a fixed RAG path falls
short. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

The production view puts more weight on testability and governance. Agentic
systems need outcome-based tests, traces, and tool-call checks. High-risk paths
also need human review. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Enterprise agent discussions add data lineage and guardrails. They also add
customer-specific evaluation data and LLM judges aligned to human
labels. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Coordination Patterns

Sequential flows are the easiest multi-agent design to review. Each agent
receives a bounded input, produces an output, and gives it to the next role.
Teams can review the sequence because work moves through a known order. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Manager-agent orchestration fits tasks where one interface should hide several
specialized workers. The manager routes the request and reviews results. It can
retry a failed step and check requirements. It can also switch between parallel
development tasks when needed. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
This keeps routing and review in one place instead of asking every agent to
negotiate with every other agent.

Peer collaboration lets agents exchange outputs directly. It helps when the
input and target output are clear but the path between them is detailed. In a
coding workflow, a design agent and engineering agents can share feedback while
they refine the same product. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
The tradeoff is cost and latency, so direct collaboration is a poor fit for many
real-time responses.

Collaborating agents can resemble [[evolutionary-algorithms=>evolutionary algorithms]]
when they generate candidate outputs, exchange feedback, and improve a result.
The comparison is limited. A multi-agent system isn't automatically an
evolutionary algorithm. Many useful designs are simple handoff flows. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Tools and Shared State

Modern agents orchestrate LLM calls, tools, knowledge stores, and memory. A
multi-agent system inherits that machinery and adds a coordination layer between
roles. Planning may be single-step, multi-pass, or self-reflective before a
team splits the work into several roles. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@15:10=>Building Agentic AI Systems]]

Tool boundaries matter when several agents can act. In SRE, an agentic system
may use observability data and source code. It may also use Kubernetes and
remediation options. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@22:50=>Building Agentic AI Systems]]

Teams can abstract over observability and deployment tools, but each source
still has quirks. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

In a multi-agent design, teams decide which agent may call which tool and what
each tool result exposes to the rest of the system.

Current agent tooling includes SDK handoffs, guardrails, and MCP-style
integrations. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
Reasoning scratchpads are separate from inter-agent communication. An agent may
use a planning server internally. It normally passes task results to other
agents rather than exposing every reasoning step. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Memory and Context

Multi-agent systems need explicit memory boundaries because each role may see a
different slice of context. Context engineering means choosing what to send to
the LLM, not stuffing every document, log line, or metric into the prompt. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Manager-agent orchestration often gives the manager requirements, state, and
summaries. Worker agents usually need task-specific inputs and tool results.
That split should be deliberate because retrieval can serve a worker, the
manager, or a shared workspace.

[[retrieval-augmented-generation=>RAG]] is one tool an agent can use, not the
whole system. Agents move beyond a fixed retrieval workflow when they pick
between search, tables, database queries, or other tools. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Many systems don't need memory, so teams should add tools or memory only when
the product needs them. Retrieval memory differs from conversation memory. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

That caution keeps a memory agent, shared scratchpad, or long-term profile store
out of the design until the task requires one.

## Evaluation and Traces

Multi-agent evaluation checks goal completion and role handoffs, plus tool
choice and workflow boundaries. Agent evaluation covers answers and tool calls.
It also covers parameters and other behavior, not only a final response. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Software-style tests apply here. Teams mock tools, cover integrations, rerun
regressions, and assert outcomes.

Outcome assertions matter because several valid paths can produce the same
correct result. A calendar-agent test should check whether the system created
the right invite rather than forcing one exact trace. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Monitoring uses traces to measure agent consistency and output variance. Teams
also track LLM communication with tools such as Arize Phoenix. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Manager-agent traces need to show the acting agent and tool call. They also
need to show the handoff, review, and rerun points.

Sensitive settings need customer-specific golden datasets and LLM judges aligned
to human labels. They also need red-team stress tests. Critical actions such as
high-value refunds need human review. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]
Those requirements connect multi-agent work to
[[llm-evaluation-workflows=>LLM Evaluation Workflows]] and
[[ai-red-teaming=>AI Red Teaming]].

## Guardrails and Governance

Multi-agent systems create a governance problem because data and actions can
move through several roles before the user sees an answer. Companies need to
know what each agent did and how user data was processed. They also need to
track where data went and which offline workflows touched it. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]
That visibility connects to retention, data lineage, auditability, and
compliance.

Guardrails should sit near the tool boundary. A refund workflow can keep
high-value Stripe actions behind human review. The agent can still handle
lower-risk cases. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]
In a manager-agent design, the manager can enforce that policy. It routes edge
cases to a human queue instead of passing them to another agent.

Human review remains part of evaluation because the team needs ground truth for
the LLM judge. The team also needs a drift signal. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]
That makes multi-agent governance part of
[[responsible-ai-and-governance=>Responsible AI and Governance]], not a separate
prompt-engineering concern.

## Use Cases and Limits

Add agents only when the workflow demands them. A working RAG system shouldn't
gain agentic complexity unless users need broader actions. Tool calls or
corpus-level operations can justify the extra machinery. The fixed path has to
fall short first. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Start with the problem, then a small LLM system, then data and evaluation. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

The same boundary separates RAG and agents. RAG works for simple question
answering over a large search space. Agents become useful when context changes
or planning is dynamic. They also help when data comes from multiple sources or
the task needs several API integrations. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Use a multi-agent system when one agent's planning and tool use become too
broad to test or reason about as a single role. Memory can create the same
pressure, but memory alone isn't a reason to add another agent.

That decision still sits inside product engineering. A vertical finance agent
can be a full product with a TypeScript UI and FastAPI backend. It may also use
RAG plus agents. Infrastructure and data pipelines stay in the product.
Evaluation stays there too. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

Durable workflow tools can provide queues and retries for the agentic world. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]
That keeps multi-agent design close to [[ai-engineer-role=>AI Engineer Role]]
work. Teams still own data and interfaces. They also own tests, traces,
permissions, and the user-facing product.

## Related Pages

These pages cover the adjacent agent, evaluation, governance, and algorithm
topics:

- [[agent-engineering=>Agent Engineering]]
- [[llm-production-patterns=>LLM Production Patterns]]
- [[llm-evaluation-workflows=>LLM Evaluation Workflows]]
- [[responsible-ai-and-governance=>Responsible AI and Governance]]
- [[evolutionary-algorithms=>Evolutionary Algorithms]]
