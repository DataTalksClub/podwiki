---
layout: wiki
title: "Generative AI"
summary: "How DataTalks.Club guests cover generative AI as applied language, chatbot, agent, coding, and content-generation systems."
related:
  - LLMs
  - LLM Production Patterns
  - NLP
  - Agent Engineering
  - Business Intelligence
  - Responsible AI and Governance
---

Generative AI covers systems that produce new outputs from prompts and context.
Those outputs can be text, code, images, or structured data. They can also be
summaries, translations, recommendations, or actions. DataTalks.Club guests
mostly discuss the term through [[LLMs]] and
chatbots. It also appears through
[[retrieval-augmented-generation|retrieval-augmented generation]],
coding assistants, workflow automation, and
[[agent-engineering|AI agents]].

[[person:meryemarik|Meryem Arik]] gives the clearest model-level distinction:
generative models separate from non-generative models, and that distinction
drives model selection for classification and generation tasks
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Not every AI product needs a generator; some problems still fit classifiers,
retrieval systems, or deterministic software better.
[[book:20241017-build-large-language-model-from-scratch|Build a Large Language Model (From Scratch)]]
by Sebastian Raschka shows the internals of the transformer architectures that
power these generative models.
[[book:20211108-generative-ai-with-python-and-tensorflow-2|Generative AI with Python and TensorFlow 2]]
by Joseph Babcock and Raghav Bali is a practitioner reference for the underlying deep learning architectures (GANs, VAEs, transformers) behind generative systems.

## From Model Output to Product Systems

The term is often used more narrowly than the market does, as a product or
engineering capability. The model generates an output, and teams add retrieval
and tools around it, along with validation, monitoring, and human review.

[[person:bartoszmikulski|Bartosz Mikulski]] makes this engineering view
explicit: invisible AI sits inside workflows such as augmented generation and
review analysis, and prompt work moves from examples to evaluation, with
formatting, quality, and cost part of it
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). The
model is only one component.

The useful product also needs data pipelines, prompts, and APIs. It needs
caching, latency controls, and tests too.
In [[Business Intelligence]],
the same production boundary appears when teams add natural-language querying
and text-to-SQL. Retrieval and LLM summaries sit on top of governed metrics.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] gives a similar working
definition: everyday LLM use cases such as summaries, translation, and CSV
workflows; a generator-evaluator check for quality control; and a shift from
prompting to evaluation sets, failure analysis, and retrieval fixes
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

## Trust Boundaries

Guests differ less on whether generative AI is useful and more on where teams
should put the trust boundary.

[[person:mariasukhareva|Maria Sukhareva]] treats the chatbot as a risky
interface, drawing on findings from a large chatbot hacking exercise:
hallucinations, legal exposure, financial incidents, and data exfiltration
through prompts and knowledge-base retrieval
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

In this account, a usable generative AI system includes
[[security]],
[[AI red teaming]], output
validation, and human review.

Meryem focuses on deployment choices: open-source versus API models, hidden API
model changes, and why model size, compression, and inference optimization
matter
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

That version of generative AI depends on control, privacy, latency, cost, and
the team's ability to run the model reliably.

[[person:micheallanham|Micheal Lanham]] connects generative AI to agent systems
through task decomposition, sequential flows, and manager agents, and applies it
to games via generated levels and replayability
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]). The
emphasis is orchestration: the model generates, but the surrounding agent design
decides how far the system can go.

## Product Uses

In these episodes, generative AI works best when the product gives the model a
bounded job and a reviewable output.

Augmented generation and review analysis fit internal tools because the model
drafts or classifies within an existing business workflow, and AI-assisted
writing drafts and rewrites while preserving voice
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). The
model doesn't replace the person who owns the final text.

Hugo's examples are also practical and bounded: summaries, translation, CSV
workflows, and transcript processing, with automation tools such as Gemini,
Descript, and Loom
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

An email assistant built with the Gmail API and RAG is a concrete product design
that doesn't rely on chat alone; it connects model output to documents, APIs,
and a user's existing work
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Maria adds another product category: language support, spanning AI-augmented
translation, prompt-customized machine translation, and low-resource language
challenges
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
These examples connect generative AI to [[NLP]] and
data quality, especially when spelling, scripts, or domain language are
inconsistent.

## RAG and Grounding

[[retrieval-augmented-generation|Retrieval-augmented generation]]
is the default answer when the model needs changing or private knowledge.

The deployment argument favors retrieval over continuous retraining when
knowledge changes, grounding answers with indexed documents and injected
passages, plus summarizers and retrieval layers, connecting the design to
[[embeddings]], vector indexes, and semantic search
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

The product-building version frames RAG as a quick path to business wins,
compares chunking strategies such as fixed length and sliding windows, and draws
the boundary between RAG and agent tool calls
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Use [[rag-vs-fine-tuning|RAG vs fine-tuning]] for that
tradeoff in more detail.

## Production Engineering

Generative AI production work starts when the demo has to survive real users.
Teams then have to handle cost limits, latency targets, data drift, and
repeatable evaluation.

Production AI engineering connects generative AI to [[data engineering]]:
preprocessing and fine-tuning data, prompt formatting plus examples affecting
quality and cost, and prompt compression and caching as system design tools
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

A Chrome extension with a backend AI integration shows why the interface,
backend, and model call need to be designed together
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

The model-serving side compares prototyping with API models against running
open-source models, where latency, cost, self-hosting, and hardware choices
become the production constraints
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Use [[LLM Production Patterns]]
for the deployment choices that appear across these episodes.

## Security and Trust

Generative AI systems can fail in ways that normal application code doesn't.
The output may be plausible but wrong, and the prompt can become an attack
surface.

The main DataTalks.Club reference here recommends layered defenses such as
output validation and query analysis, non-LLM classifiers as a more robust
option for some safety checks, and human-in-the-loop review with AI as an
assistant rather than a final authority; hallucinations connect directly to
user trust and adoption risk
([[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

This is where generative AI overlaps with
[[Responsible AI and Governance]].
The repeated warning is against "add a chatbot and trust it." Teams define the
task and narrow the permissions, validate the output, keep humans in the right
places, and monitor how the system behaves.

## Evaluation

Prompt quality isn't enough, so the work repeatedly moves from prompt design to
test cases and failure categories, plus monitoring and review.

The generator-evaluator check uses one model or evaluator to look at another
output; gold evaluation sets bring cost, size, and representativeness tradeoffs;
and categorizing failures lets teams decide whether to fix retrieval, prompts,
data, or product scope
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Those practices are covered in more depth in
[[LLM Evaluation Workflows]].

The same point covers gold-standard examples and output-driven evaluation,
separating classification metrics from generative evaluation and human judgment
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

Monitoring for agent systems adds feedback pipelines and tools such as Arize
Phoenix as part of agent evaluation
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Tools and Agent Workflows

Generative AI tooling spans IDE assistants, browser extensions, Slack
assistants, email assistants, search tools, and agent frameworks.

Coding assistants compare Cursor, GitHub Copilot, and alternatives, alongside
search-focused assistants and tool selection
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

These examples belong with [[LLM tools]].
The choice is often less about the model and more about where the tool fits in
the developer's work.

On the agent side, embedded Slack agents, actions beyond chat, and a four-step
framework for agents appear in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
while the OpenAI Agents SDK, MCP integration, sequential thinking servers, and
coding agents in game development appear in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].

Use [[Agent Engineering]] for
workflow design and tool calls, plus memory, orchestration, and evaluation.

## Related Pages

These pages cover the nearby concepts that generative AI pages link to most
often.

- [[LLMs]]
- [[NLP]]
- [[Prompt Engineering]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
- [[LLM Production Patterns]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[Responsible AI and Governance]]
- [[AI Red Teaming]]
