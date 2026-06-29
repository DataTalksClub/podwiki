---
layout: wiki
title: "LLMs"
summary: "How the podcast archive treats large language models as production components for generation, retrieval, agents, and language workflows."
related:
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - NLP
  - Generative AI
---

## Definition and Scope

Large language models process and generate language. In the podcast archive,
teams use them for generation, retrieval, classification, and assistant
interfaces. Guests don't treat LLMs as stand-alone products. They use them
inside systems that still need data pipelines, evaluation, deployment,
security, and human review.

Use [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
as the larger hub for production design. Use this bridge for episodes and
people pages that use the `LLMs` topic slug.

## Contents

Use these links to jump between the main LLM sections.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

LLMs revive older NLP questions. The archive connects LLMs to older NLP work
rather than treating them as a clean break. Ivan Bilan's NLP-team episode
discusses tokenization, annotation, pipelines, and deployment before it reaches
GPT-3. Meryem Arik's production episode reframes those language-system concerns
around open-source models, API models, fine-tuning, and retrieval.

Retrieval beats retraining for changing knowledge. Several guests separate
model behavior from model knowledge. Fine-tuning can help with task style, tone,
domain language, or repeated formats. When a system needs fresh facts,
documents, citations, or reviewable evidence, the archive favors RAG over
continuous retraining.

Model choice is an operational decision. Open-source models provide control,
privacy, and deployment flexibility. API models can provide strong quality and a
faster start. The archive treats hidden model changes, latency, cost, and serving
complexity as production concerns, so model choice belongs with infrastructure
and product risk.

Evaluation has to match the task. LLM applications need representative
examples, gold test sets, traces, and failure analysis. For retrieval-backed
systems, teams should measure retrieval quality separately from final answer
quality. For assistants and agents, tests need to cover tool calls, outcomes,
and regressions.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Deploying LLMs in Production](https://datatalks.club/podcast.html): The
  10:24 clip covers generative and non-generative language models. The 16:48 and
  18:46 clips compare open-source models, API models, and model-drift risk. The
  26:30 and 40:46 clips frame fine-tuning as specialization and prefer retrieval
  for changing knowledge.
- [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html): The
  9:28 clip covers everyday LLM use cases. The 13:56 and 23:00 clips introduce
  generator-evaluator checks and gold tests. The 44:26 clip prioritizes RAG and
  chunking for business workflows.
- [Applied LLM Research](https://datatalks.club/podcast.html): The 10:15 clip
  covers long-context evaluation. The 12:36 clip reports performance drops
  around 32k-64k context in a financial benchmark. The 14:54 clip returns to
  chunking, retrieval, and summarization for large documents.
- [Building Agentic AI Systems](https://datatalks.club/podcast.html): The 11:00
  clip defines agents through autonomy, objectives, and LLMs. The 21:21 clip
  uses context engineering to design useful model inputs. The 51:17 clip turns
  evaluation into custom datasets and system benchmarks.
- [Hardening Generative AI Chatbots](https://datatalks.club/podcast.html): The
  11:38 clip discusses chatbot failures and hallucinations. The 16:15 and 17:00
  clips recommend layered defenses and non-LLM classifiers when generative models
  are too easy to manipulate.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})

## Maintenance Notes

Future updates should keep this page concise and route deeper material to the
larger hubs.

- Keep deeper production guidance in
  [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
- Add compact podcast summaries for `deploying-llms-in-production-fine-tuning-retrieval-open-source-api.md`,
  `practical-llm-engineering-and-rag.md`, and
  `building-agentic-ai-engineering-tooling-retrieval-evaluation.md`.
- When new LLM episodes appear, classify evidence by model choice, grounding,
  evaluation, deployment, security, and product workflow.
