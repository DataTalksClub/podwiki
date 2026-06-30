---
layout: wiki
title: "Generative AI"
summary: "How the podcast archive covers generative AI as applied language, chatbot, agent, coding, and content-generation systems."
related:
  - LLMs
  - LLM Production Patterns
  - NLP
  - Agent Engineering
  - Responsible AI and Governance
---

## Definition

Generative AI covers systems that produce new outputs from prompts and context.
Those outputs can be text, code, images, or structured data. They can also be
summaries, translations, recommendations, or actions. In the DataTalks.Club
archive, the term mostly appears through [LLMs]({{ '/wiki/llms/' | relative_url }})
and chatbots. It also appears through
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
coding assistants, workflow automation, and
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}).

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the clearest
model-level distinction in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 10:24, she separates generative models from non-generative models, and at
11:44 she connects that distinction to model selection for classification and
generation tasks. That framing matters because not every AI product needs a
generator. Some problems still fit classifiers, retrieval systems, or
deterministic software better.

## Common Definition

The archive's practical definition is narrower than the market term. Guests
usually treat generative AI as a product or engineering capability. The system
uses a model to generate an output. Teams then add retrieval and tooling. They
also add validation, monitoring, and human review.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) makes this
engineering view explicit in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 21:46, he discusses invisible AI inside workflows such as augmented
generation and review analysis. At 25:13 and 28:16, he moves from prompt
examples to evaluation. Formatting, quality, and cost become part of prompt
work. The model is only one component.

The useful product also needs data pipelines, prompts, and APIs. It also needs
caching, latency controls, and tests.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) gives
a similar working definition in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 9:28, he lists everyday LLM use cases such as summaries, translation, and
CSV workflows. At 13:56, he describes a generator-evaluator check for quality
control. At 23:00 and 26:43, he shifts from prompting to evaluation sets,
failure analysis, and retrieval fixes.

## Guest Differences

Guests differ less on whether generative AI is useful and more on where teams
should put the trust boundary.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) treats the
chatbot as a risky interface in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 9:28, she discusses findings from a large chatbot hacking exercise. At
11:38 and 13:20, she covers hallucinations, legal exposure, and financial
incidents. She also covers data exfiltration through prompts and knowledge-base
retrieval. Her
definition of a usable generative AI system includes
[security]({{ '/wiki/security/' | relative_url }}),
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}), output
validation, and human review.

Meryem focuses on deployment choices. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she compares open-source and API models at 16:48. At 18:46, she warns about
hidden API model changes. At 25:26, she explains why model size, compression,
and inference optimization matter.

Her version of generative AI depends on control, privacy, latency, and cost. It
also depends on the team's ability to run the model reliably.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) connects
generative AI to agent systems in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 20:57 and 23:48, he discusses task decomposition, sequential flows, and
manager agents. At 38:57, he applies generative AI to games through generated
levels and replayability. His emphasis is orchestration: the model generates,
but the surrounding agent design decides how far the system can go.

## Product Uses

Generative AI works best in the archive when the product gives the model a
bounded job and a reviewable output.

Bartosz describes augmented generation and review analysis at 21:46 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
Those use cases fit internal tools because the model drafts or classifies
within an existing business process. At 56:17, he says teams use AI-assisted
writing to draft and rewrite while preserving voice. The model doesn't replace
the person who owns the final text.

Hugo's examples in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
are also practical and bounded. At 9:28 and 12:22, he covers summaries and
translation. He also covers CSV workflows and transcript processing. Automation
tools include Gemini, Descript, and Loom.

At 53:34, he uses an email assistant built with the Gmail API and RAG as a
concrete product design. The product doesn't rely on chat alone. It connects
model output to documents, APIs, and a user's existing work.

Maria adds another product category: language support. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
she discusses AI-augmented translation at 29:53, prompt-customized machine
translation at 32:28, and low-resource language challenges at 53:01. These
examples connect generative AI to [NLP]({{ '/wiki/nlp/' | relative_url }}) and
data quality, especially when spelling, scripts, or domain language are
inconsistent.

## RAG and Grounding

The archive treats
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
as the default answer when the model needs changing or private knowledge.

Meryem gives the deployment argument in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46, she recommends retrieval over continuous retraining when knowledge
changes. At 42:02 and 46:42, she explains grounding answers with indexed
documents and injected passages. She also covers summarizers and retrieval
layers. At 48:01, she
connects this design to
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), vector indexes, and
semantic search.

Hugo gives the product-building version in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 44:26, he frames RAG as a quick path to business wins. At 48:20, he compares
chunking strategies such as fixed length and sliding windows. At 50:19, he
draws the boundary between RAG and agent tool calls. Use
[RAG vs fine-tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) for that
tradeoff in more detail.

## Production Engineering

Generative AI production work starts when the demo has to survive real users.
Teams then have to handle cost limits, latency targets, data drift, and
repeatable evaluation.

Bartosz's
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})
episode connects generative AI to [data engineering]({{ '/wiki/data-engineering/' | relative_url }}).
At 18:38, he discusses preprocessing and fine-tuning data. At 28:16, prompt
formatting plus examples affect quality and cost. At 30:00 and 31:45,
prompt compression and prompt caching become system design tools.

At 41:04, Bartosz uses a Chrome extension with a backend AI integration design.
That example shows why the interface, backend, and model call need to be
designed together.

Meryem covers the model-serving side in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 49:44 and 51:35, she compares prototyping with API models against running
open-source models. Latency, cost, self-hosting, and hardware choices become
the production constraints. Use
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for the deployment choices that appear across these episodes.

## Security and Trust

Generative AI systems can fail in ways that normal application code doesn't.
The output may be plausible but wrong, and the prompt can become an attack
surface.

Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode is the archive's main reference for this. At 16:15, she recommends
layered defenses such as output validation and query analysis. At 17:00, she
uses non-LLM classifiers as a more robust option for some safety checks.
At 18:01, she connects hallucinations to user trust and adoption risk. At
25:34 and 27:13, she describes human-in-the-loop review and AI as an assistant
rather than a final authority.

This is where generative AI overlaps with
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).
The archive's repeated guidance isn't "add a chatbot and trust it." Teams
define the task and narrow the permissions. They validate the output, keep
humans in the right places, and monitor how the system behaves.

## Evaluation

Prompt quality isn't enough, so guests repeatedly move from prompt design to
test cases and failure categories. They also add monitoring and review.

Hugo describes this shift in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 13:56, the generator-evaluator check uses one model or process to look at
another output. At 23:00, he discusses gold evaluation sets and their cost. He
also covers set size and representativeness. At 26:43, he categorizes failures so teams can decide
whether to fix retrieval, prompts, data or product scope.

This connects directly to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

Meryem makes the same point in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 53:34, she discusses gold-standard examples and output-driven evaluation.
At 56:39, she separates classification metrics from generative evaluation and
human judgment.

Micheal adds monitoring for agent systems in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 57:39, feedback pipelines and tools such as Arize Phoenix appear as part of
agent evaluation.

## Tools and Agent Workflows

Generative AI tooling in the archive spans IDE assistants, browser extensions,
Slack assistants, and email assistants. It also includes search tools and agent
frameworks.

Bartosz discusses coding assistants in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 42:05 and 44:38, he compares Cursor, GitHub Copilot, and alternatives. At
47:19, he discusses search-focused assistants and tool selection.

These examples belong with [LLM tools]({{ '/guides/llm-tools/' | relative_url }}).
The choice is often less about the model and more about where the tool fits in
the developer's work.

Hugo and Micheal cover the agent side. Hugo discusses embedded Slack agents at
33:14 and actions beyond chat at 40:12 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 56:21, he gives a four-step framework for agents. Micheal discusses the
OpenAI Agents SDK and MCP integration at 31:31 in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 33:25 and 35:42, Micheal covers sequential thinking servers and coding
agents in game development.

Use [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) for
workflow design and tool calls, plus memory, orchestration, and evaluation.

## Related Pages

These pages cover the nearby concepts that generative AI pages link to most
often.

- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
