---
layout: wiki
title: "AI Engineering Roadmap"
summary: "A podcast-backed roadmap for learning AI engineering through software foundations, LLM applications, RAG, evaluation, agents, LLMOps, and production ownership."
related:
  - AI Engineering
  - AI Engineer Role
  - LLM Production Patterns
  - RAG
  - Agent Engineering
  - LLM Evaluation Workflows
  - AI Infrastructure
  - MLOps
---

An AI engineering roadmap is a learning sequence for building software around
models. It also teaches you to prove that the software behaves well enough for
real users. In the DataTalks.Club archive, the role starts with product and
software ownership rather than prompt tricks. [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})
puts full-stack product work and [RAG]({{ '/wiki/rag/' | relative_url }}) in
one skill stack. He also includes agents, evaluation, and LLMOps in
[Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }})
frames the role around product discovery, context management, and building
usable applications in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).

Use this roadmap as a build order. Start with
[software engineering]({{ '/wiki/software-engineering/' | relative_url }})
because AI products still need APIs, data stores, tests, and deployment paths.
Then add [LLMs]({{ '/wiki/llms/' | relative_url }}) and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).
After that, add [LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}), and
production operation.

## Link Map

Use these pages while moving through the roadmap:

- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}) for the
  role boundary and guest disagreements.
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
  for model choice, RAG, agents, and feedback loops.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
  and [Evaluation]({{ '/wiki/evaluation/' | relative_url }}) for gold sets and
  failure analysis.
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
  [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}),
  and [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
  for context and knowledge-system decisions.
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
  [AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), and
  [Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }})
  for tool-using workflows.
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}),
  [MLOps]({{ '/wiki/mlops/' | relative_url }}), and
  [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
  for deployment, monitoring, and ownership.

Start with these podcast discussions:

- [Paul Iusztin's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})
- [Ruslan Shchuchkin's role episode]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})
- [Nasser Qadri on understanding the role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }})
- [Revathy Ramalingam on a project-led transition]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }})
- [Hugo Bowne-Anderson on practical LLM engineering]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
- [Ranjitha Kulkarni on agentic systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
- [Bartosz Mikulski on production AI]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})

## Common Sequence

Move through these stages in order.

## Stage 1: Build Normal Software

Start with backend code, HTTP APIs, persistence, and tests before deployment.
Paul includes product shipping in the AI engineering stack
([Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
22:29-42:28). Ruslan's BranchGPT example shows the same boundary because it
uses product behavior and context management
([Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}),
7:51-10:41).

## Stage 2: Add LLM Calls

Once the application shell exists, add model calls and make the output
inspectable. [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
uses everyday LLM tasks and role prompts as the practical starting point. He
also covers structured outputs and transcript workflows in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
Use [prompt engineering]({{ '/wiki/prompt-engineering/' | relative_url }}) to
guide that workflow.

## Stage 3: Build Evaluation

Create a representative test set and define pass/fail criteria, then categorize
errors before adding more architecture. Paul calls evaluation one of the most
important AI engineering skills
([Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
38:41-41:39). [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }})
keeps precision, recall, and accuracy in view for generative AI systems
([Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}),
7:45-7:55). Use [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for the mechanics.

## Stage 4: Add Retrieval

Add RAG when the system needs changing knowledge or citations. Proprietary
documents and inspectable source evidence are also strong retrieval signals.
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) draws the production
boundary in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).

Fine-tuning changes model behavior or specialization, while retrieval fits
changing knowledge and grounded responses. [Atita Arora]({{ '/people/atitaarora/' | relative_url }})
connects RAG to retrieval and generation. She also covers citations and human
review in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
30:38-48:09.

## Stage 5: Add Agents

Move from RAG to agents when the product needs planning or tool use.
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) defines
agents through autonomy and objectives. She also includes tools, memory, and
knowledge stores in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
11:00-12:31.

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) emphasizes
minimalism and task decomposition in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
20:57-33:25.

## Stage 6: Operate the System

Track prompt versions, retrieval data, and traces. Watch monitoring and
feedback, then add cost checks, safety tests, and rollback paths.
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) connects
production AI to data pipeline tests and prompt evaluation. He also covers
compression, caching, and latency in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
9:05-31:45.

[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) ties
end-to-end AI ownership to requirements and deployment. Monitoring plus
feedback loops appear in the same discussion in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
17:27-49:55.

## Guest Differences

Guests agree that AI engineering is product engineering around models, but they
start from different constraints.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) emphasizes a
full-stack builder path. He treats backend work and frontend work as product
surfaces. Data work, RAG, and agents are shipping tools too. See
[Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})
at 12:09-46:31.

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }})
starts from product discovery and context management. His roadmap rewards
people who can translate business needs into usable AI features. See
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})
at 19:40-23:19.

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) keeps the role close
to data science and domain knowledge. Evaluation can depend on healthcare,
finance, or national-security context
([Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}),
8:26-10:12). [Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }})
shows a career-break route built around learning in public and a telecom ML
capstone. She also used AI-assisted prototypes, interview practice, and a PDF
Q&A assistant
([How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }}),
11:00-44:30).

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) starts
from fast practical loops. His path combines prompts and RAG with gold tests,
traces, and failure analysis
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
13:56-27:38 and 44:26-56:21).

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
starts from agentic workflows. Tools and memory define that work, while context
engineering and outcome-based tests matter too
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
21:21-37:39 and 51:17-57:23).

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }})
starts from production discipline. Data trust and prompt evaluation sit
alongside caching, compression, and latency control
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
9:05-31:45).

## Practical Project Sequence

Build projects in this order:

1. Build a model-backed task assistant for one user task and one interface.
   Add deployment with logs, structured I/O, and tests while following Paul's
   product-shipping framing and Ruslan's application examples.
2. Build an evaluation harness with representative examples and pass/fail
   criteria, then add failure categories, cost notes, and latency notes. This
   follows Hugo's gold-test workflow and Nasser's metric discipline.
3. Build a RAG assistant with ingestion, chunking, metadata, embeddings,
   retrieval, citations, and failure analysis. This follows Meryem's
   retrieval-versus-fine-tuning boundary and Atita's search-grounded RAG
   discussion.
4. Build a constrained tool-using workflow with typed inputs, timeouts,
   permissions, traces, mocked-tool tests, and outcome assertions. This follows
   Ranjitha's agent testing guidance and Micheal's minimal workflow advice.
5. Build a production-style capstone with versioned prompts, evaluation
   history, monitoring, and feedback capture. Add cost controls, caching,
   rollback notes, and an operating note. Bartosz's production AI episode and
   Mariano's notebook-to-production framing support this capstone.

Make each project domain-specific because generic demos don't show judgment.
Nasser's domain-knowledge discussion and Revathy's telecom capstone both show
that standard. The builder should explain user context, data limits, and
evaluation criteria. Those choices matter more than the framework. See
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }})
at 8:26-10:12 and
[How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }})
at 11:00-44:30.

## Study-Build Boundary

Stop studying and build when you can write a small service and call an LLM API.
You should also be able to parse structured output and store data. Write tests
and define examples that should pass or fail. The archive supports this
boundary because Paul and Ruslan both describe AI engineering through shipped
applications.

Hugo places evaluation and traces inside early builder loops. Paul supports the
same boundary through full-stack shipping examples, while Ruslan supports it
through application examples and product context. See
[Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})
at 22:29-42:28. See
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})
at 7:51-10:41. See
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 13:56-27:38.

Study the next technique when your project exposes that constraint. Add RAG
when source knowledge, citations, or freshness become the bottleneck. Add agents
when the workflow needs tools and multi-step action.

Add LLMOps and platform work when repeatable releases or traces become
necessary. Cost controls can justify the same move. Add monitoring and rollback
when the system has production users.

Meryem explains the retrieval and deployment tradeoffs in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 40:46-51:35. Ranjitha adds the agent-readiness boundary in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
at 29:30-37:39. Bartosz adds production AI constraints in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})
at 9:05-31:45.

## Role Milestones

Entry-level readiness means you can ship a small LLM application. You can also
create a representative evaluation set, explain failures, and deploy a usable
prototype.
That maps to Paul's entry path through full-stack AI skills and Hugo's early
evaluation loop. See
[Paul's skill-stack episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})
at 22:29-42:28 and
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 13:56-27:38.

Mid-level readiness means ownership of a RAG or constrained agent workflow. The
work includes model choices and retrieval choices. It also includes cost
tracking, debugging bad outputs, and collaboration with domain experts.

Meryem's deployment choices and Atita's retrieval-quality discussion support
this stage. Ranjitha's agent tests and Nasser's domain-knowledge framing support
it too.

Meryem's deployment discussion covers the first part in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
at 16:48-51:35. Atita's search episode covers retrieval quality in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 30:38-48:09. Ranjitha covers agent tests in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
at 51:17-57:23. Nasser covers domain knowledge in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }})
at 8:26-10:12.

Senior readiness means you can design the AI product architecture and set
evaluation standards. You can manage security and governance tradeoffs. You can
guide model choices and connect AI systems to data and MLOps platforms.

Bartosz's production discipline supports this stage. Aditya Gautam's
agent-governance framing and Mariano's end-to-end production ownership support
it too. See
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})
at 9:05-31:45,
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
at 30:26-50:18, and
[From Notebook to Production: Building End-to-End AI Systems]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
at 17:27-49:55.

## Related Pages

Continue with these related pages:

- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [RAG]({{ '/wiki/rag/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [AI Agents]({{ '/wiki/ai-agents/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
- [Machine Learning for Software Engineers]({{ '/guides/machine-learning-for-software-engineers/' | relative_url }})
- [LLM Tools]({{ '/guides/llm-tools/' | relative_url }})
