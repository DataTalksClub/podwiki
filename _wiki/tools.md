---
layout: wiki
title: "Tools"
summary: "How DataTalks.Club podcast guests choose, operate, teach, and sustain tools across data engineering, MLOps, DataOps, search, RAG, open source, and developer experience."
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
platforms, or workflows. DataTalks.Club guests treat tools as most useful when
they encode a practice.

They can encode ingestion, transformation, orchestration and experiment
tracking, and they can also encode deployment. Monitoring, retrieval,
evaluation, and contribution belong in the same tool conversation. Tools matter
less when the conversation turns into names without ownership, tests, docs, or
feedback.

Several episodes return to that structure. [[person:nataliekwong|Natalie Kwong]]
uses Airbyte, dbt, and Airflow to explain modern data engineering tradeoffs.
She also covers CDC, data lakes, and warehouses in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]].

[[person:simonstiebellehner|Simon Stiebellehner]]
frames ML platform tools as part of MLOps. In his framing, MLOps combines
people, processes, and technology
in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
[[person:vincentwarmerdam|Vincent Warmerdam]]
uses scikit-learn and plugins to show why tool sustainability is also
governance. CI and teaching material bring education into the same discussion
in
[[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].

Start with these nearby pages:

- [[Data Engineering Tools]]
- [[MLOps Tools]]
- [[DataOps]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[Open Source and Developer Relations]]
- [[Developer Experience]]

## Tool Value

DataTalks.Club guests don't treat tools as a shopping list. A tool matters when it
removes a concrete bottleneck or makes a practice repeatable. In
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
Natalie starts from the pipeline layout. Airbyte handles extract-load work,
teams run dbt-style transformations after data is loaded into the warehouse,
and Airflow coordinates recurring jobs.

Around 39:06, low-code and no-code tools change the data engineering role.
They don't remove the need for data engineers.

Teams choose tools by deciding where ingestion and transformation belong. They
also decide who owns orchestration and the resulting data.

Simon makes the same point from the ML platform side. In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
he links experiment tracking and model registries to the data science
workflow. Batch inference, online serving, and orchestration belong there too.
Metadata and monitoring sit on the same path.

Around 47:08 and 49:19, he warns against building a heavy platform before a
team has real models and business value. The team also needs repeated needs
before a platform tool is worth the weight.

[[person:raphaelhoogvliets|Raphaël Hoogvliets]]
adds the adoption test in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
His centralized MLOps team starts from product-team pain points and quick
wins. It also listens for feedback. Only then do CI and repository structure
become meaningful.

Tests and traceability fit into the same adoption path. Data versioning and
package registries fit there too, along with serving. Monitoring, Docker, and
Kubernetes also enter the same platform conversation. Databricks appears in
that discussion as well.

For nearby graph nodes, see:

- [[Platform Engineering]]
- [[Platform Adoption]]
- [[ML Platforms]]
- [[Data Engineering Platforms]]

## Tools Versus Practices

Many podcast guests separate a tool category from the practice around it. In
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]],
[[person:tomaszhinc|Tomasz Hinc]] discusses Terraform,
Terragrunt, and Atlantis. He also covers Git branches, merge requests, Docker,
and fixed versions. IAM and password managers belong to the same operational
surface. Command-line comfort and CI migration belong there too.

Those are tools, but his larger point is reproducible and less frightening
data work.
At 12:40-13:07, platform onboarding moves from asking someone for
infrastructure to making reviewed changes through the platform team's path.

[[person:larsalbertsson|Lars Albertsson]] makes the
same distinction in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
Around 30:34-35:57, he places storage, compute, and a workflow engine at the
center of a data platform. The workflow engine handles dependencies,
schedules, data-arrival triggers, and retries. Spark, Flink, SQL, or another
compute system does the processing.

Teams still need dependency-aware data delivery, and the orchestrator is only
one part of it.

[[person:christopherbergh|Christopher Bergh]] gives
the reliability version in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
He connects DataOps to version control and testing, with CI/CD and
observability next to those practices. Runbooks and automation belong there
too. Christopher keeps the emphasis on delivery confidence and recovery rather
than tool labels.

See also:

- [[Orchestration]]
- [[ci-cd|CI/CD]]
- [[Reproducibility]]
- [[Data Quality and Observability]]

## Data Engineering Stack

Data engineering tool choices start with where work belongs. Natalie's modern
stack discussion uses Airbyte for ingestion, while warehouses and lakes handle
storage. Analysts use dbt-style SQL transformations for analytics work, while
Airflow handles scheduling and orchestration.

At 7:57 and 12:39 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
Natalie explains the ELT benefit. Analysts get more room to work in SQL after
raw data is loaded. At 30:59, Airflow appears as the scheduler. Natalie
doesn't present Airflow as the place where every transformation should live.

Her episode also keeps storage decisions concrete. Data lakes fit
unstructured files, logs, and media, but they need governance to avoid data
swamps. Warehouses fit structured analytics and consumption layers. Around
27:39, she treats lake-versus-warehouse as an architecture decision rather
than a winner-takes-all tool choice. Around 43:45-49:32, the same episode
connects Airbyte's open-source and cloud model to licensing risk and CDC.

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

MLOps tool discussions in these episodes start from the model lifecycle, but they
quickly become platform discussions. Simon's episode names self-service
compute, notebooks, BigQuery, and Databricks. It then adds experiment tracking
and model registries. Batch inference, online serving, and pipeline tools come
next.

Simon also covers metadata and lineage. Governance, prediction schemas, and
monitoring complete that platform view
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
21:03-54:15). Around 8:11, he names cloud infrastructure, Kubernetes, and
Terraform as core platform skills.

Raphaël's episode gives the operating-team version. His MLOps team supports
product teams and gathers pain points. It standardizes CI and repository
structure.

Testing and traceability come next. Dependency management and package
registries complete the operating path, along with serving and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
23:01-56:50). Around 51:21, experiment tracking and model registry appear as
the recognizable MLOps toolset. Serving and monitoring appear there too. The
earlier adoption discussion explains why a team would introduce them.

[[person:willempienaar|Willem Pienaar]] shows a
narrower ML tool boundary in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]].
He distinguishes upstream transformation systems such as dbt, Airflow, and
Spark from feature-store responsibilities such as feature serving and
materialization.

Feast relies more on existing upstream jobs for backfills, while Tecton can
own more of that flow. That makes feature stores part of the MLOps stack, but
not a replacement for orchestration or transformation design.

See also:

- [[MLOps]]
- [[MLOps Tools]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Orchestration]]

For article coverage, see
[[MLOps Tools]].

## Search, RAG, and Agent Tooling

Search and RAG episodes treat tools as retrieval architecture, not as a prompt
decoration. [[person:atitaarora|Atita Arora]] starts
from Solr, Lucene, and full-text search in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
She then moves to NLP and vector databases.

At 17:01 and 20:27, she compares standalone vector databases with adding
vectors to an existing search stack. At 38:24-42:49, her transcript chatbot
uses chunking and overlap. It also uses embeddings and LangChain
orchestration. Prompt context and citations are part of that same RAG design.
At 48:09, evaluation and human review come back into the system.

[[person:danielsvonava|Daniel Svonava]] adds the
production-search view in
[[podcast:building-production-search-systems|Building Search Systems]].
His discussion separates retrieval from ranking, vector compute from vector
storage, and pure similarity from production ranking. Filters and recency
still matter. Business rules and evaluation matter too. Those distinctions
explain why vector databases are one tool inside a search product, not the
whole product.

[[person:ranjithakulkarni|Ranjitha Kulkarni]] extends
the tool question to agents in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 12:31, agents use tools and memory, with knowledge stores nearby. At
18:23-24:59, she discusses prompts, SDKs and wrappers. Integration
abstractions matter too. She also contrasts code agents with natural-language
agents.

At 44:08-48:00, framework choices include building from scratch and using
LangChain. She also discusses the OpenAI Agents SDK and smaller agent
libraries. Agent marketplaces and tool protocols enter the same discussion.


For evaluation, she adds custom datasets and mocked tools. Integration tests,
regression tests, and outcome-based assertions complete that testing view.

See also:

- [[Search]]
- [[Vector Databases]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[Agent Engineering]]
- [[LLM Production Patterns]]
- [[LLM Tools]]

## Open Source and Developer Experience

Open-source tool discussions add governance and contribution paths, plus
licensing and education. Business models are part of the same topic. Vincent's
[[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]
episode discusses scikit-learn governance and NumFOCUS. It also covers
plugin-versus-core strategy, maintainer transition, and volunteer motivation.

He also discusses CI cost and custom runners, and he teaches Docker, pip, and
Git. For business models, he names training and consulting. Partnerships are
another option. Around 14:01, plugins become a way to expand the ecosystem
without forcing every idea into scikit-learn core.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
connects developer relations to tool adoption in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
At 13:52, Metaflow integrations include AWS, Kubernetes and Argo. ML
interoperability appears in the same discussion. At 18:03, DevRel becomes
education and documentation. It also becomes a wisdom layer around tools.

At 25:17 and 36:27, feedback and documentation become part of tool
improvement. Dogfooding and reproducible workflows matter there too.

[[person:elleobrien|Elle O'Brien]] gives the
data-science DevRel version in
[[podcast:devrel-data-science-open-source-tools|DevRel for Data Science]].
Her work around DVC and CML shows that developer experience is work, not
decoration. Docs, pull requests, and videos belong there too. Support and
community work belong there as well.

Public tools need people to learn them and trust them. They also need people
to report friction and contribute without creating avoidable maintainer load.

See also:

- [[Open Source]]
- [[Developer Relations]]
- [[Documentation]]
- [[Contributing]]
- [[Technical Writing]]
- [[Open Source Portfolio Evidence]]

## Choosing a Tool

Across these episodes, tool choice starts with the work the team must repeat. For
data engineering, the question is where ingestion and transformation belong.
Teams also decide where orchestration and quality belong. Storage and
activation belong in that decision too.

Natalie's Airbyte, dbt, and Airflow discussion gives that map. CDC, warehouses,
and lakes are part of the same decision
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]]).

For MLOps, the question is whether the team has repeated model workflows that
need tracking and registries. They may also need deployment paths, monitoring,
and governance.
Simon warns against building the platform too early. Raphaël shows how a
central MLOps team earns adoption through pain points and quick wins
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

For search, RAG, and agents, the question is whether the product needs
retrieval and ranking. It may also need context packaging or tool use. Some
products need actions and evaluation.

Atita and Daniel keep evaluation in the same conversation as tooling. Ranjitha
does too
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
[[podcast:building-production-search-systems|Building Search Systems]],
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For open source, the question is whether the project can sustain users and
contributors. Vincent and Hugo connect tool health to docs and examples, and
Elle does too.

They also connect tool health to governance and CI, while contribution
etiquette and feedback belong in the same decision. Business models belong
there too
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]],
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]],
[[podcast:devrel-data-science-open-source-tools|DevRel for Data Science]]).

## Related Pages

These pages cover the main neighboring graph nodes for tool choices:

- [[Data Engineering Tools]]
- [[MLOps Tools]]
- [[DataOps Tools]]
- [[Orchestration]]
- [[Platform Engineering]]
- [[ML Platforms]]
- [[Developer Experience]]
- [[Open Source and Developer Relations]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[Agent Engineering]]
