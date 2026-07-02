---
layout: wiki
title: "Data Product Intake and Prioritization"
summary: "How DataTalks.Club guests turn stakeholder requests into scoped data products through intake, KPI framing, feasibility checks, pilots, and production handoff."
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

Data product intake and prioritization is the operating layer between an
unstructured stakeholder request and a committed [[data-products|data product]].
It decides what problem enters the funnel and which
[[KPIs]] or
[[metrics]] define success. It also sets
the feasibility checks before delivery and gives the team a way to say no,
defer, or run a smaller experiment.

Use this page with [[Data Product Management]],
[[Data Products]], and
[[Data Product Adoption]].
Those pages cover the product role, the maintained artifact, and adoption in
real decisions. Intake narrows the scope to request framing and Definition of
Done documents. It also covers exploratory checks, pilots, and production
handoffs.

[[person:ioannismesionis|Ioannis Mesionis]] gives the
clearest operating model in
[[podcast:building-data-products-lead-data-scientist|Building Data Products at Scale]].
His easyJet example starts with embedded stakeholder observation. It then moves
through a "single front door" and Definition of Done. The same workflow
continues through inception and EDA. R&D, pilot testing, and production rollout
come next
([[podcast:building-data-products-lead-data-scientist|7:23-27:32]]).

## Intake as Decision System

Across the podcast discussions, intake isn't a ticket queue where every
dashboard, model, or analysis request automatically becomes delivery work. It
is a decision system. Mesionis describes weekly collaboration with Digital,
Customer, and Marketing stakeholders. He uses those meetings to understand pain
points and business strategy. He also learns the PPC, SEO, and metric context
before the work enters the formal product funnel
([[podcast:building-data-products-lead-data-scientist|7:23-14:00]]).

The formal intake step gives business problems and ideas a single route into
the funnel. The kickoff includes business analysts, finance, lead data science,
and data engineering. The group assesses whether the request has a real
opportunity. It compares the request with other
submitted ideas and chooses the most important work first
([[podcast:building-data-products-lead-data-scientist|15:23-17:37]]).
That makes intake a prioritization mechanism for
[[data science project management]],
not only a form.

[[person:caitlinmoorman|Caitlin Moorman]] adds the
adoption boundary in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].
For her, the request should be framed around the decision the product will
enable. A data team may build a dashboard or A/B testing tool. Success is
whether a product manager can use it at the moment of decision. The same rule
applies to a marketing team or operator
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|34:00-40:53]]).

Good intake therefore asks who will act, what they'll compare, and where the
data product enters their workflow.

## Different Intake Risks

The guests agree that intake needs business context, but they focus on
different failure modes. Mesionis focuses on lifecycle control. His intake
model protects the team from moving into technical work before the problem,
benefits, baseline, and production meaning are agreed
([[podcast:building-data-products-lead-data-scientist|15:23-20:03]]).

Moorman focuses on whether the request will produce adoption. She warns that
technical availability is only table stakes, because users still need to find,
understand, and trust the product. They also need to use it in their decision
process.

If the cost of using the data product is higher than its perceived benefit, it
won't be adopted
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|20:02-28:10]]).
That shifts prioritization toward high-value decisions and low-friction
interfaces.

[[person:liorbarak|Lior Barak]] focuses on translation
and proof. In
[[podcast:data-translator-role-and-data-strategy|Data Strategist Guide]],
he argues that data people should sit with business users and see their
workflow. They can identify small automations or prototypes before committing
to heavier development. A quick MVP can prove that a problem matters and create the
business ownership needed for productionization
([[podcast:data-translator-role-and-data-strategy|14:20-30:30]]).
His version gives teams more room to validate a request with temporary work
before it becomes a formal product commitment.

## Single-Front-Door Intake

A single-front-door intake route gives data teams one path for new data
product ideas. In Mesionis's operating model, the first task is clarity on the
problem statement. The request enters a funnel, then a cross-functional group
reviews the idea and compares it with other candidate work
([[podcast:building-data-products-lead-data-scientist|15:23-17:37]]).
The front door reduces random priority changes because stakeholders see how
finance, business analysis, data science, and engineering evaluate the same
request.

The front door also works only if the team has regular contact with the
business before the request is written. Mesionis joins weekly stakeholder
meetings and learns departmental goals. He also observes how people make
decisions
([[podcast:building-data-products-lead-data-scientist|8:32-10:33]]).

Barak makes the same point from the translator role. Data engineers can sit
with business teams for a day or two and find operational friction that a
ticket may hide. Analysts and data scientists can do the same
([[podcast:data-translator-role-and-data-strategy|14:20-18:50]]).
The strongest intake systems combine a clear formal route with embedded
discovery.

## KPI Framing and Definition of Done

Prioritization depends on a Definition of Done before the team chooses a
solution. Mesionis describes a short template that captures the product and
what production means. It also names which business KPIs should move, how
benefits will be measured, and which calculation method will prove those
benefits
([[podcast:building-data-products-lead-data-scientist|17:37-19:22]]).
At this stage, the team captures the "what" of the product, not the "how."

This distinction keeps [[evaluation]]
and delivery aligned. A request for random numbers isn't ready, and a forecast
or model needs the same test. The team must know how to judge whether the
output is good.

Mesionis explicitly places KPI work in the Definition of Done before data
science work begins. He also puts success criteria and fail-fast checks in the
same document
([[podcast:building-data-products-lead-data-scientist|17:37-20:03]]).
For product-facing work, Moorman adds that the KPI framing should match the
decision. In her A/B testing example, the reporting product should help a
product manager decide whether to roll out a feature. It should also show
business impact instead of only statistical output
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|28:42-38:15]]).

## Feasibility, EDA, and Saying No

After stakeholders sign off on the Definition of Done, Mesionis moves the work
into inception. This is where exploratory data analysis starts. The team checks
data access, data presence, and distributions. It also reviews GDPR concerns,
constraints, and feasibility
([[podcast:building-data-products-lead-data-scientist|19:22-21:12]]).

The team can still stop the work if the data isn't available or the request
isn't feasible. Mesionis calls this a fail-fast scenario, where the team doesn't
continue and moves to the next prioritized idea
([[podcast:building-data-products-lead-data-scientist|19:22-20:03]]).

This is how intake creates a disciplined way to say no or defer work. The team
doesn't reject a request because it's inconvenient. It rejects, delays, or
resizes the work when the agreed KPI can't be measured. The same response fits
missing data, unresolved privacy constraints, or a product that can't reach the
defined production state. Those checks place intake next to
[[data quality and observability]],
[[data governance]], and
[[production]].

Moorman gives the adoption-side version of saying no. If a built product isn't
used, the team should treat that as user research. Users may not know it
exists, may not know how to use it, or may find that it doesn't solve their
real problem
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|26:21-28:10]]).
That feedback can send a request back to discovery instead of pushing more
engineering into the wrong interface.

## Analytics, ML, or Smaller Prototype

Intake should decide whether a request needs analytics, machine learning, a
hybrid team, or a lightweight prototype. Mesionis says the inception phase is
where analysts and data scientists discuss the "how." They confirm whether the
work is a data science project, an analytics project, or a hybrid. Even when
the technical lead changes from data scientist to analyst, he keeps
end-to-end accountability for delivery
([[podcast:building-data-products-lead-data-scientist|20:54-22:48]]).

Barak's prototype-first advice gives a useful triage option before production
engineering. Teams can automate a repetitive workflow with a quick MVP or use a
spreadsheet to prove value. They can also use rough code before transferring
the work to a production owner.

The prototype isn't the final product. It proves the use
case and creates the ownership needed to rebuild or improve it
([[podcast:data-translator-role-and-data-strategy|23:54-32:20]]).
This keeps prioritization from treating every useful idea as a six-month build.

## Pilots, Experiments, and Production Handoff

Mesionis's pilot phase tests the new product against the baseline defined
earlier. The team compares the current "as-is" process with the future "to-be"
process. It often uses [[a-b-testing|A/B testing]]
to check whether the product improves the KPI of interest. Stakeholder
feedback during the pilot can trigger another iteration before rollout
([[podcast:building-data-products-lead-data-scientist|25:17-27:25]]).

Production is a spectrum in this model. It may mean insights in Tableau,
predictions in an external tool, or a fuller [[MLOps]]
path with monitoring. Mesionis rolls out more broadly only after the pilot
shows benefits and beats the baseline
([[podcast:building-data-products-lead-data-scientist|27:25-28:18]]).
That handoff links intake to [[model monitoring]],
[[business intelligence]],
and [[analytics engineering]],
depending on the product form.

Moorman's last-mile advice adds a second rollout test: the product must enter
the actual decision meeting or workflow. She recommends low-fidelity sketches,
whiteboards, and fast feedback because stakeholders give better input before a
team has over-invested in a polished interface
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|38:15-40:53]]).
For intake, that means a pilot isn't only a technical validation. It's also a
behavioral validation of whether the product changes a decision.

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
- [[a-b-testing|A/B Testing]]
