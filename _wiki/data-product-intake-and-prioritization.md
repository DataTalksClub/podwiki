---
layout: wiki
title: "Data Product Intake"
summary: "How teams scope data product requests with KPI framing, feasibility checks, pilots, and production handoff before committing delivery."
related:
  - Data Product Management
  - Data Products
  - Data Product Adoption
  - Data Science Project Management
  - Metrics
  - KPIs
  - Evaluation
  - A/B Testing
---

Data product intake turns an unstructured stakeholder request into a scoped
[[data-products=>data product]] commitment. Teams decide which problem enters
the funnel and which [[KPIs]] or [[metrics]] define success. They also set the
feasibility checks and choose when to say no, defer, or run a smaller
experiment.

Role and artifact context sits in [[Data Product Management]],
[[Data Products]], and
[[Data Product Adoption]].
Those pages cover the product role, the maintained artifact, and adoption in
real decisions. Intake narrows the scope to request framing and Definition of
Done documents. It also covers exploratory checks, pilots, and production
handoffs.

[[person:ioannismesionis=>Ioannis Mesionis]] gives the
clearest operating model: his easyJet example starts with embedded stakeholder
observation. It then moves
through a "single front door" and Definition of Done. The same workflow
continues through inception and EDA. R&D, pilot testing, and production rollout
come next.[[cite:building-data-products-lead-data-scientist=>Building Data Products at Scale]]

## Intake as Decision System

Intake is a decision system, not a ticket queue where every dashboard or model
automatically becomes delivery work. In Mesionis's easyJet model, the data team
works weekly with Digital, Customer, and Marketing stakeholders. That contact
gives the team business, channel, and metric context before work enters the
formal product funnel[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

[[person:boyanangelov=>Boyan Angelov]] gives the
strategy-side version of the same funnel.

After due diligence, teams brainstorm use cases around data, skills, and
infrastructure.

Boyan names the sequence as ideation, feasibility, and prioritization. The team
lists plausible use cases and checks whether data, skills, and infrastructure
make them feasible. Then it ranks them by importance and business impact
[[cite:data-strategy-and-dataops-for-ai-powered-products@13:28=>Feasibility and prioritization]].
That makes intake the front door for
[[machine-learning-for-business=>machine learning for business]] when a proposed
model has to compete on feasibility and business impact before delivery.
Teams tie intake to [[Data Strategy]] because delivery needs a clear reason and
feasibility path.

Business problems and ideas enter through one formal route. Business analysts,
finance, data science, and engineering join the kickoff. The group checks for a
real opportunity and compares the request with other ideas[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
That makes intake a prioritization mechanism for
[[data science project management]],
not only a form.

[[person:caitlinmoorman=>Caitlin Moorman]] adds the
adoption boundary.
For her, the request should be framed around the decision the product will
enable. A data team may build a dashboard or A/B testing tool. Success is
whether a product manager can use it at the moment of decision. The same rule
applies to a marketing team or operator.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

Good intake therefore asks who will act, what they'll compare, and where the
data product enters their workflow. It also asks which meeting or operating
ritual will use it.
Outcome-first intake prevents a request from becoming a polished report that
never reaches the decision.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@34:00=>Last-Mile Data Delivery]]

Moorman gives intake a ranking heuristic: start with financials and cost
centers, then choose a problem big enough to matter and small enough to move.
A narrower decision can come first when it has clearer ownership and better data
readiness than the largest spend area.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@47:52=>Last-Mile Data Delivery]]

Pareto thinking makes that ranking practical. The team looks for high-impact
questions where a small amount of analysis can change a large decision. It still
has to bring the answer to the operator at the moment of action. A technically
useful answer loses most of its value when it never enters the meeting, campaign
decision, or operations review.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@16:45=>Last-Mile Data Delivery]]

## Different Intake Risks

The guests agree that intake needs business context, but they focus on
different failure modes. Mesionis focuses on lifecycle control. His intake
model protects the team from moving into technical work before the problem,
benefits, baseline, and production meaning are agreed[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

Moorman focuses on whether the request will produce adoption. She warns that
technical availability is only table stakes, because users still need to find,
understand, and trust the product. They also need to use it in their decision
process.

Users won't adopt a data product when its cost exceeds its perceived
benefit[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]].
That shifts prioritization toward high-value decisions and low-friction
interfaces.

The first adoption candidate should also have a willing owner when possible. A
smaller project with a stakeholder who wants to make decisions with data can
create an advocate and a visible success story. Trying to convert the most
resistant owner first can turn intake into change management before the team has
proof that the product helps.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@49:25=>Last-Mile Data Delivery]]

Lior Barak focuses on translation and proof[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
Data people should sit with business users and see their workflow[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
Small automations or prototypes can come before heavier development[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
A quick MVP can prove the problem and create business
ownership[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
His version gives teams more room to validate a request with temporary work
before it becomes a formal product commitment.

## Single-Front-Door Intake

A single-front-door intake route gives data teams one path for new ideas[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
In Mesionis's operating model, the team first clarifies the problem
statement[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
A cross-functional group then reviews the request against other candidate
work[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
The front door reduces random priority changes because stakeholders see how
finance, business analysis, data science, and engineering evaluate the same
request.

The front door also works only if the team has regular contact with the
business before the request is written. Mesionis joins weekly stakeholder
meetings and learns departmental goals. He also observes how people make
decisions[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

Barak makes the same point from the translator role. Data engineers can sit
with business teams for a day or two and find operational friction that a
ticket may hide. Analysts and data scientists can do the same[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
The strongest intake systems combine a clear formal route with embedded
discovery.

That embedded discovery can produce concrete intake evidence. Barak describes
watching repeated bidding-platform clicks and proposing a one-week MVP front end
to remove the manual work. The observation turned workflow friction into a
testable product idea instead of a vague request.
[[cite:data-translator-role-and-data-strategy@14:20=>Data Translator Role]]

## KPI Framing and Definition of Done

The team needs a Definition of Done before it chooses a solution. Mesionis
describes a short template that captures the product and production meaning. The
template names which business KPIs should move. It also defines how benefits
will be measured[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
At this stage, the team captures the "what" of the product, not the "how."

This distinction keeps [[evaluation]]
and delivery aligned. A request for random numbers isn't ready, and a forecast
or model needs the same test. The team must know how to judge whether the
output is good.

Mesionis puts KPI work in the Definition of Done before data science begins. The
team also records success criteria and fail-fast checks there[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
For product-facing work, Moorman adds that the KPI framing should match the
decision. In her A/B testing example, the reporting product should help a
product manager decide whether to roll out a feature. The report should also
show business impact instead of only statistical output[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]].

Decision-first KPI framing should include the unit the decision-maker needs.
For an experiment result, dollars or rollout confidence may matter more than a
generic dashboard field. That intake choice changes event data, joins,
transformation work, and the final interface from the beginning.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@34:42=>Last-Mile Data Delivery]]

## Feasibility, EDA, and Saying No

After stakeholders sign off on the Definition of Done, Mesionis moves the work
into inception. This is where exploratory data analysis starts. The team checks
data access, data presence, and distributions. It also reviews GDPR concerns,
constraints, and feasibility[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

The team can still stop the work if the data isn't available or the request
isn't feasible. Mesionis calls this a fail-fast scenario, where the team doesn't
continue and moves to the next prioritized idea[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

Boyan's scope-creep example shows why the feasibility gate has to include target
architecture. Adding text data to a churn use case can require new storage,
different skills, and NLP work. A request that looks like "just another dataset"
may become a different product
[[cite:data-strategy-and-dataops-for-ai-powered-products@16:21=>Scope creep in data products]].
The team asks whether the changed use case would be useful and still fits the
current delivery plan.

This is how intake creates a disciplined way to say no or defer work. The team
doesn't reject a request because it's inconvenient. It rejects, delays, or
resizes the work when the agreed KPI can't be measured. The same response fits
missing data, unresolved privacy constraints, or a product that can't reach the
defined production state. Those checks place intake next to
[[data quality and observability]],
[[data governance]], and
[[production]].

Moorman gives the adoption-side version of saying no. The team should treat
unused products as user research because users may not know they exist or how to
use them.
They may also find that it doesn't solve their real problem[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]].
That feedback can send a request back to discovery instead of pushing more
engineering into the wrong interface.

## Analytics, ML, or Smaller Prototype

Intake should decide whether a request needs analytics, machine learning, a
hybrid team, or a lightweight prototype. Mesionis says the inception phase is
where analysts and data scientists discuss the "how." They confirm whether the
work is a data science project, an analytics project, or a hybrid. Even when
the technical lead changes from data scientist to analyst, he keeps
end-to-end accountability for delivery[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

Some intake systems also need a lane for ideas that are too large or uncertain
for the normal quarterly queue. Three-month OKRs are useful for incremental data
science work tied to direct metric movement. They can also hide AI product
opportunities that need six months or a year to explore. In intake terms, that separates a
near-term [[KPIs=>KPI]] improvement from a protected [[experimentation]] track for a
longer-term [[data-product-manager-roadmap=>data product manager roadmap]] bet[[cite:ai-ml-product-design-and-experimentation@39:33=>AI Product Design]].

A request may start as user research, sketches, or a rough workflow. The
[[product-designer-to-data-product-manager=>product designer to data product manager]]
transition gives a useful handoff. Keep the discovery habit before adding SQL,
data quality, and lifecycle literacy. Then commit the team to a data product
build.
[[cite:product-designer-to-data-product-manager=>Product Designer to Data Product Manager]].

For release authority versus product direction, use
[[data-product-owner-vs-data-product-manager=>Data Product Owner vs Data Product Manager]].
It separates the consumer promise from roadmap ownership before the team turns
the request into a roadmap item
[[cite:building-data-products-product-owner-vs-product-manager=>Product Owners in Data Science]].

Those bets still need evidence. Teams can collect proof through quick
experiments and a business case. They can also form a time-limited task force
around a specific problem. The team shows results, then decides whether to build
a durable team or send people back to their home teams.

Some problems need a dedicated team with structured user-centered work and a
clear link to company vision. Task forces are an intake option, not a replacement
for roadmap ownership. Liesbeth Dingemans' task-force example keeps the work
time-boxed around evidence. The decision then returns to the product roadmap
instead of letting the experiment become a permanent shadow backlog[[cite:ai-ml-product-design-and-experimentation@49:16=>AI Product Design]].

Barak's prototype-first advice gives a useful triage option before production
engineering. Teams can automate a repetitive workflow with a quick MVP or use a
spreadsheet to prove value. They can also use rough code before transferring
the work to a production owner.

The prototype isn't the final product. It proves the use case and creates
ownership for later rebuilds or improvements[[cite:data-translator-role-and-data-strategy=>Data Translator Role]].
This keeps prioritization from treating every useful idea as a six-month build.

Barak adds a timebox rule to that choice: prove value in roughly one or two
weeks before treating the idea as a larger product commitment. Once the team has
proof, the rough prototype can be discarded or rebuilt. The team keeps a clear
use case plus business ownership.
[[cite:data-translator-role-and-data-strategy@23:54=>Data Translator Role]]

## Pilots, Experiments, and Production Handoff

Mesionis's pilot phase tests the new product against the baseline defined
earlier. The team compares the current "as-is" process with the future "to-be"
process. It often uses [[a-b-testing=>A/B testing]]
to check whether the product improves the KPI of interest. Stakeholder feedback
can trigger another pilot iteration[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].

Production can mean Tableau insights or external-tool predictions. It can also
mean a fuller [[MLOps]] path with monitoring[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
Mesionis rolls out more broadly only after the pilot beats the baseline[[cite:building-data-products-lead-data-scientist=>Data Product Intake]].
That handoff links intake to [[model monitoring]],
[[business intelligence]],
and [[analytics engineering]],
depending on the product form.

Moorman's last-mile advice adds a second rollout test. The product must enter
the actual decision meeting or workflow. She recommends low-fidelity sketches,
whiteboards, and fast feedback. Stakeholders give better input before the team
over-invests in a polished interface[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]].

For intake, that means a pilot isn't only a technical validation. It's also a
behavioral validation of whether the product changes a decision.

Exploratory data work also needs an uncertainty label. Linear projects can be
planned step by step because the next action is known. Circular projects need
discovery loops because the team doesn't know what the data will reveal until it
looks. Intake should set that expectation before stakeholders interpret learning
as delivery failure.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@58:11=>Last-Mile Data Delivery]]

## Related Pages

These adjacent pages cover the artifact, role, adoption, and measurement
practices around intake:

- [[Data Product Management]]
- [[Data Products]]
- [[Data Product Adoption]]
- [[Data Science Project Management]]
- [[Metrics]]
- [[KPIs]]
- [[Evaluation]]
- [[a-b-testing=>A/B Testing]]
