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

[[person:meryemarik|Meryem Arik]] gives the clearest
model-level distinction in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 10:24, she separates generative models from non-generative models, and at
11:44 she connects that distinction to model selection for classification and
generation tasks. That framing matters because not every AI product needs a
generator. Some problems still fit classifiers, retrieval systems, or
deterministic software better.
[[book:20241017-build-large-language-model-from-scratch|Build a Large Language Model (From Scratch)]]
by Sebastian Raschka shows the internals of the transformer architectures that
power these generative models.
[[book:20211108-generative-ai-with-python-and-tensorflow-2|Generative AI with Python and TensorFlow 2]]
by Joseph Babcock and Raghav Bali is a practitioner reference for the underlying deep learning architectures (GANs, VAEs, transformers) behind generative systems.

## From Model Output to Product Systems

Guests usually use the term more narrowly than the market does. They treat
generative AI as a product or engineering capability. The model generates an
output. Teams add retrieval and tools around it. They also add validation,
monitoring, and human review.

[[person:bartoszmikulski|Bartosz Mikulski]] makes this
engineering view explicit in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
At 21:46, he discusses invisible AI inside workflows such as augmented
generation and review analysis. At 25:13 and 28:16, he moves from prompt
examples to evaluation. Formatting, quality, and cost become part of prompt
work. The model is only one component.

The useful product also needs data pipelines, prompts, and APIs. It needs
caching, latency controls, and tests too.
In [[Business Intelligence]],
the same production boundary appears when teams add natural-language querying
and text-to-SQL. Retrieval and LLM summaries sit on top of governed metrics.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] gives
a similar working definition in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 9:28, he lists everyday LLM use cases such as summaries, translation, and
CSV workflows. At 13:56, he describes a generator-evaluator check for quality
control. At 23:00 and 26:43, he shifts from prompting to evaluation sets,
failure analysis, and retrieval fixes.

## Trust Boundaries

Guests differ less on whether generative AI is useful and more on where teams
should put the trust boundary.

[[person:mariasukhareva|Maria Sukhareva]] treats the
chatbot as a risky interface in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
At 9:28, she discusses findings from a large chatbot hacking exercise. At
11:38 and 13:20, she covers hallucinations, legal exposure, and financial
incidents. She also covers data exfiltration through prompts and knowledge-base
retrieval.

For her, a usable generative AI system includes
[[security]],
[[AI red teaming]], and output
validation. It also includes human review.

Meryem focuses on deployment choices. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
she compares open-source and API models at 16:48. At 18:46, she warns about
hidden API model changes. At 25:26, she explains why model size, compression,
and inference optimization matter.

Her version of generative AI depends on control, privacy, latency, and cost. It
also depends on the team's ability to run the model reliably.

[[person:micheallanham|Micheal Lanham]] connects
generative AI to agent systems in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
At 20:57 and 23:48, he discusses task decomposition, sequential flows, and
manager agents. At 38:57, he applies generative AI to games through generated
levels and replayability. His emphasis is orchestration: the model generates,
but the surrounding agent design decides how far the system can go.

## Product Uses

In these episodes, generative AI works best when the product gives the model a
bounded job and a reviewable output.

Bartosz describes augmented generation and review analysis at 21:46 in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
Those use cases fit internal tools because the model drafts or classifies
within an existing business workflow. At 56:17, he says teams use AI-assisted
writing to draft and rewrite while preserving voice. The model doesn't replace
the person who owns the final text.

Hugo's examples in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
are also practical and bounded. At 9:28 and 12:22, he covers summaries and
translation. He also covers CSV workflows and transcript processing. Automation
tools include Gemini, Descript, and Loom.

At 53:34, he uses an email assistant built with the Gmail API and RAG as a
concrete product design. The product doesn't rely on chat alone. It connects
model output to documents, APIs, and a user's existing work.

Maria adds another product category: language support. In
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]],
she discusses AI-augmented translation at 29:53, prompt-customized machine
translation at 32:28, and low-resource language challenges at 53:01. These
examples connect generative AI to [[NLP]] and
data quality, especially when spelling, scripts, or domain language are
inconsistent.

## RAG and Grounding

Guests treat
[[retrieval-augmented-generation|retrieval-augmented generation]]
as the default answer when the model needs changing or private knowledge.

Meryem gives the deployment argument in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 40:46, she recommends retrieval over continuous retraining when knowledge
changes. At 42:02 and 46:42, she explains grounding answers with indexed
documents and injected passages. She also covers summarizers and retrieval
layers. At 48:01, she
connects this design to
[[embeddings]], vector indexes, and
semantic search.

Hugo gives the product-building version in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 44:26, he frames RAG as a quick path to business wins. At 48:20, he compares
chunking strategies such as fixed length and sliding windows. At 50:19, he
draws the boundary between RAG and agent tool calls. Use
[[rag-vs-fine-tuning|RAG vs fine-tuning]] for that
tradeoff in more detail.

## Production Engineering

Generative AI production work starts when the demo has to survive real users.
Teams then have to handle cost limits, latency targets, data drift, and
repeatable evaluation.

Bartosz's
[[podcast:production-ready-ai-engineering|Production AI Engineering]]
episode connects generative AI to [[data engineering]].
At 18:38, he discusses preprocessing and fine-tuning data. At 28:16, prompt
formatting plus examples affect quality and cost. At 30:00 and 31:45,
prompt compression and prompt caching become system design tools.

At 41:04, Bartosz uses a Chrome extension with a backend AI integration design.
That example shows why the interface, backend, and model call need to be
designed together.

Meryem covers the model-serving side in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 49:44 and 51:35, she compares prototyping with API models against running
open-source models. Latency, cost, self-hosting, and hardware choices become
the production constraints. Use
[[LLM Production Patterns]]
for the deployment choices that appear across these episodes.

## Security and Trust

Generative AI systems can fail in ways that normal application code doesn't.
The output may be plausible but wrong, and the prompt can become an attack
surface.

Maria's
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]
episode is the main DataTalks.Club reference for this. At 16:15, she recommends
layered defenses such as output validation and query analysis. At 17:00, she
uses non-LLM classifiers as a more robust option for some safety checks.
At 18:01, she connects hallucinations to user trust and adoption risk. At
25:34 and 27:13, she describes human-in-the-loop review and AI as an assistant
rather than a final authority.

This is where generative AI overlaps with
[[Responsible AI and Governance]].
Guests repeatedly warn against "add a chatbot and trust it." Teams define the
task and narrow the permissions. They validate the output, keep humans in the
right places, and monitor how the system behaves.

## Evaluation

Prompt quality isn't enough, so guests repeatedly move from prompt design to
test cases and failure categories. They also add monitoring and review.

Hugo describes this shift in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 13:56, the generator-evaluator check uses one model or evaluator to look at
another output. At 23:00, he discusses gold evaluation sets and their cost. He
also covers set size and representativeness. At 26:43, he categorizes failures so teams can decide
whether to fix retrieval, prompts, data or product scope.

Those practices are covered in more depth in
[[LLM Evaluation Workflows]].

Meryem makes the same point in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 53:34, she discusses gold-standard examples and output-driven evaluation.
At 56:39, she separates classification metrics from generative evaluation and
human judgment.

Micheal adds monitoring for agent systems in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
At 57:39, feedback pipelines and tools such as Arize Phoenix appear as part of
agent evaluation.

## Tools and Agent Workflows

Guests discuss generative AI tooling across IDE assistants, browser extensions,
Slack assistants, and email assistants. They also cover search tools and agent
frameworks.

Bartosz discusses coding assistants in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
At 42:05 and 44:38, he compares Cursor, GitHub Copilot, and alternatives. At
47:19, he discusses search-focused assistants and tool selection.

These examples belong with [[LLM tools]].
The choice is often less about the model and more about where the tool fits in
the developer's work.

Hugo and Micheal cover the agent side. Hugo discusses embedded Slack agents at
33:14 and actions beyond chat at 40:12 in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 56:21, he gives a four-step framework for agents. Micheal discusses the
OpenAI Agents SDK and MCP integration at 31:31 in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
At 33:25 and 35:42, Micheal covers sequential thinking servers and coding
agents in game development.

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
