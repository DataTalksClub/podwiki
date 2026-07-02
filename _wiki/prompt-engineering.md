---
layout: wiki
title: "Prompt Engineering"
summary: "Practical prompt engineering patterns from DataTalks.Club episodes: role prompts, examples, structured output, evaluation, context engineering, RAG prompts, compression, caching, and prompt-injection risks."
related:
  - LLMs
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Retrieval-Augmented Generation
  - Agent Engineering
  - AI Red Teaming
  - AI Tooling
---

Prompt engineering shapes the input to an
[LLM]({{ '/wiki/llms/' | relative_url }}). It names the role and task, provides
examples and retrieved context, and sets output constraints before the model
answers. In the
DataTalks.Club LLM episodes, guests treat prompts as part of the product
interface. The prompt sits between the user task, retrieved evidence, model
behavior, and checks that decide whether the answer is usable.

Prompt engineering is narrower than the whole LLM application. Use
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for serving, deployment, observability, and model choice. Use
[AI Tooling]({{ '/wiki/ai-tooling/' | relative_url }}) for libraries and
developer tools around prompts. The prompt-engineering question is what the model
sees and how the team constrains the answer. It also covers how they test prompt
changes and when they stop trying to fix the system with wording alone.

Use
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
when the decision is whether a system needs better prompts, retrieved context,
or model adaptation.
Michael Taylor and James Phoenix's
[Prompt Engineering for Generative AI]({{ '/books/20240701-prompt-engineering-for-generative-ai/' | relative_url }})
catalogs the same role, example, and structured-output techniques as a
practitioner reference, with prompt-testing patterns across image and text
generation.

## Prompt and Context Interface

Hugo Bowne-Anderson, Bartosz Mikulski, and Ranjitha Kulkarni converge on a
practical definition. Prompt engineering gives the model the right job,
evidence, and target format. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
starts with a role and objective, then adds examples and heuristics at 11:11.
In his timestamp example at 13:33-15:58, teams iterate on prompt details and add
audience-specific criteria. They also involve the person who used to do the
work.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) gives the
same definition through in-context learning in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 25:13, he says examples tell the model what should happen in a similar case.
At 27:45, he argues that when a stronger model still misses the task, examples
usually work better than a longer explanation.

Prompt engineering belongs inside
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) even though it
isn't the whole system. [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
draws that boundary in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}):
at 28:17-29:30, she frames context engineering as a deliberate information
choice. Teams choose what to give the LLM instead of stuffing everything into
the input. That broader practice is covered as
[Context Engineering]({{ '/wiki/context-engineering/' | relative_url }}).

## Role Prompts and Task Framing

Role prompts help when the role changes the answer criteria. Hugo's example in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
uses a chief marketing officer writing a campaign, then adds examples and
heuristics. The role isn't valuable because it flatters the model. It's
valuable when it tells the model which audience, constraints, and judgment rules
to apply.

In the timestamp discussion, a prompt that only asks for YouTube chapters may
produce plausible timestamps. Hugo adds audience relevance, detailed review, and
a pass/fail evaluator at
13:33-15:10. That turns a loose role prompt into a reviewable task definition.
It also connects prompt work to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
because the team needs to decide whether the prompt produced a usable result.

Roles can also hide weak task design. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) warns at
23:19-24:25 that developers can get stuck in endless prompt optimization. A
prompt that says "be accurate" or "act as a secure assistant" doesn't remove
model nondeterminism, provider updates, or the need for validation.

## Structured Output and Examples

Bartosz treats structured output as a prompt-engineering problem in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 28:16, he uses sentiment analysis as the example. The team can describe the
JSON keys, or it can show a review and the expected JSON output. Examples often
make the model follow the format even when the instruction is short.

Hugo makes the same point from the evaluation side in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 23:05-24:59, he says early prompt checks can stay simple. Teams can eyeball
the output, then add structured outputs or regular expressions. They can also
use string matching or cheaper models where the behavior is easy to assert. That
keeps structured output close to testing instead of treating it as a formatting
preference.

Bartosz says at 29:33-30:00 that each extra example adds tokens and money. The
team should prepare evaluation inputs and expected outputs so it can stop adding
examples when quality stops improving. The broader
[LLM system design]({{ '/wiki/llm-system-design-interview/' | relative_url }})
material uses the same cost-aware framing. Model calls, context size, and
reliability belong to one design decision.

## Prompt Evaluation

Prompt evaluation starts with representative cases, not with clever wording.
Hugo's generator-evaluator setup at 13:56 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
uses one model to generate an output and another to check it. He also says the
final signal can be pass/fail with feedback, because a product usually needs to
know whether the result can ship.

At 23:00-25:25 in the same episode, Hugo ties prompt iteration to gold test
sets. Teams can start with manual review, but reliable software eventually
needs examples that represent real user interactions. The test set should avoid
overfitting to a few cases without wasting time and money.

Teams use failure analysis to decide whether more prompt work is worthwhile. At
26:43, Hugo recommends categorizing errors and ranking them. If most failures
come from retrieval, the next fix belongs in chunking, indexing, or source data.
It doesn't belong in another prompt rewrite. Ranjitha makes a similar
evaluation point for agents at 51:17-56:02 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).

Public benchmarks test model capability. Product teams need custom datasets,
mocked tools, integration tests, and outcome assertions.

## Compression, Caching, and Context Budget

Prompt size matters because every token can affect cost, latency, and answer
quality. Bartosz discusses prompt compression at 30:00-31:45 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
He describes it as creating a shorter prompt that should preserve the same
behavior. Bartosz treats this as an optimization topic, not a replacement
for evaluation. A compressed prompt still needs the same expected-output checks
as the original.

At 31:45-33:03, Bartosz discusses provider-side caching for repeated prompt
prefixes. A coding assistant may reuse a shared codebase context with different
user requests. He tells listeners to verify the internal mechanism in provider
documentation. At the product level, stable shared context can reduce repeated
processing when many requests start with the same material.

Ranjitha adds the quality side of the context budget in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 29:30-30:27, she names latency, cost, and garbage-in-garbage-out as reasons
not to fill a large context window with noisy material. That links prompt
budgeting to [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and [production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
because the prompt is only as useful as the context selected for it.

## Context Engineering and RAG

Context engineering is the broader term for prompt work that selects and
packages information for the model. Ranjitha says at 28:17-32:48 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
that teams should be deliberate about the context they provide. They choose how
to chunk it, which metadata to attach, and which wrapper helps the LLM use it.
She treats RAG as one example of context engineering, not as a universal answer.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) explains the RAG
prompt structure in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 46:42, she describes injecting relevant sections into a prompt and asking
the model to answer from those documents. For sensitive tasks, she suggests a
narrower flow. The system retrieves the relevant section, summarizes or
rephrases it, and keeps the answer grounded in that source.

Hugo's chunking discussion in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
adds the practical constraint. At 44:26-46:39, he argues that a simple RAG bot
can solve real support questions faster than an ambitious AI tutor. Chunking
still depends on the source structure.

A podcast transcript may work better by question-answer pair or speaker turn. A
book needs a different strategy. The prompt can only use context that the
retrieval system preserved.

## Prompt Injection and Trust Boundaries

Prompt engineering also defines an attack surface. Maria's chatbot security
episode shows why instructions inside the prompt aren't enough protection. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
she describes a Siemens challenge with 1,500 participants at 9:28. Participants
tried to bypass bot restrictions, and some extracted hidden knowledge-base
content.

At 11:38-15:12, Maria explains the failure mode. A bot may have instructions not
to reveal confidential information, and another layer may check the output.
Users can still overload the prompt, use dense characters, craft API requests,
or otherwise distract the model from the original restriction. Prompt
engineering therefore has a direct boundary with
[AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}) and
[Security]({{ '/wiki/security/' | relative_url }}). A secure system needs query
analysis, output validation, retrieval controls, and human review where the
risk warrants it.

Prompt injection is especially important for RAG because the model may receive
instructions from user input and retrieved documents. If the system retrieves
restricted or adversarial text, the prompt can include that text in the answer.
Maria's 13:20 discussion shows that attackers can extract knowledge-base data.
The prompt template can state the rule, but access control and validation must
enforce it.

## Limits of Prompting

Several guests draw a clear stopping point for prompt engineering. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 26:30-46:42, Meryem says fine-tuning is better for behavior and style. She
also includes tone and domain adaptation. Retrieval is better for changing
knowledge and grounded facts.

If a prompt repeatedly fails because the model lacks the right knowledge, the
team should add retrieval. If it repeatedly fails because the model needs a
specialized behavior, fine-tuning may be the better tool.

Ranjitha makes the workflow boundary explicit. At 37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she separates cases where RAG is enough from cases that need planning, tools, or
agents. At 53:20-56:02, she shows why those systems need software-style tests,
not only better instructions. This links prompt engineering to
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) without
turning every prompt problem into an agent problem.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) adds one more
boundary in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 14:09-17:25, he discusses evolutionary algorithms for prompt engineering.
They can find useful prompt variations, but they're computationally expensive.

That reinforces the practical theme across these episodes. Prompt iteration is
useful, but teams should measure whether more iteration beats retrieval or
fine-tuning. They should also compare it with tool design, human review, or a
smaller product target.
