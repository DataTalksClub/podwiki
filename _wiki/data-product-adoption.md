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
[Caitlin Moorman's]({{ '/people/caitlinmoorman/' | relative_url }}) last-mile
discussion, the adoption problem starts after a modern stack has made data
available. Teams still have to turn that availability into decisions people can
make in real workflows
([last-mile data delivery, 8:48-15:56]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

The podcast archive treats adoption as product work, not a launch announcement.
A technically correct output can still sit unused. People need to find it and
trust it. They also need to interpret it and connect it to a decision.

That connects adoption to [data products]({{ '/wiki/data-products/' | relative_url }})
and [data product management]({{ '/wiki/data-product-management/' | relative_url }}).
It also connects to [platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}),
[metrics]({{ '/wiki/metrics/' | relative_url }}), and
[communication]({{ '/wiki/communication/' | relative_url }}).

## Common Definition

Teams adopt a data product when data is present at the moment of decision and
changes what people do. In [Moorman's]({{ '/people/caitlinmoorman/' | relative_url }})
last-mile episode, the problem isn't only getting data into the warehouse. It
also isn't only transforming it or creating a dashboard.

Teams still have to connect the output to real choices in meetings and
workflows. Different groups bring different incentives and comfort with data
([last-mile data delivery, 8:48-15:56]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Guests also treat adoption as a two-sided job. Teams increase the value of using
the data product and reduce the cost of using it. Moorman names discoverability,
interpretability, trust, and clear decision context as levers. She also argues
for lower reliance on analysts for every follow-up question
([last-mile data delivery, 20:02-26:36]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Barak reaches the same place from a translator role: business teams need shared
definitions and proactive data-quality communication. [Lior Barak]({{ '/people/liorbarak/' | relative_url }})
also argues that users need enough visibility into how numbers are produced
before they'll use them confidently
([data translator role, 4:08-13:15]({{ '/podcasts/data-translator-role-and-data-strategy/' | relative_url }})).

## Guest Differences

Guests agree that adoption is behavioral, but they assign the work to different
operating levers. [Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
emphasizes product design and decision mapping. Her advice starts with the
intended decision, and the team works backward from there. The next choices
cover data sources and transformations. They also cover dashboard design and
meeting rituals
([last-mile data delivery, 34:00-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Barak's]({{ '/people/liorbarak/' | relative_url }}) organizational translation
starts with data people sitting beside business users and learning their
workflows. They remove small frictions and prove value with fast prototypes
before the team decides what deserves production engineering
([data translator role, 14:20-29:19]({{ '/podcasts/data-translator-role-and-data-strategy/' | relative_url }})).

[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) approaches adoption as
operating discipline for a growing [data team]({{ '/wiki/data-teams/' | relative_url }}).
Her team needed business-facing communication and an internal data wiki. They
also needed workshops and Q&A sessions. Without that work, dashboards and web
apps would sit unused
([building and scaling a data team, 17:11-22:34 and 47:08-50:52]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) applies the
same sequence to machine learning. Before the team builds, stakeholders should
agree on the business case and KPIs. They should also agree on alternatives and
the bar for production
([human-centered MLOps, 4:50-12:22]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) puts heavier weight on
[KPI]({{ '/wiki/metrics/' | relative_url }}) design. Metrics must be tied to
strategy and visible to the organization. Teams should review them periodically
and discard them when nobody uses them for decisions
([KPI design and metrics strategy, 22:41-44:59]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).

## Trust Before Usage

Several guests argue that adoption breaks when trust breaks. [Barak]({{ '/people/liorbarak/' | relative_url }})
describes small operational signals as trust-building work rather than polish.
Those signals include telling users when a data job failed or when numbers are
safe to use. He also recommends confidence intervals, QA dashboards, and
explanations that business users can look at when they suspect a number
([data translator role, 7:46-13:15]({{ '/podcasts/data-translator-role-and-data-strategy/' | relative_url }})).

[Liang]({{ '/people/tammyliang/' | relative_url }}) gives the operational
consequence. A dashboard that appears to work but shows wrong values can create
frustration. Stakeholders may then fall back to their own judgment or
spreadsheets. Her team responded with a data accuracy and governance playbook.
They also used open error communication, dbt tests, and regular dashboard checks
([building and scaling a data team, 35:38-41:42]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

For ML systems, [Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})
adds that trust also depends on demos of bad cases, fallbacks, and service
levels. Teams also need agreement about what happens during incidents
([human-centered MLOps, 18:29-27:14]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

## Start From Decisions

[Moorman's]({{ '/people/caitlinmoorman/' | relative_url }}) strongest adoption
advice is to start from the decision rather than the dataset. For an A/B testing
reporting product, the team isn't trying to publish a dashboard with experiment
data. The product manager needs to decide whether to roll out a feature. They
also need to understand business impact and check guardrail metrics.

That decision determines what data must be joined. It also sets how results
should be shown and what language the interface should use
([last-mile data delivery, 34:00-38:15]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

Decision-first adoption work links data product adoption to [metrics]({{ '/wiki/metrics/' | relative_url }}).
[Sroka]({{ '/people/adamsroka/' | relative_url }}) argues that KPIs should be
easy to understand and aligned with strategy. They should also be few enough
that people can remember them. He recommends making KPIs visible in tools and
company-wide rituals. In reviews, teams can ask whether people made decisions
from the numbers
([KPI design and metrics strategy, 22:41-44:59]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).

## User Research And Prototyping

Guests repeatedly treat low adoption as a user-research signal. [Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
suggests asking whether users know the product exists and know how to use it.
Teams should also ask whether users believe it solves their real problem. She
recommends sitting in the meetings where decisions happen. Before building the
polished system, teams can sketch reports or workflows on paper
([last-mile data delivery, 26:21-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Barak]({{ '/people/liorbarak/' | relative_url }}) makes a similar case for
embedded observation. When data engineers, analysts, or data scientists sit
beside business users, they discover practical frictions that wouldn't appear in
a ticket queue. His examples include replacing repetitive manual clicks with a
quick MVP. He also uses prototypes or temporary spreadsheets to prove that a
workflow has a business owner. Only then does the team invest in a maintainable
implementation
([data translator role, 14:20-34:52]({{ '/podcasts/data-translator-role-and-data-strategy/' | relative_url }})).

## Education And Rituals

Adoption is also reinforced through rituals. [Liang's]({{ '/people/tammyliang/' | relative_url }})
team used a weekly newsletter, internal wiki, workshops, and later Q&A-style
sessions to help people find and use dashboards. The shift from lecture-style
walkthroughs to question-driven sessions mattered. It trained users to locate
answers in context instead of watching a demo passively
([building and scaling a data team, 17:11-22:34 and 47:08-50:52]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) describes
education as part of human-centered MLOps. Stakeholders may not know how to
formulate user stories, KPIs, constraints, or alternative solutions for ML work.
In those cases, the data or ML team has to help define the business case with
them. The team also has to build enough data literacy for the project to be
owned outside the technical team
([human-centered MLOps, 4:50-15:07 and 54:49-56:28]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

## Measuring Adoption

Adoption evidence shouldn't stop at page views or dashboard counts. [Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
recommends narrow wins with visible stakes. Help one stakeholder make a better
decision first. That stakeholder might work in sales or marketing, product or
operations. Then use that success story to build advocacy with the next team
([last-mile data delivery, 41:18-49:25]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

For less measurable work, she accepts proxies and time studies. She also accepts
surveys and practical before-and-after comparisons when they're the closest
evidence available
([last-mile data delivery, 42:18-45:35]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

[Sroka]({{ '/people/adamsroka/' | relative_url }}) gives data teams a more
explicit metric direction by translating model performance into money saved or
revenue. Teams can also measure risk reduction or time saved for the business.
They should track whether reusable BI tools and applications are used again.
Pipelines and services should show reuse too
([KPI design and metrics strategy, 51:12-1:00:02]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})).

Teams that measure adoption connect [data teams]({{ '/wiki/data-teams/' | relative_url }})
to [data observability]({{ '/wiki/data-observability/' | relative_url }}) and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}). The product
has to work, stay trusted, and leave evidence that it changed behavior.

## Related Pages

These pages cover adjacent adoption work:

- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Communication]({{ '/wiki/communication/' | relative_url }})
- [Data Teams]({{ '/wiki/data-teams/' | relative_url }})
