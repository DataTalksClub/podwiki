---
title: "AI Copilot — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=OTiOdt17hZg&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # AI Copilot"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › AI Copilot

## Notes

---
video_url: "https://www.youtube.com/watch?v=OTiOdt17hZg&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# AI Copilot

Building workflows manually can be slow. You need to know which plugin to use, look up the exact property names, remember the right syntax, and connect each task together in the correct order. For a non-trivial flow, this can take a long time before you even run it once. While Kestra's autocomplete helps, you still have to build each task one at a time.

AI Copilot changes the approach. Instead of building each step manually, you describe your inputs and your goal — and the AI Copilot generates the flow structure for you. You then tweak the last 5% to get the exact behaviour you want. The AI Copilot handles the boilerplate; you focus on the logic that's specific to your use case.

This works reliably because Kestra's AI Copilot is grounded in the current plugin documentation, valid property names, and best practices for your running version of Kestra — unlike a generic AI assistant, which guesses.

## Setup

> Note: In Kestra's Open Source edition, the AI Copilot only supports Gemini as its AI provider.

Before using AI Copilot, you need to configure Gemini API access in your Kestra instance. If you haven't done this yet, follow the setup instructions to obtain your Gemini API key and configure it as a secret.

Access AI Copilot:

1. Open Kestra UI at http://localhost:8080
2. Create a new flow or open an existing one
3. Click the AI Copilot button (sparkle icon ✨) in the top-right corner of the Flow Editor

## Hands-On: Compare Copilot vs. Raw ChatGPT

Use the same prompt from the previous lesson, but this time with AI Copilot:

1. Click the AI Copilot button in Kestra's Flow Editor
2. Enter:
   ```
   Create a Kestra flow that loads NYC taxi data from a CSV file to BigQuery. The flow should extract data, upload to GCS, and load to BigQuery.
   ```
3. Observe the results — correct, up-to-date plugin types, valid property names, and working executable YAML.

## The 5% Rule

Copilot gets you to a working flow quickly, but it won't know everything about your environment. After generation, review the output and make the small adjustments that are specific to your setup - your environment variables, your secrets, your error handling preferences, or a task that needs a slightly different configuration than the default.

The bulk of the structure is done. You're just closing the gap between a general solution and your exact requirements.

## Iterative Refinement

AI Copilot helps with both creating new flows and refining existing ones. The conversation is cumulative — each follow-up preserves the existing flow structure and only modifies what's needed.

Example conversation:

1. "Create a flow that downloads a CSV file and loads it to BigQuery" → Copilot generates a basic flow
2. "Add a task that checks data quality in BigQuery" → Copilot adds SQL validation tasks
3. "Schedule the flow to run daily at 9 AM UTC" → Copilot adds a `Schedule` trigger
4. "Send a Slack notification if it fails" → Copilot adds a `SlackIncomingWebhook` task in an `errors` branch

Then you make the final tweaks manually - adjusting the SQL query, setting your specific Slack channel, or adding a retry count that matches your SLA. You're collaborating with AI, not starting from scratch each time.

## Example Use Cases

- Generate new flows: "Create a flow that syncs data from Postgres to GCS"
- Add tasks: "Add an If-task performing conditional branching"
- Configure triggers: "Add a webhook trigger"
- Add error handling: "Add retry logic with exponential backoff"

## Alternative: Agent Skills

If you're using an AI coding assistant (such as Claude or Cursor), Kestra's [agent-skills](https://github.com/kestra-io/agent-skills) repository gives your AI assistant the same grounding that AI Copilot has inside the UI — current plugin documentation, valid property names, and best practices. This means you can generate reliable, correct Kestra flows di

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [PostgreSQL](/course-wiki/postgresql/)
- [Agent Skills and Subagents](/course-wiki/agent-skills-and-subagents/)
- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [BigQuery](/course-wiki/bigquery/)
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
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=OTiOdt17hZg&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/04-ai-copilot.md)
