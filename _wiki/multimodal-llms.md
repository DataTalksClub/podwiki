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

Different data types can share a representation space.
[[Embeddings]] map text and images into
the same vector space. A text query can find a matching image, and a model can
reason about a scene from both its visual and linguistic content. That connects
multimodal LLMs to [[LLMs]],
[[computer vision]],
[[generative AI]], and
[[vector databases]].

## CLIP and Cross-Modal Embeddings

The most concrete multimodal architecture discussed in the podcast is CLIP
(Contrastive Language-Image Pre-training). OpenAI developed CLIP to map text and
images into a shared vector space.

In
[[podcast:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search: Embeddings, Hybrid Architectures and Scalable Indexing]],
[[person:danielsvonava=>Daniel Svonava]] explains CLIP at
33:11. The model turns text into vectors and images into vectors in such a way
that you can use text to look for images. Writing "black cat" returns images of
black cats. This is cross-modal retrieval: the query and the target live in
different modalities, but the shared embedding space makes matching possible.

The 33:13 discussion shows why CLIP matters for production systems. A team might
start with a text embedding model like BERT and later need images. Replacing the
embedding model and re-indexing the entire pipeline would be expensive. The
embedding architecture determines how easily the system can add new modalities
later.

Teams have to solve this in [[vector databases]]
and [[search]], not only in the model.
The multimodal embedding pipeline must handle text and image ingestion, keep
modalities consistent, and support fast query-time retrieval across all of them.

## Modality Fusion and Feature Engineering

In production multimodal systems, a single document often has multiple
embeddings:

- one for its title
- one for its content
- one for its images
- one for parameters like price or popularity

At 38:11 in Daniel's episode, the discussion covers how these multiple
embeddings and metadata must be linked together in the database.

Modality fusion creates one vector per article or product that encodes all
relevant signals. Teams combine structured and unstructured data into a shared
representation. At 50:41, Daniel notes that Big Tech teams have long built
custom embedding models that combine both kinds of information. The open
question is now more about how to productionize it and let people iterate
quickly.

Daniel also references VectorHub tutorials at 49:36 that illustrate how to
combine graph and text embeddings together, and how to combine image and text
embeddings. These are practical starting points for engineers building
multimodal retrieval systems.

## Multimodal LLMs in Autonomous Driving

[[person:aishwaryajadhav=>Aishwarya Jadhav]] addresses
multimodal LLMs in the context of self-driving in
[[podcast:from-computer-vision-research-to-autonomous-driving-ai=>Lessons from Applied AI on Tesla, Waymo, and Beyond]].

At 52:53, she notes that teams have made many attempts to use multimodal LLMs for
autonomous driving. Some companies use them for end-to-end self-driving. The
appeal is that LLMs are pretrained on massive data, so they include world
knowledge that curated datasets might miss.

At 53:20, she identifies the core challenge. Multimodal LLMs need to be fast
enough for real-time vehicle inference. Tradeoffs and optimization techniques
are needed, but researchers and companies are actively exploring the approach.

At 54:17, the discussion turns to whether LLMs' broad training data helps them
adapt to different geographic driving cultures. Aishwarya suggests that training
data might already capture differences between Italian and German driving
cultures, for example. That could make systems easier to tune for global use.
This connects multimodal LLMs to
[[autonomous driving AI]]
and the broader
[[model optimization]] challenge
of running large models under hard latency constraints.

## Visual Language Models and Agent Infrastructure

[[person:adityagautam=>Aditya Gautam]] discusses the
multimodal shift in the context of AI agents in
[[podcast:s23e03-future-of-ai-agents=>The Future of AI Agents]].

At 21:57, he describes a shift away from text-only interactions. Infrastructure
tooling is getting better, and there's a multimodality shift where visual
language models (VLMs) and other multimodal elements are coming up. Visual
capabilities are getting much better than they were a year before.

Agents can perceive and act on more context as they become multimodal. A
text-only agent can read logs and API responses. A multimodal agent can also
interpret screenshots, diagrams, video feeds, and visual interfaces. At 22:38,
Aditya notes that infrastructure reliability services and AI governance are
maturing to support this shift. That includes the ability to audit which agent is
interacting with which system.

## The Future of Multimodal Agents

At 1:06:12 in Aditya's episode, the discussion turns to where multimodal AI is
heading. He describes multimodality as going in an exponential direction. Within
three years, he wouldn't be surprised if a user could give access to their
photo gallery and a prompt to produce a movie. The movie could show children
grown up looking exactly as they did in childhood, or the user as they were ten
years ago.

At 1:06:53, he frames this as a potential inflection point for adoption.
Producing a 4K thirty-minute movie based on family photos would be an
experiential moment that makes multimodal AI tangible for many people. A
capability like that requires deep integration of vision, language, and temporal
reasoning.

These predictions connect multimodal LLMs to
[[generative AI]] and
[[AI engineering]]. Building systems
that can take a photo gallery as input and produce coherent video output isn't
only a model problem. It requires data pipelines, memory management, retrieval,
and evaluation across modalities.

## Deployment and Evaluation Challenges

Multimodal LLMs face the same production pressures as text-only
[[LLMs]], but amplified. More input types mean
more preprocessing, larger payloads, and more failure modes.

In Daniel's search episode, multimodal embedding work appears in both ingestion
and query handling. The pipeline must batch-embed documents and images during
ingestion, then embed the user query quickly at query time. At 30:22, he
describes these as two instances of the same vector compute problem, with
different latency requirements. Ingestion can be batched, but query handling must
be fast. Both processes must stay consistent because they land in the same
vector space.

Aishwarya's autonomous driving context at 53:20 adds the real-time inference
constraint. A vehicle can't wait seconds for a multimodal model to process a
scene. The model must be compressed, quantized, and optimized to run on
on-vehicle hardware within milliseconds. These are
[[model optimization]] and
[[production]] challenges that apply to
any multimodal system deployed under latency constraints.

For the search and retrieval side, Daniel's episode at 34:00 covers hybrid
search. It combines multimodal vector similarity with business constraints like
recency, filters, and popularity. The system layers vector proximity with
metadata constraints. The results satisfy both semantic relevance and product
requirements.

## Related Pages

These pages cover adjacent model, retrieval, and production topics:

- [[LLMs]]
- [[Generative AI]]
- [[Embeddings]]
- [[Vector Databases]]
- [[Computer Vision]]
- [[Autonomous Driving AI]]
- [[AI Engineering]]
