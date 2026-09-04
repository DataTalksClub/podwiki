---
title: "Setting up Kestra — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=ghkf93rfb2w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Setting up Kestra"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › Setting up Kestra

## Notes

---
video_url: "https://www.youtube.com/watch?v=ghkf93rfb2w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Setting up Kestra

Here's how to set up everything you need to run the example flows in this module.

## Prerequisites

This module requires [Docker](https://docs.docker.com/get-started/get-docker/) with Docker Compose to run Kestra locally. [Docker Desktop](https://www.docker.com/products/docker-desktop/) is the easiest way to get both on Mac and Windows. If you don't have Docker installed, set that up before proceeding.

## Step 1: Start Kestra

This module includes a `docker-compose.yml` with Kestra pre-configured:

```bash
cd 03-orchestration
docker compose up -d
```

Once the container starts, access the Kestra UI at http://localhost:8080.

To shut down Kestra:

```bash
docker compose down
```

## Step 2: Obtain API Keys

**Gemini API Key (Required)**

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" and copy your key

The free tier is sufficient for light use, but rate limits are relatively low — you may hit quota quickly if you run the agent and multi-agent flows repeatedly. If you run into `429 Resource Exhausted` errors, wait a minute before retrying, or consider upgrading to a paid tier.

**OpenAI API Key (Required for flow 3)**

1. Visit [platform.openai.com](https://platform.openai.com/home) and sign in or create an account
2. Go to **API keys** and create a new key

**Tavily API Key (Required for web search: flows 3, 5, and 6)**

1. Visit [Tavily](https://tavily.com/)
2. Sign up for the free tier
3. Get your API key from the dashboard

The free tier includes 1,000 searches/month.

## Step 3: Configure API Keys in Kestra

Kestra reads secrets from environment variables prefixed with `SECRET_` where the value is base64-encoded. Export your keys before starting Kestra:

```bash
export GEMINI_API_KEY="your-gemini-api-key-here" # required
export SECRET_GEMINI_API_KEY=$(echo -n $GEMINI_API_KEY | base64) # required
export SECRET_OPENAI_API_KEY=$(echo -n "your-openai-api-key-here" | base64)   # required for flow 3
export SECRET_TAVILY_API_KEY=$(echo -n "your-tavily-api-key-here" | base64)   # optional
```

Then start (or restart) Kestra:

```bash
docker compose up -d
```

In flows, reference secrets with `{{ secret('GEMINI_API_KEY') }}` — omit the `SECRET_` prefix when calling `secret()`.

> [!WARNING]
> Never commit API keys to Git!

## Step 4: Import Example Flows

```bash
cd 03-orchestration

# Adjust username and password to match your Kestra setup
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/1_chat_without_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/2_chat_with_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/3_rag_with_websearch.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/4_simple_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/5_web_research_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/6_multi_agent_research.yaml
```

Alternatively, copy-paste the flow YAML directly into Kestra's UI.

## Step 5: Run Your First Agent

1. Open Kestra UI at http://localhost:8080
2. Navigate to the `zoomcamp` namespace
3. Find the `4_simple_agent` flow and click "Execute"
4. Leave default inputs or customize them
5. Watch the execution and review the outputs
6. Then run `5_web_research_agent` and `6_multi_agent_research` and analyze the logs and outputs

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [Docker](/course-wiki/docker/)
- [Kestra](/course-wiki/kestra/)

## Related notes

- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=ghkf93rfb2w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/03-setup.md)
