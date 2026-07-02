---
layout: wiki
title: "Applied Research"
summary: "How DataTalks.Club guests describe applied research as hypothesis-driven work that turns uncertain ML ideas into products, reusable systems, and production-ready evidence."
related:
  - Machine Learning
  - Production
  - Machine Learning System Design
  - Academic Researcher to Data Science
  - Experimentation
  - MLOps
---

## Research for Practical Decisions

Teams do applied research when they aim research at a practical decision,
product, or system. DataTalks.Club guests use the term for work
that still has scientific uncertainty but must produce something a team can use.
That output may be a dataset, benchmark, or prototype. It may also be a
modeling approach, validation method, or production design.

The topic overlaps with [[machine learning]],
[[experimentation]], and
[[production]] because teams test more
than model accuracy. They aren't only reading papers or training models. They
also decide whether ideas can survive product constraints, engineering
constraints, and real users.

## Hypotheses, Benchmarks, and Reusable Evidence

In these interviews, applied research usually means hypothesis-driven technical
work with a use case attached. In
[[podcast:make-money-with-machine-learning-roles-skills|Monetize Machine Learning]],
[[person:vinvashishta|Vin Vashishta]] describes machine
learning research as artifact creation. Teams create datasets, run experiments,
study model behavior, and build knowledge that can support ML products. Around
the 36:10 chapter, he frames the research skill set around hypothesis design and
experimentation. He also includes explainability and iterative evidence
gathering.

[[person:mihaileric|Mihail Eric]] gives the matching
engineering version in
[[podcast:research-to-production-ml-systems-roadmap|From Research to Production]].
At 8:34 and 10:52, he connects research infrastructure with data collection and
prototyping. He also connects it with hypotheses and benchmarks. Eric's version
of applied research doesn't stop when a notebook works. Researchers continue
until they can turn the idea into a reproducible
[[machine-learning-system-design|ML system design]].

Teams use applied research to test an uncertain technical idea and turn what
they learn into reusable evidence for product, engineering, or business
decisions.

## Product, Platform, and Domain Boundaries

Vashishta, Eric, and Jadhav all treat applied research as hypothesis-driven
work, but each one emphasizes a different output.

[[person:vinvashishta|Vin Vashishta]] puts applied
research close to [[data products]]
and ML monetization. In
[[podcast:make-money-with-machine-learning-roles-skills|Monetize Machine Learning]],
the 20:15 and 26:58 chapters separate research work from pure product
management and pure architecture. Researchers create the technical evidence
that lets a team decide whether a model can become a revenue-generating product.

[[person:mihaileric|Mihail Eric]] puts the boundary
between research and [[MLOps]] under
pressure. In
[[podcast:research-to-production-ml-systems-roadmap|From Research to Production]],
the 23:32, 30:16, and 34:20 chapters argue that researchers need engineering
rigor and engineers need experimental rigor. He describes embedded teams and
code reviews for researchers. He also describes engineers who read papers or
reproduce models.

[[person:aishwaryajadhav|Aishwarya Jadhav]] makes the
definition domain-specific. In
[[podcast:from-computer-vision-research-to-autonomous-driving-ai|Applying Computer Vision Research to Building Production-Ready AI Systems]],
she ties applied research to sensors, latency, and labeling strategy. She also
ties it to safety checks and staged deployment. The 29:45 and 32:43 chapters
connect [[computer vision]]
research in autonomous driving with simulation and closed-track tests. They also
cover on-road tests and release controls before the system becomes usable.

## Turning Research Into Product Decisions

Teams benefit from applied research when it changes a decision. In Vin
Vashishta's
[[podcast:make-money-with-machine-learning-roles-skills|Monetize Machine Learning]],
the 43:28 chapter connects product management with researchable use cases. A
business question has to become a technical hypothesis before researchers can
test it. The 48:54 chapter adds feasibility studies and gated decisions, which
keeps research connected to product risk instead of open-ended exploration.

[[person:lorismarini|Loris Marini]] describes a similar
SaaS case. In
[[podcast:data-professionals-business-skills-in-saas|Data Professionals Need Business Skills in SaaS]],
the 2:45 chapter describes research skills applied in a startup. The 8:30
chapter discusses reinforcement learning applied to practical problems. Marini
ties applied research to stakeholder language and business metrics. He also
ties the work to model deployment rather than treating research as a separate
track.

For a data team, applied research should produce a decision-ready answer. The
team should know whether to continue, stop, or simplify. It should also know
whether to collect different data, change the metric, or move toward production.
When teams need stronger evidence, they move toward
[[experimentation and causal inference]].
When they need to know whether the approach can be served reliably, they move
toward
[[machine learning system design]].

## Reproducible Research Systems

Several guests treat reproducibility as part of applied research, not as cleanup
after the fact. In
[[podcast:research-to-production-ml-systems-roadmap|From Research to Production]],
[[person:mihaileric|Mihail Eric]] says researchers need
engineering rigor at the 23:32 chapter. In the 44:36 and 46:57 chapters, he
recommends end-to-end systems, deployment practice, and code reviews. If no one
can reproduce the result or run the system, the research can't guide production
work.

[[person:johannabayer|Johanna Bayer]] makes the same
argument from academia in
[[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]].
At 8:30, she discusses reproducible manuscripts with embedded code. At 12:10
and 16:36, she frames research software engineering around software-focused
research outputs and reusable toolboxes. Bayer connects applied research with
[[open source]]
and [[software engineering]].

[[person:elenitziritazacharatou|Eleni Tzirita Zacharatou]]
adds a systems-research version in
[[podcast:big-data-analytics-and-postdoc-research|Big Data Analytics and Postdoc Research]].
The 23:08 and 24:15 chapters discuss Nebula Stream and Agora infrastructure.
They also discuss system-driven research that grows from earlier
stream-processing systems such as Apache Flink. In that setting, researchers do
not only produce an insight. They also produce an infrastructure idea that other
researchers or industry teams can
evaluate.

## Deployment Constraints Direct the Research

The work changes when the deployment domain changes. In
[[podcast:from-computer-vision-research-to-autonomous-driving-ai|Applying Computer Vision Research to Building Production-Ready AI Systems]],
[[person:aishwaryajadhav|Aishwarya Jadhav]] discusses
sensor tradeoffs at 11:22 and on-vehicle inference at 22:17. She covers model
compression at 23:28 and staged validation from 29:45 onward. Those constraints
make the research question more specific than "which model is best?" The team
has to ask which model works under the product's cost, latency, privacy, and
safety requirements.

In the same episode, the 51:28 chapter discusses sensitive-case testing and the
52:53 chapter discusses multimodal LLMs in autonomous-driving contexts. These
autonomous-driving examples connect applied research to
[[LLM production patterns]]
and [[notebook-to-production-ai-systems|notebook-to-production AI systems]].
The research idea has to meet evaluation, rollout, monitoring, and system
coordination constraints before a team can operate it.

## Adjacent Applied Research Topics

The topic connects to adjacent roles, systems, and practices:

- [[Machine Learning]]
- [[Experimentation]]
- [[MLOps]]
- [[Production]]
- [[Machine Learning System Design]]
- [[Academic Researcher to Data Science]]
- [[Computer Vision]]
- [[Open Source]]
