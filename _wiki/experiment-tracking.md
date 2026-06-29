---
layout: wiki
title: "Experiment Tracking"
summary: "A bridge page for podcast evidence about capturing model runs, parameters, metrics, artifacts, data references, and exploratory knowledge for reproducible ML work."
related:
  - MLOps
  - ML Platforms
  - Model Registry
  - Reproducibility
---

## Definition and Scope

Experiment tracking records what happened during model development. Teams
capture code versions, parameters, metrics, and data references. They may also
capture artifacts, notes, and environment details. In the archive, teams use
tracking to stop losing knowledge in notebooks, spreadsheets, and personal
machines.

Use this page for run capture and reproducibility before a model is promoted.
Use [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) for model
artifact handoff after a run becomes a candidate for deployment.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive treats experiment tracking as an early MLOps habit:

- Tracking is an early reproducibility win. Simon Stiebellehner says even a
  single model or a small team can benefit because the team stops moving from
  spreadsheet notes to lost run history.
- Tracking connects exploration to production. Raphaël Hoogvliets warns that
  exploratory work can disappear when notebooks stay on desktops or get
  commented out. Keeping the useful parts helps later root cause analysis.
- Data references matter as much as metrics. Guests connect reproducibility to
  code, parameters, data versions, and traceability. Job images and artifacts
  also matter.
- Tool choice is secondary to capture discipline. The archive names MLflow,
  Weights & Biases, Neptune, Comet, and SageMaker. The main point is whether
  teams can recover what produced a model.
- Tracking creates governance questions when teams log full datasets,
  especially under privacy rules such as GDPR.

## Episode Evidence

These episodes connect tracking to reproducibility:

- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 29:41, Simon frames experiment tracking as an early win for
  reproducibility and collaboration. At 42:48-45:50, he connects run metadata
  to job images, inputs, outputs, and code versions. He also covers data
  references, artifact logging, and governance tradeoffs. Reuse the
  [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 39:06-44:22,
  Raphaël covers CI, repository structure, parameterization, and testing. The
  same section covers exploratory knowledge, data versioning, traceability, and
  experiment capture.
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

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/devrel-open-source-machine-learning.md`
- `../datatalksclub.github.io/_podcast/teaching-reproducible-research-and-open-science-coding-practices-for-academia.md`

Keep this page about experiment capture. Put artifact promotion and lifecycle
state on [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) and
production behavior on [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).
