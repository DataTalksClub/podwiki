---
title: "Retrieval Augmented Generation — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=FhGZV173xrk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Retrieval Augmented Generation"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › Retrieval Augmented Generation

## Notes

---
video_url: "https://www.youtube.com/watch?v=FhGZV173xrk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Retrieval Augmented Generation

AI Copilot solves the context problem for flow generation. But what about workflows that need to answer questions from your own data? That's where RAG comes in.

> Note: Flows 1 and 2 use `{{ secret('GEMINI_API_KEY') }}`. Flow 3 uses `{{ secret('OPENAI_API_KEY') }}` and `{{ secret('TAVILY_API_KEY') }}`. Make sure you've completed the setup instructions to configure the relevant secrets before running them.

## What is RAG?

RAG (Retrieval Augmented Generation) is a technique that retrieves relevant information from your data sources, augments the AI prompt with that context, and generates a response grounded in real data. This solves the hallucination problem by ensuring the AI has access to current, accurate information at query time.

For a deeper dive into RAG concepts, see Module 1: Intro to RAG. For vector search, see Module 2: Vector Search.

## How RAG Works in Kestra

RAG has two phases. In the demo flows below they run back-to-back, but in production you'd typically schedule them separately — ingest on a cadence, query on demand.

```mermaid
graph LR
    subgraph Ingest ["Ingest (run once / on schedule)"]
        A[Fetch Docs] --> B[Create Embeddings]
        B --> C[Store in KV Store]
    end
    subgraph Query ["Query (run on demand)"]
        D[User Question] --> E[Find Similar Content]
        E --> F[Add Context to Prompt]
        F --> G[LLM Answer]
    end
    C --> E
```

Ingest phase (run once, or on a schedule when your data changes):

1. Fetch documents: load documentation, release notes, or other data sources
2. Create embeddings: convert text into vectors using an embedding model
3. Store embeddings: save vectors in Kestra's KV Store

> Note: The flows store embeddings in Kestra's KV Store for simplicity. This is convenient for learning and small-scale demos, but it is not a replacement for a proper vector database. For any serious workload, e.g. larger document sets, low-latency retrieval, or production use, you should use a dedicated vector store. See Module 2: Vector Search for a deeper look at vector search in practice.

Query phase (runs every time a question is asked):

4. Retrieve context: find the embeddings most similar to the user's question
5. Augment the prompt: add the retrieved content to the LLM prompt
6. Generate response: the LLM answers using real, grounded context

## Example: Kestra Release Features

### Step 1: Without RAG

Flow: `1_chat_without_rag.yaml`

This flow asks Gemini: "Which features were released in Kestra 1.1?"

Without RAG, the model might hallucinate features that don't exist, provide outdated information, or give vague generic answers.

Import and run this flow, then check the output — the response won't be accurate.

### Step 2: With RAG

Flow: `2_chat_with_rag.yaml`

This flow:

1. Ingests the Kestra 1.1 release blog post from GitHub
2. Creates embeddings using Gemini's embedding model
3. Stores embeddings in Kestra's KV Store
4. Asks the LLM the same question with RAG enabled
5. Returns an accurate response with real features from that release

Import and run `2_chat_with_rag.yaml` and compare the output quality against the previous flow.

## Extending RAG with web search

The examples above use static RAG — documents are ingested once and stored in the KV Store. Kestra also supports web search as a retriever, which fetches live results at query time and passes them as context to the LLM.

Flow: `3_rag_with_websearch.yaml`

> Note: This flow uses OpenAI as its AI provider. To run it, you'll need an OpenAI API key:
>
> 1. Visit [platform.openai.com](https://platform.openai.com/home) and sign in or create an account
> 2. Go to API keys and create a new key
> 3. Export it as a secret before starting Kestra:
>    ```bash
>    export SECRET_OPENAI_API_KEY=$(echo -n "your-openai-api-key-here" | base64)
>    docker compose up -d
>    ``

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [RAG](/course-wiki/rag/)
- [Docker](/course-wiki/docker/)
- [Vector Search](/course-wiki/vector-search/)
- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [Embeddings](/course-wiki/embeddings/)
- [Kestra](/course-wiki/kestra/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
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
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=FhGZV173xrk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/05-rag.md)
