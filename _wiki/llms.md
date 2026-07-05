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
  - Long-Context LLM Evaluation
  - Agent Engineering
  - Generative AI
  - Multimodal LLMs
  - NLP
---

Large language models are machine learning models trained to process and
generate language. Teams use them for text generation, summarization,
translation, and information extraction. They also show up in retrieval-backed
question answering, agents, and developer tools.

An LLM is rarely a finished product on its own. The model sits inside a larger
system with prompts, retrieval, data pipelines, and evaluation. Deployment
controls, security checks, and human review sit around that system.

That places LLMs near [[AI]]
and [[NLP]]. It also links them to
[[generative AI]],
[[agent engineering]], and
[[LLM production patterns]].

## Capabilities and Prompting

An LLM is a general language model that teams can prompt for many language
tasks, then adapt with context, examples, and retrieval. Teams further tune it
with fine-tuning or tools when prompting isn't enough.
[[book:20241017-build-large-language-model-from-scratch=>Build a Large Language Model (From Scratch)]]
grounds that definition by walking through a transformer-based model from the
ground up.

Generative and non-generative language models are distinct. Modern LLMs use
transformers because they handle unstructured text at scale
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

The traditional NLP pipeline labels data, designs the task, tests behavior, and
deploys the system. GPT-3-style prompting contrasts with that pipeline: a model
can produce useful behavior from a prompt instead of a task-specific training
pipeline
[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]].
The
[[book:20230306-gpt-3=>GPT-3]]
book by Sandra Kublik and Shubham Saboo collects the early practitioner stories
behind that prompt-driven shift.

Everyday uses include summaries, translation, and CSV workflows. Prompting
practice adds role prompts, structured output, and timestamps
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Deployment Boundaries

LLMs are useful, but different failure modes call for drawing different
boundaries first.

For deployment, open-source and API models differ in control, privacy, and
fine-tuning. Model-drift risk appears when an API provider changes behavior
behind the scenes
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
That makes LLM adoption an
[[AI infrastructure]] and
[[production]] decision. Making models
smaller and faster for deployment is the practice of
[[Model Optimization]].

For NLP team design, GPT-3 has limits around cost and control plus bias and
privacy risks. It's useful for MVPs, but it doesn't replace in-house pipelines
when the team needs control
[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]].

For applied research, long-context evaluation reveals performance drops around
32k-64k context in a financial benchmark. That ties LLM quality to empirical
tests rather than advertised context length
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

For trust and safety, hallucinations, legal exposure, and financial incidents
drive layered defenses. Non-LLM classifiers can help when a generative model is
too easy to manipulate
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].

## LLM Use Cases

Practical language work includes summaries, translation, and CSV handling.
Transcript automation uses tools such as Gemini, Descript, and Loom. Developer
assistants include GitHub Copilot, Cursor, and IDE agents
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Use [[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
for the personal workflow version of these examples.
Screenshots, diagrams, audio, and video move the same product boundary toward
[[multimodal-llms=>multimodal LLMs]].

LLMs also appear as product interfaces for chatbots, controlled machine
translation, and moderation support. In high-risk workflows, people review the
model output
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].

Agents are a separate use case because the model does more than answer once.
Agents combine LLM autonomy with objectives and tool use. They may also use
memory and knowledge stores
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
The
[[agent-engineering=>AI agents]] page separates agent
workflow design from ordinary prompting.

## RAG and Fine-Tuning

Changing model behavior and adding current knowledge are separate jobs.

Fine-tuning handles specialization, domain adaptation, and tone and format
control. Retrieval handles changing knowledge: the team indexes documents and
retrieves relevant passages without retraining the model for every fact update
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] uses the
same split. Retrieval helps when the system needs fresh documents, citations,
proprietary knowledge, or reviewable evidence. Fine-tuning helps when the model
should behave differently. It can also help with a repeated output style or a
repeated task.

On the implementation path, RAG with chunking and embeddings can be a quick
business win. Chunk size, sliding windows, and context rot decide what the model
sees
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Chunking, retrieval, and summarization for large documents are the research
reason to prefer retrieval in many long-document settings, given long-context
performance limits
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

## Evaluation

LLM evaluation is task-specific because a model's general benchmark score
doesn't prove its workflow.

Generator-evaluator runs provide automated quality control. Gold tests raise
questions of cost, representativeness, and test-set size. Failure analysis
decides whether retrieval, prompts, or data should change
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

For agents, evaluation extends to custom datasets and system benchmarks. It also
uses mocked tools, integration tests, and regression tests. Outcome assertions
fit better than exact path matching because valid agent runs may take different
tool-call paths
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Long-context models need tests that match the document task. In one financial
setting, evaluation checks long-context behavior instead of relying on
context-window size alone
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].
That makes [[long-context-llm-evaluation=>long-context LLM evaluation]] part of
the evaluation path for document-heavy systems.

Use [[LLM Evaluation Workflows]]
for evaluation patterns and
[[Production Search Evaluation]]
for retrieval quality when RAG depends on search.

## Serving, Cost, and Operations

Production LLM systems need normal software and ML operations. Teams have to
plan deployment, latency control, and cost control. They also need monitoring,
observability, rollback plans, and ownership.

Serving covers model size, compression, and inference optimization. Teams may
prototype with GPT-3.5 or GPT-4 APIs before choosing open-source LLMs for
production. That choice brings latency, cost, self-hosting, and hardware
questions
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

Production LLM work treats context engineering as a core design task. RAG also
brings latency, cost, and noisy inputs. The retrieval backend also needs
chunking, metadata, and wrappers so the system gives the LLM useful context
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Operational feedback loops rest on logging, traces, and debuggable MVPs
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Those practices connect LLM work to [[MLOps]],
[[software engineering]],
and [[AI engineering]].

## Security and Trust

Security isn't a late-stage add-on for LLM systems because the model receives
instructions from users and sometimes from retrieved documents. That creates
new attack paths around prompt injection, data exfiltration, hallucinated
answers, and overconfident users.

A large-scale chatbot hacking exercise exposes data exfiltration through prompt
overload and knowledge-base retrieval. The defenses include output validation,
query analysis, layered defenses, and non-LLM classifiers where they're harder
to manipulate than generative models
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].

GPT-3 risks include concerns around cost, control, bias, and privacy
[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]].
Those concerns connect LLMs to
[[AI red teaming]],
[[security]], and
[[privacy engineering for ML]].

Security also affects retrieval because a RAG system may retrieve confidential
or poisoned documents. The LLM can then expose or amplify them, so validation,
query analysis, and layered checks need to surround generation
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].

## Related Pages

These pages cover the surrounding techniques, roles, and production concerns.

- [[LLM Production Patterns]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[retrieval-augmented-generation=>RAG]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[agent-engineering=>AI Agents]]
- [[Prompt Engineering]]
- [[Vector Databases]]
- [[Generative AI]]
- [[multimodal-llms=>Multimodal LLMs]]
- [[NLP]]
- [[Security]]
- [[AI Red Teaming]]
- [[LLM Tools]]
- [[LLM System Design Interview]]
