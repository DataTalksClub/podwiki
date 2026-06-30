---
layout: wiki
title: "Reproducibility"
summary: "How DataTalks.Club podcast guests make data science, ML, research, and data pipeline work rerunnable, reviewable, and explainable."
related:
  - MLOps
  - DataOps
  - Experiment Tracking
  - Data Quality and Observability
  - ML Platforms
  - Practices
  - Software Engineering
---

Reproducibility means a team can rerun a data result, review it, or explain it
after the original work has moved on. In the DataTalks.Club podcast archive,
it's not just a research virtue or a tooling label. It's the operating habit
that connects an output to the code, data, environment, and parameters behind
it. It also preserves the tests, approvals, and people who shaped the result.

The archive uses reproducibility in three connected settings.
[Johanna Bayer]({{ '/people/johannabayer/' | relative_url }}) describes the
research version as packaging code and papers. The same workflow preserves data
and environments so another researcher can recreate the result in
[Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }}).
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
[DataOps]({{ '/wiki/dataops/' | relative_url }}) version through immutable
datasets and functional transformations in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) and
[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) give
the [MLOps]({{ '/wiki/mlops/' | relative_url }}) version through
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}), metadata, and
lineage. Their episodes also connect reproducibility to data references,
containers, and deployment records in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
and
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).

That makes reproducibility a bridge across engineering, operations, and
platform work. The engineering side includes
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), and
[Testing]({{ '/wiki/testing/' | relative_url }}). The operating side includes
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}).

The exact capture mechanism changes by domain, but the podcast discussions
converge on the same standard. A reproducible team can explain how a result was
produced. It can also identify what must be rerun, reviewed, or changed.

## Common Definition

Across the podcast discussions, reproducibility means a team can recover the
path from input to result. The result may be a paper figure or analytics table.
It may also be a model artifact, dashboard, or prediction. The common requirement is that
someone other than the original author can look at the assumptions, rerun the
work, or explain why the result changed.

[Johanna Bayer]({{ '/people/johannabayer/' | relative_url }}) gives the
research definition in
[Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 8:30-8:51. Her reproducible-paper example packages code with the manuscript
so another person can start from the data and regenerate the paper. At
39:27-43:11, she turns that idea into engineering practice. She names project
structure, environments, Git branches, and formatting. She also uses MLflow for
model version control and preserves metadata or model parameters when sensitive
clinical data can't be shared.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
data-platform definition in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
at 16:42-21:29. He argues that mutable warehouse-style tables make reruns
unstable because the same ETL process can produce different results at
different times. His answer is immutable raw data plus functional
transformations, orchestrated as pipelines that create new datasets instead of
overwriting old ones.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
connects the same principle to ML delivery in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 42:54-44:46. He says full reproducibility is hard, but tying code to data
versions helps teams reverse-engineer what happened. He also makes maturity
part of the definition. Smaller teams may not need full data versioning on day
one, but work with regulation or customer-facing decisions may need it earlier.

## Different Emphases

Guests differ most on scope and timing because some start from teaching, while
others start from operations or platform risk.

Bayer and O'Brien start from teaching.
Researchers and junior data scientists need Git, data management,
and reproducible examples. They also need an end-to-end view of a project
before they enter teams that depend on their work. O'Brien discusses this in
[DevRel for Data Science]({{ '/podcasts/devrel-data-science-open-source-tools/' | relative_url }})
at 4:22-7:59 and 52:06-55:28.

Albertsson and Bergh start from operations. Albertsson emphasizes
architectural immutability and raw-data history, while Bergh emphasizes
delivery discipline. Teams put code, reports, and
transformations in version control. They also run automated tests, use CI/CD,
and run the whole system against test data when possible
([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
at 33:47-44:12).

Hoogvliets and
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
start from ML platforms. They focus on experiment tracking, model registries,
metadata, and data references. They also focus on deployment records, package
registries, and monitoring.

Stiebellehner is especially cautious about copying every training dataset into
an experiment tracker. Large datasets can make that approach unworkable. Cost
and GDPR deletion requests can do the same
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 42:48-46:32).

They don't disagree about whether reproducibility matters. They disagree about
where to spend the next unit of effort. A research lab may need tests and a
reproducible paper template. A data platform may need immutable raw inputs and
workflow orchestration.

An ML platform may need experiment tracking first. As
model risk grows, it may also need data versioning, dependency management, and
lineage.

## Research and Teaching

The academic episodes frame reproducibility as a skill gap as much as a tooling
gap. Bayer says academia faces a reproducibility crisis. People publish papers
that others can't recreate, especially in fields such as neuroimaging
([Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 8:30-8:51).

Her course sequence starts with Git and reproducible publications. It then
moves into tests, open source contribution, packaging, and environments. It
also covers requirements files.

O'Brien describes the same gap from data science education. In
[DevRel for Data Science]({{ '/podcasts/devrel-data-science-open-source-tools/' | relative_url }})
at 4:22-7:59, she says labs often lack training for long-lived data
management, collaboration, and complete reproduction of code. She joined
Iterative because she wanted to work on DVC. She later moved into teaching so
applied data science students could make educated choices about managing
projects before they enter industry.

[Mihail Eric]({{ '/people/mihaileric/' | relative_url }}) adds the
research-to-production bridge in
[From Research to Production]({{ '/podcasts/research-to-production-ml-systems-roadmap/' | relative_url }})
at 11:01-12:49. Researchers use notebooks, benchmarks, and tools such as
Weights & Biases to validate hypotheses. At 17:35-17:53, he contrasts that
with the ML engineer's responsibility for deployment, uptime, and monitoring.
He also names Docker, cloud infrastructure, and web services. Reproducibility
improves when researchers learn engineering fundamentals and engineers learn
how to reproduce models and track experiments.

## Data Pipelines

Pipeline reproducibility starts with stable inputs. Albertsson's
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
discussion treats immutable raw data as the foundation. At 16:42-21:29, he
argues that teams should transform immutable datasets into new datasets rather
than mutate tables in place. At 30:34-35:57, he adds workflow orchestration.
Pipelines need explicit dependencies so late data, transient failures, and bugs
can be retried and repaired.

Bergh's DataOps version starts from the delivery path. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
at 33:47-34:37, he names version control, automated tests, and development
tests. He also names deployment automation and error tracking as practical
steps.

At 44:12-48:59, he pushes beyond unit tests. Data teams should run the system
end to end against realistic test data. They should also keep tests close to
the code while running checks in development and production.

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) shows why
infrastructure belongs in the same reproducibility conversation. In
[DataOps and GitOps for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})
at 23:42-26:21, he describes infrastructure as code with Terraform,
Terragrunt, and Atlantis. Teams use merge requests, review, and dry runs. At
1:01:27-1:01:43, he gives a dependency example where an unspecified Python
package version caused a Dockerized application to fail after it fetched a
newer API. Pinning versions
isn't ceremony there because it prevents a future run from silently becoming a
different run.

## MLOps and Platforms

ML reproducibility extends the pipeline record with experiment and artifact
history. Stiebellehner describes experiment tracking as an early win for
collaboration in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:58. The tracked run sits near the model registry because a useful
run may become an artifact that downstream systems consume.

At 42:48-43:28 in the same episode, Stiebellehner expands the record. A
platform may need to store which job image ran, which inputs it consumed, which
outputs it wrote, and how metadata connects across pipeline runs. The model
registry alone isn't enough if a team wants to reproduce a model result from
three years ago. Code versions, data versions, metadata, and workflow design all
matter.

Hoogvliets turns that into an adoption sequence. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 39:06-42:54, he groups CI, repository structure, and parameterization with
testing and experiment preservation. At 48:41-53:08, he recommends starting
from a real pain point. Start with CI/CD when deployment takes months, and
start with monitoring when models are opaque in production. Escalate missing
version control immediately.

Teams should add experiment tracking and model registries when they remove a
concrete delivery risk. The same applies to serving, monitoring, package
registries, and containers.

## Data Boundaries and Governance

Reproducibility can conflict with privacy, cost, and governance. Bayer's
neuroimaging example shows why this matters for research in
[Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }}).
At 42:22-44:12, she says sensitive consortium data can't simply be pushed to a
repository. Model parameters and metadata may still be shareable.

Stiebellehner gives the platform version. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 44:05-46:32, he distinguishes tools that log a query or metadata from tools
that copy the full dataset artifact. Copying a 50 GB training dataset for every
run can create cost problems. It can also create GDPR deletion problems because
the team may need to find and remove one person's data across many duplicated
artifacts.

Albertsson makes a similar point about lakes. In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
at 23:29-24:38 and 1:06:01-1:08:06, raw dumps and history help teams reproduce
past states, but personal data requires separation and governance. Full
database dumps preserve more history than mutable tables, yet they also require
clear handling for GDPR and change capture.

## Capture Set

The episodes support a practical capture set rather than a universal tool
checklist.

- Code and workflow definitions, including reports, transformations, model
  code, infrastructure code, and orchestration dependencies
  ([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
  at 33:47-34:37 and
  [DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  at 1:04:18-1:06:01).
- Inputs or input references. Teams may use immutable raw data, versioned
  datasets, query metadata, or controlled-access data depending on privacy and
  scale
  ([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  at 44:05-46:32).
- Environment and dependency records, including package versions, Docker
  images, requirements files, and package registries
  ([DataOps and GitOps for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})
  at 1:01:27-1:01:43 and
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  at 53:08-56:50).
- Run metadata, experiment logs, parameters, metrics, and model registry
  entries
  ([Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
  at 39:27-43:11 and
  [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  at 29:41-30:58).
- Tests and checks, including data transformation tests, end-to-end tests,
  production data quality checks, and development regression checks
  ([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
  at 44:12-48:59 and
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  at 40:10-42:54).
- Governance and downstream artifacts, including model outputs,
  visualizations, catalogs, and data governance changes when those artifacts
  change together
  ([Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
  at 51:21-53:33).

Use the capture set only when it matches the risk. A tutorial project can use a
small, fully bundled dataset. A bank model, clinical dataset, or
customer-facing fraud decision may need stricter metadata and lineage. It may
also need stricter approval, deletion, and audit paths.

## Related Pages

These related pages cover the operating layers around reproducibility.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Data Lake]({{ '/wiki/data-lake/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Testing]({{ '/wiki/testing/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
