---
layout: wiki
title: "Agent Engineering"
summary: "Agent engineering across workflow design, tools, retrieval, evaluation, guardrails, and production constraints."
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

An agent is an LLM-backed system organized around an objective rather than only
a single response. It can choose the next step in a task through orchestration
and tool use. It may also use memory or knowledge stores.
This differs from [[reinforcement-learning]], where an agent learns a policy
from rewards inside an environment or simulator.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
[[cite:from-game-ai-to-modern-ai-agents=>Game AI to Agents]]

The boundary with [[retrieval-augmented-generation=>RAG]] matters because
retrieval-only systems stop after they fetch context and generate an answer.
Agentic systems add planning and tool calls. Retrieval can be one step inside a
larger task.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Agentic AI Systems]]

Teams often start with RAG.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
They add tools and agent behavior when the task needs actions or durable
memory.
The [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] turns that
sequence into a production path. Later stages cover RAG rollout, evaluation,
agent behavior, and operations.

Hugo Bowne-Anderson's framing keeps that boundary practical. Start with a
specific problem and try the smallest RAG or LLM workflow that can help. Add
tools only when retrieval can't answer.

Tool calls fit tasks that need an API call or current state. They also fit
tasks that need an action.
[[cite:practical-llm-engineering-and-rag@50:19=>From RAG to Agents]]
Broad questions can also force the boundary. A RAG retriever may find relevant
chunks. A summarization tool or sub-agent can still be better for a whole
document, inbox, or course.

That extra power comes with more tool descriptions, tests, and traces.

## Choose the Smallest Action Boundary

Agent design becomes safer when the team chooses the least autonomous workflow
that can meet the goal, then expands it only after the evidence supports the
next action. A useful decision sequence is:

1. Name the user outcome and test whether retrieval or a deterministic workflow
   is enough. Add a tool when the task needs current state or an external action;
   add an agent when the next step genuinely depends on dynamic planning. The
   RAG-to-agent discussion makes this an explicit boundary rather than a default
   escalation to autonomy.[[cite:practical-llm-engineering-and-rag@50:19=>From RAG to Agents]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@37:39=>RAG or Agents]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@40:17=>Agent Use Cases]]
2. Write an action matrix before exposing tools. For each tool, record the
   allowed inputs, data scope, side effect, permission, timeout, and reversal or
   human approval path. A personal assistant that can inspect or change a
   machine belongs in an isolated environment with deliberately limited access,
   not an unrestricted shell.[[cite:s24e09-engineering-your-own-ai-assistant@16:31=>Sandboxed Assistant Actions]][[cite:s24e09-engineering-your-own-ai-assistant@21:40=>Permission Boundaries]]
3. Start with a sequential or single-agent flow when it is sufficient. Add
   manager-agent or peer collaboration only when the workflow needs it and the
   additional state can be traced. The coordination choice changes how easily
   engineers can review and debug the system.[[cite:from-game-ai-to-modern-ai-agents@37:39=>Agent Coordination]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@12:31=>Agent Orchestration]]
4. Define escalation triggers before production. Route missing context,
   low-confidence or conflicting results, sensitive requests, and irreversible
   writes or messages to a human. Chatbot security work treats human approval as
   a control for hallucinations, unsafe commitments, and legal or trust risk;
   agent governance extends the same boundary to tool actions.[[cite:generative-ai-chatbots-in-production-security@25:34=>Human Review for Chatbots]][[cite:s23e03-future-of-ai-agents@43:30=>Agent Reliability]][[cite:s24e04-from-genai-pilots-to-production@43:00=>Human Escalation]]
5. Test the action boundary with mocked tools, integration tests, regression
   cases, and goal-based assertions. Verify the outcome and the trace rather
   than requiring one exact tool-call path. Promote a new permission only when
   the test set covers both success and refusal or escalation.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@51:17=>Agent Evaluation Strategy]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@53:20=>Mocked Tool Tests]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@56:02=>Goal-Based Agent Evaluation]]

The output is an action matrix, a permission and escalation runbook, a mocked
tool test set, and traces that connect an action to its retrieved context and
approver. If the team cannot observe the tool call, reproduce the failure, or
name who takes over, keep the workflow retrieval-only or human-assisted while
the missing control is built.

## Design Constraints

The shared definition doesn't force one architecture because each setting has a
different first constraint.

Operational agents start from integrations. An on-call agent needs logs and
metrics before it can help with real incidents. It also needs permissioned tools
and remediation options.

Ranjitha Kulkarni grounds this in Noird.ai's on-call work. The agents reason
over logs and metrics before suggesting or taking remediation steps.

[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@07:44=>Agentic AI]]
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@22:50=>SRE agents]]

The engineering challenge is making the agent behave like a constrained
operator inside the incident workflow, not like a general chatbot with log
access.

Teams adopting agents start from a narrow problem and keep the first version
small enough to evaluate.

The email assistant starts with Gmail API access and RAG. The team chooses that
boundary.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Use [[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
for the personal productivity version of that boundary.

[[person:pauliusztin=>Paul Iusztin]] and [[person:alexeygrigorev=>Alexey Grigorev]] highlight the same constraint from a personal-assistant
workflow: a tool that can inspect a machine or change system state should run
only inside an isolated environment with deliberately limited access. A narrow,
reviewable action can be useful for a concrete incident; an always-on assistant
with unrestricted access is a different risk profile. The anecdotal server
example does not establish production readiness for any named tool.[[cite:s24e09-engineering-your-own-ai-assistant@16:31=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@21:29=>Engineering Your Own AI Assistant]]

His four-step agent frame names the constraint. Define the problem, start small,
make the data available, and decide how the team will evaluate the result.
Without those four pieces, an agent can look impressive in chat while
remaining hard to test or improve.
[[cite:practical-llm-engineering-and-rag@56:21=>Four-Step Agent Framework]]
The same four pieces give
[[ai-engineering-portfolio-projects=>AI Engineering Portfolios]] concrete
evidence for agent projects.

Coordination style affects debugging, so teams decompose agents.
Sequential flows are easier to review than manager-agent orchestration or
direct collaboration.
Lanham's game-AI lineage behind that taxonomy is covered in
[[game-ai-to-llm-agents=>Game AI to LLM Agents]].[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]

Enterprise teams start from governance. They need specialized models,
guardrails, and data lineage before broad autonomy is safe. Multi-tenant
evaluation, human-label alignment, and deployment risk matter too.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Agent Design

Agent design starts with the task boundary. A useful agent needs a concrete job,
not a vague instruction to "be helpful." Planning can be single-step,
multi-pass, or self-reflective, so the system still needs limits on which tools
it can call and when it should stop.
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@15:10=>Agent planning]]
As the plan becomes dynamic, evaluation has to cover both final outcomes and
tool-use behavior.

The implementation choice also changes the failure mode. Code agents can expose
tool use and state through executable programs, while natural-language agents
can be easier to prompt but harder to constrain and debug. That tradeoff links
agent design to [[Software Engineering]], [[Testing]], and
[[ai-coding-tools=>AI coding tools]]
as much as to prompt writing.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@19:58=>Code and language agents]]

Start with the smallest workflow that solves the task. Use task decomposition so
the agent doesn't become one broad prompt that owns every decision.
Decomposition clarifies the orchestration choice.[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]
Options include sequential pipelines, manager-agent orchestration, and
collaboration.
For the narrower search family behind fitness functions, mutation, and
candidate selection, use [[evolutionary-algorithms=>Evolutionary Algorithms]].
That distinction matters for [[Software Engineering]] because a linear workflow
is easier to test and debug than an open-ended multi-agent system.

Agents create value when they act on documents, APIs, and workflow state. Chat
alone isn't the point. Teams use embedded agents for Slack-style work and
proactive assistants. Agent design becomes a product workflow question as much
as a model question.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

The email-assistant example shows the same product boundary. A Gmail API plus
RAG can answer and act on messages only after the team chooses the inbox state.
The team also has to choose the retrieved knowledge and user permissions the
assistant may use.
[[cite:practical-llm-engineering-and-rag@53:34=>Email Assistant with Gmail API and RAG]]

## Tooling and Integration

Tools are part of the agent's interface with the world, but bad tools create
noisy context and unsafe actions. Good tools expose constrained actions, typed
inputs, traceable outputs, and enforceable permissions.

Prompts, SDKs, and tool wrappers pair with integration abstractions for diverse
tools, which puts agent tooling inside the broader
[[llm-tools=>LLM Tools for Real Products]] stack. Agent marketplaces and
MCP-style protocols make tools discoverable and callable.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
These are [[Tools]] questions, but the agent page keeps the workflow-specific
part. Tools should match the decisions the agent is allowed to make.

The [[game-ai-to-llm-agents=>Game AI to LLM Agents]] discussion places the
OpenAI Agent SDK and MCP integration alongside scratchpads.
It also mentions internal reasoning servers.[[cite:from-game-ai-to-modern-ai-agents=>Game AI]]
The agent may need private reasoning state. It may also need task state that
isn't shown directly to the user. Engineers still need enough observability to
debug the system. Hidden state shouldn't replace tests.

Production AI engineering covers a browser extension architecture with a backend
AI integration. It also covers search-focused assistants and tool selection.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
Those examples keep agent engineering close to normal application architecture.
A tool call still needs a backend, authentication, latency control, and failure
handling.

Iusztin places agents inside a broader full-stack AI engineer role. The agent
is one system piece beside frontend, backend, databases, and RAG. Deployment
and LLMOps sit in the same product path. That keeps agent work grounded in
product ownership instead of a standalone demo.
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@22:29=>AI Engineering Skill Stack]]

## Retrieval, Memory, and Context

Retrieval is one of the main tools agents use. It gives the system access to
documents, logs, and emails. It can also expose code, tickets, and other
external state. Guests don't treat retrieval as automatic. They discuss
chunking, metadata, wrappers, and failure analysis.

[[context-engineering=>Context engineering]] is the design of effective LLM
inputs. The RAG reality check is that latency, cost, and noisy context can break
a system. Teams often need to rework retrieval backends, chunking, metadata, and
wrappers so retrieved information fits the agent's job.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

For the broader retrieval architecture, see
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

Chunking strategies include fixed length and sliding windows. Retrieval memory
is distinct from multi-turn conversation memory.[[cite:practical-llm-engineering-and-rag@57:41=>Agent Memory Design]]
That distinction is central to agent engineering. A support assistant may need
durable customer facts and ticket history, while a coding agent may need
repository context and task state. A short conversation memory isn't enough for
either system.

The first memory question is whether the workflow needs memory at all. If the
agent only answers one request from supplied context, memory may add risk
without adding value. If the agent has to remember preferences, prior decisions,
or long-running task state, treat memory as a designed data source with its own
evaluation cases.

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
[[Agent Ops]]. The serving and release-ownership side of that work belongs with
[[llm-deployment=>LLM Deployment]].

Production AI engineering covers prompt evaluation and cost tradeoffs. Prompt
compression and caching are model-efficiency tools.[[cite:production-ready-ai-engineering=>Production AI]]
These techniques aren't agent-specific. Agents make them more important because
extra steps add tokens, latency, and failure modes.

Generic agent products miss details that live in each task. Teams need specific
integrations, context, datasets, and evaluation.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
An agent should be designed around a real workflow and measured against that
workflow.

## Related Pages

Agent engineering connects these production and workflow pages.

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
