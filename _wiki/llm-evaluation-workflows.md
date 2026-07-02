---
layout: wiki
title: "LLM Evaluation Workflows"
summary: "Practical podcast-backed workflows for evaluating LLM, RAG, and agent systems before and after production."
related:
  - Evaluation
  - Retrieval-Augmented Generation
  - RAG
  - LLM Production Patterns
---

LLM evaluation workflows are the repeatable checks teams use before they ship
prompts, [RAG]({{ '/wiki/rag/' | relative_url }}) pipelines,
[agents]({{ '/wiki/agent-engineering/' | relative_url }}), and AI product
behavior. DataTalks.Club guests treat evaluation as engineering work. Teams
collect examples, define pass criteria, and review failures. They feed
production behavior back into the next test set.

LLM evaluation connects [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
with [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}). A good
workflow tells the team what failed and where the next fix belongs. The fix may
belong in prompting or retrieval. It may also belong in data preparation, tool
use, guardrails, or the product boundary. New production failures then become
future evaluation cases.

## Evaluation Sets and Pass Criteria

An LLM evaluation workflow is a small production discipline. Teams collect
representative examples, define what a good answer or action looks like, and
run the system. They look at failures and keep the eval set fresh as the
product changes.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
anchors the builder version in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 13:56, he describes generator-evaluator checks. At 23:00-25:25, he argues
for representative gold tests that are still cheap enough to run often. Teams
can eyeball early outputs, but reliable software eventually needs examples that
cover real user tasks, expected formats, and known failure modes.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts the same work
inside the AI engineer skill stack in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
At 38:41-41:39, evaluation appears with human review and correctness
measurement. Paul also uses validation sets, data splits, and statistics. [Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }})
keeps that rigor in
[Understanding the AI Engineer Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }})
at 7:45-7:55. Precision, recall, accuracy, and careful measurement still matter
even when the product uses generative models or agents.

Large eval sets slow iteration because every prompt, retrieval change, or model
change becomes more expensive to check. Hugo's 24:18-25:25 discussion in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
therefore treats size as a cost and coverage tradeoff. The set should be large
enough to avoid overfitting to a few examples, but small enough that teams
actually run it. Use
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) when the
eval result is deciding whether to change prompts and retrieval or change model
behavior through fine-tuning.

## Cheap Checks Before LLM Judges

Guests differ most on what should judge the system and where to spend money.
Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
discussion at 24:39-24:59 is cost-aware. Simple assertions, structured output,
regular expressions, and string matching can be enough when the expected
behavior is easy to check. Cheaper models and spreadsheets can also keep
iteration affordable. Save LLM-as-judge calls for cases where deterministic
checks are too brittle.

[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) is more explicit
about LLM judges in enterprise agent settings. In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
he describes golden datasets, pass thresholds, and LLM judges trained against
human labels at 46:19-50:18. Red teaming and guardrails appear in the same
discussion. He also warns that judges can be biased, so teams must validate the
judge instead of treating it as an oracle.

## Human Review and Failure Analysis

Human review is most useful when the team is learning the failure taxonomy.
Common failure types include unsupported answers, missing citations, and wrong
tone. Unsafe advice, stale knowledge, broken formatting, and tool misuse also
belong in the taxonomy.

Hugo's spreadsheet-style failure
analysis at 26:43-27:20 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
shows how teams can categorize failures and rank the largest error classes.
They avoid spending engineering time on minor formatting if the major problem is
retrieval quality. This keeps [Testing]({{ '/wiki/testing/' | relative_url }})
and [Evaluation]({{ '/wiki/evaluation/' | relative_url }}) close together:
tests catch repeatable failures, while review discovers which failures matter.

Teams use automated checks to make that review repeatable. Deterministic checks
can validate JSON schema, exact fields, and required citations. They can also
check forbidden strings, SQL syntax, tool parameters, and regular expressions.

Other checks need semantic judgment. Aditya's
[Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
discussion at 46:19-48:11 shows the LLM-judge version, but it also implies a
second eval problem. Teams must compare automated judgments against human labels
and watch for judge bias.

## RAG Evaluation

RAG evaluation has to separate retrieval failures from generation failures. A
bad answer can come from missing source documents, poor chunking, or weak
embeddings. It can also come from loose metadata filters, stale indexes, prompt
wording, or a model that ignores the retrieved evidence. Hugo's
failure-analysis example at
26:43-27:20 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
asks where the next fix belongs before adding more architecture.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the search-side
version in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 38:24-48:09, she connects chunk size, overlap, and embedding choice.
Retrieval strategy, answer quality, and citations belong in the same evaluation
workflow. Human-in-the-loop evaluation belongs there too. LLM eval is therefore
part of
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
not only model scoring.

The same evidence keeps [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
close to source trust. The answer quality check should ask whether the answer
is useful and whether it's grounded in the retrieved material. The retrieval
check should ask whether the right evidence was available to the model before
generation.

## Agent and Tool Evaluation

Agent evaluation adds software behavior to answer quality. [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
says public benchmarks such as SQuAD evaluate model capability, not the deployed
system
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
51:17-51:42). Teams therefore need custom datasets that represent user goals,
tool constraints, and product workflows.

Her agent testing workflow is close to ordinary
[testing]({{ '/wiki/testing/' | relative_url }}) and
[orchestration]({{ '/wiki/orchestration/' | relative_url }}). Mock external
tools, assert outputs, check tool names and parameters, and keep integration
tests for the real systems. At 56:02-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
the calendar-agent example shows why outcome assertions matter more than exact
trace matching. Several valid action paths can create the same correct invite.

## Production Feedback and Traces

Offline eval sets decay unless production behavior feeds them. Aditya describes
explicit feedback, such as thumbs up or thumbs down. He also describes implicit
feedback, such as a user repeating or reframing a query after a bad answer
([The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
38:49-42:20). Those signals can become synthetic data, human labeling work, or
new gold cases. They can also lead to updated prompts, fine-tuning examples, or
new guardrail tests.

Production feedback also needs traces. Hugo discusses logs and traces at 27:38
in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
The team has to reconstruct whether the wrong output came from retrieval or
context packaging. The problem can also come from tool use or generation. This
puts LLM evaluation next to [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
and [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
instead of leaving it as an offline score.

## Governance and Guardrails

High-risk LLM workflows need more than accuracy checks. Aditya's enterprise
agent discussion at 30:00-32:27 in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
adds logging, auditability, data lineage, and guardrails. Compliance also
matters for sensitive settings such as healthcare and finance. Evaluation in
those settings belongs with
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

Guardrails can be evaluated like any other product behavior. Unsafe requests
should be refused or routed, and sensitive data shouldn't leak through
retrieved context. Citations should reference allowed sources. Tool calls should
stay inside permission boundaries. Red-team cases then become part of the same
regression suite as ordinary product examples.
