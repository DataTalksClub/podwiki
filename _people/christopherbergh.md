---
layout: "person"
title: "Christopher Bergh"
summary: "Christopher Bergh's DataTalks.Club podcast contributions on DataOps, reliable pipelines, automation, observability, and production data practices."
source_url: "https://datatalks.club/people/christopherbergh.html"
podcast_episodes: ["dataops-automation-and-reliable-data-pipelines", "dataops-for-data-engineering"]
twitter: "ChrisBergh"
linkedin: "chrisbergh"
curated: "true"
expertise: ["DataOps", "data engineering reliability", "data observability", "CI/CD for data pipelines", "production data systems", "MLOps and DataOps overlap"]
---

## Background

Christopher Bergh is the CEO and Head Chef at DataKitchen. He co-authored the
DataOps Cookbook and DataOps Manifesto. In DataTalks.Club interviews, he
advocates for [DataOps]({{ '/wiki/dataops/' | relative_url }}) as the operating
discipline around data and analytics delivery.

His podcast contributions focus on how data teams reduce production errors,
shorten deployment cycle time, and make pipeline work less dependent on
individual heroics.

Bergh came to this view after moving from software engineering into data
leadership. In
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he described data science, data engineering, and visualization as a factory for
insights. In
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
he revisited the same lesson from pre-cloud SQL Server systems. For Bergh, the
hard part wasn't writing data code alone. It was operating the systems around
the work.

## DataOps as Operating Practice

Bergh defines DataOps as a system for improving how data teams work. He
separates it from [data engineering]({{ '/wiki/data-engineering/' | relative_url }}).
Around 6:42 in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he reduces the practice to three measurable targets. Teams should lower
production errors, shorten deployment cycle time, and improve team
productivity.

That framing shows up again around 15:52 in
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
where he groups automation with testing. He adds monitoring and observability
to the same operating loop. For Bergh, that work lets teams move without fear
or unsustainable heroism.

His factory metaphor keeps attention on the whole value stream. In the 2022
discussion, he warns that a data pipeline can have a strong model or dashboard.
It can still fail if the path from source data to user value is brittle.

Use Bergh's DataOps view with
[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}) and the
practical tool categories in
[DataOps Tools]({{ '/wiki/dataops-tools/' | relative_url }}). The operating
layer matters when it makes changes reviewable and testable. It also needs to
make those changes observable and recoverable.

## Automation, CI/CD, and Observability

Bergh's concrete advice starts with version control and automated tests. He
connects them to [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}). Around
33:47-34:37 in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he recommends version control for code and transformation logic. Reports,
tests, and deployment logic belong there too. Teams should then run automated
checks in development and production.

Around 30:55 and 42:39 in
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
he adds regression tests, realistic test data, and infrastructure as code. He
also argues for end-to-end checks before changes reach production users.

Observability is the other half of that release path. Around 7:22 in the 2022
episode, Bergh treats production data failures as quality and observability
problems. The team should know when output is blank, late, malformed, or
unusable before a customer or executive reports it. That places his work
directly beside
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

In the 2024 episode around 50:29, he explains why DataKitchen's focus shifted
toward observing production systems first. Many teams already had production
assets with weak development practice. Monitoring the running system became a
practical entry point for change.

## Data Engineering, MLOps, and Production

Bergh treats [MLOps]({{ '/wiki/mlops/' | relative_url }}) and DataOps as
overlapping reliability disciplines rather than competing movements. Around
50:42 in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he connects DataOps and MLOps through shared DevOps principles. The same
principles apply to pipelines and models. They also apply to visualizations
and governance. Around 18:46 in
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
he argues that the core principles still matter when the current buzzword is
MLOps, LLMs, or data observability.

His practical boundary is [production]({{ '/wiki/production/' | relative_url }}).
Around 23:56-26:54 in the 2024 episode, he separates day-one delivery from
day-two operation and day-three change. A model, dashboard, or pipeline isn't
ready just because it works once. It must keep working with new data. It should
expose problems before customers feel them and let a new teammate make a small
change without putting the system at risk.

[Orchestration]({{ '/wiki/orchestration/' | relative_url }}) becomes relevant
for the same reason. Schedulers and workflow tools help only when they
participate in the broader release, monitoring, and recovery loop.

## Runbooks, Recovery, and Team Sustainability

Bergh repeatedly pushes teams from manual checklists toward automated
playbooks. Around 34:37-38:08 in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he treats runbooks as a starting point, not the final state. Teams should
document how the system works. They should then automate recurring checks and
recovery steps so the system runs without constant human attention and alerts
when something is wrong.

That recovery focus is also a management stance. In both episodes, Bergh
contrasts fear-based teams with hero-based teams. Fear produces slow review
queues and excessive process. Heroism produces weekend fixes, brittle
handoffs, and knowledge trapped in one person.

His DataOps contribution to the podcast archive is the argument that reliable
data pipelines come from owning the process. Teams should measure errors and
cycle time. They should test with realistic data, automate deployments and
recovery, and make production work sustainable for the people who operate it.
