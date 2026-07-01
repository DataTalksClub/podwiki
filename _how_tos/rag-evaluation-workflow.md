---
layout: article
title: "How to Run a RAG Evaluation Workflow"
keyword: "rag evaluation workflow"
summary: "A practical workflow for evaluating RAG systems with user tasks, gold examples, retrieval checks, answer checks, citations, human review, traces, and production feedback."
search_intent: "Help readers who search for a RAG evaluation workflow understand how to test retrieval, answer grounding, citations, human review, logs, and production feedback using DataTalks.Club podcast evidence."
related_wiki:
  - RAG
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Search, RAG, and Knowledge Systems
  - Production Search Evaluation
  - Search and RAG Project Checklist
  - LLM Production Patterns
  - Agent Engineering
---

When you evaluate RAG, separate retrieval from generation:

1. The retriever found the evidence the user needed.
2. The model used that evidence to produce a correct, useful, and cited answer.

Run the workflow as an engineering cycle. Start with user tasks and gold
examples, then test retrieval and answers. Review failures, add traces, and
feed production behavior back into the next eval set.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
frames the workflow as practical LLM engineering in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 23:00-25:25, he recommends representative gold tests that are small enough
to run often. At 26:43-27:38, he adds failure analysis. Logs and traces then
show whether a bad answer came from retrieval, prompting, formatting, or another
part of the system.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the search
version in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 38:24-48:09, she moves from chunking and embeddings to prompt context,
citations, and offline tests. She also includes human-in-the-loop evaluation.
That makes RAG evaluation part of
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
not only an answer-scoring exercise.

Use the
[LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }})
when this workflow sits inside a broader production plan.

## Start With User Tasks

Write the eval set around real user tasks, not around generic questions. A
support assistant might need to answer from current product documentation. An
internal knowledge assistant might need to find the policy, cite it, and refuse
when the policy doesn't exist. A research assistant might need to compare
multiple retrieved sources before summarizing.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts this inside
the AI engineering skill stack in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
At 22:29, the work includes full-stack engineering. At 29:12, RAG and
knowledge management become part of shipping AI products. At 42:28, the focus
is the product system, not a demo.

For each task, record:

1. The user type and workflow.
2. The question or input the user will provide.
3. The source collection the system is allowed to use.
4. The expected answer format.
5. The evidence that must be retrieved.
6. The refusal or escalation behavior when evidence is missing.

This first step connects RAG evaluation to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[AI Engineer Role]({{ '/wiki/ai-engineer-role/' | relative_url }}), and the
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }}).

## Build Gold Examples

Gold examples should be representative, cheap to run, and easy to review.
Hugo's 23:00-25:25 discussion in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
is useful because it treats eval size as a coverage and cost tradeoff. A tiny
set lets the team move quickly, but it can overfit to a few hand-picked cases.
A huge set may become so expensive that nobody runs it during prompt,
retriever, or chunking changes.

Create examples that include:

1. Common successful questions.
2. Long-tail questions that should still work.
3. Questions with similar wording but different answers.
4. Stale or missing-knowledge cases that should refuse or route.
5. Citation-sensitive cases where the exact source matters.
6. Security or permission cases when the corpus contains restricted material.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the production
reason for RAG in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46-46:42, changing knowledge makes retrieval a better fit than
continuous retraining. At 53:34-56:39, gold-standard examples and human
evaluation remain part of the quality loop. Use
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
when the failure might belong to retrieval, model behavior, or both.

## Check Retrieval First

Evaluate retrieval before answer quality. If the right document or chunk isn't
in the candidate set, the model can't reliably answer from it. If the right
evidence is present but buried or poorly formatted, the fix may belong in
ranking or filtering. It may also belong in chunking, metadata, or context
packaging.

Atita's transcript-chatbot example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
starts with ingestion, chunking, and overlap at 38:24. It also covers embedding
models and vectorization. At 42:49, the retrieved context becomes prompt
context with citations. At 48:09, evaluation covers multiple levels of the
pipeline.

For each gold example, record:

1. The expected source document, section, or chunk.
2. Whether the expected evidence appears in the top results.
3. Whether metadata filters and permissions were applied correctly.
4. Whether the chunk has enough surrounding context to answer the question.
5. Whether citations can reference a useful source, not only an opaque vector id.

This is the retrieval side of
[RAG]({{ '/wiki/rag/' | relative_url }}),
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[Search]({{ '/wiki/search/' | relative_url }}), and
[Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
Use
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
when the evaluation shows a storage or search-stack decision.

## Check Answers And Citations

After retrieval passes, evaluate the generated answer. The answer should be
correct, grounded in retrieved evidence, useful for the task, and honest about
uncertainty. It should include citations when the product depends on source
trust.

Atita connects RAG references to explainability and user trust at 42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Hugo's generator-evaluator discussion at 13:56 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
adds the repeatable checking approach. Simple assertions can handle structured
outputs, required fields, and required citations. More subjective answers may
need human review or an LLM judge that has been compared with human labels.

Score answers on separate dimensions:

1. Correctness: the answer satisfies the user task.
2. Grounding: every substantive claim is supported by retrieved evidence.
3. Citation quality: sources are visible, relevant, and specific enough to
   check.
4. Completeness: the answer covers the important parts of the task without
   inventing extras.
5. Refusal behavior: the system declines or routes when evidence is missing.
6. Format: the output matches the product schema.

Keep formatting failures separate from factual failures. Hugo's failure
analysis at 26:43 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
is explicit about categorizing errors before deciding what to fix. That
boundary keeps
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
from becoming one undifferentiated score.

## Review Failures With Humans

Use human review to discover the failure taxonomy and label the failure source.

The problem may be missing documents, poor chunking, or weak ranking. It may
also be bad prompt context or model behavior. Stale data and missing citations
can be separate labels. Product policy can be its own label.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) makes
the system-evaluation point in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 51:17-53:20, she argues for custom datasets and system benchmarks. She also
uses mocked tools and integration tests. Regression tests belong in the same
workflow. At 56:02-57:23, outcome assertions matter more than exact path
matching because multiple traces can still produce the same correct result.

For a plain RAG assistant, the same idea applies because a correct answer can
come from different retrieved chunks. A bad answer can look fluent while hiding
a retrieval miss. Reviewers should look at both the answer and the evidence the
model saw.

Store review labels as structured fields:

1. `retrieval_missing`
2. `retrieval_low_rank`
3. `chunk_too_small`
4. `chunk_too_noisy`
5. `citation_missing`
6. `citation_wrong`
7. `answer_unsupported`
8. `answer_incomplete`
9. `refusal_failed`
10. `format_failed`

Use
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) only when
the workflow needs planning, tools, or action. Ranjitha's 36:11-37:39
discussion separates cases where RAG is enough from cases where an agentic
system is needed.

## Add Logs And Traces

Every eval run should leave enough trace data to reproduce the failure.

Log:

1. The user input and query rewrite, if one exists.
2. Retrieval parameters, filters, scores, and retrieved document ids.
3. Chunk text or source references.
4. Prompt version, model version, generated answer, and citations.
5. Latency, cost, and review labels.

Hugo names logs and traces at 27:38 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
Those traces make debugging possible because a bad answer can come from source
preparation, retrieval, or context packaging. It can also come from prompt
wording, model choice, or output policy.

Meryem adds another production reason in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 18:46, provider or model drift can change behavior. At 49:44-51:35,
latency, cost, and serving choices become production constraints. The team can
use versioned traces to compare runs when the model, index, embedding model, or
prompt changes.

These logs connect RAG evaluation to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

## Feed Production Back Into The Eval Set

Offline gold tests decay as production users ask new questions, documents
change, and retrieval failures appear in segments the original eval set didn't
cover. Add production feedback to the workflow without letting raw user traffic
become an unreviewed benchmark.

Useful feedback sources include:

1. Thumbs-up or thumbs-down labels.
2. Repeated or reformulated questions after a bad answer.
3. Clicks on citations or source documents.
4. Escalations to support or subject-matter experts.
5. Empty retrieval results and low-confidence answers.
6. High-latency or high-cost queries.
7. Human review notes from sampled conversations.

Atita's 48:09 discussion in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
keeps offline tests and human-in-the-loop review together. Hugo's 26:43-27:38
discussion in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
turns those observations into failure categories and traces.

For product search and RAG systems, connect feedback to the task outcome, not
only to answer prettiness. [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
covers relevance, freshness, and latency. It also covers business metrics, A/B
tests, and monitoring. The same discipline applies when the search result is
fed to a model instead of shown directly to a user.

## Workflow Checklist

Use this sequence when building or reviewing a RAG evaluation workflow:

1. Define the user tasks, source collections, answer format, and refusal
   behavior, following Paul's product-focused AI engineering framing in
   [his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
2. Build a small gold set with common questions, hard questions, missing-answer
   cases, citation-sensitive cases, and permission cases, following Hugo's
   23:00-25:25 guidance in
   [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
3. Evaluate retrieval before generation. Check expected evidence, top-result
   coverage, and filters before checking chunk context and source references.
   Use Atita's 38:24-48:09 RAG pipeline in
   [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
4. Evaluate answers for correctness, grounding, citation quality, completeness,
   refusal behavior, and format, connecting the checks to
   [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).
5. Run human review to label the failure source, using Ranjitha's custom
   datasets and outcome-evaluation guidance in
   [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
6. Store logs and traces for every run so changes to prompts, embedding models,
   indexes, rerankers, or model providers can be compared.
7. Add production feedback and reviewed failures back into the gold set, then
   rerun the workflow before retrieval, prompt, model, or data-source changes.
8. Decide the next fix from the labels. Missing evidence usually means the
   team should change source preparation, chunking, indexing, or search. When
   answers are unsupported, change prompting, answer policy, or model behavior.
   Changing knowledge belongs in RAG, while repeated behavior or style failures
   may belong in
   [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}).

If the workflow needs structured relationships instead of similar text, compare
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
and
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }}).
If the project is still being scoped, pair this workflow with the
[LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }})
and the
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }}).
