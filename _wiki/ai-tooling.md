---
layout: wiki
title: "AI Tooling"
summary: "How teams choose and operate AI tooling for model APIs, open-source LLMs, RAG, prompts, agents, evaluation, and deployment."
related:
  - Tools
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Retrieval-Augmented Generation
  - Agent Engineering
  - MLOps Tools
  - AI Engineering
---

AI tooling covers the systems around model access and deployment. It includes
retrieval and prompts, plus agent frameworks and evaluation. It also includes
observability, cost control, and release workflows. A model API is rarely the
whole product.

Production AI systems need data and context around the model. They also need
controlled actions, tests, traces, and clear ownership[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]][[cite:production-ready-ai-engineering=>Production AI Engineering]].

For the whole role, use the
[[AI Engineer Role]]. Use
[[LLM Tools]] for practical stack
selection around model APIs, RAG, and evaluation. It also covers agents,
observability, and cost.
Use
[[LLM Production Patterns]]
for production architecture and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
for retrieval systems. Use
[[Agent Engineering]] for
tool-using agents and [[LLM Evaluation Workflows]]
for evaluation design.

## Model Boundary

AI tooling starts with [[LLMs]] and general [[Tools]], but most engineering work
sits around the model boundary. Teams structure model inputs with [[Prompt
Engineering]] and attach outside knowledge with
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]. [[Vector
Databases]] and [[Embeddings]] support that retrieval layer. Agent frameworks,
evaluation tools, monitoring, and deployment systems turn model calls into owned
products[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]][[cite:production-ready-ai-engineering=>Production AI Engineering]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

The development cycle is iterative. Prompting practices and generator-evaluator
checks lead to gold test sets. Failure analysis, logs, and traces make behavior
measurable[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Agent tooling expands the same stack with planning and tool use. Memory and
knowledge stores add context. The testing side uses mocked tools and
integration tests. Regression tests and outcome-based checks make agent behavior
testable[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Open-source tooling adds a second operating layer. Documentation and governance
affect whether teams can rely on a tool over time. Maintainers, plugins, and
business models affect that reliability too[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].

## Tools Around the Model

RAG and knowledge management belong in the same AI product stack as agents,
evaluation, and LLMOps. That stack links AI tooling to [[AI Engineering]]. The
tools matter because they package the system around the model instead of
treating a prompt as the product[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].

Prompting practices and generator-evaluator checks start the LLM application
cycle. Gold test sets, failure analysis, logs, and traces help teams diagnose
failures and ship changes deliberately[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Stack Boundaries

The main disagreement is where teams draw the build-buy boundary. API models
make prototyping easier, while open-source models can improve privacy, control,
and fine-tuning options. The tradeoff shifts when API drift, latency, hardware
cost, and serving work enter the decision[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

Production data workflows create another boundary. Open-source model tools and
assistant tools can help alongside coding-assistant workflows. Teams still need
data trust, pipeline tests, preprocessing, and fine-tuning data practices around
them[[cite:production-ready-ai-engineering=>Production AI Engineering]]. Those
assistant workflows are covered in depth as [[AI Coding Tools]].

Agent frameworks create a third boundary across prompt-level implementations,
SDKs, and tool wrappers. Other options include LangChain, the OpenAI Agents SDK,
and smaller frameworks. The practical choice depends on control over tool
interfaces, state, tests, and failure handling more than novelty[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

## Model APIs and Open-Source Models

Model tooling begins with the API-versus-open-source choice. Open-source models
can make sense for private deployments, controlled deployments, or fine-tuning[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
API providers can change model behavior outside the team's release process[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Teams then need evaluation and release checks as part of the tooling decision.

GPT-style APIs help prototypes, but open-source models can fit production
constraints better. Latency and cost turn model choice into deployment
engineering[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
At that point, model tooling becomes
[[MLOps]] and
[[MLOps Tools]], not only to prompt
design.

## RAG and Vector Search Tooling

RAG tools appear when teams need fresh or private knowledge without retraining
the model[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

Retrieval handles changing knowledge, while fine-tuning handles behavior,
adaptation, or tone. Teams ground answers with
indexed documents, retrieval-augmented responses, embeddings, and vector
databases[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
That distinction is the same decision boundary covered in
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

RAG tooling becomes an iteration cycle around chunking and embeddings. Teams
choose among fixed-length chunks, sliding windows, and context rot tradeoffs.
Those are engineering choices, not just retrieval details[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Those choices sit next to [[Vector Databases]]
and [[Embeddings]]. They also connect to
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

RAG also has production risks. Latency, cost, garbage-in/garbage-out failures,
and backend changes all affect how useful retrieved material is to the LLM.
Retrieval can be the whole architecture or a tool an agent calls inside a larger
workflow[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

## Prompt and Context Tooling

Prompt tools are most useful when they make inputs structured, reusable, and
testable. In-context learning, examples, and prompt formatting connect prompt
design to evaluation. Prompt compression and prompt caching connect it to
latency and repeated work[[cite:production-ready-ai-engineering=>Production AI Engineering]].

Role prompts, structured outputs, timestamps, and transcript workflows can sit
inside automated pipelines. Gemini, Descript, Loom, and GitHub Actions show how
prompt engineering can move beyond one-off chat sessions[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Context engineering adds chunking, metadata, and wrappers to the work of
designing effective LLM inputs. That makes context tooling a bridge between
[[Prompt Engineering]], [[retrieval-augmented-generation=>RAG]], and [[Agent
Engineering]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

## Agent Frameworks and Tool Protocols

Agent tooling shows up when a system must plan, call tools, and update state
inside a workflow. Autonomy and objectives are only part of the system. Tools,
memory, and knowledge stores define one side of the engineering surface.
Single-step planning, multi-pass execution, and self-reflection define another
side[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

The tooling boundary changes for code agents and natural-language agents. It
also changes for SRE workflows that use logs, metrics, and remediation.
Integration abstractions and agent marketplaces make tool interfaces part of the
product design. Tool protocols such as MCP do the same[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Teams move from RAG into tool calls when the workflow needs actions, not only
better context[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Evaluation and Observability Tooling

Evaluation tools make AI systems easier to change without guessing.
Generator-evaluator checks and representative gold tests create the evaluation
base. Failure categories and logs connect AI tooling directly to traces,
[[Evaluation]],
[[LLM Evaluation Workflows]],
and [[Model Monitoring]][[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Agent evaluation adds custom datasets and system benchmarks. The surrounding
system uses mocked tools, integration tests, and regression tests.
Teams still need outcome-based checks because an agent may solve the same goal through
different paths[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Evaluation also belongs inside the broader AI engineering skill
stack[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].

## Deployment and Operational Tooling

Deployment tooling matters because LLM systems inherit classic production
constraints. Teams still have to manage data quality and latency. They also
need cost control, testing, and recovery[[cite:production-ready-ai-engineering=>Production AI Engineering]].

Data trust and pipeline tests sit inside AI tooling when the system has to run
in production. Great Expectations, Soda, preprocessing, and fine-tuning data
belong in the same operational layer[[cite:production-ready-ai-engineering=>Production AI Engineering]].

Serving work adds training and optimization. Serving stacks also have to account
for model size, compression, and inference optimization[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
These episodes place AI tooling next to [[Machine Learning System Design]]
and [[MLOps Tools]], especially when
teams move past demos.

## Open-Source Tool Sustainability

Open-source AI tooling depends on maintainers, governance, documentation, and
business models. Scikit-learn and related tools show the difference between
core features and plugin ecosystems. Governance, NumFOCUS, maintainer
transitions, and maintainer motivation all affect tool quality[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].

Tool ecosystems also need more than code. Documentation, interactive content,
and videos make tools easier to adopt and maintain[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].

Skrub's table vectorizer and pragmatic tabular defaults show how tool design can
encode useful defaults. Funding, training, consulting, and partnerships help
sustain the tool[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].
That makes [[Open Source and Developer Relations]] part of the AI tooling story.

## Related Pages

AI tooling overlaps with several adjacent system concerns:

- [[LLM Production Patterns]] for model, RAG, agent, and deployment patterns.
- [[LLM Evaluation Workflows]] for gold sets, failure analysis, judges, and agent tests.
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for retrieval architecture and vector search.
- [[Agent Engineering]] for tool-using workflows and agent evaluation.
- [[MLOps Tools]] for the broader machine learning operations toolkit.
