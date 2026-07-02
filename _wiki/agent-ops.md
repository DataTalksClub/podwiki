---
layout: wiki
title: "Agent Ops"
summary: "AgentOps: orchestration, guardrails, data lineage, deployment risks, and monitoring for AI agents in production."
related:
  - Agent Engineering
  - Multi-Agent Systems
  - LLM Production Patterns
  - MLOps
  - AI Engineering
---

Agent Ops is the operational discipline for deploying, monitoring, and governing
AI agents in production. It applies the lessons of
[[MLOps]] to agentic systems, adding concerns
specific to autonomous tool use, multi-step reasoning, and the non-deterministic
behavior of LLM-backed systems.

The field of agent ops "will continue to evolve," a direct parallel to how data
science matured into MLOps. The trajectory runs from experimentation to
engineering rigor, with monitoring and evaluation becoming standard practice
([Understanding the AI Engineer Role](https://datatalks.club/podcast/s23e07-understanding-ai-engineer-role.html)).

Agent Ops builds on
[[Agent Engineering]],
[[LLM Production Patterns]],
and [[agent-engineering|AI Agents]].

## Orchestration and the Rise of Agent Ops

Orchestration is a core AI engineer skill that distinguishes agent work from
simple API calls. Agents must decide when to invoke tools, how to route decisions
between tools or sub-agents, and how to incorporate evaluation feedback into
improvements. Starting with one orchestration framework and developing depth
before experimenting with alternatives works better than sampling many at once,
like a gym routine that starts with one exercise before trying all fifteen
([Understanding the AI Engineer Role](https://datatalks.club/podcast/s23e07-understanding-ai-engineer-role.html)).

Agent ops descends from the data science lineage. MLOps brought monitoring of
data drift and concept drift to machine learning models, and agents follow the
same path. The field "oscillates" between being a statistical exercise and an
engineering exercise, and agent ops is where those two modes meet
([Understanding the AI Engineer Role](https://datatalks.club/podcast/s23e07-understanding-ai-engineer-role.html)).

## Guardrails and Data Lineage

Guardrails and data lineage form part of what is called Agent MLOps. Sensitive
industries like healthcare and legal require handcrafted automation with a human
in the loop to ensure correctness. Even with sophisticated
[[retrieval-augmented-generation|RAG]] and vector databases, "this is a field
where you cannot mess up"
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

Guardrails constrain agent actions. For an airline customer service agent,
guardrails might require a human in the loop for refunds above a certain amount.
Red teaming stress-tests adverse scenarios, and guardrails wrap sensitive tool
calls like Stripe API payments. Performance thresholds determine whether an
agent can deploy, but edge cases still route to a human queue
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

## Agent Infrastructure and Deployment Risks

Kubernetes suits agent deployment, since every agent is "basically a simplistic
microservice with a fancy non-deterministic LLM." Nothing prevents agent
deployment on Kubernetes, though GPU and CPU workload mixing may require separate
services. Over-reliance on agents is a risk: "do not be too reliant on agents.
They might get consciousness at certain point in time"
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

The ground truth problem remains. Even if an LLM-as-judge reaches high accuracy,
human-in-the-loop sampling is still needed; without it, there is no way to detect
bias that replicates in production over time. Agents should never operate
completely autonomously, regardless of their measured accuracy
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

## Evaluation Strategy for Agents

Custom datasets and system benchmarks beat public benchmarks like SQuAD, which
evaluate model capability rather than system quality. Agent testing mirrors
software engineering testing: mocked tools, integration tests, and regression
tests with 200-300 test cases for a calendar agent
([Building Agentic AI Systems](https://datatalks.club/podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.html)).

Goal-based evaluation checks whether the goal was achieved rather than the exact
tool-call path. Finding a skip-level manager directly or by traversing an org
chart are both valid approaches; the assertion checks the outcome, not the path.
This is a key distinction from traditional software testing
([Building Agentic AI Systems](https://datatalks.club/podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.html)).

The generator-evaluator pattern runs a loop where one model generates output and
another evaluates it, scoring pass or fail with feedback. Gold test sets, cost,
and representativeness shape the evaluation set, and failure analysis decides
whether retrieval needs to change. These evaluation habits become more important
when systems start calling tools and taking actions
([Practical LLM Engineering and RAG](https://datatalks.club/podcast/practical-llm-engineering-and-rag.html)).

## Aligning LLM Judges with Human Labels

Aligning LLM judges with human labels matters at scale. In a multi-tenancy
scenario, each customer needs a golden dataset, and evaluation must reach more
than 95% accuracy, with critical cases at 100%. An LLM-as-judge fine-tuned on
human data within the use case may still carry bias, so the judge's correlation
with human annotators should stay above 90-95%. Sampling from production traffic
and sending it to human annotators is how teams understand gaps and detect drift
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

## Evaluation and Monitoring Tools

Evaluation connects to production monitoring. Evaluation pipelines and tools like
Arize Phoenix monitor LLM communication and prompts, applying data science
techniques for success metrics: controlling variables and explaining agent
behavior for production applications
([From Game AI to LLM Agents](https://datatalks.club/podcast/from-game-ai-to-modern-ai-agents.html)).
For a broader comparison of open-source and free options such as Arize Phoenix,
LangSmith, DeepEval, and Ragas, see
[Open Source and Free AI Agent Evaluation Tools](https://datatalks.club/blog/open-source-free-ai-agent-evaluation-tools.html).

At enterprise scale, feedback intelligence tools analyze production logs to
identify where users are frustrated, feed that into evaluations, and support
fine-tuning, much as cloud providers made databases easier through managed
services like MongoDB and Redis. Agent evaluation infrastructure is becoming a
similar standardized layer
([The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html)).

## Related Pages

- [[Agent Engineering]]
- [[agent-engineering|AI Agents]]
- [[multi-agent-systems|Multi-Agent Systems]]
- [[LLM Production Patterns]]
- [[MLOps]]
- [[LLM Evaluation Workflows]]
- [[Production]]
- [[Responsible AI and Governance]]
