---
layout: wiki
title: "Leadership"
summary: "Data and AI leadership across management, senior IC work, decision rights, accountability, platforms, and strategy."
related:
  - Data Teams
  - Hiring
  - Career Growth
  - Mentoring in Tech
  - Team Building
  - Data Team Lead Role
  - Communication
  - Data Science for Managers
  - Data Strategy
  - Data Trust and Strategy
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

Leadership increases other people's ability to do useful data and AI work. That
work appears in formal management, senior IC
[[mentoring-in-tech=>mentoring]], and platform ownership.
First data hires show leadership when they build business trust. Executives show
it when they turn data work into strategy. [[person:terezaiofciu=>Tereza Iofciu]]
makes that boundary explicit in
[[cite:data-leadership-coaching=>Data Leadership Coaching]]:
people don't need a leadership title to develop leadership skills.

Data and AI leadership stays close to operating work through manager and expert
paths. It sets decision rights, accountability, coaching habits, and stakeholder
translation. Portfolio judgment, platform ownership, and scale belong in the
same leadership surface.

For [[data-engineering-manager-role=>Data Engineering Manager]] roles, that means aligning people with
priorities and connecting platform work to reliability. The manager still needs
technical judgment, but the job is no longer to personally own every pipeline.

For data science managers, the same leadership work requires working knowledge
of [[data science]],
[[machine learning]], and
[[MLOps]]. That knowledge lets managers guide
problem framing. It also helps them ask about data quality, baselines, and
operational responsibility. It doesn't mean replacing the team's strongest
modeler, machine learning engineer, or platform specialist.

[[person:sadatanwar=>Sadat Anwar]] gives the transition version of the same
boundary. Moving from engineering management into data science management
keeps the people-management surface. It changes the domain, stakeholder
questions, and success evidence.

Conflict resolution and hiring become part of the manager's technical-adjacent
work. Business metrics and team-health signals also move into the manager's work
([[cite:from-software-engineering-to-leading-data-science-teams@30:25=>Software Engineer to Data Science Manager]],
[[cite:from-software-engineering-to-leading-data-science-teams@57:34=>Software Engineer to Data Science Manager]]).
That path connects leadership directly to the [[Data Team Lead Role]].

## Manager and Expert Paths

[[person:barbarasobkowiak=>Barbara Sobkowiak]] gives the
cleanest manager-versus-expert distinction in
[[cite:data-science-manager-vs-expert-hiring-guide=>Data Science Manager vs Expert]].

She says a data science manager needs broad technical literacy and strategy.
The manager also needs stakeholder communication and team development. They
need the judgment to redirect a modeling effort when "good enough" is enough.
The expert role is different. The expert brings deep technical and domain
knowledge for hard modeling or domain-specific problems.

That distinction matters for leadership because the wrong hire creates the
wrong operating system for the team. Sobkowiak warns that companies often write
manager job descriptions as if they were hiring a senior technical expert. They
then attach some team duties. If the team needs coordination and translation,
a deep expert alone leaves gaps. The same is true for prioritization and people
development
([[cite:data-science-manager-vs-expert-hiring-guide@34:04=>Data Science Manager vs Expert]]).

[[person:katiebauer=>Katie Bauer]] adds a career-path
boundary in
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>How to Hire, Manage, and Grow a Data Science Team in B2B SaaS]].
She treats the move between individual contributor and people management as a
real option rather than a one-way promotion ladder. Trying management can make
someone a better senior IC because they learn how managers think about
stakeholders, tradeoffs, and growth.

Senior IC leadership still exists. Staff-style roles and delegation give people
more scope without people management. So do cross-functional influence and
technical leadership.
For AI systems, the [[staff-ai-engineer=>staff AI engineer]] page shows the same
leadership path. Architecture, evaluation standards, and cross-team influence
can replace direct reports
([[cite:from-academia-to-staff-ai-engineer-interviews-and-career-growth=>Staff AI Engineer Transition]]).

For data engineering, the same boundary separates a manager from the deepest
platform specialist. That specialist may focus on streaming, transformation,
orchestration, or cloud infrastructure. A manager still needs enough technical
literacy to ask good questions and assign the right decision owner.

The manager's impact comes from decision ownership, roadmap tradeoffs,
standards, and recovery habits. Deep architecture and niche platform work can
stay with senior engineers or staff engineers when that's the stronger path
([[Data Engineer Role]],
[[Data Engineering Platforms]]).

For data science managers, literacy is a map rather than expert depth.
Sobkowiak's manager-versus-expert episode ties that map to project discovery
and data quality. It also covers baselines and success metrics. Managers need to
tell stakeholders when a simpler approach is enough.

[[person:geojolly=>Geo Jolly]] adds the
platform-product version in
[[cite:ml-product-manager-and-mlops-platform-strategy=>Product Management for Machine Learning]]:
technical leaders should define the problem and outcome before jumping to a
solution. They should then measure adoption and productivity for the internal
users of an ML platform.

That's the manager literacy floor: understand problem framing and data
availability. Leaders should ask about baselines and modeling. They then follow
the work through evaluation, deployment, monitoring, and adoption. The leader
should also know which decisions need a specialist. They should know which
choices are reversible and which ones create production or stakeholder risk
([[Machine Learning System Design]],
[[MLOps]]).

## Data Engineering Management

[[person:16rahuljain=>Rahul Jain]] gives the clearest
data engineering leadership discussion in
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership and Modern Data Platforms]].
He frames the manager role as servant leadership. That means enabling a
self-motivated team, setting quality expectations, and supporting career
growth. It also means keeping the team away from monotonous work. Technical
credibility still matters because the manager must be able to coach engineers
and discuss implementation choices when needed.

That makes data engineering management an operating role. The manager clarifies
ownership for orchestration, warehouse work, and streaming. Schema changes and
governance need owners too, as do
[[finops-for-data-engineers=>cloud cost]], data
contracts, and incident response.

Managers also decide when a one-off pipeline request should become a reusable
platform path. That synthesis connects Jain's engineering leadership to
[[Data Engineering]],
[[DataOps]], and
[[Data Quality and Observability]].

[[person:slawomirtulski=>Slawomir Tulski]] adds the
role-design boundary in
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]].
He separates platform-oriented engineering from product-facing data
engineering. The platform side emphasizes shared infrastructure, conventions,
cost-aware systems, and developer experience. Product-facing data engineering
sits closer to domains and modeled datasets. It also stays close to metrics and
stakeholder delivery.

For a manager, that distinction decides the roadmap and the hiring brief. A
team that tries to do both without naming the split can let urgent stakeholder
requests crowd out reliability work. Platform work can also drift away from
real users.

The same episode also challenges architecture theater. Tulski's real-time
discussion asks whether low latency changes the business outcome before the
team chooses Kafka, Spark, or streaming architecture. That's
leadership because the manager protects the team from overbuilding. The manager
still reserves capacity for the systems that make data usable.

## Decision Rights Across Org Models

Data leaders don't only choose an org chart. They decide where craft standards,
delivery priorities, and accountability live. [[person:lisacohen=>Lisa Cohen]]
gives one of the clearest data science org-design discussions in
[[cite:data-science-team-structure-and-org-design=>Designing High-Impact Data Science Teams]].

In Cohen's comparison, central teams protect standards and knowledge sharing.
They also protect career development and peer learning. Data scientists embedded
in product teams gain domain context and faster product decisions. Hybrid models
try to hold both benefits.

Leaders need to know who can change priorities and who protects craft. They also
need a conflict path when product pressure and data quality pull in different
directions. Cohen ties data science teams to product, engineering, design, and
research partners through shared OKRs and planning rhythms. The related
[[team building]] page owns the hiring order, team structure, rituals, and trust
details behind that operating model.

[[person:katiebauer=>Katie Bauer]] describes the matrix version in
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>Hiring and Managing Data Science Teams in B2B SaaS]].
A data person may report to a data leader while working day to day with product,
engineering, marketing, or another business group. In that structure, the data
leader protects craft quality and documentation. The data leader also protects
peer review and career growth when a dotted-line stakeholder drives daily
priorities. In this example, leadership is about [[data teams]], not one title.

[[person:tammyliang=>Tammy Liang]] shows the first-team version in
[[cite:building-and-scaling-data-team=>Building and Leading Data Teams]].
Her team started by proving the value of business health dashboards and added
data engineering capacity after management trusted the team's impact. The
leadership move isn't a universal hiring sequence. It's deciding when the current
constraint has become a responsibility that needs an owner.

[[person:nicolasrassam=>Nicolas Rassam]] makes the data engineering version
concrete in
[[cite:hiring-for-data-engineering-jobs-in-europe=>Hiring Data Engineers in Europe]].
Titles hide relevant experience, so a
[[data-engineering-manager-role=>data engineering manager]] should name the
missing capability and assign the decision owner. Platform-heavy teams need
storage and orchestration. They also need access, cloud infrastructure,
[[finops-for-data-engineers=>cost]], and standards.

Product-facing teams need domain pipelines, data products, event definitions,
and stakeholder collaboration. The deeper hiring mechanics belong with
[[hiring]] and [[hire-data-engineers=>hiring data engineers]].

## Mentorship and Feedback

Leadership includes creating growth conditions for other people.
[[person:marianosemelman=>Mariano Semelman]]
describes his data science manager work as meetings, mentoring, and coaching.
Planning and people development sit in the same job in
[[cite:data-science-leadership-hiring-mlops=>Data Science Leadership]].

When he took over a team, he used a 30-60-90 plan. He first met
people and listened. Then he learned the projects and domain before giving
feedback
([[cite:data-science-leadership-hiring-mlops@12:52=>Data Science Leadership]],
[[cite:data-science-leadership-hiring-mlops@15:16=>Data Science Leadership]]).

Semelman's feedback practice is careful because manager feedback changes a
person's career. He recommends asking permission, showing care, and offering
options rather than treating managerial opinion as objective truth
([[cite:data-science-leadership-hiring-mlops@44:17=>Data Science Leadership]]).
His one-on-one discussion also frames mistakes as part of a safe learning
environment.

[[person:terezaiofciu=>Tereza Iofciu]] makes the coaching version more
explicit in [[cite:data-leadership-coaching=>Data Leadership Coaching]].
She treats the move from senior IC to lead as a career change, not as a small
extension of technical seniority. A new lead has to learn people problems,
stakeholder framing, feedback, and self-evaluation. The team also has to help
the new lead see how teammates receive leadership behavior
([[cite:data-leadership-coaching@6:17=>Data Leadership Coaching]],
[[cite:data-leadership-coaching@9:15=>Data Leadership Coaching]]).

For leaders, feedback is an accountability practice, not only a relationship
skill. Iofciu recommends training people to give and receive feedback. Even
useful feedback feels uncomfortable. The leader separates critique of work from
critique of the person. That creates enough trust for teammates to surface
problems early
([[cite:data-leadership-coaching@19:43=>Data Leadership Coaching]],
[[cite:data-leadership-coaching@20:18=>Data Leadership Coaching]]).

This connects leadership to [[Team Building]] and the
[[Data Team Lead Role]]. A data lead can't scale by personally solving every
unclear analysis, modeling, or pipeline problem. Iofciu's span-of-control
discussion uses the "pizza" metaphor. A manager may technically supervise more
than seven or eight direct reports, but attention and relationship quality drop.
Data leaders should treat manager bandwidth as a team-design constraint, not as
a heroic time-management problem
([[cite:data-leadership-coaching@12:38=>Data Leadership Coaching]]).

Coaching and mentoring also serve different moments. Iofciu says pure coaching
would use open questions until the person finds their own answer. Data
leadership clients often expect some training, examples, or concrete advice
because they came for data-specific judgment. That puts her practice between
coaching, mentoring, and consultation
([[cite:data-leadership-coaching@34:38=>Data Leadership Coaching]]).

The [[Mentoring in Tech]] page covers longer mentoring relationships. Leaders
choose among reflection, repeated examples from other teams, and direct advice
for a blocked next step.

Rahul Jain adds a useful boundary for leaders who mentor. Mentoring isn't the
same as jumping to an answer. He recommends listening first and probing the
person's context. Leaders should avoid the "advice monster" response where the
senior person immediately prescribes a fix
[[cite:mentoring-in-tech-how-to-find-and-become-a-mentor@30:40=>Mentoring People Skills]].

Managers see this when mentees bring imposter syndrome. They also see it when
someone feels pressure to choose management over technical work. External
perspective also helps when the reporting line shapes the advice
[[cite:mentoring-in-tech-how-to-find-and-become-a-mentor@36:40=>Mentee Challenges]]
[[cite:mentoring-in-tech-how-to-find-and-become-a-mentor@39:50=>External Mentors]].

Jain also separates manager one-on-ones from mentoring. A manager can coach,
while external mentors can give more neutral advice. Leaders shouldn't treat all
growth support as something the reporting manager alone must provide.

[[person:16rahuljain=>Rahul Jain]] adds the data engineering version of this
same coaching work in
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].
The manager creates standards and career paths while leaving room for engineers
to own the work. That keeps mentorship connected to quality, not only to morale.

[[person:leonidkholkine=>Leonid Kholkine]] adds the community-development
example. Conferences expose junior data scientists to speakers and workshops
outside their day job. Cross-domain talks add another growth lever when a team
needs broader perspective. The operating side belongs with
[[data-ai-conference-building=>data AI conference building]]. Organizers decide
speaker selection, pricing, sponsor fit, and practitioner trust for the learning
environment
[[cite:s23e09-starting-data-conference-data-makers-fest-story=>Starting a Data Conference]].

The practical learning path for managers starts with questions, not libraries
or modeling techniques. Managers need to ask better questions about people,
problems, and tradeoffs. [[Data Science for Managers]] belongs near leadership
because managers still need technical literacy. They use it to scope, coach,
and evaluate work rather than to become the strongest individual contributor
again.

Sadat warns new managers who came from deep hands-on work that losing the
dopamine loop of coding is part of the role change. The manager needs new
feedback loops around team momentum, influence, and business value
([[cite:from-software-engineering-to-leading-data-science-teams=>Software Engineer to Data Science Manager]]).

Managers can learn from these examples:

- Sobkowiak for role boundaries and project discovery
- Cohen for team-structure tradeoffs
- Iofciu for influence, feedback, and visibility
- Jain for standards, career paths, and self-motivated teams

([[cite:data-science-manager-vs-expert-hiring-guide=>Data Science Manager vs Expert]],
[[cite:data-science-team-structure-and-org-design=>Designing High-Impact Data Science Teams]],
[[cite:data-leadership-coaching=>Data Leadership Coaching]],
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]).

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
([[cite:data-leadership-coaching@46:00=>Data Leadership Coaching]],
[[cite:data-leadership-coaching@49:20=>Data Leadership Coaching]]). She also argues
that data foundation work, models, and open-source work need visibility because
impact isn't always customer-facing.

Iofciu places foundation work in the same leadership surface. Data leaders have
to make platform, reliability, and product-enablement work visible through KPIs
and stakeholder language. Important data work is often not directly
customer-facing
([[cite:data-leadership-coaching@24:32=>Data Leadership Coaching]]).

That's the practical side of [[Communication]]. Data people often need product
managers, engineers, sales leaders, or executives to change a roadmap. Those
people often don't report to the data team. Iofciu's advice isn't to repeat
the same technical argument louder.

The data leader should learn the other person's work language and listen for
their goals. They should frame the request around what that person already has
to deliver. That makes influencing without authority part of everyday
leadership, not a political exception
([[cite:data-leadership-coaching=>Data Leadership Coaching]]).

Semelman gives the product version of the same practice. He warns that data
scientists can spend time on technically interesting work that doesn't change
user outcomes. He connects product managers and data scientists. He starts
from user impact and spends modeling time where it changes the product or
production test
([[cite:data-science-leadership-hiring-mlops=>Data Science Leadership]]).

This links leadership to
[[MLOps]] because product impact depends on
deployment and testing. It also depends on monitoring and iteration, not only
offline model quality.

[[person:jackblandin=>Jack Blandin]] adds an applied ML
stakeholder lesson in
[[cite:from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership=>From Software Engineer to VP of Machine Learning]].
He describes stakeholder buy-in as something leaders earn through product-level
understanding and trust. Leaders also need to speak in the stakeholder's metrics.

His fast proof-of-concept advice keeps ML leadership honest because teams start
with baselines and demos before larger requests. They then use quick hypothesis
tests before asking for larger engineering investment.

Cohen's team-design episode adds the metrics version of stakeholder work.
Product changes can move more than one metric, so data science leaders need
cross-functional interpretation. Product, engineering, and design partners help
interpret those tradeoffs. Research and leadership partners do too
([[cite:data-science-team-structure-and-org-design=>Designing High-Impact Data Science Teams]]).

Geo's ML product episode adds the platform version. Internal tools still have
users, so leaders need requirements and rollout plans. They also need
observability and release governance. Adoption measures matter more than a list
of impressive capabilities.

For data science and ML projects, useful stakeholder communication usually names:

- the current workflow
- the decision or workflow that should improve
- the baseline and success metric
- the guardrail metric
- the main uncertainty
- the next stakeholder decision

Those checks connect leadership to
[[communication]],
[[metrics]], and
[[experimentation]].

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
([[Data Engineering Platforms]],
[[Data Product Management]]).
That keeps platform investment tied to faster onboarding and safer schema
changes. It also ties work to lower support load, clearer lineage, and fewer
downstream surprises rather than to the appearance of maturity.

## Project and Portfolio Signals

Managers need better project signals than "the model is almost done" or "the
pipeline is in progress." Data and AI work contains discovery risk. Leaders
need to separate exploration, validation, production, and adoption.
[[person:barbarasobkowiak=>Barbara Sobkowiak]] gives
the first filter.

Managers should ask:

- what the stakeholder does today
- what data exists
- what baseline is credible
- what success metric would justify more work

([[cite:data-science-manager-vs-expert-hiring-guide=>Data Science Manager vs Expert]]).

Healthy portfolio signals are practical. The team can explain the baseline and
why a new approach should beat it. Data quality risks are visible before heavy
modeling starts. The project has a decision owner, not only a technical sponsor.

Evaluation metrics connect to business or product outcomes. A path to
deployment, monitoring, support, and adoption exists before the system becomes
business-critical.

Those signals aren't only for data science.
[[person:terezaiofciu=>Tereza Iofciu]] argues in
[[cite:data-leadership-coaching=>Data Leadership Coaching]]
that foundation work needs visibility alongside models and open-source work.
Teams may not see that impact in customer-facing metrics.

[[person:christopherbergh=>Christopher Bergh]] and
[[person:barrmoses=>Barr Moses]] make the same point for
data engineering reliability. Tests and observability are project signals.
Ownership, SLAs, and runbooks also tell stakeholders whether important data can
be trusted after launch
([[cite:dataops-for-data-engineering=>DataOps for Data Engineering]],
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]).

## ML Limits

Good data leadership includes the ability to slow down an ML request.
[[person:barbarasobkowiak=>Barbara Sobkowiak]]
describes stakeholders asking for AI or ML because they expect "magic." Her
response is managerial. Clarify the current workflow and check the data. Compare
against a baseline.

Then decide whether a moving average or rule already solves the problem. A
dashboard or workflow change may be enough too
([[cite:data-science-manager-vs-expert-hiring-guide=>Data Science Manager vs Expert]]).

[[person:valeriybabushkin=>Valerii Babushkin]] makes the
same boundary a system-design habit in
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
Avoiding ML is a valid design outcome when a heuristic, rule, or
existing product behavior is enough.
[[person:benwilson=>Ben Wilson]] adds the production
engineering version in
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]:
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
[[person:geojolly=>Geo Jolly]] puts observability and
release governance inside product leadership for ML systems in
[[cite:ml-product-manager-and-mlops-platform-strategy=>Product Management for Machine Learning]].
Platform adoption belongs there too.
[[person:marianosemelman=>Mariano Semelman]] adds in
[[cite:data-science-leadership-hiring-mlops=>Data Science Leadership]]
that product impact depends on deployment and testing, not only on a promising
notebook.

That literacy means asking:

- who owns input data quality after launch
- who watches prediction quality, drift, and latency
- who responds to failures
- how changes are validated
- what fallback exists when the model is wrong, stale, or unavailable

[[Machine Learning System Design]]
and [[Model Monitoring]] cover the
technical practice in more depth. On this page, the leadership point is
ownership: production ML shouldn't depend on informal heroics or a manager's
hope that "deployment" means "finished."

## Platform Ownership and Scaling

Leadership becomes more architectural when a team scales. [[person:mehdiouazza=>Mehdi OUAZZA]]
describes scale-up pressure in
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].
Companies grow users, products, and teams faster than early data systems can
comfortably support.

His response goes beyond hiring more engineers because he describes
self-service data platforms and onboarding conventions. He also describes
playbooks, Kafka schemas, and data contracts.

Those practices let more teams move without routing every request through the
same data engineers.

Senior leadership shows up as broader impact. People look beyond one team's
backlog, talk with nearby teams, and solve problems that help more than one
group. The platform side belongs with
[[self-service-data-platforms=>self-service data platforms]]
and [[data engineering platforms]].

The team-structure side of scale-ups belongs with [[team building]] and
[[platform adoption]]. That includes senior hiring, onboarding sessions, support
channels, and adoption rituals. On this page, the leadership point is ownership:
a growing team can't depend on one leader micromanaging every project.

## Reliability and DataOps

Reliability is a leadership responsibility because managers set how work is
reviewed, deployed, monitored, and recovered. [[person:christopherbergh=>Christopher Bergh]]
turns this into an operating model in
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

He connects reliable data delivery to automation and observability.
Productivity, version control, and tests are part of the same operating model.
He also emphasizes CI/CD and realistic test data. Deployment confidence is part
of the same discussion.

Weak operating habits create fear and hero-driven recovery, and they also
create turnover and avoidable rework.

[[person:barrmoses=>Barr Moses]] gives the observability
side in
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

She argues that data incidents aren't limited to failed jobs. Teams need
freshness and volume. They also need distribution and schema visibility.
Lineage matters because a pipeline can run and still deliver late, incomplete,
or misleading data. Her later discussion of
RACI-style accountability, SLAs, and runbooks makes ownership visible before
stakeholders discover the problem first.

For data engineering managers, DataOps is therefore not a separate tool list.
It's the management habit of defining review, deployment, observability, and
incident communication. Recovery paths for important datasets and pipelines
belong in the same habit. For the discipline in more depth, use
[[DataOps]]. Here, DataOps is part of
leadership because the team needs explicit standards and owners.

## Strategy and Operating Discipline

At executive scope, leadership turns data work into a strategy that other
leaders can act on. [[person:marcodesa=>Marco De Sa]]
describes the [[chief-data-officer-role=>Chief Data Officer role]] in
[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]]
as data strategy and governance. The role also covers AI direction and team
design. It includes preparation for future products.

He separates strategy from
tactics by breaking a broad direction into goals and KPIs. Teams can then
execute smaller strategy blocks.

De Sa's org-design comments keep strategy grounded in delegation. He says data
leaders need the right teams and people who know the details better than the
executive. The leader then articulates a single vision across those teams. Later, he frames the CDO as closer to executive strategy. The VP
of data is more attached to specific strategy components, though the exact split
depends on the organization.

Leadership in these examples sits inside
[[data strategy]] and
[[data teams]], and it pushes manager
literacy upward into strategy. De Sa works backward from goals, governance,
platforms, and AI investment. Geo does the same at product scope by turning ML
platform work into roadmaps, adoption, and release quality. Sobkowiak does it at
team scope by separating management, expert depth, and project prioritization.
This is also where leadership connects to
[[data-trust-and-strategy=>data trust and strategy]].

Leadership works through visibility, tradeoffs, and ownership. Sobkowiak ties
management to strategy, stakeholder communication, personal development, and
project prioritization. Bauer ties leadership to craft quality and growth in
matrix teams. Semelman ties it to product impact and feedback.

Jain ties leadership to self-organized engineering teams and quality, while
OUAZZA ties it to self-service platforms and senior influence. Liang ties it to
trust, adoption, and ownership. De Sa ties it to organization-wide strategy and
delegation. Together, they make leadership a data and AI delivery practice, not
only a manager title.
