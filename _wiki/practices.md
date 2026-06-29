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

Practices are the repeatable engineering habits that keep technical work usable
after the first demo. In the DataTalks.Club podcast archive, this covers
version control and testing. It also covers CI/CD, documentation, monitoring,
and ownership. Feedback loops are part of the same practice layer.

These habits appear in [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). They also appear in
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[open source]({{ '/wiki/open-source/' | relative_url }}).

The interviews define practices as the operating system around technical work.
They're not one tool, and they aren't one process document.
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) frames
DataOps practice around three goals in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
Teams reduce errors, shorten deployment cycles, and improve productivity.

[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) gives the
same structure for MLOps in
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).
Teams need reusable CI/CD, standard repositories, and clear deployment paths.
Registries and monitoring matter too before model delivery can scale.

## Common Definition

Across the archive, a practice is useful when it has these properties:

- It's repeatable, so a team can run it again without relying on memory.
- It's visible, so other people can review the decision, artifact, or failure.
- It changes behavior, so it's more than a policy written after the fact.

That definition connects several episodes. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes CI, repository structure, and parameterization. Testing sits in the
same bundle. He also connects data versioning and traceability to the work of
keeping models deployed. Experiment capture serves the same purpose.

In
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}),
[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) adds shared
vocabulary, requirements alignment, and documentation. She also covers Model
Cards, Datasheets, and checklists because ML systems fail through organizational
ambiguity as well as code defects.

## Guest Differences

The guests differ most on timing and scope. Bergh argues for an automation-first
DataOps view where version control, tests, and CI/CD cover the data workflow.
Runbooks, observability, and environment management should cover the same flow
from data to model to visualization.

Vechtomova is more pragmatic about adoption. In her MLOps episode, the starting
point is often existing infrastructure. Git, Kubernetes, and CI/CD come before
specialized platform pieces. Object storage and package registries are part of
that foundation too.

Hoogvliets emphasizes developer experience and trust. His MLOps team starts
with pain points and quick wins before standardizing too much. Adoption feedback
and deployment metrics guide the next step.

Nahar emphasizes the socio-technical side. Requirements, team integration, and
documentation matter because ML products cross several boundaries.
Accountability matters for the same reason. The archive doesn't give one
maturity ladder. It gives a consistent rule: introduce the practice when it
removes real delivery risk.

## Version Control and Reproducibility

Version control is the baseline practice. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
Bergh treats version control as part of the seven practical steps for healthier
data pipelines. Later in the same episode, he expands the scope beyond source
code, models, and visualizations. Governance and other production artifacts
need the same treatment.

The MLOps interviews add artifact and environment reproducibility. In
[Pragmatic MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
Vechtomova discusses model registries and artifact storage. She also covers
service principals and standardized repositories. Moving notebook logic into
packages is another part of that practice.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Hoogvliets ties reproducibility to data versioning and experiment capture. He
also covers traceability and dependency management. Package registries,
containers, and deployment records belong in the same operating model.

These practices overlap with
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
[MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}).

## Tests and Quality Gates

Testing practice changes by domain. Data pipelines need data quality checks,
snapshot tests, SQL tests, and integration tests.

In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) discusses
snapshot and integration testing for data pipelines. He compares Great
Expectations, Soda, SQL tests, and Spark tests. The same episode extends
testing into AI applications through prompt evaluation. It also covers prompt
compression trade-offs and caching decisions.

Product experiments need different gates. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) focuses on
randomization, traffic assignment, and A/A tests. He also connects reliable
experiments to metric stability, power analysis, statistical tests, and
monitoring. Those practices belong with
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }}), and
[Causal Inference]({{ '/wiki/causal-inference/' | relative_url }}) rather than
with generic software unit testing.

Open source projects expose another version of the same idea. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) connects
good issues and pull requests to reproducible examples and tests. CI and
packaging give maintainers a cleaner review path. Pre-commit hooks and
documentation serve the same goal. The practice is social as well as technical
because a maintainer can only help when the failure is easy to reproduce.

## CI/CD and Release Habits

CI/CD appears as a release-risk reducer across DataOps, MLOps, and open source.
Bergh links CI/CD to deployment cycle time and production reliability in the
DataOps episode. Vechtomova describes reusable CI/CD templates and standardized
repositories as central MLOps team responsibilities. Hoogvliets lists CI,
parameterized repositories, testing, and registries as core habits. Dependency
management and deployment frequency make model release less manual.

CI/CD isn't only a pipeline runner. Teams use it to encode quality gates and
packaging rules. Environment assumptions and handoff expectations belong there
too.

For model systems, those expectations connect to
[MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) work. For data
pipelines, they connect to [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
For open source, Warmerdam shows the same habit in contribution guides and
pre-commit hooks. Tests and packaging checks serve the same role.

## Documentation and Handoffs

Documentation is a practice when it changes how people hand off work.

In
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}),
Nahar connects documentation to shared vocabulary and expectation setting. She
also covers Model Cards and Datasheets. Factsheets, checklists, and responsible
AI accountability sit in the same family. Useful documentation keeps
requirements and data assumptions visible. It also keeps model behavior and
stakeholder expectations visible.

Bergh makes a similar argument from the operational side. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
runbooks become a bridge from manual checklists to automated playbooks, and
documentation reduces fragile handoffs and on-call load. Warmerdam's open source
episode shows the same principle for public projects.

README files and guides make a project easier to use. API references, examples,
and contribution guides make it easier to maintain. See also
[Documentation]({{ '/wiki/documentation/' | relative_url }}) and
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).

## Feedback Loops and Ownership

Practices need feedback loops or they turn into ceremony. Bergh separates
customer validation from data and model validity in DataOps. Hoogvliets uses
feedback loops inside MLOps adoption. His team collects pain points, delivers
quick wins, measures deployment frequency, and keeps platform work tied to
product-team needs. Vechtomova makes a similar point when she discusses
organizational buy-in and DevOps cooperation for standardized MLOps.

Ownership also differs by context. In DataOps, ownership spans pipelines and
recovery while also covering quality and environments. In MLOps, ownership
covers model release and monitoring. It also covers reproducibility and support
for product teams.

In experimentation, Graff keeps ownership close to metric design and assignment
tracking. Power analysis and interpretation stay with the same owner. These
differences matter for role pages such as
[MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) and for
comparison pages such as
[MLOps vs DataOps]({{ '/articles/mlops-vs-dataops/' | relative_url }}).

## Related Pages

These pages cover the adjacent concepts and comparisons:

- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Testing]({{ '/wiki/testing/' | relative_url }})
- [Documentation]({{ '/wiki/documentation/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
