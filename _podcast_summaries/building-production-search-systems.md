---
layout: podcast_summary
title: "Building Search Systems: Dense Embeddings, MLOps and Evaluation Metrics"
source_episode: "datatalksclub.github.io/_podcast/building-production-search-systems.md"
source_url: "https://datatalks.club/podcast/building-production-search-systems.html"
season: 17
episode: 9
guests: ["danielsvonava"]
topics: ["information retrieval", "vector databases", "embeddings", "MLOps", "evaluation metrics", "production", "search"]
summary_status: source-index
youtube_url: "https://www.youtube.com/watch?v=gEmSrknGKDE"
spotify_url: "https://open.spotify.com/episode/19R0rLA8hULTBZi9FhZuTs?si=xggb0OzfRHCFSmXtJWm7bA"
apple_url: "https://podcasts.apple.com/us/podcast/building-production-search-systems-daniel-svonava/id1541710331?i=1000650138905"
---
# Building Search Systems: Dense Embeddings, MLOps and Evaluation Metrics

## Original Episode

Use these links for the canonical episode and media sources.

- [Open the original DataTalks.Club podcast page](https://datatalks.club/podcast/building-production-search-systems.html)
- [Watch on YouTube](https://www.youtube.com/watch?v=gEmSrknGKDE)
- [Listen on Spotify](https://open.spotify.com/episode/19R0rLA8hULTBZi9FhZuTs?si=xggb0OzfRHCFSmXtJWm7bA)
- [Listen on Apple Podcasts](https://podcasts.apple.com/us/podcast/building-production-search-systems-daniel-svonava/id1541710331?i=1000650138905)

## Episode Overview

How do you build search systems that balance dense embeddings, MLOps, and meaningful evaluation metrics? In this episode Daniel Svonava — an entrepreneurial technologist with 20 years of experience (from competitive programming and research internships to leading ML infrastructure at YouTube Ads) and co-founder of Superlinked/VectorHub — walks through practical design and operational decisions for modern search and retrieval.

## People

Use these links to connect the episode to guest notes.

- [Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }})

## Chapter Summary

Use these checkpoints to decide whether to open the source transcript.

- 0:00 - [Podcast Introduction](https://www.youtube.com/watch?v=gEmSrknGKDE&t=0)
- 1:47 - [Guest Introduction: Daniel Svonava, Superlinked & VectorHub](https://www.youtube.com/watch?v=gEmSrknGKDE&t=107)
- 2:40 - [Career Highlights: Internships, YouTube Ads, and Startups](https://www.youtube.com/watch?v=gEmSrknGKDE&t=160)
- 4:59 - [Competitive Programming Influence on Engineering](https://www.youtube.com/watch?v=gEmSrknGKDE&t=299)
- 6:20 - [Framing Search: Decision Problem & Relevance](https://www.youtube.com/watch?v=gEmSrknGKDE&t=380)
- 9:10 - [Information Retrieval vs Recommender Boundaries; Representation Learning](https://www.youtube.com/watch?v=gEmSrknGKDE&t=550)
- 11:29 - [From Bag-of-Words to Dense Vector Representations](https://www.youtube.com/watch?v=gEmSrknGKDE&t=689)
- 12:45 - [Inverted Index Mechanics, Candidate Generation & Ranking](https://www.youtube.com/watch?v=gEmSrknGKDE&t=765)
- 16:45 - [Practical Indexing: Document Chunking and Ingestion](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1005)
- 17:40 - [Use Existing Engines: Lucene and Open-source Tools](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1060)
- 18:49 - [Index Data Structures: Trees, Alphabetical Ordering, and Lookups](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1129)
- 20:02 - [Search Maintenance: Brittleness, Synonyms, and Configuration Debt](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1202)
- 21:55 - [Multi-modal Retrieval and Personalization Requirements](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1315)
- 27:21 - [Vector Databases: Storing Embeddings and Nearest-Neighbor Search](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1641)
- 29:00 - [Vector Compute: Ingestion Encoding vs Query-Time Encoding](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1740)
- 30:22 - [Pipeline Challenges: Recomputing Embeddings and Model Versioning](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1822)
- 32:43 - [CLIP Example: Text-to-Image Cross-modal Search](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1963)
- 33:13 - [Embedding Strategy Changes: Model Swaps and Pipeline Flexibility](https://www.youtube.com/watch?v=gEmSrknGKDE&t=1993)
- 34:00 - [Hybrid Search: Combining Vector Similarity with Filters and Recency](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2040)
- 36:21 - [Custom Embeddings, Ranking Models, and MLOps Trade-offs](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2181)
- 38:11 - [Multi-embedding Design: Titles, Content, Images, and Behavioral Signals](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2291)
- 39:53 - [Expressing Constraints: Lucene Must/Should vs Vector-query Approaches](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2393)
- 40:48 - [Recency and Bias: Encoding Time and Applying Weights in Embeddings](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2448)
- 41:56 - [Timestamp & Positional Encoding Techniques in Vector Space](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2516)
- 45:11 - [Normalizing Components and Late-binding Query Weights](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2711)
- 46:18 - [LLM Contexting: Prompted Timestamps and Limitations](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2778)
- 47:37 - [Limits of LLM-only Retrieval; Value of Specialized Encoders](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2857)
- 49:36 - [Resources & Tutorials: VectorHub Guides on Combining Modalities](https://www.youtube.com/watch?v=gEmSrknGKDE&t=2976)
- 52:35 - [Vendor Selection: Vector DB Feature Comparison and Trade-offs](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3155)
- 54:56 - [When to Use Lucene/Elasticsearch vs Dedicated Vector Databases](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3296)
- 57:48 - [E-commerce Strategy: Prototype with Embeddings for Mid-size D2C](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3468)
- 58:17 - [Rapid Prototyping with CLIP and Steps to Productionize](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3497)
- 1:01:25 - [Measuring Search Impact: Business Metrics, A/B Testing, and USD](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3685)
- 1:03:50 - [Operational Metrics, Offline Evaluation, and Empowering Engineers](https://www.youtube.com/watch?v=gEmSrknGKDE&t=3830)
