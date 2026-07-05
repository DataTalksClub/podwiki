---
layout: wiki
title: "Generative AI"
summary: "Generative AI as applied language, chatbot, agent, coding, and content-generation systems."
related:
  - LLMs
  - LLM Production Patterns
  - NLP
  - Agent Engineering
  - Multimodal LLMs
  - Business Intelligence
  - Responsible AI and Governance
---

Generative AI systems produce new outputs from prompts and context. Common
outputs include text and code. They also include images and structured data.

Sandra Kublik frames generative AI through GPT applications. Later
AI-engineering interviews connect the same capability to summaries,
translations, recommendations, and coding assistants. They also connect it to
workflow automation and [[Agent Engineering]]
[[book:20230306-gpt-3=>GPT-3]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

Most examples sit close to [[LLMs]], chatbots,
[[retrieval-augmented-generation=>retrieval-augmented generation]], and
production AI systems. Use [[LLM Production Patterns]] when the question is
how teams operate the model, context, evaluation, and guardrails around a
generated output.

The model-level distinction matters because generative and non-generative models
fit different tasks. Some products need a bounded decision rather than a new
output. Classification and retrieval may fit those products better.
Deterministic software may also
fit.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
[[book:20241017-build-large-language-model-from-scratch=>Build a Large Language Model (From Scratch)]]
covers the transformer internals behind modern language models.
[[book:20211108-generative-ai-with-python-and-tensorflow-2=>Generative AI with Python and TensorFlow 2]]
covers deep learning architectures such as GANs, VAEs, and transformers.

## Model and System Boundary

Generative AI isn't just the model call. Product teams usually wrap the
generator with data pipelines and prompts. They also add APIs and retrieval.
They add validation and monitoring. They also manage latency, cost, and human
review.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Internal AI features make this visible through augmented generation, review
analysis, and writing support. The model is only one
component in the wider
system.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Teams use the same production boundary in [[Business Intelligence]] when they
add natural-language querying and text-to-SQL on top of governed metrics.
Everyday LLM workflows add another version of the same boundary. The examples
include summaries, translation, CSV processing, and transcript tooling. They
also include generator-evaluator checks, evaluation sets, failure analysis, and
retrieval fixes.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

## Trust Boundaries

Generative AI is useful for bounded tasks, but teams draw the trust boundary in
different places.

Chatbot-heavy systems put the trust boundary at the interface. A large chatbot
hacking exercise surfaced hallucinations, legal exposure, and financial
incidents. It also showed how prompts and knowledge-base retrieval can expose
data. For chatbot products, [[security]] and [[AI Red Teaming]] sit inside the
product. So do output validation and human
review.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Model deployment puts the boundary around control, privacy, and latency. Cost
and operational reliability also matter. Open-source and API models have
different risks. Hidden API model changes can affect the product. Model size, compression,
inference optimization, and hardware choices also affect the final
system.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Agentic systems put the boundary around orchestration. Task decomposition,
sequential flows, and manager agents depend on the surrounding
[[Agent Engineering]] design. Game teams also rely on that design for generated
levels and replayability. The model generates, but the agent design sets how far the
system can act.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Product Uses

Generative AI works best in these examples when the product gives the model a
bounded job and a reviewable output.

Internal tools can use augmented generation and review analysis when the model
drafts or classifies within an existing business workflow. Writing assistants
can draft and rewrite while preserving
voice.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
The model doesn't replace the person who owns the final text.

In UnrealMe, Pauline Clavelloux started from a DreamBooth-inspired
selfie-to-art idea and then compared API fine-tuning with running GPUs herself.
Her comparison put product speed, cost, and infrastructure burden next to model
capability. The same API-versus-self-hosted boundary appears in larger
[[LLM Production Patterns]] pages
[[cite:data-scientist-and-indie-hacker-bootstrapping-side-projects@23:33=>Indie Hacking Side Projects]]
[[cite:data-scientist-and-indie-hacker-bootstrapping-side-projects@25:48=>Indie Hacking Side Projects]].
That image-generation example is also where generative AI connects to
[[multimodal-llms=>multimodal LLMs]].

Other bounded use cases include summaries, translation, and CSV workflows.

Transcript processing can use Gemini and Descript. Loom appears in the same
workflow.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Use [[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
for the personal workflow version of these use cases.

An email assistant built with the Gmail API and RAG is a concrete product design
that doesn't rely on chat alone. It connects model output to documents, APIs,
and a person's existing work.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Language support is another product category. Translation products connect
generative AI to [[NLP]] and data quality through AI augmentation and prompt
customization. Low-resource language work makes that connection especially visible
when spelling, scripts, or domain language are
inconsistent.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## RAG and Grounding

[[retrieval-augmented-generation=>Retrieval-augmented generation]]
is the default answer when the model needs changing or private knowledge.

When knowledge changes, retrieval can beat continuous retraining. The system
grounds answers with indexed documents and injected passages. Summarizers and
retrieval layers then connect the design to [[embeddings]], vector indexes, and
semantic search.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

RAG can create product wins.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Teams still choose chunking strategies such as fixed length or sliding windows.
They also draw the boundary between RAG and agent tool calls.
Use [[rag-vs-fine-tuning=>RAG vs fine-tuning]] for that
tradeoff in more detail.

## Production Engineering

Generative AI production work starts when the demo has to survive real users.
Teams then have to handle cost limits, latency targets, data drift, and
repeatable evaluation.

Production AI engineering connects generative AI to [[data engineering]]. Teams
preprocess data, fine-tune data, and format prompts with examples. Prompt
compression and caching become system design
tools.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

A Chrome extension with a backend AI integration shows why the interface,
backend, and model call need to be designed
together.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Production teams can prototype with API models or run open-source models
themselves. When they move toward reliable serving, they have to manage latency
and cost. They also have to manage self-hosting and hardware choices.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
Use [[LLM Production Patterns]]
for the deployment choices that appear across these episodes.

## Security and Trust

Generative AI systems can fail in ways that normal application code doesn't.
The output may be plausible but wrong, and the prompt can become an attack
surface.

Teams use layered defenses such as output validation and query analysis. They
can use non-LLM classifiers for some safety checks. Human-in-the-loop review
keeps AI in an assistant role rather than a final-authority role. Hallucinations
connect directly to user trust and adoption
risk.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Generative AI overlaps here with [[Responsible AI and Governance]]. Teams
shouldn't add a chatbot and trust it by default. They define the task and narrow
the permissions. They validate the output, keep humans in the right places, and
monitor how the system behaves.

## Evaluation

Prompt quality isn't enough, so the work repeatedly moves from prompt design to
test cases and failure categories, plus monitoring and review.

The generator-evaluator check uses one model or evaluator to look at another
output. Gold evaluation sets bring cost, size, and representativeness tradeoffs.
Categorizing failures lets teams decide whether to fix retrieval or prompts. It
also separates data issues from product scope, which belongs with
[[LLM Evaluation Workflows]].[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Deployment work also uses gold-standard examples and output-driven evaluation,
with a boundary between classification metrics, generative evaluation, and human
judgment.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Monitoring for agent systems adds feedback pipelines and tools such as Arize
Phoenix as part of agent
evaluation.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Tools and Agent Workflows

Generative AI tooling spans IDE assistants, browser extensions, and Slack
assistants. It also includes email assistants, search tools, and agent
frameworks.

Coding assistants compare Cursor, GitHub Copilot, and alternatives, alongside
search-focused assistants and tool
selection.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

These examples connect generative AI to [[LLM tools]]. The choice is often less
about the model and more about where the tool fits in the developer's work.

On the agent side, embedded Slack agents and actions beyond chat appear in
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
That episode also covers a four-step framework for agents. Another agent
discussion covers the OpenAI Agents SDK and MCP integration. It also covers
sequential thinking servers and coding agents in game development
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]].

Use [[Agent Engineering]] for
workflow design and tool calls, plus memory, orchestration, and evaluation.

## Related Pages

These pages cover the nearby concepts that generative AI pages link to most
often.

- [[LLMs]]
- [[NLP]]
- [[Prompt Engineering]]
- [[multimodal-llms=>Multimodal LLMs]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[LLM Production Patterns]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[Responsible AI and Governance]]
- [[AI Red Teaming]]
