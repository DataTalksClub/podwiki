---
layout: "person"
title: "Danny Leybzon"
summary: "Danny Leybzon on production model monitoring, data observability, MLOps architecture, and tooling tradeoffs."
source_url: "https://datatalks.club/people/dannyleybzon.html"
podcast_episodes: ["mlops-model-monitoring-data-observability"]
expertise: ["MLOps", "model monitoring", "data observability", "tools", "data engineering"]
github: "dleybz"
twitter: "dleybz"
linkedin: "dleybz"
web: "http://web.dleybz.co/"
curated: "true"
---

# Danny Leybzon

Danny Leybzon joined DataTalks.Club as an MLOps Architect at WhyLabs in
[MLOps Architect Guide: Production Model Monitoring, Data Observability & Tooling]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
He brought context from computational statistics, product work at Qubole, and
field engineering at Imply. In the episode, Danny frames [MLOps]({{ '/wiki/mlops/' | relative_url }})
as both a technical and organizational problem. He focuses on monitoring and
upstream data failures after a model reaches [production]({{ '/wiki/production/' | relative_url }}).
He also covers platform fit and how teams choose tools.

## MLOps Architecture as Translation Work

Danny describes MLOps architecture as translation work. The role sits between
customers, business needs, and technical constraints. Around 8:42 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
Danny says customer communication and market awareness matter. He also needs
enough technical depth to reason about production ML systems.

Around 10:32, he adds that the "architect" title came from helping customers
and partners understand the MLOps tooling landscape. He also uses that context
inside WhyLabs.

Use Danny's discussion for [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
and [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}). He doesn't present
architecture as a fixed reference stack, but as a set of tradeoffs. Teams need
to know which tools interoperate and which choices are swappable. They also need
to know which decisions matter for the people operating the model.

## Production Model Monitoring

Danny prioritizes the late part of the ML lifecycle. Around 25:49 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he says WhyLabs focuses on models after deployment, when teams need to know
whether the model still performs well. He cares most about tooling close to
production, especially inference and serving choices such as managed services,
self-hosted APIs, and other deployment paths.

Use his production-first framing with these pages:

- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [MLOps vs DevOps]({{ '/comparisons/mlops-vs-devops/' | relative_url }})
- [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})

He treats monitoring as a production responsibility, not a final dashboard added
after the data science work is done. Around 29:31, he says the easiest
conversations are with teams that already deployed a model and felt pain. He
also tries to talk to teams before they hit that failure.

## Data Observability and Upstream Failures

Danny's strongest operational point is that model problems often start before
the model. At around 27:35 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he says data drift can come from the real world. Data quality problems can come
from something upstream of the model. Teams debugging model behavior need
visibility into ETL and transformation work. They also need orchestration
context and the full data pipeline.

Use this section with the data reliability pages:

- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})

Use Danny's framing when a model alert might come from a feature pipeline or
schema change. It might also come from a missing value spike or distribution
shift rather than a broken model artifact.

## Profile-Based Observability and Alerting

Danny separates WhyLogs from WhyLabs in the monitoring architecture. Around
33:49 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he says WhyLogs creates profiles, which are statistical summaries of data.
WhyLabs stores and analyzes those profiles with visualizations, anomaly
detection, and alerts. Around 55:50, he draws the product boundary again.

WhyLogs is open source profiling. WhyLabs is the SaaS layer that tracks changes
over time.

Danny's profile-based framing fits
[Model Monitoring vs Data Observability]({{ '/comparisons/model-monitoring-vs-data-observability/' | relative_url }})
because the same summaries can help different teams. Danny says data scientists
can catch model performance degradation, model failure, and data drift. Data
engineers can catch data quality issues such as null spikes or breaking schema
changes.

## Tooling Tradeoffs and Build vs Buy

Danny doesn't claim that one MLOps stack fits every team. Around 34:54 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he frames build-vs-buy as an early decision. He often helps data scientists and
machine learning engineers make the business case. He translates
model monitoring into KPIs, objectives, and company risk, not only feature
lists.

Around 36:47, he says WhyLabs stays platform agnostic and integrates with tools
that can run Python or Java. By the time teams want monitoring, they usually
already chose an inference architecture. Danny can still help during later
architectural reviews. He has broad exposure to many tools, even when the
customer has deeper experience with a single stack. Use this part of the
episode with [MLOps Frameworks]({{ '/guides/mlops-frameworks/' | relative_url }}) and
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

## Fairness, Bias, and Segmentation

Danny also covers fairness and bias. Around 41:00 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he says he became interested in whether explainability addresses bias.
He concludes that teams can often do more by segmenting model behavior. They
should also track disparate impact instead of treating explainability as the
whole fairness answer.

Danny spends less time on this topic than on monitoring, but the point still
shows why observability needs slices, cohorts, and segments. Aggregate model
metrics can hide which groups experience harm, so fairness questions feed back
into monitoring design.
Use this alongside [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) when the
question is how teams look at model behavior after deployment.

## Related Pages

Continue from Danny's page into the main episode and topic pages:

- [MLOps Architect Guide: Production Model Monitoring, Data Observability & Tooling]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [MLOps Architecture]({{ '/guides/mlops-architecture/' | relative_url }})
- [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
- [Model Monitoring vs Data Observability]({{ '/comparisons/model-monitoring-vs-data-observability/' | relative_url }})
