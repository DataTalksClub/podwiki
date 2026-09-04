---
title: "Storing Data in PostgreSQL — LLM Zoomcamp Module 5"
summary: "--- video_url: 'https://www.youtube.com/watch?v=iXRu_AbMtuU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Storing Data in PostgreSQL"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Storing Data in PostgreSQL

## Notes

---
video_url: "https://www.youtube.com/watch?v=iXRu_AbMtuU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Storing Data in PostgreSQL

The metrics disappear when we close the app, so we need somewhere to
keep them. We store every conversation in PostgreSQL, which we run only
for monitoring. No other part of the system touches this database. We
pick Postgres for two reasons: it handles structured data well, and
Grafana connects to it easily later on.

## Starting PostgreSQL with Docker

First we create a Docker network. Postgres and Grafana both run in
containers, and Grafana reaches Postgres by name, so they need to share
a network.

Create the network:

```bash
docker network create monitoring
```

Start PostgreSQL with a volume for data persistence and connect it to
the network:

```bash
docker run -it \
    --name course-assistant-pg \
    --network monitoring \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=course_assistant \
    -p 5432:5432 \
    -v pgdata:/var/lib/postgresql/data \
    postgres:17
```

If the commands feel opaque, paste them into ChatGPT and ask it to walk
you through each flag. The first module of our
[data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
goes deeper into Docker if you want the longer version.

These are long commands we'll run again and again, so they go in the
`Makefile` from lesson 02. The `postgres` target depends on `network`,
so `make postgres` creates the network first and then starts the
container.

Add these targets:

```makefile
network:
	docker network create monitoring

postgres: network
	docker run -it \
		--name course-assistant-pg \
		--network monitoring \
		-e POSTGRES_USER=user \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_DB=course_assistant \
		-p 5432:5432 \
		-v pgdata:/var/lib/postgresql/data \
		postgres:17
```

Now we can just run:

```bash
make postgres
```

To reach Postgres from Python, we install the `psycopg` driver:

```bash
uv add "psycopg[binary]"
```

## Initializing the database

The table stores everything from our `LLMCallRecord`, plus the question
and the course. I call it `conversations`, which isn't the best name. I
carried it over from materials I recorded a couple of years ago.
Something like `llm_call_records` would describe it better, but the name
stuck. Name yours however you like.

Two fields are worth a word. We store the `course` because the same
assistant can serve more than one course. Right now everything is
`llm-zoomcamp`, but keeping the column means we don't have to reshape the
table when we add others. The `timestamp` is timezone-aware
(`TIMESTAMP WITH TIME ZONE`) on purpose. Without the time zone, Grafana
won't line the data up correctly on its time axis later.

The SQL to create the table:

```sql
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    course TEXT NOT NULL,
    model TEXT NOT NULL,
    instructions TEXT NOT NULL,
    prompt TEXT NOT NULL,
    prompt_tokens INTEGER NOT NULL,
    completion_tokens INTEGER NOT NULL,
    total_tokens INTEGER NOT NULL,
    response_time FLOAT NOT NULL,
    cost FLOAT NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
)
```

We can run this via `psql` or any other tool, but let's create a
Python script.

Create `db_init.py`.

Imports:

```python
import os
import psycopg
from datetime import datetime

DB_TIMEZONE = datetime.now().astimezone().tzinfo
print(f"Using timezone: {DB_TIMEZONE}")
```

A helper to connect to the database.

It uses environment variables with defaults matching the Docker
container we just started:

```python
def get_db_connection():
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB", "course_assistant"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
    )
```

The init function creates the table. 

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
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=iXRu_AbMtuU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/05-database.md)
