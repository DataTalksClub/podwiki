---
layout: wiki
title: "LLM Production Patterns"
summary: "How DataTalks.Club guests turn LLM demos into production systems with model choice, RAG, agents, and evaluation."
related:
  - LLMs
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Agent Engineering
  - AI Engineer Role
  - AI Red Teaming
  - Business Intelligence
  - Notebook to Production AI Systems
---

LLM production patterns are the design choices teams use when a
[[llms=>large language model]] becomes a product
feature instead of a demo. DataTalks.Club guests discuss those choices through
model serving and [[retrieval-augmented-generation|retrieval-augmented generation]].
They also include [[rag-vs-fine-tuning|RAG vs fine-tuning]],
[[agent engineering]],
evaluation, and security. Cost, latency, and ownership stay part of the same
production question.

An LLM is a product component rather than the whole system. In production it
ties deployment and model ownership to fine-tuning and retrieval. Cost and
latency stay in the same decision
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
In [[business intelligence]],
the model can help with questions and summaries. The product still depends on
governed metrics, access controls, and review.

The same production problem breaks down into prompts, RAG, and gold tests. It
also includes failure analysis, logs, traces, and tool use
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].

## Production System Boundary

Guests define production LLM work by the system boundary around measurable
product behavior. Hugo starts from a small LLM application, then adds
generator-evaluator checks and representative gold tests. He covers failure
analysis, logs, traces, and tool use or agents in the same production workflow
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
That makes [[LLM evaluation workflows]]
part of production design rather than a final audit.

[[person:pauliusztin=>Paul Iusztin]] places RAG and
agents inside one AI engineering skill stack
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].
LLMOps and product shipping sit in that same stack. He also includes queues,
retries, traces, and monitoring in that shipping discussion.

[[person:marianosemelman=>Mariano Semelman]] keeps the
same product boundary in
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
Requirements and data still matter. Deployment, monitoring, and feedback matter
too.

Guests therefore don't stop at "pick a model and prompt it." They bring LLM
work into [[software engineering]],
[[MLOps]], and [[evaluation]].
They also bring it into [[notebook-to-production-ai-systems|notebook-to-production AI systems]].
Teams choose the model boundary and package the context. They test the
behavior, watch the system in use, and change the design when failures show
where the next fix belongs.

## Different Starting Constraints

Guests differ on the constraint they treat as the first production problem.
Meryem starts with the serving boundary. In
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
she compares open-source models with hosted APIs. She connects
that choice to control and privacy. Provider drift appears there too.

She also covers fine-tuning, compression, and inference optimization, with
latency and cost in the same production discussion.

Hugo starts with builder iteration. He treats prompts and structured outputs as
parts of a testable system in
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
RAG and tools appear in the same testable system.

[[person:ranjithakulkarni=>Ranjitha Kulkarni]]
starts from agentic workflows. Context engineering and tools appear with memory in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Ranjitha adds mocked tool tests, integration tests, and outcome assertions.

[[person:adityagautam=>Aditya Gautam]] starts from
enterprise reliability. In
[[cite:s23e03-future-of-ai-agents|The Future of AI Agents]],
he ties agents to guardrails and lineage. He also discusses feedback and
multi-tenancy. Golden datasets, thresholds, and LLM judges appear in the same
section.

[[person:mariasukhareva=>Maria Sukhareva]] starts from
adversarial trust. Prompt injection and data exfiltration come before output
validation and non-LLM classifiers in
[[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].

## Model Choice and Serving

Teams first choose a serving boundary. They may use a hosted API or a
self-hosted open-source model. They may also use a fine-tuned model or a mix.
Meryem anchors that decision in
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

She links model-source choices to control and privacy while also covering model
size, compression, and inference optimization. She separates prototype
convenience from production choices around self-hosting, where hardware,
latency, and cost also affect that choice.

[[person:sandrakublik=>Sandra Kublik]] gives the
product version of the same tradeoff in
[[cite:practical-llm-use-cases-and-product-patterns|Practical LLM Use Cases]].
She discusses model, architecture, and integration decisions for LLM
applications. She also names cost and latency. Proprietary-data and IP
concerns appear in the same discussion. Model choice therefore depends on
[[AI infrastructure]] and
[[data governance]], not only on
benchmark scores.

## RAG, Fine-Tuning, and Context

Meryem separates retrieval from fine-tuning in practical terms.
She discusses fine-tuning for specialization, domain adaptation, tone, and
format in
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
She discusses retrieval for changing knowledge and indexes. She also covers
grounded responses and summarizers there.

[[person:atitaarora=>Atita Arora]] adds the search
engineering version in
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].

She describes RAG as retrieval plus generation, covers chunking and overlap,
and connects retrieval to prompt design and citations. Embeddings and
vectorization appear there too. She connects RAG to multi-level metrics,
offline tests, and human-in-the-loop evaluation. This is why production RAG
belongs with
[[retrieval-augmented-generation=>retrieval-augmented generation]]
and [[production search evaluation]].

Ranjitha puts context engineering between prompting and autonomous agents. She
names noisy context and chunking, then covers metadata and wrappers. Latency,
cost, and garbage-in-garbage-out appear in the same discussion
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].

[[person:lavanyagupta=>Lavanya Gupta]]
adds the long-context case in
[[cite:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]:
her discussion covers financial long-context evaluation. Large context windows
still need task-specific evaluation. Retrieval or summarization can still
matter there.

## Tool Use and Agents

Agents fit cases where the LLM must plan or call tools. They also fit cases
where the system must use memory or take action beyond retrieving context. Ranjitha
defines agents around autonomy and objectives in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
She includes orchestration, tools, memory, and knowledge stores. She then
separates retrieval as one tool from cases that need planning or action.

Tool use becomes production work when teams constrain and test the callable
interfaces. Ranjitha discusses SDKs and tool wrappers. Integration abstractions
appear there too. She then adds mocked tools and integration tests in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Regression tests and outcome assertions appear in the same section.

[[person:micheallanham=>Micheal Lanham]] adds a
minimalist agent-design boundary in
[[cite:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
Task decomposition and sequential workflows appear there. Manager-agent
orchestration appears in the same discussion, along with Agent SDKs and
MCP-style integrations.

Those examples keep [[agent engineering]]
close to [[tools]] and
[[orchestration]]. They also keep
agent work close to [[testing]]. A
production agent isn't only a prompt. It's a bounded workflow with permissions,
callable interfaces, state, and retrieval. Teams also need evaluation and
rollback paths.

## Evaluation and Feedback Loops

Production LLM systems need evaluation before launch and feedback after launch.
Hugo gives the base workflow in
[[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
He covers generator-evaluator checks, structured checks, gold tests, and
failure categories. Logs and traces show where the team
needs to know whether the next fix belongs in retrieval or prompting. The fix
may also belong in data preparation, formatting, or product scope.

Agent systems extend evaluation into software behavior. Ranjitha argues for
custom datasets, system benchmarks, mocked tools, and integration tests in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Regression tests and outcome-based assertions appear there too.

Aditya adds the enterprise layer in
[[cite:s23e03-future-of-ai-agents|The Future of AI Agents]].
He covers golden datasets, thresholds, and LLM judges aligned with human
labels. Feedback loops, multi-tenancy, and scale also become operating
requirements there.

Feedback can also be a product signal. Mariano discusses explicit and implicit
feedback loops in
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
He shows how generated media for e-commerce sellers used customer requirements
and factuality checks. That example links LLM production to [[model monitoring]] and
[[data products]].

## Guardrails, Security, and Human Review

Production LLM systems need controls around user input and retrieved context.
They also need controls around generated output and tool calls. Maria describes
a large-scale hacking exercise in
[[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
She then covers legal and financial exposure from hallucinations. Data
exfiltration through prompt overload and knowledge-base retrieval appears in
the same discussion.

Maria discusses layered defenses, including output validation, query analysis,
and non-LLM classifiers. These controls put LLM production in the same
operational space as
[[AI red teaming]] and
[[security]]. She also discusses
moderation support and human review for higher-risk outputs
[[cite:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].

Human review also appears in product risk. Sandra discusses hallucinations and
brand safety in
[[cite:practical-llm-use-cases-and-product-patterns|Practical LLM Use Cases]].
She covers editorial curation in the same section. Aditya adds auditability,
guardrails, lineage, and compliance for enterprise agents in
[[cite:s23e03-future-of-ai-agents|The Future of AI Agents]].
Those enterprise controls place production LLM work next to
[[Agent Ops]] and
[[responsible AI and governance]].

## Cost, Latency, and Operability

Cost and latency affect the design because prompts and retrieved context add
runtime and model spend. Judge calls, tool calls, and retries add more.
Multi-step agents add more runtime and spend. Meryem covers serving efficiency
and compression in
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
She also covers hardware, latency, and cost in the same serving discussion.

Ranjitha adds the RAG and agent version in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Retrieval quality and context quality affect whether the system is usable.
Latency and cost affect that decision too.

[[person:bartoszmikulski=>Bartosz Mikulski]] contributes
the application-engineering view in
[[cite:production-ready-ai-engineering|Production AI Engineering]].
He connects prompt evaluation and prompt compression to model efficiency.
Caching appears in the same section. He discusses backend AI integrations and
browser extension architecture. Search assistants and tool selection appear
there too.

Those examples make LLM production a [[software engineering]]
and [[data engineering]] topic,
not only a prompt-writing topic. Teams need these production choices because
they expose the parts that fail or slow down. They also expose data leaks,
costly calls, and behavior the team can't evaluate.

For the specific techniques that reduce LLM spend, see
[[LLM Cost Optimization]].

## Related Pages

These adjacent pages cover the model and retrieval pieces around LLM
production.

They also cover evaluation, agents, governance, and project ideas:

- [[LLMs]]
- [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[AI Engineer Role]]
- [[AI Engineering]]
- [[Notebook to Production AI Systems]]
- [[AI Red Teaming]]
- [[Responsible AI and Governance]]
- [[RAG Portfolio Projects]]
- [[LLM System Design Interview]]
- [[book:20241104-llm-engineer-s-handbook=>LLM Engineer's Handbook]]
