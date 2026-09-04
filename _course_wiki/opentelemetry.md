---
title: "OpenTelemetry"
summary: "Instrumenting an AI-built app with traces, metrics, and logs flowing into Prometheus, Loki, Tempo, and Grafana."
related_course:
  - Prometheus and Grafana
  - Playwright
  - CI/CD
  - Model Monitoring
  - Coding Agents
---

Module 4 starts from a deployment truth: a shipped app can still fail silently. OpenTelemetry instruments the application once, with vendor-neutral APIs, and emits three signal types — metrics (counts and latencies), logs (structured events), and traces (request journeys across services). The course wires those into a self-hosted stack: Prometheus for metrics, Loki for logs, Tempo for traces, all browsable in Grafana.

The observability stack feeds the module's incident workflow: an actionable alert fires, a human (or the bounded agent responder) investigates using traces to find where the request went wrong. Observability is what makes the AI-assisted app operable after the agents stop writing code.

## Taught in

- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 4: DevOps and Observability for AI-Built Apps

## Related concepts

- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [Playwright](/course-wiki/playwright/)
- [CI/CD](/course-wiki/ci-cd/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Coding Agents](/course-wiki/coding-agents/)
