---
layout: wiki
title: "Testing"
summary: "How DataTalks.Club guests test data, ML, and AI systems through data checks, CI/CD, evaluation sets, monitoring, and production readiness practices."
related:
  - DataOps
  - CI/CD
  - Data Quality and Observability
  - Evaluation
  - LLM Evaluation Workflows
  - Production
---

Testing in data, ML, and AI systems means checking whether a change preserves
the behavior that downstream users depend on. The thing under test might be a
table, a dbt model, a batch pipeline, or a trained model. It might also be a
retrieval system, a prompt, or an agent that calls external tools. In
DataTalks.Club podcast discussions, guests treat testing as production
discipline rather than unit tests around application code.

Testing links [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) with
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
It also sits next to [evaluation]({{ '/wiki/evaluation/' | relative_url }}),
[production]({{ '/wiki/production/' | relative_url }}),
[data observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}), and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}). Tests
encode expectations a team knows before release. Monitoring catches behavior
the team didn't know how to encode yet.

For data teams, testing usually means data-quality assertions and
transformation checks. It also means realistic test data, regression suites,
and CI/CD gates. For ML teams, it means offline evaluation sets and baselines.
For AI systems, it means prompt evals and RAG evals. It also means tool-call
tests and production feedback loops.

## Test Assertions

DataTalks.Club guests use tests for failures a team can name before those
failures reach a user. A test can assert that a dbt column isn't null. Another
test can check that a pipeline produces an expected snapshot or that an agent
calls the right tool with the right parameters.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes the analytics-engineering version in
[Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
At 6:59, she explains how dbt brings software development habits into
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
SQL files live with YAML documentation, version control, and tests. At 39:04,
she describes dbt tests as queries that return failing rows. A non-null test
passes when the query returns nothing, and a failure can become a warning or an
error before dependent models build.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) gives the
production AI version in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 10:44, he says a team needs tests to prove a data pipeline works before it
can defend a dashboard number. At 11:53-14:04, he prefers making the pipeline
run, observing acceptable outputs, and turning those examples into tests. For
data pipelines, that often means integration or snapshot tests rather than only
small unit tests.

## Known and Unknown Failures

Teams get the most value when they already know the failure mode.

Perez Mola uses dbt tests to stop known bad source data
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
Those tests run before downstream models build.
She also says at 40:19 that teams rarely reach a point where every future
data-quality problem is covered.

[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) makes that limit
explicit in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
At 51:33-53:26 she argues that data teams need both tests and monitoring.
Tests cover expected failures while observability catches unknown unknowns.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) starts
from operating discipline rather than one testing tool. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he ties testing to the definition of "done": a pipeline isn't done merely
because a stakeholder saw a dashboard. Around 21:02, he says the system should
tell the team when something is wrong while it runs and should let someone make
a change quickly. In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
he connects that idea to CI/CD and regression tests at 30:55 and 42:39. He also
includes realistic test data, version control, and automated checks.

LLM and agent guests use the word evaluation more often than testing. They
describe the same production discipline. [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
argues in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
that teams eventually need representative gold test sets for reliable software
at 23:35-24:59.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
adds in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
that public benchmarks measure model capability, not the deployed
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}) system.
At 53:20-56:02, she frames agent checks as software tests with mocked tools.
She also includes integration tests, regression tests, and outcome assertions.

## Data and Analytics Tests

Data tests usually encode expectations about required fields, allowed ranges,
and uniqueness. They also cover source quality and transformation assumptions.
In Perez Mola's dbt discussion, tests protect analytical models from bad inputs.
She describes checks for city names and numeric ranges around 36:57. At 39:04,
she explains that source tests can block downstream models so teams don't build
reports on wrong data
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Analytics-engineering testing differs from a one-off analyst query because the
test belongs near the model definition and runs with the transformation flow.
It tells the team whether a shared business definition can still be trusted.
Documentation and peer review matter too. Perez Mola ties good SQL, tests,
guidelines, and review practices to the analytics engineer role at 42:27-44:12.

Mikulski adds another data-pipeline check: run representative input through the
pipeline and compare the output with an expected snapshot. At 13:32-14:04 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
he says unit tests are less useful for whole pipelines than integration-style
checks. Those tests can be named after the business rule they protect, which
makes failures easier to understand during debugging.

## CI/CD and Pipeline Regression

Testing becomes more valuable when it runs automatically, and Bergh's DataOps
episodes make automation the core operating point. In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
the 30:55 discussion ties safe change to regression tests and automated
deployment. It also includes monitoring, realistic test data, and
infrastructure as code. At 42:39, he warns that Git alone isn't enough. Teams
need end-to-end tests and automated checks before production.

In [Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he lists practical components at 33:47-48:25. Teams can use version control,
automated tests, CI/CD, and test environments. They can also use dbt tests,
Great Expectations, SQL checks, and other strategies that fit the pipeline. The
exact tool matters less than the habit of proving a change with data before
relying on it downstream.

Testing belongs beside [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) and
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) because a data
or ML release should preserve the relationship between code, data, artifacts,
and tests. It should also preserve metadata and deployment behavior. Otherwise a
team may know a pipeline passed once but still not know what changed after a
failure.

## Evaluation for ML, Search, and LLM Systems

Some systems need evaluation sets rather than pass/fail data checks. For ML or
search applications, teams ask whether the system performs well enough against
representative cases and a meaningful baseline. [RAG]({{ '/wiki/rag/' | relative_url }}),
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
and LLM applications need the same question with language-specific checks.

Bowne-Anderson's LLM engineering episode gives a practical LLM testing
approach. At 23:35, he compares gold test sets to holdout and test sets in
machine learning. Natural language and tool calls make the practice different,
but not every case requires an LLM judge. At 24:39-24:59, he says teams can use
structured output checks and regular expressions. They can also use string
matching, cheaper models, and human review
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})).

Failure analysis turns evaluation into engineering work. At 26:43 in the same
episode, Bowne-Anderson recommends categorizing errors and ranking the largest
failure classes. If most failures come from retrieval, teams should fix
retrieval before polishing formatting. Testing for these systems belongs with
[search, RAG, and knowledge systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

## Agent and Tool Tests

Agent systems add tool behavior to answer quality. In Kulkarni's discussion,
model benchmarks and system benchmarks are separate. At 51:42 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she says teams need datasets that represent real users. Public benchmarks
measure model capability, not the product system.

At 53:20-55:13, teams mock external tools and assert outputs as software-style
tests. They also check whether the agent tries to call the right system with
the right parameters. That matters because a calendar, SRE, or enterprise agent
can fail through a bad tool call even when the generated text looks plausible.

Kulkarni also warns against overfitting the test to one reasoning path. At
56:02, she says an LLM can reach the same goal through different acceptable
paths. For [agent engineering]({{ '/wiki/agent-engineering/' | relative_url }})
and [LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
the test should often assert the outcome and required constraints, not every
intermediate step.

## Monitoring After Tests Pass

Tests don't remove the need for production monitoring. In
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
Moses frames that gap by naming freshness and volume alongside distribution,
schema, and lineage at 16:38. At 21:57, she distinguishes a successful pipeline
run from good data. A job can complete while publishing late, incomplete,
shifted, or semantically wrong data.

Her test-driven data discussion at 51:33-53:26 gives a practical boundary.
Tests specify what the team already knows might go wrong. Monitoring and
observability help the team notice new failures and diagnose root cause. That's
why [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}) sit next to testing
instead of after it.

For ML and AI systems, monitoring also checks whether evaluation still holds
after launch. A feature distribution can shift, labels can arrive late, a schema
can change, or an upstream retrieval index can become stale. Use
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) when the
alert concerns model behavior and [MLOps]({{ '/wiki/mlops/' | relative_url }})
when the work includes training, deployment, rollback, and model lifecycle
control.

## Production Readiness

These episodes treat production readiness as the point where tests and
evaluation meet monitoring and ownership. Bergh's "done versus good" discussion
in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
gives the operating version. A team should be able to run the system, know when
something is wrong, make changes safely, and onboard another person into the
work.

Mikulski's production AI discussion makes the same point through trust. At
9:51-11:31 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
he says the phrase "this number doesn't look correct" is damaging because trust
is hard to regain. Tests don't prove perfection, but they give the team
something concrete to rely on during debugging.

For LLM and agent systems, teams add representative test sets and failure
analysis. They also add traces, mocked tool tests, outcome assertions, and
feedback from real use. The same production work appears in
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
and [production]({{ '/wiki/production/' | relative_url }}). A demo becomes a
system only when the team can change it, check it, observe it, and respond when
it fails.

## Adjacent Practices

Testing supports production confidence alongside [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), which cover the delivery
machinery around tests. [Data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [data observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
cover the gap between known assertions and new production failures. For models,
[evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
cover pre-release checks. [Model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}) cover the checks that continue
after training and deployment.

[Analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
uses tests to protect shared business definitions. [Agent engineering]({{ '/wiki/agent-engineering/' | relative_url }})
and [LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
extend testing to prompts and retrieval. They also cover tool calls, traces,
and user feedback.
[Production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
focuses on whether retrieval behavior still supports the product task.
