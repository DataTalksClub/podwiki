---
layout: wiki
title: "Applied Research"
summary: "How the archive describes applied research as hypothesis-driven ML work that turns uncertain ideas into reusable artifacts, products, and production systems."
related:
  - Machine Learning
  - Production
  - Machine Learning System Design
  - Academic Researcher to Data Science
  - AI
---

## Definition and Scope

Teams do applied research when they aim research at a practical product,
workflow, or business decision. In the podcast archive, applied researchers
produce datasets and models. They also produce benchmarks, experiments,
prototypes, and product insights. The work is still scientific, but it's
anchored to a use case and domain. Production constraints guide it too.

Use this page when evidence connects research to practical ML systems. Use
[Academic Researcher to Data Science]({{ '/wiki/academic-researcher-to-data-science/' | relative_url }})
for career-transition material.

## Contents

Use these sections to move through the page.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Teams start applied research with hypotheses, not only models. Vin Vashishta
describes the first model as a hypothesis about how a system works. The
researcher then uses data, experiments, model behavior, and explainability to
refine that hypothesis. Production feedback can confirm or reject it.

Research teams should make artifacts reusable. The archive treats novel
datasets, benchmarks, model prototypes, and experimental results as
intellectual property that downstream data scientists and ML engineers can
reuse. This work is valuable when it improves the next product decision or
production build.

The research-to-production gap is organizational as much as technical. Mihail
Eric argues for embedded teams, role fluidity, code reviews for researchers,
and engineers reading papers and reproducing models. The handoff fails when
researchers throw notebooks over the wall and engineers receive unclear
assumptions.

Real-world deployment changes the research question. Computer-vision and
autonomous-driving episodes move from model quality to latency and sensor cost.
They also bring in labeling, simulation, staged rollouts, and privacy. Safety
checks, edge cases, and system coordination become part of the work too.

## Episode Evidence

These episodes give the strongest applied-research evidence.

- [Monetize Machine Learning](https://datatalks.club/podcast.html)
  (20:15-29:18) separates applied researchers from science
  researchers and frames applied research as business-aligned artifact creation.
- [Monetize Machine Learning](https://datatalks.club/podcast.html)
  (36:10-43:28) defines research as hypothesis design,
  experimentation, and explainability while also covering model deconstruction
  and iterative evidence gathering.
- [From Research to Production](https://datatalks.club/podcast.html)
  (8:34-20:25) covers research infrastructure, prototyping, and benchmarks while
  Mihail also discusses experimental tooling and deployment stacks.
- [From Research to Production](https://datatalks.club/podcast.html)
  (23:32-51:28) covers reproducibility, engineering rigor,
  embedded teams, and code reviews. Later sections cover end-to-end systems,
  paper reading, and model reproduction.
- [Applying Computer Vision Research to Production AI](https://datatalks.club/podcast.html)
  (29:45-36:12) describes simulation, closed-track testing, and
  on-road testing. Aishwarya also covers anonymized sensor data, labeling
  strategy, safety checks, and staged deployments.
- [Applying Computer Vision Research to Production AI](https://datatalks.club/podcast.html)
  (51:28-55:25) discusses sensitive-case evaluation, broader scenario
  tests, gradual rollout, and multimodal LLM constraints.

## Related Pages

Use these pages for adjacent ML, production, and career material.

- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Academic Researcher to Data Science]({{ '/wiki/academic-researcher-to-data-science/' | relative_url }})
- [AI]({{ '/wiki/ai/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})

## Maintenance Notes

Best source files for future expansion:

- `../datatalksclub.github.io/_podcast/make-money-with-machine-learning-roles-skills.md`
- `../datatalksclub.github.io/_podcast/research-to-production-ml-systems-roadmap.md`
- `../datatalksclub.github.io/_podcast/from-computer-vision-research-to-autonomous-driving-ai.md`
- `../datatalksclub.github.io/_podcast/s24e01-competitions-beyond-kaggle-leaderboard.md`

Add future evidence when an episode explains a research artifact, hypothesis, or
benchmark. Also add episodes that explain a prototype, validation stage, or
production handoff. Keep pure career advice on transition pages unless it
changes how research work is done.
