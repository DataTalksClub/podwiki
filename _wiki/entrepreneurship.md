---
layout: wiki
title: "Entrepreneurship"
summary: "Podcast-backed notes on entrepreneurship in data, AI, open-source tooling, and consulting."
related:
  - Career Transitions in Data
  - Machine Learning
  - MLOps
  - Data Product Management
  - Data Strategy
  - Open Source
  - Freelance
---

Entrepreneurship in the DataTalks.Club podcast archive often starts with a data
or AI capability. The strongest founder stories don't treat that capability as
the product. Guests first find painful data work, learn the customer's operating
context, prove that someone will pay or adopt, and then choose the right
business model.

Data founders therefore need a different playbook from generic startup advice.
[Elena Samuylova]({{ '/people/elenasamuylova/' | relative_url }}) makes the
first rule explicit. Technical founders shouldn't start by deciding to build a
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) startup.

Around 7:34 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
she says a founder who starts from the model may miss the real problem. Her
example is missing inventory data in a grocery workflow. Across the
entrepreneurship episodes, founders form the business around the customer
problem rather than the founder's preferred tool.

## Problem Discovery in Data and AI Markets

Data founders in these episodes look for repeated operational pain. Samuylova
suggests looking inside businesses for inefficient work. Founders then need to
check whether the pain is large enough and whether people want to pay to solve
it. She also recommends teaming with domain experts when industry context
matters. Her examples include insurance, finance, and healthcare
([How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
around 8:51-10:40).

[Carmine Paolino]({{ '/people/carminepaolino/' | relative_url }}) gives a
concrete retail version in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}).
FreshFlow didn't stay with the first computer-vision idea. The team watched
fresh-product managers at 6 a.m. and saw them combine shelf checks with
stockroom counts. They also accounted for local conditions such as weather and
events across hundreds of products.

Around 5:46-10:17, Paolino explains how that fieldwork became an ordering
system for supermarkets. In
[data product management]({{ '/wiki/data-product-management/' | relative_url }}),
founders have to learn the store work before deciding what the software should
automate.

[Maria Bruckert]({{ '/people/mariabruckert/' | relative_url }}) describes the
healthcare version in
[Building Digital Health Startups]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }}).
SQIN's team had to understand healthcare from several sides before turning AI
skin diagnosis into a product. Bruckert names clinical work, pharmacy and
hospital constraints, and regulation. She also names rural access and legacy
workflows.

Around 12:55-24:08, she explains how the team used cold outreach and clinical
meetings. Accelerators and an AR lipstick MVP also helped them learn what could
become a profitable digital clinic flow. For sensitive domains,
[data strategy]({{ '/wiki/data-strategy/' | relative_url }}) includes trust and
workflow design. It also includes communication, not only dataset access.

## Validation Before Building

Several guests use early conversations instead of premature code.
Samuylova says that before building Evidently, the team talked to about 50
people and then more than 100 during early development. Around 42:15-45:45 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
she describes repeated complaints about model monitoring. People talked about
broken models, data scientists leaving projects, and production systems nobody
watched.
Those interviews shaped Evidently's direction before the team committed to the
product.

[Aleksander Kruszelnicki]({{ '/people/aleksanderkruszelnicki/' | relative_url }})
uses the same discipline for consulting and product ideas. In
[Build a Data Consulting Business]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }}),
he explains around 9:08-13:07 that founders should ask about the customer's
current work and recent incidents. They should also ask about consequences and
frequency. Those questions work better than asking whether someone would buy a
hypothetical product.

His team found a first customer through those interviews, then realized that
the paid value wasn't the data-stack shell they wanted to productize. The
customer needed someone to map the business into SQL models and make the data
useful.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) shows another
validation path in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}).
After years of freelance [data engineering]({{ '/articles/data-engineering-freelance/' | relative_url }})
work, he saw the same problem repeat. Teams could set up a warehouse, but they
struggled to align stakeholders on basic entities and metrics. Around
36:00-40:19, his company used a workshop to test whether Python users could
build incremental pipelines with the new interface. Teaching became product
research because completion checkpoints and live support showed where users
could proceed and where the tool still got in the way.

## Consulting, Products, and Open Source

Guests describe consulting, freelancing, and product startups as different ways
to commercialize data expertise. Kruszelnicki moved from failed product ideas
into a boutique analytics consultancy. Clients paid for hands-on implementation
and accountability.

Around 22:42-29:18 in
[Build a Data Consulting Business]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }}),
he argues that much of the value sits in understanding the business question.
Consultants also create value by building the modeling layer and getting the
client unstuck. Around 45:19-52:15, he gives value-based pricing advice.
Consultants should benchmark the market and start from the value delivered.
They shouldn't price only from the time spent.

Brudaru frames freelancing as highly autonomous but limited when the founder
wants to build a product. Around 8:16-13:42 in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}),
he says subcontracting pushed him toward agency management. Product work let
him target a recurring pain he had seen across data warehouse projects.
Around 31:08-33:19, he says the company funded early work with savings,
consulting revenue, and design-partner projects. For
[freelance]({{ '/wiki/freelance/' | relative_url }}) data workers, services can
reveal repeated pain, fund the first version, and test a product on real data.

Open source gives founders another route. [Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }})
turned years of identity-resolution consulting into Zingg, an open-source
ML-powered tool for matching entities across datasets. The entities can be
customers, suppliers, or products. They can also be other business records.

In
[Building an Open-Source Data Product for Identity Resolution]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she explains around 2:58-5:47 that the modern data stack made the problem more
visible. Companies finally had data in one place. Around 24:14-29:22, she
frames open source as both a community choice and a distribution strategy.
Zingg helped smaller teams access identity resolution and surfaced more use
cases. Goyal used AGPL licensing to protect the business from simple SaaS
rehosting.

Samuylova's Evidently story makes a similar open-source business argument for
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}). Around
48:11-56:17 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
she discusses open core, cloud, and on-premise deployments. She also discusses
bottom-up adoption by engineers and data-safety concerns. For developer tools,
founders in the archive use open source to earn trust and reach practitioners,
not only to pick a license.

## Technical Scope and Operating Discipline

Data and AI founders still need engineering discipline, but the podcast guests
argue for stage-appropriate systems. In
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}),
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
recommends SaaS and cloud services for small teams around 11:54-17:38. A
company with four to ten people shouldn't spend scarce hiring capacity on
server maintenance. He still warns about cloud complexity and migration
friction. Vendor lock-in matters when teams adopt managed ML platforms before
they know which parts must remain portable.

Paolino's FreshFlow experience makes the same point from a CTO seat. Around
53:09 in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}),
he describes moving away from Kubeflow complexity toward managed cloud choices.
Radojkovic makes the general rule explicit around 18:29-21:35. Early teams
often need PostgreSQL, Python, simple APIs, and CI/CD. They may also need
orchestration and observability before they need a full platform.

Founders can read
[machine learning for startups]({{ '/articles/machine-learning-for-startups/' | relative_url }})
through that lens. They should build enough infrastructure to learn from
customers and protect reliability. They shouldn't build so much that
infrastructure becomes the company.

The domain changes how much rigor founders need early. Bruckert's healthcare
discussion requires more caution than a normal consumer app because AI messages
can affect health anxiety, clinical trust, and inclusion. Around 24:08-35:57 in
[Building Digital Health Startups]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }}),
she describes working with doctors, designing a full diagnosis-to-treatment
flow, and handling sensitive messaging. She also describes making the product
useful across skin tones, genders, and access constraints. In data/AI
entrepreneurship, the
minimum viable product still has to respect the risk level of the domain.

## Founder Roles, Teams, and Fundraising

Technical founders in the archive often move beyond technical work quickly.
Samuylova says a startup role changes constantly and rewards people who can
look at what they're doing, for whom, and why it's needed. Around 31:50-36:24
in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
she normalizes failure and long early-stage hours.

She also discusses weekend MVPs and bootstrapping. Grants, accelerators, and
angel funding come up as possible paths too. She isn't saying that every
founder must raise venture capital. She's saying founders need to understand
the funding path that matches the company they're building.

Paolino's episode adds co-founder and role design. Entrepreneur First helped
him find a team, learn sales and marketing, and test ideas outside his
technical bubble. Once FreshFlow had a direction, he and his co-founder split
work.

Around 42:24-43:08 in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}),
Paolino handled pipelines, dashboards, and machine learning engineering. His
co-founder handled sales, business development, investors, and the pitch deck.
Data/AI companies often need both domain sales and technical credibility at the
same time.

Goyal's retrospective shows what happens when one founder owns too much. In
[Building an Open-Source Data Product for Identity Resolution]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
around 21:51-24:14, she describes stopping consulting. She then spent about a
year and a half building Zingg before the public release.

Around 54:11, she says she would look for a co-founder from the day she decided
to start. One person can't easily cover funding conversations, community work,
product direction, and implementation. For data founders, team design is part
of the product strategy. The same people must cover research and engineering.
They must also cover sales, community, and customer trust.
