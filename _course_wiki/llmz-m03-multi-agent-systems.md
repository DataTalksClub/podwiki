---
title: "Multi-Agent Systems — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Multi-Agent Systems"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › Multi-Agent Systems

## Notes

---
video_url: "https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Multi-Agent Systems

For complex tasks, you can design systems where multiple specialized agents collaborate. Each agent has a clear responsibility, and one agent can call another as a tool.

The main benefits are separation of concerns (each agent focuses on one thing) and easier debugging (you can isolate issues to a specific agent).

## Example: Company Research

Flow: `6_multi_agent_research.yaml`

This flow demonstrates a two-agent system for competitor research:

| Agent | Specialization | Tools | Responsibility |
|-------|---------------|-------|----------------|
| Research Agent | Web research and data gathering | Tavily web search | Find factual, current information |
| Main Analyst Agent | Analysis and synthesis | Research agent (used as a tool) | Create structured reports |

How it works:

1. Input: company name (e.g., "kestra.io")
2. Main agent receives prompt: "Research this company"
3. Main agent calls the research agent tool: "Find information about kestra.io"
4. Research agent uses Tavily to gather data from the web
5. Research agent returns findings to the main agent
6. Main agent structures the findings into a final JSON output

The key pattern here is using `AIAgent` as a tool. The main agent treats the research agent exactly like a web search or database call — it invokes it when needed and works with whatever comes back.

## Best Practices

1. Define clear responsibilities: each agent should have a specific role and stay within it
2. Monitor token usage: multiple agents means multiple LLM calls — costs add up
3. Document agent purposes: make the system maintainable by describing what each agent does in your flow and task descriptions

## Key concepts

- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [Kestra](/course-wiki/kestra/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
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
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)

## Sources

- [Video](https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/07-multi-agent.md)
