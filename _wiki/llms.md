---
layout: wiki
title: "LLMs"
summary: "How DataTalks.Club guests discuss large language models as language, retrieval, agent, evaluation, production, and security components."
related:
  - AI
  - AI Engineering
  - AI Tooling
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Agent Engineering
  - Generative AI
  - NLP
---

Large language models are machine learning models trained to process and
generate language. Their uses span text generation and summarization,
translation, information extraction, retrieval-backed question answering, agents,
and developer tools.

An LLM is rarely a finished product on its own. The model sits inside a larger
system with prompts and retrieval, data pipelines and evaluation, and deployment,
security checks, and human review.

That places LLMs near [[AI]]
and [[NLP]]. It also links them to
[[generative AI]],
[[agent engineering]], and
[[LLM production patterns]].

## Language Model Capabilities

The practical definition is simple: an LLM is a general language model that
teams can prompt for many language tasks, then adapt with context, examples, and
retrieval, and further tune with fine-tuning or tools when prompting isn't
enough.
[[book:20241017-build-large-language-model-from-scratch|Build a Large Language Model (From Scratch)]]
by Sebastian Raschka walks through implementing a transformer-based model
from the ground up, which grounds the same capabilities discussed below.

Generative and non-generative language models are distinct, and modern LLMs are
built on transformers; they matter because they handle unstructured text at scale
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

The traditional NLP pipeline labels data, designs the task, tests behavior, and
deploys the system. GPT-3-style prompting contrasts with that pipeline: a model
can produce useful behavior from a prompt instead of a task-specific training
pipeline
([[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]]).
The
[[book:20230306-gpt-3|GPT-3]]
book by Sandra Kublik and Shubham Saboo collects the early practitioner stories
behind that prompt-driven shift.

Everyday uses include summaries, translation, and CSV workflows; prompting
practice adds role prompts, structured output, and timestamps
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

## Deployment, Research, and Safety Boundaries

LLMs are useful, but different failure modes call for drawing different
boundaries first.

From the deployment angle, open-source and API models differ in control, privacy,
and fine-tuning, and model-drift risk arises when an API provider changes
behavior behind the scenes
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
That framing makes LLM adoption an
[[AI infrastructure]] and
[[production]] decision. Making models
smaller and faster for deployment is the practice of
[[Model Optimization]].

From the NLP team-design angle, GPT-3 carries limitations around cost and
control plus bias and privacy risks; it is useful for MVPs but not a replacement
for in-house pipelines when the team needs control
([[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]]).

From the applied-research angle, long-context evaluation reveals performance
drops around 32k-64k context in a financial benchmark, tying LLM quality to
empirical tests rather than advertised context length
([[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]).

From the trust-and-safety angle, hallucinations, legal exposure, and financial
incidents drive layered defenses, with non-LLM classifiers added when a
generative model is too easy to manipulate
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

## LLM Use Cases

LLM use cases start with practical language work: summaries, translation, and
CSV handling, plus transcript automation with tools such as Gemini, Descript,
and Loom, and developer assistants such as GitHub Copilot, Cursor, and IDE agents
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

LLMs also appear as product interfaces: chatbots, controlled machine
translation, moderation support, and human review, with the model kept in an
assistant role where people review high-risk outputs
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Agents are a separate use case because the model does more than answer once.
Agents combine autonomy, objectives, and LLMs with tools, memory, and knowledge
stores
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
That's why the
[[agent-engineering|AI agents]] page separates agent
workflow design from ordinary prompting.

## RAG and Fine-Tuning

There is a strong line between changing model behavior and adding current
knowledge.

Fine-tuning handles specialization, domain adaptation, and tone and format
control, while retrieval handles changing knowledge: the team indexes documents
and retrieves relevant passages without retraining the model for every fact
update
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

[[rag-vs-fine-tuning|RAG vs Fine-Tuning]] uses the
same split. Retrieval helps when the system needs fresh documents, citations,
proprietary knowledge, or reviewable evidence. Fine-tuning helps when the model
should behave differently. It can also help with a repeated output style or a
repeated task.

On the implementation path, RAG with chunking and embeddings is a quick business
win, and chunking strategy matters: chunk size, sliding windows, and context rot
decide what the model sees
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Chunking, retrieval, and summarization for large documents are the research
reason to prefer retrieval in many long-document settings, given long-context
performance limits
([[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]).

## Evaluation

LLM evaluation is task-specific. A model's general benchmark score does not prove
its workflow.

A generator-evaluator loop provides automated quality control; gold tests raise
questions of cost, representativeness, and test-set size; and failure analysis
decides whether retrieval, prompts, or data should change
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

For agents, evaluation extends to custom datasets and system benchmarks, mocked
tools, integration tests, and regression tests, with outcome assertions instead
of exact path matching because valid agent runs may take different tool-call
paths
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Long-context work shows why evaluation has to match the document task:
long-context models are tested in a financial setting instead of relying on
context-window size alone
([[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]).

Use [[LLM Evaluation Workflows]]
for evaluation patterns and
[[Production Search Evaluation]]
for retrieval quality when RAG depends on search.

## Serving, Cost, and Operations

Production LLM systems need normal software and ML operations. Teams have to
plan deployment, latency control, and cost control. They also need monitoring,
observability, rollback plans, and ownership.

Serving covers model size, compression, and inference optimization. Prototyping
with GPT-3.5 or GPT-4 APIs is separate from production choices around
open-source LLMs, which bring latency, cost, self-hosting, and hardware choices
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

Production workflow design names context engineering as a core design task,
along with a RAG reality check around latency, cost, and noisy inputs and the
rework of retrieval backends — chunking, metadata, and wrappers so the system
gives the LLM useful context
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Operational feedback loops rest on logging, traces, and debuggable MVPs
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Those practices connect LLM work to [[MLOps]],
[[software engineering]],
and [[AI engineering]].

## Security and Trust

Security isn't a late-stage add-on for LLM systems because the model receives
instructions from users and sometimes from retrieved documents. That creates
new attack paths around prompt injection, data exfiltration, hallucinated
answers, and overconfident users.

A large-scale chatbot hacking exercise exposes data exfiltration through prompt
overload and knowledge-base retrieval; the defenses are output validation, query
analysis, layered defenses, and non-LLM classifiers where they're harder to
manipulate than generative models
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Related risks include GPT-3 concerns around cost, control, bias, and privacy
([[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]]).
Those concerns connect LLMs to
[[AI red teaming]],
[[security]], and
[[privacy engineering for ML]].

Security also affects retrieval because a RAG system may retrieve confidential
or poisoned documents. The LLM can then expose or amplify them. Teams need
access controls before retrieval, validation after generation, and audit trails
for high-risk workflows.

## Related Pages

These pages cover the surrounding techniques, roles, and production concerns.

- [[LLM Production Patterns]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[retrieval-augmented-generation|RAG]]
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[agent-engineering|AI Agents]]
- [[Prompt Engineering]]
- [[Vector Databases]]
- [[Generative AI]]
- [[NLP]]
- [[Security]]
- [[AI Red Teaming]]
- [[LLM Tools]]
- [[LLM System Design Interview]]
