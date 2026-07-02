---
layout: wiki
tags: ["roadmap"]
title: "AI Engineering Roadmap"
summary: "A podcast-backed roadmap for learning AI engineering through software foundations, LLM applications, RAG, evaluation, agents, LLMOps, and production ownership."
related:
  - AI Engineering
  - AI Engineer Role
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - Agent Engineering
  - LLM Evaluation Workflows
  - AI Infrastructure
  - MLOps
---

An AI engineering roadmap gives learners a sequence for building software
around models and proving that the software behaves well enough for real users.
DataTalks.Club guests start with product and software ownership, then add
[[LLMs]] and
[[retrieval-augmented-generation|retrieval-augmented generation]].
Later stages add
[[LLM evaluation workflows]],
[[agent engineering]], and
production operation.

[[person:pauliusztin|Paul Iusztin]] puts full-stack
product work and [[retrieval-augmented-generation|RAG]] in one skill stack.
He also includes agents, evaluation, and LLMOps in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]],
especially 22:29-42:28. [[person:ruslanshchuchkin|Ruslan Shchuchkin]]
frames the same role around product discovery, context management, and usable
applications in
[[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]],
7:51-23:19. For the role boundary, use
[[AI Engineer Role]]. For the
broader discipline, use [[AI Engineering]].
The editorial [[ai-engineering-roadmap|AI Engineer Roadmap]]
turns this sequence into concrete build stages with portfolio milestones.

## Roadmap Boundary

Learners enter AI engineering when model use becomes product engineering. AI
engineers build product software around model behavior by calling models,
managing context, evaluating outputs, and operating the resulting product.

Paul describes this as a full-stack AI engineer skill stack. His stack spans
frontend, backend, and database work. It then adds RAG and agents. Deployment,
evaluation, and LLMOps come next in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his skill-stack discussion]],
22:29-42:28.

The shared sequence treats AI engineering as applied product work, not only
prompt writing. Ruslan's BranchGPT example combines a web application, context
management, and user behavior in
[[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|his role episode]],
7:51-10:41. [[person:nasserqadri|Nasser Qadri]] keeps
precision, recall, and accuracy in view when generative AI systems replace older
ML workflows in
[[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
7:45-7:55.

Learners need more than a list of tools. You learn
[[software engineering]]
because AI products still need services, storage, tests, and deployment. You
also learn [[prompt engineering]]
and [[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]].
Then add [[LLM Production Patterns]]
and [[MLOps]].

Model behavior depends on context and examples, plus traces, data, and release
discipline.

## Roadmap Emphasis

Guests mostly differ on how wide the roadmap should be and where learners
should start.

Paul starts from the full-stack builder path. In his version, product shipping
includes backend and frontend work. It also includes database design and data
work. RAG, agents, and evaluation belong in the shipping skill set too.
Monitoring belongs there too
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul Iusztin's AI engineering episode]],
12:09-46:31).

Ruslan starts from product discovery and context management. His version rewards
people who translate business needs into usable AI features. It also rewards
people who watch the tooling landscape without confusing tools for product
judgment
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]],
19:40-23:19 and 57:39-1:03:12).

Nasser keeps the role close to data science and statistical rigor. He also
emphasizes domain knowledge. He uses healthcare and finance examples to make
that point. National-security examples show the same domain-specific evaluation
constraint
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
7:45-10:12).

[[person:revathyramalingam|Revathy Ramalingam]]
shows a career-break path where learning in public and a telecom ML capstone
become evidence of readiness. She also used AI-assisted prototypes, interview
practice, and a PDF Q&A assistant
([[podcast:s23e04-how-to-become-ai-engineer-after-career-break|How to Become an AI Engineer After a Career Break]],
11:00-44:30).

[[person:hugobowneanderson|Hugo Bowne-Anderson]] starts
from practical LLM engineering. His path covers prompts, structured outputs,
gold tests, and traces. The same discussion later covers RAG and failure
analysis
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
13:56-27:38 and 44:26-56:21).

[[person:ranjithakulkarni|Ranjitha Kulkarni]]
starts from agentic systems. Tools and memory define that work, while context
engineering and outcome-based tests matter too
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
11:00-37:39 and 51:17-57:23).

[[person:bartoszmikulski|Bartosz Mikulski]]
starts from production AI. His version combines data trust, pipeline tests, and
prompt evaluation. It also covers caching, compression, and latency control
([[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-31:45).

## Stage 1: Build Normal Software

Start with ordinary application engineering by building a small service and one
interface or API. Add persistence, logs, and tests before you add complex AI
architecture. Paul's roadmap places product shipping and frontend work inside
the AI engineering stack. Backend work and databases belong there too. So do
deployment and monitoring
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his skill-stack episode]],
22:29-42:28).

Ruslan's BranchGPT example shows why this stage comes first. The project needed
an application structure and context-management behavior, not only a model call
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]],
7:51-10:41). For this stage, use
[[Notebook to Production AI Systems]],
[[AI Infrastructure]], and
[[Machine Learning for Software Engineers]].

## Stage 2: Add LLM Calls and Structured Outputs

After the application shell works, add model calls and make the model output
inspectable. Hugo uses everyday LLM tasks and role prompts as an early
practical path. He also covers transcript workflows, structured outputs, and
traces in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
13:56-27:38.

Build a narrow product, not a generic chatbot. The learner should show the user
task, the prompt or message format, the expected output format, and the failure
cases. Ruslan's daily-life project advice and hiring
signals support that project-first standard
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]],
48:48-57:39). For tool choices, connect this stage to
[[LLM Tools]] and
[[Prompt Engineering]].

## Stage 3: Build Evaluation Before More Architecture

Create a representative test set and define pass/fail criteria, then categorize
errors before adding retrieval, agents, or fine-tuning. Paul calls evaluation one
of the technical pillars for shipping AI products
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul Iusztin's AI engineering episode]],
38:41-42:28). Nasser's metric framing keeps precision, recall, and accuracy in
view for generative systems
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
7:45-7:55).

Hugo adds gold tests, traces, and failure analysis to early LLM engineering.
They belong there, not only after production launch
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
13:56-27:38). Use [[LLM Evaluation Workflows]]
and [[Evaluation]] for the detailed
evaluation mechanics.

## Stage 4: Add Retrieval When Knowledge Is the Bottleneck

Add [[retrieval-augmented-generation|RAG]] when the product needs changing
knowledge, private documents, citations, or auditable source context. Paul puts
RAG and knowledge management inside the AI engineer stack at 29:12 in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his skill-stack episode]].

[[person:meryemarik|Meryem Arik]] draws the production
boundary between retrieval and fine-tuning. She also compares open-source models
with hosted APIs in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
16:48-51:35. [[person:atitaarora|Atita Arora]] explains
RAG as retrieval plus generation. She then covers chunking, citations, and
human-in-the-loop evaluation in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
30:38-48:09.

A good roadmap project at this stage includes ingestion, chunking, and
metadata. It also includes embeddings, retrieval, citations, and retrieval
failure analysis. Compare the choices through
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]],
[[Search and RAG Project Checklist]],
and [[RAG Portfolio Projects]].

## Stage 5: Add Agents Only for Tool-Using Work

Move from RAG to agents when the user task needs planning or tools. Agents can
also fit tasks that need memory or multi-step action. Ranjitha defines agents
through autonomy and objectives. She then adds tools, memory, and knowledge
stores. Her discussion also covers context engineering, planning, and
outcome-based tests in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
11:00-37:39 and 51:17-57:23.

[[person:micheallanham|Micheal Lanham]] gives a more
minimal engineering rule. Decompose the task and avoid unnecessary complexity
when a simpler workflow works
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to Modern AI Agents]],
20:57-33:25). For this stage, use
[[Agent Engineering]],
[[agent-engineering|AI Agents]], and
[[multi-agent-systems|Multi-Agent Systems]].

An agent project should show tool contracts, typed inputs, and permissions. It
should also show timeouts, traces, mocked-tool tests, and outcome assertions.
Ranjitha's testing guidance supports outcome-based checks rather than brittle
exact-path tests
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
51:17-57:23).

## Stage 6: Operate the System

Operate the product by versioning prompts, retrieval data, examples, and traces.
Add monitoring, feedback capture, and cost checks when the product has users.
Add latency work, safety tests, and rollback paths too. Bartosz connects
production AI to data pipeline tests and prompt evaluation. He also covers
compression, caching, and latency in
[[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-31:45.

[[person:marianosemelman|Mariano Semelman]] ties
end-to-end AI ownership to requirements and deployment. He also covers
monitoring and feedback in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]],
17:27-49:55. [[person:adityagautam|Aditya Gautam]]
adds agent guardrails and data lineage. He also covers feedback iteration and
LLM judge alignment in
[[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]],
30:26-50:18. For this stage, use
[[AI Red Teaming]],
[[Security]], and
[[Responsible AI and Governance]].

## Portfolio Project Sequence

Start with a focused model-backed task assistant for a specific user task.
Include deployment, logs, structured input and output, and tests. Paul's
full-stack framing makes this the first portfolio step in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]],
22:29-42:28. Ruslan's BranchGPT example shows the same choice in
[[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|his role episode]],
7:51-10:41.

Then build an evaluation harness with representative examples and pass/fail
criteria. Add failure categories, cost notes, and latency notes. Hugo's
gold-test workflow anchors this stage in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
13:56-27:38. Nasser's metric discipline adds precision, recall, and accuracy in
[[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
7:45-7:55.

Next, build a RAG assistant with ingestion, chunking, and metadata. Add
embeddings, retrieval, citations, and failure analysis. Meryem's deployment
tradeoffs define the retrieval and fine-tuning boundary in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
16:48-51:35. Atita's search-grounded RAG discussion adds chunking, citations,
and human review in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
30:38-48:09.

After that, build a constrained tool-using workflow with permissions, timeouts,
and traces. Add mocked tools and outcome assertions. Ranjitha's agent testing
guidance explains why outcome assertions belong in the project in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
51:17-57:23. Micheal's minimal workflow advice keeps the project constrained in
[[podcast:from-game-ai-to-modern-ai-agents|From Game AI to Modern AI Agents]],
20:57-33:25.

Build the capstone as a production-style AI product with versioned prompts and
evaluation history. Add monitoring and feedback capture. Include cost controls,
caching, rollback notes, and an operating note.

Bartosz's production AI episode ties the capstone to pipeline tests and prompt
evaluation. It also covers latency in
[[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-31:45. Mariano's notebook-to-production framing adds requirements and
deployment. He also covers monitoring and feedback in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]],
17:27-49:55.

Nasser's domain-knowledge discussion supports domain-specific projects. A
learner should explain user context, data limits, and evaluation criteria
instead of shipping a generic demo
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
8:26-10:12). Revathy's telecom capstone supports the same standard in
[[podcast:s23e04-how-to-become-ai-engineer-after-career-break|How to Become an AI Engineer After a Career Break]],
15:37-44:30.

## Study-Build Boundary

Start building when you can write a small service and call an LLM API. You
should also be able to parse structured output, store data, and write tests
around expected behavior. Paul and Ruslan both describe AI engineering through
shipped applications rather than passive study
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's skill-stack episode]],
22:29-42:28). Ruslan's BranchGPT discussion gives the same signal in
[[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]],
7:51-10:41.

Study the next technique when the project exposes that constraint. Add RAG when
source knowledge, citations, or freshness block a useful answer. Add agents when
the task needs tools, planning, and multi-step action.

Add LLMOps and platform work when releases or traces become necessary. Cost
controls, monitoring, and rollback paths can justify the same move. Meryem
covers retrieval and deployment tradeoffs in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
40:46-51:35. Ranjitha covers the agent-readiness boundary in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
29:30-37:39. Bartosz covers production constraints in
[[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-31:45.

## Career Readiness Milestones

Entry-level readiness means you can ship a small LLM application. You can also
create a representative evaluation set, explain failures, and deploy a usable
prototype. Paul's full-stack AI skills define the application side of this
milestone
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|Paul's skill-stack episode]],
22:29-42:28). Hugo's early evaluation work adds gold tests and traces
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
13:56-27:38).

Mid-level readiness means you can own a RAG or constrained agent workflow. You
can choose models and retrieval strategies, debug bad outputs, and track cost
and latency. You can also work with domain experts. Meryem's deployment choices
cover the model, retrieval, and serving decisions behind this stage
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
16:48-51:35).

Atita's retrieval-quality discussion adds search-system judgment
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
30:38-48:09). Ranjitha's agent tests add the agent side
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
51:17-57:23). Nasser's domain-knowledge framing adds the domain side
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]],
8:26-10:12).

Senior readiness means you can design the AI product architecture and set
evaluation standards. You can manage security and governance tradeoffs. You can
also guide model choices and connect AI systems to data and MLOps platforms.
Bartosz's
production discipline defines the reliability side of this stage
([[podcast:production-ready-ai-engineering|Production AI Engineering]],
9:05-31:45).

Aditya's agent-governance framing adds guardrails and lineage. It also adds LLM
judge alignment
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]],
30:26-50:18). Mariano's end-to-end ownership adds requirements and deployment.
He also covers monitoring and feedback
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]],
17:27-49:55).

## Related Pages

Continue with these roadmap and reference pages:

- [[AI Engineering]]
- [[AI Engineer Role]]
- [[LLMs]]
- [[LLM Production Patterns]]
- [[Prompt Engineering]]
- [[LLM Evaluation Workflows]]
- [[Evaluation]]
- [[retrieval-augmented-generation|RAG]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[RAG Portfolio Projects]]
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
- [[Agent Engineering]]
- [[agent-engineering|AI Agents]]
- [[multi-agent-systems|Multi-Agent Systems]]
- [[AI Infrastructure]]
- [[AI Red Teaming]]
- [[Security]]
- [[Responsible AI and Governance]]
- [[MLOps]]
- [[MLOps Roadmap]]
- [[Notebook to Production AI Systems]]
