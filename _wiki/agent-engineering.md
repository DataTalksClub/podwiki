---
layout: wiki
title: "Agent Engineering"
summary: "How DataTalks.Club guests define AI agents and engineer them through workflow design, tools, retrieval, evaluation, guardrails, and production constraints."
related:
  - AI Engineer Role
  - AI Engineering Roadmap
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Search, RAG, and Knowledge Systems
  - Tools
---

Agent engineering is the practice of building AI systems that can pursue a goal
and act inside a workflow. These systems may use tools, retrieve information,
and keep task state. In the DataTalks.Club archive, agents aren't only
chatbots. Guests discuss on-call assistants, email assistants, and coding
agents. They also discuss enterprise search assistants, multi-agent support
systems, and workflow automation.

The clearest definition comes from
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 11:00, she frames an agent around autonomy and objectives. She also connects
the definition to LLM reasoning. At 12:31, she adds orchestration and tool use.
She also adds memory and knowledge stores.

That puts agent engineering next to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

## Common Definition

Across the archive, an agent is an LLM-backed system that can decide the next
step in a task rather than only return one answer. It may call APIs or run
search. It may also look at logs, draft code, update a document, or route work
to another component.

Beyond prompts, engineers define task decomposition, tool interfaces, and
retrieved context. They also define permissions, evaluation, observability, and
fallback behavior.

The archive also keeps a strong boundary between
[RAG]({{ '/wiki/rag/' | relative_url }}) and agents. In Ranjitha's episode, the
37:39 section separates cases where retrieval is enough from cases that need an
agent. At 36:11, she describes retrieval as a tool the agent can call.

In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
makes the same progression. His 44:26 section starts with chunking and
embeddings for quick RAG wins. At 50:19, he discusses when teams should add
tool calls and agent behavior.

This definition connects agent engineering to the
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}). In
[Paul Iusztin's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) places agents
inside a broader AI product stack. His 22:29 chapter covers the full-stack AI
engineer skill set. His 29:12 chapter emphasizes RAG and knowledge management.
The 42:28 chapter moves from techniques to shipping AI products.

## Guest Differences

Guests agree that agents need tool use, context, and evaluation, but they differ
on where to start.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) starts
from production workflows. Her
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
episode uses on-call automation and SRE workflows as examples. The 22:50
section covers logs, metrics, and remediation. The 24:59 section shows that
agents need usable integrations before they can help with operational work.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) starts
from practical adoption. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
his 56:21 framework begins with the problem, starts small, then adds data and
evaluation. His 53:34 email assistant example shows a concrete path from Gmail
API access and RAG to a useful assistant.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) starts from
workflow design and multi-agent history. In
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
the 20:57 section emphasizes minimalism and task decomposition. At 23:48, he
compares sequential flows with manager-agent orchestration. At 31:31, he brings
in OpenAI Agent SDK and MCP integration.

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) starts from
enterprise risk. In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
the 19:16 section connects specialized models with agent governance. At 30:26,
he discusses guardrails and data lineage. At 43:30 and 50:18, he connects
evaluation to multi-tenancy, scale, and alignment with human labels.

## Agent Design

Agent design begins with the task boundary. A useful agent needs a concrete job,
not a vague instruction to "be helpful." Ranjitha's 15:10 section compares
single-step, multi-pass, and self-reflection planning. A planning agent also
needs limits on how long it can plan. It needs limits on which tools it can call
and when it should stop.

Micheal's episode adds a practical design warning: start with the smallest
workflow that solves the task. The 20:57 section favors minimalism and task
decomposition. The 23:48 section distinguishes a sequential pipeline from
manager-agent orchestration. That distinction matters for
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
because a linear workflow is easier to test and debug than an open-ended
multi-agent system.

Hugo's 40:12 section gives the product reason to use agents. Value appears when
the system acts on documents, APIs, and workflow state, not only when it chats.
The same episode's 33:14 section discusses embedded agents in Slack-style
workflows and proactive assistants. That makes agent design a product workflow
question as much as a model question.

## Tooling and Integration

Tools are part of the agent's interface with the world, but bad tools create
noisy context and unsafe actions. Good tools expose constrained actions, typed
inputs, traceable outputs, and enforceable permissions.

Ranjitha's 18:23 section covers prompts, SDKs, and tool wrappers, while the
24:59 section discusses integration abstractions for diverse tools. At 48:00, she connects
agent marketplaces and MCP-style protocols to the problem of making tools
discoverable and callable. These are [Tools]({{ '/wiki/tools/' | relative_url }})
questions, but the agent page keeps the workflow-specific part. Tools should
match the decisions the agent is allowed to make.

Micheal's 31:31 section also references OpenAI Agent SDK and MCP integration.
His 33:25 discussion of scratchpads and internal reasoning servers shows a
separate integration layer. The agent may need private reasoning state or task
state that isn't shown directly to the user. That state should be observable
enough for debugging, but it shouldn't replace tests.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) adds a
production AI view in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 41:04, he walks through a browser extension architecture with a backend AI
integration. At 47:19, he discusses search-focused assistants and tool
selection. Those examples keep agent engineering close to normal application
architecture. A tool call still needs a backend, authentication, latency
control, and failure handling.

## Retrieval, Memory, and Context

Retrieval is one of the main tools agents use. It gives the system access to
documents, logs, and emails. It can also expose code, tickets, and other
external state. The archive doesn't treat retrieval as automatic. Guests discuss
chunking, metadata, wrappers, and failure analysis.

Ranjitha's 21:21 section names context engineering as the design of effective
LLM inputs. At 29:30, she gives the RAG reality check. Latency, cost, and noisy
context can break a system. At 31:38 and 32:48, she discusses reworking
retrieval backends. She also covers chunking, metadata, and wrappers so
retrieved information fits the agent's job.

For the broader retrieval architecture, see
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).

Hugo's 48:20 section compares chunking strategies, including fixed length and
sliding windows. His 57:41 section distinguishes retrieval-based memory from
multi-turn conversation memory. That distinction is central to agent
engineering. A support assistant may need durable customer facts and ticket
history, while a coding agent may need repository context and task state. A
short conversation memory isn't enough for either system.

Paul's 29:12 chapter connects RAG and knowledge management to the AI engineer
skill stack. That link matters because many agent failures are knowledge-system
failures. If the source documents lack metadata, ownership, or a refresh
process, the agent will act on weak context.

## Evaluation and Testing

Agent evaluation checks whether the system accomplished the goal under realistic
conditions. It can't only compare one final string to a reference answer
because multiple valid tool-call paths may exist.

Ranjitha's 51:17 section recommends custom datasets and system benchmarks. At
53:20, she discusses mocked tools, integration tests, and regression tests. At
56:02, she emphasizes goal-based evaluation and outcome assertions over exact
paths. That framing connects directly to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [Testing]({{ '/wiki/testing/' | relative_url }}).

Hugo's 13:56 section introduces a generator-evaluator loop for automated
quality control. At 23:00, he discusses gold test sets, cost, and
representativeness. At 26:43, he uses failure analysis to decide whether
retrieval needs to change. Those evaluation habits are useful before a system
becomes agentic, then become more important when the system starts calling
tools.

Aditya's episode adds the enterprise version through evals for multi-tenancy
and scale at 43:30. At 50:18, he covers aligning LLM judges with human labels.
Micheal's 57:39 section adds evaluation and monitoring tools such as Arize
Phoenix. Together, these episodes make evaluation part of daily agent work
rather than a one-time benchmark.

## Production and Governance

Production agents need permission checks, audit logs, lineage records, and
guardrails. They also need monitoring and human review for high-risk actions.
Cost and latency controls matter because tool calls, retrieval, and multi-step
reasoning can multiply runtime.

Aditya's
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
episode is the strongest governance source. The 13:13 section covers reliability
in legal and healthcare settings. The 30:26 section links guardrails and data
lineage to Agent MLOps. At 36:55, he discusses user feedback loops. At 56:40,
he names infrastructure and deployment risks.

These discussions connect agent engineering to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
and [Production]({{ '/wiki/production/' | relative_url }}).

Bartosz's production AI episode adds cost and performance mechanics through
prompt evaluation and cost tradeoffs at 28:16. At 30:00 and 31:45, he connects
prompt compression and caching to model efficiency. These techniques aren't
agent-specific, but agents make them more important because every extra step can
add tokens, latency, and failure modes.

Generic agent products miss details that live in each task. Ranjitha's 58:11
section says teams need specific integrations, context, datasets, and
evaluation. An agent should be designed around a real workflow and measured
against that workflow.

## Related Pages

These pages cover the role, retrieval layer, evaluation work, and production
constraints around agent systems.

- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
- [AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG]({{ '/wiki/rag/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Tools]({{ '/wiki/tools/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
