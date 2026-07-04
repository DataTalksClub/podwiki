---
layout: wiki
title: "Agent Ops"
summary: "AgentOps: orchestration, guardrails, data lineage, deployment risks, and monitoring for AI agents in production."
related:
  - Agent Engineering
  - Multi-Agent Systems
  - LLMOps
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Model Monitoring
  - MLOps
  - AI Engineering
  - Responsible AI and Governance
  - AI Red Teaming
---

Agent Ops is the operating discipline for deploying, monitoring, evaluating,
and governing AI agents in production. It applies [[MLOps]] habits to
LLM-backed systems that plan, call tools, route work to other agents, and take
actions in user or business workflows.

The topic sits inside [[Agent Engineering]] and next to [[LLMOps]]. LLMOps
covers the broader production layer for LLM systems. Agent Ops narrows the
focus to autonomous tool use and orchestration. It also covers data lineage,
human escalation, and production feedback for agents.

## Orchestration and Services

Agents create an orchestration problem beyond a single model call. The system
has to decide when to invoke tools and how to pass work to sub-agents or other
models. Evaluation output then needs to feed back into changes in the agent. [[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Framework depth matters more than tool sampling at the learning stage. One
discussion recommends starting with one known orchestration tool, developing
depth, and only then comparing alternatives for a specific use case. [[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Ranjitha Kulkarni gives the production version of that tradeoff. Teams can build
agent orchestration directly, or they can use libraries and SDKs. The choice
should follow the workflow's integration and testing needs. LangChain, OpenAI
Agents SDK, smolagents, and MCP-style tool protocols sit in that operating
decision. They aren't a separate tooling debate. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@44:08=>Building Agentic AI Systems]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@48:00=>Agent tool protocols]]

Infrastructure can look familiar because an agent may be a service that talks
to an LLM inference service. CPU and GPU workloads may run as separate services,
and customer replicas can be configured independently. Kubernetes is discussed
as a reasonable deployment layer when the organization already uses it. Agents
still need service management, replication, and machine coordination. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Guardrails and Data Lineage

Agent Ops adds governance because an agent can move data or call sensitive
tools. Guardrails, auditability, retention, and data lineage become operating
requirements when an agent processes user data. They also matter when an agent
sends data to another agent, writes it to a database, or sends it to an offline
workflow. [[cite:s23e03-future-of-ai-agents@30:26=>The Future of AI Agents]]

Action guardrails set boundaries around tool calls. An airline support agent
might handle routine booking questions but route high-value refunds to a human
queue. A payment workflow might require guardrails around a Stripe API call,
plus red-team tests for adverse scenarios before deployment. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

These concerns connect Agent Ops to [[Responsible AI and Governance]] and
[[AI Red Teaming]] because the operating question covers more than answer
quality. It also covers authorized actions and explainable data paths.

## Evaluation and Human Labels

Agent evaluation needs system-specific datasets. Public model benchmarks test
model capability, but agents need examples that represent real users and
expected tool behavior. The examples also need to represent the product's goal.
For a calendar assistant, tests can mock external tools and run integration
checks. They can assert that a valid invite was created instead of demanding one
exact reasoning path. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Multi-tenant systems repeat this work per customer. Each tenant may need
its own golden dataset, pass thresholds, red-team cases, and human-labeling
budget because data can't always be pooled across customers. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

LLM-as-judge can scale evaluation, but it doesn't remove the need for human
labels. Human labels calibrate the judge, and production samples detect gaps.
Ongoing human checks protect against judge drift or bias being replicated in
production. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Monitoring and Feedback

Agent monitoring needs traces, prompts, tool calls, and outcome feedback. Arize
Phoenix appears as one example for monitoring LLM communication
and prompts. Other LLMOps discussions mention Braintrust, Logfire, LangSmith,
and LangFuse as evaluation or trace tools. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]] [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

Production agent feedback includes explicit signals such as thumbs up or down.
It also includes implicit signals when users repeat queries or reframe
questions. Frustration and "why did it do that?" messages identify missing
cases too. Those gaps can become evaluation examples, synthetic data,
human-labeled data, or fine-tuning inputs. [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

Debuggable MVPs matter because agent failures are hard to infer from final
answers alone. Logging traces and function calls early gives teams a way to see
what happened before they add more tools or autonomy. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Conference and R&D work around AI observability reinforces the same operating
point. Teams need visibility into AI behavior before they can improve or trust
the system. That places observability close to agent traces, evaluation
datasets, and production feedback loops
[[cite:s23e09-starting-data-conference-data-makers-fest-story=>Data Makers Fest]].

## Agent Ops Versus LLMOps

General LLMOps can operate a fixed prompt, RAG pipeline, or model endpoint.
Agent Ops has to operate decisions. The production surface includes which tool
was chosen, which data source was accessed, whether escalation happened, and
whether the final outcome satisfied the task.

That changes the reliability model. Tests need to cover tool availability,
parameters, permissions, and goal completion. Monitoring needs to preserve
intermediate steps. Governance needs to explain data movement and action
boundaries. Feedback needs to update both the model-facing evaluation set and
the workflow rules around the agent.

## Related Pages

Useful follow-up pages:

- [[Agent Engineering]]
- [[Multi-Agent Systems]]
- [[LLMOps]]
- [[LLM Production Patterns]]
- [[LLM Evaluation Workflows]]
- [[MLOps]]
- [[Model Monitoring]]
- [[Responsible AI and Governance]]
- [[AI Red Teaming]]
