---
title: "The Course FAQ Dataset — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=Mx6EqvzVDz0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' code: - label: 'notebook.ipynb' path: 'code/notebook.ipynb' --- # The Course FAQ Dataset"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › The Course FAQ Dataset

## Notes

---
video_url: "https://www.youtube.com/watch?v=Mx6EqvzVDz0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
code:
  - label: "notebook.ipynb"
    path: "code/notebook.ipynb"
---
# The Course FAQ Dataset

Before we build the RAG pipeline, let's get familiar with the data
we'll use as our knowledge base.

We run these courses every year, and students keep asking the same
questions in Slack. We collected those into an FAQ so people can find
answers before asking. Some courses have run for five cohorts, so the
FAQ grows large and searching it by hand gets tedious. That's exactly
the problem our RAG system will solve.

The FAQ data is available as JSON from the DataTalks.Club website. I
maintain that site, so I made the data available at a JSON endpoint we
can fetch directly.

Let's fetch it:

```python
import requests

docs_url = "https://datatalks.club/faq/json/courses.json"
response = requests.get(docs_url)
courses_raw = response.json()
```

This returns a list of courses. Each course has a `path` field that
points to its FAQ data.

Let's fetch all the FAQ documents from all
courses:

```python
documents = []
url_prefix = "https://datatalks.club/faq"

for course in courses_raw:
    course_url = f"""{url_prefix}{course["path"]}"""

    course_response = requests.get(course_url)
    course_response.raise_for_status()
    course_data = course_response.json()

    documents.extend(course_data)

len(documents)
```

Each entry has:

- `id` - unique identifier
- `course` - course slug (e.g., `machine-learning-zoomcamp`)
- `section` - which section of the course
- `question` - the FAQ question
- `answer` - the FAQ answer

Let's look at one:

```python
documents[0]
```

You should see something like:

```python
{
    "id": "0e38656cfb",
    "course": "machine-learning-zoomcamp",
    "section": "General Course-Related Questions",
    "question": "How do I submit homework?",
    "answer": "- Do the tasks locally\n- Publish your code ..."
}
```

Each course has a slug - a short identifier used in URLs. For example,
`machine-learning-zoomcamp`, `data-engineering-zoomcamp`, etc. We'll
use these slugs for filtering in search.

## Using this data

In the RAG pipeline, this dataset is our knowledge base:

1. We index all the documents (the search step)
2. When a student asks a question, we search the index
3. The search returns the most relevant FAQ entries
4. We give those entries to the LLM as context
5. The LLM generates an answer based on the context

The `question` and `answer` fields contain the text we'll search
through. The `course` field lets us filter by course. For example, if a
student asks about the data engineering course, we skip results from
the ML course. The `section` field helps with ranking - knowing which
part of the course a question belongs to is useful context.

## A note on data preparation

In our case, the data is already prepared. I maintain this FAQ website
and made sure the data comes back in a convenient JSON format. So we
don't need to do much to get it ready. By the way, I cleaned a lot of
this data with the help of an LLM. That's a handy use case on its own.

Don't let that fool you. In reality, data preparation is often the most
time-consuming part of building a RAG system. You may need to scrape
websites, parse PDFs, and clean and chunk documents. That work isn't
visible here, but I did plenty of it ahead of time.

We keep the focus on the GenAI side in this course. In your own
projects, expect to spend real time on data preparation before you get
to this point.

In the next section, we'll build the search index.

## Key concepts

- [RAG](/course-wiki/rag/)

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
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
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

- [Video](https://www.youtube.com/watch?v=Mx6EqvzVDz0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/04-dataset.md)
