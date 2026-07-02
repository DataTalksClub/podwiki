---
layout: article
tags: ["roadmap"]
title: "Lean MLOps for Startups"
keyword: "lean mlops for startups"
summary: "A startup-stage roadmap for lean MLOps: SaaS-first choices, portable foundations, manual controls, versioning, evaluation, monitoring, and the point where shared infrastructure starts to pay off."
search_intent: "People searching for lean mlops for startups want a practical build order for shipping ML with small teams, managed services, manual controls, basic monitoring, and a clear boundary before heavier ML platforms."
related_wiki:
  - Startups
  - MLOps
  - MLOps Roadmap
  - MLOps Tools
  - Machine Learning Infrastructure
  - ML Platforms
  - Model Registry
  - Experiment Tracking
  - Model Monitoring
  - Reproducibility
  - CI/CD
  - Data Quality and Observability
  - Platform Adoption
  - Data Strategy
  - Security
---

Lean MLOps for startups is the smallest operating system that lets a team ship
and observe an ML-backed product. It should also let the team change the
product without turning infrastructure into the product. Use it next to
[[Machine Learning for Startups]],
which starts from product discovery. Use the broader
[[MLOps Roadmap]] when you need the
full path from experiments to shared platforms. The startup version keeps
[[MLOps]] stage-aware because small teams
run short on money, time, and people
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 7:54-11:54]]).

Use this roadmap when a [[startups|startup]] or
[[startups|startup team]] already has a model or
data product idea and needs a production path. [[person:nemanjaradojkovic|Nemanja Radojkovic]]
argues that a small company should choose managed services and mature
components first. Then it can protect future flexibility with portable choices,
repeatable deployment, and observability. It should also keep technical debt
visible
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 11:54-21:35 and 40:01-49:00]]).

## First Principles

Start from the product constraint, not from the MLOps landscape. A startup
doesn't need every tool in the
[[MLOps Tools]] map before customers
can use the product. It needs enough
[[machine learning infrastructure]]
to run the first useful product path. Nemanja describes a two-month push around
dashboards, an industrialized API, and launch readiness. He then warns against
trying twenty tools when a proven choice will move the product forward
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 17:38-18:29]]).

Treat every tool choice as a tradeoff among speed, portability, and
maintenance. A managed service can save a four-to-ten-person company from
hiring dedicated infrastructure staff. Cloud and SaaS choices still add
identity, key management, and configuration work. They also add migration and
billing decisions.

Nemanja's startup advice isn't "avoid infrastructure." It's "buy the parts that
save scarce attention, then keep the core workflow understandable enough to
move later"
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 11:54-16:25]]).

## Stage 1: Choose SaaS Before You Build

Start with a SaaS-first MVP stack. Use a hosted database and managed cloud
compute when those choices let the team learn faster. Add a simple serving
target when the product needs it. Add hosted or lightweight observability when
the team needs to debug real use.

Nemanja explicitly recommends vendor solutions for small teams. Server, BI, and
platform maintenance can consume the people who should be shipping the product
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 11:54]]).

Use cloud credits carefully because credits can make a cloud provider feel free
during the first year. The real cost appears when the team has to migrate, rewrite
service-specific workflows, or keep paying for a platform it no longer likes.
Cloud selection belongs with
[[data strategy]] and
[[security]], not just hosting
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 12:54-15:06]]).

Pick boring defaults where they remove debate:

- PostgreSQL
- Python
- Git
- simple APIs
- container images
- a mature scheduler

These choices are usually easier to change later than a full proprietary ML
platform. Nemanja contrasts generic scripts on a remote server with richer
managed ML platforms such as Vertex AI or SageMaker. The richer platform may
accelerate a narrow workflow. It can also make migration and retraining harder
if reproducibility was weak
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 18:29-21:35]]).

## Stage 2: Keep Portable Foundations

Keep the portable foundation small:

- version-controlled code
- reproducible dependencies
- a documented data reference
- a repeatable deployment command
- logs from the running system

This is the startup version of
[[reproducibility]]. It doesn't
require a custom platform, but it does require enough discipline for another
person to rebuild the environment and understand which model reached production.
Nemanja raises that concern when asking whether models trained inside vendor
platforms can be reproduced after migration
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 20:17]]).

Avoid console-only configuration when the setting is important to the product.
Manual cloud clicks may be reasonable during a launch crunch. Once the setting
becomes part of the operating path, record what changed or move it into
infrastructure as code. Nemanja describes cloud identity, key management, and
hand-configured services as a replication risk. Six months later, the team may
not remember how production was assembled
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 15:06-16:25]]).

Keep low-code and one-click ML deployment as a deliberate shortcut, not as an
unexamined foundation. Low-code can help when a startup has only a data
scientist and no software or systems engineer. The tradeoff is future
flexibility. Nemanja accepts that some startups will choose speed first. He
still prefers generic, portable components when the team can afford them
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 21:35]]).

## Stage 3: Add Manual Controls Where They Pay

Lean MLOps doesn't mean full automation. Early teams can use manual approvals,
checklists, and tactical conventions when those controls make releases safer
without blocking customer learning.

In the finance episode, Nemanja names the minimum operating pieces:

- dev, test, and production environments
- a central DevOps trail
- monitoring
- a model registry
- data versioning
- reproducible pipelines

The startup roadmap should borrow the control idea, then keep the
implementation lighter
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 31:57-35:57]]).

A model registry can start as a convention before it becomes a platform. For a
single model, record the object-store folder, artifact name, and code commit.
Add the training-data reference, metrics file, owner, and deployment note.
Nemanja uses an S3 bucket as an example of a tactical registry and
data-versioning solution. It isn't the strategic end state, but it's enough to
show which artifact is being used and how it was produced
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 35:57-37:51]]).

A startup doesn't need a large release-management department for
[[ci-cd|CI/CD]]. It does need a repeatable path
from code and model artifact to production. Nemanja's minimal startup stack
starts with Python and CI/CD-driven orchestration. Tools such as Dagster or
MLflow fit when they solve an immediate orchestration or tracking problem
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 44:10-45:39]]).

## Stage 4: Version, Evaluate, and Monitor the Basics

Version the parts that explain a production prediction:

- code
- data reference
- model artifact
- parameters
- metrics
- deployment target

For early teams,
[[experiment tracking]] can
start with MLflow or a hosted tool. A disciplined artifact-and-metadata folder
can also work. The requirement isn't tool purity. The team needs to compare
runs. It also needs to recover why a model changed before customers experience
the change
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 44:10-48:11]],
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 31:57-35:57]]).

Evaluate with the smallest set of checks that can block a bad release. Keep the
offline metric, a baseline comparison, and a data-quality check. Add one
product or business signal when labels or outcomes exist.

Raphaël Hoogvliets's scale-up advice supports this order. Standardize CI,
repository structure, parameterization, and tests before adding heavier
governance. Prioritize data-transformation tests because preprocessing and
post-processing failures often become production failures
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 39:06-44:46]]).

Monitor what the customer or internal user will notice first. A startup may
start with application errors, latency, stale jobs, and missing inputs. Add
prediction distributions and simple data-quality checks before a full
[[model monitoring]] platform.
Nemanja's startup choices include Logfire, Prometheus/Grafana, and Streamlit. A
tool working in an hour can beat a more mature stack the team can't operate yet
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 45:55-48:11]]).

## Stage 5: Manage Debt Before It Becomes the Architecture

Startup teams can take shortcuts, but they should name the shortcut and owner.
They should also name the risk and repayment trigger. Nemanja frames technical
debt as acceptable only when someone understands the risk and leaves notes. He
also warns that security holes or data leaks can destroy the company. Debt
tracking belongs in lean
[[production]] work, not in a cleanup
phase after product-market fit
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 37:54-42:12]]).

Use AI-assisted coding with review. One person can now touch infrastructure,
pipelines, web code, and deployment scripts faster than they can deeply
understand each layer. Nemanja's warning is practical: code that works today
can become a maintenance problem later. In a startup, pair that speed with code
review, ownership notes, and secrets hygiene. Revisit debt before it hardens
into the default architecture
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 37:54-41:55]]).

Keep senior judgment close to high-risk shortcuts. Nemanja cautions that a
junior practitioner shouldn't be the only data scientist in a startup. Missing
experience may hide security, maintainability, and modeling risks. A lean stack
still needs mentorship or pairing when the model touches valuable data. It also
needs an experienced reviewer for customer-facing decisions
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 34:32-35:09 and 40:57-43:25]]).

## Stage 6: Introduce Shared Infrastructure After Repetition

Move from lean conventions to shared infrastructure when projects repeat the
same deployment, tracking, monitoring, or support work. A startup with one
model can live with a tactical registry and a simple deployment path.

A startup with multiple model builders should start standardizing repositories
and templates. It should also standardize orchestration and artifact promotion.
Add observability standards when multiple services create recurring support
work. Do the same when customer incidents repeat.

Nemanja describes this framework idea as useful when similar projects repeat
over two or three years. Raphaël describes the scale-up version as an enabling
MLOps team that helps product teams deploy models. It also helps them maintain
and monitor those models
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 33:00-34:00]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 23:01-25:20]]).

Use [[platform adoption]] rules
before introducing a heavier [[ml-platforms|ML platform]].

Raphaël recommends treating the platform like an internal product:

- collect pain points
- choose quick wins where platform priorities and user pain overlap
- show a before-and-after improvement in deployment time or risk

For a startup, platform work is justified when it removes repeated friction
from product work. A missing box in the stack diagram isn't enough
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 27:56-38:46]]).

Add heavier pieces in the order the pain appears:

- If releases are slow, start with CI/CD and templates.
- If runs can't be compared, add experiment tracking.
- If no one knows which artifact is live, harden the [[model registry]].
- If customers see stale outputs, improve [[data quality and observability]].

Raphaël gives the general rule. Start from the most important organizational
problem, use tools already available, and flag missing basics such as version
control early
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 48:41-52:39]]).

## Finance and Scale-Up Contrast

Finance teams move governance earlier. In
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]],
Nemanja describes release management, approvals, and test evidence. He also
describes rollback procedures, package controls, and a clear production record.

Those controls slow delivery, but they create trust and auditability. They
matter when model changes must fit existing
[[governance]] and DevOps processes
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 21:21-27:36]]).

Scale-up MLOps moves adoption and shared-team design earlier. In
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
[[person:raphaelhoogvliets|Raphaël Hoogvliets]]
describes centralized MLOps as an enabling team. The team works with product
teams and ML engineers. It owns developer experience and deployment support. It
also owns maintenance, monitoring, and adoption metrics.

A five-person startup faces a different constraint. It first needs to ship and
observe one product path without owning a platform
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 23:01-36:55]]).

The lean startup path sits between those two. It borrows finance's respect for
traceability and rollback, but it avoids finance-level approval machinery until
risk or regulation demands it. It borrows scale-up MLOps practices such as CI
and repo structure. It also borrows testing, monitoring, and reproducibility.

It delays centralized platform work until repeated projects or repeated pain
justify the investment
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 31:57-37:51]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 39:06-56:50]]).

## The Roadmap Checkpoint

A startup is ready to leave the lean stage when production evidence answers
five checks:

- which model version is live
- which code, data reference, and metric produced it
- how the team deploys it
- which signal shows that it's broken or stale
- which shortcut will block the next migration, customer, or compliance need

Nemanja's startup and finance discussions both make the same control point
visible. A simple end-to-end process is better than a sophisticated partial
stack
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 40:01-49:00]],
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 31:57-37:51]]).

After that checkpoint, choose the next constraint deliberately. For a product
startup, continue with
[[Machine Learning for Startups]]
and [[Data Strategy]].

For platform depth, move into
[[MLOps Architecture]],
[[MLOps Roadmap]], and
[[ML Platforms]]. For sensitive data,
bring in
[[Privacy Engineering for ML]],
[[Security]], and
[[Governance]]. Do that before a
shortcut becomes customer-facing risk
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups, 41:03-42:12 and 57:09]],
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance, 21:21-23:39]]).

