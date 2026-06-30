---
layout: wiki
title: "LLM Production Patterns"
summary: "How DataTalks.Club guests turn LLM demos into production systems with model choice, RAG, agents, and evaluation."
related:
  - LLMs
  - Retrieval-Augmented Generation
  - RAG vs Fine-Tuning
  - LLM Evaluation Workflows
  - Agent Engineering
  - AI Engineer Role
  - AI Red Teaming
  - Notebook to Production AI Systems
---

LLM production work turns a language-model demo into a product feature. In the
DataTalks.Club archive, that work starts with model choice. Teams also decide
between [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) and
[fine-tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}). The work
continues through context packaging and [agents]({{ '/wiki/agent-engineering/' | relative_url }}).

It also includes evaluation and guardrails. Logs, traces, and feedback loops
belong in the same production work.

The archive's useful boundary is that an [LLM]({{ '/wiki/llms/' | relative_url }})
is rarely the whole product. [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
frames production LLM work through deployment and retrieval. She also connects
it to fine-tuning and open-source control. API drift and latency appear in the
same discussion. Cost appears in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) turns
the same idea into a practical loop of prompts, RAG, and gold tests. He adds
failure analysis, logs, and traces in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

## Link Map

Use these pages for the production pieces around this topic:

- [LLMs]({{ '/wiki/llms/' | relative_url }}) for the model-level archive view.
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) for retrieval architecture.
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) for the adaptation decision.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for gold sets, failure analysis, judges, and agent tests.
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) and [AI Agents]({{ '/wiki/ai-agents/' | relative_url }}) for tool-using systems.
- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) and [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) for the role that owns these systems.
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}), [Security]({{ '/wiki/security/' | relative_url }}), and [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}) for safety, auditability, and misuse testing.
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }}) for the broader path from experiments to owned product behavior.

The core podcast discussions are:

- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}) with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
- [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}) with [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
- [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}) with [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
- [The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}) with [Aditya Gautam]({{ '/people/adityagautam/' | relative_url }})
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}) with [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})
- [Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}) with [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }})
- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}) with [Atita Arora]({{ '/people/atitaarora/' | relative_url }})
- [Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}) with [Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }})
- [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}) with [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }})
- [From Notebook to Production: Building End-to-End AI Systems]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}) with [Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }})

## Common Production Approach

The common production approach is to start with the user workflow. Teams build
the smallest reliable LLM system and measure it. They add architecture only
where the measured failures demand it. Hugo gives this directly in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

He introduces generator-evaluator loops at 13:56. He adds representative gold
tests at 23:00 and failure analysis at 26:43.

Logs and traces appear at 27:38. He then moves from RAG to tool use and agents
at 44:26-56:21.

Recent AI engineering episodes keep the same structure. [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})
places RAG and agents inside one AI engineering skill stack in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})
at 29:12-46:31. Evaluation appears in the same skill stack. He also includes
product shipping and queues. Retries, traces, and monitoring sit in the same
shipping discussion.

[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }})
connects modern AI products back to end-to-end ownership in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
Requirements and data still matter at 17:27-21:12 in that episode. Deployment,
monitoring, and feedback matter at 41:28-49:55.

The archive therefore treats "production LLM" as a system design question
rather than a model-selection label. The model sits inside
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and [evaluation]({{ '/wiki/evaluation/' | relative_url }}).
It also sits inside product feedback loops, as shown by Hugo's evaluation
workflow, Meryem's deployment tradeoffs, and Mariano's notebook-to-production
framing.

## Guest Differences

Guests differ on the first constraint they optimize. Meryem starts with the
deployment surface, where open-source models give more control and privacy. API
models can still hide behavior changes behind provider updates
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
16:48-18:46). Her approach is to choose the model and serving path
around control, fine-tuning, latency, and cost.

Hugo starts with builder iteration. His approach turns prompts, RAG, and
structured outputs into an evaluation loop before adding more moving parts
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
13:56-27:38 and 44:26-50:19). [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
starts from workflow automation. Context engineering, tools, and memory define
the agent surface. Agentic readiness depends on mocked tool tests and outcome
assertions
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
21:21-37:39 and 51:17-57:23).

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) starts from
enterprise reliability. He ties agents to guardrails and data lineage, then
connects them to feedback and multi-tenancy.

He covers human-aligned evaluation in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
at 30:26-50:18. [Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }})
starts from adversarial trust questions. Prompt injection and data
exfiltration appear before any claim that a chatbot is production ready. Output
validation and non-LLM classifiers appear in the same security framing
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
9:28-17:00).

## Model Choice and Serving

A production LLM system starts with the serving boundary. The team may use a
hosted API or a self-hosted open-source model. They may also use a fine-tuned
variant or a mix.

Meryem's episode anchors this decision. At 16:48-25:26 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she links model-source choices to control and privacy. Fine-tuning is
part of the same model-choice discussion. She also covers model size,
compression, and inference optimization. At

49:44-51:35, she separates prototype convenience from production choices around
self-hosting and hardware. Latency or cost can decide the same choice.

[Sandra Kublik]({{ '/people/sandrakublik/' | relative_url }}) gives a product
version of the same tradeoff in
[Practical LLM Use Cases]({{ '/podcasts/practical-llm-use-cases-and-product-patterns/' | relative_url }}).
Business applications need model, architecture, and integration choices. They
also need cost and latency decisions at 32:28-35:28. Sandra also names
proprietary-data and IP concerns.
That connects model choice to
[AI infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) and
[data governance]({{ '/wiki/data-governance/' | relative_url }}), not only to
benchmark scores.

## RAG, Fine-Tuning, and Context

The archive's clearest architecture boundary is that retrieval handles changing
knowledge, while fine-tuning changes model behavior, style, or task performance.
Meryem states this boundary in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
Fine-tuning appears with specialization and domain adaptation at 26:30-31:38.
Tone and format are part of the same discussion.

Retrieval appears with changing knowledge and indexes at 40:46-46:42. Meryem
also discusses grounded responses and summarizers in that section.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) adds the search
engineering version in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38-42:49, she describes RAG as retrieval plus generation. She then walks
through chunking, overlap, embeddings, and vectorization. She also connects
retrieval to prompt design and citations. That's why production RAG belongs with
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
as much as it belongs with LLM prompts.

Context engineering is the practical middle layer between "just prompt it" and
"build an autonomous agent." Ranjitha names context engineering at 21:21 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
and then warns at 29:30-32:48 that RAG still has latency and cost problems.
She also names noisy context and garbage-in-garbage-out. Chunking, metadata,
and wrapper problems appear in the same discussion.

[Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }})
adds the long-context reason to keep this layer explicit in
[Applied LLM Research]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}).
Her 10:15-14:54 discussion of financial long-context evaluation shows that
large context windows can still degrade on specialized documents. Chunking,
retrieval, and summarization remain useful in that setting.

## Tool Use and Agents

Agents fit workflows where the LLM must do more than answer from context.
Ranjitha defines agents around autonomy and objectives at 11:00-12:31 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
She also includes orchestration, tools, memory, and knowledge stores.
At 36:11-37:39, she separates retrieval as one tool from the cases where the
system needs planning or action.

Tools should be constrained and testable. Ranjitha discusses SDKs, tool
wrappers, and integration abstractions at 18:23-24:59. She later adds mocked
tools, integration tests, regression tests, and outcome assertions at
51:17-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) adds a
minimalist agent-design boundary in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}):
task decomposition and sequential workflows appear at 20:57-23:48. Manager-agent
orchestration, Agent SDKs, and MCP-style integrations appear at 23:48-33:25.

This keeps agent work close to [tools]({{ '/wiki/tools/' | relative_url }}),
[orchestration]({{ '/wiki/orchestration/' | relative_url }}), and
[testing]({{ '/wiki/testing/' | relative_url }}). A production agent isn't only
a prompt. It's a bounded workflow with permissions and callable interfaces. It
also needs retrieval, state, evaluation, and rollback paths.

## Evaluation and Feedback Loops

Production LLM systems need evaluation before launch and feedback after launch.
Hugo's episode gives the base workflow in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 13:56-27:38. That workflow includes generator-evaluator loops and structured
checks. It also includes gold tests and failure categories.

Logging appears in the same workflow. Hugo's operational point is that teams
should know where the next fix belongs. It may belong in retrieval or prompting.
It may also belong in data preparation, formatting, or product scope.

Agent systems extend that evaluation into software behavior. Ranjitha argues
for custom datasets and system benchmarks in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
at 51:17-57:23. She also covers mocked tools and integration tests. Regression
tests and outcome-based assertions matter in the same section.

Aditya adds the enterprise layer in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
at 38:49-50:18. He covers golden datasets, thresholds, and LLM judges aligned
with human labels. He also covers feedback loops, multi-tenancy, and scale.

Feedback can also be a product signal. Mariano discusses explicit and implicit
feedback loops at 41:28 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
He then shows how generated media for e-commerce sellers used customer
requirements and factuality checks at 47:22-58:45. Mariano also covers prompt
engineering, Arize, and MLflow. His example links LLM production to
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and
[data products]({{ '/wiki/data-products/' | relative_url }}).

## Guardrails, Security, and Human Review

Production LLM systems need controls around user input and retrieved context.
They also need controls around generated output and tool calls. Maria's chatbot
security episode is the clearest source. She describes a large-scale hacking
exercise at 9:28 in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).

She then covers legal and financial exposure from hallucinations at 11:38. Data
exfiltration through prompt overload and knowledge-base retrieval appears at
13:20.

Maria discusses layered defenses at 16:15-17:00.

Maria's use of output validation, query analysis, and non-LLM classifiers
connects this page to [AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
and [security]({{ '/wiki/security/' | relative_url }}).

Human review matters when mistakes create brand or legal risk. Safety and
customer risk matter too. Sandra discusses hallucinations and brand safety at
23:29 in
[Practical LLM Use Cases]({{ '/podcasts/practical-llm-use-cases-and-product-patterns/' | relative_url }}),
where she also covers editorial curation. Maria discusses moderation support and
human review for higher-risk outputs at 25:34 in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).

Aditya's agent governance discussion adds auditability, guardrails, lineage,
and compliance for enterprise settings at 30:26 in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}).

## Cost, Latency, and Operability

Cost and latency are design constraints because LLM systems spend tokens in many
places. Prompts, retrieved context, and judge calls all add runtime. Tool calls,
retries, and multi-step agent loops add runtime too. Meryem covers serving
efficiency, compression, and hardware in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 25:26 and 51:35. She also covers latency and cost.

Ranjitha adds the RAG version at 29:30 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}):
retrieval and context quality affect whether a system is usable. Latency and
cost affect that decision too. The same constraints apply to agents in her
workflow discussion.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) contributes
the application-engineering view in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 28:16-31:45, he connects prompt evaluation, prompt compression, and caching
to model efficiency. At 41:04-47:19, he discusses backend AI integrations and
browser extension architecture. Search assistants and tool selection appear in
the same section.

Those examples make production LLM work a [software engineering]({{ '/wiki/software-engineering/' | relative_url }})
and [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) problem,
not only a prompt-writing problem.

## Practical Production Checklist

Use this checklist as a reading guide for the archive-backed practices above:

- Define the user workflow and failure cost before choosing an LLM design, as
  Mariano argues for end-to-end AI ownership in
  [From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
  at 17:27-21:12.
- Choose API, open-source, self-hosting, or fine-tuned variants using control
  and privacy needs, including API drift and cost from Meryem's production
  framing in
  [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
  at 16:48-25:26 and 49:44-51:35.
- Use RAG for changing source knowledge and citations. Reserve fine-tuning for
  behavior or repeated task gaps, following
  [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) and
  Meryem's 26:30-46:42 discussion.
- Make context explicit with chunking and metadata. Include wrappers and
  citations, then add retrieval evaluation, following Atita's
  [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
  discussion at 30:38-48:09 and Ranjitha's context-engineering discussion at
  21:21-32:48.
- Add agents only when the workflow needs planning, tool calls, or memory. Use
  them for actions beyond retrieval, following Ranjitha's 36:11-37:39 boundary
  and Hugo's 50:19-56:21 escalation path.
- Build evaluation into the loop with representative gold tests and failure
  categories, keeping logs and traces in the same loop. Agent systems also need
  mocked tools plus outcome assertions, following
  [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
  Hugo's 13:56-27:38 workflow, and Ranjitha's 51:17-57:23 agent tests.
- Add security controls, red-team cases, and output validation. Include
  permissions, audit trails, and human review where risk demands it, following
  Maria's
  [Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
  discussion at 9:28-17:00 and Aditya's governance discussion at 30:26.
- Keep cost, latency, caching, prompt size, serving, and monitoring visible,
  following Bartosz's
  [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})
  at 28:16-31:45 and Meryem's serving discussion at 25:26-51:35.

## Related Pages

Continue with these pages for adjacent production work:

- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
- [AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }})
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [LLM System Design Interview]({{ '/articles/llm-system-design-interview/' | relative_url }})
