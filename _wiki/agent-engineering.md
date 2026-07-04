---
layout: wiki
title: "Agent Engineering"
summary: "DataTalks.Club guests explain agent engineering through workflow design, tools, retrieval, evaluation, guardrails, and production constraints."
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
goal and act inside a workflow. It extends prompt engineering with
orchestration, tool use, retrieval, and memory. It also adds evaluation and
production constraints. The cited examples include on-call assistants, email
assistants, and coding agents. They also include enterprise search assistants,
multi-agent support systems, and workflow automation.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Agent engineering sits next to [[AI Engineering]] and
[[LLM Production Patterns]],
with [[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
[[LLM Evaluation Workflows]], and [[Multi-Agent Systems]] nearby. It's narrower
than AI engineering as a role, but broader than prompt writing. An agent can
select steps, call tools, and keep task state.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

## Workflow Boundary

An agent is an LLM-backed system organized around an objective, not only a
single response. It can use orchestration, tools, memory, and knowledge stores
to choose the next step in a task.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

The boundary with [[retrieval-augmented-generation=>RAG]] matters. Some systems
only retrieve documents by chunking them, embedding them, fetching context, and
generating an answer. Agentic systems add planning and tool calls. Retrieval can
be one step inside a larger task.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Agentic AI Systems]]
Practical LLM projects often start with RAG for quick business value. Teams add
tools and agent behavior when the task needs actions or durable memory.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

## Design Constraints

The shared definition doesn't force one architecture because each setting has a
different first constraint.

Operational agents start from integrations. On-call and SRE examples need logs,
metrics, remediation options, and permissioned tools before an LLM can help
with real incidents.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Teams adopting agents start from a narrow problem. The first version stays
small, with usable data and evaluation. The email assistant example starts with
Gmail API access and RAG. It becomes useful only after the task and data
boundary are clear.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Multi-agent systems start from decomposition. A sequential flow, a manager-agent
orchestration layer, and direct agent collaboration create different debugging
and evaluation problems.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Enterprise teams start from governance. They need specialized models,
guardrails, and data lineage before broad autonomy is safe. Multi-tenant
evaluation, human-label alignment, and deployment risk matter too.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Agent Design

Agent design begins with the task boundary. A useful agent needs a concrete job,
not a vague instruction to "be helpful." Planning can be single-step,
multi-pass, or self-reflective. The system still needs limits on which tools it
can call and when it should stop.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Start with the smallest workflow that solves the task. Use task decomposition so
the agent doesn't become one broad prompt that owns every decision.
Decomposition clarifies the orchestration choice.[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]
Options include sequential pipelines, manager-agent orchestration, and
collaboration.
That distinction matters for [[Software Engineering]] because a linear workflow
is easier to test and debug than an open-ended multi-agent system.

Agents create value when they act on documents, APIs, and workflow state. Chat
alone isn't the point. Teams use embedded agents for Slack-style work and
proactive assistants. Agent design becomes a product workflow question as much
as a model question.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

## Tooling and Integration

Tools are part of the agent's interface with the world, but bad tools create
noisy context and unsafe actions. Good tools expose constrained actions, typed
inputs, traceable outputs, and enforceable permissions.

Prompts, SDKs, and tool wrappers pair with integration abstractions for diverse
tools. Agent marketplaces and MCP-style protocols make tools discoverable and
callable.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
These are [[Tools]] questions, but the agent page keeps the workflow-specific
part. Tools should match the decisions the agent is allowed to make.

The OpenAI Agent SDK and MCP integration appear alongside scratchpads.[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]
Internal reasoning servers appear too.[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]
The agent may need private reasoning state. It may also need task state that
isn't shown directly to the user. Engineers still need enough observability to
debug the system. Hidden state shouldn't replace tests.

Production AI engineering covers a browser extension architecture with a backend
AI integration. It also covers search-focused assistants and tool selection.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
Those examples keep agent engineering close to normal application architecture.
A tool call still needs a backend, authentication, latency control, and failure
handling.

## Retrieval, Memory, and Context

Retrieval is one of the main tools agents use. It gives the system access to
documents, logs, and emails. It can also expose code, tickets, and other
external state. Guests don't treat retrieval as automatic. They discuss
chunking, metadata, wrappers, and failure analysis.

Context engineering is the design of effective LLM inputs. The RAG reality check
is that latency, cost, and noisy context can break a system. Teams often need to
rework retrieval backends, chunking, metadata, and wrappers so retrieved
information fits the agent's job.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

For the broader retrieval architecture, see
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

Chunking strategies include fixed length and sliding windows. Retrieval memory
is distinct from multi-turn conversation memory.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
That distinction is central to agent engineering. A support assistant may need
durable customer facts and ticket history, while a coding agent may need
repository context and task state. A short conversation memory isn't enough for
either system.

RAG and knowledge management connect to the AI engineer skill stack.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]
That link matters because many agent failures are knowledge-system failures. If
teams don't give source documents metadata, ownership, or a refresh cadence, the
agent will act on weak context.

## Evaluation and Testing

Agent evaluation checks whether the system accomplished the goal under realistic
conditions. It can't only compare one final string to a reference answer
because multiple valid tool-call paths may exist.

Agent evaluation uses custom datasets, system benchmarks, and mocked tools.
Teams also use integration tests and regression tests. The focus is goal-based
evaluation and outcome assertions over exact paths.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Those evaluation choices belong with
[[LLM Evaluation Workflows]]
and [[Testing]].

Teams use generator-evaluator loops.[[cite:practical-llm-engineering-and-rag=>RAG Eval]]
They still weigh gold test sets against cost and representativeness. Failure
analysis can change retrieval.
Those evaluation habits are useful before a system becomes agentic, then become
more important when the system starts calling tools.

Enterprise evals cover multi-tenancy and scale.[[cite:s23e03-future-of-ai-agents=>AI Agent Future]]
Human-label alignment matters too.[[cite:s23e03-future-of-ai-agents=>AI Agent Future]]

Arize Phoenix appears as a monitoring tool.[[cite:from-game-ai-to-modern-ai-agents=>Game AI to LLM Agents]]

These practices make evaluation part of daily agent work rather than a one-time
benchmark.

## Production and Governance

Production agents need permission checks, audit logs, lineage records, and
guardrails. They also need monitoring and human review for high-risk actions.
Cost and latency controls matter because tool calls, retrieval, and multi-step
reasoning can multiply runtime.

Legal and healthcare agents put reliability, guardrails, and data lineage close
to Agent MLOps. User feedback loops, infrastructure risks, and deployment risks
belong in the same governance design.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

Security overlaps here too.[[cite:generative-ai-chatbots-in-production-security=>Chatbot Security]]
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

Production AI engineering covers prompt evaluation and cost tradeoffs. Prompt
compression and caching are model-efficiency tools.[[cite:production-ready-ai-engineering=>Production AI]]
These techniques aren't agent-specific. Agents make them more important because
extra steps add tokens, latency, and failure modes.

Generic agent products miss details that live in each task. Teams need specific
integrations, context, datasets, and evaluation.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
An agent should be designed around a real workflow and measured against that
workflow.

## Related Pages

These pages cover the role, retrieval layer, evaluation work, and production
constraints around agent systems.

- [[AI Engineer Role]]
- [[AI Engineering Roadmap]]
- [[LLM Production Patterns]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[retrieval-augmented-generation=>RAG]]
- [[LLM Evaluation Workflows]]
- [[Tools]]
- [[Production]]
- [[Responsible AI and Governance]]
- [[Agent Ops]]
