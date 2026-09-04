---
title: "Prometheus and Grafana"
summary: "The metrics-scraping and dashboarding pair behind MLOps Zoomcamp's live model monitoring."
related_course:
  - Evidently
  - Model Monitoring
  - Model Deployment
  - OpenTelemetry
  - CI/CD
---

Prometheus scrapes numerical metrics from running services on a schedule and stores them as time series; Grafana queries those series and draws the operational picture. MLOps Zoomcamp connects them to ML monitoring: the prediction service exposes Evidently-derived metrics (drift scores, prediction counts, interquartile distances) on a /metrics endpoint, Prometheus collects them every 15 seconds, and Grafana dashboards show drift and traffic over time with alert rules on top.

The module's Docker Compose stack runs the whole loop locally — service, Prometheus, Grafana, and an Evidently metrics service — so learners see alerts fire when they send drifted data through the service.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 5: Model Monitoring

## Related concepts

- [Evidently](/course-wiki/evidently/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Model Deployment](/course-wiki/model-deployment/)
- [OpenTelemetry](/course-wiki/opentelemetry/)
- [CI/CD](/course-wiki/ci-cd/)
