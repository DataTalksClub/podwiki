---
layout: wiki
title: "ML Consulting Proposals"
summary: "How DataTalks.Club guests scope machine learning consulting work: discovery calls, feasibility checks, written proposals, pricing, trust, prototypes, workshops, mentoring, delivery risk, and cases where ML should not be sold."
related:
  - Freelance
  - Data Product Management
  - Startups
  - Metrics
  - Entrepreneurship
  - Solopreneur
  - Machine Learning
---

An ML consulting proposal is the bridge between a client saying "we need machine
learning" and a consultant deciding what should actually be sold. It turns a
technical request into a shared view of the business problem. It also names the
available data and feasibility limits. It sets the delivery mode, price, and
stop conditions.

For the broader services business, start with
[[freelance|Freelance Data Engineering and Consulting]].
Use this page for the proposal work. It covers what to learn before making a
promise, how to write scope down, and when to avoid selling a model.

Sometimes the useful answer is a dashboard, workshop, feasibility study, or
mentoring engagement.
Proposal mechanics are anchored in
[[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]
([[person:mikiobraun|Mikio Braun]]). The business case and feasibility-gate
view come from
[[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]
([[person:vinvashishta|Vin Vashishta]]). Startup-readiness and prototype
discipline come from
[[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]
([[person:mariannadiachuk|Marianna Diachuk]]).

## Proposal Definition

Across these episodes, a strong ML consulting proposal is a decision document,
not merely a model spec. It starts from a technical problem and asks what the
real problem is
([[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]).
That question often uncovers organizational and product work behind the ML
request.

The ML product manager translates user needs and strategy into a business case
([[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]).
The same proposal has to stay legible to research, architecture, and funding
stakeholders. For outside consultants, the proposal should frame the problem
before it names the model.

The proposal should also define what evidence would justify moving forward.
Teams should ask how they'll measure whether a solution works before the work
begins, and use silent-mode or A/B-style rollout before exposing all users to a
risky model
([[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]).
That puts
[[metrics]],
[[data product management]],
and [[model monitoring]] inside
proposal thinking before delivery.

## Different Buyer Risks

Guests agree on problem-first scoping but focus on different buyer risks. One
emphasis is trust and scope alignment before a paid engagement: unpaid intro
meetings, trust building, problem discovery, and a written summary that clients
can comment on
([[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]).

Another emphasis is executive value and funding gates: whether more research,
architecture, or production investment is justified by the business case
([[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]).

A third emphasis is readiness and execution constraints: missing support can
force the data scientist into prerequisite work instead of ML, since pipelines,
infrastructure, and analysts are part of that support
([[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]).

Those emphases change the proposal. A mentoring proposal may sell access to a
senior ML practitioner and team judgment. A feasibility proposal may sell a
two-week exploratory and a go/no-go recommendation. A prototype proposal may
sell a limited experiment and a production-risk review. A productization
proposal may need architecture, monitoring, and ROI assumptions up front.

## Discovery Call

The discovery call has two jobs: qualify whether the consultant can help and
test whether the client is asking for a solution too early. There may be several
unpaid meetings before a decision, and trust and fit matter when the engagement
may last weeks or months
([[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]).
Separating what clients want from what they need matters too: a client may ask
for deep learning while the useful answer could be a simpler model.

A good discovery call asks for the workflow and the decision. It should also
identify the user, data owner, business consequence, and current workaround. ML
product management supports that translation layer
([[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]):
users often can't express requirements in ML terms, and executives care about
revenue, cost savings, and strategy.

The consultant has to translate both directions before proposing work.

For startup clients, discovery must also test whether the organization knows
what it expects from data science, asking about four things
([[podcast:solopreneur-data-scientist|50:38-55:00]]).

The questions are:

- how the company imagines data science work
- which problems it expects to solve
- which deadlines it expects
- how teams collaborate around results

Those questions protect the client as much as the consultant. A vague "we have
data, do something with it" request may need analytics or product discovery
before ML scope. It may also need
[[data strategy]].

## Data Access and Feasibility

ML feasibility starts with data access, data meaning, and organizational
readiness. Companies should ideally have pipelines, infrastructure, supporting
engineers or DevOps, and analysts
([[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]).
Without usable data, the consultant can't honestly sell a model-focused project.

The proposal should name the required inputs before it names an algorithm:

- tables, events, and labels
- owners and permissions
- engineering support
- analytics baselines

Feasibility also includes whether ML is a better intervention than a simpler
one. Starting with exploratory analysis lets the consultant check whether a
dashboard, query, or simpler analytics step solves the problem
([[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]).
That belongs in ML consulting proposals because it gives the client a cheaper
path when
[[machine learning]] is premature.

The funding-gate version has a proposal that receives limited exploratory
funding, then returns as a feasibility study
([[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]).
The ML architect then evaluates production path, support burden, infrastructure,
and cost. A consultant can use the same structure.

Phase one should answer whether the work can succeed and whether the client
should fund the next phase. It shouldn't pretend the whole production system is
known at kickoff.

## Prototype Scope

Prototypes are useful when they're scoped as learning, not as disguised
production commitments. Braun says around 49:21 in
[[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]
that some data science consultants start with companies that lack data science
capability. They discuss what the company wants to work on, get data produced,
and build a first prototype to decide whether to continue. For proposal writing,
prototype deliverables should include what will be learned, which data will be
used, and what decision the prototype enables.

Diachuk's 90-day startup plan gives a more operational version. In the first
week, she talks to people and explores data with a problem in mind
([[podcast:solopreneur-data-scientist|21:31]]). In the
first month, she tries to produce research, insights, or a draft model
([[podcast:solopreneur-data-scientist|22:49]]).

By the first quarter, she expects reusable methodology and pipelines. Possible
deployment and A/B-style evaluation belong in the same phase
([[podcast:solopreneur-data-scientist|24:07]]).
A consulting proposal can compress or extend that timeline, but it should keep
the same progression from problem and data toward a tested prototype.

Prototype scope should also state what's out of scope.

These deliverables create different commitments:

- notebook
- dashboard
- offline model
- silent-mode trial
- production rollout

Diachuk's silent-mode example around 55:43 in
[[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]
shows why. Fraud or credit-scoring models can affect users, so the first live
step may be shadow evaluation before A/B rollout.

Proposals for
[[production]] work need a separate
deployment, monitoring, and rollback plan.

## Written Proposal

The written proposal is where scope becomes checkable. Braun says around
22:45-23:40 in
[[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]
that he writes a summary of what he understood.

The summary covers:

- the problem the client wants to solve
- the work he's offering
- the fees

He says the act of writing is insightful because it lets the client check
whether both sides share the same understanding. He may use a Google doc so the
client can comment and discuss the scope.

For ML work, that written scope should include:

- the client's current workflow
- the decision to improve
- data access and feasibility assumptions
- deliverables and timeline
- communication cadence
- success metrics and the next decision point

Measurement belongs in that written scope. Around 34:41 in
[[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]
Diachuk supports putting measurement in the beginning. Vashishta's gated-process
discussion around 46:49-47:45 in
[[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]
supports explicit continuation gates. The proposal should make it possible to
say "continue," "change data," "ship a simpler solution," or "stop."

## Pricing and Trust

Pricing is part of scope because each model allocates uncertainty differently.
Braun describes hourly work around 24:15 in
[[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]
as transparent. It still has a weak incentive: the consultant earns more by
working more hours, not necessarily by helping the client more. Around 25:19-28:07, he
discusses value-based and fixed-price alternatives, but notes that ML outcomes
are uncertain and some clients still reason in salary-like terms. Around
29:51-30:02, he says fixed rates can let the consultant focus on the work while
also giving the client a budget.

The proposal should match pricing to uncertainty:

- Hourly or day-rate work fits discovery, advisory, mentoring, and ambiguous investigation.
- Fixed-price prototypes fit when data access, deliverable, and evaluation are narrow.
- Value-based pricing needs a credible business metric and a shared attribution story.

Vashishta's monetization framing around 8:14-11:49 in
[[podcast:make-money-with-machine-learning-roles-skills|Monetizing Machine Learning]]
explains why executives care. ML is expensive, and teams need a strategy for
revenue, cost savings, or product value.

Trust is built before and during pricing. Braun treats unpaid intro meetings as
part of building trust and fit
([[podcast:freelancing-in-machine-learning|20:15]]).
Diachuk treats continuous expectation management as part of data science work,
especially because ML isn't deterministic
([[podcast:solopreneur-data-scientist|26:20-27:35]]).
For a proposal, the trust move isn't to promise certainty. It's to explain
which parts are known, which parts require exploration, and how the client will
know whether the next investment is justified.

## Workshops and Mentoring Work

Not every ML consulting proposal should sell implementation. Braun says around
7:24 in
[[podcast:freelancing-in-machine-learning|Freelancing in Machine Learning]]
that he chose not to be hands-on and works more on mentoring. This lets him help
several projects in parallel. Around 48:50-49:21, he describes longer
engagements where the output is what the team accomplishes.

Concepts and written analysis can be part of that output. For productionizing
work, the consultant may run workshops, analyze the current situation, and tell
the company what to work on.

That consulting structure is closer to
[[data product management]]
than to staff augmentation. It's also close to
[[business skills for data professionals]].
The client pays for judgment and acceleration, not just code.

The deliverables can include:

- workshops and mentoring sessions
- architecture and project reviews
- prioritization sessions
- written recommendations
- team decisions

Mentoring proposals should still have outcomes. Diachuk's communication section
around 41:46-43:54 in
[[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]
supports several delivery formats.

These delivery formats are useful:

- reports and visualizations
- team calls and one-on-one discussions
- company-wide tech talks that educate the organization

A mentoring proposal can define artifacts:

- roadmap
- review notes
- prototype critique
- evaluation plan
- workshop deck

It can measure success through team decisions and reduced delivery risk.

## Delivery Risks

ML proposals should name delivery risks explicitly because discovery often
changes the work. Diachuk says around 14:25-16:54 in
[[podcast:solopreneur-data-scientist|Introducing Data Science in Startups]]
that initial requests can be vague and priorities become clearer over time.
Feasibility, impact, and stakeholder alignment decide what should be done first.
Around 48:27-49:30, she recommends switching away from a project when it's no
longer the most important or effective way to deliver insight.

Common proposal risks include:

- unusable data or missing labels
- unclear ownership
- no analytics baseline
- no stakeholder who can act on the output
- unrealistic deadlines
- no deployment path or monitoring owner

Diachuk's readiness questions around 50:38-55:00 cover many of these risks.
Vashishta's architecture discussion around 48:59-51:20 adds production cost,
support burden, and ROI. Braun's written-scope advice around 22:45-23:40 adds
the practical fix: write the assumptions down so the client can correct them
before work begins.

## Bad ML Sales

The strongest proposal may reject ML when evidence points elsewhere. In
[[podcast:solopreneur-data-scientist|the startup episode]],
Diachuk says around 20:21 that data science isn't the first step.

Companies may need dashboards and simple analytics before automated models.
Around 28:35, she recommends starting with exploratory analysis and simpler
approaches before focusing on model building. Braun gives the consulting version
around 21:37-21:59 in
[[podcast:freelancing-in-machine-learning|his freelancing episode]].
A request for deep learning may hide a simpler problem.

Don't sell an ML implementation when the buyer can't supply usable data. The
same caution applies when there's no decision owner, measurable success
criterion, or path to action.

Sell a smaller next step:

- discovery sprint
- analytics audit
- workshop or dashboard
- data readiness review
- prototype feasibility study

The
[[Machine Learning for Startups]]
guide expands the startup version of this rule.
[[Solopreneur Data Scientist]]
uses Diachuk's episode to show how solo data work starts with small evidence
and stakeholder alignment before larger ML commitments.

## Related Pages

These pages cover adjacent service, product, metric, and startup decisions.

- [[freelance|Freelance Data Engineering and Consulting]]
- [[Data Product Management]]
- [[Metrics]]
- [[startups|Startup]]
- [[Entrepreneurship]]
- [[Solopreneur]]
- [[Machine Learning for Startups]]
- [[Solopreneur Data Scientist]]
