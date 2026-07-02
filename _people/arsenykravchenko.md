---
layout: "person"
title: "Arseny Kravchenko"
summary: "Arseny Kravchenko's DataTalks.Club podcast discussion on scalable ML systems, design docs, data strategy, edge constraints, and practical MLOps."
source_url: "https://datatalks.club/people/arsenykravchenko.html"
podcast_episodes: ["building-scalable-and-reliable-machine-learning-systems"]
github: "arsenyinfo"
linkedin: "arsenyinfo"
web: "https://arseny.info/"
curated: "true"
---

# Arseny Kravchenko

Arseny Kravchenko joined DataTalks.Club to explain how engineers design
machine learning systems when the product, data, and runtime constraints are
still unclear. In
[Build Scalable, Reliable ML Systems](https://datatalks.club/podcast/building-scalable-and-reliable-machine-learning-systems.html),
he treats [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
as practical decision work. Engineers start with goals, surface constraints,
write down assumptions, and only then choose the model or pipeline.

His background gives context for that framing. He described years of startup ML
work in financial transaction enrichment, manufacturing optimization,
augmented-reality try-on products, and ride sharing. He also focused much of
his career on computer vision and MLOps problems. His examples often sit where
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}),
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
and [production]({{ '/wiki/production/' | relative_url }}) meet.

## Scalable ML Systems Start With Constraints

In
[Build Scalable, Reliable ML Systems](https://datatalks.club/podcast/building-scalable-and-reliable-machine-learning-systems.html),
Arseny framed startup ML work as a tradeoff between reliable systems and the
pressure to ship quickly. He made that point at 6:11 and 7:54. In large
companies, engineers may inherit templates and established decisions. In
startups, a small team often has to choose the architecture and data path. It
also has to choose the model scope and delivery tradeoffs.

He defined ML system design as making decisions under constraints because the
team rarely knows all constraints upfront. Product goals, hardware, available
data, and team capacity can all constrain the design. His framing belongs near
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
and the [machine learning engineer role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).

## Edge Constraints Change Model Design

Arseny's most concrete example came from an augmented-reality mobile try-on
system. At 10:34, he explained why a real-time phone application couldn't rely
on a large cloud-served model. The team had to account for model size, latency,
frames per second, and battery use. They also had to account for device heat
and the runtime support available through Apple's Core ML.

He also separated technical constraints from product constraints. A shoe
overlay that jitters may be technically impressive but unacceptable to users.
A model that reaches enough frames per second may still drain the battery too
quickly. Arseny didn't reduce the design to "make the model faster." He
considered lower model frequency, interpolation between frames, and the product
definition of realism versus visual appeal.

Arseny used edge ML as a system-design problem, not only a model-compression
problem. That discussion links naturally to
[ML system design documents]({{ '/wiki/ml-system-design-documents/' | relative_url }}),
[MLOps architecture]({{ '/wiki/mlops-architecture/' | relative_url }}), and
[batch versus streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
because serving mode changes what the system has to guarantee.

## Design Docs Turn Unknowns Into Decisions

At 14:49 and 18:49, Arseny used "known unknowns" and "unknown unknowns" to
explain why teams need a lightweight design phase. Talking to experienced
people can expose known risks before the team builds. Dirty baselines and early
tests can reveal product behavior the team didn't expect. In his AR example,
the shoe model confused a reflection in a mirror with a second real leg.

He didn't argue for heavyweight planning. His point was that writing a design
document helps engineers discover gaps in the problem and domain. It also
helps them find weak interfaces between components.

At 20:21, he recommended starting with the problem instead of the solution. If
the team has only a few hours and a short document, he would still spend
roughly half of that effort on the problem. He asked teams to name goals and
non-goals. They should also name user scenarios, assumptions, and constraints.

His advice sits close to
[Valerii Babushkin](https://datatalks.club/people/valeriybabushkin.html)'s
[ML System Design Playbook](https://datatalks.club/podcast/ml-system-design.html).
Both guests treat design docs as a way to expose weak assumptions before a team
turns them into production work.

## Data Strategy Belongs in the Solution Blueprint

At 29:01, Arseny tied goals and non-goals to measurable objectives. Some
metrics may start informal, such as the team judging whether generated images
look acceptable. Over time, those checks can become peer review and external
human evaluation. Later, the team can use product feedback or A/B testing. His
point was that the design
needs a path from product expectations to evaluation, even when the first
metric is imperfect.

At 31:42 and 32:37, he moved from problem framing to the solution blueprint.
The team should define a baseline and the metrics used to beat that baseline.
They should also define the pipeline components and the system's data needs.

Data strategy is part of that same blueprint. The team needs to know whether
the data already exists and who owns it. They also need to know the access
cost, processing steps, and features required at training and serving time.

Arseny's data-strategy discussion links his episode to
[data strategy]({{ '/wiki/data-strategy/' | relative_url }}),
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
For him, a design doc is incomplete if it names a model but leaves the data path
and evaluation path vague.

## Production Architecture Needs Diagrams

At 37:15, Arseny agreed with using diagrams to show components and data flow.
Diagrams can also show dependencies and serving choices. A diagram can reveal
whether the system needs real-time calls or batch processing. It can also show
queues, device-side inference, model training data, and a separate data path
for evaluation.

The diagram isn't decoration because it gives reviewers a way to ask whether
each dependency is owned and whether the required data is available. Reviewers
can also check whether the system can meet its latency and reliability constraints.
This is where his discussion moves from ML modeling into
[production architecture]({{ '/wiki/production/' | relative_url }}) and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

## Practical MLOps Requires Software Engineering

Near the end of the episode, Arseny explained why ordinary system-design
fundamentals still matter for ML engineers. At 58:28, he recommended learning
from general software system design because ML systems still need software
architecture, interfaces, and reliability. A good ML engineer, in his framing,
also needs enough software engineering skill to build the system that surrounds
the model.

That view matches pages that place ML engineering between modeling, software,
and operations. Those pages include
[machine learning engineer role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[machine learning for software engineers]({{ '/wiki/machine-learning-for-software-engineers/' | relative_url }}).
Arseny's contribution is the constraint-driven version. The engineer should
write down what the system must do and where it will run. They should also
write down how the system will be measured and which data or runtime
assumptions could break it.
