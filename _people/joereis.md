---
layout: "person"
title: "Joe Reis"
summary: "Joe Reis's DataTalks.Club profile, centered on his data engineering principles from the Fundamentals of Data Engineering Book of the Week discussion and the podcast episode that recommends the book."
source_url: "https://datatalks.club/people/joereis.html"
podcast_episodes: []
github: "JoeReis"
linkedin: "josephreis"
web: "https://josephreis.com/"
curated: "true"
expertise: ["data engineering", "data architecture", "data engineering lifecycle", "data modeling", "platform practices", "career development"]
---

# Joe Reis

Joe Reis is a data engineering and architecture consultant. He co-founded
Ternary Data and co-authored Fundamentals of Data Engineering with
[Matthew Housley](https://datatalks.club/people/matthewhousley.html).
DataTalks.Club references Joe mainly through the book and its Book of the Week
Q&A, not through a tagged podcast appearance.

DataTalks.Club podcast mentions Joe when
[Santona Tuli](https://datatalks.club/people/santonatuli.html) recommends
Fundamentals of Data Engineering in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html)
around 59:16. She points listeners toward Joe and Matt's book for data
engineering skills. She then warns that books should be supplemented with
engineering blogs, practitioner conversations, and shorter-form material because
pipeline tooling moves quickly.

## Fundamentals Before Tools

Joe's clearest DataTalks.Club theme is simple: learn
[data engineering]({{ '/wiki/data-engineering/' | relative_url }})
foundations before memorizing tools. In the
[Book of the Week Q&A](https://datatalks.club/books/20220815-fundamentals-of-data-engineering.html),
he says the book gives software engineers a shared foundation. It gives the
same foundation to people working in data science, analytics, or data
engineering. Podcast guests make a similar argument in
[Data Engineering Career Path and Skills](https://datatalks.club/podcast/data-engineering-career-path-and-skills.html),
where [Jeff Katz](https://datatalks.club/people/jeffkatz.html) puts Python and SQL
before advanced distributed tools. He also puts database concepts and cloud
basics early in the path.

Santona's pipeline episode makes the same ordering practical. She starts with
ingestion and orchestration before moving to dbt-style transformation and
staging. She also covers data modeling and ML serving.

Around 59:16 in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
she recommends Joe and Matt's book as a way to learn the field. Read this page with the
[data engineering roadmap]({{ '/wiki/data-engineer-roadmap/' | relative_url }})
and [data engineering tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
pages. Tools matter, but they make more sense after the lifecycle is clear.

## Data Engineering Lifecycle

Joe repeatedly uses the data engineering lifecycle to keep the field coherent.
In the Book of the Week Q&A, he says the book covers data engineering for data
science projects through the lifecycle. He names generation, ingestion,
orchestration, and transformation as core parts of that map. The same map
includes storage, governance, and security.

That framing explains why the book appears in a podcast episode about
end-to-end data pipelines rather than only in a career reading list.

Joe's lifecycle language lines up with Santona's distinction between analytics
pipelines and ML pipelines. Around 13:25-18:44 in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
she separates business-data pipelines from model-operationalization pipelines.

Later, around 37:10-43:05, she treats deduplication and ordering guarantees as
linked design choices. She also connects PII masking, entity modeling, and
marts. Joe's lifecycle
view gives readers a stable map for those choices. Use it alongside
[DataOps]({{ '/wiki/dataops/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

## Tools Versus Principles

Joe's advice on tools is deliberately conservative. When asked how to cut
through marketing hype, he points readers toward choosing the right
technologies as a discipline, not chasing a single product. Matthew adds that
engineers should study classes of technologies rather than individual tools.
Together, that puts tool selection inside architecture judgment.

The podcast material gives that principle concrete examples. Santona compares
Upsolver and dbt by asking whether each tool is mainly for authoring,
execution, or ingestion
([Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
10:48-13:25). She then broadens the tool map to orchestrators, Spark,
Kafka/Kinesis, and feature stores. She also discusses vector databases,
Snowflake, Databricks, and lakehouse designs.

Joe's Q&A advice fits the same habit because it asks readers to decide what the
system needs before choosing the stack. For more tradeoffs, use
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[DataOps vs Data Engineering]({{ '/wiki/dataops-vs-data-engineering/' | relative_url }}),
and [MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}).

## Modeling, Quality, and Platform Practices

Joe's Book of the Week answers treat modeling and quality as core engineering
work. He argues that data modeling needs a renewed conversation, including
streaming and event data. He also discusses graph models, Data Vault,
and Kimball-style marts. Cloud warehouses changed old assumptions too. He says
data quality belongs inside data management, one of the undercurrents of the
data engineering lifecycle.

Santona's episode reinforces the operational side of that stance. Around
39:23-44:57 in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
she moves from transformation work into entity modeling, marts, and dashboards.
She then covers feature engineering, model training, and serving.

That sequence makes Joe's modeling view practical. Data engineers structure
data so analysts, dashboard builders, data scientists, and ML systems can
consume it reliably. Use
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}), and
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).

## Career Development and Stakeholder Work

Joe doesn't reduce data engineering career growth to certifications or tool
names. In the Book of the Week Q&A, he tells learners to choose practice
projects they'll keep working on after the homework is over. He also says
data scientists moving into data engineering should build a network that can
put them near good job and project opportunities. For cloud skills, he treats
cloud certifications as useful baseline context, especially for understanding
how a cloud provider expects its services to be used.

He also emphasizes business empathy. When asked about junior engineers without
stakeholder experience, Joe says embedding with business teams can help
engineers understand downstream requirements. Santona discusses persona-driven
pipeline design around 52:54 in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html).
For the career side, use [career growth]({{ '/wiki/career-growth/' | relative_url }}),
[career transitions in data]({{ '/wiki/career-transitions-in-data/' | relative_url }}),
and [data engineering portfolio projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
pages.

## Related DataTalks.Club Threads

Use these follow-up paths from Joe's DataTalks.Club material.

- [Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html)
  is the specific podcast episode that recommends Joe and Matt's book and
  covers the pipeline design topics that make the book relevant.
- [Matthew Housley](https://datatalks.club/people/matthewhousley.html) is Joe's
  co-author and Ternary Data co-founder. His Q&A answers often extend Joe's
  points on technology classes, off-the-shelf tools, and cloud data systems.
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
  [Data Engineering Roadmap]({{ '/wiki/data-engineer-roadmap/' | relative_url }}),
  and [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
  are the best follow-up hubs for Joe's recurring themes.
