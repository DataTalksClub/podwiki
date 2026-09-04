---
title: "Feedback Dashboard — LLM Zoomcamp Module 5"
summary: "We collect two kinds of feedback now. People give thumbs up and down, and the judge gives relevance labels. But we can't see either one yet. So we add them to the Streamlit dashboard from lesson 07, beside the cost and latency panels."
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Feedback Dashboard

## Notes

# Feedback Dashboard

_This lesson has no video._

We collect two kinds of feedback now. People give thumbs up and down, and
the judge gives relevance labels. But we can't see either one yet. So we
add them to the Streamlit dashboard from lesson 07, beside the cost and
latency panels.

First, add feedback queries to `db_query.py`.

Get judge relevance distribution:

```python
def get_relevance_stats():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT relevance, COUNT(*)
                FROM feedback
                WHERE source = 'judge'
                GROUP BY relevance
            """)
            rows = cur.fetchall()
    finally:
        conn.close()
    return dict(rows)
```

Get user feedback stats:

```python
def get_user_feedback_stats():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END),
                    SUM(CASE WHEN score < 0 THEN 1 ELSE 0 END)
                FROM feedback
                WHERE source = 'user'
            """)
            row = cur.fetchone()
    finally:
        conn.close()
    return row
```

Update `dashboard.py` to show the feedback panels.

Import the new functions:

```python
from db_query import get_conversations, get_stats, get_relevance_stats, get_user_feedback_stats
```

Judge relevance distribution:

```python
st.subheader("Judge relevance")
relevance = get_relevance_stats()
st.bar_chart(relevance)
```

User feedback:

```python
st.subheader("User feedback")
thumbs_up, thumbs_down = get_user_feedback_stats()
col1, col2 = st.columns(2)
col1.metric("Thumbs up", int(thumbs_up or 0))
col2.metric("Thumbs down", int(thumbs_down or 0))
```

The dashboard now shows quality alongside cost and speed. The catch is
that with only a few real conversations, the charts look empty. Before
we move to Grafana, let's fill the database with some data so there's
actually something to look at.

## Key concepts

- [LLM Monitoring](/course-wiki/llm-monitoring/)
- [Streamlit](/course-wiki/streamlit/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)

## Related notes

- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/10-feedback-dashboard.md)
