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
[[llms|large language model]] becomes a product
feature instead of a demo. DataTalks.Club guests discuss those choices through
model serving and [[retrieval-augmented-generation|retrieval-augmented generation]].
They also include [[rag-vs-fine-tuning|RAG vs fine-tuning]],
[[agent engineering]],
evaluation, and security. Cost, latency, and ownership stay part of the same
production question.

DataTalks.Club guests repeatedly treat the LLM as a product component, not the
whole system.
[[person:meryemarik|Meryem Arik]] ties LLM production
to deployment and model ownership in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
She also discusses fine-tuning, retrieval, cost, and latency there. In
[[business intelligence]],
the model can help with questions and summaries. The product still depends on
governed metrics, access controls, and review.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
turns the same production problem into prompts, RAG, and gold tests in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
He adds failure analysis, logs, traces, and tool use in the same episode.

## Production System Boundary

Guests define production LLM work by the system boundary around measurable
product behavior. Hugo starts from a small LLM application, then adds
generator-evaluator checks at 13:56 and representative gold tests at 23:00. He
covers failure analysis at 26:43, logs and traces at 27:38, and tool use or
agents at 44:26-56:21 in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
That makes [[LLM evaluation workflows]]
part of production design rather than a final audit.

[[person:pauliusztin|Paul Iusztin]] places RAG and
agents inside one AI engineering skill stack at 29:12-46:31 in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]].
LLMOps and product shipping sit in that same stack. He also includes queues,
retries, traces, and monitoring in that shipping discussion.

[[person:marianosemelman|Mariano Semelman]] keeps the
same product boundary in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
Requirements and data still matter at 17:27-21:12. Deployment, monitoring, and
feedback matter at 41:28-49:55.

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
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
she compares open-source models with hosted APIs at 16:48-25:26. She connects
that choice to control and privacy. Provider drift appears there too.

She also covers fine-tuning, compression, and inference optimization through
49:44-51:35, with latency and cost in the same production discussion.

Hugo starts with builder iteration. He treats prompts and structured outputs as
parts of a testable system in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
at 13:56-27:38. RAG and tools appear in the same testable system at
44:26-56:21.

[[person:ranjithakulkarni|Ranjitha Kulkarni]]
starts from agentic workflows. Context engineering and tools appear with memory in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]
at 21:21-37:39. Ranjitha adds mocked tool tests, integration tests, and
outcome assertions at 51:17-57:23.

[[person:adityagautam|Aditya Gautam]] starts from
enterprise reliability. In
[[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]],
he ties agents to guardrails and lineage. He also discusses feedback and
multi-tenancy. Golden datasets, thresholds, and LLM judges appear in the same
section at 30:26-50:18.

[[person:mariasukhareva|Maria Sukhareva]] starts from
adversarial trust. Prompt injection and data exfiltration come before output
validation and non-LLM classifiers in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]]
at 9:28-17:00.

## Model Choice and Serving

Teams first choose a serving boundary. They may use a hosted API or a
self-hosted open-source model. They may also use a fine-tuned model or a mix.
Meryem anchors that decision in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].

At 16:48-25:26, she links model-source choices to control and privacy. She
also covers model size, compression, and inference optimization. At
49:44-51:35, she separates prototype convenience from production choices around
self-hosting. Hardware, latency, and cost also affect that choice.

[[person:sandrakublik|Sandra Kublik]] gives the
product version of the same tradeoff in
[[podcast:practical-llm-use-cases-and-product-patterns|Practical LLM Use Cases]].
At 32:28-35:28, she discusses model, architecture, and integration decisions
for LLM applications. She also names cost and latency. Proprietary-data and IP
concerns appear in the same discussion. Model choice therefore depends on
[[AI infrastructure]] and
[[data governance]], not only on
benchmark scores.

## RAG, Fine-Tuning, and Context

Meryem separates retrieval from fine-tuning in practical terms.
She discusses fine-tuning for specialization, domain adaptation, tone, and
format at 26:30-31:38 in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 40:46-46:42, she discusses retrieval for changing knowledge and indexes.
She also covers grounded responses and summarizers there.

[[person:atitaarora|Atita Arora]] adds the search
engineering version in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].

At 30:38-42:49, she describes RAG as retrieval plus generation, covers chunking
and overlap, and connects retrieval to prompt design and citations. Embeddings
and vectorization appear there too. At 48:09, she connects RAG to
multi-level metrics, offline tests, and human-in-the-loop evaluation. This is
why production RAG belongs with
[[search-rag-and-knowledge-systems|search, RAG, and knowledge systems]]
and [[production search evaluation]].

Context engineering sits between prompting and autonomous agents. In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]
Ranjitha names context engineering at 21:21. She then names noisy context,
chunking, metadata, and wrappers at 29:30-32:48.
Latency, cost, and garbage-in-garbage-out appear in the same discussion.

[[person:lavanyagupta|Lavanya Gupta]]
adds the long-context case in
[[podcast:applied-llm-research-and-career-growth-in-practice|Applied LLM Research]]:
her 10:15-14:54 discussion covers financial long-context evaluation. Large
context windows still need task-specific evaluation. Retrieval or summarization
can still matter there.

## Tool Use and Agents

Agents fit cases where the LLM must plan or call tools. They also fit cases
where the system must use memory or take action beyond retrieving context. Ranjitha
defines agents around autonomy and objectives at 11:00-12:31 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
She includes orchestration, tools, memory, and knowledge stores. She then
separates retrieval as one tool from cases that need planning or action at
36:11-37:39.

Tool use becomes production work when teams constrain and test the callable
interfaces. Ranjitha discusses SDKs and tool wrappers at 18:23-24:59.
Integration abstractions appear there too. She then adds mocked tools and
integration tests at 51:17-57:23 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Regression tests and outcome assertions appear in the same section.

[[person:micheallanham|Micheal Lanham]] adds a
minimalist agent-design boundary in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]].
Task decomposition and sequential workflows appear at 20:57-23:48.
Manager-agent orchestration appears at 23:48-33:25, along with Agent SDKs and
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
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
at 13:56-27:38. He covers generator-evaluator checks, structured checks, gold
tests, and failure categories. Logs and traces appear at 27:38, where the team
needs to know whether the next fix belongs in retrieval or prompting. The fix
may also belong in data preparation, formatting, or product scope.

Agent systems extend evaluation into software behavior. Ranjitha argues for
custom datasets, system benchmarks, mocked tools, and integration tests in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]
at 51:17-57:23. Regression tests and outcome-based assertions appear there too.

Aditya adds the enterprise layer in
[[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]
at 38:49-50:18. He covers golden datasets, thresholds, and LLM judges aligned
with human labels. Feedback loops, multi-tenancy, and scale also become
operating requirements there.

Feedback can also be a product signal. Mariano discusses explicit and implicit
feedback loops at 41:28 in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
At 47:22-58:45, he shows how generated media for e-commerce sellers used
customer requirements and factuality checks. That example links LLM production
to [[model monitoring]] and
[[data products]].

## Guardrails, Security, and Human Review

Production LLM systems need controls around user input and retrieved context.
They also need controls around generated output and tool calls. Maria describes
a large-scale hacking exercise at 9:28 in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].
She then covers legal and financial exposure from hallucinations at 11:38.
Data exfiltration through prompt overload and knowledge-base retrieval appears
at 13:20.

Maria discusses layered defenses at 16:15-17:00, including output validation,
query analysis, and non-LLM classifiers. These controls put LLM production in
the same operational space as
[[AI red teaming]] and
[[security]]. She also discusses
moderation support and human review for higher-risk outputs at 25:34 in
[[podcast:generative-ai-chatbots-in-production-security|Hardening Generative AI Chatbots]].

Human review also appears in product risk. Sandra discusses hallucinations and
brand safety at 23:29 in
[[podcast:practical-llm-use-cases-and-product-patterns|Practical LLM Use Cases]].
She covers editorial curation in the same section. Aditya adds auditability,
guardrails, lineage, and compliance for enterprise agents at 30:26 in
[[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]].
Those enterprise controls place production LLM work next to
[[Agent Ops]] and
[[responsible AI and governance]].

## Cost, Latency, and Operability

Cost and latency affect the design because prompts and retrieved context add
runtime and model spend. Judge calls, tool calls, and retries add more.
Multi-step agents add more runtime and spend. Meryem covers serving efficiency
and compression at 25:26 and 51:35 in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
She also covers hardware, latency, and cost in the same serving discussion.

Ranjitha adds the RAG and agent version at 29:30 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
Retrieval quality and context quality affect whether the system is usable.
Latency and cost affect that decision too.

[[person:bartoszmikulski|Bartosz Mikulski]] contributes
the application-engineering view in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
At 28:16-31:45, he connects prompt evaluation and prompt compression to model
efficiency. Caching appears in the same section. At 41:04-47:19, he discusses
backend AI integrations and browser extension architecture. Search assistants
and tool selection appear there too.

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
- [[llm-rag-production-roadmap|LLM and RAG Production Roadmap]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
- [[LLM Evaluation Workflows]]
- [[Agent Engineering]]
- [[AI Engineer Role]]
- [[AI Engineering]]
- [[Notebook to Production AI Systems]]
- [[AI Red Teaming]]
- [[Responsible AI and Governance]]
- [[RAG Portfolio Projects]]
- [[LLM System Design Interview]]
- [[book:20241104-llm-engineer-s-handbook|LLM Engineer's Handbook]]
