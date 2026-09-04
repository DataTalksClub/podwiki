---
title: "AI Agents — LLM Zoomcamp Module 3"
summary: "--- video_url: 'https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # AI Agents"
related_course:
  - llmz-module-03
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 3: Orchestration](/course-wiki/llmz-module-03/) › AI Agents

## Notes

---
video_url: "https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# AI Agents

In Module 1 you built the agentic loop by hand: a `while` loop that called the LLM, executed any tool calls it returned, sent the results back, and stopped when the model produced a final answer with no more tool calls. That pattern is the foundation of every agent framework.

In Kestra, the `AIAgent` plugin handles that loop for you. You define the goal, the tools, and optionally a system message - Kestra drives the loop, manages conversation history, and surfaces the result as a task output.

> Note: The flows in this lesson use `{{ secret('GEMINI_API_KEY') }}`. Make sure you've completed the setup instructions to configure this secret before running them.

The example flows use Gemini, but the `provider` block supports any major AI provider — swap `io.kestra.plugin.ai.provider.GoogleGemini` for `OpenAI`, `Anthropic`, or others. See the [full list of supported providers](https://kestra.io/plugins/plugin-ai/provider).

Traditional Workflow — fixed sequence, predetermined logic:

```yaml
tasks:
  - id: step1
    type: Task1
  - id: step2
    type: Task2
  - id: step3
    type: Task3
```

AI Agent Workflow — agent decides what to do, in what order, based on the goal:

```yaml
tasks:
  - id: agent
    type: io.kestra.plugin.ai.agent.AIAgent
    prompt: "Research data engineering trends and create a report"
    tools:
      - WebSearch
      - TaskExecution
```

## When to Use AI Agents

Use AI Agents when the exact sequence of steps isn't known in advance, decisions depend on dynamic changing information, or you need to adapt to unexpected conditions.

Use traditional workflows when steps are deterministic and repeatable, compliance requires exact auditable processes, or cost and latency must be minimized.

## Anatomy of an AI Agent

```yaml
id: example_agent
namespace: zoomcamp

tasks:
  - id: agent
    type: io.kestra.plugin.ai.agent.AIAgent

    # Defines the agent's role and behavior
    systemMessage: |
      You are a data analyst. Analyze data and provide insights.

    # The actual task or question
    prompt: "What are the top 3 trends in this data?"

    # LLM provider configuration
    provider:
      type: io.kestra.plugin.ai.provider.GoogleGemini
      modelName: gemini-2.5-flash
      apiKey: "{{ secret('GEMINI_API_KEY') }}"

    # Tools the agent can use
    tools:
      - type: io.kestra.plugin.ai.tool.TavilyWebSearch
        apiKey: "{{ secret('TAVILY_API_KEY') }}"

    # Memory for context across executions
    memory:
      type: io.kestra.plugin.ai.memory.KestraKVStore
      memoryId: analyst_001
```

## Simple Agent Example

Flow: `4_simple_agent.yaml`

This flow demonstrates a basic AI agent that summarizes text with controllable length and language. It shows how to structure agent prompts, chain agent tasks, use `pluginDefaults` to avoid repetition, and track token usage for cost monitoring.

## Advanced Agent Example: Web Research

Flow: `5_web_research_agent.yaml`

This flow demonstrates an agent with autonomous tool usage:

1. Receives a research prompt (e.g., "Latest trends in workflow orchestration")
2. Decides to use the web search tool to gather information
3. Evaluates search results and determines if more searches are needed
4. Synthesizes findings into a structured markdown report
5. Saves the report to a file using the filesystem tool

The agent autonomously decides when to use tools, can loop (search → evaluate → search again) until satisfied, and you only specify the goal — not the exact steps.

## Agent Tools Available in Kestra

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `TavilyWebSearch` | Search the web for current information | Market research, news monitoring |
| `GoogleCustomWebSearch` | Search with Google Custom Search API | Google search |
| `CodeExecution` | Run code safely via Judge0 | Math calculations, data validation |
| `KestraTask` | Exe

## Key concepts

- [Agentic RAG](/course-wiki/agentic-rag/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/03-orchestration/06-agents.md)
