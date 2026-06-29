---
layout: wiki
title: "Practices"
summary: "A bridge page for recurring operating practices in the podcast archive: versioning, testing, documentation, CI/CD, monitoring, ownership, and feedback loops."
related:
  - MLOps and DataOps
  - Software Engineering
  - DataOps
  - Production
---

## Definition and Scope

Practices are the repeatable habits teams use to make data, ML, and AI work
reliable. In this archive, the recurring habits are version control, tests,
CI/CD, documentation, and code review. Monitoring, runbooks, ownership,
stakeholder feedback, and incremental delivery also recur.

Many archive pages link to "practices" as a topic slug. This bridge doesn't
replace the larger
[MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}) or
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
hubs. Instead, it indexes the cross-cutting habits that appear across MLOps,
DataOps, analytics engineering, and open source. Production AI and system design
episodes add more examples.

## Recurring Archive Themes

The archive repeats these habits across production operations topics:

- Guests warn against heavy process before value is proven. Teams validate the
  business case first. They add standards when risk justifies them.
- Version control applies to code, SQL transformations, model artifacts, and
  configurations. It also applies to documentation, productized notebooks, and
  sometimes full analytical environments.
- The archive includes unit tests, regression tests, integration tests, and SQL
  tests. It also includes data quality checks, snapshot tests, A/A tests, prompt
  evaluations, model validation, and monitoring thresholds.
- CI/CD, pipeline orchestration, reproducible environments, and package
  registries reduce manual release risk. Containers and deployment automation
  do the same.
- Design docs, model cards, datasheets, and factsheets preserve decisions.
  READMEs, contribution guides, runbooks, tracking plans, and wiki pages
  preserve owners, caveats, and recovery steps.
- Stakeholder feedback, developer experience, product metrics, and user
  complaints route work back to teams. Incident reviews, quick wins, and
  ownership models route problems to the right owner.

## Episode Evidence

These episodes give the most direct evidence:

- [DataOps for Data Engineering](https://datatalks.club/podcast.html):
  automation, observability, CI/CD, and regression tests. It also covers test
  data, deployment automation, data versioning, on-call readiness, and practical
  starting steps.
- [MLOps at Scale](https://datatalks.club/podcast.html): CI, repository
  structure, parameterization, and testing. It also covers data versioning,
  traceability, experiment capture, dependency management, monitoring, quick
  wins, and adoption feedback.
- [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html):
  reusable CI/CD, standardized repositories, registries, and model deployment.
  It also covers monitoring, maturity assessment, documentation,
  reproducibility, and moving notebook logic into packages.
- [Software Engineering for Machine Learning](https://datatalks.club/podcast.html):
  requirements alignment, shared vocabulary, documentation standards, and Model
  Cards. It also covers Datasheets, factsheets, checklists, team integration,
  and testing involvement.
- [Production AI Engineering](https://datatalks.club/podcast.html): snapshot
  and integration testing for data pipelines. It also covers Great
  Expectations, SQL tests, prompt evaluation, prompt compression, caching, and
  practical tool choice.
- [Open Source ML Contributions](https://datatalks.club/podcast.html):
  reproducible issues, tests, CI, and packaging. It also covers pre-commit
  hooks, documentation, contribution guides, examples, and maintainership
  habits.
- [Product Analytics and A/B Testing](https://datatalks.club/podcast.html):
  A/A tests, traffic assignment, power analysis, and metric selection. It also
  covers experiment monitoring and causal validation practices.

## Related Pages

Useful adjacent pages:

- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})

## Maintenance Notes

Future additions should name the reusable habit:

- Add evidence here when an episode contributes a reusable habit rather than a
  tool mention. Good examples include a testing approach, deployment workflow,
  documentation structure, or monitoring workflow. Incident practice, review
  practice, and feedback mechanisms also fit.
- Prefer specific pages for domain details. Use this page for cross-cutting
  practices that recur across several areas.
- Avoid turning the page into a list of slogans. Each addition should identify
  the practice, the failure mode it addresses, and the episode evidence.
