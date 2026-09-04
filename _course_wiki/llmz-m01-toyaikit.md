---
title: "ToyAIKit — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=PQpQOR3Un3w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # ToyAIKit"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › ToyAIKit

## Notes

---
video_url: "https://www.youtube.com/watch?v=PQpQOR3Un3w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# ToyAIKit

The handwritten agent loop from the previous lesson is educational but
repetitive. Every time you build a new agent, you'd write the same
while-loop, the same function-call handling, the same message
management.

ToyAIKit wraps this pattern so you can focus on tools, prompts, and
behavior. We built it together in a DataTalks.Club workshop a while
back. It does the same thing as our handwritten loop with less
boilerplate. If you open its `runners` code, you'll find the same
`while True` loop we wrote by hand.

I use it here on purpose, because I don't want to pick a winner among
the production frameworks. ToyAIKit is small and easy to read, so when
something breaks you can see exactly what happened. That makes it handy
for developing and debugging locally before you go to production.

One caveat. ToyAIKit is a teaching and experimentation library, and it
is NOT meant for production use. We use it because it's minimal and you
can see what it does.

## Setup

Install it:

```bash
uv add toyaikit
```

Import the classes we need:

```python
from toyaikit.llm import OpenAIClient
from toyaikit.tools import Tools
from toyaikit.chat import IPythonChatInterface
from toyaikit.chat.runners import OpenAIResponsesRunner, DisplayingRunnerCallback
```

## Registering the tool

We register our `search` function along with the schema from earlier
lessons:

```python
agent_tools = Tools()
agent_tools.add_tool(search, search_tool)
```

## Letting ToyAIKit generate the schema

Writing that schema by hand is annoying, and we don't want to do it
for every function. So we don't have to.

If we add a type hint and a docstring to `search`, ToyAIKit reads them
and derives the schema for us:

```python
def search(query: str) -> dict[str, str]:
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={"question": 3.0, "section": 0.5},
        filter_dict={"course": "llm-zoomcamp"}
    )
```

Then register it without passing a schema:

```python
agent_tools = Tools()
agent_tools.add_tool(search)
```

You can look at what ToyAIKit produced.

```python
agent_tools.get_tools()
```

The output is the same JSON schema we hand-wrote in the function
calling lesson. ToyAIKit generated it from the docstring and the type
hint.

Every modern agent framework does this same trick. It reads a typed
Python function with a docstring and builds the schema from it. The
OpenAI Agents SDK, PydanticAI, LangChain and Google ADK all work this
way. You write the tool and the framework figures out how to describe
it.

## The chat interface and runner

Create the chat interface and a callback, then build the runner:

```python
chat_interface = IPythonChatInterface()
callback = DisplayingRunnerCallback(chat_interface)

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=instructions,
    chat_interface=chat_interface,
    llm_client=OpenAIClient(model="gpt-5.4-mini")
)
```

The `chat_interface` handles display in the notebook. The `callback`
renders model messages and tool calls as they happen. The runner runs
the agent loop, the same `while True` we wrote by hand. It sends
messages, executes function calls, adds tool outputs back, and repeats
until the model is done.

We pick `gpt-5.4-mini` here on purpose. Without it, ToyAIKit falls
back to a smaller, faster default that doesn't follow the instructions
as reliably.

## Running one prompt

Run a single prompt:

```python
result = runner.loop(
    prompt="How do I run Olama locally?",
    callback=callback,
)
```

We used the typo "Olama" on purpose. The agent searches and gets poor
results, then retries with "Ollama". The recovery is the same as the
handwritten loop. The notebook output is nicer to watch. Each tool
call and message renders inline, so you can look at every search
result.



## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [LangChain](/course-wiki/langchain/)
- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

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
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
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
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=PQpQOR3Un3w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/15-frameworks.md)
