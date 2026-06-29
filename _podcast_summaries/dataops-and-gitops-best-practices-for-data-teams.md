---
layout: podcast_summary
title: "DataOps & GitOps for Data Teams: Onboarding, IaC, Reproducibility & Production Best Practices"
source_episode: "datatalksclub.github.io/_podcast/dataops-and-gitops-best-practices-for-data-teams.md"
source_url: "https://datatalks.club/podcast/dataops-and-gitops-best-practices-for-data-teams.html"
season: 11
episode: 3
guests: ["tomaszhinc"]
topics: ["DataOps", "GitOps", "data teams", "tools"]
summary_status: source-index
youtube_url: "https://www.youtube.com/watch?v=lem7knxqNzg"
spotify_url: "https://open.spotify.com/episode/6jLgdl59sVCdVNJezdIqJY?si=NXasnXtFQVO0KAcCFbvUtQ"
apple_url: "https://podcasts.apple.com/us/podcast/from-data-science-to-dataops-tomasz-hinc/id1541710331?i=1000583457504"
---
# DataOps & GitOps for Data Teams: Onboarding, IaC, Reproducibility & Production Best Practices

## Original Episode

Use these links for the canonical episode and media sources.

- [Open the original DataTalks.Club podcast page](https://datatalks.club/podcast/dataops-and-gitops-best-practices-for-data-teams.html)
- [Watch on YouTube](https://www.youtube.com/watch?v=lem7knxqNzg)
- [Listen on Spotify](https://open.spotify.com/episode/6jLgdl59sVCdVNJezdIqJY?si=NXasnXtFQVO0KAcCFbvUtQ)
- [Listen on Apple Podcasts](https://podcasts.apple.com/us/podcast/from-data-science-to-dataops-tomasz-hinc/id1541710331?i=1000583457504)

## Episode Overview

How do you make data work less fragile and easier to onboard while keeping production safe and reproducible? In this episode, Tomasz Hinc, a DataOps practitioner from Poznań with roots in econometrics, product analytics, data engineering and ML, walks through practical DataOps and GitOps patterns for data teams. We cover platform onboarding (requesting infra vs. merge requests), Infrastructure as Code with Terraform, Terragrunt and Atlantis, and a GitOps workflow from branch to Atlantis dry-run and apply. Tomasz.

## People

Use these links to connect the episode to guest notes.

- [Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }})

## Chapter Summary

Use these checkpoints to decide whether to open the source transcript.

- 0:00 - [Podcast Introduction](https://www.youtube.com/watch?v=lem7knxqNzg&t=0)
- 1:40 - [Guest Introduction & Episode Overview](https://www.youtube.com/watch?v=lem7knxqNzg&t=100)
- 2:25 - [Career Journey: Econometrics → ML Trainee → Data Roles](https://www.youtube.com/watch?v=lem7knxqNzg&t=145)
- 4:31 - [Early Experience: OLX, Government Statistics, Academia](https://www.youtube.com/watch?v=lem7knxqNzg&t=271)
- 5:20 - [ML Education: Multi-Dimensional Analysis to Machine Learning](https://www.youtube.com/watch?v=lem7knxqNzg&t=320)
- 6:34 - [Behavioral Analysis & Product Analytics: Clickstream Modeling](https://www.youtube.com/watch?v=lem7knxqNzg&t=394)
- 7:08 - [Operational Realities: ETL Failures, Production Constraints](https://www.youtube.com/watch?v=lem7knxqNzg&t=428)
- 12:40 - [Platform Onboarding: Requesting Infra vs. Doing a Merge Request](https://www.youtube.com/watch?v=lem7knxqNzg&t=760)
- 13:07 - [Platform Teams’ Role: Review, Enablement, and Safe Practices](https://www.youtube.com/watch?v=lem7knxqNzg&t=787)
- 14:12 - [Motivation Shift: From Model-Centric to Data-Centric Work](https://www.youtube.com/watch?v=lem7knxqNzg&t=852)
- 18:59 - [Defining DataOps: Enabling Faster, Less Scary Data Work (DataOps, DevOps)](https://www.youtube.com/watch?v=lem7knxqNzg&t=1139)
- 20:56 - [DataOps & Infra: SQL, Secrets, GitOps, and Developer Enablement](https://www.youtube.com/watch?v=lem7knxqNzg&t=1256)
- 23:04 - [GitOps & IaC Overview: Terraform, Terragrunt, Atlantis](https://www.youtube.com/watch?v=lem7knxqNzg&t=1384)
- 23:42 - [Infrastructure as Code: Declarative Configurations & Reproducibility](https://www.youtube.com/watch?v=lem7knxqNzg&t=1422)
- 26:21 - [GitOps Workflow: Branch, Merge Request, Atlantis Dry Run, Apply](https://www.youtube.com/watch?v=lem7knxqNzg&t=1581)
- 27:34 - [Onboarding Friction: Tooling Challenges for Data Scientists](https://www.youtube.com/watch?v=lem7knxqNzg&t=1654)
- 29:34 - [Learning Path: Narrow Scope, Hands-On Mentorship, Roadmap Advice](https://www.youtube.com/watch?v=lem7knxqNzg&t=1774)
- 35:55 - [Terminal Comfort: Shell Setup, Autocomplete, and Productivity Tweaks](https://www.youtube.com/watch?v=lem7knxqNzg&t=2155)
- 38:20 - [Learning Resources: YouTube, Articles, and CLI Tutorials](https://www.youtube.com/watch?v=lem7knxqNzg&t=2300)
- 40:44 - [DataOps vs Data Engineering: Support & Communication vs Pipeline Coding](https://www.youtube.com/watch?v=lem7knxqNzg&t=2444)
- 41:52 - [Proactive Support: Monitoring, Onboarding, and Cross-Team Education](https://www.youtube.com/watch?v=lem7knxqNzg&t=2512)
- 44:23 - [Suitable Backgrounds: Any Data Role; Log Reading & Troubleshooting](https://www.youtube.com/watch?v=lem7knxqNzg&t=2663)
- 47:55 - [Minimal Operational Skills: Git, Command Line, IAM, Password Managers](https://www.youtube.com/watch?v=lem7knxqNzg&t=2875)
- 54:37 - [Distinction from Management: Cross-Team Enablement vs Team Leads](https://www.youtube.com/watch?v=lem7knxqNzg&t=3277)
- 56:44 - [Infrastructure Choices for Data: Batch Workloads, ECS/AWS Batch vs Kubernetes](https://www.youtube.com/watch?v=lem7knxqNzg&t=3404)
- 58:26 - [Company-Scale Migration: Jenkins → GitLab CI and Broad Collaboration](https://www.youtube.com/watch?v=lem7knxqNzg&t=3506)
- 1:01:27 - [Reproducibility & Dependencies: Fixed Versions, Docker, Silent Failures](https://www.youtube.com/watch?v=lem7knxqNzg&t=3687)
- 1:02:28 - [Confidence in Data: Pragmatic Edge-Case Checks & Airflow Caveats](https://www.youtube.com/watch?v=lem7knxqNzg&t=3748)
