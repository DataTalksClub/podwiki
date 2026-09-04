---
title: "Context Engineering — LLM Zoomcamp Module 3"
summary: "---
video_url: "https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Context Engineering"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › Context Engineering

## Notes

---
video_url: "https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Context Engineering

Let's start by seeing what happens when AI lacks proper context.

## Experiment: ChatGPT Without Context

1. Open ChatGPT in a private browser window (to avoid any existing chat context)

2. Enter this prompt:
   ```
   Create a Kestra flow that loads NYC taxi data from a CSV file to BigQuery. The flow should extract data, upload to GCS, and load to BigQuery.
   ```

3. Observe the results. ChatGPT will generate a Kestra flow, but it likely contains:
   - Outdated plugin syntax (e.g., old task types that have been renamed)
   - Incorrect property names (e.g., properties that don't exist in current versions)
   - Hallucinated features (e.g., tasks, triggers, or properties that never existed)

## Why Does This Happen?

Large Language Models like GPT are trained on data up to a specific point in time. They don't automatically know about software updates and new releases, renamed plugins or changed APIs, new best practices in your organisation, or specific configurations for your infrastructure.

This is the fundamental challenge of using AI: the model can only work with information it has access to.

## Context is Everything

Without proper context, generic AI assistants hallucinate outdated or incorrect code that you can't trust for production use. With proper context, AI generates accurate, current, production-ready code you can iterate on quickly. The same principle applies whether you're generating flows or answering questions from your own data.

In the next section, we'll see how Kestra's AI Copilot solves this problem by giving the model everything it needs to generate correct flows.

## Key concepts

- [Context Engineering](/course-wiki/context-engineering/)

## Related notes

- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)

## Sources

- [Video](https://www.youtube.com/watch?v=xUAkcgNIcRI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/02-context-engineering.md)
