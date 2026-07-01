---
layout: wiki
title: "LLMs"
summary: "How DataTalks.Club guests discuss large language models as language, retrieval, agent, evaluation, production, and security components."
related:
  - AI Tooling
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - RAG vs Fine-Tuning
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

The archive doesn't treat an LLM as a finished product. Guests usually place
the model inside a larger system with prompts, data pipelines, and retrieval.
They also add evaluation, deployment, security checks, and human review. That
makes LLMs part of [NLP]({{ '/wiki/nlp/' | relative_url }}),
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}),
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}), and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

## Common Definition

The common definition across the podcast is practical. An LLM is a general
language model that can be prompted for many language tasks. Teams then adapt it
with context, examples, and retrieval. They can also use fine-tuning or tools.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the most direct
production definition in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 10:24, she separates generative and non-generative language models and
connects modern LLMs to transformers. At 14:45, she explains why they matter
for unstructured text at scale.

[Ivan Bilan]({{ '/people/ivanbilan/' | relative_url }}) connects LLMs to older
NLP work in
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}).
His 34:57 section walks through the traditional NLP pipeline. The team labels
data, designs the task, tests behavior, and deploys the system. At 38:55, he
contrasts that pipeline with GPT-3-style prompting, where a model can produce
useful behavior from a prompt instead of a task-specific training pipeline.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) gives
the builder's definition in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 9:28, he lists everyday uses such as summaries, translation, and CSV
workflows. At 11:11, he moves from the model to prompting practice: role
prompts. He also covers structured output and timestamps.

## Guest Differences

Guests agree that LLMs are useful, but they differ on the first risk to solve.

Meryem starts from deployment choice. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
the 16:48 section compares open-source and API models through control, privacy,
and fine-tuning. At 18:46, she adds model-drift risk when an API provider
changes behavior behind the scenes. Her framing makes LLM adoption an
[AI infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) and
[production]({{ '/wiki/production/' | relative_url }}) decision.

Ivan starts from NLP team design. In
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}),
the 43:05 section warns about GPT-3 limitations around cost and control. He
also names bias and privacy risks. At 46:10, he treats GPT-3 as useful for MVPs but not a replacement for
in-house pipelines when the team needs control.

[Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }}) starts from
applied research. In
[Applied LLM Research]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}),
the 10:15 section focuses on long-context evaluation. At 12:36, she describes
performance drops around 32k-64k context in a financial benchmark. Her view
keeps LLM quality tied to empirical tests, not advertised context length.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) starts from
trust and safety. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 11:38 section covers hallucinations, legal exposure, and financial
incidents. At 16:15, she recommends layered defenses. At 17:00, she adds
non-LLM classifiers when a generative model is too easy to manipulate.

## LLM Use Cases

The podcast's LLM use cases start with practical language work. Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
episode uses summaries, translation, and CSV handling as concrete examples. It
also covers transcript workflows and developer assistants. The 12:22 section
covers transcript automation with tools such as Gemini, Descript, and Loom. The
31:56 section discusses developer tools and assistants such as GitHub Copilot,
Cursor, and IDE agents.

LLMs also appear as product interfaces. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
Maria discusses chatbots and controlled machine translation. She also covers
moderation support and human review. Her 25:34 section keeps the model in an assistant role where
people review high-risk outputs.

Agents are a separate use case because the model does more than answer once.
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) defines
that boundary in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 11:00, she connects agents to autonomy, objectives, and LLMs. At 12:31, she
adds tools, memory, and knowledge stores. That's why the
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}) page separates agent
workflow design from ordinary prompting.

## RAG and Fine-Tuning

The archive draws a strong line between changing model behavior and adding
current knowledge.

Meryem explains this split in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 26:30, she frames fine-tuning as specialization and domain adaptation. She
also discusses tone and format control. At 40:46 and 42:02, she recommends retrieval for changing
knowledge. The team can index documents and retrieve relevant passages without
retraining the model for every fact update.

[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}) uses the
same split. Retrieval helps when the system needs fresh documents, citations,
proprietary knowledge, or reviewable evidence. Fine-tuning helps when the model
should behave differently. It can also help with a repeated output style or a
repeated task.

Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
episode gives the implementation path. At 44:26, he presents RAG with chunking
and embeddings as a quick business win. At 48:20, he shows why chunking
strategy matters. Chunk size, sliding windows, and context rot decide what the
model sees.

Lavanya's
[Applied LLM Research]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }})
episode adds a research reason to prefer retrieval in many long-document
settings. At 14:54, she discusses chunking, retrieval, and summarization for
large documents after describing long-context performance limits.

## Evaluation

LLM evaluation in the podcast is task-specific. A team shouldn't assume that a
model's general benchmark score proves its workflow.

Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
episode is the main practical source. At 13:56, he introduces a
generator-evaluator loop for automated quality control. At 23:00, he
discusses gold tests, cost, and representativeness. He also covers how large
the test set should be. At 26:43, he uses
failure analysis to decide whether retrieval, prompts, or data should change.

Ranjitha extends that logic to agents in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 51:17, she recommends custom datasets and system benchmarks. At 53:20, she
adds mocked tools, integration tests, and regression tests. At 56:02, she
emphasizes outcome assertions instead of exact path matching because valid
agent runs may take different tool-call paths.

Lavanya's long-context work shows why evaluation has to match the document
task. In
[Applied LLM Research]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}),
the 10:15 and 12:36 sections test long-context models in a financial setting
instead of relying on context-window size alone.

Use [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for evaluation patterns and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
for retrieval quality when RAG depends on search.

## Production

Production LLM systems need normal software and ML operations. Teams have to
plan deployment, latency control, and cost control. They also need monitoring,
observability, rollback plans, and ownership.

Meryem's
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
episode makes serving explicit. The 25:26 section covers model size,
compression, and inference optimization. At 49:44, she separates prototyping
with GPT-3.5 or GPT-4 APIs from production choices around open-source LLMs. At
51:35, she discusses latency and cost. She also covers self-hosting and
hardware choices.

Ranjitha adds production workflow design. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
the 21:21 section names context engineering as a core design task. At 29:30,
she gives the RAG reality check around latency, cost, and noisy inputs. At
31:38 and 32:48, she discusses reworking retrieval backends. She also covers
chunking, metadata, and wrappers so the system gives the LLM useful context.

Hugo adds operational feedback loops. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
the 27:38 section covers logging, traces, and debuggable MVPs. Those practices
connect LLM work to [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
and [AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}).

## Security and Trust

Security isn't a late-stage add-on for LLM systems because the model receives
instructions from users and sometimes from retrieved documents. That creates
new attack paths around prompt injection, data exfiltration, hallucinated
answers, and overconfident users.

Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode is the clearest security source. At 9:28, she describes a large-scale
chatbot hacking exercise. At 13:20, she covers data exfiltration through prompt
overload and knowledge-base retrieval. At 16:15, she recommends output
validation, query analysis, and layered defenses. At 17:00, she argues for
non-LLM classifiers where they're harder to manipulate than generative models.

Ivan raises related risks in
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}).
At 43:05, he discusses GPT-3 risks around cost and control. He also covers bias
and privacy.
Those concerns connect LLMs to
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}),
[security]({{ '/wiki/security/' | relative_url }}), and
[privacy engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}).

Security also affects retrieval because a RAG system may retrieve confidential
or poisoned documents. The LLM can then expose or amplify them. Teams need
access controls before retrieval, validation after generation, and audit trails
for high-risk workflows.

## Related Pages

These pages cover the surrounding techniques, roles, and production concerns.

- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG]({{ '/wiki/rag/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [AI Agents]({{ '/wiki/ai-agents/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [LLM Tools]({{ '/guides/llm-tools/' | relative_url }})
- [LLM System Design Interview]({{ '/guides/llm-system-design-interview/' | relative_url }})
