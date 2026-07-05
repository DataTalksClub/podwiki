---
layout: wiki
title: "AI"
summary: "AI across machine learning, generative AI, agents, production systems, evaluation, infrastructure, and governance."
related:
  - Generative AI
  - LLMs
  - AI Engineering
  - AI Engineer Role
  - Machine Learning
  - Data Products
  - Evaluation
  - Governance
  - Agent Engineering
  - Prompt Engineering
  - Responsible AI and Governance
---

Artificial intelligence covers systems built from models and data, which also
depend on software and workflow design. These systems support decisions,
generate content, retrieve knowledge, or automate product work.

In older conversations that often means
[[machine learning]],
[[deep learning]], and
[[NLP]]. In newer conversations it often means
[[LLMs]],
[[generative AI]],
[[retrieval-augmented-generation=>retrieval-augmented generation]],
and [[agent-engineering=>AI agents]].

The useful boundary isn't whether a system calls a model, but whether it
changes a workflow. Teams also need to evaluate, operate, secure, and improve it. Modern
generative AI work connects back to statistical rigor. AI delivery includes
human-centered design, and agents sit inside normal software engineering
discipline.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Janna Lipenkova's
[[book:20240205-creating-intelligent-products=>Creating Intelligent Products]]
develops the same product-focused view. It treats AI as an end-to-end product
discipline, not just model development. The product scope includes market
research, UX, and business model fit.
[[book:20220509-artificial-intelligence-with-python=>Artificial Intelligence with Python]]
by Prateek Joshi covers the broader toolkit that underlies these product
systems. The toolkit runs from search and optimization through ML, deep
learning, and reinforcement learning.

## AI as Product Engineering

AI is product engineering, not standalone prediction, so full-stack engineering
and RAG sit in the same skill stack. Knowledge management, LLMOps, and product
delivery become delivery concerns.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

That makes
[[AI engineering]] closer to
shipping a [[data-products=>data product]] than to
only training a model.

AI engineers combine product discovery and backend delivery. They also work
with LLM tooling and decide what should be automated. Projects and skill proof
matter more than credentials.[[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]]

That's why the AI page connects to both the
[[AI Engineer Role]] and the
[[AI Engineering Roadmap]].

AI product thinking also shows up before the LLM era. AI product teams work
with roadmaps, customer research, business metrics, and MLOps priorities. They
work backward from business problems and add success metrics, SLAs, and data
quality.[[cite:building-and-scaling-ai-data-products-with-mlops=>Build & Scale Data Products for AI]]

That discussion links AI to
[[data product management]],
[[MLOps]], and
[[data engineering]].

## Machine Learning, LLMs, and Generative AI

[[Machine learning]] is the
technical base under much of the AI archive. It covers feature work, labels, and
training data. It also covers model validation, deployment, monitoring, and
tradeoffs between accuracy and interpretability. Use the narrower
[[Machine Learning Engineer Role]]
when the discussion is about supervised learning systems, feature pipelines, or
classical production ML.

The newer LLM conversations focus on language models and generated outputs.
Production LLM work separates classification from generation. Teams compare
hosted APIs with open-source models. Fine-tuning, retrieval, and vector
databases become implementation choices. Latency, cost, and evaluation matter in
production.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

For narrower topics, use
[[LLM production patterns]],
[[vector databases]], and [[evaluation]].

[[Generative AI]] covers systems that produce generated outputs such as text,
code, summaries, and answers. The same bucket also includes translation work,
image output, and planning.

Chatbot failures show generated outputs need security controls. Large-scale
chatbot probing and knowledge-base exfiltration checks are part of that work.
Teams also add output validation, query analysis, and layered
defenses.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Those failure modes connect
[[prompt engineering]]
to [[security]] rather than treating a
prompt as only copywriting.

## Retrieval and Knowledge Systems

Many AI products become useful only when the model can work with the right
context. Search systems connect NLP and personalization to learning-to-rank and
LLMs. RAG adds retrieval plus generation to reduce hallucinations. It also
brings in chunking, embeddings, and citations. Prompt design and
human-in-the-loop evaluation stay part of the
system.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

That makes [[search]] and
[[embeddings]] central AI topics, and
[[retrieval-augmented-generation=>RAG]]
covers the broader architecture. RAG systems also inherit latency, cost, and
data-quality problems. Retrieval can be a tool inside an agent rather than the
whole system.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Agents and Action-Oriented AI

[[agent-engineering=>AI agents]] extend AI systems from
answer generation into planning and tool use. They also add memory and action.

Agentic systems use objectives, tools, memory, and stores. They also depend on
context design, custom evaluations, and mocked tools. Checks focus on outcomes
rather than exact paths.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Agent design can borrow from
[[reinforcement-learning=>reinforcement learning]],
[[evolutionary-algorithms=>evolutionary algorithms]], early NLP, and prompt
optimization. Minimal task decomposition can come before manager-agent
orchestration. Tool integration and monitoring wrap the agent system.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
Use [[game-ai-to-llm-agents=>Game AI to LLM Agents]] for that history bridge.
For design details, use
[[agent engineering]] and
[[multi-agent-systems=>multi-agent systems]].

## Evaluation, Reliability, and Cost

AI systems need [[evaluation]] because
the output is probabilistic, context-dependent, and tied to user trust.

Production AI engineering starts with data trust and pipeline tests, then moves
to prompt engineering and prompt evaluation. Engineers also manage prompt
compression, prompt caching, and token use. Latency and model efficiency become
engineering concerns too.
[[cite:production-ready-ai-engineering=>Production AI Engineering]]
A useful AI feature must survive
[[production]] traffic, not only a demo.

LLM and RAG evaluation use gold-standard examples, output-driven metrics, and
human judgment. The work separates classification metrics from generative
metrics.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Search and RAG systems add retrieval-level checks as well as answer-level
checks.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Use [[LLM Evaluation Workflows]] and
[[Production Search Evaluation]] for narrower measurement topics.
Use [[Data Quality and Observability]] and
[[data-quality-and-observability=>Data Observability]]
for data reliability.

## Infrastructure and Model Control

Infrastructure-heavy AI work asks who controls compute, data, and models. Teams
also have to own latency, privacy, and operating cost.
Cloud and on-prem choices affect privacy, control, and decentralization.
Training across multiple machines adds GPU coordination. Teams have to handle
PyTorch and NCCL communication bottlenecks, Kubernetes limits, SLURM, and
open-source orchestration.[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]

The same infrastructure concern complements model deployment. Open-source models
and hosted APIs sit alongside fine-tuning and serving optimization. Teams still
have to manage latency tradeoffs.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
For deeper implementation work, use
[[AI Infrastructure]],
[[Machine Learning Infrastructure]],
and [[MLOps]].

## Governance, Security, and Human Oversight

AI needs [[governance]] when it affects
people, regulated decisions, or private data. Safety-critical workflows need the
same discipline. Material business outcomes do too.
Teams hit the same boundary in
[[ai-for-social-good=>AI for social good]]
work. Conservation monitoring, nonprofit optimization, accessibility support,
and policy systems can turn model outputs into field work or access to
resources.[[cite:ai-for-ecology-biodiversity-and-conservation=>Conservation AI]][[cite:data-science-and-analytics-for-nonprofits-tech-for-good=>Nonprofit Analytics]][[cite:data-science-for-public-policy-ethical-ai-social-impact=>Policy]]

Responsible AI work centers trust and fairness, plus explainability,
stakeholder collaboration, and compliance. The work runs from data-level
fairness checks and
PII handling to cross-functional governance and human-in-the-loop
oversight.[[cite:responsible-explainable-ai-bias-detection=>Responsible & Explainable AI]]

For LLM systems, governance also has a security layer.
Prompt injection and data exfiltration sit beside hallucinations, controls,
ROI, and hybrid human review.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Those risks are why the AI topic links out to
[[Responsible AI and Governance]],
[[AI Red Teaming]],
[[Privacy Engineering for ML]],
and [[Security]].

## Related Pages

Use these pages for narrower AI topics and implementation details.

- [[AI Engineering]] and [[AI Engineer Role]] cover the builder role and skill stack.
- [[Generative AI]], [[LLMs]], and [[Prompt Engineering]] cover model behavior and generated outputs.
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] and [[retrieval-augmented-generation=>RAG]] cover context and retrieval.
- [[agent-engineering=>AI Agents]], [[Agent Engineering]], and [[multi-agent-systems=>Multi-Agent Systems]] cover action-oriented AI systems.
- [[Data Products]], [[MLOps]], and [[Production]] cover delivery and operations.
- [[Evaluation]], [[LLM Evaluation Workflows]], and [[Production Search Evaluation]] cover measurement.
- [[AI Infrastructure]] and [[Machine Learning Infrastructure]] cover compute, orchestration, and deployment choices.
- [[Responsible AI and Governance]], [[Governance]], [[Security]], and [[AI Red Teaming]] cover risk controls.
