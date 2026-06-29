---
layout: wiki
title: "Experiment Tracking"
summary: "A bridge page for podcast evidence about capturing model runs for reproducible ML work."
related:
  - MLOps
  - ML Platforms
  - Model Registry
  - Reproducibility
---

## Definition and Scope

Experiment tracking records what happened during model development by capturing
code versions, parameters and metrics. Teams also capture data references,
artifacts and notes. In the archive, teams use tracking to stop losing knowledge
in notebooks, spreadsheets and personal machines.

Use this page for run capture and reproducibility before a model is promoted.
Use [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) for model
artifact handoff after a run becomes a candidate for deployment.


## Recurring Archive Themes

The archive treats experiment tracking as an early MLOps habit:

- Tracking is an early reproducibility win. Simon Stiebellehner says even a
  single model or a small team can benefit because the team stops moving from
  spreadsheet notes to lost run history.
- Tracking connects exploration to production. Raphaël Hoogvliets warns that
  exploratory work can disappear when notebooks stay on desktops or get
  commented out. Keeping the useful parts helps later root cause analysis.
- Data references matter as much as metrics. Guests connect reproducibility to
  code, parameters and data versions, while job images, artifacts and
  traceability also matter.
- Tool choice is secondary to capture discipline. The archive names MLflow,
  Weights & Biases and SageMaker, but teams still need to recover what produced
  a model.
- Tracking creates governance questions when teams log full datasets,
  especially under privacy rules such as GDPR.

## Episode Evidence

These episodes connect tracking to reproducibility:

- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 29:41, Simon frames experiment tracking as an early win for
  reproducibility and collaboration. At 42:48-45:50, he connects run metadata
  to job images and code versions. He also covers inputs, outputs, data
  references and governance tradeoffs. Reuse the
  [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 39:06-44:22,
  Raphaël covers CI, repository structure and testing. He also covers
  exploratory knowledge, data versioning, traceability and experiment capture.
  At 51:21, tracking appears in the core MLOps toolset. Reuse the
  [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [DevRel Role for Machine Learning](https://datatalks.club/podcast.html):
  Hugo discusses reproducible workflows and education around full-stack ML
  tools. This is useful when tracking is part of developer onboarding or demos.
  Reuse the [summary]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
- [Teaching Reproducible Research](https://datatalks.club/podcast.html):
  Add reproducible research evidence here when it includes code, data,
  environment, or notebook practices that transfer to ML experiments.

## Related Pages

Use these pages for adjacent reproducibility and lifecycle topics.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
