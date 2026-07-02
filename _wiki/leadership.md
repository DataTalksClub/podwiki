---
layout: wiki
title: "Leadership"
summary: "How DataTalks.Club podcast guests describe data and AI leadership across manager, senior IC, platform, strategy, hiring, mentoring, stakeholder, and data science manager roles."
related:
  - Data Teams
  - Hiring
  - Career Growth
  - Data Strategy
  - Data Science
  - Machine Learning
  - Machine Learning System Design
  - Data Engineering
  - Data Engineer Role
  - Data Engineering Platforms
  - DataOps
  - MLOps
  - Data Quality and Observability
  - Data Product Management
---

DataTalks.Club guests describe leaders as people who increase other people's
ability to do useful data and AI work. The episodes place that work in formal
management, senior IC mentoring, and platform ownership. First data hires show
leadership when they build business trust. Executives show it when they turn
data work into strategy. [Tereza Iofciu](https://datatalks.club/people/terezaiofciu.html)
makes that boundary explicit in
[Data Leadership Coaching](https://datatalks.club/podcast/data-leadership-coaching.html):
people don't need a leadership title to develop leadership skills (about 6:17).

Across the podcast episodes, guests keep data and AI leadership close to
operating work. They talk about manager and expert paths. They also cover team
design, hiring, coaching, and stakeholder translation. Portfolio judgment,
platform ownership, and scale appear throughout these episodes.

For data engineering managers, that means aligning people with priorities and
connecting platform work to reliability. The manager still needs technical
judgment, but the job is no longer to personally own every pipeline.

For data science managers, the same leadership work requires working knowledge
of [data science]({{ '/wiki/data-science/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). That knowledge lets managers guide
problem framing. It also helps them ask about data quality, baselines, and
operational responsibility. It doesn't mean replacing the team's strongest
modeler, machine learning engineer, or platform specialist.

## Manager and Expert Paths

[Barbara Sobkowiak](https://datatalks.club/people/barbarasobkowiak.html) gives the
cleanest manager-versus-expert distinction in
[Data Science Manager vs Expert](https://datatalks.club/podcast/data-science-manager-vs-expert-hiring-guide.html).

She says a data science manager needs broad technical literacy and strategy.
The manager also needs stakeholder communication and team development. They
need the judgment to redirect a modeling effort when "good enough" is enough
(about 8:22, 13:29, and 15:49).
The expert role is different. The expert brings deep technical and domain
knowledge for hard modeling or domain-specific problems (about 25:02 and 28:48).

That distinction matters for leadership because the wrong hire creates the
wrong operating system for the team. Sobkowiak warns that companies often write
manager job descriptions as if they were hiring a senior technical expert. They
then attach some team duties. If the team needs coordination and translation,
a deep expert alone leaves gaps. The same is true for prioritization and people
development
([Data Science Manager vs Expert](https://datatalks.club/podcast/data-science-manager-vs-expert-hiring-guide.html),
about 31:56 and 34:04).

[Katie Bauer](https://datatalks.club/people/katiebauer.html) adds a career-path
boundary in
[How to Hire, Manage, and Grow a Data Science Team in B2B SaaS](https://datatalks.club/podcast/hiring-and-managing-data-science-teams-in-b2b-saas.html).
She treats the move between individual contributor and people management as a
real option rather than a one-way promotion ladder. Trying management can make
someone a better senior IC because they learn how managers think about
stakeholders, tradeoffs, and growth (about 25:54).

Senior IC leadership still exists. Staff-style roles and delegation give people
more scope without people management. So do cross-functional influence and
technical leadership (about 18:50).

For data engineering, the same boundary separates a manager from the deepest
platform specialist. That specialist may focus on streaming, transformation,
orchestration, or cloud infrastructure. A manager still needs enough technical
literacy to ask good questions and assign the right decision owner.

The manager's impact comes from team design and hiring. It also comes from
roadmap tradeoffs, standards, and recovery habits. Deep architecture and niche
platform work can stay with senior engineers or staff engineers when that's the
stronger path
([Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

For data science managers, literacy is a map rather than expert depth.
Sobkowiak's manager-versus-expert episode ties that map to project discovery
and data quality. It also covers baselines and success metrics. Managers need to
tell stakeholders when a simpler approach is enough (about 15:49 and 43:04).

[Geo Jolly](https://datatalks.club/people/geojolly.html) adds the
platform-product version in
[Product Management for Machine Learning](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html):
technical leaders should define the problem and outcome before jumping to a
solution. They should then measure adoption and productivity for the internal
users of an ML platform (about 11:24, 18:25, and 31:28).

That's the manager literacy floor: understand problem framing and data
availability. Leaders should ask about baselines and modeling. They then follow
the work through evaluation, deployment, monitoring, and adoption. The leader
should also know which decisions need a specialist. They should know which
choices are reversible and which ones create production or stakeholder risk
([Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }})).

## Data Engineering Management

[Rahul Jain](https://datatalks.club/people/16rahuljain.html) gives the clearest
data engineering leadership discussion in
[Data Engineering Leadership and Modern Data Platforms](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html).
He frames the manager role as servant leadership. That means enabling a
self-motivated team, setting quality expectations, and supporting career
growth. It also means keeping the team away from monotonous work. Technical
credibility still matters because the manager must be able to coach engineers
and discuss implementation choices when needed (about 7:27, 8:54, 13:15, and
33:39).

That makes data engineering management an operating role. The manager clarifies
ownership for orchestration, warehouse work, and streaming. Schema changes and
governance need owners too, as do
[cloud cost]({{ '/wiki/finops-for-data-engineers/' | relative_url }}), data
contracts, and incident response.

Managers also decide when a one-off pipeline request should become a reusable
platform path. That synthesis connects Jain's engineering leadership to
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

[Slawomir Tulski](https://datatalks.club/people/slawomirtulski.html) adds the
role-design boundary in
[Data Engineer Career in 2026](https://datatalks.club/podcast/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for.html).
He separates platform-oriented engineering from product-facing data
engineering. The platform side emphasizes shared infrastructure, conventions,
cost-aware systems, and developer experience. Product-facing data engineering
sits closer to domains and modeled datasets. It also stays close to metrics and
stakeholder delivery (about 11:54 and 25:33, with the overbuilding point around
30:56).

For a manager, that distinction decides the roadmap and the hiring brief. A
team that tries to do both without naming the split can let urgent stakeholder
requests crowd out reliability work. Platform work can also drift away from
real users.

The same episode also challenges architecture theater. Tulski's real-time
discussion asks whether low latency changes the business outcome before the
team chooses Kafka, Spark, or streaming architecture (about 38:01). That's
leadership because the manager protects the team from overbuilding. The manager
still reserves capacity for the systems that make data usable.

## Team Design and Hiring

Data leaders design the team before they design the roadmap.
[Lisa Cohen](https://datatalks.club/people/lisacohen.html) gives one of the clearest
data science org-design discussions in
[Designing High-Impact Data Science Teams](https://datatalks.club/podcast/data-science-team-structure-and-org-design.html).

She compares centralized, embedded, and hybrid models. Central teams protect
standards, knowledge sharing, career development, and peer learning.
Data scientists embedded in product teams gain domain context and faster product
decisions. Hybrid models try to hold both benefits (about 6:27, 24:53, and
25:48).

Leaders make that choice to structure how the team works. Cohen also ties data
science teams to product, engineering, and design. Research and shared OKRs
belong in the same operating model. Planning rhythms keep managers and ICs close
to the people building or using the product (about 18:43 and 21:17). The related
[team building]({{ '/wiki/team-building/' | relative_url }}) page expands this
operating model.

Bauer describes data science managers in matrix organizations. A data person
may report to a data leader while working day to day with product or
engineering. They may also work with marketing or another business group.

In that structure, the data leader protects craft quality and documentation.
The data leader also protects peer review and career growth. That matters even
when a dotted-line stakeholder drives daily priorities
([Hiring and Managing Data Science Teams in B2B SaaS](https://datatalks.club/podcast/hiring-and-managing-data-science-teams-in-b2b-saas.html),
about 8:33 and 11:58). In this example, leadership is about
[data teams]({{ '/wiki/data-teams/' | relative_url }}), not one title.

[Tammy Liang](https://datatalks.club/people/tammyliang.html) shows the first-team
version in
[Building and Leading Data Teams](https://datatalks.club/podcast/building-and-scaling-data-team.html).
Her team started by proving the value of business health dashboards. It added
data engineering capacity after management trusted the team's impact (about
7:22 and 15:04).

She later says she would have valued senior people earlier.
Early team members need business alignment and learning speed. They also need
enough leadership mindset to help grow the team (about 23:11 and 33:09).

Leadership also changes how a team hires juniors. Bauer argues that juniors can
strengthen an organization over time. They need mentorship, skills support,
project-based learning, and regular check-ins. They also need access to people
who can explain how product managers and senior leaders think (about 30:10,
34:16, and 40:12).

Hiring a junior is therefore a leadership commitment, not only a lower-cost
staffing choice. For more role-design work across data scientists, analysts,
and data engineers, see [hiring]({{ '/wiki/hiring/' | relative_url }}).

[Nicolas Rassam](https://datatalks.club/people/nicolasrassam.html) makes the data
engineering version concrete in
[Hiring Data Engineers in Europe](https://datatalks.club/podcast/hiring-for-data-engineering-jobs-in-europe.html).
He warns that titles hide relevant experience. Software engineers, BI
engineers, analysts, and data scientists may have built pipelines or modeled
data. They may also have handled scale or fixed quality problems (about 18:47
and 20:57). A data engineering manager should therefore hire for the missing
capability rather than a vague title.

The hiring brief should name the actual gap. Platform-heavy teams need storage
and orchestration while access, cloud infrastructure,
[cost]({{ '/wiki/finops-for-data-engineers/' | relative_url }}), and standards
belong in the same brief. Product-facing teams need domain pipelines, data
products, event definitions, and stakeholder collaboration.

Analytics-engineering work needs SQL modeling, tests, documentation, and
semantic definitions. BI-ready tables matter too
([Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})).
Rassam's level discussion gives managers another filter. Juniors show
fundamentals and task execution, while mid-level engineers show project
ownership. Senior engineers show tradeoff reasoning, technical influence, and
business context (about 22:55 and 26:38).

## Mentorship and Feedback

Several guests describe leadership as creating growth conditions for other
people. [Mariano Semelman](https://datatalks.club/people/marianosemelman.html)
describes his data science manager work as meetings, mentoring, and coaching.
Planning and people development sit in the same job in
[Data Science Leadership](https://datatalks.club/podcast/data-science-leadership-hiring-mlops.html)
(about 5:45).

When he took over a team, he used a 30-60-90 plan. He first met
people and listened. Then he learned the projects and domain before giving
feedback (about 12:52).

Semelman's feedback practice is careful because manager feedback changes a
person's career. He recommends asking permission, showing care, and offering
options rather than treating managerial opinion as objective truth
([Data Science Leadership](https://datatalks.club/podcast/data-science-leadership-hiring-mlops.html),
about 40:25 and 44:17). His one-on-one discussion also frames mistakes as part
of a safe learning environment (about 48:13).

Jain's data engineering leadership episode adds the engineering version of this
same coaching work. The manager creates standards and career paths while
leaving room for engineers to own the work. That keeps mentorship connected to
quality, not only to morale.

The practical learning path for managers starts here because the first skill
isn't a library or a modeling technique. It's learning how to ask better
questions about people, problems, and tradeoffs.

Managers can learn from several episodes:

- Sobkowiak for role boundaries and project discovery
- Cohen for team-structure tradeoffs
- Iofciu for influence, feedback, and visibility
- Jain for standards, career paths, and self-motivated teams

([Data Science Manager vs Expert](https://datatalks.club/podcast/data-science-manager-vs-expert-hiring-guide.html),
[Designing High-Impact Data Science Teams](https://datatalks.club/podcast/data-science-team-structure-and-org-design.html),
[Data Leadership Coaching](https://datatalks.club/podcast/data-leadership-coaching.html),
[Data Engineering Leadership](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html)).

From there, managers can add technical fluency in layers. They learn problem
framing, data quality, and metrics before adding baselines and modeling limits.
Deployment, monitoring, adoption, and governance come next. That sequence keeps
the learning path useful for both data science and data engineering leaders
instead of turning leadership into a second individual-contributor track.

## Stakeholder Work and Product Judgment

Data and AI leadership often fails when technical work can't be translated
into stakeholder priorities. Iofciu describes influence without authority as
speaking different work languages and listening actively. The leader then
connects a project to what matters for the other person
([Data Leadership Coaching](https://datatalks.club/podcast/data-leadership-coaching.html),
about 46:00 and 49:20). She also argues that data foundation work, models, and
open-source work need visibility because impact isn't always customer-facing
(about 24:32 and 43:38).

Semelman gives the product version of the same practice. He warns that data
scientists can spend time on technically interesting work that doesn't change
user outcomes. He connects product managers and data scientists. He starts
from user impact and spends modeling time where it changes the product or
production test
([Data Science Leadership](https://datatalks.club/podcast/data-science-leadership-hiring-mlops.html),
about 29:29, 30:06, and 36:50).

This links leadership to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) because product impact depends on
deployment and testing. It also depends on monitoring and iteration, not only
offline model quality.

[Jack Blandin](https://datatalks.club/people/jackblandin.html) adds an applied ML
stakeholder lesson in
[From Software Engineer to VP of Machine Learning](https://datatalks.club/podcast/from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership.html).
He describes stakeholder buy-in as something leaders earn through product-level
understanding and trust. Leaders also need to speak in the stakeholder's metrics
(about 9:01, 11:33, and 15:25).

His fast proof-of-concept advice keeps ML leadership honest because teams start
with baselines and demos before larger requests. They then use quick hypothesis
tests before asking for larger engineering investment (about 20:48, 28:46, and
31:03).

Cohen's team-design episode adds the metrics version of stakeholder work.
Product changes can move more than one metric, so data science leaders need
cross-functional interpretation. Product, engineering, and design partners help
interpret those tradeoffs. Research and leadership partners do too
([Designing High-Impact Data Science Teams](https://datatalks.club/podcast/data-science-team-structure-and-org-design.html),
about 18:43 and 37:24).

Geo's ML product episode adds the platform version. Internal tools still have
users, so leaders need requirements and rollout plans. They also need
observability and release governance. Adoption measures matter more than a list
of impressive capabilities (about 9:50, 15:19, 31:28, and 57:20).

For data science and ML projects, useful stakeholder communication usually names:

- the current workflow
- the decision or workflow that should improve
- the baseline and success metric
- the guardrail metric
- the main uncertainty
- the next stakeholder decision

Those checks connect leadership to
[communication]({{ '/wiki/communication/' | relative_url }}),
[metrics]({{ '/wiki/metrics/' | relative_url }}), and
[experimentation]({{ '/wiki/experimentation/' | relative_url }}).

Data engineering leaders face the same prioritization problem with different
artifacts.

A roadmap should name value in concrete terms:

- availability and reliability
- delivery speed and cost
- governance and downstream trust

For data engineering requests, managers should answer four questions:

- Who consumes the data?
- What decision or workflow changes?
- What reliability risk appears?
- Who owns recovery?

Those questions keep prioritization tied to actual consumers
([Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})).
That keeps platform investment tied to faster onboarding and safer schema
changes. It also ties work to lower support load, clearer lineage, and fewer
downstream surprises rather than to the appearance of maturity.

## Project and Portfolio Signals

Managers need better project signals than "the model is almost done" or "the
pipeline is in progress." Data and AI work contains discovery risk. Leaders
need to separate exploration, validation, production, and adoption.
[Barbara Sobkowiak](https://datatalks.club/people/barbarasobkowiak.html) gives
the first filter.

Managers should ask:

- what the stakeholder does today
- what data exists
- what baseline is credible
- what success metric would justify more work

([Data Science Manager vs Expert](https://datatalks.club/podcast/data-science-manager-vs-expert-hiring-guide.html),
about 15:49, 42:05, and 43:04).

Healthy portfolio signals are practical. The team can explain the baseline and
why a new approach should beat it. Data quality risks are visible before heavy
modeling starts. The project has a decision owner, not only a technical sponsor.

Evaluation metrics connect to business or product outcomes. A path to
deployment, monitoring, support, and adoption exists before the system becomes
business-critical.

Those signals aren't only for data science.
[Tereza Iofciu](https://datatalks.club/people/terezaiofciu.html) argues in
[Data Leadership Coaching](https://datatalks.club/podcast/data-leadership-coaching.html)
that foundation work needs visibility alongside models and open-source work.
That impact isn't always customer-facing (about 24:32 and 43:38).

[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) and
[Barr Moses](https://datatalks.club/people/barrmoses.html) make the same point for
data engineering reliability. Tests and observability are project signals.
Ownership, SLAs, and runbooks also tell stakeholders whether important data can
be trusted after launch
([DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html),
[Data Observability Explained](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html)).

## ML Limits

Good data leadership includes the ability to slow down an ML request.
[Barbara Sobkowiak](https://datatalks.club/people/barbarasobkowiak.html)
describes stakeholders asking for AI or ML because they expect "magic." Her
response is managerial. Clarify the current workflow and check the data. Compare
against a baseline.

Then decide whether a moving average or rule already solves the problem. A
dashboard or workflow change may be enough too
([Data Science Manager vs Expert](https://datatalks.club/podcast/data-science-manager-vs-expert-hiring-guide.html),
about 42:05 and 43:04).

[Valerii Babushkin](https://datatalks.club/people/valeriybabushkin.html) makes the
same boundary a system-design habit in
[ML System Design Interviews](https://datatalks.club/podcast/machine-learning-system-design-interview.html).
Around 52:25, avoiding ML is a valid design outcome when a heuristic, rule, or
existing product behavior is enough.
[Ben Wilson](https://datatalks.club/people/benwilson.html) adds the production
engineering version in
[Practical Machine Learning Engineering for Production](https://datatalks.club/podcast/machine-learning-engineering-production-best-practices.html):
simple SQL and statistics can be stronger than hard-to-maintain model novelty.
So can rules and timeboxed proof points when the baseline already satisfies the
product need.

Managers should pause before ML when:

- the team can't name the decision
- usable historical data is missing
- data quality problems dominate the signal
- a baseline hasn't been tried
- no adoption owner exists
- the organization can't monitor and maintain the model

Sometimes leadership means redirecting the request toward a metric or pipeline.
It can also mean choosing an experiment, dashboard, or clearer product decision.

## Production and MLOps Boundaries

A trained model creates production responsibility as well as modeling work.
Managers need enough production literacy to notice that handoff even when a
specialist owns MLOps.
[Geo Jolly](https://datatalks.club/people/geojolly.html) puts observability and
release governance inside product leadership for ML systems in
[Product Management for Machine Learning](https://datatalks.club/podcast/ml-product-manager-and-mlops-platform-strategy.html).
Platform adoption belongs there too (about 31:28, 35:18, and 57:20).
[Mariano Semelman](https://datatalks.club/people/marianosemelman.html) adds in
[Data Science Leadership](https://datatalks.club/podcast/data-science-leadership-hiring-mlops.html)
that product impact depends on deployment and testing, not only on a promising
notebook (about 33:36 and 36:50).

That literacy means asking:

- who owns input data quality after launch
- who watches prediction quality, drift, and latency
- who responds to failures
- how changes are validated
- what fallback exists when the model is wrong, stale, or unavailable

[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) cover the
technical practice in more depth. On this page, the leadership point is
ownership: production ML shouldn't depend on informal heroics or a manager's
hope that "deployment" means "finished."

## Platform Ownership and Scaling

Leadership becomes more architectural when a team scales. [Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html)
describes scale-up pressure in
[Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html).
Companies grow users, products, and teams faster than early data systems can
comfortably support (about 5:41 and 10:21).

His response goes beyond hiring more engineers because he describes
self-service data platforms and onboarding conventions. He also describes
playbooks, Kafka schemas, and data contracts.

Those practices let more teams move without routing every request through the
same data engineers (about 12:30, 17:22, and 23:26).

OUAZZA also connects scaling to seniority and role evolution. In scale-ups, he
recommends hiring senior people early to set best practices, especially for
platform and niche technology work (about 20:13). As teams grow, people often
move from broad generalist work toward more specialized platform or pipeline
roles (about 50:17).

Senior leadership shows up as broader impact. People look
beyond one team's backlog, talk with nearby teams, and solve problems that help
more than one group (about 54:31). The platform side belongs with
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

Liang's episode shows the adoption side of scaling. Her team moved from
dashboards to forecasting and data products. Business teams still needed trust,
workshops, and Q&A. They also needed data culture work before the outputs
changed daily decisions
([Building and Leading Data Teams](https://datatalks.club/podcast/building-and-scaling-data-team.html),
about 35:38, 47:08, and 49:00).

Her leadership motto is to give project ownership to the people doing the work.
A growing team can't depend on one leader micromanaging every project (about
50:52).

## Reliability and DataOps

Reliability is a leadership responsibility because managers set how work is
reviewed, deployed, monitored, and recovered. [Christopher Bergh](https://datatalks.club/people/christopherbergh.html)
turns this into an operating model in
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html).

He connects reliable data delivery to automation and observability.
Productivity, version control, and tests are part of the same operating model.
He also emphasizes CI/CD and realistic test data. Deployment confidence is part
of the same discussion (about 15:52 and 30:55, plus 42:39).

Weak operating habits create fear and hero-driven recovery. They also create turnover
and avoidable rework (about 13:27 and 34:13, plus 58:15).

[Barr Moses](https://datatalks.club/people/barrmoses.html) gives the observability
side in
[Data Observability Explained](https://datatalks.club/podcast/data-quality-data-observability-data-reliability.html).

She argues that data incidents aren't limited to failed jobs. Teams need
freshness and volume. They also need distribution and schema visibility.
Lineage matters because a pipeline can run and still deliver late, incomplete,
or misleading data (about 16:38 and 19:10, plus 21:57). Her later discussion of
RACI-style accountability, SLAs, and runbooks makes ownership visible before
stakeholders discover the problem first (about 29:00 and 35:24, plus 41:03).

For data engineering managers, DataOps is therefore not a separate tool list.
It's the management habit of defining review, deployment, observability, and
incident communication. Recovery paths for important datasets and pipelines
belong in the same habit. For the discipline in more depth, use
[DataOps]({{ '/wiki/dataops/' | relative_url }}). Here, DataOps is part of
leadership because the team needs explicit standards and owners.

## Strategy and Operating Discipline

At executive scope, leadership turns data work into a strategy that other
leaders can act on. [Marco De Sa](https://datatalks.club/people/marcodesa.html)
describes the Chief Data Officer role in
[Mastering the Chief Data Officer Role](https://datatalks.club/podcast/chief-data-officer-data-strategy-and-org-design.html)
as data strategy and governance. The role also covers AI direction and team
design. It includes preparation for future products (about 6:08, 7:17, and
10:19).

He separates strategy from
tactics by breaking a broad direction into goals and KPIs. Teams can then
execute smaller strategy blocks (about 17:37).

De Sa's org-design comments keep strategy grounded in delegation. He says data
leaders need the right teams and people who know the details better than the
executive. The leader then articulates a single vision across those teams
(about 11:40). Later, he frames the CDO as closer to executive strategy. The VP
of data is more attached to specific strategy components, though the exact split
depends on the organization (about 20:17 and 24:55).

Leadership in these examples sits inside
[data strategy]({{ '/wiki/data-strategy/' | relative_url }}) and
[data teams]({{ '/wiki/data-teams/' | relative_url }}), and it pushes manager
literacy upward into strategy. De Sa works backward from goals, governance,
platforms, and AI investment. Geo does the same at product scope by turning ML
platform work into roadmaps, adoption, and release quality. Sobkowiak does it at
team scope by separating management, expert depth, and project prioritization.

Leadership works through visibility, tradeoffs, and ownership. Sobkowiak ties
management to strategy, stakeholder communication, personal development, and
project prioritization. Bauer ties leadership to craft quality and growth in
matrix teams. Semelman ties it to product impact and feedback.

Jain ties leadership to self-organized engineering teams and quality, while
OUAZZA ties it to self-service platforms and senior influence. Liang ties it to
trust, adoption, and ownership. De Sa ties it to organization-wide strategy and
delegation. Together, they make leadership a data and AI delivery practice, not
only a manager title.
