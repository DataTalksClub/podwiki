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

The topic overlaps with [machine learning]({{ '/wiki/machine-learning/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}) because teams test more
than model accuracy. They aren't only reading papers or training models. They
also decide whether ideas can survive product constraints, engineering
constraints, and real users.

## Hypotheses, Benchmarks, and Reusable Evidence

In these interviews, applied research usually means hypothesis-driven technical
work with a use case attached. In
[Monetize Machine Learning](https://datatalks.club/podcast/make-money-with-machine-learning-roles-skills.html),
[Vin Vashishta](https://datatalks.club/people/vinvashishta.html) describes machine
learning research as artifact creation. Teams create datasets, run experiments,
study model behavior, and build knowledge that can support ML products. Around
the 36:10 chapter, he frames the research skill set around hypothesis design and
experimentation. He also includes explainability and iterative evidence
gathering.

[Mihail Eric](https://datatalks.club/people/mihaileric.html) gives the matching
engineering version in
[From Research to Production](https://datatalks.club/podcast/research-to-production-ml-systems-roadmap.html).
At 8:34 and 10:52, he connects research infrastructure with data collection and
prototyping. He also connects it with hypotheses and benchmarks. Eric's version
of applied research doesn't stop when a notebook works. Researchers continue
until they can turn the idea into a reproducible
[ML system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

Teams use applied research to test an uncertain technical idea and turn what
they learn into reusable evidence for product, engineering, or business
decisions.

## Product, Platform, and Domain Boundaries

Vashishta, Eric, and Jadhav all treat applied research as hypothesis-driven
work, but each one emphasizes a different output.

[Vin Vashishta](https://datatalks.club/people/vinvashishta.html) puts applied
research close to [data products]({{ '/wiki/data-products/' | relative_url }})
and ML monetization. In
[Monetize Machine Learning](https://datatalks.club/podcast/make-money-with-machine-learning-roles-skills.html),
the 20:15 and 26:58 chapters separate research work from pure product
management and pure architecture. Researchers create the technical evidence
that lets a team decide whether a model can become a revenue-generating product.

[Mihail Eric](https://datatalks.club/people/mihaileric.html) puts the boundary
between research and [MLOps]({{ '/wiki/mlops/' | relative_url }}) under
pressure. In
[From Research to Production](https://datatalks.club/podcast/research-to-production-ml-systems-roadmap.html),
the 23:32, 30:16, and 34:20 chapters argue that researchers need engineering
rigor and engineers need experimental rigor. He describes embedded teams and
code reviews for researchers. He also describes engineers who read papers or
reproduce models.

[Aishwarya Jadhav](https://datatalks.club/people/aishwaryajadhav.html) makes the
definition domain-specific. In
[Applying Computer Vision Research to Building Production-Ready AI Systems](https://datatalks.club/podcast/from-computer-vision-research-to-autonomous-driving-ai.html),
she ties applied research to sensors, latency, and labeling strategy. She also
ties it to safety checks and staged deployment. The 29:45 and 32:43 chapters
connect [computer vision]({{ '/wiki/computer-vision/' | relative_url }})
research in autonomous driving with simulation and closed-track tests. They also
cover on-road tests and release controls before the system becomes usable.

## Turning Research Into Product Decisions

Teams benefit from applied research when it changes a decision. In Vin
Vashishta's
[Monetize Machine Learning](https://datatalks.club/podcast/make-money-with-machine-learning-roles-skills.html),
the 43:28 chapter connects product management with researchable use cases. A
business question has to become a technical hypothesis before researchers can
test it. The 48:54 chapter adds feasibility studies and gated decisions, which
keeps research connected to product risk instead of open-ended exploration.

[Loris Marini](https://datatalks.club/people/lorismarini.html) describes a similar
SaaS case. In
[Data Professionals Need Business Skills in SaaS](https://datatalks.club/podcast/data-professionals-business-skills-in-saas.html),
the 2:45 chapter describes research skills applied in a startup. The 8:30
chapter discusses reinforcement learning applied to practical problems. Marini
ties applied research to stakeholder language and business metrics. He also
ties the work to model deployment rather than treating research as a separate
track.

For a data team, applied research should produce a decision-ready answer. The
team should know whether to continue, stop, or simplify. It should also know
whether to collect different data, change the metric, or move toward production.
When teams need stronger evidence, they move toward
[experimentation and causal inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).
When they need to know whether the approach can be served reliably, they move
toward
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

## Reproducible Research Systems

Several guests treat reproducibility as part of applied research, not as cleanup
after the fact. In
[From Research to Production](https://datatalks.club/podcast/research-to-production-ml-systems-roadmap.html),
[Mihail Eric](https://datatalks.club/people/mihaileric.html) says researchers need
engineering rigor at the 23:32 chapter. In the 44:36 and 46:57 chapters, he
recommends end-to-end systems, deployment practice, and code reviews. If no one
can reproduce the result or run the system, the research can't guide production
work.

[Johanna Bayer](https://datatalks.club/people/johannabayer.html) makes the same
argument from academia in
[Teaching Open Science and Reproducible Research](https://datatalks.club/podcast/teaching-reproducible-research-and-open-science-coding-practices-for-academia.html).
At 8:30, she discusses reproducible manuscripts with embedded code. At 12:10
and 16:36, she frames research software engineering around software-focused
research outputs and reusable toolboxes. Bayer connects applied research with
[open source]({{ '/wiki/open-source/' | relative_url }})
and [software engineering]({{ '/wiki/software-engineering/' | relative_url }}).

[Eleni Tzirita Zacharatou](https://datatalks.club/people/elenitziritazacharatou.html)
adds a systems-research version in
[Big Data Analytics and Postdoc Research](https://datatalks.club/podcast/big-data-analytics-and-postdoc-research.html).
The 23:08 and 24:15 chapters discuss Nebula Stream and Agora infrastructure.
They also discuss system-driven research that grows from earlier
stream-processing systems such as Apache Flink. In that setting, researchers do
not only produce an insight. They also produce an infrastructure idea that other
researchers or industry teams can
evaluate.

## Deployment Constraints Direct the Research

The work changes when the deployment domain changes. In
[Applying Computer Vision Research to Building Production-Ready AI Systems](https://datatalks.club/podcast/from-computer-vision-research-to-autonomous-driving-ai.html),
[Aishwarya Jadhav](https://datatalks.club/people/aishwaryajadhav.html) discusses
sensor tradeoffs at 11:22 and on-vehicle inference at 22:17. She covers model
compression at 23:28 and staged validation from 29:45 onward. Those constraints
make the research question more specific than "which model is best?" The team
has to ask which model works under the product's cost, latency, privacy, and
safety requirements.

In the same episode, the 51:28 chapter discusses sensitive-case testing and the
52:53 chapter discusses multimodal LLMs in autonomous-driving contexts. These
autonomous-driving examples connect applied research to
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and [notebook-to-production AI systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }}).
The research idea has to meet evaluation, rollout, monitoring, and system
coordination constraints before a team can operate it.

## Adjacent Applied Research Topics

The topic connects to adjacent roles, systems, and practices:

- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Experimentation]({{ '/wiki/experimentation/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Academic Researcher to Data Science]({{ '/wiki/academic-researcher-to-data-science/' | relative_url }})
- [Computer Vision]({{ '/wiki/computer-vision/' | relative_url }})
- [Open Source]({{ '/wiki/open-source/' | relative_url }})
