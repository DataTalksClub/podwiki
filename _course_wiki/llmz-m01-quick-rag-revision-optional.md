---
title: "Quick RAG Revision (Optional) — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=gH8fB-6Emmo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Quick RAG Revision (Optional)"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Quick RAG Revision (Optional)

## Notes

---
video_url: "https://www.youtube.com/watch?v=gH8fB-6Emmo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Quick RAG Revision (Optional)

Before we talk about agents, let's set up the RAG pipeline we built
in Part 1.

Our courses have a lot of participants. They ask the same questions
over and over, so we keep a FAQ document and point students to it. RAG
takes that FAQ and finds the entry that matches a question. It then
sends the entry to an LLM so it can answer. That way a student gets a
reply right away instead of scrolling through a long document.

We'll use two helpers we defined earlier in this module:

- `rag_helper.py` - the `RAGBase` class wrapping search, prompt building, and the LLM call
- `ingest.py` - `load_faq_data` and `build_index` for loading the FAQ and building a minsearch index

If you're working through Part 2 as a standalone workshop (without
Part 1), download them into your project:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/01-agentic-rag/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/01-agentic-rag/code/ingest.py
```

## Setting up RAG

Set up the OpenAI client:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Load the data and build the search index:

```python
from rag_helper import RAGBase
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Create the assistant:

```python
instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=instructions,
)
```

## Testing it

Let's try a question:

```python
assistant.rag("How do I run Ollama locally?")
```

This works fine. The search finds relevant FAQ entries about Ollama,
and the LLM gives a good answer.

Now try something slightly different:

```python
assistant.rag("How do I run Olama locally?")
```

The word "Olama" doesn't match "Ollama" in our index. We use lexical
search, so it looks for the exact word and finds nothing. The LLM
gets these bad results and either says "I don't know" or answers with
irrelevant information.

This is the limitation of a fixed pipeline. The search runs once with
the exact query the user typed, and there's no second chance. The
pipeline doesn't know the search failed, so it can't try again with a
corrected query.

We need something smarter. We need an agent.

## Key concepts

- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
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
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=gH8fB-6Emmo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/12-rag-revision.md)
