---
layout: wiki
title: "LLM Evaluation Workflows"
summary: "Practical workflows for evaluating LLM and agent behavior before and after production."
related:
  - Evaluation
  - Retrieval-Augmented Generation
  - Annotation Quality Workflows
  - LLM Production Patterns
  - LLMOps
  - Agent Ops
---

Teams use LLM evaluation workflows before shipping prompts,
[[agent-engineering=>agents]], and AI product behavior. Evaluation is
engineering work where teams collect examples, define pass criteria, and review
failures. They then feed production behavior back into the next test set
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
The same habit scales down for
[[ai-tools-for-personal-productivity=>AI tools for personal productivity]]:
keep a few known examples and review the output before trusting repeated AI
workflows.

LLM evaluation connects [[Evaluation]]
with [[LLM Production Patterns]],
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]], and
[[Model Monitoring]]. It also connects to [[LLMOps]] and [[agent-ops=>Agent Ops]].

A team should be able to tell what failed and where the next fix belongs. The
fix may belong in prompting or data preparation. It may also belong in
retrieval, tool use, guardrails, or the product boundary. New production
failures then become future evaluation cases. For RAG-specific workflow details,
use
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

Use [[llm-system-design-interview=>LLM system design interview]] framing when
the evaluation design has to become part of the architecture answer. The design
needs separate checks for retrieval and generation. It also needs checks for
tools, guardrails, and product outcomes.

## Evaluation Sets and Pass Criteria

An LLM evaluation workflow is a small production discipline. Teams collect
representative examples, define what a good answer or action looks like, and
run the system. They look at failures and keep the eval set fresh as the
product changes.

Generator-evaluator checks give teams one starting approach. Representative gold
tests should still be cheap enough to run often. Teams can eyeball early outputs
first. Later they can collect examples that cover real user tasks, expected
formats, and known failure modes
([[cite:practical-llm-engineering-and-rag@13:56=>Generator-Evaluator Checks]]).

Hugo Bowne-Anderson's generator-evaluator check fits products that already
create many outputs. Transcript summaries and structured content are examples.
One model or rule-based evaluator can check whether the generated output meets
the expected structure. The team still needs a gold set so the evaluator has
something concrete to match
([[cite:practical-llm-engineering-and-rag@13:56=>Generator-Evaluator Checks]]).

Generator-evaluator checks are useful when manual checking doesn't scale, but
they don't remove subject-matter review. The evaluator criteria need to name the
output properties that matter. Examples include timestamps, required fields,
citations, and task-specific correctness.

The same work sits inside the AI engineer skill stack. Evaluation appears with
human review and correctness measurement, alongside validation sets, data
splits, and statistics
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
Precision, recall, accuracy, and careful measurement still matter even when the
product uses generative models or agents
([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).

Large eval sets slow iteration. Every prompt, retrieval change, or model change
becomes more expensive to check. Set size is a cost and coverage tradeoff. It
should be large enough to avoid overfitting to a few examples, but small enough
that teams actually run it
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
When repeated prompt prefixes or stable context blocks drive cost instead of
quality, [[Caching]] belongs in the serving path rather than the eval set.

Representativeness matters more than raw count. Hugo's eval-set discussion ties
gold tests to cost and failure coverage. A small set can be useful when it
covers the product's common tasks and known edge cases. A larger set can still
miss the real failures if it only repeats easy examples
([[cite:practical-llm-engineering-and-rag@23:00=>LLM Evaluation Sets]]).

[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] covers decisions where evaluation
has to separate prompt or retrieval fixes from model-behavior changes through
fine-tuning.

## Cheap Checks Before LLM Judges

Practitioners differ most on what should judge the system and where to spend
money. A cost-aware approach uses simple assertions, structured output, regular
expressions, and string matching when the expected behavior is easy to check.
Cheaper models and spreadsheets can also keep iteration affordable. Save
LLM-as-judge calls for cases where deterministic checks are too brittle
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

This keeps eval sets runnable. A representative set that runs during prompt,
retrieval, and model changes is more useful than a large set that waits until
after release.

In enterprise agent settings, teams make LLM judges more explicit. They use
golden datasets and pass thresholds. They also train judges against human
labels. Red teaming and guardrails belong in the same workflow
([[cite:s23e03-future-of-ai-agents@50:18=>The Future of AI Agents]]). Judges can be
biased, so teams must validate the judge instead of treating it as an oracle.

When those human labels become reusable judge-training evidence,
teams need the guidebooks and agreement checks described in
[[annotation-quality-workflows=>Annotation Quality Workflows]]. Review queues
keep the labels from becoming another noisy evaluator.

Multi-tenant products add another evaluation boundary because each customer can
have different data, policies, and pass thresholds. That pushes LLM evaluation
toward tenant-specific golden sets and [[agent-ops=>Agent Ops]] traces rather
than one global benchmark.[[cite:s23e03-future-of-ai-agents@43:30=>The Future of AI Agents]]

## Human Review and Failure Analysis

Human review is most useful when the team is learning the failure taxonomy.
Common failure types include unsupported answers and missing citations. Wrong
tone and unsafe advice also belong in the same review. So do stale knowledge,
broken formatting, and tool misuse
([[cite:practical-llm-engineering-and-rag@26:43=>LLM Failure Analysis]]).

Spreadsheet-style failure analysis lets teams categorize failures and rank the
largest error classes. That helps them avoid spending engineering time on minor
formatting when the major problem is retrieval quality
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Hugo's failure-analysis path treats error categories as product backlog input.
If the largest group is missing source material, the next change belongs in
chunking, retrieval, or indexing. If the largest group is bad formatting, a
schema or deterministic check may be enough
([[cite:practical-llm-engineering-and-rag@26:43=>LLM Failure Analysis]]).

This keeps [[Testing]] and [[Evaluation]] close together: tests catch repeatable
failures, while review discovers which failures matter.

Teams use automated checks to make that review repeatable. Deterministic checks
can validate JSON schema, exact fields, and required citations. They can also
check forbidden strings, SQL syntax, tool parameters, and regular expressions.

Other checks need semantic judgment, so the LLM-judge version raises a second
eval problem. Teams must compare automated judgments against human labels and
watch for judge bias
([[cite:s23e03-future-of-ai-agents@50:18=>The Future of AI Agents]]).
Teams are evaluating the judge in that comparison, but the human judgment
records still need annotation-quality controls before they become a gold set.

## Retrieval Boundaries

Teams should triage source-lookup failures without turning this page into the
RAG playbook. A bad answer can come from missing source documents or stale
indexes. Prompt wording, tool misuse, or a model that ignores available
evidence can cause the same symptom. Failure analysis asks whether the next fix
belongs in [[context-engineering=>context engineering]] or prompting. The fix
may also belong in model behavior, product policy, or the retrieval layer
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Use [[rag-evaluation-workflow=>RAG Evaluation Workflow]] for corpus setup,
ranking checks, source references, and review fields. Use
[[Production Search Evaluation]] when the problem is search quality rather than
answer behavior
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
LLM-specific evaluation still centers eval sets and judges. It also includes
human review, traces, guardrails, and production feedback.

## Agent and Tool Evaluation

Agent evaluation adds software behavior to answer quality. Public benchmarks
such as SQuAD evaluate model capability, not the deployed system
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Teams therefore need custom datasets that represent user goals, tool
constraints, and product workflows.

Agent testing is close to ordinary
[[testing]] and
[[orchestration]]. Teams can mock external tools, assert outputs, and check tool
names and parameters. They still keep integration tests for the real systems.

A calendar-agent example shows why outcome assertions matter more than exact
trace matching. Several valid action paths can create the same correct invite
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@53:20=>Agent eval]]).
The same rule applies to SRE-style agents. Mock logs and metrics in regression
tests before letting the agent touch live systems.

That's why goal-based agent evals should assert the product outcome, not the
exact reasoning path. Regression tests can preserve known successful outcomes
while allowing the agent to choose a different valid sequence of tool calls
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@56:02=>Building Agentic AI Systems]]).

## Production Feedback and Traces

Production behavior keeps offline eval sets fresh through explicit and implicit
feedback. Explicit feedback can be thumbs up or down. Implicit feedback can be a
repeated or reframed query after a bad answer
([[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]). Those signals
can become [[synthetic-data=>synthetic data]], human labeling work, or new gold
cases. They can also lead to updated prompts, fine-tuning examples, or new
guardrail tests.

Production feedback also needs traces. Logs and traces let the team reconstruct
whether the wrong output came from retrieval,
[[context-engineering=>context engineering]], tool use, or generation
([[cite:practical-llm-engineering-and-rag@27:38=>LLM Logs and Traces]]).
For vibe-coded MVPs, the same rule applies earlier. Add logging and trace views
while the prototype is still small. The team can then see prompt inputs,
retrieved context, function calls, and outputs before the workflow grows.

This puts LLM evaluation next to [[Model Monitoring]]
and [[LLM Production Patterns]]
instead of leaving it as an offline score.

## Governance and Guardrails

High-risk LLM workflows need more than accuracy checks. Enterprise agents need
logging and auditability, as well as data lineage and guardrails. Compliance
also matters in sensitive settings such as healthcare and finance
([[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]). Evaluation in
those settings belongs with
[[Responsible AI and Governance]].

Guardrails can be evaluated like any other product behavior. Unsafe requests
should be refused or routed, and sensitive data shouldn't leak through
retrieved context. Citations should reference allowed sources. Tool calls should
stay inside permission boundaries. Red-team cases then become part of the same
regression suite as ordinary product examples.
