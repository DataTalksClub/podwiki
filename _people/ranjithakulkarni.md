---
layout: "person"
title: "Ranjitha Kulkarni"
source_person: "../datatalksclub.github.io/_people/ranjithakulkarni.md"
person_id: "ranjithakulkarni"
summary: "Staff ML engineer focused on agentic AI, assistant evaluation, retrieval, and pragmatic LLM product engineering."
expertise: ["LLMs", "AI", "agent engineering", "retrieval-augmented generation", "MLOps", "tools"]
podcast_episodes: ["building-agentic-ai-engineering-tooling-retrieval-evaluation"]
curated: "true"
source_url: "https://datatalks.club/people/ranjithakulkarni.html"
---

## Background

Ranjitha Gurunath Kulkarni is a Staff Machine Learning Engineer at NeuBird.ai.
She previously built LLM- and agent-powered product capabilities at Dropbox Dash
and worked on speech recognition, language modeling, online metrics, and
assistant evaluation at Microsoft. That mix of production ML and assistant
evaluation frames her DataTalks.Club episode,
[Building Agentic AI Systems: Pragmatic Agent Engineering, Tooling, Retrieval & Evaluation](https://datatalks.club/podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.html).

## Agent Engineering as Systems Work

Ranjitha defines an agent around autonomous task completion, not around a single
library or prompt template. Around 11:00-12:31 in
[the episode](https://datatalks.club/podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.html),
she connects the older reinforcement-learning idea of an agent to modern LLM
systems. The agent pursues a goal while the implementation orchestrates LLM
calls, memory, knowledge stores, and
[tools]({{ '/wiki/tools/' | relative_url }}).

Her contribution to [agent engineering]({{ '/wiki/agent-engineering/' | relative_url }})
is practical because an agent isn't only "an LLM with tools." Engineers design
the wrapper and planning strategy. They also define tool interfaces, decide
which context reaches the model, and add checks that make repeated behavior
possible.

Around 15:23-19:06, she separates single-step agents from multi-step and
multi-pass systems. She notes that many companies end up with custom agentic
platforms because broad abstractions rarely fit the product problem cleanly.

## Production Agents and Operational Tools

Her example fits
[LLM production patterns][llm-production-patterns]
because she centers operations.

Around 21:21-27:33, agents assemble context across logs, metrics, and
operational APIs.

The investigation may also need deployment state and source code.

The production problem isn't only connecting to observability tools or
infrastructure tools. She names Datadog, New Relic, Kubernetes, and
ElasticSearch as examples.

Teams also have to abstract those integrations. The agent still has to work
across many customer setups while respecting the domain details that experienced
SREs know.

Use her episode for [MLOps]({{ '/wiki/mlops/' | relative_url }})
and the [AI engineer role]({{ '/wiki/ai-engineer-role/' | relative_url }})
when the page needs a concrete agent-production example.
She emphasizes reliability, customer feedback, and repeatable operations. She
also brings in integration variance because customer tool stacks differ.

Around 44:36-47:21, she gives a pragmatic framework view. Libraries can help
bootstrap agents, but teams should understand the tools and instructions. They
also need to understand memory and data queries well enough to debug what the
agent is doing.

## Retrieval, Context, and RAG Boundaries

Ranjitha's retrieval discussion is a strong bridge between
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and agent design. Around 28:17-35:09, she treats context engineering as being
deliberate about what information reaches the LLM. Long context windows don't
remove the need for retrieval because latency, cost, and noisy inputs still
matter. RAG remains useful, but she frames vanilla RAG as only one way to reduce
a large search space before the model answers.

She's especially useful on when RAG is enough. Around 36:11-40:00, she says
RAG fits large search spaces with relatively simple question-answering needs.
It's weaker when the task depends on current context or several data sources.
It's also weaker when the task needs dynamic planning or multiple API
integrations. In those cases, retrieval becomes one tool the agent can call
rather than the whole system.

In her calendar assistant example at 40:30-43:06, the agent may need calendars
and org data. It may also need meeting transcripts and different plans depending
on the request.

## Evaluation, Tests, and Outcome Assertions

Ranjitha's strongest evaluation point is that public model benchmarks don't
measure the system a team is shipping. Around 51:17-53:20, she argues that
teams need custom datasets representing real users and real tasks. Use her for
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
when the question isn't only whether the model can answer. Her evaluation
framing also asks whether the product calls the right tools with the right
parameters.

Around 53:20-57:23, she maps agent evaluation to software testing. Teams can
mock tools to avoid external service calls and run integration tests against
controlled inputs. They can also keep regression suites for common tasks such
as calendar booking or SRE investigations.

She also warns against asserting one exact path: an LLM-based agent may reach
the same correct result through different valid tool calls. A stronger test
asserts the outcome, such as whether the calendar invite has the right
attendees, time, and metadata. Domain knowledge still matters because the test
has to know which outcomes count as correct.

[llm-production-patterns]: {{ '/wiki/llm-production-patterns/' | relative_url }}
