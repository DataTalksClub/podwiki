---
title: "User Feedback — LLM Zoomcamp Module 5"
summary: "---
video_url: "https://www.youtube.com/watch?v=GEifsHDadBw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# User Feedback"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › User Feedback

## Notes

---
video_url: "https://www.youtube.com/watch?v=GEifsHDadBw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# User Feedback

So far we capture execution metrics like response time, tokens, and
cost. But none of that tells us whether the answer was any good. The
people using the system know, the way you can rate a reply in ChatGPT. So
we add thumbs-up and thumbs-down buttons, then record what people click.

This feedback is worth collecting beyond the dashboard. It feeds back
into evaluation. If a user marks an answer as good, the judge you built
in the previous module should ideally agree. That agreement gives you
data to align the judge against.

The signal is noisy. Someone clicks by accident, or rates a bad answer as
good (I do it myself in the demo). But it's still valuable for building an
evaluation dataset. And on the dashboard, a wave of thumbs-down in the
last hour is a clear sign. Go check what broke.

## Feedback table

Feedback can come from a person or, later, from an LLM judge. So we use
one feedback table with a `source` column that records where each row
came from. For now `source` is `"user"` and we store a score.

Add a new function `init_feedback` to `db_init.py`:

```python
def init_feedback():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS feedback")

            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id INTEGER REFERENCES conversations(id),
                    source TEXT NOT NULL,
                    relevance TEXT,
                    explanation TEXT,
                    score INTEGER,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()
```

Update the `__main__` block to call both:

```python
if __name__ == "__main__":
    init_db()
    init_feedback()
    print("Database initialized")
```

Re-run the init script:

```bash
uv run python db_init.py
```

- `source`: `"user"` for human feedback, `"judge"` for LLM evaluations
- `score`: +1 for thumbs up, -1 for thumbs down
- `relevance` and `explanation`: will be used later by the built-in judge

## Saving feedback

Create `db_feedback.py`:

```python
from datetime import datetime
from db_init import get_db_connection, DB_TIMEZONE

def save_feedback(conversation_id, source, relevance=None,
                  explanation=None, score=None):
    timestamp = datetime.now(DB_TIMEZONE)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO feedback (
                    conversation_id, source, relevance,
                    explanation, score, timestamp
                ) VALUES (
                    %s, %s, %s, %s, %s, %s
                )
                """,
                (conversation_id, source, relevance,
                 explanation, score, timestamp),
            )
        conn.commit()
    finally:
        conn.close()
```

## Adding buttons to the app

We already save conversations in `app.py` from lesson 05. To attach
feedback to the right answer, we need the `conversation_id` that
`save_conversation` returns. We keep it in `st.session_state`. Streamlit
reruns the whole script on every click. Session state is how we carry the
id from the answer to the button press.

Add this import to `app.py`:

```python
from db_feedback import save_feedback
```

Update the ask button to save the conversation ID:

```python
if st.button("Ask"):
    with st.spinner("Processing..."):
        answer = assistant.rag(user_input)
        st.success("Completed!")
        st.write(answer)

        record = assistant.last_call
        st.write(f"Response time: {record.response_time:.2f}s")
        st.write(f"Prompt tokens: {record.prompt_tokens}")
        st.write(f"Completion tokens: {record.completion_tokens}")
       

## Key concepts

- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=GEifsHDadBw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/08-user-feedback.md)
