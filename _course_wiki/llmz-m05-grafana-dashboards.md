---
title: "Grafana Dashboards — LLM Zoomcamp Module 5"
summary: "--- video_url: 'https://www.youtube.com/watch?v=Pmh2jT8tEiw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Grafana Dashboards"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Grafana Dashboards

## Notes

---
video_url: "https://www.youtube.com/watch?v=Pmh2jT8tEiw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Grafana Dashboards

Our Streamlit dashboard already works. We bring in Grafana because it
does more. It's a dedicated dashboarding tool: it connects to many data
sources and offers more panel types. It can also raise alerts when a
metric crosses a line.

The tradeoff is that it's a separate, heavier application to run. That's
exactly why, if your needs are simple, the Streamlit dashboard is enough.
When you want more, Grafana reads straight from the Postgres we already
have and shows what's happening in real time.

## Starting Grafana with Docker

Start Grafana on the same network with a volume for data persistence:

```bash
docker run -d \
    --name grafana \
    --network monitoring \
    -p 3000:3000 \
    -v grafana_data:/var/lib/grafana \
    grafana/grafana
```

We already created the network and started PostgreSQL on it in the
database lesson. We run Grafana detached with `-d`. If you'd rather watch
its logs while you set things up, drop the `-d` and run it attached. The
volume means everything you build in Grafana survives a restart, both
data sources and dashboards.

Access Grafana at `http://localhost:3000`. The first login is admin /
admin, and it asks you to set a new password. For local work, admin /
admin again is fine.

## Setting up the data source

Connect Grafana to PostgreSQL:

1. Go to Configuration > Data Sources > Add data source
2. Select PostgreSQL
3. Fill in the connection details:
   - Host: `course-assistant-pg:5432`
   - Database: `course_assistant`
   - User: `user`
   - Password: `password`
   - SSL Mode: disable
4. Click Save & Test. It should say "Database Connection OK"

## Creating the dashboard

Create a new dashboard. We add panels one at a time, and each panel is a
SQL query that Grafana runs against PostgreSQL.

Two habits make these queries behave. First, alias your time column as
`time`. Grafana reads that column to place points on the x-axis, so a
time chart needs it. Second, filter on the selected time range. The panel
then follows whatever you pick at the top instead of the whole table.

Grafana gives us special SQL variables for exactly that filtering:

- `$__timeFrom()`: start of the selected time range
- `$__timeTo()`: end of the selected time range
- `$__timeGroup(column, interval)`: groups results by time intervals

Including `$__timeFrom()` and `$__timeTo()` in the `WHERE` clause isn't
strictly required, but it's better to be explicit. The panel then tracks
whatever range you select at the top.

## Response Time Panel

Shows how long the LLM takes to respond over time.

Each row in the conversations table is already one LLM call, so we
just plot the raw values:

```sql
SELECT
  timestamp AS time,
  response_time
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
ORDER BY timestamp
```

Use the Time series visualization for this panel.

## Token Usage Panel

Shows token consumption over time.

Over a long time range there would be too many points to plot
individually.

We group by time intervals (e.g. every 5 minutes) and take the average
within each bucket:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  AVG(total_tokens) AS avg_tokens
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY 1
ORDER BY 1
```

- `$__timeGroup` rounds timestamps into buckets.
- `GROUP BY 1` groups by the first column (the bucket). 
- `AVG` gives the average tokens per bucket.

Use the Time series visualization for this panel.

## Cost Panel

Shows cumulative cost over time.

Same idea, but instead of averaging we `SUM` the costs within each
time bucket:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  SUM(cost) AS total_cost
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
  AND cost > 0
GROUP BY 1
ORDER BY 1
```

Use the Time series visualization for this panel.

## Model Usage Panel

Sho

## Key concepts

- [Model Monitoring](/course-wiki/model-monitoring/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)

## Related notes

- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=Pmh2jT8tEiw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/12-grafana.md)
