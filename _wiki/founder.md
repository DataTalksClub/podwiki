---
layout: wiki
title: "Founder"
summary: "How DataTalks.Club podcast guests describe the founder role in data, AI, MLOps, open-source, consulting, and digital health startups."
related:
  - Entrepreneurship
  - Startup
  - Startups
  - Data Product Management
  - Machine Learning
  - MLOps
  - Open Source
  - Team Building
---

A founder in the DataTalks.Club archive keeps the company moving through
uncertainty. Founders choose the problem and find users. They define the product,
hire the missing skills, and prove that the business can reach customers and
make money. That makes the role narrower than
[entrepreneurship]({{ '/wiki/entrepreneurship/' | relative_url }}), which covers
the broader path of starting and running independent work. Here, founder means
the operating role inside data, AI, and open-source startups.

Across these episodes, founders don't start with the technology they like.
[Elena Samuylova]({{ '/people/elenasamuylova/' | relative_url }}) warns against
framing a company as a "machine learning startup" before the problem is known.
In
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }})
around 7:23, she argues that a founder should look for a painful workflow first.
Only after that should the founder decide whether
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) is the right
tool. That distinction also shapes
[Machine Learning for Startups]({{ '/guides/machine-learning-for-startups/' | relative_url }}):
ML helps only when it improves a real customer decision or workflow.

## Problem Selection

Founder work starts with choosing a problem that can become a company. Samuylova
describes this as a problem-first search, not a search for places to use a
favorite model. Her grocery-store example is deliberately non-glamorous: a team
may think the problem is forecasting. After customer conversations, they may
learn that the store can't collect basic inventory data yet
([7:23-11:12]({{ '/podcasts/building-mlops-startup/' | relative_url }})).

For a founder, that means the first decision isn't model architecture. It's
whether the customer has a routine pain, whether the pain is large enough, and
whether the customer wants to pay for a fix.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) gives the same lesson
from identity resolution. Zingg came from repeated consulting work where
companies struggled with customer, supplier, patient, and product records. In
[Building an Open-Source ML-Powered Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she traces the product back to use cases she saw across domains. Around 2:58,
11:09, and 18:13, she also describes why a scalable identity-resolution tool had
to work inside the modern data stack. When several clients expose the same gap,
the founder can test whether the repeated consulting problem deserves a product.

[Maria Bruckert]({{ '/people/mariabruckert/' | relative_url }}) adds the
regulated-market version. SQIN began with healthcare as a domain that needed
technology help. The founders spent roughly the first one and a half to two
years learning the industry before settling on the product structure. In
[Building Digital Health Startups]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }}),
she describes talking with pharmacists and doctors. The founders also talked
with hospitals, patients, pharma companies, and regulatory players before
turning AI diagnosis into a digital clinic flow
([2:05 and 24:08]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }})).

In healthcare, the founder has to choose a problem that's useful and ethical.
The problem also has to be data-feasible and safe enough to put in front of
patients.

## Customer Validation

The founder also owns the proof that the problem is real. Samuylova says
founders should talk to potential users before coding. That matters especially
for technical founders who are tempted to build a polished system too early. In
Evidently's case, the team talked to roughly 50 people before starting. They
talked to more than 100 during early development.

Teams kept describing broken models. They
also described abandoned monitoring and production failures that no one noticed,
so Evidently validated model monitoring
([40:13-45:45]({{ '/podcasts/building-mlops-startup/' | relative_url }})).

That makes [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
not just a technical category, but a customer-discovery result.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) shows a
developer-tools version of validation. In
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}),
the DLT team tested its interface through a three-day workshop where about 60
Python users built an incremental pipeline. The team added checkpoints, live
support, and a shared Codespaces environment so they could see where people got
stuck
([36:00-42:01]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }})).
Teaching can double as product research when the exercise exposes whether users
understand the abstraction.

[Aleksander Kruszelnicki]({{ '/people/aleksanderkruszelnicki/' | relative_url }})
grounds validation in consulting and positioning. In
[Build a Data Consulting Business]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }}),
he explains why his team moved away from "data stack as a service" after market
validation. The team moved toward hands-on analytics consulting because clients
needed help bridging business questions to data models more than they needed
infrastructure alone
([4:16-26:03]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }})).
For founders, validation can say no to the product they wanted and yes to the
business customers are ready to buy.

## Product Strategy

Founders decide what the product is and what it isn't. Brudaru frames DLT as a
developer-focused library rather than a platform. Around 40:50 and 53:24, he
connects that choice to the product's principles. DLT should fit into a data
engineer's stack. It should integrate with tools such as DuckDB and avoid trying
to take over the whole workflow
([From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }})).

That's a product-management decision as much as an engineering decision, and it
sits close to [data product management]({{ '/wiki/data-product-management/' | relative_url }}).

Samuylova's Evidently story makes the same point for infrastructure startups.
For [MLOps]({{ '/wiki/mlops/' | relative_url }}), open source made sense because
model monitoring users needed to try small pieces quickly. Around 48:11, she
describes open core and cloud as monetization paths. Around 49:29, she explains
that open source shortens feedback loops. Users can try small features before a
closed product is fully deployed
([How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }})).

The founder has to match product packaging to the buyer's trust threshold, data
sensitivity, and adoption path.

Bruckert's SQIN example shows why product strategy includes ethics and user
experience. The app couldn't simply tell a user that they might have a serious
skin condition. The founders had to design a flow from diagnosis to
consultation, treatment, pharmacies, and prescriptions. They also had to keep
communication sensitive and inclusive.

The founders focused the algorithm on a
specific starting market and added fallbacks for cases the model couldn't
handle
([24:08-28:01]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }})).
For AI founders, the product boundary includes what the system should refuse,
defer, or route to another path.

## Distribution

The archive treats distribution as founder work, not a late marketing add-on.
Sonal Goyal says open source was both a personal choice and a business decision.
Zingg could reach more companies than a closed-source product that required
direct sales. It also helped the team discover more use cases than door-to-door
outreach could
([24:14-25:25]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

At the end of the episode, she makes distribution explicit. Even with open
source, founders must know where early users are. They need to know which
communities or channels they can reach and what content will help those users
try the product
([57:09]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

Brudaru describes the day-to-day version of that work as go-to-market for a
library. His job became finding personas, understanding where data engineers
hang out, identifying tool communities with matching use cases, and building
ecosystem partnerships. The DocDB example worked because DLT and DocDB could
run together in notebooks and demos, creating a useful path for both products
([47:56-53:24]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }})).
This is adjacent to
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) and
[open-source and developer relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }}),
but the founder still owns the strategic choice of audience, channel, and
positioning.

For service businesses, Kruszelnicki gives a network-first distribution model.
His team reached out to people who could introduce them to customers, then kept
iterating on target customer, value proposition, and message. He warns that
"doing everything" becomes no positioning at all. The founder has to say who
the offer is for and what business problem it solves
([27:59-36:33]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }})).
That's why distribution and positioning belong on a founder page, not only on
[freelance]({{ '/wiki/freelance/' | relative_url }}) or consulting articles such
as [Data Engineer Consulting]({{ '/guides/data-engineer-consulting/' | relative_url }}).

## Hiring and Founder Roles

Founders begin as generalists because the company has more jobs than people.
Samuylova says her role at Evidently evolved from user conversations and
feedback processing into content, investor conversations, company setup, and
open-source evangelism. She calls the CEO role "chief everything officer" in
that context, but the concrete work depends on the startup's go-to-market. A
direct enterprise-sales startup would put the founder into sales. Evidently's
open-source path put her into content and community
([46:32-47:58]({{ '/podcasts/building-mlops-startup/' | relative_url }})).

Goyal describes the founder role at Zingg as product work, coding, integrations,
and community support. It also included content and hiring, plus incorporation,
taxation, and funding. She still wrote code, but she also called the role
"company building" rather than a pure development role
([32:59-35:10]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

Her first-hire logic was practical. She looked at where her time went and
whether the work deserved a full-time role. She also checked whether someone
else could own it and what demand came from outside the company. Zingg's first
full-time hire was a developer because the technical product needed engineering
depth
([35:14-37:25]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

Samuylova gives the hiring threshold from the other side. Before
product-market fit, a small team can change course without spending money on a
feature list that may not matter. Hiring should follow business need. Founders
hire when they have more users, more features users actually want, or more
capacity to serve demand
([57:06-57:23]({{ '/podcasts/building-mlops-startup/' | relative_url }})).
That connects founder work to
[team building]({{ '/wiki/team-building/' | relative_url }}), but the founder
decision is about timing and risk, not just org design.

## Pricing and Business Model

Founders also decide how value turns into revenue. Samuylova describes a model
where engineers and data scientists adopt the open-source tool first.
Enterprises pay for security and reliability once the product matters in
production. They also pay for someone to be responsible for the product
([51:48-56:38]({{ '/podcasts/building-mlops-startup/' | relative_url }})).

That business model depends on trust. Open source reduces the data-sharing
barrier because users can run the tool themselves. The paid offerings cover the
enterprise need for accountability.

Brudaru separates product-market fit from the paid product. DLT first looked for
adoption of the open-source library, then the company worked toward a paid
complementary product that wouldn't restrict the library. Around 55:10, he says
the team was doing user research before building that paid solution
([From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }})).
The founder decision is what stays free, what becomes paid, and whether the paid
offer strengthens or weakens adoption.

Bruckert's health-tech discussion adds a different revenue constraint. SQIN had
to prove not only technical credibility but also that healthcare AI could earn
money. She describes AI integrations with partners and point-of-sale health
checks. She also describes SaaS-like use cases and e-commerce cuts. The exact
model depends on the market, regulation, and the software being sold
([44:00-47:48]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }})).

For regulated AI founders, business model design is part of investor trust and
patient safety.

Kruszelnicki gives the pricing discipline for consulting and services. His team
benchmarked competitors, priced around value rather than production cost, and
treated willingness to pay as early evidence. He also explains why day rates
include a premium for flexibility. Founders need a starting rate and a minimum
they'll accept, and referrals punish bad incentives in a small ecosystem
([45:19-55:45]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }})).

Across software and services, founders price around customer value. They update
the model as real buyers reveal what they trust and pay for.
