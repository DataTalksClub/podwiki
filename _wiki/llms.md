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
generate language. In DataTalks.Club episodes, guests use them for text
generation and summarization. They also use them for translation, information
extraction, and retrieval-backed question answering. Other episodes cover
agents and developer tools.

DataTalks.Club guests don't treat an LLM as a finished product. They usually
place the model inside a larger system with prompts and retrieval. Data
pipelines and evaluation belong there too. So do deployment, security checks,
and human review.

That places LLMs near [[AI]]
and [[NLP]]. It also links them to
[[generative AI]],
[[agent engineering]], and
[[LLM production patterns]].

## Language Model Capabilities

The practical definition across the podcast is simple: an LLM is a general
language model that teams can prompt for many language tasks. Teams then adapt
it with context, examples, and retrieval. They can also use fine-tuning or
tools when prompting isn't enough.
[[book:20241017-build-large-language-model-from-scratch|Build a Large Language Model (From Scratch)]]
by Sebastian Raschka walks through implementing a transformer-based model
from the ground up, which grounds the same capabilities discussed below.

[[person:meryemarik|Meryem Arik]] gives the most direct
production definition in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 10:24, she separates generative and non-generative language models and
connects modern LLMs to transformers. At 14:45, she explains why they matter
for unstructured text at scale.

[[person:ivanbilan|Ivan Bilan]] connects LLMs to older
NLP work in
[[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]].
His 34:57 section walks through the traditional NLP pipeline. The team labels
data, designs the task, tests behavior, and deploys the system. At 38:55, he
contrasts that pipeline with GPT-3-style prompting, where a model can produce
useful behavior from a prompt instead of a task-specific training pipeline.
The
[[book:20230306-gpt-3|GPT-3]]
book by Sandra Kublik and Shubham Saboo collects the early practitioner stories
behind that prompt-driven shift, which anchors the same GPT-3 experiments Ivan
references.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] gives
the builder's definition in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 9:28, he lists everyday uses such as summaries, translation, and CSV
workflows. At 11:11, he moves from the model to prompting practice: role
prompts. He also covers structured output and timestamps.

## Deployment, Research, and Safety Boundaries

Guests agree that LLMs are useful, but they start from different failure modes.
That changes which boundary they draw first.

Meryem starts from deployment choice. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
the 16:48 section compares open-source and API models through control, privacy,
and fine-tuning. At 18:46, she adds model-drift risk when an API provider
changes behavior behind the scenes. Her framing makes LLM adoption an
[[AI infrastructure]] and
[[production]] decision. Making models
smaller and faster for deployment is the practice of
[[Model Optimization]].

Ivan starts from NLP team design. In
[[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]],
the 43:05 section warns about GPT-3 limitations around cost and control. He
also names bias and privacy risks. At 46:10, he treats GPT-3 as useful for MVPs but not a replacement for
in-house pipelines when the team needs control.

[[person:lavanyagupta|Lavanya Gupta]] starts from
applied research. In
[[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]],
the 10:15 section focuses on long-context evaluation. At 12:36, she describes
performance drops around 32k-64k context in a financial benchmark. Her view
keeps LLM quality tied to empirical tests, not advertised context length.

[[person:mariasukhareva|Maria Sukhareva]] starts from
trust and safety. In
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]],
the 11:38 section covers hallucinations, legal exposure, and financial
incidents. At 16:15, she recommends layered defenses. At 17:00, she adds
non-LLM classifiers when a generative model is too easy to manipulate.

## LLM Use Cases

The podcast's LLM use cases start with practical language work. Hugo's
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
episode uses summaries, translation, and CSV handling as concrete examples. It
also covers transcript workflows and developer assistants. The 12:22 section
covers transcript automation with tools such as Gemini, Descript, and Loom. The
31:56 section discusses developer tools and assistants such as GitHub Copilot,
Cursor, and IDE agents.

LLMs also appear as product interfaces. In
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]],
Maria discusses chatbots and controlled machine translation. She also covers
moderation support and human review. Her 25:34 section keeps the model in an assistant role where
people review high-risk outputs.

Agents are a separate use case because the model does more than answer once.
[[person:ranjithakulkarni|Ranjitha Kulkarni]] defines
that boundary in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 11:00, she connects agents to autonomy, objectives, and LLMs. At 12:31, she
adds tools, memory, and knowledge stores. That's why the
[[agent-engineering|AI agents]] page separates agent
workflow design from ordinary prompting.

## RAG and Fine-Tuning

Guests draw a strong line between changing model behavior and adding current
knowledge.

Meryem explains this split in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 26:30, she frames fine-tuning as specialization and domain adaptation. She
also discusses tone and format control. At 40:46 and 42:02, she recommends retrieval for changing
knowledge. The team can index documents and retrieve relevant passages without
retraining the model for every fact update.

[[rag-vs-fine-tuning|RAG vs Fine-Tuning]] uses the
same split. Retrieval helps when the system needs fresh documents, citations,
proprietary knowledge, or reviewable evidence. Fine-tuning helps when the model
should behave differently. It can also help with a repeated output style or a
repeated task.

Hugo's
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
episode gives the implementation path. At 44:26, he presents RAG with chunking
and embeddings as a quick business win. At 48:20, he shows why chunking
strategy matters. Chunk size, sliding windows, and context rot decide what the
model sees.

Lavanya's
[[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]
episode adds a research reason to prefer retrieval in many long-document
settings. At 14:54, she discusses chunking, retrieval, and summarization for
large documents after describing long-context performance limits.

## Evaluation

LLM evaluation in the podcast is task-specific. A team shouldn't assume that a
model's general benchmark score proves its workflow.

Hugo's
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
episode is the main practical source. At 13:56, he introduces a
generator-evaluator loop for automated quality control. At 23:00, he
discusses gold tests, cost, and representativeness. He also covers how large
the test set should be. At 26:43, he uses
failure analysis to decide whether retrieval, prompts, or data should change.

Ranjitha extends that logic to agents in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 51:17, she recommends custom datasets and system benchmarks. At 53:20, she
adds mocked tools, integration tests, and regression tests. At 56:02, she
emphasizes outcome assertions instead of exact path matching because valid
agent runs may take different tool-call paths.

Lavanya's long-context work shows why evaluation has to match the document
task. In
[[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]],
the 10:15 and 12:36 sections test long-context models in a financial setting
instead of relying on context-window size alone.

Use [[LLM Evaluation Workflows]]
for evaluation patterns and
[[Production Search Evaluation]]
for retrieval quality when RAG depends on search.

## Serving, Cost, and Operations

Production LLM systems need normal software and ML operations. Teams have to
plan deployment, latency control, and cost control. They also need monitoring,
observability, rollback plans, and ownership.

Meryem's
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
episode makes serving explicit. The 25:26 section covers model size,
compression, and inference optimization. At 49:44, she separates prototyping
with GPT-3.5 or GPT-4 APIs from production choices around open-source LLMs. At
51:35, she discusses latency and cost. She also covers self-hosting and
hardware choices.

Ranjitha adds production workflow design. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
the 21:21 section names context engineering as a core design task. At 29:30,
she gives the RAG reality check around latency, cost, and noisy inputs. At
31:38 and 32:48, she discusses reworking retrieval backends. She also covers
chunking, metadata, and wrappers so the system gives the LLM useful context.

Hugo adds operational feedback loops. In
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
the 27:38 section covers logging, traces, and debuggable MVPs. Those practices
connect LLM work to [[MLOps]],
[[software engineering]],
and [[AI engineering]].

## Security and Trust

Security isn't a late-stage add-on for LLM systems because the model receives
instructions from users and sometimes from retrieved documents. That creates
new attack paths around prompt injection, data exfiltration, hallucinated
answers, and overconfident users.

Maria's
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]
episode is the clearest security source. At 9:28, she describes a large-scale
chatbot hacking exercise. At 13:20, she covers data exfiltration through prompt
overload and knowledge-base retrieval. At 16:15, she recommends output
validation, query analysis, and layered defenses. At 17:00, she argues for
non-LLM classifiers where they're harder to manipulate than generative models.

Ivan raises related risks in
[[podcast:nlp-team-hiring-and-production-mlops|Lead NLP Teams]].
At 43:05, he discusses GPT-3 risks around cost and control. He also covers bias
and privacy.
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
