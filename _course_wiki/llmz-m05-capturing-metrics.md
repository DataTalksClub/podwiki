---
title: "Capturing Metrics — LLM Zoomcamp Module 5"
summary: "---
video_url: "https://www.youtube.com/watch?v=JGh6-DqaueA&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Capturing Metrics"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Capturing Metrics

## Notes

---
video_url: "https://www.youtube.com/watch?v=JGh6-DqaueA&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Capturing Metrics

Our chat app works, but every call is a black box. We don't know how
long it took, how many tokens it used, or what it cost. To monitor the
system, we first have to capture those numbers as they happen. So we
instrument the RAG pipeline.

Create `metrics.py`.

Imports:

```python
import time
from dataclasses import dataclass, field
from datetime import datetime

from rag_helper import RAGBase
```

Every call produces a bundle of values we want to keep together. We
could pass them around as a dictionary, but then you have to remember
what keys are in it. A dataclass spells the fields out, so anyone reading
the code can see what we record for each call.

The `LLMCallRecord` dataclass:

```python
@dataclass
class LLMCallRecord:
    model: str
    prompt: str
    instructions: str
    answer: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    response_time: float
    cost: float
    timestamp: datetime = field(default_factory=datetime.now)
```

## Cost calculation

Next we need the cost of each call. The provider charges a price per
million input tokens and another per million output tokens. So we
multiply each count by its rate and divide by a million. The `usage`
object comes straight from the LLM response. It carries the token counts
for the call we just made.

```python
def calculate_cost(model, usage):
    cost = 0
    if "gpt-5.4-mini" in model:
        cost = (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000
    return cost
```

I keep copy-pasting a version of this function across modules, which
isn't the tidiest thing in the world. For a real project you'd pull it
into one shared place, but here it keeps each lesson self-contained.

## Instrumented RAG

`RAGBase` already works, and I like carrying it around as-is because it
keeps things simple. So instead of rewriting it, we subclass it and only
change the one method that calls the LLM. Everything else stays the same,
and every time `rag()` makes a call, the metrics get recorded for free.

The same trick works for agents. You'd capture each tool call the same
way we captured LLM calls in the evaluation module.

Also in `metrics.py`, the subclass that captures metrics:

```python
class RAGWithMetrics(RAGBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_call: LLMCallRecord = None

    def llm(self, prompt):
        start_time = time.time()
        response = self._call_llm(prompt)
        response_time = time.time() - start_time
        self._log_response(prompt, response, response_time)
        return response.output_text
```

The `_call_llm` method sends the request to the LLM:

```python
    def _call_llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]
        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )
        return response
```

The `_log_response` method builds the record and stashes it on
`self.last_call`. Keeping state on the object isn't the cleanest design.
If two things called it at once, they'd fight over `last_call`.

But it lets us read the metrics back without changing the method's return
type. For one person clicking through a Streamlit app, that's good
enough. We also print the record so we can see what we're capturing.

The `_log_response` method captures all the metrics:

```python
    def _log_response(self, prompt, response, response_time):
        usage = response.usage
        cost = calculate_cost(self.model, usage)

        call_record = LLMCallRecord(
            model=self.model,
            prompt=prompt,
            instructions=self.instructions,
            answer=response.output_text,
            prompt_tokens=usage.input_tok

## Key concepts

- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
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
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
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

- [Video](https://www.youtube.com/watch?v=JGh6-DqaueA&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/04-metrics.md)
