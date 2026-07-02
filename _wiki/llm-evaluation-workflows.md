---
layout: wiki
title: "LLM Evaluation Workflows"
summary: "Practical podcast-backed workflows for evaluating LLM, RAG, and agent systems before and after production."
related:
  - Evaluation
  - Retrieval-Augmented Generation
  - LLM Production Patterns
---

LLM evaluation workflows are the repeatable checks teams use before they ship
prompts, [[retrieval-augmented-generation|RAG]] pipelines,
[[agent-engineering|agents]], and AI product
behavior. Evaluation is engineering work: teams collect examples, define pass
criteria, and review failures, then feed production behavior back into the next
test set.

LLM evaluation connects [[Evaluation]]
with [[LLM Production Patterns]],
[[retrieval-augmented-generation|Retrieval-Augmented Generation]],
and [[Model Monitoring]]. A good
workflow tells the team what failed and where the next fix belongs. The fix may
belong in prompting or retrieval. It may also belong in data preparation, tool
use, guardrails, or the product boundary. New production failures then become
future evaluation cases.

## Evaluation Sets and Pass Criteria

An LLM evaluation workflow is a small production discipline. Teams collect
representative examples, define what a good answer or action looks like, and
run the system. They look at failures and keep the eval set fresh as the
product changes.

Generator-evaluator checks are one approach; representative gold tests should
still be cheap enough to run often. Teams can eyeball early outputs, but
reliable software eventually needs examples that cover real user tasks, expected
formats, and known failure modes
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

The same work sits inside the AI engineer skill stack, where evaluation appears
with human review and correctness measurement, alongside validation sets, data
splits, and statistics
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
Precision, recall, accuracy, and careful measurement still matter even when the
product uses generative models or agents
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Large eval sets slow iteration because every prompt, retrieval change, or model
change becomes more expensive to check. Set size is a cost and coverage
tradeoff: large enough to avoid overfitting to a few examples, but small enough
that teams actually run it
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Use
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]] when the
eval result is deciding whether to change prompts and retrieval or change model
behavior through fine-tuning.

## Cheap Checks Before LLM Judges

Practitioners differ most on what should judge the system and where to spend
money. A cost-aware approach uses simple assertions, structured output, regular
expressions, and string matching when the expected behavior is easy to check.
Cheaper models and spreadsheets can also keep iteration affordable. Save
LLM-as-judge calls for cases where deterministic checks are too brittle
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

In enterprise agent settings, LLM judges are more explicit: golden datasets,
pass thresholds, and LLM judges trained against human labels, with red teaming
and guardrails in the same workflow
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). Judges can be
biased, so teams must validate the judge instead of treating it as an oracle.

## Human Review and Failure Analysis

Human review is most useful when the team is learning the failure taxonomy.
Common failure types include unsupported answers, missing citations, and wrong
tone. Unsafe advice, stale knowledge, broken formatting, and tool misuse also
belong in the taxonomy.

Spreadsheet-style failure analysis lets teams categorize failures and rank the
largest error classes, so they avoid spending engineering time on minor
formatting when the major problem is retrieval quality
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
This keeps [[Testing]] and [[Evaluation]] close together: tests catch repeatable
failures, while review discovers which failures matter.

Teams use automated checks to make that review repeatable. Deterministic checks
can validate JSON schema, exact fields, and required citations. They can also
check forbidden strings, SQL syntax, tool parameters, and regular expressions.

Other checks need semantic judgment. The LLM-judge version raises a second eval
problem: teams must compare automated judgments against human labels and watch
for judge bias
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

## RAG Evaluation

RAG evaluation has to separate retrieval failures from generation failures. A
bad answer can come from missing source documents, poor chunking, or weak
embeddings. It can also come from loose metadata filters, stale indexes, prompt
wording, or a model that ignores the retrieved evidence. Failure analysis asks
where the next fix belongs before adding more architecture
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

The search-side version connects chunk size, overlap, and embedding choice.
Retrieval strategy, answer quality, and citations belong in the same evaluation
workflow, as does human-in-the-loop evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
LLM eval is therefore part of
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
and [[Production Search Evaluation]],
not only model scoring.

The same evidence keeps [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
close to source trust. The answer quality check should ask whether the answer
is useful and whether it's grounded in the retrieved material. The retrieval
check should ask whether the right evidence was available to the model before
generation.

## Agent and Tool Evaluation

Agent evaluation adds software behavior to answer quality. Public benchmarks
such as SQuAD evaluate model capability, not the deployed system
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Teams therefore need custom datasets that represent user goals, tool
constraints, and product workflows.

Agent testing is close to ordinary
[[testing]] and
[[orchestration]]: mock external
tools, assert outputs, check tool names and parameters, and keep integration
tests for the real systems. A calendar-agent example shows why outcome
assertions matter more than exact trace matching, since several valid action
paths can create the same correct invite
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

## Production Feedback and Traces

Offline eval sets decay unless production behavior feeds them. Explicit feedback
includes thumbs up or thumbs down; implicit feedback includes a user repeating
or reframing a query after a bad answer
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). Those signals
can become synthetic data, human labeling work, or new gold cases, and can lead
to updated prompts, fine-tuning examples, or new guardrail tests.

Production feedback also needs traces. Logs and traces let the team reconstruct
whether the wrong output came from retrieval, context packaging, tool use, or
generation
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
This puts LLM evaluation next to [[Model Monitoring]]
and [[LLM Production Patterns]]
instead of leaving it as an offline score.

## Governance and Guardrails

High-risk LLM workflows need more than accuracy checks. Enterprise agents add
logging, auditability, data lineage, and guardrails, and compliance matters for
sensitive settings such as healthcare and finance
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]). Evaluation in
those settings belongs with
[[Responsible AI and Governance]].

Guardrails can be evaluated like any other product behavior. Unsafe requests
should be refused or routed, and sensitive data shouldn't leak through
retrieved context. Citations should reference allowed sources. Tool calls should
stay inside permission boundaries. Red-team cases then become part of the same
regression suite as ordinary product examples.
