---
layout: wiki
title: "AI Engineering"
summary: "Archive-backed guide to AI engineering as the discipline of shipping LLM applications, RAG systems, agents, evaluations, and production AI products."
related:
  - AI Engineer Role
  - AI Engineering Roadmap
  - LLM Production Patterns
  - Search, RAG, and Knowledge Systems
  - Agent Engineering
  - LLM Evaluation Workflows
  - Notebook to Production AI Systems
  - AI Infrastructure
  - MLOps
---

AI engineering turns foundation models into usable software. In the
DataTalks.Club archive, guests describe it as product engineering around models
rather than prompt writing alone. [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})
puts full-stack product work and [RAG]({{ '/wiki/rag/' | relative_url }}) in
one skill stack. He also includes agents, evaluation, and LLMOps in
[Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
especially at 22:29 and 42:28.

Guests also frame AI engineering as a production discipline. [Bartosz
Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) connects production
AI to data pipeline tests and prompt evaluation in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
from 9:05 through 28:16. He then covers compression and caching at 30:00 and
31:45. [Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }})
adds end-to-end ownership in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
where he discusses product-driven AI at 7:18 and ownership at 17:27. He then
covers requirements at 37:39, feedback loops at 41:28, and the move away from
notebooks at 55:28.

## Application Ownership

AI engineers own the application layer around model behavior, and Paul
describes the role as a full-stack builder path. The engineer needs frontend
and backend skill plus database design, RAG, and agents to ship a working
product. Paul also
includes evaluation and deployment in that path
([Paul Iusztin episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
22:29 and 42:28). That puts AI engineering near
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[machine learning engineering]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
and [data engineering]({{ '/wiki/data-engineer-role/' | relative_url }}).

[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) gives the
same ownership a product-builder flavor in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
His BranchGPT discussion at 7:51 and 10:41 treats an AI project as a web
application with context management. It also covers user behavior. His
"universal soldier" chapter at 19:40 places product discovery beside technical
delivery.
For role boundaries, see [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
and [AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }}).

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) keeps the boundary
closer to data science and domain expertise. In
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}),
he connects generative AI evaluation to statistical rigor at 7:45. He contrasts
research mindsets with engineering speed at 12:13 and compares AI roles at big
tech companies and startups at 20:27. His later chapters cover orchestration at
45:50 and latency at 56:10. Those chapters show why AI engineering crosses role
boundaries rather than
replacing every older [data scientist]({{ '/wiki/data-scientist-role/' | relative_url }})
or [ML engineer]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
responsibility.

## Core System Pieces

AI engineers repeatedly work with the application and model layers. They also
handle context and evaluation. They also handle data pipelines, deployment, and
operations. Paul groups RAG and knowledge management with agents. He also
includes evaluation and LLMOps in his shipping
chapters at 29:12 and 42:28
([Paul Iusztin episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})).

Bartosz adds tested data pipelines at 9:05 and 11:47. He returns to prompt
mechanics at 25:13, 28:16, 30:00, and 31:45
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})).

AI engineering is broader than [LLM tools]({{ '/guides/llm-tools/' | relative_url }})
or a framework choice. The engineer has to choose where to put knowledge and
which model behavior to trust. They also need to look at failures and operate
the feature after launch. For related production work, see
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}), and
[MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }}).

Mariano's notebook-to-production discussion adds the product and deployment
concerns. He moves from product-driven AI at 7:18 to end-to-end ownership at
17:27. He then covers business-to-ML requirements at 37:39, feedback loops at
41:28, and image description architecture at 48:26. At 1:02:53, he names a
modern stack with FastAPI, UV, and Arize
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).
For those topics, see
[Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }}),
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
and [machine learning for software engineers]({{ '/guides/machine-learning-for-software-engineers/' | relative_url }}).

## Context, RAG, and Knowledge Systems

AI engineering often starts to differ from ordinary application development when
the model needs private or changing knowledge. Paul calls out RAG and knowledge
management at 29:12, then folds them into the technical pillars for shipping AI
products at 42:28
([Paul Iusztin episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})).
Ruslan's BranchGPT example also shows context management as part of the product
rather than a hidden implementation detail
([Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}),
7:51-10:41).

For deeper retrieval and knowledge-system work, start with
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).
Then compare [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
and [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}).
Use retrieval when a product needs grounded, changing, or auditable knowledge.
Then evaluate retrieval and generation together rather than treating the prompt
as the whole system.

## Evaluation and Reliability

AI engineers need evaluation before they can call a feature production-ready.
Paul names evaluation as one of the technical pillars for shipping AI products
at 42:28
([Paul Iusztin episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})).
Nasser brings older data-science discipline into generative AI. He discusses
statistical rigor at 7:45, then balances research mindsets with engineering
speed at 12:13
([Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }})).

Bartosz makes reliability concrete through tests and examples while tracking
cost and latency.
His production AI episode covers data trust at 9:05 and snapshot plus
integration testing at 11:47. He then covers prompt evaluation at 28:16, prompt
compression at 30:00, and prompt caching at 31:45
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})).
For evaluation workflows, see
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [Evaluation]({{ '/wiki/evaluation/' | relative_url }}). For prompt and
production work, see [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
and [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

Mariano adds feedback loops and monitoring from an end-to-end product view. His
chapters at 41:28 and 1:02:53 cover explicit and implicit feedback plus modern
tools for production AI systems
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).
That makes evaluation an ongoing operating practice, not a final checklist
before launch.

## Agents and Tool Use

AI engineering includes agent engineering for planning and tool use.
Nasser covers agent rigor at 42:05 and orchestration at 45:50 in
[his role episode]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).

Guests treat agents as software systems, not as magic prompts. An AI engineer
has to define tool contracts and permissions. They also define retries, traces,
latency limits, and outcome tests. Use
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) for
deeper agent-specific work.

## Data Pipelines and Deployment

Production AI still depends on data engineering. Bartosz starts his production
discussion with data trust at 9:05. He covers data pipeline tests at 11:47,
testing tools at 13:14, and Spark choices at 17:10. He then connects
preprocessing and fine-tuning data to AI work at 18:38
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})).
For adjacent data work, see [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}), and
[How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }}).

Mariano shows the deployment side through end-to-end AI systems. His chapters
cover ownership at 17:27, requirements at 37:39, and system architecture at
48:26. He also discusses production code at 55:28 and a modern serving and
monitoring stack at 1:02:53
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).
The same operational work runs through [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}), and
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}).

## Career and Learning Signals

Guests point toward project evidence rather than credentials alone. Paul places
AI engineering learning in shipped projects during his generalist-edge chapter
at 32:17 and portfolio chapter at 54:05
([Paul Iusztin episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})).
Ruslan makes the same argument through side projects, local community work,
daily-life project ideas, and hiring signals. He also discusses using AI to
learn at 1:03:12
([Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})).

For a learner, that means a strong AI engineering portfolio should show more
than a chatbot demo. It should show a product problem and a user interface or
API. It should also show context strategy, evaluation cases, and deployment
notes. Add monitoring or feedback plus a tradeoff around latency or cost. Data
quality and model choice are also useful tradeoffs.

Use [AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }}),
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }}),
and [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
for project sequencing.

## Podcast Starting Points

These episodes give the fastest path into the archive-backed AI engineering
thread:

- [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) explains the
  broad skill stack in
  [Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
  with 22:29 covering the full-stack skill stack. Use 29:12 for RAG, 42:28 for
  shipping pillars, and 54:05 for portfolio work.
- [Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) focuses
  on the role and product discovery in
  [Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}).
  Start with 7:51 for BranchGPT, 19:40 for the role, 48:48 for project ideas,
  and 57:39 for hiring signals.
- [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) covers statistical
  rigor and role boundaries in
  [Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).
  Start with 7:45 for evaluation and 42:05 for agents. Then use 45:50 for
  orchestration, 56:10 for latency, and 1:01:20 for fine-tuning.
- [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) covers
  production AI through data tests and prompt evaluation in
  [Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
  Start with 9:05 for data trust and 11:47 for tests. Then use 28:16 for
  prompt evaluation, 30:00 for compression, and 31:45 for caching.
- [Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) shows how
  notebook work becomes an end-to-end AI system in
  [From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
  Start with 17:27 for ownership and 37:39 for requirements. Then use 41:28 for
  feedback, 55:28 for production code, and 1:02:53 for tooling.

## See Also

These pages extend the AI engineering topic into role and roadmap work. They
also cover retrieval, agents, evaluation, and deployment.

Start with these related pages:

- [AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }})
- [AI Engineering Roadmap]({{ '/wiki/ai-engineering-roadmap/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }})
