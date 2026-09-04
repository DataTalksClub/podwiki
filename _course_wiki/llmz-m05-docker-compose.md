---
title: "Docker Compose — LLM Zoomcamp Module 5"
summary: "By now we have three pieces running - PostgreSQL, Grafana, and the Streamlit app. Starting each by hand works, but it adds up. You have to remember the network and type out long commands. Next time around, Docker complains that a container..."
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Docker Compose

## Notes

# Docker Compose

_This lesson has no video._

By now we have three pieces running - PostgreSQL, Grafana, and the
Streamlit app. Starting each by hand works, but it adds up. You have to
remember the network and type out long commands. Next time around, Docker
complains that a container with that name already exists, and you have to
go remove it.

Docker Compose describes all three services in one file and starts them
together on a shared network. You run one command instead.

## Project structure

The project layout:

```text
code/
├── docker-compose.yaml
├── Dockerfile
├── .env
├── pyproject.toml
├── uv.lock
├── .python-version
├── app.py           # Streamlit app
├── assistant.py     # RAG pipeline + LLM
├── db_init.py       # Database init
├── db_save.py       # Save conversations
└── dashboard.py     # Streamlit dashboard
```

## Dockerfile

The Streamlit app needs its own container:

```dockerfile
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Environment variables

The `.env` file stores configuration:

```text
POSTGRES_DB=course_assistant
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres
OPENAI_API_KEY=your-key-here
```

## Docker Compose

The Compose file defines all three services on the same network:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:17
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - postgres
```

The Streamlit service is built from the Dockerfile:

```yaml
  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8501:8501"
    depends_on:
      - postgres

volumes:
  postgres_data:
  grafana_data:
```

## Starting everything

Start all services:

```bash
docker-compose up
```

Initialize the database:

```bash
uv run python db_init.py
```

Access the app at `http://localhost:8501` and Grafana at
`http://localhost:3000` (login: admin / admin).

To stop:

```bash
docker-compose down
```

The data in PostgreSQL and Grafana persists across restarts thanks to
Docker volumes.

## Key concepts

- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)

## Related notes

- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
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

- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/13-docker-compose.md)
