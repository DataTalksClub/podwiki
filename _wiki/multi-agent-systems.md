---
layout: wiki
title: "Multi-Agent Systems"
summary: "How DataTalks.Club guests discuss multi-agent systems through sequential flows, manager-agent orchestration, peer collaboration, tool use, memory, evaluation, and guardrails."
related:
  - AI Agents
  - Agent Engineering
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Responsible AI and Governance
  - Evolutionary Algorithms
---

Multi-agent systems split an [AI agent]({{ '/wiki/ai-agents/' | relative_url }})
task across more than one specialized agent. DataTalks.Club guests treat that
split as an engineering choice, not as the default structure of agentic
software.
The design question is whether a task needs a sequential handoff or a manager
agent. Some tasks need direct collaboration between agents. In many cases,
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}) with
bounded tools and tests is enough.

The most explicit taxonomy comes from
[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 20:57-31:17, he contrasts sequential agent flows, manager-agent
orchestration, and direct collaboration. Other podcast discussions add the
production boundaries. [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
defines agent tools, memory, and evaluation in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
warns against adding memory or agents before the product needs them in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) frames
production agents through governance and evaluation in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}).

## Coordination Patterns

Lanham describes a sequential flow as an assembly line of agents. One agent
handles requirements, another plans, and another executes. Each agent passes
its output to the next
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
23:48). Teams can review this more easily because work moves through a known
order.

Manager-agent orchestration adds a front-facing agent that calls other agents
as needed. Lanham says the orchestrator looks at outputs and gives feedback.
It also checks whether the work still meets the requirements
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
25:20). Teams use manager-agent orchestration when the user should see one
interaction, but the system needs separate planning and building agents. It may
also need review or repair agents behind it.

Peer collaboration lets agents exchange outputs directly through a shared
message channel. Lanham calls it powerful, but he also warns that it's
expensive and weak for real-time responses
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
26:25-29:05). He reserves it for complex problems where the input and desired
output are clear, but the path between them is detailed. Coding work is the
concrete example in the interview. A designer, front-end developer, and
back-end developer can work in parallel while they share feedback
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
28:46-30:09).

## Flow, Orchestration, and Collaboration

Guests distinguish these designs by looking at how agents communicate.
Sequential flows use handoffs between agents, while orchestration puts routing
and review with a manager agent. Collaboration lets agents share intermediate
outputs with each other.

Lanham teaches agents through minimalism. He recommends breaking the work into
tasks for individual agents. With that split, one large agent doesn't have too
many tools and instructions
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
20:57). That advice matters because a multi-agent system multiplies prompts,
tool calls, state, and possible failure paths. A sequential requirements-plan-
execution flow is often enough before a team adds a manager agent or peer
collaboration.

Manager-agent orchestration becomes useful when the system has to choose
between workflows or retry a failed step. It also helps when the system must
compare output to requirements. Lanham says an orchestration agent can review
the output and choose whether to rerun or continue. It can also switch between
parallel development tasks when needed
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
23:18 and 30:09). This keeps the coordination logic in one place instead of
letting every agent negotiate with every other agent.

Agents in direct collaboration share outputs that become inputs for other
agents. They can then refine a solution together. Lanham compares that style to
[evolutionary algorithms]({{ '/wiki/evolutionary-algorithms/' | relative_url }})
because collaboration can resemble candidate search. In his analogy, agents
first generate candidate outputs and then exchange them for judgment and
improvement
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
27:45 and 29:05). Keep the comparison limited because the episode doesn't
claim that every multi-agent system is an evolutionary algorithm.

## Tools and Shared State

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) gives the
clearest archive definition of an agent's components. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she says modern agents orchestrate calls to LLMs and tools at 12:31. They also
call knowledge stores and memory. Multi-agent systems inherit that same
machinery, then add a coordination layer between agents.

Tool boundaries matter more when several agents can act. Ranjitha's SRE
example has an agentic system move across logs and metrics. It can also reach
source code, Kubernetes, and remediation options
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
22:50-27:33).

She says teams abstract over different observability and deployment tools.
They still need domain knowledge for each source's quirks. In a multi-agent
design, teams define which agent can call which
[tools]({{ '/wiki/tools/' | relative_url }}). They also define what each call
returns to the rest of the system.

Lanham links current multi-agent tooling to the OpenAI Agents SDK and
handoffs. He also discusses guardrails and MCP-style integrations
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
31:31-33:08). He also separates reasoning scratchpads from inter-agent
communication. Agents may use a sequential-thinking server to plan, but they
usually pass results to other agents. They don't expose every reasoning step
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
33:25-34:03).

## Memory and Context

Multi-agent systems need an explicit memory boundary because each agent may see
a different slice of context. Ranjitha says context engineering means choosing
what to send to the LLM. Teams do this instead of stuffing every document, log
line, or metric into the prompt
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
21:21-34:02).

For manager-agent orchestration, the manager often needs requirements and
state. It may also need summaries, while the worker agent needs task-specific
inputs and tool results.

Ranjitha also treats [RAG]({{ '/wiki/rag/' | relative_url }}) as one tool an
agent can choose, not the whole system. She says agents move beyond a fixed
retrieval workflow by deciding when to use search or tables. They can also
choose MongoDB queries and other tools
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
36:11-37:39).

Retrieval can serve a single worker or the manager, and it can also serve a
shared workspace. The team still has to define who may read and write each
piece of state.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) adds a
useful caution in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}):
many systems don't need memory at all. He recommends adding tools or memory
only as needed, and he distinguishes retrieval-based memory from active
conversation memory at 56:21-59:59. In a multi-agent system, that caution
prevents teams from adding a memory agent too early. It also cautions against a
shared scratchpad or long-term profile store before the task requires one.

## Evaluation

Multi-agent evaluation checks whether the system reached the goal and used the
right tools. It also checks whether the agents stayed inside the allowed
workflow. Ranjitha says agent evaluation has to cover the answer and tool
calls. It also has to cover parameters and other behavior, not only a final
response
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
51:17). At 53:20-57:23, she recommends software-style tests.

Those tests mock tools, cover integrations, rerun regressions, and assert
outcomes. Her calendar example evaluates whether the system created the right
invite, not whether it followed one exact path.

Lanham makes the same point from the monitoring side. He says builders should
measure agent performance for consistency and understand variance in outputs.
They should also monitor LLM communication and prompts with tools such as Arize
Phoenix
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
57:39-58:04). In a manager-agent system, traces need to show which agent
acted and which tool it called. They also need to show what the agent passed
on and where a rerun or review happened.

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) extends this to
multi-tenant and regulated settings in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}).
For a multi-agent workflow serving separate customers, he says teams need
customer-specific golden datasets and LLM judges aligned to human labels. They
also need red-team stress testing and human review for critical actions such as
high-value refunds at 43:30-50:18. In multi-agent systems, those requirements
belong with
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}).

## Guardrails and Governance

Multi-agent systems create a governance problem because data and actions can
move through several agents before the user sees an answer. Aditya says
companies need to know what each agent is doing and how user data is processed.
They also need to know where data has gone and what offline workflows touched it
([The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
30:26-36:31). He connects that visibility to retention, data lineage,
auditability, and compliance.

Guardrails also have to sit near the tool boundary. Aditya's refund example
puts high-value Stripe actions behind human review, even when the agent handles
lower-risk cases
([The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
48:11-48:42). In a manager-agent design, the manager can enforce that policy by
routing edge cases to a human queue instead of passing them to another agent.

Human review remains part of production evaluation. Aditya says he wouldn't be
comfortable deploying an agent without human-in-the-loop data. The team needs a
ground truth for the LLM judge and a way to detect drift
([The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
50:18-55:26). That makes multi-agent governance part of
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
rather than a separate prompt-engineering concern.

## Use Cases and Limits

Guests add agents only when the workflow demands them. Hugo says a working RAG
system shouldn't gain agentic complexity unless users need broader actions.
Tool calls or corpus-level operations can also justify the extra machinery when
the fixed path can't answer
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
49:21-51:10). He starts with the problem, then a small LLM system. Data and
evaluation come next
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
53:34-56:53).

Ranjitha draws a similar boundary between RAG and agents. RAG works when the
task is simple question answering over a large search space. Agents become
useful when context changes or planning is dynamic. They also help when data
comes from multiple sources, or when the task needs multiple API integrations
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
37:39-41:18).

Use multi-agent systems when one agent's planning and tool use become too broad
to test or reason about as a single role. Memory can create the same pressure.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts that decision
inside normal product engineering. In
[Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
he describes a vertical finance agent as a full product with a TypeScript UI
and FastAPI backend at 22:29-29:12. The same product uses RAG and agents. He
also includes AWS infrastructure and data pipelines. Evaluation belongs in that
same product work.

At 42:28-46:31, Paul says durable workflow tools can provide queues and retries
for the agentic world.
That framing keeps multi-agent design close to
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) work.
Teams still own data and interfaces. They also own tests and traces.
Permissions and the user-facing product remain part of the same work.
