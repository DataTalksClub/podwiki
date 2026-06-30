---
layout: wiki
title: "Experiment Tracking"
summary: "Podcast-grounded reference page for experiment tracking as run history, reproducibility practice, and ML platform capability."
related:
  - MLOps
  - ML Platforms
  - Model Registry
  - Model Monitoring
  - Reproducibility
  - Developer Experience
  - Governance
---

Experiment tracking records model-development runs. The record usually includes
run code, parameters, metrics, and artifacts. It can also capture environment
details, data references, and notes.

In the DataTalks.Club archive it sits between exploratory
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) work and
production [MLOps]({{ '/wiki/mlops/' | relative_url }}). It isn't the same as a
[model registry]({{ '/wiki/model-registry/' | relative_url }}). The two are
often packaged together because a promising run eventually needs an artifact
handoff path
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:58).

The archive's practical definition is narrower than "all experimentation."
This topic covers run capture, reproducibility, and team memory during model
development. Use [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
for promoted artifacts, [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
for deployed behavior, and [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
for the metrics and decision criteria used to judge the run.

## Link Map

These wiki pages cover the closest neighboring topics:

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) and [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) and [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) and [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}), [Governance]({{ '/wiki/governance/' | relative_url }}), and [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

These podcast interviews anchor the page:

- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
  anchors the platform view. He places experiment tracking before registries,
  serving, and governance work.
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  with [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
  anchors the operating view. He connects experiment capture with CI,
  repository structure, testing, and traceability.
- [Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
  with [Johanna Bayer]({{ '/people/johannabayer/' | relative_url }})
  shows the research version. Her discussion includes MLflow, project setup,
  Git, and sensitive-data limits.
- [DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
  with [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
  connects experiment trackers such as Weights & Biases and Comet to
  interoperable ML tooling and developer education.

## Common Definition

Across the archive, experiment tracking moves run history out of private memory.
It turns local notebooks and spreadsheets into a shared record.
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
gives the cleanest definition in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:06. He says teams that evaluate models with metrics benefit from a
tracker because the run record becomes shared and transparent.

The same episode places tracking inside an ML platform lifecycle. Teams explore
data, train models, evaluate runs, and persist candidates in a
[model registry]({{ '/wiki/model-registry/' | relative_url }}). Then they
decide on batch or online serving
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-31:51). That sequence is why experiment tracking belongs near
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}), not only near
notebook hygiene.

[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
adds the reproducibility layer in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 40:10-42:54. He argues that exploration contains knowledge useful for later
monitoring and root-cause analysis. He also argues that teams shouldn't let
original exploration vanish on a departed employee's desktop. At 42:54-44:46,
he ties reproducibility to traceability plus data versioning. Sector and legal
obligations affect when a team needs the heavier version of that practice.

## Guest Differences

Guests differ mostly on entry point. Simon Stiebellehner treats tracking as an
early platform component because it gives teams reproducibility benefits
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 29:41-30:58).

Raphael Hoogvliets starts from team pain points. In his view, the first MLOps
move depends on the organization. A team may start with monitoring, deployment
work, or CI/CD
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 48:41-50:04).

They also draw the data boundary differently. Simon compares tools that log a
query or pointer with tools that copy the whole data artifact. He then warns
about cost and GDPR deletion problems
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 44:05-46:32).

Johanna Bayer gives the research version in
[Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 39:27-43:50. She uses Git and MLflow. She also uses environments and
formatting.
Sensitive clinical data can't simply be pushed to a repository, so metadata and
parameters may be shareable when raw data isn't.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
adds a tool-ecosystem boundary rather than a governance one.
In [DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
at 52:04 he describes Metaflow interoperating with experiment trackers such as
Weights & Biases and Comet. This differs from Simon's platform-integration
warning, but both support the same practical requirement. The tracker must fit
the team's workflow and surrounding tools.

## Run Record

The podcast evidence supports a compact run record rather than a generic
dashboard wishlist. A useful tracked run should preserve the model-development
context. Simon names job images and consumed inputs. He also names written
outputs, persistent metadata, and connected pipeline runs
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 42:48-43:28).

Raphael's episode adds exploratory context. Visualizations and data checks can
help later monitoring and root-cause work. Teams should separate exploratory
work from deployment code without discarding useful exploration
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 40:10-42:54). That links experiment tracking to
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}).
The tracker is valuable when it captures context without forcing data
scientists into a workflow they'll bypass.

## Data References and Governance

The archive treats data references as part of experiment tracking. It doesn't
turn them into one universal storage rule. Simon explains that some tools store
metadata around the query used to fetch data. Others log the full dataset
artifact
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 44:05-45:50).

He then warns that copying datasets for every training run can
be expensive. It can also create deletion problems when personal data is involved
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 45:50-46:32).

Johanna's academic example reaches the same boundary from a different direction.
Her neuroimaging work uses sensitive consortium data. The project can share
model parameters or metadata more easily than raw data
([Teaching Open Science and Reproducible Research]({{ '/podcasts/teaching-reproducible-research-and-open-science-coding-practices-for-academia/' | relative_url }})
at 42:22-43:50).

For wiki navigation, that puts experiment tracking next to
[Governance]({{ '/wiki/governance/' | relative_url }}),
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}), and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

## From Runs to Production

Experiment tracking is useful before a model is promoted. It becomes more
valuable when connected to the production path. Simon explicitly links
experiment trackers, model registries, and metadata stores
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 30:32-30:58). He later connects stored metadata and model registry contents
to reproducibility. Code versions, data versions, and process design matter
when a team needs to reproduce an old model result
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 42:48-43:28).

Raphael places experiment tracking inside a broader MLOps toolbelt
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
at 51:21-53:08).

In that list, tracking sits next to:

- version control and CI/CD
- containers and registries
- monitoring and serving

That makes experiment tracking one component of
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
It doesn't replace testing, packaging, deployment, or
[production]({{ '/wiki/production/' | relative_url }}) monitoring.

## Tool Choice

The archive names tools such as MLflow and Weights & Biases. Comet, Neptune,
and SageMaker appear in the same tool discussions. It doesn't support choosing a
tracker by brand alone. Simon says most teams should integrate an existing
tracker rather than build one from scratch.
The hard work is fitting it to the data science workflow and surrounding
constraints
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
at 34:01-35:14).

Hugo's Metaflow discussion makes the same integration point from an ecosystem
view. He describes interoperability with experiment trackers such as Weights &
Biases and Comet
([DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
at 52:04).

## Related Pages

These pages cover adjacent lifecycle and operating decisions.

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) - reproducible training, deployment, monitoring, and ownership.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) - shared tracking, registries, serving, and governance.
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) - tracking, registries, orchestration, monitoring, and deployment tools.
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) - artifact handoff after a tracked run becomes a candidate.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) - production feedback that uses model versions and run context.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) - recoverable code, data, environments, and outputs.
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) - adoption of the tracking workflow by teams.
- [Governance]({{ '/wiki/governance/' | relative_url }}) - audit, lineage, retention, and compliance boundaries.
