---
layout: wiki
title: "Data Strategy"
summary: "Data strategy as the link between business goals, operating models, governance, platforms, adoption, and tool choices."
related:
  - Data Engineering Platforms
  - Data Product Management
  - Data Governance
  - Data Products
  - Data Product Adoption
  - Data Mesh
  - Data Mesh vs Centralized Data Platform
  - Data Teams
  - AI for Social Good
  - Data Translator Role
  - Communication
---

Data strategy links data work to business goals. Teams use it to choose which
problems deserve data investment and who owns the work. They also choose which
platform capabilities matter, which data requires governance, and how data will
change decisions or workflows.

Data strategy isn't a static plan or a tool shopping list. It works through
domain ownership and self-service platforms. Governance scope belongs there
too. It also covers event tracking, DataOps, vendor selection, and adoption.
The strategy matters only when teams ship trusted [[data products]] and
dependable [[data engineering platforms]]. It also has to create useful
business workflows.[[cite:data-strategy-and-dataops-for-ai-powered-products=>Data Strategy and DataOps]]

[[ai-for-finance-decision-support=>Finance decision support]] is one such
workflow because ERP and CRM data have to support CFO planning. Expense and
operating data also need to stay usable instead of trapped in rigid systems or
side spreadsheets
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]].

## Business-First Choices

Data strategy is a practical set of business and operating choices. Teams start
from business questions and constraints, then work backward into data collection
and platform design. They define ownership, quality, governance, and delivery.

At executive scope, the [[chief-data-officer-role=>Chief Data Officer role]]
owns that horizontal view. It connects business lines with infrastructure,
governance, analytics, and AI. Marco De Sa frames the CDO as the leader who
turns strategy into goals, resources, and owned work
[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]].

[[person:boyanangelov=>Boyan Angelov]] makes that definition more operational.
He describes strategy as a plan to get value from data. The plan has to be
actionable and flexible enough to change once teams start using it
[[cite:data-strategy-and-dataops-for-ai-powered-products=>Data Strategy and DataOps]].
That means a strategy deck isn't just a list of goals. It needs connected
artifacts such as data dictionaries, use-case notes, and due-diligence findings
that let teams adjust the plan as evidence changes.

[[person:arpitchoudhury=>Arpit Choudhury]] gives the
growth-stack version. Teams document events, properties, and ownership in a
tracking plan before they rely on product data. The stack then moves from
collection to storage, analysis, and activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
The modern growth stack includes collection and product analytics alongside a
warehouse and reverse ETL. That keeps the strategy tied to questions and
workflows instead of isolated tools.

[[person:jessiashdown=>Jessi Ashdown]] and
[[person:urigilad=>Uri Gilad]] give the governance
version. Start with the reason for governance, then build minimum viable
governance that can expand later
[[cite:cloud-data-governance=>Cloud Data Governance]].
This puts [[data governance]] inside
data strategy because the right policy depends on risk, use case, data
sensitivity, and business value.

[[person:christopherbergh=>Christopher Bergh]] gives the
operating-model version. Error reduction, deployment cycle time, and
productivity are the core targets. Teams should optimize the whole value stream
across silos and governance
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
[[DataOps]] turns data strategy into daily
engineering work. Without that operating layer, teams get a backlog of fragile
pipelines.

## Different Failure Modes

Data strategy should produce value, but different approaches start from
different failure modes.

[[person:zhamakdehghani=>Zhamak Dehghani]] starts from
centralized bottlenecks. Enterprise data friction drives a socio-technical
shift toward autonomy plus interoperability. In that model, ownership connects
to business domains and federated governance keeps domain autonomy from turning
into fragmentation
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]].
This puts data strategy close to
[[Data Mesh]], domain-owned
[[data products]], and shared
platform standards.

Arpit Choudhury starts from growth and activation. This strategy is less about
organizational topology and more about whether product, support, sales, and
marketing teams can act on trusted events. Event data flows into support, sales,
and engagement tools. Activation events and personalized onboarding make the
data useful outside dashboards
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
This growth-and-activation strategy belongs with
[[data activation]],
[[analytics engineering]],
and [[data product management]].

Jessi Ashdown and Uri Gilad start from governability by moving from governance
definition into classification and policy. They then ask how catalog usage,
cost, and compliance value can show return on investment
[[cite:cloud-data-governance=>Cloud Data Governance]].
This version matters when a company has many datasets, many consumers, and
unclear sensitivity or ownership.

[[person:mehdiouazza=>Mehdi OUAZZA]] starts from scale-up
pressure. The platform is self-service infrastructure for onboarding and scale,
but an Airflow cluster isn't enough. Conventions, playbooks, and best practices
make it usable. Kafka schemas, schema registry, and data contracts become
strategy because they protect downstream teams while the company moves quickly
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data Engineering Teams]].

## Business Alignment

Business alignment means choosing data work from the problem backward, not
starting from a reference architecture and then looking for a use case.

Boyan Angelov frames due diligence as the first alignment step. Teams need to
understand where the company is and what data it already has. They also need to
know what the business is trying to achieve before proposing models, platforms,
or hiring plans. In his retail example, the strategy work is translating a
business goal such as selling more products faster into feasible data use cases.
Then the team checks whether the data, skills, and infrastructure support them
[[cite:data-strategy-and-dataops-for-ai-powered-products=>Data Strategy and DataOps]].

Boyan uses a design loop to turn that alignment into intake discipline. Teams list
candidate use cases after due diligence and test feasibility against current
data, skills, and infrastructure. They then prioritize by business impact. A
small change in a use case can cascade into new storage, NLP skills, target
architecture, and governance needs. Teams have to catch scope creep before
delivery starts
[[cite:data-strategy-and-dataops-for-ai-powered-products=>Data Strategy and DataOps]].

That connects data strategy to [[Data Product Intake and Prioritization]],
[[machine learning for business]], and
[[data-science-for-managers=>data science for managers]]. Ideas need
feasibility, priority, and a business result before they become roadmap
commitments.

The growth stack makes this visible at the event level. A tracking plan forces
product and data teams to agree on the important events, the properties that
describe them, and the team that owns changes. A signup event, invoice event, or
project creation event matters because teams can use it in product analytics and
support context. It can also drive lifecycle messaging or personalization
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].

[[person:alexanderhendorf=>Alexander Hendorf]] adds the
enterprise AI version. That version keeps AI initiatives and experiments aligned
with company goals. It also avoids hype-driven work without evaluation and
transparency, and favors impact and "good enough" engineering over perfection
[[cite:scaling-enterprise-ai-mlops-data-first-strategy=>Scale Enterprise AI]].

[[person:andreyshtylenko=>Andrey Shtylenko]] gives the industrial AI version.
The executive sponsor shapes the strategy, so reporting lines matter. CTO
reporting tends toward product capability, while CIO reporting tends toward
internal optimization. CMO reporting points toward marketing and sales analytics.
CEO reporting points toward cross-functional data work.

He ties that sponsor choice to a practical warning. Start from customer or
business value, then choose the talent, algorithms, and infrastructure. Don't
start from a shiny technology and search for somewhere to plug it in
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops=>Industrial AI and MLOps Practice]].

Lior Barak connects the [[data-translator-role=>data translator role]] to the
same lean-delivery strategy. Build the smallest prototype that can test value.
Then decide whether the use case deserves production ownership. A spreadsheet
can prove that a business workflow should change. A quick dashboard, hackathon
tool, or one-week front end can do the same.

Another owner may then rewrite the rough code or automate the manual proof. The
team shouldn't treat the prototype as the final system
[[cite:data-translator-role-and-data-strategy@23:54=>Data Translator Role and Data Strategy]]
[[cite:data-translator-role-and-data-strategy@29:19=>Data Translator Role and Data Strategy]].

OKRs and iteration are useful only when they leave room for this learning. A
short diversion can miss part of a target while still saving more time than it
costs.

Prototype-first strategy also needs expectation-setting. The first version can
move fast because it uses the minimum ingredients. Later features need more
design, maintainability, and ownership because the team has moved from proving
value to supporting a product
[[cite:data-translator-role-and-data-strategy@34:52=>Prototype versus product]].

That same strategy boundary shows up in
[[ai-for-finance-decision-support=>AI Finance Decision Support]]. A spreadsheet
or quick interface can prove the finance decision flow. Teams need governed ERP
and CRM context before the product can support planning reliably
[[cite:s22e06-from-black-box-systems-to-augmented-decision-making=>From Black-Box Systems to Augmented Decision-Making]].

AI and ML strategy belong in the same frame. Projects need a business reason, a
data path, an evaluation plan, and an operating model. The production side
overlaps with [[MLOps]] and the
[[machine learning engineer role]].

Different strategic problems need different success measures. DataOps looks at
error reduction, cycle time, and productivity
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Governance looks at ROI plus compliance value
[[cite:cloud-data-governance=>Cloud Data Governance]]. Growth looks at
activation plus self-service access
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].

## Operating Model

A data strategy has to name the operating model. It should say who owns
domains and who runs the platform. It should also say who approves access, who
handles incidents, and who supports consumers.

The Data Mesh model gives one end of the spectrum. Domain teams own data because
they understand the business context. The model uses shared metadata, identity,
authorization, and interoperability to keep that ownership usable across the
organization
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]].
[[Data Mesh vs Centralized Data Platform]] covers the ownership tradeoff between
domain autonomy and central platform control.

Self-service platform abstractions reduce the burden on domain teams. The
organization may be ready to pair domain ownership with shared standards. When
it isn't, the central platform should keep more operating responsibility.

Mehdi OUAZZA gives the scale-up platform version. The platform enables
onboarding and scale, with work split between platform engineering and use-case
pipelines
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data Engineering Teams]].
[[Data teams]]
need that balance because a platform-only team may lose contact with business
needs, while a request-only team may never create reusable capabilities.

Christopher Bergh gives the reliability version. It separates leadership habits
from tooling automation and adds version control, tests, and CI/CD.
Documentation and replaceability reduce dependency on individual people. The
operating model lives in everyday engineering practice rather than an org chart
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

## Governance and Risk

Governance is part of data strategy when data creates risk, trust problems, or
coordination cost. Maximal governance isn't right for every team.

Cloud governance is explicit about scope. Minimal governance is fine when the
organization doesn't need a large program. Data classification and taxonomy come
next. Policies cover retention, freshness, and purpose-based access
[[cite:cloud-data-governance@19:40=>Cloud Data Governance]][[cite:cloud-data-governance@24:14=>Cloud Data Governance]].
Those policies keep
governance tied to decisions the team can explain.

A federated model automates shared policy enforcement across domain-owned data
products
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]].
Data Mesh treats retention, metadata, validation, and contracts as operating
controls. Strategy decides whether those controls can move closer to domains. It
can also keep them centralized until the organization can operate them
consistently.

Alexander Hendorf extends risk into AI and ML. Production systems in that frame
need retraining, feedback loops, and MLOps automation. Standardization and CI/CD
sit beside governance and reproducibility on the path from experiment to
production
[[cite:scaling-enterprise-ai-mlops-data-first-strategy=>Scale Enterprise AI]].
Data strategy should decide where governance belongs before a model becomes a
product dependency.

## Platform and Tool Choices

Tool choices belong after strategy, not before it. The guests still give clear
guidance on which capabilities teams often need.

The growth stack maps from collection through activation. It starts with event
collection tools and warehouse-first analytics, then adds reverse ETL and
operational analytics
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
Those tools matter when the strategy depends on product events moving into
analysis and customer-facing workflows.

Platform tools need conventions around them because Airflow matters, but the
lesson is broader than orchestration. Reusable templates, playbooks, and naming
practices help engineers onboard quickly and keep pipelines understandable.
Kafka schemas and contracts serve the same purpose for event-driven systems
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data Engineering Teams]].
[[Apache Airflow]]
and [[streaming]] cover those platform
choices in more detail.

[[person:adrianbrudaru=>Adrian Brudaru]] gives the
modern-stack caution. The caution treats packaged modern data stacks as targets
for criticism in favor of open-source alternatives. Apache Iceberg and catalogs
separate storage from compute, with access, metadata, and lineage sitting in the
catalog layer
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering]]. Tool
selection comes with a warning about vendors. Architecture decisions stay tied
to lock-in, cost, maturity, and team capability.

## Adoption and Value

Data strategy succeeds when people use data to make better decisions or run
better workflows. Tables, dashboards, models, and catalogs aren't enough. At
strategy level, leaders decide which decisions matter, which teams own the
workflow change, and which measures prove value.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@08:48=>Last-Mile Data Delivery]]
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@34:00=>Last-Mile Data Delivery]]

Data democratization connects to literacy, documentation, and self-service
analytics
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
Governance policies act as guardrails for democratized access, not only as
restrictions [[cite:cloud-data-governance@42:04=>Cloud Data Governance]].
Request workflows can make that guardrail feel like a shopping-cart access path
rather than a bespoke ticket queue
[[cite:cloud-data-governance@47:02=>Cloud Data Governance]]. Early
releases and customer iteration beat heroic delivery
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
[[Data Product Adoption]] covers the user research, enablement, and behavior
measurement that follow from those strategy choices.

The discussion around Data is Like a Plate of Hummus uses the same
foundation-first logic. Teams need stable ground, shared understanding, and
usable data before models or advanced automation can support a business decision
[[cite:data-translator-role-and-data-strategy=>Data Translator Role and Data Strategy]].

Boyan adds a budgeted-use-case version of adoption. When pitching a strategy to
a business stakeholder, start with one small use case. Avoid technical language,
name the budget, and ask for a clear yes-or-no commitment. Then set a baseline
before implementation. Later impact reviews can compare pre- and post-launch
business metrics
[[cite:data-strategy-and-dataops-for-ai-powered-products=>Data Strategy and DataOps]].

[[person:parvathykrishnan=>Parvathy Krishnan]] brings
the same logic into the nonprofit sector. Data maturity spans people, process,
and technology dimensions. Discovery workshops assess where a nonprofit
actually stands before tools are chosen.

The progression runs from descriptive to prescriptive curriculum, while team
profiles range from analysts to data engineers. Optimization use cases include
waste-collection routing and healthcare
access
[[cite:data-science-and-analytics-for-nonprofits-tech-for-good=>Analytics for Nonprofits]].

The strategy question is the same as in private-sector teams. Invest in people,
processes, and technology together, or the data never changes decisions.
