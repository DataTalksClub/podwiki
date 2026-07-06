---
layout: wiki
title: "Tools"
summary: "How data and ML teams choose and sustain tools across data engineering, MLOps, search, RAG, open source, and developer experience."
related:
  - Data Engineering Tools
  - MLOps Tools
  - DataOps
  - Orchestration
  - Retrieval-Augmented Generation
  - Open Source and Developer Relations
  - Developer Experience
---

Tools help data and ML teams repeat work through systems, libraries,
platforms, or workflows. Tools are most useful when they encode a practice.

They can encode ingestion, transformation, orchestration and experiment
tracking, and they can also encode deployment. Monitoring, retrieval,
evaluation, and contribution belong in the same tool conversation. Tools matter
less when the conversation turns into names without ownership, tests, docs, or
feedback.

That structure appears across data engineering, ML platforms, and open-source
tooling. [[person:nataliekwong=>Natalie Kwong]]
uses Airbyte, dbt, and Airflow to explain modern data engineering tradeoffs.
She also covers CDC, data lakes, and warehouses in
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].

[[person:simonstiebellehner=>Simon Stiebellehner]]
frames ML platform tools as part of MLOps. In his framing, MLOps combines
people, processes, and technology
in
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
[[person:vincentwarmerdam=>Vincent Warmerdam]]
uses scikit-learn and plugins to make tool sustainability a governance question.
CI and teaching material make education part of tool sustainability
in
[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].

Start with these nearby pages:

- [[Data Engineering Tools]]
- [[MLOps Tools]]
- [[DataOps]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Open Source and Developer Relations]]
- [[Developer Experience]]

## Tool Value

Tool choice isn't a shopping list. A tool matters when it removes a concrete
bottleneck or makes a practice repeatable. In
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]],
Natalie starts from the pipeline layout. Airbyte handles extract-load work,
teams run dbt-style transformations after data is loaded into the warehouse,
and Airflow coordinates recurring jobs.

Low-code and no-code tools change the data engineering role without removing
the need for data engineers.

Teams choose tools by deciding where ingestion and transformation belong. They
also decide who owns orchestration and the resulting data.

Simon makes the same point from the ML platform side. In
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]],
he links experiment tracking and model registries to the data science
workflow. Batch inference, online serving, and orchestration belong there too.
Metadata and monitoring sit on the same path.

He warns against building a heavy platform before a team has real models and
business value. The team also needs repeated use cases that make the platform
tool worth the weight.

[[person:raphaelhoogvliets=>Raphaël Hoogvliets]]
adds the adoption test in
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
His centralized MLOps team starts from product-team pain points and quick
wins. It also listens for feedback. Only then do CI and repository structure
become meaningful.

Tests and traceability fit into the same adoption path. Data versioning and
package registries fit there too, along with serving. Monitoring, Docker, and
Kubernetes also enter the same platform conversation. Databricks belongs in
that platform toolset as well.

For nearby graph nodes, see:

- [[Platform Engineering]]
- [[Platform Adoption]]
- [[ML Platforms]]
- [[Data Engineering Platforms]]

## Tools Versus Practices

A tool category still has to be separated from the practice around it. In
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]],
[[person:tomaszhinc=>Tomasz Hinc]] discusses Terraform,
Terragrunt, and Atlantis. He also covers Git branches, merge requests, Docker,
and fixed versions. IAM and password managers belong to the same operational
surface. Command-line comfort and CI migration belong there too.

Those are tools, but his larger point is reproducible and less frightening
data work. Platform onboarding moves from asking someone for infrastructure to
making reviewed changes through the platform team's path.

[[person:larsalbertsson=>Lars Albertsson]] makes the
same distinction in
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
He places storage, compute, and a workflow engine at the center of a data
platform. The workflow engine handles dependencies, schedules,
data-arrival triggers, and retries. Spark, Flink, SQL, or another compute
system does the processing.

Teams still need dependency-aware data delivery, and the orchestrator is only
one part of it.

[[person:christopherbergh=>Christopher Bergh]] gives
the reliability version in
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
He connects DataOps to version control and testing, with CI/CD and
observability next to those practices. Runbooks and automation belong there
too. Christopher keeps the emphasis on delivery confidence and recovery rather
than tool labels.


- [[Orchestration]]
- [[ci-cd=>CI/CD]]
- [[Reproducibility]]
- [[Data Quality and Observability]]

## Data Engineering Stack

Data engineering tool choices start with where work belongs. Natalie's modern
stack account uses Airbyte for ingestion, while warehouses and lakes handle
storage. Analysts use dbt-style SQL transformations for analytics work, while
Airflow handles scheduling and orchestration.

In
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]],
Natalie explains the ELT benefit. Analysts get more room to work in SQL after
raw data is loaded. Airflow appears as the scheduler, not the place where every
transformation should live.

Storage decisions stay concrete because data lakes fit unstructured files, logs,
and media, but they need governance to avoid data swamps. Warehouses fit
structured analytics and consumption layers. She treats lake-versus-warehouse as
an architecture decision rather than a
winner-takes-all tool choice, and connects Airbyte's open-source and cloud
model to licensing risk and CDC.

That stack view links directly to these graph nodes:

- [[Modern Data Stack]]
- [[ETL]]
- [[ETL vs ELT]]
- [[dbt]]
- [[Data Lake]]
- [[Data Warehouse]]

For article coverage, see
[[Data Engineering Tools]]
and [[Apache Airflow]].

## MLOps and ML Platform Tools

MLOps tooling starts from the model lifecycle, but it quickly becomes platform
work. Simon names self-service compute, notebooks, BigQuery, and Databricks. He
then adds experiment tracking
and model registries. Batch inference, online serving, and pipeline tools come
next.

Simon also covers metadata and lineage. Governance, prediction schemas, and
monitoring complete that platform view
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
He names cloud infrastructure, Kubernetes, and Terraform as core platform
skills. The [[ml-platform-engineer-role=>ML Platform Engineer Role]] covers that
tool ownership when it becomes a shared internal service.

Raphaël gives the operating-team version. His MLOps team supports
product teams and gathers pain points. It standardizes CI and repository
structure.

Testing and traceability come next. Dependency management and package
registries complete the operating path, along with serving and monitoring
([[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
Experiment tracking and model registry appear as the recognizable MLOps
toolset. Serving and monitoring appear there too. The earlier adoption
path explains why a team would introduce them.

[[person:willempienaar=>Willem Pienaar]] draws a
narrower ML tool boundary in
[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]].
He distinguishes upstream transformation systems such as dbt, Airflow, and
Spark from feature-store responsibilities such as feature serving and
materialization.

Feast relies more on existing upstream jobs for backfills, while Tecton can
own more of that flow. That makes feature stores part of the MLOps stack, but
not a replacement for orchestration or transformation design.


- [[MLOps]]
- [[MLOps Tools]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Orchestration]]

For article coverage, see
[[MLOps Tools]].

## Search, RAG, and Agent Tooling

Search and RAG tooling is retrieval architecture, not prompt decoration.
[[person:atitaarora=>Atita Arora]] starts
from Solr, Lucene, and full-text search in
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
She then moves to NLP and vector databases.

She compares standalone vector databases with adding vectors to an existing
search stack. Her transcript chatbot uses chunking and overlap, embeddings,
and LangChain orchestration. Prompt context and citations are part of that
same RAG design. When a team is choosing model and retrieval pieces, continue
with [[llm-tools=>LLM Tools for Real Products]] for evaluation and review too.
Evaluation and human review come back into the system.

[[person:danielsvonava=>Daniel Svonava]] adds the
production-search view in
[[cite:building-production-search-systems=>Building Search Systems]].
He separates retrieval from ranking, vector compute from vector
storage, and pure similarity from production ranking. Filters and recency
still matter. Business rules and evaluation matter too. Those distinctions
explain why vector databases are one tool inside a search product, not the
whole product.

[[person:ranjithakulkarni=>Ranjitha Kulkarni]] extends
the tool question to agents in
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Agents use tools and memory, with knowledge stores nearby. She discusses
prompts, SDKs, wrappers, and integration abstractions. She also contrasts code
agents with natural-language agents, which makes
[[multi-agent-systems=>Multi-Agent Systems]] part of the same tooling boundary.

Framework choices include building from scratch and using LangChain. She also
discusses the OpenAI Agents SDK and smaller agent libraries. Agent
marketplaces and tool protocols enter the same agent-tooling surface.


For evaluation, she adds custom datasets and mocked tools. Integration tests,
regression tests, and outcome-based assertions complete that testing view.


- [[Search]]
- [[Vector Databases]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Agent Engineering]]
- [[LLM Production Patterns]]

## Open Source and Developer Experience

Open-source tooling adds governance and contribution paths, plus licensing and
education. Business models are part of the same topic. In
[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]],
Vincent covers scikit-learn governance and NumFOCUS. He also covers
plugin-versus-core strategy, maintainer transition, and volunteer motivation.

He also discusses CI cost and custom runners, and he teaches Docker, pip, and
Git. For business models, he names training and consulting. Partnerships are
another option. Plugins become a way to expand the ecosystem without forcing
every idea into scikit-learn core.

[[person:hugobowneanderson=>Hugo Bowne-Anderson]]
connects developer relations to tool adoption in
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Metaflow integrations include AWS, Kubernetes, and Argo, and ML
interoperability belongs to the same adoption surface. DevRel becomes education
and documentation. It also becomes a wisdom layer around tools.

Feedback, documentation, dogfooding, and reproducible workflows all become
part of tool improvement.

[[person:elleobrien=>Elle O'Brien]] gives the
data-science DevRel version in
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].
Her work around DVC and CML treats developer experience as work, not
decoration. Docs, pull requests, and videos belong there too. Support and
community work belong there as well.

Public tools need people to learn them and trust them. They also need people
to report friction and contribute without creating avoidable maintainer load.


- [[Open Source]]
- [[Developer Relations]]
- [[Documentation]]
- [[Contributing]]
- [[Technical Writing]]
- [[Open Source Portfolio Evidence]]

## Choosing a Tool

Tool choice starts with the work the team must repeat. For data engineering,
the question is where ingestion and transformation belong.
Teams also decide where orchestration and quality belong. Storage and
activation belong in that decision too.

Natalie's Airbyte, dbt, and Airflow map covers that structure. CDC, warehouses,
and lakes are part of the same decision
([[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]]).

For MLOps, the question is whether the team has repeated model workflows that
need tracking and registries. They may also need deployment paths, monitoring,
and governance.
Simon warns against building the platform too early. Raphaël's centralized
MLOps team earns adoption through pain points and quick wins
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]],
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

For search, RAG, and agents, the question is whether the product needs
retrieval and ranking. It may also need context packaging or tool use. Some
products need actions and evaluation.

Atita and Daniel keep evaluation in the same conversation as tooling. Ranjitha
does too
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]],
[[cite:building-production-search-systems=>Building Search Systems]],
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

For open source, the question is whether the project can sustain users and
contributors. Vincent and Hugo connect tool health to docs and examples, and
Elle does too.

They also connect tool health to governance and CI, while contribution
etiquette and feedback belong in the same decision. Business models belong
there too
([[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]],
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]],
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]]).

## Related Pages

Data, ML, orchestration, and open-source tool choices split across these pages:

- [[Data Engineering Tools]]
- [[MLOps Tools]]
- [[DataOps Tools]]
- [[Orchestration]]
- [[Platform Engineering]]
- [[ML Platforms]]
- [[Developer Experience]]
- [[Open Source and Developer Relations]]
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
- [[Agent Engineering]]
