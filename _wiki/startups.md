---
layout: wiki
title: "Startups"
summary: "Recurring startup lessons across DataTalks.Club podcast discussions: problem discovery, validation, MLOps scope, open-source distribution, consulting paths, funding, and startup career tradeoffs."
related:
  - Founder
  - Entrepreneurship
  - Open Source
  - Open Source and Developer Relations
  - Freelance
  - Data Product Management
  - MLOps
  - MLOps Roadmap
---

DataTalks.Club guests discuss tech startups through concrete company examples.
In these episodes, tech startups usually mean data and AI companies. Guests
focus on machine learning products, [[MLOps]]
tools, and [[open-source|open-source]] developer
products.

They also cover consulting firms, indie products, and early jobs in
four-person teams. Across these discussions, startup teams learn the real
workflow and choose a narrow product boundary. They also have to reach users
early and avoid technical scope that outruns the business.

This page maps the end-to-end founder playbook and the repeated lessons across
these episodes. It links startup discussions to
[[founder|founders]],
[[entrepreneurship]], and
[[open source]]. It also keeps
[[freelance]],
[[data product management]],
and [[MLOps]] in view.

## Problem Discovery and Product Boundaries

Across these episodes, a data or AI startup is a learning system wrapped in a
business. [[person:elenasamuylova|Elena Samuylova]]
warns technical founders not to begin with "I want to build a machine learning
startup." Around 7:23 in
[[podcast:building-mlops-startup|How to Build a Successful ML Startup]],
she starts from a painful workflow and asks whether machine learning is needed
at all. Her grocery example shows why this matters: the obvious forecasting
idea may fail if the store can't collect basic inventory data.

[[person:carminepaolino|Carmine Paolino]] makes the
same lesson concrete in retail. In
[[podcast:launch-and-build-retail-startup|Build a Grocery Retail OS to Cut Supermarket Food Waste]],
around 5:46-10:17, FreshFlow learned by shadowing fresh-product managers. The
team watched how shelf checks and stockroom counts affected ordering. It also
had to account for weather, events, and empty-shelf risk. The startup moved
from a narrower computer-vision idea toward a retail operating system because
the workflow, not the first technical idea, set the product boundary.

[[person:aleksanderkruszelnicki|Aleksander Kruszelnicki]]
shows the consulting version. Around 4:16-18:01 in
[[podcast:data-consulting-business-pricing-and-client-acquisition|Build a Data Consulting Business]],
his team moved away from a "data stack as a service" idea. Interviews showed
that clients needed help translating business questions into usable data
models. Across these episodes, startups succeed when the team lets customer
evidence change the product.

Startup discussions keep returning to product discovery because data products
fail when the team automates the wrong decision. Samuylova describes speaking
with roughly 50 people before building and more than 100 during early
development. Around 42:15-45:45 in
[[podcast:building-mlops-startup|How to Build a Successful ML Startup]],
those conversations uncovered repeated pain around broken models, abandoned
monitoring, and production systems nobody watched.

Kruszelnicki gives a reusable interview routine for early ideas. Around
9:08-15:55 in
[[podcast:data-consulting-business-pricing-and-client-acquisition|Build a Data Consulting Business]],
he asks about the customer's current workflow. He also asks about recent
incidents, consequences, and problem frequency. Those questions move the conversation
away from "would you buy this?" and toward observable evidence.

Startup discovery therefore overlaps with
[[data product management]].
The team has to understand the user, the decision, and the cost of the current
workflow before it builds a roadmap.

Brudaru's DLT workshop shows discovery for a developer tool. Around
36:00-42:01 in
[[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]],
participants built an incremental pipeline with checkpoints, live support, and
a shared development environment. The exercise taught users, but it also showed
the startup where Python users understood the abstraction and where the product
still blocked them.

## Startup Routes

The podcast doesn't present venture-backed growth as the only startup path.
Samuylova's Evidently story is about an MLOps infrastructure company. Evidently
uses open source and cloud paths for adoption, plus enterprise paths for
monetization
([[podcast:building-mlops-startup|How to Build a Successful ML Startup]],
around 48:11-56:17).

Paolino's FreshFlow story is a vertical retail AI company. It has pilots,
store operations, and domain-specific sales cycles
([[podcast:launch-and-build-retail-startup|Build a Grocery Retail OS to Cut Supermarket Food Waste]],
around 24:47-36:40).

[[person:sonalgoyal|Sonal Goyal]] and
[[person:adrianbrudaru|Adrian Brudaru]] both start from
repeated data engineering pain, but they package it differently. Goyal turns
identity resolution into an open-source ML product. She uses AGPL licensing to
protect the business from simple SaaS rehosting
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source ML-Powered Identity Resolution Tool]],
around 24:14-31:10).

Brudaru frames DLT as a developer library. The team uses workshops and
documentation to test the tool, then examples and ecosystem partnerships to
spread it
([[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]],
around 36:00-53:24).

Other guests choose smaller or service-led paths. Kruszelnicki treats
consulting as the right business after product ideas failed. Customers were
ready to pay for hands-on translation and delivery
([[podcast:data-consulting-business-pricing-and-client-acquisition|Build a Data Consulting Business]],
around 22:42-30:17).

[[person:paulineclavelloux|Pauline Clavelloux]]
describes indie hacking as bootstrapping side products while keeping a day job.
She covers landing pages, legal setup, payments, and pricing. She also covers
costs and niche marketing
([[podcast:data-scientist-and-indie-hacker-bootstrapping-side-projects|Indie Hacking and Bootstrapping Side Projects]],
around 7:23-33:11).

## Product Strategy in High-Risk Domains

Some startup discussions add product strategy where a wrong output can harm a
user. [[person:liesbethdingemans|Liesbeth Dingemans]]
gives the general AI product design frame in
[[podcast:ai-ml-product-design-and-experimentation|AI Product Design]].
Around 6:43-18:21, she argues that product teams should design interfaces that
collect useful signals, frame the problem before the solution, and test parallel
options before scaling. Around 37:15-54:11, she connects roadmaps to
prioritization, evidence, and investment cases.

[[person:mariabruckert|Maria Bruckert]] shows the
health-tech version in
[[podcast:building-ai-digital-health-startups|Building Digital Health Startups]].
Around 2:05-6:11 and 12:20-24:08, she describes industry immersion before
product structure. The team uses cold outreach and accelerators, and clinical
meetings help them learn pharmacy constraints, hospital constraints, and legacy
workflows. Around 24:08-35:57, SQIN has to route AI diagnosis into consultation
and treatment, and it also covers pharmacies and prescriptions. The app needs
sensitive messaging, inclusive design, and fallbacks when the model shouldn't
decide alone. In high-risk domains, product strategy includes what the system
should refuse or defer, and what it should hand to a human.

## Technical Scope Stays Stage-Aware

Guests expect startup engineering discipline and warn against building platforms
too early.

[[person:nemanjaradojkovic|Nemanja Radojkovic]] argues
around 11:54-21:35 in
[[podcast:lean-mlops-for-startups|Lean MLOps for Startups]]
that small teams should use SaaS and managed cloud services when that saves
team capacity. He still warns about vendor lock-in and migration
friction when managed ML platforms hide too much of the system.

Paolino gives the CTO version from FreshFlow. Around 53:09 in
[[podcast:launch-and-build-retail-startup|Build a Grocery Retail OS to Cut Supermarket Food Waste]],
he describes moving away from Kubeflow complexity toward managed cloud choices.

Paolino isn't arguing against MLOps. He's arguing for enough deployment,
observability, and data reliability to learn safely.

Platform work still has to match the startup stage. Read this with the
[[MLOps roadmap]] and
[[MLOps]] as operating context.

[[person:antonisstellas|Antonis Stellas]] shows this
from an employee and freelancer perspective. Around 17:39-25:12 in
[[podcast:from-startup-engineering-to-freelance-data-science|Freelance Data Scientist Playbook]],
he connects lean startup habits with model monitoring. He also describes an
MLOps course project with MLflow, Prefect, and Grafana. For small teams,
production skill often grows through monitoring and deployment work before a
formal platform team exists.

## Distribution Depends on Trust

For open-source and developer-tool startups, distribution is part of product
strategy. Guests don't treat it as a late marketing task.
[[podcast:building-mlops-startup|How to Build a Successful ML Startup]]
covers the Evidently version around 48:11-56:17. Samuylova explains that open
source helped Evidently reach engineers and data scientists who needed to try
monitoring pieces before buying a managed product. It also fit teams with
sensitive data or on-premise constraints.

Goyal makes the same argument for Zingg. Around 24:14-29:22 in
[[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source ML-Powered Identity Resolution Tool]],
open source helps smaller teams try identity resolution. It also helps the
company discover use cases across customer, supplier, patient, and product
records.
Startup distribution belongs with
[[open source]] and
[[open-source-and-developer-relations|open-source developer relations]].
Repository adoption, documentation, examples, and community feedback become
part of the sales path.

[[person:belawiertz|Bela Wiertz]] adds the investor
view. Around 13:42-16:40 and 32:31-39:01 in
[[podcast:investing-in-open-source-developer-tools|Early-Stage Investing in Open Source Developer Tools]],
he describes open source as community-driven distribution and bottom-up
adoption. He still looks at the team and the market need. He also checks
commercialization, user interviews, and real engagement.

GitHub stars can help discovery, but they don't replace proof that developers
use the tool. They also don't prove that a business can capture value.

## Services, Side Projects, and Startup Careers

Several guests start outside a classic venture-backed company. Brudaru moved
from freelance data engineering work into a product startup after seeing
recurring warehouse and JSON ingestion problems. He also saw stakeholder
alignment problems
([[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]],
around 8:16-19:38). His early funding mix included savings, consulting revenue,
and design-partner work
([[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]],
around 31:08-34:20). That makes [[freelance]]
work a source of startup evidence, not just a separate career path.

Clavelloux shows a smaller bootstrapped route. Around 15:09-21:46 in
[[podcast:data-scientist-and-indie-hacker-bootstrapping-side-projects|Indie Hacking and Bootstrapping Side Projects]],
she covers company setup and landing pages. She also covers legal and payment
work, Python and Flask architecture, marketing channels, and costs for side
products such as crypto alerts.

Around 23:33-30:37, she discusses UnrealMe. She compares API fine-tuning with
self-hosted GPUs and explains pricing constraints for generative AI products.
These are startup decisions at a smaller scale. The builder still has to decide
what to build, how to ship, how much it costs to run, and how users find it.

Stellas covers startup work as a career environment. Around 8:19-15:49 in
[[podcast:from-startup-engineering-to-freelance-data-science|Freelance Data Scientist Playbook]],
he chose a startup over a corporation because it matched his topic and offered
variety. In a four-person team, he had to communicate, learn the business, and
organize his own work. Around 28:43-35:31, open-source contribution and
freelance projects became ways to broaden his data work beyond the startup.

For data professionals, a startup can be an employer or client. It can also be
a product lab or future company.

Use [[founder]] for the operating role
inside a startup, covering problem choice and validation plus hiring, funding,
and distribution. Use
[[entrepreneurship]] for
independent-work paths across products, consulting, and solo work.

Use [[open source]] and
[[open-source-and-developer-relations|open-source developer relations]]
for repository-led adoption, licensing, community, and developer trust. Use
[[freelance]] for service businesses
that can reveal product ideas or fund early startup work.
