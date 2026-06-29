---
layout: podcast_summary
title: "Deploying LLMs in Production: Fine-Tuning, Retrieval & Open-Source vs API Tradeoffs"
source_episode: "datatalksclub.github.io/_podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.md"
source_url: "https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html"
season: 15
episode: 3
guests: ["meryemarik"]
topics: ["LLMs", "MLOps", "open-source", "production", "retrieval-augmented generation"]
summary_status: source-index
youtube_url: "https://www.youtube.com/watch?v=6dn6uZFkk04"
spotify_url: "https://open.spotify.com/episode/0tmi2ytNk1bEPldcbhkvhN?si=DtU2OM3RTFmPBdY8sFCv5g"
apple_url: "https://podcasts.apple.com/us/podcast/llms-for-everyone-meryem-arik/id1541710331?i=1000622675129"
---
# Deploying LLMs in Production: Fine-Tuning, Retrieval & Open-Source vs API Tradeoffs

## Original Episode

- [Open the original DataTalks.Club podcast page](https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html)
- [Watch on YouTube](https://www.youtube.com/watch?v=6dn6uZFkk04)
- [Listen on Spotify](https://open.spotify.com/episode/0tmi2ytNk1bEPldcbhkvhN?si=DtU2OM3RTFmPBdY8sFCv5g)
- [Listen on Apple Podcasts](https://podcasts.apple.com/us/podcast/llms-for-everyone-meryem-arik/id1541710331?i=1000622675129)

## Episode Overview

How do you take large language models from experiment to reliable production—balancing fine-tuning, retrieval strategies, and the tradeoffs between open-source models and API services? In this episode, Meryem Arik, a recovering physicist and co-founder of TitanML, walks through practical choices for LLM deployment based on her pivot from computer vision to building tools that make models smaller, cheaper, and easier to run in production.

## Chapter Summary

- 0:00 - [Episode Introduction: LLMs for Everyone](https://www.youtube.com/watch?v=6dn6uZFkk04&t=0)
- 1:07 - [Guest Introduction: Meryem Arik and TitanML](https://www.youtube.com/watch?v=6dn6uZFkk04&t=67)
- 1:45 - [Career Journey: Theoretical Physics → Banking → Tech](https://www.youtube.com/watch?v=6dn6uZFkk04&t=105)
- 2:13 - [Founding TitanML: pivot from computer vision to LLM deployability](https://www.youtube.com/watch?v=6dn6uZFkk04&t=133)
- 4:49 - [Startup Realities: co-founder roles, operations, and tradeoffs](https://www.youtube.com/watch?v=6dn6uZFkk04&t=289)
- 6:42 - [Early LLM Interest: customer-driven pivot and GPT-3 experience](https://www.youtube.com/watch?v=6dn6uZFkk04&t=402)
- 9:17 - [ChatGPT Breakthrough: conversational interface and accessibility](https://www.youtube.com/watch?v=6dn6uZFkk04&t=557)
- 10:24 - [LLM Fundamentals: generative vs. non-generative models and transformers](https://www.youtube.com/watch?v=6dn6uZFkk04&t=624)
- 11:44 - [Model Selection: classification tasks vs. generative tasks](https://www.youtube.com/watch?v=6dn6uZFkk04&t=704)
- 13:45 - [Open-source Model Landscape: LLaMA, FLAN-T5, Falcon, MPT](https://www.youtube.com/watch?v=6dn6uZFkk04&t=825)
- 14:45 - [Why LLMs Matter: handling unstructured text at scale](https://www.youtube.com/watch?v=6dn6uZFkk04&t=885)
- 16:48 - [Open-source vs API Models: control, privacy, and fine-tuning benefits](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1008)
- 18:46 - [Model Drift & API Risk: hidden model changes and production impact](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1126)
- 23:37 - [TitanML Product Suite: Train, Optimized, and Takeoff server](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1417)
- 25:26 - [Serving Challenges: model size, compression, and inference optimization](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1526)
- 26:30 - [Fine-tuning Purpose: specialization, domain adaptation, and tone](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1590)
- 31:38 - [Fine-tuning Generative Models: data formats and end-task considerations](https://www.youtube.com/watch?v=6dn6uZFkk04&t=1898)
- 33:58 - [Workforce Impact: productivity gains and job disruption scenarios](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2038)
- 40:46 - [Dealing with Changing Knowledge: retrieval over continuous retraining](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2446)
- 42:02 - [Grounding Answers: indexing docs and retrieval-augmented responses](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2522)
- 46:42 - [Retrieval Patterns: injecting passages, summarizers, and grounding layers](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2802)
- 48:01 - [Vector Databases Explained: embeddings, indexing, and semantic search](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2881)
- 49:44 - [Prototyping vs Production: when to use GPT-3.5/4 APIs vs open-source LLMs](https://www.youtube.com/watch?v=6dn6uZFkk04&t=2984)
- 51:35 - [Latency & Cost Tradeoffs: self-hosting performance and hardware choices](https://www.youtube.com/watch?v=6dn6uZFkk04&t=3095)
- 53:34 - [Data Quality Metrics: gold-standard examples and output-driven evaluation](https://www.youtube.com/watch?v=6dn6uZFkk04&t=3214)
- 55:32 - [Dataset Expansion: LLM-assisted augmentation for training data](https://www.youtube.com/watch?v=6dn6uZFkk04&t=3332)
- 56:39 - [Evaluation & Benchmarking: classification vs generative metrics and human](https://www.youtube.com/watch?v=6dn6uZFkk04&t=3399)
- 59:08 - [Learning Resources: Hugging Face, Cohere LLM University, community content](https://www.youtube.com/watch?v=6dn6uZFkk04&t=3548)
