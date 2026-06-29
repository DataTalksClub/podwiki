---
layout: wiki
title: "Software Engineering"
summary: "A bridge page for podcast evidence about applying software engineering discipline to data, ML, and AI systems."
related:
  - Machine Learning System Design
  - MLOps and DataOps
  - Production
  - Practices
---

## Definition and Scope

Software engineering in this archive means the engineering discipline that makes
data, ML, and AI systems understandable. It also makes them testable,
deployable, maintainable, and owned. The archive connects this to requirements,
modular design, version control, and CI/CD. It also connects it to tests,
documentation, interfaces, logging, deployment paths, and collaboration across
teams.

This isn't a general software engineering textbook page. It collects podcast
evidence where engineering practice changes the outcome of data or ML work. For
ML-specific design decisions, use
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
For operational lifecycle work, use
[MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}).

## Recurring Archive Themes

The archive connects software engineering to data and ML reliability in several
ways:

- The software-engineering-for-ML episode distinguishes ML products through
  uncertain model behavior and data workflows. It also names monitoring needs
  and hidden technical debt.
- Guests trace failures back to weak requirements and unrealistic expectations.
  Missing data access, unclear business buy-in, and unusable outputs also show
  up as failure causes.
- Production ML and DataOps guests push teams to move logic out of notebooks
  and scripts. Packages, pipelines, tests, CI/CD, and documented workflows lower
  operational risk.
- Data products, model APIs, prediction schemas, and data contracts are
  interfaces. Feature pipelines, semantic layers, and BI models are interfaces
  too. Weak interfaces create downstream breakage.
- Model cards, datasheets, factsheets, and design docs preserve operational
  memory. Checklists, README files, and runbooks preserve decisions, owners,
  assumptions, limitations, and recovery paths.

## Episode Evidence

These episodes give the most direct evidence:

- [Software Engineering for Machine Learning](https://datatalks.club/podcast.html):
  hidden technical debt, uncertainty, data workflows, and monitoring. It also
  covers requirements alignment, team structures, documentation practices,
  responsible AI, and involving ML practitioners from requirements through
  testing.
- [Practical Machine Learning Engineering for Production](https://datatalks.club/podcast.html):
  refactoring monolithic code into modular components. It also covers avoiding
  search-driven complexity, using simpler baselines, timeboxing experiments, and
  building maintainable systems.
- [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html):
  documentation, reproducibility, code quality, and testing. It adds Git,
  CI/CD, registries, standardized repositories, packages, and pipelines.
- [DataOps for Data Engineering](https://datatalks.club/podcast.html):
  deployment automation, regression tests, CI/CD, and test data. It also covers
  version control, on-call readiness, and production monitoring.
- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  software engineering fundamentals, API schemas, logging, and orchestration. It
  also covers lineage, governance, and developer experience.
- [Open Source ML Contributions](https://datatalks.club/podcast.html):
  reproducible issues, tests, CI, and packaging. It also covers pre-commit,
  documentation, contribution guides, and maintainership.

## Related Pages

Useful adjacent pages:

- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Practices]({{ '/wiki/practices/' | relative_url }})
- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})

## Maintenance Notes

Future additions should stay tied to engineering discipline:

- Add evidence here when a guest discusses engineering practices that improve
  maintainability or reliability across data and ML work. Good examples include
  requirements, modularity, tests, CI/CD, and documentation. APIs, version
  control, reviews, packaging, logging, and team integration also fit.
- Don't turn this page into a generic career or computer science page. Keep it
  tied to archive evidence about data, ML, AI, and production systems.
