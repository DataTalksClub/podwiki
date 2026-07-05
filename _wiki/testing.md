---
layout: wiki
title: "Testing"
summary: "Testing data, ML, and AI systems through data checks, CI/CD, evaluation sets, monitoring, and production readiness practices."
related:
  - DataOps
  - CI/CD
  - Data Quality and Observability
  - Evaluation
  - LLM Evaluation Workflows
  - Production
---

Testing in data, ML, and AI systems checks whether a change preserves behavior
that downstream users depend on. Data teams test tables, dbt models, and batch
pipelines. ML and AI teams test trained models, retrieval systems, prompts, and
agents that call external tools.

Testing connects [[dataops=>DataOps]] and [[ci-cd=>CI/CD]] with
[[data-quality-and-observability=>data quality and observability]], and it also
sits beside [[evaluation]], [[production]], and [[model-monitoring=>model monitoring]].
Tests encode expectations a team can name before release, while monitoring
catches behavior the team didn't know how to encode yet.

## Testing Scope

Testing covers known failure modes before they reach a user. Data teams usually
encode data-quality assertions and transformation checks. They also use
realistic test data and regression suites. CI/CD gates run those checks before
release.

ML teams add offline evaluation sets and baselines, while AI teams add prompt
and [[retrieval-augmented-generation=>RAG]] evaluations. AI teams also add
tool-call tests, traces, and production feedback loops.

No single tool defines testing here. A team names the behavior it depends on
and turns that expectation into an automated check where possible. It still
needs monitoring for failures the test suite can't predict.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]][[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

## Boundaries and Tradeoffs

The boundary between testing, evaluation, and monitoring changes by system type.
Analytics engineering leans on dbt tests and source checks near the model
definition. DataOps discussions focus on automated regression tests, realistic
test data, version control, and CI/CD. LLM and agent discussions often call the
same discipline evaluation. Their outputs are language, retrieval behavior, or
tool use rather than a single table constraint.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

The system type also changes what counts as enough. A dbt non-null test can pass
by returning no failing rows. A data pipeline may need an integration or
snapshot test that proves representative input produces an expected output. An
agent test may need to verify the final outcome and required constraints. It
shouldn't force one exact reasoning path.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]][[cite:production-ready-ai-engineering=>Production AI Engineering]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Test Assertions

Data and AI tests work best when the team can name the failure before release.
A dbt test can assert that a column isn't null. Other tests can check city names
or numeric ranges. In dbt, these tests run as queries that return failing rows.
They can stop downstream models before reports build on bad source data.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

Pipeline tests often need representative input and expected output rather than
only small unit tests. A team can run the pipeline, observe acceptable outputs,
and turn those examples into integration or snapshot tests. Naming those tests
after the business rule they protect makes failures easier to debug.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Agent tests extend the same idea to tool use. A test can mock external systems
and assert that the agent calls the right tool with the right parameters. It can
also check whether the final answer satisfies the required constraints. A
calendar, SRE, or enterprise agent can fail through a bad tool call even when
the generated text looks plausible.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Data and Analytics Tests

[[analytics-engineering=>Analytics engineering]] testing puts checks near the
shared model definition instead of leaving them as one-off analyst queries. SQL
files, YAML documentation, version control, and tests live together. With those
checks in place, a team can see whether a shared business definition still
holds. The check runs when source data or transformation logic changes.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

Documentation and peer review support the same reliability goal. Good SQL and
tests protect shared reporting logic, while guidelines and review practices add
the human check a reused metric needs.[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]

Data-pipeline tests add a broader production check. A pipeline can run
successfully and still publish an output nobody should trust. Teams need tests
that prove the data moved through the expected transformation, not only that the
job finished.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

## CI/CD and Pipeline Regression

Testing becomes more useful when it runs automatically. DataOps ties safe
change to regression tests and automated deployment. It also relies on realistic
test data, monitoring, infrastructure as code, and test environments.

Git alone isn't enough when a team needs end-to-end confidence before production.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
When the tested change includes infrastructure or access,
[[gitops-for-data-teams=>GitOps for data teams]] adds the branch-plan-review
path around those checks.
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]]

Teams can use dbt tests, Great Expectations, SQL checks, and other strategies
that fit the pipeline. The exact tool matters less than proving a change with
data before relying on it downstream. Use
[[dataops-checks-for-data-pipelines=>DataOps checks for data pipelines]] for the
pipeline-specific version of those gates.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Testing belongs beside [[ci-cd=>CI/CD]] and [[reproducibility]] because a data
or ML release has to preserve code, data, artifacts, and tests. It also has to
preserve metadata and deployment behavior. Without that relationship, a team may
know a pipeline passed once but still not know what changed after a failure.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

When teams use [[ai-coding-tools=>AI coding tools]] inside pull requests or CI,
the same rule applies. The generated changes need runnable tests and a readable
diff. Reviewers still need to check them before they become production code.

Coding assistants can speed up scaffolding and refactoring. The release still
depends on the team's existing test and review loop.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

## Evaluation for ML, Search, and LLM Systems

Some systems need evaluation sets rather than pass/fail data checks. ML and
search applications ask whether the system performs well enough against
representative cases and a meaningful baseline. [[retrieval-augmented-generation=>RAG]]
and LLM applications ask the same question with language-specific checks.

Gold test sets for LLM applications play a role similar to holdout and test
sets in machine learning. Natural language and tool calls make the practice
different, but not every case needs an LLM judge. Teams can use structured
output checks and regular expressions. They can also use string matching,
cheaper models, and human review.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]][[llm-evaluation-workflows=>LLM Evaluation Workflows]]

Teams turn evaluation into engineering work by categorizing errors and ranking
the largest failure classes. If most failures come from retrieval, fixing
retrieval comes before polishing formatting. This connects testing to
[[retrieval-augmented-generation=>retrieval-augmented generation]] and
[[production-search-evaluation=>production search evaluation]].[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

## Agent and Tool Tests

Agent systems add tool behavior to answer quality. Public benchmarks measure
model capability, not the deployed [[agent-engineering=>agent engineering]]
system. Production teams need datasets that represent real users and product
tasks.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Agent tests often mock tools, assert outcomes, and add integration or regression
checks. They should usually assert the outcome and required constraints, not
every intermediate step. An LLM can reach the same acceptable result through
more than one path.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

That boundary matters for [[agent-engineering=>agent engineering]] and
[[llm-production-patterns=>LLM production patterns]]. A brittle test that
hard-codes one reasoning path can reject a correct answer. A loose test can
miss a harmful tool call or broken product constraint.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Monitoring After Tests Pass

Tests don't remove the need for production monitoring. A pipeline can complete
successfully while publishing late, incomplete, shifted, or semantically wrong
data. Freshness and volume checks cover failures that a job-status check
misses. Distribution, schema, and lineage checks cover another set of failures.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Tests specify what the team already knows might go wrong. Monitoring and
observability help the team notice new failures and diagnose root cause. That
is why [[data-quality-and-observability=>data quality and observability]] and
[[dataops=>DataOps]] sit next to testing instead of after it. Data engineering
teams use
[[data-observability-for-data-engineering=>data observability for data engineering]]
to turn that boundary into freshness and schema checks, lineage review, and
runbook ownership.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

For ML and AI systems, monitoring checks whether evaluation still holds after
launch. A feature distribution can shift, labels can arrive late, a schema can
change, or an upstream retrieval index can become stale. Use
[[model-monitoring=>model monitoring]] when the alert concerns model behavior
and [[mlops=>MLOps]] when the work includes training, deployment, rollback, and
model lifecycle control. Use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
to separate those model-specific alerts from the data reliability signals that
the team already tracks.

## Production Readiness

Production readiness starts when tests and evaluation meet monitoring and
ownership. A team should be able to run the system, know when something is
wrong, make changes safely, and onboard another person into the work.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Trust is part of that readiness. When a dashboard number looks wrong, confidence
is hard to regain. Tests don't prove perfection, but they give the team a
concrete check to rely on during debugging.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

For LLM and agent systems, production readiness adds representative test sets
and failure analysis. It also adds traces, mocked tool tests, outcome
assertions, and feedback from real use. A demo becomes a system only when the
team can change it, check it, observe it, and respond when it fails.
[[llm-production-patterns=>LLM production patterns]],
[[llm-evaluation-workflows=>LLM evaluation workflows]], and [[production]] cover
those operating concerns.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]][[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Related Pages


- [[dataops=>DataOps]] and [[ci-cd=>CI/CD]] cover delivery and automation around tests.
- [[data-quality-and-observability=>Data quality and observability]] covers the gap between known assertions and new production failures.
- [[evaluation]] and [[llm-evaluation-workflows=>LLM evaluation workflows]] cover pre-release checks for models, retrieval, and LLM systems.
- [[model-monitoring=>Model monitoring]] and [[mlops=>MLOps]] cover checks that continue after training and deployment.
- [[analytics-engineering=>Analytics engineering]], [[agent-engineering=>agent engineering]], [[llm-production-patterns=>LLM production patterns]], and [[production-search-evaluation=>production search evaluation]] cover testing in specific system contexts.
