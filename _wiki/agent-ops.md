---
layout: wiki
title: "Agent Ops"
summary: "AgentOps: orchestration, guardrails, data lineage, deployment risks, and monitoring for AI agents in production."
related:
  - Agent Engineering
  - AI Agents
  - Multi-Agent Systems
  - LLM Production Patterns
  - MLOps
  - AI Engineering
---

Agent Ops is the operational discipline for deploying, monitoring, and governing
AI agents in production. It applies the lessons of
[MLOps]({{ '/wiki/mlops/' | relative_url }}) to agentic systems, adding concerns
specific to autonomous tool use, multi-step reasoning, and the non-deterministic
behavior of LLM-backed systems.

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) names the field
explicitly in
Understanding the AI Engineer
Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).
At 54:03, he says "this field of agent ops will continue to evolve," drawing a
direct parallel to how data science matured into MLOps. He sees the same
trajectory for agents: from experimentation to engineering rigor, with
monitoring and evaluation becoming standard practice.

Agent Ops builds on
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and [AI Agents]({{ '/wiki/agent-engineering/' | relative_url }}).

## Orchestration and the Rise of Agent Ops

Nasser's 45:02 section identifies orchestration as a core AI engineer skill
that distinguishes agent work from simple API calls. Agents must decide when to
invoke tools, how to route decisions between tools or sub-agents, and how to
incorporate evaluation feedback into improvements. His 46:40 section recommends
starting with one orchestration framework and developing depth before
experimenting with alternatives, using a gym analogy: start with one exercise
before trying all fifteen.

His 53:22 section connects agent ops to the data science lineage. He describes
how MLOps brought monitoring of data drift and concept drift to machine learning
models, and expects the same to happen with agents. The field "oscillates"
between being a statistical exercise and an engineering exercise, and agent ops
is where those two modes meet.

## Guardrails and Data Lineage

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) provides the
strongest governance perspective in
[The Future of AI
Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}). His
30:26 section links guardrails and data lineage to what he calls Agent MLOps.
He explains that sensitive industries like healthcare and legal require
handcrafted automation with a human in the loop to ensure correctness. Even
with sophisticated [RAG]({{ '/wiki/rag/' | relative_url }}) and vector
databases, "this is a field where you cannot mess up."

His 47:16 section covers guardrails for agent actions. For an airline customer
service agent, guardrails might require a human in the loop for refunds above a
certain amount. He recommends red teaming for stress-testing in adverse
scenarios and building guardrails around sensitive tool calls like Stripe API
payments. Performance thresholds determine whether an agent can deploy, but
edge cases still route to a human queue.

## Agent Infrastructure and Deployment Risks

Aditya's 56:40 section covers infrastructure and deployment risks. He discusses
Kubernetes for agent deployment, noting that every agent is "basically a
simplistic microservice with a fancy non-deterministic LLM." He sees no reason
agent deployment cannot use Kubernetes, though GPU and CPU workload mixing may
require separate services. He also warns about over-reliance on agents: "do not
be too reliant on agents. They might get consciousness at certain point in
time."

His broader point at 59:37 is about the ground truth problem. Even if an LLM-as-
judge reaches high accuracy, you still need human-in-the-loop sampling. Without
it, you have no way to detect bias that replicates in production over time. He
would never have agents operating completely autonomously, regardless of their
measured accuracy.

## Evaluation Strategy for Agents

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) covers
agent evaluation in
[Building Agentic AI
Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
Her 51:17 section recommends custom datasets and system benchmarks over public
benchmarks like SQuAD, which evaluate model capability rather than system
quality. Her 53:20 section treats agent testing like software engineering
testing: mocked tools, integration tests, and regression tests with 200-300 test
cases for a calendar agent.

Her 56:02 section emphasizes goal-based evaluation. Rather than checking the
exact tool-call path, evaluation focuses on whether the goal was achieved. For
example, finding a skip-level manager directly or by traversing an org chart are
both valid approaches. The assertion checks the outcome, not the path. This is
a key distinction from traditional software testing.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) adds
the generator-evaluator pattern in
[Practical LLM Engineering and
RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
His 13:56 section introduces a loop where one model generates output and another
evaluates it, scoring pass or fail with feedback. His 23:00 section covers gold
test sets, cost, and representativeness. His 26:43 section uses failure analysis
to decide whether retrieval needs to change. These evaluation habits become more
important when systems start calling tools and taking actions.

## Aligning LLM Judges with Human Labels

Aditya's 50:18 section covers aligning LLM judges with human labels. In a
multi-tenancy scenario, each customer needs a golden dataset, and evaluation
must reach more than 95% accuracy, with critical cases at 100%. An LLM-as-judge
is fine-tuned on human data within the use case, but may have bias. To manage
this, the judge's correlation with human annotators should stay above 90-95%.
Sampling from production traffic and sending it to human annotators is how teams
understand gaps and detect drift.

## Evaluation and Monitoring Tools

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) connects
evaluation to production monitoring in
[From Game AI to LLM
Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
His 57:39 section recommends building evaluation pipelines and using tools like
Arize Phoenix to monitor LLM communication and prompts. He frames this as
applying data science techniques for success metrics: controlling variables and
explaining agent behavior for production applications.

Aditya's 43:30 section adds the enterprise scale version. He discusses feedback
intelligence tools that analyze production logs to identify where users are
frustrated, feed that into evaluations, and support fine-tuning. He compares
this to how cloud providers made databases easier through managed services like
MongoDB and Redis. Agent evaluation infrastructure is becoming a similar
standardized layer.

## Related Pages

- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [AI Agents]({{ '/wiki/agent-engineering/' | relative_url }})
- [Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
