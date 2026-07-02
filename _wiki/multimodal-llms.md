---
layout: wiki
title: "Multimodal LLMs"
summary: "How DataTalks.Club guests discuss large language models that process text, images, video, and audio: architectures like CLIP, cross-modal embeddings, autonomous driving applications, multimodal agent futures, and the deployment and evaluation challenges of running multimodal systems in production."
related:
  - LLMs
  - Generative AI
  - Embeddings
  - Vector Databases
  - Computer Vision
  - Autonomous Driving AI
  - AI Engineering
---

Multimodal LLMs are large language models that process more than one input
modality. They take text alongside images, video, or audio and produce outputs
that reason across those modalities. DataTalks.Club guests discuss multimodal
LLMs across several contexts: autonomous driving perception, cross-modal search
and retrieval, and the future trajectory of AI agents.

The core idea is that different data types can share a representation space.
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}) map text and images into
the same vector space, so a text query can find a matching image, or a model can
reason about a scene from both its visual and linguistic content. This connects
multimodal LLMs to [LLMs]({{ '/wiki/llms/' | relative_url }}),
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}),
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}), and
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}).

## CLIP and Cross-Modal Embeddings

The most concrete multimodal architecture discussed in the podcast is CLIP
(Contrastive Language-Image Pre-training), which OpenAI developed to map text
and images into a shared vector space.

In
[Production ML Search: Embeddings, Hybrid Architectures and Scalable Indexing](https://datatalks.club/podcast/production-ml-search-vector-search-embeddings-hybrid-search.html),
[Daniel Svonava](https://datatalks.club/people/danielsvonava.html) explains CLIP at
33:11. The model turns text into vectors and images into vectors in such a way
that you can use text to look for images. Writing "black cat" returns images of
black cats. This is cross-modal retrieval: the query and the target live in
different modalities, but the shared embedding space makes matching possible.

At 33:13, the discussion shows why CLIP matters for production systems. If a
team started with a text embedding model like BERT and later needed to add
images, replacing the embedding model and re-indexing the entire pipeline is
expensive. The architecture choice at the embedding layer determines how easily
the system can incorporate new modalities later.

This is a [vector databases]({{ '/wiki/vector-databases/' | relative_url }})
and [search]({{ '/wiki/search/' | relative_url }}) question, not only a model
question. The multimodal embedding pipeline must handle ingestion for both text
and images, maintain consistency across modalities, and support fast query-time
retrieval across all of them.

## Modality Fusion and Feature Engineering

In production multimodal systems, a single document often has multiple
embeddings: one for its title, one for its content, one for its images, and one
for parameters like price or popularity. At 38:11 in Daniel's episode, the
discussion covers how these multiple embeddings and metadata must be linked
together in the database.

The goal of modality fusion is to end up with one vector per article or product
that encodes all relevant signals. This requires combining structured and
unstructured data into a shared representation. At 50:41, Daniel notes that in
Big Tech, people have been building custom embedding models that combine
structured and unstructured information into a shared vector representation for
a long time. The open question is now more about how to productionize it and let
people iterate quickly.

Daniel also references VectorHub tutorials at 49:36 that illustrate how to
combine graph and text embeddings together, and how to combine image and text
embeddings. These are practical starting points for engineers building
multimodal retrieval systems.

## Multimodal LLMs in Autonomous Driving

[Aishwarya Jadhav](https://datatalks.club/people/aishwaryajadhav.html) addresses
multimodal LLMs in the context of self-driving in
[Lessons from Applied AI: Tesla, Waymo, and Beyond](https://datatalks.club/podcast/from-computer-vision-research-to-autonomous-driving-ai.html).

At 52:53, she notes that there have been many attempts to use multimodal LLMs
for autonomous driving. Some companies are using them for end-to-end
self-driving. The appeal is that LLMs are pretrained on massive data, so they
carry world knowledge that curated datasets might miss.

At 53:20, she identifies the core challenge: making multimodal LLMs fast enough
for real-time vehicle inference. Tradeoffs and optimization techniques are
needed, but the approach is actively explored in research and by companies.

At 54:17, the discussion turns to whether LLMs' broad training data helps them
adapt to different geographic driving cultures. Aishwarya suggests that LLMs
might already know differences between, for example, Italian and German driving
patterns from their training data, which could make it easier to tune systems
for global use. This connects multimodal LLMs to
[autonomous driving AI]({{ '/wiki/autonomous-driving-ai/' | relative_url }})
and the broader
[model optimization]({{ '/wiki/model-optimization/' | relative_url }}) challenge
of running large models under hard latency constraints.

## Visual Language Models and Agent Infrastructure

[Aditya Gautam](https://datatalks.club/people/adityagautam.html) discusses the
multimodal shift in the context of AI agents in
[The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html).

At 21:57, he describes a shift away from text-only interactions. Infrastructure
tooling is getting better, and there is a multimodality shift where visual
language models (VLMs) and other multimodal elements are coming up. Visual
capabilities are getting much better than they were a year before.

This matters for agents because it expands what an agent can perceive and act
on. A text-only agent can read logs and API responses, but a multimodal agent
can also interpret screenshots, diagrams, video feeds, and visual interfaces.
At 22:38, Aditya notes that infrastructure reliability services and AI
governance are maturing to support this shift, including the ability to audit
which agent is interacting with which system.

## The Future of Multimodal Agents

At 1:06:12 in Aditya's episode, the discussion turns to where multimodal AI is
heading. He describes multimodality as going in an exponential direction. Within
three years, he would not be surprised if a user could give access to their
photo gallery and a prompt to produce a movie. The movie could show children
grown up looking exactly as they did in childhood, or the user as they were ten
years ago.

At 1:06:53, he frames this as a potential inflection point for adoption.
Producing a 4K thirty-minute movie based on family photos would be an
experiential moment that makes multimodal AI tangible for many people. This is a
generative AI capability that requires deep integration of vision, language, and
temporal reasoning.

These predictions connect multimodal LLMs to
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}) and
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}). Building systems
that can take a photo gallery as input and produce coherent video output is not
only a model problem. It requires data pipelines, memory management, retrieval,
and evaluation across modalities.

## Deployment and Evaluation Challenges

Multimodal LLMs face the same production pressures as text-only
[LLMs]({{ '/wiki/llms/' | relative_url }}), but amplified. More input types mean
more preprocessing, larger payloads, and more failure modes.

In Daniel's search episode, the multimodal embedding pipeline must handle the
vector compute problem twice: once for ingestion (batch-embedding documents and
images) and once for query handling (fast embedding of the user query). At
30:22, he describes these as two instances of the same vector compute problem,
with different latency requirements. Ingestion can be batched, but query
handling must be fast, and both must be consistent because they land in the same
vector space.

Aishwarya's autonomous driving context at 53:20 adds the real-time inference
constraint. A vehicle cannot wait seconds for a multimodal model to process a
scene. The model must be compressed, quantized, and optimized to run on
on-vehicle hardware within milliseconds. These are
[model optimization]({{ '/wiki/model-optimization/' | relative_url }}) and
[production]({{ '/wiki/production/' | relative_url }}) challenges that apply to
any multimodal system deployed under latency constraints.

For the search and retrieval side, Daniel's episode at 34:00 covers hybrid
search as the practical pattern for combining multimodal vector similarity with
business constraints like recency, filters, and popularity. The system layers
vector proximity with metadata constraints to produce results that satisfy both
semantic relevance and product requirements.

## Related Pages

- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Computer Vision]({{ '/wiki/computer-vision/' | relative_url }})
- [Autonomous Driving AI]({{ '/wiki/autonomous-driving-ai/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
