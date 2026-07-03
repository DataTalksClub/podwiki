---
layout: wiki
title: "LLMOps"
summary: "LLMOps covers operating LLM systems in production, from deployment and tracing to evaluation, guardrails, cost control, and feedback loops."
related:
  - MLOps
  - LLM Production Patterns
  - AI Engineering
  - Model Monitoring
  - Agent Engineering
  - Agent Ops
  - Evaluation
  - LLM Evaluation Workflows
  - LLM Deployment
  - LLM Cost Optimization
  - Caching
  - DataOps
  - GitOps for Data Teams
  - MLOps vs DevOps
---

LLMOps is the operating discipline for production systems built with
[[llms=>large language models]]. It extends [[MLOps]] into prompts and
retrieval. It also covers agent traces and evaluation datasets. Provider choice,
cost controls, guardrails, and human feedback belong in the same operating
layer.

The topic sits between
[[LLM Production Patterns]], [[AI Engineering]], and [[Agent Engineering]].
It also connects to [[Model Monitoring]] and [[Evaluation]].

The operating boundary is wider than model deployment because LLM systems need
ingestion pipelines for [[retrieval-augmented-generation=>RAG]]. They also need
durable workflows for agent or retrieval steps, observability for
multi-call responses, and evaluation loops. Those loops must survive changing
prompts, tools, and model versions. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]

## Shipping Boundary

Production LLM work combines product code, data pipelines, and model behavior.
The AI engineering stack includes creating and evaluating agents, ingesting data
for RAG, and making knowledge accessible to those agents. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]

Durable workflow tools such as Prefect or Dagster appear in this operating
layer because ingestion and retrieval need queues, retries, and resilient
execution. The same workflow layer can coordinate data jobs and agentic steps
instead of splitting them across unrelated orchestrators. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]

## Traces and Debugging

LLMOps observability starts with traces rather than only aggregate metrics. A
trace records what happens between a request and response. A thread groups the
conversation-level sequence of user inputs and outputs. That makes it possible
to sample whole conversations, look at function calls, and debug failures
inside the chain rather than only judging the final answer. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]

The tooling examples vary by stack. Arize Phoenix and Logfire appear as trace
or monitoring tools. LangSmith, Braintrust, and LangFuse appear in the same
tooling category. The operating habit matters more than the vendor: log the
intermediate calls early and keep the MVP debuggable. Use those traces for
failure analysis before adding more architecture. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]] [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]

## Evaluation and Regression

LLMOps treats evaluation as a production workflow, not a one-time model score.
A generator-evaluator loop can have one model create an output and another
score it with pass/fail feedback. Representative gold tests keep prompt and RAG
changes measurable, while failure analysis shows whether the next fix belongs
in retrieval or formatting. It can also show whether model choice or prompt
design needs to change. [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]

Agentic systems add tool calls, parameters, memory, and variable execution
paths. Public benchmarks like SQuAD test model capability, but
production agents need system-specific datasets. Tests can mock tools, separate
integration checks from regression tests, and assert successful outcomes rather
than one exact tool-call sequence. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]

That makes [[LLM Evaluation Workflows]] a core LLMOps dependency. The
evaluation set, trace logs, and production feedback need to evolve together as
the product changes.

## Guardrails, Lineage, and Human Review

Enterprise LLMOps includes governance around where data goes, what an agent is
allowed to do, and how teams prove the system behaved correctly. Agent MLOps
discussions connect guardrails and auditability to regulated use cases. They
also connect retention and data lineage to finance, legal, and healthcare
workflows. [[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

Lineage matters because one entry-point agent can send user data to another
agent, write it to a database, or pass it into an offline workflow. Cost and
latency are visible symptoms, but data movement and retention determine whether
the system can satisfy governance requirements. [[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

Human review remains part of the loop even when LLM judges scale evaluation.
For sensitive systems, golden datasets and LLM-as-judge checks work together.
Production sampling and human annotators protect the ground truth when judges
drift or encode bias. [[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

## Feedback Loops

Feedback loops turn production behavior into new evaluation examples. Explicit
signals such as thumbs up or thumbs down are useful, but implicit signals also
matter. Users repeat a query, reframe a question, ask why an agent did
something, or show frustration. Those gaps can become synthetic examples,
human-labeled examples, fine-tuning data, or new regression tests. [[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

This is where [[Agent Ops]] overlaps with LLMOps. Agents take actions, so
feedback must cover answer quality and tool use. It must also cover
permissions, lineage, and human escalation.

## Cost and Model Ownership

Cost control includes both prompt efficiency and serving choices. Prompt
compression creates a shorter prompt intended to preserve behavior while
reducing tokens. Prompt caching reuses the shared part of repeated prompts so
large context can be reused. A codebase, for example, doesn't have to be
processed the same way on every request. [[cite:production-ready-ai-engineering|Production AI Engineering]]

Teams choose a model-ownership boundary when they deploy. Teams can use
API-based models for fast prototypes because they can produce a demo quickly.
Longer-term production
systems may move toward open-source or self-hosted models for control, privacy,
and predictable model versions. Latency and cost can push the same choice.
Hidden provider-side model changes are an operational risk because product
behavior can shift without the application team changing its own code. [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]

These tradeoffs connect [[LLM Deployment]], [[LLM Cost Optimization]],
[[Caching]], and [[AI Infrastructure]].

## Operating Tradeoffs

LLMOps discussions start from different failure modes. One starting point is the
serving boundary, where teams compare API speed with self-hosting control.
Another starting point is debugging, where traces and evaluation tools come
before the system grows. A third is governance, where guardrails and lineage
control agents that touch sensitive workflows.

The shared operating requirement is ownership. Production LLM teams need to
know what context was supplied and which tools or models were called. They also
need cost data, output evaluations, and feedback that can change the next
version.

## Related Pages

Useful follow-up pages:

- [[MLOps]]
- [[LLM Production Patterns]]
- [[AI Engineering]]
- [[Agent Engineering]]
- [[Agent Ops]]
- [[Evaluation]]
- [[LLM Evaluation Workflows]]
- [[Model Monitoring]]
- [[LLM Deployment]]
- [[LLM Cost Optimization]]
- [[Caching]]
