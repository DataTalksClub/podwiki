---
layout: "person"
title: "Meryem Arik"
source_person: "../datatalksclub.github.io/_people/meryemarik.md"
person_id: "meryemarik"
summary: "LLM startup founder focused on deployable language models, fine-tuning, retrieval, open-source models, and production tradeoffs."
expertise: ["LLMs", "MLOps", "open-source", "production", "retrieval-augmented generation"]
podcast_episodes: ["deploying-llms-in-production-fine-tuning-retrieval-open-source-api"]
source_url: "https://datatalks.club/people/meryemarik.html"
curated: "true"
---

## Background

Meryem Arik is co-founder of TitanML, an NLP development platform focused on deployable language models. Her DataTalks.Club contribution is useful because she treats [LLMs]({{ '/wiki/llms/' | relative_url }}) as production systems, not only as demos. In [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}), the recurring question is how teams make models cheaper and more controllable. She also focuses on reliability after the demo works.

## Deploying LLMs as Production Systems

Meryem frames LLM deployment as an [MLOps]({{ '/wiki/mlops/' | relative_url }}) and [production]({{ '/wiki/production/' | relative_url }}) problem. A model that works in a prototype still has to fit serving infrastructure, privacy constraints, cost limits, and evaluation expectations. In the episode, she describes TitanML's work as helping companies train, optimize, and serve language models. Some customers run those models on-premise or in their own cloud when data security requires it.

That production lens leads to a practical split. API models are useful for fast validation because they make it possible to get a demo working quickly. For longer-lived systems, Meryem argues that teams often move toward [open source]({{ '/wiki/open-source/' | relative_url }}) models. They can control the model version, host it under their own privacy constraints, and optimize it for the workload they actually need.

## Fine-Tuning, RAG, and Changing Knowledge

Meryem's most useful distinction is between what belongs in the model weights and what should stay in a retrievable knowledge source. For [RAG]({{ '/wiki/rag/' | relative_url }}) and [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}), her contribution is concrete. Fine-tuning is strong for specialization, domain language, task labels, and tone. Retrieval is often better when the answer depends on documentation that changes over time.

In the customer-support example from the episode, she prefers retrieval over repeatedly retraining the model when product documentation changes. Cost matters, but so does grounding. Retrieval grounds the answer in current documentation and reduces hallucination risk. It lets the model rephrase or summarize the retrieved passage instead of inventing a plausible answer from stale weights.

## Vector Databases and Retrieval Design

Her explanation of [vector databases]({{ '/wiki/vector-databases/' | relative_url }}) stays close to the production retrieval workflow. Teams embed unstructured documents, index those vectors, embed the user's query, and retrieve the most semantically similar chunks. She connects vector databases directly to the first stage of a grounded LLM system. The application finds relevant passages before asking the model to answer.

Meryem also points out a design choice inside retrieval systems. A simple approach injects relevant sections into the prompt. A more controlled approach uses one retrieval step to find the right sections and another model step to summarize or change tone. That keeps the generation layer closer to the source material. The discussion makes her episode a useful companion to [LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}) and search-backed knowledge systems.

## Open-Source Models and API Tradeoffs

In the episode, Meryem compares open-source models such as LLaMA, Falcon, and MPT with API-hosted models. Her argument isn't that APIs are bad. It's that API convenience comes with control limits. She highlights the risk that a provider can change, distill, retire, or otherwise alter a model behind a stable endpoint. That can change application behavior without the builder choosing that change.

That makes model choice a [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and operations issue, not only a benchmark issue. For business-critical LLM applications, Meryem values version control and visibility into model weights. She also values controlled upgrades and the ability to fine-tune or optimize the model on the team's own schedule. APIs remain attractive for prototyping. Open-source deployments become more compelling when privacy, stability, cost, or long-term ownership matter.

## Serving Constraints, Latency, and Cost

Meryem repeatedly brings the discussion back to serving constraints. Because LLMs are large, production teams have to think about compression and inference servers. They also have to plan hardware cost and whether the workload runs on GPUs or CPUs.

In the TitanML discussion, she describes serving infrastructure as an extension of the same deployability problem as fine-tuning. Easier serving can reduce hardware requirements while preserving latency targets.

Her latency and cost tradeoff is pragmatic. API models can be fast because providers run them on expensive infrastructure. Teams can also run self-hosted models quickly with strong inference tooling and hardware. The larger production win may be comparable latency at much lower cost or acceptable latency on the hardware a business already has.

## Evaluation and Production Readiness

Meryem is careful about [evaluation]({{ '/wiki/evaluation/' | relative_url }}) limits. For classification and natural-language-understanding tasks, she treats benchmarking as more straightforward because teams can measure right and wrong labels. For generative LLM behavior, evaluation is harder. There are many ways to be right, many ways to be wrong, and human review remains important for judging whether outputs are sensible.

Her data-quality advice also supports [LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}). Start with smaller, high-quality "gold standard" examples and use output quality as the practical signal. Consider LLM-assisted dataset expansion when hand-labeling everything would be slow or expensive.

The through-line is production tradeoff management. Pick the adaptation method,
retrieval design, serving setup, and evaluation process that match the actual
risk and constraint profile of the system.
