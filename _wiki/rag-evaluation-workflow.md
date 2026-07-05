---
layout: article
tags: ["how-to"]
title: "RAG Evaluation Workflow"
keyword: "rag evaluation workflow"
secondary_keywords:
  - "rag evaluation"
  - "rag eval"
  - "rag evaluation framework"
  - "llm rag evaluation"
  - "retrieval augmented generation evaluation"
summary: "A practical workflow for RAG eval: user tasks, gold examples, retrieval checks, answer checks, citations, review, traces, and feedback."
related_wiki:
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Long-Context LLM Evaluation
  - Production Search Evaluation
  - Search and RAG Project Checklist
  - LLM Production Patterns
  - Agent Engineering
  - Agent Ops
---

When you run a RAG evaluation workflow, separate retrieval from generation:

1. The retriever found the evidence the user needed.
2. The model used that evidence to produce a correct, useful, and cited answer.

Start with user tasks and gold examples, then test retrieval and answers.
Review failures, add traces, and feed production behavior back into the next
eval set.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Representative gold tests should be small enough to run often, but broad enough
to reveal common failure modes. Failure analysis and traces show whether a bad
answer came from retrieval, prompting, formatting, or another part of the
system.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

RAG evaluation work covers measurement and quality judgment across eval tasks
and labels, plus traces, review, and feedback.
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers the
concept boundary, [[RAG Portfolio Projects]] covers project-type choice, and the
[[Search and RAG Project Checklist]] covers implementation review fields. The
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] covers the wider
learning and rollout sequence.

Search evaluation starts before answer scoring because chunking and embeddings
affect the evidence the model sees. Prompt context, citations, offline tests,
and human review determine whether the final answer can be trusted. That makes
RAG evaluation a [[context-engineering=>context engineering]] workflow, not only
an answer-scoring workflow.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>RAG Evaluation Layers]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@50:52=>Human-in-the-Loop RAG Evaluation]]
RAG evaluation therefore connects
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] with
[[Production Search Evaluation]] instead of reducing the work to answer scoring.

## Start With User Tasks

Write the eval set around real user tasks, not around generic questions. A
support assistant might need to answer from current product documentation. An
internal knowledge assistant might need to find the policy, cite it, and refuse
when the policy doesn't exist. A research assistant might need to compare
multiple retrieved sources before summarizing.

RAG evaluation belongs in the product system, not in a standalone demo. The
same AI engineering skill stack includes full-stack product work, knowledge
management, and the discipline needed to ship AI products.
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

For each task, record:

1. The user type and workflow.
2. The question or input the user will provide.
3. The source collection the system is allowed to use.
4. The expected answer format.
5. The evidence that must be retrieved.
6. The refusal or escalation behavior when evidence is missing.

When the evaluation backs a portfolio project or project README, link the task
records from the [[Search and RAG Project Checklist]]. Don't duplicate the
project checklist here.

## Build Gold Examples

Gold examples should be representative, cheap to run, and easy to review. Eval
size is a coverage and cost tradeoff. A tiny set lets the team move quickly, but
it can overfit to a few hand-picked cases. A huge set may become so expensive
that nobody runs it during prompt, retriever, or chunking changes.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Create examples that include:

1. Common successful questions.
2. Long-tail questions that should still work.
3. Questions with similar wording but different answers.
4. Stale or missing-knowledge cases that should refuse or route.
5. Citation-sensitive cases where the exact source matters.
6. Security or permission cases when the corpus contains restricted material.

Changing knowledge makes retrieval a better fit than continuous retraining.
Gold-standard examples and human evaluation still belong in the quality loop.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
Link to [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] when the failure might belong
to retrieval, model behavior, or both.

## Check Retrieval First

Evaluate retrieval before answer quality. If the right document or chunk isn't
in the candidate set, the model can't reliably answer from it. If the right
evidence is present but buried or poorly formatted, the fix may belong in
ranking or filtering. It may also belong in chunking, metadata, or context
packaging.
For large-document tasks, add
[[long-context-llm-evaluation=>long-context LLM evaluation]] before treating
retrieval as the only possible fix
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

Evaluate the full RAG path
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]].

Human review belongs in the loop because retrieval metrics can
miss whether a passage actually answers the user's task or supports the final
claim.

The search-side evaluation is layered. Start with embedding and chunking
choices, then test retrieval strategy, answer quality, and citations together.
That makes a failed answer actionable because the team can decide whether to
change corpus preparation, retrieval, prompting, or review policy
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>RAG Evaluation Layers]].

For each gold example, record:

1. The expected source document, section, or chunk.
2. Whether the expected evidence appears in the top results.
3. Whether metadata filters and permissions were applied correctly.
4. Whether the chunk has enough surrounding context to answer the question.
5. Whether citations can reference a useful source, not only an opaque vector id.

This is the measurement view of retrieval in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
[[Search]], and
[[Information Retrieval]].
It also gives the team concrete [[context-engineering=>context engineering]]
inputs to look at before rewriting the prompt.
Link to [[Vector Database vs Search Engine]] when the evaluation shows a storage or
search-stack decision.

## Check Answers And Citations

After retrieval passes, evaluate the generated answer. The answer should be
correct, grounded in retrieved evidence, useful for the task, and honest about
uncertainty. It should include citations when the product depends on source
trust.

RAG references support explainability and user trust, while
generator-evaluator patterns add repeatable checks for output quality. Simple
assertions can handle structured outputs, required fields, and required
citations. More subjective answers may need human review or an LLM judge that
has been compared with human labels.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Score answers on separate dimensions:

1. Correctness: the answer satisfies the user task.
2. Grounding: every substantive claim is supported by retrieved evidence.
3. Citation quality: sources are visible, relevant, and specific enough to
   check.
4. Completeness: the answer covers the important parts of the task without
   inventing extras.
5. Refusal behavior: the system declines or routes when evidence is missing.
6. Format: the output matches the product schema.

Keep formatting failures separate from factual failures, and categorize errors
before deciding what to fix.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
That boundary keeps
[[LLM Evaluation Workflows]]
from becoming one undifferentiated score.

## Review Failures With Humans

Use human review to discover the failure taxonomy and label the failure source.

The problem may be missing documents, poor chunking, or weak ranking. It may
also be bad prompt context or model behavior. Stale data, missing citations, and
product policy can each get separate labels.

Custom datasets and system benchmarks belong in the same evaluation workflow.
When retrieval is part of an agentic workflow, add mocked tools, integration
tests, and regression tests. The production version of that workflow also needs
[[agent-ops=>Agent Ops]] practices for tool-call traces, permissions, and
feedback. Outcome assertions matter more than exact path matching because
multiple traces can still produce the same correct result.
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

For a plain RAG assistant, a correct answer can come from different retrieved
chunks. A bad answer can look fluent while hiding a retrieval miss. Reviewers
should look at both the answer and the evidence the model saw.

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

Link to [[Agent Engineering]] only when the workflow needs planning, tools, or
action. Some products only need RAG. Others need an agentic system that uses
retrieval as one tool among several.
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Add Logs And Traces

Every eval run should leave enough trace data to reproduce the failure.

Log:

1. The user input and query rewrite, if one exists.
2. Retrieval parameters, filters, scores, and retrieved document ids.
3. Chunk text or source references.
4. Prompt version, model version, generated answer, and citations.
5. Latency, cost, and review labels.

Logs and traces make debugging possible because a bad answer can come from
source preparation, retrieval, or context packaging. It can also come from
prompt wording, model choice, or output policy.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Provider drift can change behavior, while latency, cost, and serving choices
also become production constraints. Use versioned traces to compare runs when
the model, index, embedding model, or prompt changes.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

These logs connect RAG evaluation to
[[Model Monitoring]],
[[MLOps]], and
[[Production Search Evaluation]].
Link to [[LLM Production Patterns]] when traces become a monitoring and operations
design question.

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

Offline tests and human-in-the-loop review belong together. Reviewers turn
production observations into failure categories and traces for the next eval run.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

For product search and RAG systems, connect feedback to the task outcome, not
only to answer style. [[Production Search Evaluation]] covers relevance,
freshness, latency, and business metrics. It also covers A/B tests and
monitoring. The same discipline applies when the search result is fed to a
model instead of shown directly to a user.

## Eval Run Sequence

Use this sequence for a RAG evaluation run:

1. Define the user tasks, source collections, answer format, and refusal behavior that the product needs before you write the first gold example. [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]
2. Build a small gold set that covers common and hard questions, missing-answer cases, citation-sensitive cases, and permission cases. [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
3. Evaluate retrieval before generation. Check expected evidence, top-result
   coverage, and filters before checking chunk context and source references.
   [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
4. Evaluate answers for correctness, grounding, citation quality, completeness,
   refusal behavior, and format, connecting the checks to
   [[LLM Evaluation Workflows]].
5. Run human review to label the failure source before deciding what to fix. [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
6. Store logs and traces for every run so changes to prompts, embedding models,
   indexes, rerankers, or model providers can be compared.
7. Add production feedback and reviewed failures back into the gold set, then
   rerun the workflow before retrieval, prompt, model, or data-source changes.
8. Decide the next fix from the labels. Missing evidence usually means the
   team should change source preparation, chunking, indexing, or search. When
   answers are unsupported, change prompting, answer policy, or model behavior.
   Changing knowledge belongs in RAG, while repeated behavior or style failures
   may belong in
   [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

If the workflow needs structured relationships instead of similar text, compare
[[Graph RAG vs Vector RAG]]
and
[[Knowledge Graph vs Vector Search]].
Pair this workflow with [[RAG Portfolio Projects]] when the project is still
being scoped. Once implementation is ready, use the
[[Search and RAG Project Checklist]]. For the broader production sequence, use
the [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].
