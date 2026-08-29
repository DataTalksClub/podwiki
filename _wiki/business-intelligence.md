---
layout: wiki
title: "Business Intelligence"
summary: "How business intelligence connects metrics, dashboards, data products, governance, product analytics, and AI-assisted analysis."
related:
  - Analytics Engineering
  - Data Warehouse
  - Metrics
  - Data Products
  - Data Product Adoption
  - Product Analytics
  - Text-to-SQL
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - Data Governance
  - Data Trust and Strategy
  - AI Powered Business Intelligence
  - AI for Finance Decision Support
---

Business intelligence turns modeled data into dashboards, metrics, reports, and
decision routines. BI sits between [[analytics engineering]] and
[[data-warehouse=>data warehouses]]. It also sits between [[metrics]] and the
business meetings where people act on the numbers.

The newer BI interface can use AI, but AI changes the interface more than it
replaces analytics fundamentals. Natural language can help people ask better
questions and find governed data. It can also draft first-pass analysis.
[[text-to-sql=>Text-to-SQL]] is the structured query version of that interface.
[[ai-powered-business-intelligence=>AI in Business Intelligence]] covers the
narrower AI-assisted BI design, including governed metrics, source display, and
human review.

It can also turn unclear definitions and fragile pipelines into
confident-sounding answers. Useful BI still depends on owned
[[data products]] and trusted
metrics. It also needs access controls and user research. The decision context
has to be clear.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]][[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]
That makes BI a visible surface for
[[data-trust-and-strategy=>data trust and strategy]].

## Business Questions to Governed Answers

The BI layer reduces the distance between a business question and a usable
answer. In AI-assisted BI, that layer can include natural-language access over
metrics or a text-to-SQL assistant. It can also include semantic search over
documentation or an analyst copilot that drafts a first explanation before
human review.

Urban data science gives a concrete version of this workflow. Transport
analytics teams combine fare-card records with sensors and GPS. They also use
computer vision, historical data, and real-time APIs. Natural-language access
and text-to-SQL sit on top of metadata and retrieval infrastructure. Query
restrictions make the interface safer.[[cite:urban-data-science=>Urban Data Science]]

That's the useful model for AI-powered business intelligence. The interface
gets easier, but the underlying BI system still depends on modeled data and
metadata. It also depends on permissions and domain knowledge. The related
foundations are [[data products]] and
[[retrieval-augmented-generation=>RAG]], with
[[LLM production patterns]]
for review and guardrails.

## Reporting Layer, Product Surface, and Operating Routine

BI sits downstream of warehouses and marts after modern-stack transformations.[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering]]

BI also appears as a last-mile product adoption problem. Dashboards and
analytics tools have to reach the meetings where decisions happen.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

The [[ai-powered-business-intelligence=>AI in Business Intelligence]] interface
adds natural-language queries and LLM summaries. Those features help only when
definitions, permissions, and human review already exist.[[cite:urban-data-science=>Urban Data Science]][[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]

## Metrics, Dashboards, and Decisions

BI routines are most useful when they start from repeated decision patterns,
not novelty. A sales leader may ask why pipeline conversion dropped. A product
manager may ask whether an experiment should ship. A finance team may ask which
budget variance needs attention.

When the product-manager question is the analyst's main surface,
[[product-analyst-vs-data-analyst=>product analyst vs data analyst]] separates
that role from broader BI and reporting work.
When repeated KPI and dashboard logic starts moving into modeled tables, metric
definitions, and tests, analysts are changing the work they own. The
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer]]
transition runs from BI reporting into analytics
engineering.[[cite:from-math-graduate-to-data-analytics=>How to Break into Data Analytics]]

AI helps only if the system can find the right metric and explain the
definition. It also has to identify caveats and route uncertain answers back to
an analyst.

[[person:caitlinmoorman=>Caitlin Moorman]]'s last-mile
data delivery episode is the strongest reminder that BI adoption is product
work. Teams start from the decision they want to enable. Then they map
metrics into real meetings. They prototype quickly and prove impact with
narrow wins.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

AI follows the same adoption rule as ordinary BI. A conversational interface
doesn't remove discoverability, interpretability, trust, or decision context.
Teams should place
[[ai-powered-business-intelligence=>AI in Business Intelligence]] inside the
same adoption work instead of a separate chatbot pilot.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

[[person:anushaakkina=>Anusha Akkina]] describes another
useful workflow in her finance episode. Finance teams often work around rigid
ERP systems with spreadsheets and local business logic. They also rely on tribal
knowledge. Strategic finance, spreadsheet dependency, user research, and
real-time decision insights all influence the BI interface. For the finance
product version, use
[[ai-for-finance-decision-support=>AI Finance Decision Support]].

For AI-assisted BI, the practical takeaway is direct. The system has to meet
people inside existing finance workflows instead of assuming a clean data
environment.[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>Augmented Finance Decisions]]

For product teams, AI-powered BI also overlaps with
[[product analytics]]. Product
analytics tools make funnels, cohorts, journeys, and experiments easier to
study. BI and warehouse models handle broader joins and governed reporting. AI
can summarize these views, but the answer is only usable when metrics, tracking
plans, and experiment design are sound.

## AI-Powered Business Intelligence

Teams usually build AI-powered BI around three layers.

1. Governed data products with modeled tables, metrics, semantic definitions,
   ownership, freshness expectations, and known limitations.
2. Retrieval over definitions, dashboards, documentation, and approved examples.
3. Constrained answers with SQL safety, source citations, confidence signals,
   and human escalation when the question is ambiguous.

This is where [[data products]] and
[[retrieval-augmented-generation=>RAG]] meet. RAG can ground an answer in
business definitions and metric documentation. It can also use dashboard notes
and previous analysis. It shouldn't be treated as a guarantee that the final
answer is true.

[[person:sandrakublik=>Sandra Kublik]]'s LLM product
discussion keeps the same caution. Useful LLM applications need
human-in-the-loop review for hallucinations and brand safety. Teams also need
controls for latency, data risk, cost, and model-choice tradeoffs.[[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]

In BI, the system should show where an answer came from:

- A summary should link to the metric, dashboard, query, or source document.
- A SQL query should be reviewable before it runs against sensitive data.
- An explanation should name assumptions, filters, and joins.

Without those controls, AI-powered business intelligence becomes a faster way
to spread unreviewed analysis.

## Governance and Access

Governance isn't a blocker to AI-powered BI because it makes broader access safe
enough to allow.

[[person:bartvandekerckhove=>Bart Vandekerckhove]]'s
data access management episode frames governance as trust in data, not just
compliance. Catalogs and dictionaries sit beside lineage, access management,
and ownership.

Approval workflows, access reviews, revocation, and masking cover the access
side. Filtering, active metadata, and access-as-code appear in the same
discussion.[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]]

For BI powered by AI, a chatbot shouldn't become a side door around permissions.
The assistant needs to inherit the user's access and respect sensitive fields.
It should explain why access is denied. It should also avoid exposing raw
records when an aggregate is enough.

The governance model also needs audit trails. Teams should know who asked a
question, what data was retrieved, which query ran, and what answer was shown.

The broader [[data governance]]
page connects those controls to classification, catalogs, policies, and lineage.
It also covers quality signals, retention, access workflows, and stewardship. AI
changes the interface, but it doesn't remove the need for ownership and policy
automation.

## Trust Comes From Product Adoption

Trust in AI-powered BI is earned in the same way as trust in ordinary BI. The
answer has to be timely, explainable, useful, and correct often enough for the
decision at hand. AI also adds new failure modes. It can write plausible
explanations for stale data. It can generate SQL that joins the wrong grain,
hide uncertainty, or summarize a dashboard without understanding the business
context.

That's why [[data product adoption]]
matters. Adoption work starts with the intended decision and works backward
through user research, prototypes, meeting rituals, and impact measurement.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

Teams building AI-powered BI should do the same by watching how people use
answers. Sales and finance workflows matter alongside product and operations
workflows. Executive reviews matter as well.

Measure whether the assistant reduces analyst follow-up load or speeds up
recurring review meetings. Also measure whether it improves decision quality or
simply creates another place to check.

Trust also requires feedback loops. People need a way to flag wrong answers,
unclear definitions, and missing data. They also need to flag broken
permissions.

Analysts need access to those failures because that evidence helps them improve
semantic definitions and examples. It also helps them improve tests, retrieval,
and guardrails.

## Limits and Failure Modes

BI powered by AI is a bad fit when the organization lacks shared metric
definitions, ownership, data quality signals, and an access model. In that
environment, a natural-language interface may make analytics feel modern while
making the actual decision process worse.

Several limits are predictable:

- Natural language can hide ambiguity. "Revenue," "active user," and "churn"
  may have multiple valid definitions.
- Text-to-SQL can produce syntactically correct but analytically wrong queries.
- RAG can retrieve outdated documentation or miss the dashboard that matters.
- LLM summaries can overstate certainty when data is stale, sparse, or
  contradictory.
- Broad access can expose sensitive data unless permissions, masking, and
  auditing are enforced.
- Cost and latency can make interactive BI worse if the AI layer is added to
  every question without prioritization.

[[person:sandrakublik=>Sandra Kublik]]'s LLM episode is
useful here because it frames LLMs as product components with tradeoffs, not
magic.

Model choice and embeddings matter alongside prompt iteration and fine-tuning.
Teams also have to consider proprietary APIs, open-source models, IP concerns,
and data risk. Latency and cost matter too.[[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]
The [[LLM production patterns]]
page extends the same point. Evaluation, observability, guardrails, and human
review are production infrastructure.

## Starting With One BI Routine

Start with one decision-heavy BI routine, not a company-wide assistant. Pick a
recurring meeting or analysis where the data is already mostly trusted and the
business value is visible. Begin with a decision, prototype around real
meetings, and use adoption evidence before expanding.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

Good candidates include:

- experiment readouts
- pipeline reviews
- budget variance analysis
- customer health reviews
- product funnel diagnosis
- operational incident summaries

A practical first version can be simple:

1. Choose one workflow and name the decision it supports.
2. Identify the governed metrics, dashboards, tables, and documents it may use.
3. Add retrieval over metric definitions, dashboard notes, and source docs.
4. Restrict generated SQL to approved datasets and read-only queries.
5. Show citations, filters, assumptions, and freshness in the answer.
6. Require analyst review for high-stakes or externally visible decisions.
7. Track adoption, wrong-answer reports, time saved, and decisions changed.

Business intelligence with AI should stay close to the recurring BI lesson.
A BI product succeeds when people trust it enough to use it inside real
decisions. LLM product work adds the AI-specific constraint. Teams still need
review and evaluation. They also need latency controls, cost awareness, and
data-risk controls before a generated answer should influence a high-stakes
decision.[[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]

## Related Topics

Adjacent pages cover the modeled data, trust, and product surfaces behind BI.

- [[data products]]
- [[data product adoption]]
- [[LLM production patterns]]
- [[retrieval-augmented-generation=>RAG]]
- [[data governance]]
- [[product analytics]]
