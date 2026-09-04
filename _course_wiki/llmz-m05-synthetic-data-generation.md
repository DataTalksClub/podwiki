---
title: "Synthetic Data Generation — LLM Zoomcamp Module 5"
summary: "A fresh dashboard with three conversations in it doesn't show much. You
could keep asking the app questions until there's enough to chart, but
that's slow and dull. Instead we write a small script that pumps fake
conversations into Postgres. Then we "
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Synthetic Data Generation

## Notes

# Synthetic Data Generation

_This lesson has no video._

A fresh dashboard with three conversations in it doesn't show much. You
could keep asking the app questions until there's enough to chart, but
that's slow and dull. Instead we write a small script that pumps fake
conversations into Postgres. Then we can see how the dashboard behaves
with real volume.

The script inserts a new conversation every second until we stop it. That
also lets us watch Grafana update in close to real time.

## Sample data

Create `generate_data.py`.

Imports and sample data:

```python
import time
import random

from metrics import LLMCallRecord
from db_save import save_conversation
from db_feedback import save_feedback
```

Sample data:

```python
SAMPLE_QUESTIONS = [
    "How do I install Docker?",
    "Can I still join the course?",
    "What are the prerequisites?",
    "How do I submit homework?",
    "When are the office hours?",
]

SAMPLE_ANSWERS = [
    "You can install Docker by downloading Docker Desktop from the official website.",
    "Yes, you can join at any time. The materials remain available.",
    "You need basic Python knowledge and familiarity with the command line.",
    "Submit your homework through the course portal before the deadline.",
    "Office hours are held weekly. Check the calendar for details.",
]

RELEVANCE = ["RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"]
```

## Generating conversations

A helper to create a fake `LLMCallRecord`:

```python
def fake_record(question, answer):
    return LLMCallRecord(
        model="gpt-5.4-mini",
        prompt=question,
        instructions="",
        answer=answer,
        prompt_tokens=random.randint(50, 200),
        completion_tokens=random.randint(50, 300),
        total_tokens=random.randint(100, 500),
        response_time=random.uniform(0.5, 5.0),
        cost=random.uniform(0.0001, 0.01),
    )
```

## Generating one conversation

A helper to randomly pick a thumbs up or down.

We put more 1s than -1s to simulate that most users are happy with the answers:

```python
def random_score():
    return random.choice([1, 1, 1, 1, -1])
```

A function that generates a single conversation with optional feedback:

```python
def generate_one():
    question = random.choice(SAMPLE_QUESTIONS)
    answer = random.choice(SAMPLE_ANSWERS)
    record = fake_record(question, answer)

    conversation_id = save_conversation(
        record, question, "llm-zoomcamp"
    )

    if random.random() < 0.7:
        relevance = random.choice(RELEVANCE)
        save_feedback(
            conversation_id, "judge",
            relevance=relevance,
            explanation=f"Answer is {relevance.lower()}.",
        )

    if random.random() < 0.5:
        score = random_score()
        save_feedback(conversation_id, "user", score=score)
```

## Live data

Keep inserting new conversations every second:

```python
def generate_live():
    print("Starting live data generation (Ctrl+C to stop)...", flush=True)
    while True:
        generate_one()
        time.sleep(1)
```

## Running it

The entry point:

```python
if __name__ == "__main__":
    try:
        generate_live()
    except KeyboardInterrupt:
        print("Stopped.")
```

Run it:

```bash
uv run python generate_data.py
```

The script keeps generating live data every second. We'll use this data
in Grafana in the next lesson. The dashboard will come alive with charts
updating in real time.

## Key concepts

- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)

## Related notes

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
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/11-synthetic-data.md)
