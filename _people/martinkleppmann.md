---
layout: "person"
title: "Martin Kleppmann"
summary: "Martin Kleppmann's DataTalks.Club material on reliable data systems, distributed systems, consistency, storage, streaming, and engineering tradeoffs."
source_person: "../datatalksclub.github.io/_people/martinkleppmann.md"
person_id: "martinkleppmann"
source_url: "https://datatalks.club/people/martinkleppmann.html"
podcast_episodes: []
expertise: ["distributed systems", "data engineering", "data systems", "streaming", "storage", "consistency"]
twitter: "martinkl"
linkedin: "martinkleppmann"
web: "https://martin.kleppmann.com/"
curated: "true"
---

Martin Kleppmann is a distributed-systems researcher at the University of
Cambridge. He's also the author of Designing Data-Intensive Applications. In
DataTalks.Club, his main contribution is the
[Designing Data-Intensive Applications Book of the Week AMA](https://datatalks.club/books/20210308-designing-data-intensive-applications.html).
[DataTalks.Club Behind the Scenes]({{ '/podcasts/datatalksclub-building-scaling-data-community/' | relative_url }})
later describes that AMA as one of the community's most notable guest moments.

His answers keep data engineering close to engineering judgment. Teams should
understand the requirements, preserve flexibility where it matters, and choose
systems by their tradeoffs instead of hype. That framing explains why later
DataTalks.Club guests recommend the book in practical episodes about
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), and
[streaming]({{ '/wiki/streaming/' | relative_url }}).

## Reliable Data Systems Start Simple

When a community member asked whether startups should plan for data-intensive
scale from the beginning, Martin argued against early over-investment for
ordinary SaaS companies. If the product isn't yet processing large volumes of
data, he preferred a simple PostgreSQL-based architecture. Early-stage teams
need flexibility and quick customer learning. A complicated scalable design can
wait until the team has a real scale problem
([Designing Data-Intensive Applications AMA](https://datatalks.club/books/20210308-designing-data-intensive-applications.html)).

That answer fits the way DataTalks.Club episodes discuss
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Infrastructure becomes valuable when scale creates operating pressure. It also
complements
[How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }}).
A practical pipeline design starts from source systems and consumers. It then
adds orchestration and quality checks rather than a tool-first stack.

## Tool Choices Are Tradeoffs, Not Badges

Martin repeatedly pushed back on universal answers. In the AMA, he said teams
should consider familiarity with existing tools. They also shouldn't stretch
one familiar tool across every problem. He warned that fashion can influence
technical choices when people follow conference talks or social-media
excitement instead of requirements.

When a community member asked for the most
overlooked principle in data-intensive applications, Martin declined to name a
single rule. He emphasized knowing the tradeoffs well enough to choose the
right tool for the job.

This is why Designing Data-Intensive Applications appears as a recommended
resource in Angela Ramirez's fraud-detection episode. Angela points listeners
toward data-engineering overview material and the book.

The conversation also notes that a third reading would still surface more detail
([Build and Scale Data Engineering Systems for Fraud Detection]({{ '/podcasts/building-and-scaling-data-engineering-systems-for-fraud-detection/' | relative_url }}),
1:00:17-1:01:12). [Angela Ramirez]({{ '/people/angelaramirez/' | relative_url }})
discusses batch features, real-time scoring, and graph databases in that
episode. She also covers dashboards and production debugging. The recommendation
sits in a concrete
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) setting.

## Event Streams and Consistency Boundaries

Martin's microservices answer turns a distributed-systems concept into
architecture guidance. He said most microservices keep transactions inside one
service boundary rather than across services. If two services need atomic
commit, teams can make the boundary coarser and merge them. Teams can also
communicate through a persistent log such as Kafka.

That gives a different guarantee from distributed transactions. It still gives
stronger assurance that consumers can read the same durable messages
([Designing Data-Intensive Applications AMA](https://datatalks.club/books/20210308-designing-data-intensive-applications.html)).

He makes the same kind of distinction in the consistency discussion. For a
distributed queue, he says linearizability is a property of particular
operations, not a label to paste onto a whole system. Enqueue and dequeue
operations can be linearizable even if other operations have different
guarantees. That precision is useful for DataTalks.Club pages on
[streaming]({{ '/wiki/streaming/' | relative_url }}),
[batch vs streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}),
[CDC]({{ '/wiki/cdc/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
Those pages need the same guarantee check for each pipeline.

## Storage, Caches, and Data Modeling

Several AMA threads dig into storage mechanics. Martin explained that
in-memory databases can avoid conversion between disk-oriented and
memory-oriented representations. In a cache discussion, he separated database
buffer caches from application-level caches such as Redis or Memcached.

Application caches can store precomputed responses and business logic, so they
can save computation as well as I/O. In a question about B-trees and LSM trees,
he framed LSM-style writes as a more sequential disk access structure. He did
not reduce the topic to whether one design writes less data.

His data-modeling advice is similarly contextual. For banking systems, he said
"banking" is too broad for one database style. Fraud-prevention, mortgage, and
trading workloads can have different needs.

He still showed sympathy for organizations that stay with a relational database
when it covers many needs. Adopting another storage technology also means
backups and disaster recovery. It also means ETL, audit logs, and operational
support. That makes his answers
relevant to [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}), and
[data strategy]({{ '/wiki/data-strategy/' | relative_url }}), not just low-level
storage internals.

## Raw Data, Derived State, and Dataflow Interfaces

For an NLP startup storing large semi-structured documents, Martin avoided a
generic prescription and asked for the access paths first. Postgres might still
work with sharding. Object storage such as S3 could scale large objects, but it
could make indexing harder. His strongest reusable approach was to keep raw
customer data and separately store derived data. That lets the team re-run
processing logic when requirements change
([Designing Data-Intensive Applications AMA](https://datatalks.club/books/20210308-designing-data-intensive-applications.html)).

In another thread, he said a major idea from the book's final chapter had moved
slowly. The idea was to redesign APIs around dataflow rather than
request-response interaction. He referenced change data capture, stream
processing, and event subscriptions as pieces that move applications closer to
reliable derived views. That idea sits naturally beside DataTalks.Club pages on
[data products]({{ '/wiki/data-products/' | relative_url }}),
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}), and
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).
Downstream teams need stable, understandable interfaces to data.

## Distributed Systems Research and Learning

Martin's short bio matters because it explains the stance in his answers. He
moved from software engineering and startups into research because he wanted
space to think over a longer time horizon. He also wanted to improve the
foundations of how software is built.

In the AMA, he named CRDTs and local-first software as research areas he was
excited about. He described Rust as interesting for systems work because it's
memory-safe, thread-capable, portable, and avoids a garbage-collected runtime.
He still refused to name a universal programming language for distributed
systems. The architecture and runtime needs of the particular system matter
more.

DataTalks.Club returns to the book as a learning reference in career
conversations. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
the discussion identifies Martin as the author of Designing Data-Intensive
Applications. That happens after
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) mentions
data-intensive systems books during a resource discussion (1:01:56-1:02:22).

The recurring approach is clear. Martin's DataTalks.Club footprint is less
about one tool and more about reasoning through
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[data engineering roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }}),
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}), and
distributed-systems tradeoffs.
