---
title: "The LLM — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=KHePGkeFn54&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' code: - label: 'notebook.ipynb' path: 'code/notebook.ipynb' --- # The LLM"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › The LLM

## Notes

---
video_url: "https://www.youtube.com/watch?v=KHePGkeFn54&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
code:
  - label: "notebook.ipynb"
    path: "code/notebook.ipynb"
---
# The LLM

The last component of our RAG pipeline is the LLM. It takes
the prompt we built and generates an answer.

## Sending the prompt to the LLM

We have the prompt from the previous section.

We send it to the
LLM:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=prompt
)
```

We use OpenAI's Responses API (`openai_client.responses.create`). OpenAI
has two APIs: chat completions and responses. Chat completions is the
older one, and it's now considered legacy. When the first edition of
this course started, the Responses API didn't exist, so we used chat
completions. Now we prefer responses because it's more convenient.

There's a catch worth knowing. Many other providers like Groq and
Gemini give you an OpenAI-compatible client. But they expose chat
completions, not responses. So if you switch providers, you keep the
OpenAI client but call `chat.completions` instead of `responses`.

## Exploring the response

The response is a Pydantic object. The answer is in `response.output` -
a list of output items.

The first one is the message:

```python
response.output[0]
```

The message has a `content` list, and the text is in the first item:

```python
response.output[0].content[0].text
```

That's quite a journey to reach one string.

The shortcut spares us all of it:

```python
response.output_text
```

Same result, less code. The answer should be something like: "Yes, you
can still join. If you want to receive a certificate, make sure to
submit your project while submissions are still open."

The usage counts tell you how many tokens the request consumed:

```python
response.usage
```

You'll see something like:

```text
ResponseUsage(input_tokens=334, output_tokens=39, total_tokens=373)
```

## Calculating the price

You can use different models.

In this course we'll use
[gpt-5.4-mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini):

- Input: $0.75 per million tokens
- Output: $4.50 per million tokens

Let's calculate the cost of the request we just made:

```python
input_price = 0.75 / 1_000_000
output_price = 4.50 / 1_000_000

cost = (
    response.usage.input_tokens * input_price +
    response.usage.output_tokens * output_price
)

cost
```

This particular request costs a fraction of a cent. Even a full RAG
query with a long prompt stays under $0.01. We need to send a lot of
queries to even spend one cent. These models are cheap to play with.

The usage object also reports cached input tokens. Those are billed at
a lower rate when the same prompt prefix repeats.

## Message history

Previously we sent only one string as input and got back a response.
In practice, you typically send a message history - a list of messages
where each message has a role.

Think of a ChatGPT conversation. It starts with a hidden system prompt
that tells the LLM how to behave, one you never see. After that, your
messages and the LLM's replies alternate. The LLM has no memory of its
own, so it needs the full history passed in to continue the
conversation.

We won't build a multi-turn chat here. But we still use this message
format to separate our instructions from the user prompt.

We send two messages:

- `developer` - system-level instructions (how the LLM should behave)
- `user` - the actual prompt with the question and context

```python
message_history = [
    {"role": "developer", "content": INSTRUCTIONS},
    {"role": "user", "content": prompt}
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=message_history
)
```

This separates the fixed instructions from the user prompt, which
changes every request.

OpenAI accepts both `developer` and `system` for the instruction role.
There may be some difference between them, but in practice I don't see
it change the result either way. We use 

## Key concepts

- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)

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
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
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
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
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

- [Video](https://www.youtube.com/watch?v=KHePGkeFn54&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/07-llm.md)
