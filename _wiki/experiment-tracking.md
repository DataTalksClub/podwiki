---
layout: wiki
title: "Experiment Tracking"
summary: "Experiment tracking as run history, reproducibility practice, and ML platform capability."
related:
  - MLOps
  - ML Platforms
  - MLOps Tools
  - Model Registry
  - Model Monitoring
  - Reproducibility
  - Developer Experience
  - Governance
---

Experiment tracking records machine-learning and AI model development runs. The
record helps a team compare results, understand how a model was produced, and
recover the context behind a promising or failed experiment. A tracked run
usually includes code version, parameters, metrics, and artifacts. It can also
include environment details, data references, and notes about the modeling
decision.

Guests place experiment tracking between exploratory
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) work and
production [MLOps]({{ '/wiki/mlops/' | relative_url }}). It isn't the same as a
[model registry]({{ '/wiki/model-registry/' | relative_url }}), but the two
often appear together because a useful run eventually needs an artifact handoff
path. [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
puts experiment trackers before registries, serving, orchestration, and
governance in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-31:51.

Experiment tracking for ML and AI work centers on run capture and
reproducibility. It also preserves team memory and connects runs to the wider
platform. It doesn't cover general product
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}) or broader
[experimentation]({{ '/wiki/experimentation/' | relative_url }}). For adjacent
topics, use
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) for judging runs and
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for deployed
behavior. Use [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
for the wider recovery problem across code, data, environments, and outputs.

## Shared Run History

Guests describe experiment tracking as moving run history out of private
memory. It turns local notebooks and ad hoc spreadsheets into a shared record.
It also captures one-off terminal output that other people can look at later.
Simon gives the clearest platform definition in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:06. Teams that evaluate models with metrics need a transparent way
to compare runs and outputs.

That definition is practical rather than tool-branded. The tracker is useful
because it records enough context to compare experiments and reproduce later
work. In Simon's platform sequence, teams explore data and train models. They
evaluate runs, persist candidate artifacts in a
[model registry]({{ '/wiki/model-registry/' | relative_url }}), and choose batch
or online serving
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 21:03 and 29:41-31:51). That's why experiment tracking belongs with
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}), and
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
not only with notebook hygiene.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }}) adds
the operating definition in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 40:10-42:54. Exploration contains knowledge that can help later monitoring
and root-cause analysis. Teams shouldn't let original model work disappear on a
departed employee's laptop. At 42:54-44:46, he ties reproducibility to
traceability, data versioning, and legal context. Sector requirements determine
how heavy the practice must become.

## Adoption Timing

Guests mostly differ on when teams should add tracking. Simon starts early
because tracking gives teams a quick reproducibility and collaboration win
before the full release path
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:58).

Raphael starts from team pain points instead of a fixed tool sequence. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 48:41-50:04, he argues that the first MLOps move depends on the
organization. A team might start with CI/CD, deployment, monitoring, or another
visible bottleneck. It can then add experiment capture as part of the operating
system for ML.

[Johanna Bayer]({{ '/people/johannabayer/' | relative_url }}) gives the
research version in
[Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 39:27-43:50. Her stack includes Git, environments, and formatting. It also
includes versioning and MLflow. The project uses sensitive clinical data that
can't simply be pushed to a repository. In that setting, metadata, parameters,
and project structure may be shareable even when raw data isn't.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) draws
an ecosystem boundary. In
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
at 52:04, he describes Metaflow interoperating with experiment trackers such as
Weights & Biases and Comet. That matches Simon's warning about integration. The
hard work isn't naming a tracker. It's fitting the tracker into the data
science workflow and the surrounding platform
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 34:01-35:14).

## Run Records

Simon and Raphael support a compact run record rather than a generic dashboard
wishlist. A useful tracked run preserves enough model-development context for a
teammate or future maintainer to understand what happened. Simon names job
images, consumed inputs, and written outputs. He also names persistent metadata
and connected pipeline runs
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 42:48-43:28).

Raphael adds the exploratory context that often gets lost when teams clean up
code for deployment. Visualizations, data checks, and early analysis can help
with later monitoring and root-cause work. Teams still need to separate
exploratory notebooks from production code
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 40:10-42:54). That links experiment tracking to
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}):
the system is valuable only if data scientists can use it without bypassing it.

## Data and Governance

Experiment tracking needs data context, but no universal storage rule.

Some tools log only a query or pointer, while others copy the data artifact.
Simon covers this in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 44:05-45:50.

He also warns against copying datasets for every run because the cost can grow.
Personal-data deletion can become harder too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 45:50-46:32).

Johanna reaches the same boundary from academic open science. Her neuroimaging
work uses sensitive consortium data, so the reproducible record has to respect
access controls. Parameters, metadata, and project structure can travel more
easily than raw clinical data
([Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 37:01 and 42:22-43:50). For navigation, this puts experiment tracking near
[Governance]({{ '/wiki/governance/' | relative_url }}),
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

## From Experiments to Production

Experiment tracking is most useful before a model is promoted. It becomes more
valuable when connected to the production path. Simon explicitly links
experiment trackers, model registries, and metadata stores
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 30:32-30:58). Later in the same episode, he connects stored metadata and
code versions to reproducing an old model result. Data versions and process
design matter too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 42:48-43:28).

Raphael places experiment tracking inside broader MLOps tooling, near version
control and CI/CD. It also sits near containers, registries, serving, and
monitoring
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 51:21-53:08). [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
makes a related standardization point in
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
at 18:41-24:01.

In Maria's discussion, version control and CI/CD appear as maturity signals.
Registries and documentation do too, along with reproducibility and
traceability. Tracking doesn't replace testing or packaging. It doesn't replace
deployment or [production]({{ '/wiki/production/' | relative_url }}) monitoring
either, but it gives those later steps a recoverable model-history record.

## Tool Choice and Integration

Guests name tools such as MLflow, Weights & Biases, and Comet. They also name
Neptune and SageMaker. Simon doesn't recommend choosing an experiment tracker
by brand alone.
Simon argues that most teams should integrate an existing tracker rather than
build one from scratch. Teams have to fit the tracker to the data science
workflow, data constraints, and surrounding infrastructure
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 34:01-35:14).

Hugo's Metaflow discussion makes the same point from an ML ecosystem focus.
Workflow tools, compute backends, and experiment trackers need to interoperate.
That lets practitioners move from local work to reproducible runs. They don't
have to change every habit in one step
([DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
at 13:52, 36:27, and 52:04).

Teams therefore need to ask what record they need, not which tracker is
fashionable. That record should connect to code and data. It should also
connect to artifacts, serving, monitoring, and governance.

## Related Pages

These pages cover the surrounding lifecycle, platform, and operating decisions.

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) - operational practices around reproducible training, deployment, monitoring, and ownership.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) - shared infrastructure for tracking, registries, serving, and governance.
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) - the surrounding tool categories for tracking, registries, orchestration, monitoring, and deployment.
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) - the artifact handoff after a tracked run becomes a candidate.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) - production feedback that depends on model versions and run context.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) - recoverable code, data, environments, and outputs.
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) - adoption of the tracking workflow by data scientists and ML engineers.
- [Governance]({{ '/wiki/governance/' | relative_url }}) - audit, lineage, retention, and compliance boundaries.
