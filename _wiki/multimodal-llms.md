---
layout: wiki
title: "Multimodal LLMs"
summary: "Guide to multimodal LLMs: text, image, audio, and video inputs; architecture choices, evaluation, and production use."
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
LLMs in autonomous driving perception, cross-modal search and retrieval, and the
future trajectory of AI agents.

Different data types can share a representation space. [[Embeddings]] map text
and images into the same vector space, so a text query can retrieve a matching
image. That connects multimodal LLMs to [[LLMs]], [[Computer Vision]],
[[Generative AI]], and [[Vector Databases]].

## CLIP and Cross-Modal Embeddings

The most concrete multimodal architecture discussed in the podcast is CLIP
(Contrastive Language-Image Pre-training). CLIP maps text and images into a
shared vector space. That makes text-to-image retrieval possible: a query such
as "black cat" can retrieve images of black cats.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search|33:11]]

This matters for production search architecture. A team may start with a
text-only embedding model and later need to include images. Swapping the model
and re-indexing the corpus becomes easier when the ingestion, indexing, and
vector-compute pipeline already treats embeddings as replaceable production
components.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]

The challenge lives in [[Vector Databases]] and [[Search]], not only in the
model. The pipeline has to ingest text and images, keep their representations
consistent, and serve low-latency query-time retrieval from the same vector
space.

## Modality Fusion and Feature Engineering

In production multimodal systems, a single document often has multiple
embeddings:

- one for its title
- one for its content
- one for its images
- one for parameters like price or popularity

Those embeddings and metadata have to be linked in the database. Some systems
fuse them into one representation for articles, products, users, and business
signals.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]

Feature fusion is described as an older Big Tech practice made newly accessible.
Custom embedding models can combine structured and unstructured data into a
shared vector representation. The product problem is how to productionize the
workflow and let teams iterate quickly.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]

## Multimodal LLMs in Autonomous Driving

Autonomous driving is the most safety-critical multimodal setting covered here.
Some companies are exploring multimodal LLMs for end-to-end self-driving because
pretrained models may contain world knowledge that curated driving datasets
miss.[[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving AI|52:53]]

The core production issue is latency. A self-driving system can't wait seconds
for a model to understand a scene. Multimodal LLMs need optimization and careful
tradeoffs before they fit real-time vehicle inference.[[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving AI|53:20]]

Broad training data may help with geographic variation. The idea remains
tentative.[[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving AI|54:17]]
This connects multimodal LLMs to [[Autonomous Driving AI]] and [[Model Optimization]].

## Visual Language Models and Agent Infrastructure

AI agent discussions treat multimodality as part of the move beyond text-only
interfaces. Visual language models and related multimodal components are getting
better while infrastructure tooling, reliability services, and AI governance
mature around them.[[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

A text-only agent can read logs and API responses, while a multimodal agent can
interpret screenshots and diagrams. It can work with video feeds and visual
interfaces too. This wider input surface changes agent governance. Teams need to
audit which agent interacts with which system and how data moves through the
organization.[[cite:s23e03-future-of-ai-agents|The Future of AI Agents]]

## The Future of Multimodal Agents

One future-facing agent discussion predicts that multimodal systems could turn a
photo gallery and prompt into a long generated movie. The prediction highlights
the integration challenge more than the specific timeline. Such systems would
need vision, language, and temporal reasoning. They would also need retrieval,
memory, and evaluation across modalities.[[cite:s23e03-future-of-ai-agents|The Future of AI Agents|1:06:12]]

These predictions connect multimodal LLMs to [[Generative AI]] and [[AI Engineering]].
The production work goes beyond model architecture. Teams need data pipelines
and memory management, plus retrieval, observability, and evaluation that can
handle more than text.

## Deployment and Evaluation Challenges

Multimodal LLMs face the same production pressures as text-only
[[LLMs]], but amplified. More input types mean more preprocessing, larger
payloads, modality-specific failure modes, and harder evaluation.

Multimodal embedding work appears in both ingestion and query handling. The
pipeline may batch-embed documents and images during ingestion, then embed the
user query quickly at query time. Ingestion can be batched. Query handling must
be fast. Both paths must stay consistent because they land in the same vector
space.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search|30:22]]

Autonomous driving adds the hard real-time version of the same constraint. A
vehicle can't wait seconds for a multimodal model to process a scene. The model
must be optimized to run on vehicle hardware within tight latency budgets.
These are [[Model Optimization]] and [[Production]] challenges.[[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving AI]]

For search and retrieval, hybrid search combines vector similarity with business
constraints such as recency, filters, and popularity. The system layers vector
proximity with product requirements so results satisfy both semantic relevance
and operational constraints.[[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]

## Related Pages

Adjacent model, retrieval, and production topics:

- [[LLMs]]
- [[Generative AI]]
- [[Embeddings]]
- [[Vector Databases]]
- [[Computer Vision]]
- [[Autonomous Driving AI]]
- [[AI Engineering]]
