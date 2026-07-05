---
layout: article
tags: ["roadmap"]
title: "AI Engineering Roadmap"
keyword: "ai engineering roadmap"
summary: "A roadmap for learning AI engineering through software foundations, LLM applications, RAG, evaluation, agents, LLMOps, and production ownership."
related_wiki:
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
A practical path starts with product and software ownership, then adds [[LLMs]]
and
[[retrieval-augmented-generation=>retrieval-augmented generation]].
Later stages add
[[LLM evaluation workflows]],
[[agent engineering]], and
production operation.

[[person:pauliusztin=>Paul Iusztin]] puts full-stack
product work and [[retrieval-augmented-generation=>RAG]] in one skill stack.
He also includes agents, evaluation, and LLMOps in
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].

[[person:ruslanshchuchkin=>Ruslan Shchuchkin]]
frames the same role around product discovery, context management, and usable
applications [[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]].
For the role boundary, use
[[AI Engineer Role]]. For the
broader discipline, use [[AI Engineering]].

## From Product App To AI System

The first learning step is still product software. Paul describes the starting
point as a full-stack AI engineer skill stack. It starts with frontend, backend,
and database work. Then it adds RAG, agents, deployment, and evaluation. LLMOps
comes after that
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].

Ruslan's BranchGPT example keeps the same sequence grounded in a concrete
application. The product starts as a web application, then adds context
management and user behavior in
[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]].
[[person:nasserqadri=>Nasser Qadri]] keeps
precision, recall, and accuracy in view when generative AI systems replace older
ML workflows [[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]].

That makes the order clear. Learn [[software engineering]] first, then
[[prompt engineering]] and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]. After that,
add [[LLM Production Patterns]], evaluation, and [[MLOps]].

## Entry Paths Into The Roadmap

Different learners can enter the same sequence from different strengths:

- Full-stack builders can start at Stage 1, then add RAG, agents, evaluation,
  and monitoring as product features
  ([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
- Product and domain switchers can start with Stage 1 and Stage 2. Then use
  [[AI Engineer Role]] and
  [[nontraditional-paths-to-ai-engineering=>nontraditional paths to AI engineering]]
  for AI product proof
  ([[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]])
  ([[cite:s23e04-how-to-become-ai-engineer-after-career-break=>Career Break to AI Engineer]]).
- Data-science learners should keep Nasser's metric and domain-evaluation
  discipline visible while moving through the LLM, RAG, and evaluation stages
  ([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).
- Agent-focused learners shouldn't skip prompts, structured outputs, gold
  tests, traces, and RAG before adding tools and memory
  ([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]])
  ([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
- Production-focused learners should deepen the later stages with data trust,
  pipeline tests, and prompt evaluation. Caching, compression, and latency
  control belong there too
  ([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

## Stage 1: Build Normal Software

Start with ordinary application engineering by building a small service and one
interface or API. Finish this stage with persistence, tests, and deployment. Add
a basic monitoring path before complex AI architecture. Paul's
roadmap keeps product shipping, application layers, databases, and deployment
inside the AI engineering stack. Monitoring belongs there too
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@22:29=>AI Engineering Skill Stack]]).

Ruslan's BranchGPT example shows why this stage comes first. The project needed
an application structure and context-management behavior, not only a model call
([[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]]).
For this stage, use
[[Notebook to Production AI Systems]],
[[AI Infrastructure]], and
[[machine-learning-for-software-engineers=>machine learning for software engineers]].

## Stage 2: Add LLM Calls and Structured Outputs

After the application shell works, add model calls and make the model output
inspectable. Hugo uses everyday LLM tasks and role prompts as an early
practical path. He also covers transcript workflows, structured outputs, and
traces [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Build a narrow product, not a generic chatbot. The learner should show the user
task, the prompt or message format, the expected output format, and the failure
cases. Ruslan's daily-life project advice and hiring
signals support that project-first standard
([[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]]).

The same project boundary shows up in
[[llm-system-design-interview=>LLM system design interview]] practice. Candidates
need to explain the user task, source of truth, and context. They also need
failure modes and operating constraints.
For tool choices, connect this stage to
[[LLM Tools]] and
[[Prompt Engineering]].

## Stage 3: Build Evaluation Before More Architecture

Create a representative test set and define pass/fail criteria, then categorize
errors before adding retrieval, agents, or fine-tuning. Paul calls evaluation one
of the technical pillars for shipping AI products
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
Nasser's metric framing keeps precision, recall, and accuracy in
view for generative systems
([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).

Hugo adds gold tests, traces, and failure analysis to early LLM engineering.
They belong there, not only after production launch
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Use [[LLM Evaluation Workflows]]
and [[Evaluation]] for the detailed
evaluation mechanics.

## Stage 4: Add Retrieval When Knowledge Is the Bottleneck

Add [[retrieval-augmented-generation=>RAG]] when the product needs changing
knowledge, private documents, citations, or auditable source context. Paul puts
RAG and knowledge management inside the AI engineer stack
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@29:12=>AI Engineering Skill Stack]].

[[person:meryemarik=>Meryem Arik]] draws the production
boundary between retrieval and fine-tuning. She also compares open-source models
with hosted APIs [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
[[person:atitaarora=>Atita Arora]] explains
RAG as retrieval plus generation. She then covers chunking, citations, and
human-in-the-loop evaluation [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

A good roadmap project at this stage includes ingestion, chunking, and
metadata. It also includes embeddings, retrieval, citations, and retrieval
failure analysis. Compare the choices through
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]],
[[Search and RAG Project Checklist]],
and [[RAG Portfolio Projects]].

## Stage 5: Add Agents Only for Tool-Using Work

Move from RAG to agents when the user task needs planning or tools. Agents can
also fit tasks that need memory or multi-step action. Ranjitha defines agents
through autonomy and objectives. She then adds tools, memory, and knowledge
stores. Her discussion also covers context engineering, planning, and
outcome-based tests in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

[[person:micheallanham=>Micheal Lanham]] gives a more
minimal engineering rule. Decompose the task and avoid unnecessary complexity
when a simpler workflow works
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to Modern AI Agents]]).
For this stage, use
[[Agent Engineering]],
[[agent-engineering=>AI Agents]], and
[[multi-agent-systems=>Multi-Agent Systems]].

An agent project should show tool contracts, typed inputs, and permissions. It
should also show timeouts, traces, mocked-tool tests, and outcome assertions.
Ranjitha's testing guidance supports outcome-based checks rather than brittle
exact-path tests
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

## Stage 6: Operate the System

Operate the product by versioning prompts, retrieval data, examples, and traces.
Add monitoring, feedback capture, and cost checks when the product has users.
Add latency work, safety tests, and rollback paths too. Bartosz connects
production AI to data pipeline tests and prompt evaluation. He also covers
compression, caching, and latency [[cite:production-ready-ai-engineering=>Production AI Engineering]].

[[person:marianosemelman=>Mariano Semelman]] ties
end-to-end AI ownership to requirements and deployment. He also covers
monitoring and feedback [[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].
[[person:adityagautam=>Aditya Gautam]]
adds agent guardrails and data lineage. He also covers feedback iteration and
LLM judge alignment [[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]].
For this stage, use
[[AI Red Teaming]],
[[Security]], and
[[Responsible AI and Governance]].

## Portfolio Project Sequence

Start with a focused model-backed task assistant for a specific user task.
Include deployment, logs, structured input and output, and tests. Paul's
full-stack framing makes this the first portfolio step in
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].
Ruslan's BranchGPT example shows the same choice
[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]].

Then build an evaluation harness with representative examples and pass/fail
criteria. Add failure categories, cost notes, and latency notes. Hugo's
gold-test workflow anchors this stage in
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Nasser's metric discipline adds precision, recall, and accuracy
[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]].

Next, build a RAG assistant with ingestion, chunking, and metadata. Add
embeddings, retrieval, citations, and failure analysis. Meryem's deployment
tradeoffs define the retrieval and fine-tuning boundary in
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Atita's search-grounded RAG discussion adds chunking, citations,
and human review in
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

After that, build a constrained tool-using workflow with permissions, timeouts,
and traces. Add mocked tools and outcome assertions. Ranjitha's agent testing
guidance explains why outcome assertions belong in the project in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Micheal's minimal workflow advice keeps the project constrained
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to Modern AI Agents]].

Build the capstone as a production-style AI product with versioned prompts and
evaluation history. Add monitoring and feedback capture. Include cost controls,
caching, rollback notes, and an operating note.

Bartosz ties production AI work to pipeline tests, prompt evaluation, and latency
control
[[cite:production-ready-ai-engineering=>Production AI Engineering]].
Mariano's notebook-to-production framing adds requirements and deployment. He
also covers monitoring and feedback
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

Domain-specific projects need user context, data limits, and evaluation criteria
instead of a generic demo
([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).
Revathy's telecom capstone supports the same standard
[[cite:s23e04-how-to-become-ai-engineer-after-career-break=>Career Break to AI Engineer]].
Use [[ai-engineering-portfolio-projects=>AI engineering portfolio projects]]
when this sequence needs concrete project shapes, review signals, and README
evidence.

## Study-Build Boundary

Start building when you can write a small service and call an LLM API. You
should also be able to parse structured output, store data, and write tests
around expected behavior. Paul and Ruslan both describe AI engineering through
shipped applications rather than passive study
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
Ruslan's BranchGPT discussion gives the same signal
[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]].

Study the next technique when the project exposes that constraint. Add RAG when
source knowledge, citations, or freshness block a useful answer. Add agents when
the task needs tools, planning, and multi-step action.

Add LLMOps and platform work when releases or traces become necessary. Cost
controls, monitoring, and rollback paths can justify the same move. Meryem
covers retrieval and deployment tradeoffs in
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Ranjitha covers the agent-readiness boundary
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Bartosz covers production constraints
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

## Career Readiness Milestones

Entry-level readiness means you can ship a small LLM application. You can also
create a representative evaluation set, explain failures, and deploy a usable
prototype. Paul's full-stack AI skills define the application side of this
milestone
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
Hugo's early evaluation work adds gold tests and traces
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Mid-level readiness means you can own a RAG or constrained agent workflow. You
can choose models and retrieval strategies, debug bad outputs, and track cost
and latency. You can also work with domain experts. Meryem's deployment choices
cover the model, retrieval, and serving decisions behind this stage
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
Candidates use the same model, retrieval, and serving choices in
[[llm-system-design-interview=>LLM system design interview]] preparation.

Atita's retrieval-quality discussion adds search-system judgment
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Ranjitha's agent tests add the agent side
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Nasser's domain-knowledge framing adds the domain side
([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).

Senior readiness means you can design the AI product architecture and set
evaluation standards. You can also manage security and governance tradeoffs.
Model choices, data dependencies, and MLOps platforms become part of the same
work. A [[staff-ai-engineer=>staff AI engineer]] operates at that level when the
work crosses teams and standards without requiring a manager title
([[cite:from-academia-to-staff-ai-engineer-interviews-and-career-growth=>Staff AI Engineer Transition]]).
Bartosz's
production discipline defines the reliability side of this stage
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

Aditya's agent-governance framing adds guardrails and lineage. It also adds LLM
judge alignment
([[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]).
Mariano's end-to-end ownership adds requirements and deployment.
He also covers monitoring and feedback
([[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]).

## Related Pages

Continue with these roadmap and reference pages:

- [[AI Engineering]]
- [[AI Engineer Role]]
- [[ai-engineering-portfolio-projects=>AI engineering portfolio projects]]
- [[LLMs]]
- [[LLM Production Patterns]]
- [[llm-system-design-interview=>LLM system design interview]]
- [[Prompt Engineering]]
- [[LLM Evaluation Workflows]]
- [[Evaluation]]
- [[retrieval-augmented-generation=>RAG]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[RAG Portfolio Projects]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[Agent Engineering]]
- [[agent-engineering=>AI Agents]]
- [[multi-agent-systems=>Multi-Agent Systems]]
- [[AI Infrastructure]]
- [[AI Red Teaming]]
- [[Security]]
- [[Responsible AI and Governance]]
- [[MLOps]]
- [[MLOps Roadmap]]
- [[Notebook to Production AI Systems]]
