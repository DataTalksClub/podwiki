---
layout: wiki
title: "Data Product Adoption"
summary: "How podcast guests describe getting dashboards, models, analytics tools, and data products into real business decisions."
related:
  - Data Products
  - Data Product Management
  - Platform Adoption
  - Metrics
  - Communication
  - Data Teams
---

Data product adoption means getting data outputs into a team's decisions. Those
outputs also need to enter team rituals and operating habits. In
[[person:caitlinmoorman|Caitlin Moorman's]] last-mile
discussion, the adoption problem starts after a modern stack has made data
available. Teams still have to turn that availability into decisions people can
make in real workflows
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 8:48-15:56]]).

DataTalks.Club guests treat adoption as product work, not a launch
announcement. A technically correct output can still sit unused. People need
to find it and trust it. They also need to interpret it and connect it to a
decision.

Adoption sits beside [[data products]]
and [[data product management]],
and it also depends on [[platform adoption]],
[[metrics]], and
[[communication]].

## Decision Use, Not Delivery

Teams adopt a data product when data is present at the moment of decision and
changes what people do. In [[person:caitlinmoorman|Moorman's]]
last-mile episode, the problem isn't only getting data into the warehouse. It
also isn't only transforming it or creating a dashboard.

Teams still have to connect the output to real choices in meetings and
workflows. Different groups bring different incentives and comfort with data
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 8:48-15:56]]).

Guests also treat adoption as a two-sided job. Teams increase the value of using
the data product and reduce the cost of using it. Moorman names discoverability,
interpretability, trust, and clear decision context as levers. She also argues
for lower reliance on analysts for every follow-up question
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 20:02-26:36]]).

Barak reaches the same place from a translator role: business teams need shared
definitions and proactive data-quality communication. [[person:liorbarak|Lior Barak]]
also argues that users need enough visibility into how numbers are produced
before they'll use them confidently
([[podcast:data-translator-role-and-data-strategy|data translator role, 4:08-13:15]]).

## Adoption Levers Across Roles

Guests agree that adoption is behavioral, but they assign the work to different
operating levers. [[person:caitlinmoorman|Moorman]]
emphasizes product design and decision mapping. Her advice starts with the
intended decision, and the team works backward from there. The next choices
cover data sources and transformations. They also cover dashboard design and
meeting rituals
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 34:00-40:53]]).

[[person:liorbarak|Barak's]] organizational translation
starts with data people sitting beside business users and learning their
workflows. They remove small frictions and prove value with fast prototypes
before the team decides what deserves production engineering
([[podcast:data-translator-role-and-data-strategy|data translator role, 14:20-29:19]]).

[[person:tammyliang|Tammy Liang]] approaches adoption as
operating discipline for a growing [[data-teams|data team]].
Her team needed business-facing communication and an internal data wiki. They
also needed workshops and Q&A sessions. Without that work, dashboards and web
apps would sit unused
([[podcast:building-and-scaling-data-team|building and scaling a data team, 17:11-22:34 and 47:08-50:52]]).

[[person:linaweichbrodt|Lina Weichbrodt]] applies the
same sequence to machine learning. Before the team builds, stakeholders should
agree on the business case and KPIs. They should also agree on alternatives and
the bar for production
([[podcast:human-centered-mlops-and-model-monitoring|human-centered MLOps, 4:50-12:22]]).

[[person:adamsroka|Adam Sroka]] puts heavier weight on
[[metrics|KPI]] design. Metrics must be tied to
strategy and visible to the organization. Teams should review them periodically
and discard them when nobody uses them for decisions
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI design and metrics strategy, 22:41-44:59]]).

## Trust Before Usage

Several guests argue that adoption breaks when trust breaks. [[person:liorbarak|Barak]]
describes small operational signals as trust-building work rather than polish.
Those signals include telling users when a data job failed or when numbers are
safe to use. He also recommends confidence intervals, QA dashboards, and
explanations that business users can look at when they suspect a number
([[podcast:data-translator-role-and-data-strategy|data translator role, 7:46-13:15]]).

[[person:tammyliang|Liang]] gives the operational
consequence. A dashboard that appears to work but shows wrong values can create
frustration. Stakeholders may then fall back to their own judgment or
spreadsheets. Her team responded with a data accuracy and governance playbook.
They also used open error communication, dbt tests, and regular dashboard checks
([[podcast:building-and-scaling-data-team|building and scaling a data team, 35:38-41:42]]).

For ML systems, [[person:linaweichbrodt|Weichbrodt]]
adds that trust also depends on demos of bad cases, fallbacks, and service
levels. Teams also need agreement about what happens during incidents
([[podcast:human-centered-mlops-and-model-monitoring|human-centered MLOps, 18:29-27:14]]).

## Decision-First Design

[[person:caitlinmoorman|Moorman's]] strongest adoption
advice is to start from the decision rather than the dataset. For an A/B testing
reporting product, the team isn't trying to publish a dashboard with experiment
data. The product manager needs to decide whether to roll out a feature. They
also need to understand business impact and check guardrail metrics.

That decision determines what data must be joined. It also sets how results
should be shown and what language the interface should use
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 34:00-38:15]]).

Decision-first adoption work links data product adoption to [[metrics]].
[[person:adamsroka|Sroka]] argues that KPIs should be
easy to understand and aligned with strategy. They should also be few enough
that people can remember them. He recommends making KPIs visible in tools and
company-wide rituals. In reviews, teams can ask whether people made decisions
from the numbers
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI design and metrics strategy, 22:41-44:59]]).

## User Research and Prototyping

Guests repeatedly treat low adoption as a user-research signal. [[person:caitlinmoorman|Moorman]]
suggests asking whether users know the product exists and know how to use it.
Teams should also ask whether users believe it solves their real problem. She
recommends sitting in the meetings where decisions happen. Before building the
polished system, teams can sketch reports or workflows on paper
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 26:21-40:53]]).

[[person:liorbarak|Barak]] makes a similar case for
embedded observation. When data engineers, analysts, or data scientists sit
beside business users, they discover practical frictions that wouldn't appear in
a ticket queue. His examples include replacing repetitive manual clicks with a
quick MVP. He also uses prototypes or temporary spreadsheets to prove that a
workflow has a business owner. Only then does the team invest in a maintainable
implementation
([[podcast:data-translator-role-and-data-strategy|data translator role, 14:20-34:52]]).

## Enablement and Operating Rituals

Adoption is also reinforced through rituals. [[person:tammyliang|Liang's]]
team used a weekly newsletter, internal wiki, workshops, and later Q&A-style
sessions to help people find and use dashboards. The shift from lecture-style
walkthroughs to question-driven sessions mattered. It trained users to locate
answers in context instead of watching a demo passively
([[podcast:building-and-scaling-data-team|building and scaling a data team, 17:11-22:34 and 47:08-50:52]]).

[[person:linaweichbrodt|Weichbrodt]] describes
education as part of human-centered MLOps. Stakeholders may not know how to
formulate user stories, KPIs, constraints, or alternative solutions for ML work.
In those cases, the data or ML team has to help define the business case with
them. The team also has to build enough data literacy for the project to be
owned outside the technical team
([[podcast:human-centered-mlops-and-model-monitoring|human-centered MLOps, 4:50-15:07 and 54:49-56:28]]).

## Measuring Behavior Change

Adoption evidence shouldn't stop at page views or dashboard counts. [[person:caitlinmoorman|Moorman]]
recommends narrow wins with visible stakes. Help one stakeholder make a better
decision first. That stakeholder might work in sales or marketing, product or
operations. Then use that success story to build advocacy with the next team
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 41:18-49:25]]).

For less measurable work, she accepts proxies and time studies. She also accepts
surveys and practical before-and-after comparisons when they're the closest
evidence available
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|last-mile data delivery, 42:18-45:35]]).

[[person:adamsroka|Sroka]] gives data teams a more
explicit metric direction by translating model performance into money saved or
revenue. Teams can also measure risk reduction or time saved for the business.
They should track whether reusable BI tools and applications are used again.
Pipelines and services should show reuse too
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI design and metrics strategy, 51:12-1:00:02]]).

Teams that measure adoption connect [[data teams]]
to [[data-quality-and-observability|data observability]] and
[[model monitoring]]. The product
has to work, stay trusted, and leave evidence that it changed behavior.

## Adjacent Adoption Work

Data product adoption sits next to adjacent roles, platform patterns, and
measurement practices:

- [[Data Products]]
- [[Data Product Management]]
- [[Data Product Manager]]
- [[Data Product Manager vs Product Manager]]
- [[Platform Adoption]]
- [[Metrics]]
- [[Communication]]
- [[Data Teams]]
