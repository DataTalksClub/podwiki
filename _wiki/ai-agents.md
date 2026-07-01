---
layout: wiki
title: "AI Agents"
summary: "What DataTalks.Club guests have said about AI agents: autonomy, tool use, memory, RAG boundaries, evaluation, governance, and infrastructure."
related:
  - Agent Engineering
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - AI Red Teaming
  - Multi-Agent Systems
  - LLM Evaluation Workflows
  - Responsible AI and Governance
  - Tools
---

AI agents are LLM-backed systems that pursue a goal over time. They often use
tools, retrieval, memory, and workflow state. In DataTalks.Club podcast
discussions, guests treat agents as more than chat interfaces.
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) ties
them to autonomy, objectives, orchestration, and tool use. She also adds memory
and knowledge stores in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
at 11:00 and 12:31.

For agent-specific reading, focus on agent planning and tool calls. Then
compare memory, the
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
boundary, evaluation, and governance. The implementation discipline around
these systems lives in
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}). The
broader production practices live in
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

## Core Podcast Threads

The agent discussions in the podcast cluster around six recurring threads:

- [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}) with [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) for autonomy, orchestration, tools, memory, and SRE workflows. The same episode covers agentic RAG, MCP-style tool protocols, and goal-based evaluation.
- [The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}) with [Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) for enterprise adoption, specialized models, guardrails, and data lineage. He also covers multi-tenant evaluation, human-label alignment, and deployment risk.
- [From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}) with [Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) for the lineage from game AI and multi-agent systems to LLM agents. He also covers task decomposition, orchestration designs, SDKs, MCP integration, coding agents, and monitoring.
- [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}) with [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) for generator-evaluator loops, embedded workflow assistants, and RAG-to-agent progression. His examples include email assistants, agent memory, and small-start evaluation.
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}) with [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) for agents inside the wider AI engineering skill stack.
- [Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}) with [Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) for security risks that become sharper when an LLM can retrieve data or take actions.

The supporting pieces appear throughout the article and connect agents to these
neighboring topics:

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) and [RAG]({{ '/wiki/rag/' | relative_url }}) for search-backed grounding.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for tests, judges, and failure analysis.
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) for adversarial testing and security.
- [Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) for manager agents and collaboration.
- [Tools]({{ '/wiki/tools/' | relative_url }}) for action interfaces.
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}) for controls.

## Agentic System Boundaries

Across the agent-focused episodes, guests describe an AI agent as an LLM system
that can plan or route the next step in a task. It can also use tools and
update workflow state. Ranjitha makes the definition explicit at 11:00 and
12:31 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}):
the agent has an objective and some autonomy. It also has an orchestration
layer and access to tools, memory, or knowledge stores.

That definition separates an agent from a plain chatbot. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
Hugo moves from prompting and retrieval toward embedded assistants. At 33:14 he
discusses Slack-style workflow assistants, and at 40:12 he describes agentic
value through actions, documents, and automation. The agent matters when the
system changes a workflow, not only when it writes a response.

These episodes also treat agents as an extension of normal product engineering.
In
[Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
Paul places agents beside RAG and knowledge management. He also connects them
to LLMOps and shipped AI products. That puts agents close to the
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) and the
[AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }}),
not in a separate research-only category.

## Production, Adoption, Design, and Governance Lenses

Guests agree on tools and context. They also agree on evaluation and
guardrails, but they start from different failure modes.

Ranjitha starts from production workflows. Her on-call automation example at
7:44 and SRE workflow section at 22:50 show agents reading logs and metrics,
then helping with remediation. At 24:59 she emphasizes integration
abstractions, because the agent can't act unless tools expose the right
interfaces.

Hugo starts from adoption and evaluation. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
he recommends starting with the problem and a small workflow at 56:21. Teams
then add data and evaluation. His email assistant example at 53:34 uses Gmail
API access plus RAG to show how teams can grow from retrieval into actions.

Micheal starts from agent design history. In
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
he ties modern LLM agents to game AI and reinforcement learning. He also links
them to multi-agent systems and workflow design. His 20:57 section favors
minimalism and task decomposition, while 23:48 contrasts sequential flows with
manager-agent orchestration. That emphasis connects AI agents to
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) and
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}).

Aditya starts from enterprise reliability. In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
he discusses legal and healthcare reliability at 13:13. He covers specialized
models and agent governance at 19:16, guardrails and lineage at 30:26, and
deployment risks at 56:40. His view connects agents to
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
and [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}).

## Autonomy and Workflow Action

An agent needs a bounded objective and a way to stop. Ranjitha's 15:10 section
compares single-step, multi-pass, and self-reflection planning. Those planning
styles only help when the system has a concrete task. Examples include
triaging an incident, retrieving enterprise knowledge, scheduling work, and
calling an API. Her 40:30 calendar and meeting assistant example shows the
agent changing plans as workflow state changes.

Hugo's examples draw the same boundary from the product side. At 31:56 he
discusses developer assistants such as Copilot, Cursor, and IDE agents. At
33:14 and 40:12 he moves to embedded assistants that work in Slack, documents,
and automation flows. The agent uses context and tools because the task spans
more than one prompt and acts over a real work surface.

Micheal's 20:57 and 23:48 sections add a design constraint: start with the
smallest flow that works. A sequential pipeline is easier to look at than a
manager-agent system. A manager agent or parallel agent collaboration only
makes sense when the task naturally splits across roles, tools, or state, as he
discusses at 26:25.

## Tools, Interfaces, and Agent Infrastructure

Tools turn an agent from a text generator into a system that can act, but they
also create the main operational risk. Ranjitha discusses prompts, SDKs, and
tool wrappers at 18:23. At 24:59 she shows why teams need integration
abstractions for operational systems. Examples include logs, metrics, tickets,
and calendars. The agent can only pick a useful next step when each tool has a
clear action, schema, permission boundary, and observable result.

Both Ranjitha and Micheal discuss newer infrastructure for exposing tools.
Ranjitha covers framework choices at 44:08 in her
[agentic AI episode]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 46:00 she discusses LangChain, the OpenAI Agents SDK, and small agents. At
48:00 she turns to agent
marketplaces and MCP-style protocols.

Micheal discusses OpenAI Agent SDK and MCP integration at 31:31 in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 33:25 he covers sequential thinking servers and scratchpads.

Those discussions connect this topic to
[Tools]({{ '/wiki/tools/' | relative_url }}) and
[LLM Tools]({{ '/guides/llm-tools/' | relative_url }}). A tool's existence
isn't enough. Teams also need to know whether the tool is safe for the agent to
call without human review. They need traceable results and a known workflow
state after a failed call.

## Memory, Context, and RAG Boundaries

Agents often use retrieval, but RAG and agents aren't the same thing.
Ranjitha's 29:30 section gives a RAG reality check around latency, cost, and
bad context. At 31:38 and 32:48 she discusses reworking retrieval backends,
chunking, metadata, and wrappers so the model receives usable context. At
36:11 she frames retrieval as a tool inside an agent. At 37:39 she separates
cases where RAG is enough from cases that need agent behavior.

Hugo makes the same progression in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 44:26 he starts with quick RAG wins through chunking and embeddings. At
48:20 he compares chunking strategies and context rot. At 50:19 he discusses
when teams should add tooling and tool calls. At 57:41 he distinguishes
retrieval-based memory from multi-turn conversation memory.

That distinction matters for
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [RAG]({{ '/wiki/rag/' | relative_url }}). A support agent may need customer
history, policy documents, ticket state, and previous actions. A coding agent
may need repository structure, open files, test results, and task history. A
short chat window can't substitute for a designed memory and retrieval layer.

## Evaluation and Feedback Loops

Agent evaluation asks whether the system completed the task under realistic
conditions, not whether one final sentence matches a reference answer.
Ranjitha's 51:17 section recommends custom datasets and system benchmarks. At
53:20 she discusses mocked tools, integration tests, and regression tests. At
56:02 she emphasizes goal-based evaluation and outcome assertions rather than
exact path matching.

Hugo gives a practical evaluation path before and after agents enter the
workflow. His generator-evaluator section at 13:56 shows automated quality
control. At 23:00 he covers gold test sets, cost, and representativeness. At
26:43 he uses failure analysis to decide whether a retrieval component needs
repair. Teams keep those habits for agents because each tool call can introduce
a new failure mode.

Aditya extends evaluation to enterprise scale through evals for multi-tenancy
and scale at 43:30. At 50:18 he covers aligning LLM judges with human labels.
Micheal adds monitoring tools such as Arize Phoenix at 57:39.

In practice, teams collect failures and label what went wrong. They update
tools or context, then rerun regression tests. See
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for the broader evaluation vocabulary.

## Governance, Guardrails, and Security

Agents need stronger controls than one-shot generation because they can combine
retrieval with actions. Aditya gives the strongest governance discussion. He
discusses reliability in legal and healthcare at 13:13, specialized models and
governance at 19:16, and guardrails and data lineage at 30:26. He then covers
user feedback at 36:55 and deployment risks at 56:40.

Those controls overlap with security work from
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 13:20 in that episode,
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) discusses
prompt overload and knowledge-base retrieval attacks.
For agents, the same retrieval risk can become an action risk. That matters
when the system can call tools, write data, send messages, or trigger
workflows.

Across these discussions, teams keep agents governed by narrowing tool permissions
and tracing the data used for each answer or action. They also keep human
review around high-impact decisions and test failures repeatedly. Practical
agent work therefore draws on
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}),
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}).

## Adjacent Agent Topics

Agent work usually crosses these neighboring topics:

- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) for implementation practice around tool design, retrieval, tests, and deployment.
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}) for model choice, serving, cost, latency, guardrails, and production constraints.
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) and [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}) for grounding and knowledge-update choices before adding agent behavior.
- [Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) for manager agents, parallel collaboration, and older multi-agent design ideas.
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) for testing prompt injection, retrieval abuse, and action risks.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for gold sets, evaluator loops, traces, and regression checks.
