---
layout: wiki
title: "Applied Research"
summary: "How applied research turns uncertain ML ideas into usable systems, benchmarks, prototypes, and production evidence."
related:
  - Machine Learning
  - Production
  - Machine Learning System Design
  - Simulation and Digital Twins
  - Synthetic Data
  - Academic Researcher to Data Science
  - Experimentation
  - MLOps
---

Teams use applied research to aim uncertain technical work at a practical
decision, product, or system. The output may be a dataset, benchmark, or
prototype. It may also be a modeling approach, validation method, or production
design. The work still contains scientific uncertainty, but the team expects
evidence it can use.

The topic sits between [[Machine Learning]], [[Experimentation]], [[Production]],
and [[Machine Learning System Design]]. Applied-research teams do more than
read papers or train models. They also test whether ideas can survive product
constraints, engineering constraints, domain constraints, and real users.

## Applied Research Boundary

Across the cited episodes, the work is hypothesis-driven and tied to a use case.
Research teams create datasets, experiments, model-behavior studies, and
explainability work. They also create reusable knowledge that can support ML
products [[cite:make-money-with-machine-learning-roles-skills=>Monetize
Machine Learning]].

Teams aiming at production start with research infrastructure, data collection,
prototyping, and hypotheses. Benchmarks belong in that system too. The work
doesn't stop when a notebook works. The idea has to become reproducible enough
for [[machine-learning-system-design=>ML
system design]] and production handoff [[cite:research-to-production-ml-systems-roadmap=>From
Research to Production]].

Applied-research teams should produce a decision-ready answer. A team should
know whether to continue, stop, or simplify. It should also know whether to
collect different data, change the metric, or move toward production. When the
evidence question gets stronger, the work moves toward [[Experimentation and
Causal Inference]].
When serving constraints matter, it moves toward [[Machine Learning System
Design]].

## Different Research Outputs

The cited episodes agree on hypothesis-driven work, but they focus on different
outputs.

[[person:vinvashishta=>Vin Vashishta]] puts applied research close to [[Data
Products]] and ML monetization. Research creates the technical evidence a team
needs before it can decide whether a model can become a revenue-generating
product [[cite:make-money-with-machine-learning-roles-skills=>Monetize Machine
Learning]].

[[person:mihaileric=>Mihail Eric]] puts the boundary between research and
[[MLOps]] under pressure. Researchers need engineering rigor and engineers need
experimental rigor. Teams can narrow the gap with embedded research work, code
reviews for researchers, paper reading, and model reproduction
[[cite:research-to-production-ml-systems-roadmap=>From Research to Production]].

[[person:aishwaryajadhav=>Aishwarya Jadhav]] makes the definition
domain-specific. In autonomous driving, applied computer vision research has to
handle sensors and latency. Labeling strategy sets another boundary, and safety
checks constrain release decisions. Simulation, closed-track tests, and on-road
tests guide the work. Release gates add another constraint
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Computer Vision
Research to Production AI]].

[[person:lavanyagupta=>Lavanya Gupta]] adds the LLM benchmarking version through
provider comparisons for financial use cases. The tests covered long context
and multimodal ability, plus NLU, code, and math. They also measured latency and
throughput, so the work didn't end at "which model scored highest." It gives
the institution evidence for adoption and fallback design. It can also produce a
publishable result when the benchmark reveals reusable evidence
[[cite:applied-llm-research-and-career-growth-in-practice@8:43=>Applied LLM Research in Practice]]
[[cite:applied-llm-research-and-career-growth-in-practice@15:28=>Long Context LLMs on Financial Concepts]].

## Turning Research Into Product Decisions

Research creates value when it changes a product or business decision.
A business question has to become a technical hypothesis before researchers can
test it. Feasibility studies and gated decisions keep research connected to
product risk instead of open-ended exploration
[[cite:make-money-with-machine-learning-roles-skills=>Monetize Machine Learning]].

Startup and SaaS examples add the business boundary. Research skills have to
connect to stakeholder language, business metrics, and deployment plans.
Reinforcement learning or other advanced methods still need a practical problem
and a way into the product [[cite:data-professionals-business-skills-in-saas=>Business
Skills for Data Professionals in SaaS]].

This is why applied research belongs near [[Machine Learning for Business]] and
[[Data Product Management]]. A useful research output is more than a higher
score. It tells the product or engineering team what to build, what not to
build, or which evidence is still missing.

## Reproducible Research Systems

Reproducibility is part of applied research, not cleanup after the fact. If no
one can reproduce the result or run the system, the research can't guide
production work. End-to-end systems, deployment practice, code reviews, and
engineering rigor turn research into reusable evidence
[[cite:research-to-production-ml-systems-roadmap=>From Research to Production]].

Academic and open-science discussions make the same point through research
software. Reproducible manuscripts, embedded code, software-focused research
outputs, and reusable toolboxes connect applied research with [[Open Source]]
and [[Software Engineering]]. They also connect it with [[Academic Researcher to
Data Science]]
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching
Open Science and Reproducible Research]].

Systems research can produce infrastructure ideas rather than only model
results. Nebula Stream and Agora show applied research as a systems lineage:
researchers build on earlier stream-processing systems. They also produce
designs that other researchers or industry teams can evaluate
[[cite:big-data-analytics-and-postdoc-research=>Big Data Analytics and Postdoc
Research]].

Industry applied-research teams can also publish benchmarks when managers
support external sharing. Lavanya describes an industry-track publication path:
the team couldn't release bank data, but it could publish a reusable finding
from long-context LLM benchmarking. The work happened on top of regular product
work, so manager support and a clear underexplored contribution mattered
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research
in Practice]].

Lavanya describes why manager support and community channels matter. The team
had to decide that the result should be shared outside the company. Then the
work moved through arXiv endorsement and conference submission channels.
[[Technical Writing]] becomes part of the research system. Community review
does too, instead of sitting in a separate career lane
[[cite:applied-llm-research-and-career-growth-in-practice@17:28=>Publishing from Corporate Teams]]
[[cite:applied-llm-research-and-career-growth-in-practice@19:45=>Manager Support for Publishing]]
[[cite:applied-llm-research-and-career-growth-in-practice@22:10=>arXiv and Early Publications]].

## Deployment Constraints Direct the Research

The deployment domain changes the research question. In autonomous driving,
sensor choice, on-vehicle inference, and model compression constrain the model.
Simulation, closed-track validation, and on-road testing make the question more
specific than "which model is best?" Labeling strategy and staged deployment add
the same pressure
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Computer Vision
Research to Production AI]].

The team has to ask which model works under the product's cost, latency,
privacy, and safety requirements. Sensitive-case testing and multimodal LLM
work add the same constraint. A research idea has to meet evaluation, rollout,
monitoring, and system coordination requirements before a team can operate it
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Computer Vision
Research to Production AI]].

LLM research adds another domain-specific example. Long-context evaluation,
chunking, retrieval, and summarization connect applied research to [[LLM
Evaluation Workflows]]. Benchmarks, rapid prototypes, and feedback tools also
connect it to [[Long Context LLM Evaluation]] and [[RAG Evaluation Workflow]]
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research
in Practice]].

Lavanya used Streamlit-style prototypes to get feedback before treating a
research idea as finished. Her team used Streamlit because it let researchers
share a working demo with leadership and stakeholders without waiting for an
engineering handoff. The prototype exposes whether stakeholders can use the
model behavior. It also helps the team choose more research, better
[[LLM Evaluation Workflows]], or production hardening
[[cite:applied-llm-research-and-career-growth-in-practice@30:14=>Rapid LLM Prototyping]].

## Related Pages

These pages cover adjacent roles, systems, and practices:

- [[Machine Learning]]
- [[Experimentation]]
- [[MLOps]]
- [[Production]]
- [[Machine Learning System Design]]
- [[Academic Researcher to Data Science]]
- [[Computer Vision]]
- [[Open Source]]
