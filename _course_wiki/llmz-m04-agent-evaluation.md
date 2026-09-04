---
title: "Agent Evaluation — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=2SW86BehVdI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Agent Evaluation"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Agent Evaluation

## Notes

---
video_url: "https://www.youtube.com/watch?v=2SW86BehVdI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Agent Evaluation

For RAG, we used the A->Q->A' setup:

- A = original answer in the FAQ
- Q = generated question from this answer
- A' = answer produced by our RAG system

For agents, we use the same setup. A' comes from an agent instead of a
fixed RAG pipeline.

We also save the trajectory. Here, the trajectory means only the tool
calls the agent made before producing the final answer.

## Loading the data

Use the same ground truth questions:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground_truth-new.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Load the FAQ documents and the search index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()

documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

documents = documents_llm
index = build_index(documents)
```

Create a lookup table:

```python
doc_idx = {}

for doc in documents:
    doc_idx[doc["id"]] = doc
```

## Running the agent

Reuse the ToyAIKit agent from module 01. It handles the agent loop and
stores the full message history.

First, set up the model clients:

```python
from dotenv import load_dotenv
from openai import OpenAI
from toyaikit.llm import OpenAIClient

load_dotenv()
openai_client = OpenAI()
```

Define the search tool:

```python
def search(query: str) -> list[dict]:
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={"question": 1.0, "answer": 2.0, "section": 0.1},
        filter_dict={"course": "llm-zoomcamp"}
    )
```

Create the runner:

```python
from toyaikit.tools import Tools
from toyaikit.chat.runners import OpenAIResponsesRunner

agent_tools = Tools()
agent_tools.add_tool(search)

instructions = """
You're a course teaching assistant. Answer student questions based on
the FAQ search results. Use the search tool before answering.
""".strip()

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=instructions,
    llm_client=OpenAIClient(model="gpt-5.4-mini")
)
```

The result contains:

- `last_message`: the final response
- `all_messages`: the full message history
- `cost`: the cost of all LLM calls in this run

Run it for one ground truth question:

```python
rec = ground_truth[0]

result = runner.loop(prompt=rec["question"])
```

Look at the full message history:

```python
result.all_messages
```

For this lesson, the trajectory is only the tool calls. We don't need
to send the full message history to the judge.

Extract the function name and arguments:

```python
def extract_tool_calls(messages):
    tool_calls = []

    for message in messages:
        if isinstance(message, dict):
            continue

        if message.type == "function_call":
            tool_calls.append({
                "name": message.name,
                "arguments": message.arguments,
            })

    return tool_calls
```

For this example:

```python
tool_calls = extract_tool_calls(result.all_messages)

tool_calls
```

You should see something like this:

```python
[
    {
        "name": "search",
        "arguments": "{\"query\":\"own pace certificate at the end self-paced course certificate\"}"
    }
]
```

Get the original answer:

```python
doc_id = rec["document"]
original_doc = doc_idx[doc_id]
answer_orig = original_doc["answer"]
```

Save the A->Q->A' record and the trajectory:

```python
agent_result = {
    "question": rec["question"],
    "answer_agent": result.last_message,
    "answer_orig": answer_orig,
    "tool_calls": json.dumps(tool_calls),
    "cost": result.cost.total_cost,
    "document": doc_id,
}

agent_result
```

The `answer_agent` field is what we evaluate with the LLM judge. The
`tool_calls` field lets the judge see how the agent got there. 
Wrap `tool_

## Key concepts

- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=2SW86BehVdI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/14-agent-evaluation.md)
