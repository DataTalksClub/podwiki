---
layout: "person"
title: "Valerii Babushkin"
summary: "Valerii Babushkin's DataTalks.Club discussions on ML system design interviews, design documents, fraud detection, experimentation, monitoring, and production ML tradeoffs."
source_url: "https://datatalks.club/people/valeriybabushkin.html"
podcast_episodes: ["machine-learning-system-design-interview", "ml-system-design"]
github: "VENHEADs"
linkedin: "venheads"
curated: "true"
---

# Valerii Babushkin

Valerii Babushkin appears in two DataTalks.Club episodes about
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
In
[ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he speaks from experience leading data teams focused on ML at Blockchain.com and Meta.
Earlier roles included Alibaba, X5 Retail Group, and Yandex. In
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}),
he uses the same production background to explain why teams need written,
maintained design documents before and after launch.

The short bio matters because his podcast arguments come from hiring,
interviewing, and running production systems at scale. At 7:31 in
[ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he says he had led teams up to roughly 150 people and conducted hundreds or
thousands of interviews. At 8:08, he adds that his work covered machine
learning and analytics. He also worked with A/B testing, data engineering, and
MLOps on large event-volume systems.

## ML System Design Interviews as Practical Reasoning

Valerii frames the ML system design interview as a test of system reasoning. A
candidate needs to tell a coherent 45-minute story about an ML system. Reciting
model families isn't enough. At 9:36 and 11:23 in
[the interview episode]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he says large tech companies use this round for machine learning engineers.
Interviewers want to see full-system reasoning.

Use his episode with the
[Machine Learning System Design Interview]({{ '/wiki/machine-learning-system-design-interview/' | relative_url }})
guide for ML-heavy roles. The
[Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }})
uses the same distinction.

His advice is to make assumptions explicit and invite correction. Around 20:33,
he says a candidate can state an assumption and ask whether the interviewer
agrees. Label delay, domain context, latency, and operational constraints can
change the whole design. Around 29:09, he recommends sketching a baseline first.

Then the candidate can iterate deeper if the interviewer wants more detail. The
same answer style supports the broader
[Machine Learning Engineer Roadmap]({{ '/wiki/machine-learning-engineer-roadmap/' | relative_url }}),
where production reasoning matters more as a candidate moves beyond junior work.

## Fraud Detection, Metrics, and A/B Testing

The fraud-detection walkthrough is Valerii's clearest example of ML system
design. At 13:58 in
[ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he separates software system design from ML system design. The software version
centers throughput and storage. It also covers caches, sharding, and load
balancing.

The ML version starts with probabilities and loss functions, then adds real-time
decisions, transaction value, and calibration. At 16:43, he uses fraud labels and
class imbalance to show why metric choice is part of the system, not an
afterthought.

The discussion feeds the
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
page and the
[Machine Learning for Software Engineers]({{ '/wiki/machine-learning-for-software-engineers/' | relative_url }})
guide.

Valerii repeatedly brings the design back to product validation. At 24:28, he
describes an ML model as a system with features and outputs. Feature preparation
and A/B testing sit around it. At 40:21, he starts from the business goal and
asks whether the team can measure it directly or needs a proxy.

At 57:37, he says production validation is usually best handled through A/B
testing. Human labels come in when the domain needs manual judgment. Those points
link his episode to
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[Causal Inference]({{ '/wiki/causal-inference/' | relative_url }}), and
[Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }}).

## Features, Labels, and Production Pipelines

Valerii pushes candidates and teams to talk about labels and features before
model architecture. Validation and serving belong in that same discussion. At
44:11 in
[ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he walks from target definition to labels and features. Then he covers model
choice and loss function. Preprocessing, offline validation, and A/B testing come
next.

At 47:52, he says algorithms are only a small part of an ML system. Good features
and labels matter more than a sophisticated model with bad inputs.

The same ideas appear in
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
where projects need visible data and label decisions. They also need metrics and
validation choices.

His production view also changes role expectations. At 50:57, he says a model
has little value unless it's integrated into a product system. That's why he
prefers the machine learning engineer framing over a notebook-only view of data
science. His episodes fit beside
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
when a page needs a bridge from modeling work to operational ownership.

## Design Documents That Fail Fast

In
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}),
Valerii shifts from interviews to delivery. At 7:06, he says the purpose of an
ML design document is to make a weak project fail early. The team should learn
that before spending months on implementation. At 8:39 and 11:34, he says teams
should use a design doc like a blueprint. They should discover feasibility
problems, missing data, unclear goals, and conflicting assumptions before
implementation.

Valerii uses that argument in
[ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
and [Data Science Project Management]({{ '/wiki/data-science-project-management/' | relative_url }}).

Valerii says the document isn't just a startup artifact. At 14:36, writing the
design down lets other people review it. They can challenge the need for ML and
suggest simpler options.

His hierarchy is practical: an if statement can be better than linear regression,
and linear regression can be better than a nonlinear model. A nonlinear model can
be better than a neural network when the simple solution is enough. At 55:13, he
returns to the same point by warning that skipping a baseline may cost a team
months of unnecessary work.

## Ownership, Documentation, and Bus Factor

Valerii treats ML design documents as living engineering artifacts. At 19:01 in
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}),
he says documentation breaks when teams mark it done while the system keeps
changing. At 24:37, he argues that a team should write who owns each area. Then
the right person can update the right part of the document when reality changes.
His view links ML design to [Documentation]({{ '/wiki/documentation/' | relative_url }})
and [Leadership]({{ '/wiki/leadership/' | relative_url }}).

The ownership discussion becomes a risk-management argument at 31:59. Valerii
uses bus factor to ask how many people understand each critical area and where a
project has single-person dependencies. At 36:50 and 41:01, he proposes modular
chapters and owners or maintainers per chapter. He also proposes update signals
and performance incentives for design-doc reviews. His design-doc episode is
useful for pages about production ML tradeoffs, not only for documentation pages.

## Monitoring, Drift, and Fallbacks

Valerii's production ML advice consistently ends with monitoring and fallback
planning. In
[ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
he says at 46:09 that real systems need monitoring for distribution shift,
class-balance changes, and broken models. They also need monitoring for degraded
performance. At 47:48, he argues that mentioning those failure modes in an
interview helps a candidate. It shows exposure to production behavior.

In
[ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}),
he makes the same point more operational. At 47:46, he distinguishes data drift
from data errors and concept drift. He also names prediction drift and model
quality problems. At 51:59, he places reliability, monitoring, and fallbacks in
the integration and growth part of the design.

A team may need a weaker model, a few rules, or even a constant placeholder when
the preferred model or data path fails. Use these episodes beside
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[MLOps Architecture]({{ '/wiki/mlops-architecture/' | relative_url }}), and
[Model Monitoring vs Data Observability]({{ '/wiki/model-monitoring-vs-data-observability/' | relative_url }}).

## Related Pages

These pages expand the main threads from Valerii's two DataTalks.Club episodes.

- [ML System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }})
- [ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
- [Machine Learning System Design Interview]({{ '/wiki/machine-learning-system-design-interview/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
