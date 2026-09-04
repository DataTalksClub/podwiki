---
title: "Vector Search with PGVector — LLM Zoomcamp Module 2"
summary: "---
video_url: "https://www.youtube.com/watch?v=0P54MFyz-mc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Vector Search with PGVector"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Vector Search with PGVector

## Notes

---
video_url: "https://www.youtube.com/watch?v=0P54MFyz-mc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Vector Search with PGVector

Many real databases can do vector search. Elasticsearch has it, and
there are dedicated stores like Qdrant and Chroma. We'll go with
Postgres. Most of us already run it at work, and the data engineering
course uses it too. The concept is the same as with sqlitesearch, only
the database under the hood changes.

[pgvector](https://github.com/pgvector/pgvector) is the PostgreSQL
extension that makes this work. Install it and Postgres can do vector
similarity search. On top of that you get the usual production features,
like concurrent access, transactions, and large datasets.

We'll run Postgres with pgvector in Docker.

## Starting Postgres with pgvector

Pull the image and start a container:

```bash
docker run -it \
    --name pgvector \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=pswd \
    -e POSTGRES_DB=faq \
    -v pgvector_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    pgvector/pgvector:pg17
```

This image has the pgvector extension pre-installed. The `-v` flag
creates a named volume so data persists across container restarts.

## Installing the Python client

Install the driver:

```bash
uv add psycopg[binary]
```

Note: if using Zshell use `uv add 'psycopg[binary]'`

We'll use `psycopg` (v3) to connect and run queries. Note: this is
different from `psycopg2` - psycopg v3 supports `conn.execute()`
directly without creating a cursor.

## Preparing the data

We need the FAQ documents and their embeddings.

Here's what we did in previous units as one script:

```python
from tqdm.auto import tqdm

from ingest import load_faq_data
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = load_faq_data()
texts = [doc["question"] + " " + doc["answer"] for doc in documents]

batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)
```

Now we connect to Postgres:

```python
import psycopg

conn = psycopg.connect(
    "postgresql://user:pswd@localhost:5432/faq"
)
conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
```

The second line activates pgvector. The Docker image we started isn't
plain Postgres, it ships the extension inside, and this turns it on. It
adds the `vector` column type and the similarity search operators.

## Creating a table

Create a table for storing documents with their embeddings:

```python
conn.execute("""
    DROP TABLE IF EXISTS documents
""")

conn.execute("""
    CREATE TABLE documents (
        id SERIAL PRIMARY KEY,
        course TEXT,
        section TEXT,
        question TEXT,
        answer TEXT,
        embedding vector(384)
    )
""")
```

The `vector(384)` column stores our 384-dimensional embeddings from
`all-MiniLM-L6-v2`.

## Inserting documents with embeddings

Let's insert the documents and their vectors into PGVector:

```python
def vec_to_str(vector):
    return "[" + ",".join(str(x) for x in vector) + "]"

for doc, vec in tqdm(zip(documents, vectors), total=len(documents)):
    conn.execute(
        """
        INSERT INTO documents (course, section, question, answer, embedding)
        VALUES (%s, %s, %s, %s, %s::vector)
        """,
        (doc["course"], doc["section"], doc["question"], doc["answer"],
         vec_to_str(vec))
    )

conn.commit()
```

We loop over the documents and insert each one with its embedding. We
hand Postgres the vector as text, so the `::vector` cast tells it to
parse that string back into a vector. We call `conn.commit()` to persist
the changes.

## Searching with cosine similarity

Search with a query:

```python
query = "I just discovered the course. Can I still join it?"
query_vector = model.encode(query)
query_str = vec_to_str(query_vector)
```

Search for the most similar documents:

```python
results = con

## Key concepts

- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
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

- [Video](https://www.youtube.com/watch?v=0P54MFyz-mc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/08-pgvector.md)
