---
layout: wiki
title: "Prompt Engineering"
summary: "DataTalks.Club episodes on prompt engineering techniques: role prompts, examples, structured output, evaluation, RAG context, and injection risks."
related:
  - LLMs
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Retrieval-Augmented Generation
  - Agent Engineering
  - AI Red Teaming
  - AI Tooling
---

Prompt engineering shapes the input to an [[llms=>LLM]]. It names the role and
task before the model answers. It also provides examples, retrieved context, and
output constraints. In LLM applications, the prompt sits between the user task
and the retrieved evidence. It also sits between model behavior and answer
checks.

Prompt engineering is narrower than the whole LLM application. [[LLM Production Patterns]]
covers serving, deployment, observability, and model choice. [[AI Tooling]]
covers libraries and developer tools around prompts. The prompt-engineering
question is what the model sees and how the team constrains the answer. It also
covers how teams test prompt changes and when wording alone stops helping.

The [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] comparison covers the boundary
between better prompts, retrieved context, and model adaptation. Michael Taylor
and James Phoenix's
[[book:20240701-prompt-engineering-for-generative-ai=>Prompt Engineering for Generative AI]]
catalogs the same role, example, and structured-output techniques as a
practitioner reference. It also covers prompt-testing patterns across image and
text generation.

## Prompt Interface

Prompt engineering gives the model the right job, evidence, and target format.
Role and objective come first. Examples, heuristics, audience-specific criteria,
and expert review define what a good answer should satisfy. The person who used
to do the work can help define the expected answer. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

In-context learning gives the same definition from the example side. Examples
tell the model what should happen in a similar case. When a stronger model still
misses the task, examples usually work better than a longer explanation. [[cite:production-ready-ai-engineering=>Production AI Engineering]]

Prompt engineering belongs inside [[AI engineering]] even though it isn't the
whole system. [[Context Engineering]] draws the wider boundary. Teams choose what
to give the LLM instead of stuffing everything into the input. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Machine translation is a narrow example of that interface work. Prompts can
customize ChatGPT translation behavior. Quality control still has to sit around
the model rather than trusting a fluent translation by default.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## Boundaries and Tradeoffs

Prompt engineering can be the main task interface. Role and examples describe
the work the model should do. Output schema and evaluation criteria describe
what the answer must satisfy. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

It can also be one layer in a larger system. Retrieval, context selection, tests,
and security controls all affect whether the answer can be trusted. Tool
orchestration adds another failure point outside the prompt. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

The stopping point also differs by failure mode. When the model lacks current or
source-grounded knowledge, [[Retrieval-Augmented Generation]] is the stronger
move. For specialized behavior or style, fine-tuning may be a better fit.
Security failures need more than stronger wording. Validation and access control
must enforce the boundary. [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## Role Prompts and Task Framing

Role prompts help when the role changes the answer criteria. A chief marketing
officer campaign prompt becomes useful when the role comes with examples,
heuristics, audience constraints, and judgment rules. The role isn't valuable
because it flatters the model. It's valuable when it changes what the answer
must satisfy. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

A prompt that only asks for YouTube chapters may produce plausible timestamps.
Audience relevance and detailed review narrow the task. A pass/fail evaluator
turns the loose role prompt into a reviewable task definition. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
The team can then use [[LLM Evaluation Workflows]] to decide whether the prompt
produced a usable result.

Roles can also hide weak task design. A prompt that says "be accurate" or "act
as a secure assistant" doesn't remove model nondeterminism, provider updates,
or the need for validation. Endless prompt optimization can delay the system
controls that actually reduce risk. [[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## Structured Output and Examples

Teams handle structured output as a prompt-engineering problem, not just a
formatting detail. The team can describe the JSON keys, or it can show a review
and the expected JSON output. Examples often make the model follow the format
even when the instruction is short. [[cite:production-ready-ai-engineering=>Production AI Engineering]]

Early prompt checks can stay simple: teams can eyeball the output, then add
structured outputs or regular expressions. They can also use string matching or
cheaper models where the behavior is easy to assert. That keeps structured
output close to testing instead of treating it as a formatting preference. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Each extra example costs tokens and money. Teams use expected outputs for
evaluation inputs to see when quality stops improving. That tells them when to
stop adding examples. [[cite:production-ready-ai-engineering=>Production AI Engineering]]
The broader [[llm-system-design-interview=>LLM system design]] material uses the
same cost-aware framing. Model calls, context size, and reliability belong to
the same design decision.

## Prompt Evaluation

Prompt evaluation starts with representative cases, not clever wording. A
generator-evaluator setup can use one model to generate an output and another to
check it. The final signal can be pass/fail with feedback, because a product
usually needs to know whether the result can ship. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Teams can start with manual review, but reliable software eventually needs
examples that represent real user interactions. The test set should avoid
overfitting to a few cases without wasting time and money. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Teams use failure analysis to decide whether more prompt work is worthwhile.
Categorizing and ranking errors shows where the next fix belongs. If most
failures come from retrieval, the next fix belongs in chunking, indexing, or
source data. It doesn't belong in another prompt rewrite. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Agent systems need the same style of evaluation because tool use and retrieval
can fail outside the prompt. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Public benchmarks test model capability. Product teams need custom datasets,
mocked tools, integration tests, and outcome assertions. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Compression, Caching, and Context Budget

Prompt size matters because every token can affect cost, latency, and answer
quality. Prompt compression creates a shorter prompt that should preserve the
same behavior. It's an optimization topic, not a replacement for evaluation. A
compressed prompt still needs the same expected-output checks as the original. [[cite:production-ready-ai-engineering=>Production AI Engineering]]

Provider-side caching can help with repeated prompt prefixes. A coding assistant
may reuse a shared codebase context with different user requests. Teams still
need to verify the internal mechanism in provider documentation. At the product
level, stable shared context can reduce repeated processing when many requests
start with the same material. [[cite:production-ready-ai-engineering=>Production AI Engineering]]

The context budget has a quality side because latency, cost, and noisy context
all affect quality. Teams avoid filling large windows with material that creates
garbage-in-garbage-out failures. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Prompt budgeting therefore connects to [[retrieval-augmented-generation=>retrieval-augmented generation]]
and [[production search evaluation]]. The prompt is only as useful as the context
selected for it.

## Context Engineering and RAG

Context engineering is the broader term for prompt work that selects and
packages information for the model. Teams choose how to chunk it, which metadata
to attach, and which wrapper helps the LLM use it. RAG is one example of context
engineering, not a universal answer. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

RAG prompt structure injects relevant sections into a prompt and asks the model
to answer from those documents. For sensitive tasks, a narrower flow retrieves
the relevant section, summarizes or rephrases it, and keeps the answer grounded
in that source. [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Chunking adds the practical constraint. A simple RAG bot can solve real support
questions faster than an ambitious AI tutor, but chunking still depends on the
source structure. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

A podcast transcript may work better by question-answer pair or speaker turn. A
book needs a different strategy. The prompt can only use context that the
retrieval system preserved.

## Prompt Injection and Trust Boundaries

Prompt engineering also defines an attack surface, but instructions inside the
prompt aren't enough protection. In a Siemens chatbot challenge, 1,500
participants tried to bypass bot restrictions, and some extracted hidden
knowledge-base content. [[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

A bot may have instructions not to reveal confidential information, and another
layer may check the output. Users can still overload the prompt, use dense
characters, craft API requests, or otherwise distract the model from the
original restriction. [[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]
Prompt engineering therefore has a direct boundary with [[AI Red Teaming]] and
[[Security]]. A secure system needs query analysis, output validation, retrieval
controls, and human review where the risk warrants it.

Prompt injection is especially important for RAG because the model may receive
instructions from user input and retrieved documents. If the system retrieves
restricted or adversarial text, the prompt can include that text in the answer.
The chatbot challenge shows that attackers can extract knowledge-base data. [[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]
The prompt template can state the rule, but access control and validation must enforce it.

## Limits of Prompting

Prompt engineering has a clear stopping point. Fine-tuning is better for
behavior, style, tone, and domain adaptation. Retrieval is better for changing
knowledge and grounded facts. [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

If a prompt repeatedly fails because the model lacks the right knowledge, the
team should add retrieval. If it repeatedly fails because the model needs a
specialized behavior, fine-tuning may be the better tool.

RAG is enough for some cases, but planning, tools, or agents are better fits
when the system must coordinate multiple steps. Those systems need software-style
tests, not only better instructions. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
This links prompt engineering to [[Agent Engineering]] without turning every
prompt problem into an agent problem.

Evolutionary algorithms can find useful prompt variations, but they're
computationally expensive. [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Prompt iteration is useful, but teams should measure whether more iteration
beats retrieval or fine-tuning. They should also compare it with tool design,
human review, or a smaller product target.

## Related Pages

Prompt engineering connects most directly to these adjacent wiki pages.

- [[LLMs]]
- [[LLM Production Patterns]]
- [[LLM Evaluation Workflows]]
- [[Retrieval-Augmented Generation]]
- [[Agent Engineering]]
- [[AI Red Teaming]]
