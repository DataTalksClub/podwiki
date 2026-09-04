---
title: "The Agentic Loop — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=ePlQUcTPPjw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # The Agentic Loop"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › The Agentic Loop

## Notes

---
video_url: "https://www.youtube.com/watch?v=ePlQUcTPPjw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# The Agentic Loop

In the previous lesson, we did function calling by hand. We sent a
message and got back a function call. We ran it, sent the result back,
and got the answer.

That works for one function call. It breaks down when the model wants
to search several times, or when the first search misses the answer.
We don't know in advance how many calls the model will want. So we
need a loop that keeps calling the model and running tools until it's
done. An agent is exactly that.

## Anatomy of an agent

With the LLM in the driver's seat, we have an agent. It's an AI
assistant whose goal is to help the user.

An agent has three parts:

- Instructions, the role and behavior we want. We pass this as the
  `developer` message. The better the instructions, the better the
  agent helps.
- Tools, the functions the agent can call to carry out the task. For
  us that's only `search`.
- Memory, the message history. We append every prompt, every model
  output, and every tool result. The agent reads this to know what it
  has already tried.

Everything below is the code that wires these three together inside a
loop.

## A developer prompt

So far we've relied on the model to figure out when to search. We make
that more reliable with a `developer` message that spells out how to
behave. This is where we give the agent its role. The same message
also pushes it toward multiple searches, so we get to watch the loop
run more than once.

```python
instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches.

Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()
```

## A function-call helper

We'll be running function calls repeatedly inside the loop, so let's
wrap that in a small helper. It turns the JSON arguments into a Python
dict, calls the right function, and serializes the result. We only
have one tool for now, so we dispatch on the function name directly.

```python
def make_call(call):
    args = json.loads(call.arguments)

    if call.name == "search":
        result = search(**args)

    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }
```

The helper returns the exact structure the Responses API expects.
When we add more tools later, we'll extend this with more `if`
branches (or switch to a registry).

## Processing one response

Let's process a single model response. We append each output entry to
the conversation, print any messages, and run any function calls.
Function-call results get appended too.

```python
question = "I just discovered the course. Can I join it?"

messages = [
    {"role": "developer", "content": instructions},
    {"role": "user", "content": question},
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=[search_tool],
)

messages.extend(response.output)
has_function_calls = False

for item in response.output:
    if item.type == "function_call":
        print("function_call:", item.name, item.arguments)
        call_output = make_call(item)
        messages.append(call_output)
        has_function_calls = True

    elif item.type == "message":
        print("ASSISTANT:")
        print(item.content[0].text)
```

The `has_function_calls` flag tells us whether the model needs another
API call. If the response contains a function call, the updated
`messages` has tool output the model hasn't seen yet. We'll need to
send it back.

## The full agent loop

We wrap this in a `while` l

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [Function Calling](/course-wiki/function-calling/)
- [Agentic RAG](/course-wiki/agentic-rag/)
- [LangChain](/course-wiki/langchain/)
- [Prompt Engineering](/course-wiki/prompt-engineering/)

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
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
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

- [Video](https://www.youtube.com/watch?v=ePlQUcTPPjw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/14-agentic-loop.md)
