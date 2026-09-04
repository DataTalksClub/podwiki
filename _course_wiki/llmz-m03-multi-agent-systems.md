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

_No glossary concepts detected in this lesson._

## Related notes

- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)

## Sources

- [Video](https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/07-multi-agent.md)
