---
layout: wiki
title: "Startup"
summary: "How DataTalks.Club podcast guests build, validate, fund, and operate data, AI, MLOps, and open-source startups."
related:
  - Startups
  - Founder
  - Entrepreneurship
  - Open Source
  - Open Source and Developer Relations
  - Solopreneur
  - Consultant or Freelancer to Data Product Founder
  - Freelance
  - Data Product Management
  - MLOps
  - MLOps Roadmap
  - Data Strategy
---

In the DataTalks.Club archive, a startup isn't just a small company using new
technology. Guests describe startups as constrained experiments. Founders must
learn the customer problem, build only enough product to test it, choose a
business model, and keep the team alive while evidence changes.

DataTalks.Club guests discuss startup work in data, AI,
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[open source]({{ '/wiki/open-source/' | relative_url }}). Use
[Startups]({{ '/wiki/startups/' | relative_url }}) for the broader
cross-episode cluster and this page for the singular founder playbook. For the
operating role, see [founder]({{ '/wiki/founder/' | relative_url }}). For the
broader choice to build independent work, see
[entrepreneurship]({{ '/wiki/entrepreneurship/' | relative_url }}). For a
startup-specific ML implementation view, see
[Machine Learning for Startups]({{ '/guides/machine-learning-for-startups/' | relative_url }}).

## Start With the Problem

[Elena Samuylova]({{ '/people/elenasamuylova/' | relative_url }}) gives the
clearest warning in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}).
Around 7:23, she tells technical founders not to begin with "I want to build a
machine learning startup." Start with a painful workflow instead. Her grocery
example is useful because the first apparent problem may be forecasting, but
the real blocker may be missing inventory data. If the customer can't collect
the basic data, a model isn't the first product.

[Carmine Paolino]({{ '/people/carminepaolino/' | relative_url }}) shows a
similar move from FreshFlow in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}).
Around 5:46-10:17, the team watches supermarket fresh-product managers and
learns that ordering depends on shelf checks, stockroom counts, and weather.
Local events and the fear of empty shelves also affect the order. The startup
moves from a computer-vision idea toward a broader retail operating system
because store work forces the product boundary.

[Maria Bruckert]({{ '/people/mariabruckert/' | relative_url }}) adds the
healthcare version in
[Building Digital Health Startups]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }}).
Around 2:05-6:11 and 12:20-24:08, she describes industry immersion before
product structure. The team uses cold outreach and accelerators. Clinical
meetings help them learn pharmacy constraints, hospital constraints, and legacy
workflows.

In this kind of startup,
[data strategy]({{ '/wiki/data-strategy/' | relative_url }}) includes trust and
workflow design. It also includes safe messaging, not only dataset access.

## Validate Before the Build Gets Heavy

Startup guests validate with direct evidence. Samuylova says Evidently talked
to roughly 50 people before building and more than 100 during early development.
Around 42:15-45:45 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
those interviews surfaced repeated pain around broken models and data
scientists leaving projects. People also described unmonitored production
systems. Evidently used those signals to validate
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) as a
business problem.

[Aleksander Kruszelnicki]({{ '/people/aleksanderkruszelnicki/' | relative_url }})
describes validation for consulting businesses in
[Build a Data Consulting Business]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }}).
Around 9:08-18:01, he recommends asking about the customer's current work,
recent incidents, and consequences. He also asks how often the problem happens.
Those questions come before a product pitch. His
team moved away from a "data stack as a service" idea after learning that
clients needed help translating business questions into usable data models.

That makes validation relevant to
[data engineering consulting]({{ '/guides/data-engineering-consulting/' | relative_url }})
and not only venture-backed software.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) turns
validation into a workshop in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}).
Around 36:00-40:19, the DLT team runs a three-day workshop with checkpoints,
live support, and a shared development environment. Participants came to learn,
but the startup also learned where Python users understood the abstraction and
where the tool blocked them. For open-source data products, documentation,
examples, and teaching can expose product fit earlier than a polished sales
demo. This is the service-to-product path covered more directly in
[Consultant or Freelancer to Data Product Founder]({{ '/wiki/consultant-or-freelancer-to-data-product-founder/' | relative_url }}).

## Keep the Early Stack Small

The archive doesn't treat startup speed as permission to ignore engineering.
It argues for smaller engineering choices that match the stage.

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) frames
this as lean MLOps in
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}).
Around 11:54-21:35, he recommends SaaS and managed cloud services for small
teams. Hiring someone to run infrastructure can cost more than paying for a
focused tool.

He still warns about vendor lock-in, especially when managed ML
platforms make future migration hard. Around 44:10-49:00, he names a minimal
stack around Python, CI/CD, and orchestration. He also includes observability
and portable primitives.

Paolino gives the CTO version. Around 53:09 in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}),
FreshFlow moved away from Kubeflow complexity and toward managed cloud choices.

Open source can still fit startups, but a food-waste startup needs scarce
attention for retailer learning, pilots, and forecasting quality before months
of infrastructure operations.

Radojkovic's advice also fits the [MLOps roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}).
Startup MLOps depends on stage, so founders should build enough deployment,
observability, and data reliability to learn safely. Don't turn platform
engineering into the product unless the startup is selling a platform.

## Open Source as Distribution

Several startup discussions use [open source]({{ '/wiki/open-source/' | relative_url }})
and [open source and developer relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
as go-to-market, not as a license preference. In Evidently's case, Samuylova
connects open source to model-monitoring adoption around 48:11-56:17 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}).
Open core, cloud, and on-premise deployments give the company different ways to
capture value. Engineers can try small pieces, keep sensitive data in their own
environment, and build trust before an enterprise sale.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) gives the identity
resolution case in
[Building an Open-Source ML-Powered Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
Around 2:58-11:09, she traces Zingg to repeated consulting pain around
customer, supplier, and patient records. Product records created the same kind
of matching problem. Around 24:14-31:10, she
explains why open source helped smaller teams try identity resolution. It also
helped Zingg discover more use cases, while AGPL licensing protected the
business from simple SaaS rehosting.

[Bela Wiertz]({{ '/people/belawiertz/' | relative_url }}) describes what
investors look for in
[Early-Stage Investing in Open Source Developer Tools]({{ '/podcasts/investing-in-open-source-developer-tools/' | relative_url }}).
Around 13:42-16:40, he frames open source as community-driven distribution and
bottom-up adoption. Around 32:31-39:01, he says investors still look at team,
market need, and commercialization. GitHub stars help discovery, but active
users, developer interviews, and community engagement matter more than a vanity
number.

## Services Can Become Products

Startup paths in the archive often begin with
[freelance]({{ '/wiki/freelance/' | relative_url }}), consulting, or
[solopreneur]({{ '/wiki/solopreneur/' | relative_url }}) work. Brudaru
started from data engineering projects where clients repeatedly struggled with
warehouse setup, JSON ingestion, and stakeholder alignment. Around 12:31-19:38
in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}),
he explains why building a product became more attractive than growing an
agency. Around 31:08-34:20, he says savings, consulting revenue, and
design-partner work helped fund the early company. Careful spending mattered
too.

Kruszelnicki shows the opposite choice. After product ideas failed, his team
chose consulting because clients paid for hands-on accountability and data
modeling work. Around 22:42-30:17 in
[Build a Data Consulting Business]({{ '/podcasts/data-consulting-business-pricing-and-client-acquisition/' | relative_url }}),
he ties the business to network-first acquisition, positioning, and a specific
customer segment. For data workers, the transition from consulting or
freelance work to a product isn't automatic. The repeated pain must be narrow
enough to package and valuable enough to fund.

That's why startup work connects to career and product transitions. A data
practitioner may move from implementation to diagnosis, then to reusable
assets, then to a company. The
[Consultant or Freelancer to Data Product Founder]({{ '/wiki/consultant-or-freelancer-to-data-product-founder/' | relative_url }})
page follows that transition when services reveal repeated product pain. The
[data product management]({{ '/wiki/data-product-management/' | relative_url }})
question is whether the reusable asset has a user, a workflow, and a buying
path. The [ML product manager role]({{ '/wiki/ml-product-manager-role/' | relative_url }})
adds the same discipline for ML platforms and ML-enabled products.

## Funding, Hiring, and Founder Fit

When founders raise money, they change the operating model. Around 34:06-35:47
in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}),
Samuylova discusses accelerators, angels, and grants. She also discusses
bootstrapping and investor expectations. She doesn't present venture capital as
mandatory. She presents funding as a choice that should match the kind of
company, growth speed, and commitment the founders want.

Paolino's FreshFlow story gives a more investor-facing path. Around 36:40-40:13
in
[Build a Grocery Retail OS to Cut Supermarket Food Waste]({{ '/podcasts/launch-and-build-retail-startup/' | relative_url }}),
Paolino discusses Entrepreneur First, angels, and pilots. He also discusses
demo-day narrative and investor fit. He warns that finding any investor isn't
the same as finding a good investor. Expertise, board behavior, and
expectations affect the startup after the money arrives.

Samuylova says around 57:06 in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }})
that founders shouldn't overhire before product-market fit. Hire when actual
business needs create demand for more people, not because the feature list is
long. Around 43:47-57:09, Paolino makes a similar point about early hiring. He
uses freelancers and international talent, but motivation and behavior can
matter more than a narrow skill checklist.

## Product Strategy Under Risk

Guests treat product strategy for startups as practical and domain-specific.
[Liesbeth Dingemans]({{ '/people/liesbethdingemans/' | relative_url }}) gives a
general AI product design frame in
[AI Product Design]({{ '/podcasts/ai-ml-product-design-and-experimentation/' | relative_url }}).
Around 6:43-18:21, she argues that product teams should design interfaces that
collect useful signals. They should frame the problem before the solution and
test parallel options before scaling. Around 37:15-54:11, she connects roadmaps
to prioritization, evidence, and investment cases.

Bruckert shows why this matters in health tech. Around 24:08-35:57 in
[Building Digital Health Startups]({{ '/podcasts/building-ai-digital-health-startups/' | relative_url }}),
SQIN has to route AI diagnosis into consultation and treatment. It also covers
pharmacies and prescriptions.

The app needs sensitive messaging, inclusive design, and fallbacks when the
model shouldn't decide alone. In high-risk domains, product strategy
includes what the system should refuse or defer. It also includes what the
system should hand to a human.

Brudaru's DLT example has less user risk but still needs strategy. Around
40:50-58:11 in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}),
the team positions DLT as a developer-focused library rather than a platform.
By choosing a library, the team changes its documentation, partnerships,
and bottom-up adoption. That choice also changes the future paid product. Users
need a narrow enough product to understand how to adopt it.

## Related Pages

Use [Startups]({{ '/wiki/startups/' | relative_url }}) for the broader
cross-episode map and [Founder]({{ '/wiki/founder/' | relative_url }}) for the
operating role inside a startup. [Entrepreneurship]({{ '/wiki/entrepreneurship/' | relative_url }})
covers the broader independent-work path, while
[Solopreneur]({{ '/wiki/solopreneur/' | relative_url }}) covers deliberately
small businesses.

[Open Source]({{ '/wiki/open-source/' | relative_url }}) and
[Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
cover developer-tool distribution and community adoption. [Freelance]({{ '/wiki/freelance/' | relative_url }}),
[Data Engineering Consulting]({{ '/guides/data-engineering-consulting/' | relative_url }}),
and [Consultant or Freelancer to Data Product Founder]({{ '/wiki/consultant-or-freelancer-to-data-product-founder/' | relative_url }})
cover service paths that reveal startup ideas.

[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}),
[ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }}),
and [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }}) cover product
strategy and data feasibility. [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}), and
[Machine Learning for Startups]({{ '/guides/machine-learning-for-startups/' | relative_url }})
cover startup ML systems and implementation tradeoffs.
