---
layout: "person"
title: "Lars Albertsson"
source_person: "../datatalksclub.github.io/_people/larsalbertsson.md"
person_id: "larsalbertsson"
summary: "Data engineering founder and speaker contributing DataOps patterns for scalable platforms, immutable pipelines, and self-service data work."
expertise: ["DataOps", "data engineering", "MLOps", "data strategy", "production"]
podcast_episodes: ["dataops-principles-and-scalable-data-platforms"]
curated: "true"
source_url: "https://datatalks.club/people/larsalbertsson.html"
---

## Background

Lars Albertsson is the founder of Scling, a data engineering startup in
Stockholm. In his DataTalks.Club episode, he draws on work at Google and
Spotify. He also brings experience from Schibsted and consulting projects to
explain [DataOps]({{ '/wiki/dataops/' | relative_url }}) for growing data
teams.

## DataOps as Enablement

In
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
Lars defines DataOps around enablement, workflows, and people alignment. Around
11:50, he describes DataOps as the discipline that lets data teams deliver data
work repeatedly instead of treating every pipeline as a one-off project.

That framing makes his episode useful for
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[DataOps platforms]({{ '/wiki/dataops-platforms/' | relative_url }}), and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
The emphasis isn't only tooling. The team needs working agreements, repeatable
delivery, and a platform that lets analysts and engineers use data without
waiting on every request.

## Immutable Pipelines and Reproducibility

Lars's strongest technical contribution is the case for immutable pipelines.
Around 16:42, he connects data platform design with functional architecture.
Around 20:12, he contrasts reproducible immutable paths with mutable ETL jobs
that overwrite outputs and make debugging harder.

This is why wiki pages cite him when they discuss [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}),
[DataOps vs Data Engineering]({{ '/wiki/dataops-vs-data-engineering/' | relative_url }}),
and [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
For Lars, a pipeline should let the team rerun work and look at versions. The
team should also understand which code produced which data. Reproducibility is
the operating base for trust.

## Platform Components and Self-Service

The episode also explains how a platform team can serve many data users. Around
7:52, Lars discusses scaling data teams and self-service at Spotify. Around
28:22 and 30:34, he separates data entry and exit paths from storage, compute,
and workflow engines. That gives agents a useful map for pages about
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
[orchestration]({{ '/wiki/orchestration/' | relative_url }}), and
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}).

Lars treats a data lake or lakehouse as a platform component. Storage needs
compute and workflow management. It also needs governance and clear access
paths. At 50:13, he adds the organizational side: teams can embed engineers
with analysts so self-service doesn't mean unsupported work.

## Batch, Streaming, and Lakehouse Tradeoffs

Around 41:53, Lars compares batch processing with streaming by latency and use
case.
Around 45:11, he discusses micro-batching and dependency management. Around
1:07:52, he describes lakehouse architecture as warehouse-like capabilities
layered on a data lake.

These sections support [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}),
[Data Warehouse vs Data Lakehouse]({{ '/wiki/data-warehouse-vs-data-lakehouse/' | relative_url }}),
and [Delta Lake]({{ '/wiki/delta-lake/' | relative_url }}). The practical rule
is to choose the architecture that matches latency, dependency, governance, and
recovery needs.

## DataOps, MLOps, and Data Mesh

Around 53:31, Lars compares [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). The two share delivery,
reproducibility practices, and operations work, but ML adds model-specific
requirements. Around 57:46 and 1:03:02, he covers
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}) and the risk of splitting
platform ownership before the organization can support it.

That makes Lars a useful source for
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}),
[Data Mesh vs Centralized Data Platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }}),
and [data strategy]({{ '/wiki/data-strategy/' | relative_url }}).

## Concepts Connected

Use this page when a wiki or guide page needs Lars's specific contribution to
these topics.

- [DataOps]({{ '/wiki/dataops/' | relative_url }}) and [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) for platform delivery and pipeline discipline.
- [MLOps]({{ '/wiki/mlops/' | relative_url }}) for overlap between data platform reliability and ML operations.
- [data strategy]({{ '/wiki/data-strategy/' | relative_url }}), [production]({{ '/wiki/production/' | relative_url }}), and [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}) for organizational use of data platforms.
