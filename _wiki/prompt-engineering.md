---
layout: wiki
title: "Prompt Engineering"
summary: "DataTalks.Club episodes on prompt engineering patterns: role prompts, examples, structured output, evaluation, RAG context, and injection risks."
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
[[llms=>LLM]]. It names the role and task, provides
examples and retrieved context, and sets output constraints before the model
answers. In the
DataTalks.Club LLM episodes, guests treat prompts as part of the product
interface. The prompt sits between the user task, retrieved evidence, model
behavior, and checks that decide whether the answer is usable.

Prompt engineering is narrower than the whole LLM application. Use
[[LLM Production Patterns]]
for serving, deployment, observability, and model choice. Use
[[AI Tooling]] for libraries and
developer tools around prompts. The prompt-engineering question is what the model
sees and how the team constrains the answer. It also covers how they test prompt
changes and when they stop trying to fix the system with wording alone.

Use
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
when the decision is whether a system needs better prompts, retrieved context,
or model adaptation.
Michael Taylor and James Phoenix's
[[book:20240701-prompt-engineering-for-generative-ai=>Prompt Engineering for Generative AI]]
catalogs the same role, example, and structured-output techniques as a
practitioner reference. It also covers prompt-testing patterns across image and
text generation.

## Prompt and Context Interface

Hugo Bowne-Anderson, Bartosz Mikulski, and Ranjitha Kulkarni converge on a
practical definition. Prompt engineering gives the model the right job,
evidence, and target format. [[person:hugobowneanderson=>Hugo Bowne-Anderson]]
starts with a role and objective, then adds examples, heuristics, and
audience-specific criteria. He also involves the person who used to do the work ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

[[person:bartoszmikulski=>Bartosz Mikulski]] gives the
same definition through in-context learning. Examples tell the model what
should happen in a similar case. When a stronger model still misses the task,
examples usually work better than a longer explanation ([[cite:production-ready-ai-engineering|Production AI Engineering]]).

Prompt engineering belongs inside
[[AI engineering]] even though it
isn't the whole system. [[person:ranjithakulkarni|Ranjitha Kulkarni]]
draws that boundary by framing context engineering as a deliberate information
choice. Teams choose what to give the LLM instead of stuffing everything into
the input ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
That broader practice is covered as
[[Context Engineering]].

## Role Prompts and Task Framing

Role prompts help when the role changes the answer criteria. Hugo's chief
marketing officer campaign prompt adds examples and heuristics to the role. The
role isn't valuable because it flatters the model. It's valuable when it tells
the model which audience, constraints, and judgment rules to apply ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A prompt that only asks for YouTube chapters may produce plausible timestamps.
Hugo adds audience relevance, detailed review, and a pass/fail evaluator. That
turns a loose role prompt into a reviewable task definition ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
It also connects prompt work to
[[LLM Evaluation Workflows]],
because the team needs to decide whether the prompt produced a usable result.

Roles can also hide weak task design. [[person:mariasukhareva=>Maria Sukhareva]]
warns that developers can get stuck in endless prompt optimization. A prompt
that says "be accurate" or "act as a secure assistant" doesn't remove model
nondeterminism. It also doesn't remove provider updates or the need for
validation ([[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

## Structured Output and Examples

Bartosz treats structured output as a prompt-engineering problem with sentiment
analysis. The team can describe the JSON keys, or it can show a review and the
expected JSON output. Examples often make the model follow the format even when
the instruction is short ([[cite:production-ready-ai-engineering|Production AI Engineering]]).

Hugo makes the same point from the evaluation side in his practical LLM
engineering discussion. Early prompt checks can stay simple: teams can eyeball
the output, then add structured outputs or regular
expressions. They can also use string matching or cheaper models where the
behavior is easy to assert. That keeps structured output close to testing
instead of treating it as a formatting preference ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Bartosz also notes that each extra example adds tokens and money. The team
should prepare evaluation inputs and expected outputs so it can stop adding
examples when quality stops improving ([[cite:production-ready-ai-engineering|Production AI Engineering]]). The broader
[[llm-system-design-interview=>LLM system design]]
material uses the same cost-aware framing. Model calls, context size, and
reliability belong to one design decision.

## Prompt Evaluation

Prompt evaluation starts with representative cases, not with clever wording.
Hugo's generator-evaluator setup uses one model to generate an output and
another to check it. He also says the final signal can be pass/fail with
feedback. A product usually needs to know whether the result can ship ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Hugo ties prompt iteration to gold test sets in the same episode. Teams can
start with manual review, but reliable software eventually needs examples that
represent real user interactions. The test set should avoid overfitting to a few
cases without wasting time and money ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Teams use failure analysis to decide whether more prompt work is worthwhile.
Hugo recommends categorizing errors and ranking them. If most failures come from
retrieval, the next fix belongs in chunking, indexing, or source data. It
doesn't belong in another prompt rewrite ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Ranjitha makes a similar evaluation point for agents ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

Public benchmarks test model capability. Product teams need custom datasets,
mocked tools, integration tests, and outcome assertions.

## Compression, Caching, and Context Budget

Prompt size matters because every token can affect cost, latency, and answer
quality. Bartosz describes prompt compression as creating a shorter prompt that
should preserve the same behavior. He treats this as an optimization topic, not
a replacement for evaluation. A compressed prompt still needs the same
expected-output checks as the original ([[cite:production-ready-ai-engineering|Production AI Engineering]]).

Bartosz also discusses provider-side caching for repeated prompt prefixes. A
coding assistant may reuse a shared codebase context with different user
requests. He tells listeners to verify the internal mechanism in provider
documentation. At the product level, stable shared context can reduce repeated
processing when many requests start with the same material ([[cite:production-ready-ai-engineering|Production AI Engineering]]).

Ranjitha adds the quality side of the context budget in her agentic systems
discussion. She names latency, cost, and
garbage-in-garbage-out as reasons not to fill a large context window with noisy
material ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
That links prompt budgeting to [[retrieval-augmented-generation|retrieval-augmented generation]]
and [[production search evaluation]],
because the prompt is only as useful as the context selected for it.

## Context Engineering and RAG

Context engineering is the broader term for prompt work that selects and
packages information for the model. Ranjitha says teams should be deliberate
about the context they provide. They choose how to chunk it, which metadata to
attach, and which wrapper helps the LLM use it. She treats RAG as one example
of context engineering, not as a universal answer ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

[[person:meryemarik=>Meryem Arik]] explains the RAG
prompt structure as injecting relevant sections into a prompt and asking the
model to answer from those documents. For sensitive tasks, she suggests a
narrower flow. The system retrieves the relevant section, summarizes or
rephrases it, and keeps the answer grounded in that source ([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

Hugo's chunking discussion adds the practical constraint. A simple RAG bot can
solve real support questions faster than an ambitious AI tutor. Chunking still
depends on the source structure ([[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A podcast transcript may work better by question-answer pair or speaker turn. A
book needs a different strategy. The prompt can only use context that the
retrieval system preserved.

## Prompt Injection and Trust Boundaries

Prompt engineering also defines an attack surface. Maria's chatbot security
episode shows why instructions inside the prompt aren't enough protection. In
her Siemens challenge example, 1,500 participants tried to bypass bot
restrictions, and some extracted hidden knowledge-base content ([[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).

Maria explains the failure mode: a bot may have instructions not to reveal
confidential information, and another layer may check the output. Users can
still overload the prompt, use dense characters, craft API requests, or
otherwise distract the model from the original restriction ([[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
Prompt engineering therefore has a direct boundary with
[[AI Red Teaming]] and
[[Security]]. A secure system needs query
analysis, output validation, retrieval controls, and human review where the
risk warrants it.

Prompt injection is especially important for RAG because the model may receive
instructions from user input and retrieved documents. If the system retrieves
restricted or adversarial text, the prompt can include that text in the answer.
Maria's challenge example shows that attackers can extract knowledge-base data ([[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]).
The prompt template can state the rule, but access control and validation must
enforce it.

## Limits of Prompting

Several guests draw a clear stopping point for prompt engineering. Meryem says
fine-tuning is better for behavior and style. She also includes tone and domain
adaptation. Retrieval is better for changing knowledge and grounded facts ([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

If a prompt repeatedly fails because the model lacks the right knowledge, the
team should add retrieval. If it repeatedly fails because the model needs a
specialized behavior, fine-tuning may be the better tool.

Ranjitha makes the workflow boundary explicit. She separates cases where RAG is
enough from cases that need planning, tools, or agents. She also shows why those
systems need software-style tests, not only better instructions ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
This links prompt engineering to
[[Agent Engineering]] without
turning every prompt problem into an agent problem.

[[person:micheallanham=>Micheal Lanham]] adds one more
boundary. Evolutionary algorithms can find useful prompt variations, but
they're computationally expensive ([[cite:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

That reinforces the practical theme across these episodes. Prompt iteration is
useful, but teams should measure whether more iteration beats retrieval or
fine-tuning. They should also compare it with tool design, human review, or a
smaller product target.
