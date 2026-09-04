---
title: "Environment — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=3U4gBrmkZyM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Environment"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Environment

## Notes

---
video_url: "https://www.youtube.com/watch?v=3U4gBrmkZyM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Environment

For this module, all you need is Python with Jupyter.

## Prerequisites

You need the following:

- Python (3.14 or later)
- An [OpenAI account](https://openai.com/) (or an OpenAI-compatible
  provider like Groq, Gemini, or Ollama)
- Basic familiarity with Python and the command line

## Creating the project

We'll start from scratch with no cloning needed - you'll create the
project yourself, step by step, either locally or on GitHub Codespaces.

## Creating the project locally

First, install uv - it's a Python package manager, and I switched all my
projects to it because it's fast and convenient. Once I started using
it, I never wanted to go back.

On Mac or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

(You can also use `pip install uv` if you prefer.)

Create an empty folder for the project and initialize it:

```bash
mkdir llm-zoomcamp-2026-code
cd llm-zoomcamp-2026-code
uv init
```

This creates a `pyproject.toml` and a basic project structure.

## Creating the project on GitHub Codespaces

We suggest using Codespaces because everyone gets the same Ubuntu,
Python, and Docker. That makes it easier to help each other when
problems come up.

Setup:

- Create a new repo on GitHub. Name it whatever you want, for example
  `llm-zoomcamp-2026-code` or `introduction-to-rag`, and add a README.
- Open the repo, click the green `<> Code` button, switch to the
  Codespaces tab, and create a codespace.

You now have a remote environment running in Codespaces. By default it
opens an in-browser editor, but you can connect VS Code on your desktop
for a better experience. Click `Codespaces` in the bottom-left corner and
pick "Open in Visual Studio Code Desktop" from the dropdown.

Once VS Code opens, press `` ctrl+` `` to bring up the terminal and
initialize the project the same way as locally:

```bash
pip install uv
uv init
```

## Adding dependencies
Now add the dependencies we'll need:

```bash
uv add requests minsearch openai jupyter python-dotenv
```

This installs:

- `requests` - to fetch the FAQ dataset from the internet
- `minsearch` - a simple in-memory search engine for indexing and
  searching text
- `openai` - the OpenAI API client for calling the LLM
- `jupyter` - the notebook environment where we'll write and run code
- `python-dotenv` - to load API keys from a `.env` file

## Setting up API keys

We need an API key to talk to the LLM. If you're using OpenAI, you'll
need to deposit some money first. The minimum is $5 (as of June 2026).
This lesson costs well under 10 cents to run, so that $5 goes a long
way.

I also recommend creating a separate OpenAI project for the course.
Then you can open the usage page and see exactly how much you spent
here, apart from your other work.

The safest way to store the key is in a `.env` file that never gets
committed to git.

Create a `.env` file in your project folder and put your API key in
it:

```bash
OPENAI_API_KEY=sk-YOUR_KEY_HERE
```

Now add `.env` to `.gitignore` to make sure you never accidentally
commit your key:

```bash
.env
```

Never commit `.env` to git. Treat the API key like a password. If it
leaks, someone else can run up charges on your account.

## Starting Jupyter

Start Jupyter:

```bash
uv run jupyter notebook
```

Create a new notebook. Throughout the course, you'll copy code from
the section notes into notebook cells.

Check that the OpenAI client works:

```python
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
openai_client = OpenAI()
```

If you see an error, make sure the key in your `.env` file is
correct.

For Groq or other OpenAI-compatible providers, add the key to
`.env`:

```bash
GROQ_API_KEY=your_key_here
```

And configure the client:

```python
from openai import OpenAI

## Key concepts

- [Vector Search](/course-wiki/vector-search/)

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

- [Video](https://www.youtube.com/watch?v=3U4gBrmkZyM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/02-environment.md)
