---
layout: wiki
title: "Technical Writing"
summary: "Technical writing across documentation, public learning, portfolios, and developer education."
related:
  - Developer Relations
  - Career Growth
  - Communication
  - Open Source and Developer Relations
  - Open Source Portfolio Evidence
  - Data Science
  - Machine Learning
---

## Technical Writing Scope

Technical writing explains technical work so another person can use it,
evaluate it, reproduce it, or extend it. In the DataTalks.Club podcast, writing
appears in public posts and tutorials. It also appears in READMEs, design docs,
and decision logs. Demo scripts, conference proposals, and teaching material use
the same skill.

Across those forms, the writer serves a concrete reader. The reader may need to
understand the work or run the project. They may also need to review a decision
or continue independently.

Eugene Yan starts from early blog posts and meetups. He frames writing as
learning, sharing, and being useful to future readers. Writing gets stronger
when the audience narrows from "everyone" to a
peer, future teammate, or hiring manager. Reader experience determines whether
an article works.[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]]
Writing also exposes gaps in the writer's own understanding. Teaching through
public explanation becomes a learning loop
[[cite:technical-writing-for-data-scientists@09:30=>Writing to learn]].

As a [[data science]] and [[machine learning]] skill, technical writing sits
between [[documentation]], [[developer relations]], and
[[open source portfolio evidence]]. Project docs preserve team memory. Demos and
adoption writing make tools easier to try. Public proof and
[[career growth]] come from making technical decisions visible.

## Reader-Centered Explanation

Technical writing in these episodes is defined less by format than by reader
need. A strong article helps someone solve a problem. It may also help them
understand a tradeoff or decide what to try next. Structure and examples make
the explanation usable rather than merely polished. Code, screenshots, and
diagrams can add the context a reader needs.

Data journalism is data-driven news and general-audience storytelling, while
technical writing is a how-to form built around clarity and audience. A how-to
article is structured around the problem, solution, and result. It adds code
repositories when the reader needs to reproduce the work.[[cite:data-journalism-python-visualization-storytelling=>Practical Data Journalism]]

Tutorial design also starts with audience and goals.[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]
Technical writing therefore sits beside [[communication]]
and [[developer experience]].
The writer has to know what the reader is trying to accomplish before deciding
how much setup belongs in the piece. Code, context, and conceptual explanation
depend on that reader.

## Boundary Differences

A data-journalism story, a DevRel tutorial, and a portfolio README each serve a
different reader decision. Data journalism aims at public stories from data.
DevRel writing aims at tutorials and demos that help developers adopt a tool.
Portfolio writing aims at evidence a reviewer can look at. All three require
explanation, but the success criteria differ by audience and
decision.[[cite:data-journalism-python-visualization-storytelling=>Practical Data Journalism]]
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]]

Public drafts and self-publishing can create early reader feedback, while
traditional publishing adds editorial support and accountability. The right path
depends on whether the writer already has readers, income, and a draft that can
become a product.[[cite:interpretable-machine-learning@17:07=>Interpretable Machine Learning]]
[[cite:solopreneur-developer-and-data-professional=>Solopreneur Guide]]

## Audience, Outline, and Cadence

Writers can use a weekly cadence and start with an outline. They can select and
order ideas before drafting, then test whether the outline works by rewriting
it from memory. They set a time budget to avoid endless editing. They also
cover idea sources, topic prioritization, titles, and article length
[[cite:technical-writing-for-data-scientists@20:00=>Weekly writing cadence]]
[[cite:technical-writing-for-data-scientists@25:00=>Outline-first writing]]
[[cite:technical-writing-for-data-scientists@29:00=>Writing time budget]].

The method matters for technical topics because the audience determines the
level of detail. A
[[data-scientist-role=>data scientist]] may need
dataset assumptions, baselines, evaluation, and code. A platform engineer may
need interfaces, failure modes, and operational notes. A hiring manager may care
more about scope, tradeoffs, ownership, and impact.

Choosing the audience is therefore both a writing rule and a career rule. A
technical article gives stronger evidence when the reader can see the choice it
supports.

Consistency is a craft habit, but writers still need to start despite friction.
Writers can use hosted platforms such as Medium and Substack. They can also use
WordPress or Jekyll on GitHub Pages. Writers can mix morning writing reps with
weekend deep work. When they distribute through Twitter and LinkedIn, writing
becomes part of [[career growth]] without reducing it to personal branding
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].

Swyx adds the owned-platform version. A mailing list, newsletter, and personal
site give public learning a durable home outside a single social feed
[[cite:developer-personal-brand-learn-in-public@25:54=>Learn in Public]].

Jose Maria Sanchez Salas gives the data-engineering version. His newsletter
aims to explain how non-technical readers can get value from data. He treats
daily repetition as a way to build confidence and opportunity signals for remote
work
[[cite:remote-data-engineering-work-and-building-iot-platforms@32:17=>Data newsletter]]
[[cite:remote-data-engineering-work-and-building-iot-platforms@38:10=>Newsletter as opportunity signal]].

That ownership changes the role of technical writing. Social posts can help a
piece find readers, but the durable asset is the body of work a writer controls.
A writer controls the domain, newsletter, and mailing list. Reusable posts become
part of the same distribution decision
[[cite:developer-personal-brand-learn-in-public@25:54=>Learn in Public]].

Using AI to draft can lower the cost of turning rough notes into a post, but it
doesn't remove the writer's voice problem. The bounded uses are sentence
rewrites, structure from dumped notes, and drafts from bullet points. The author
still edits the result back into their style. For free drafting, a plain editor
can be better than autocomplete when the writer needs imperfect but intentional
text
[[cite:production-ready-ai-engineering@56:17=>Production AI Engineering]].

That boundary also makes technical writing part of
[[ai-tools-for-personal-productivity=>AI tools for personal productivity]].
Use the assistant for drafts and rewrites, then keep human review on voice,
argument, and evidence.
For consultants, that makes AI a drafting aid rather than a substitute for the
discoverable expertise that writing is supposed to prove.

## Technical Writing for Data and ML

Data and ML writing needs enough technical detail for the reader to judge the
work. That usually means naming the dataset, problem, method, and evaluation.
The writer should also show the code path, assumptions, and failure modes. A
reader should be able to tell whether the article is about exploration or a
model. They should also see when it's about a pipeline, production system, or
business decision.

Portfolio projects need a README plus a quickstart and repo tour. Together,
these help another person understand the project without private context
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].
Use the same README, quickstart, and repo-tour standard for
[[portfolio projects]] and
[[competitions-beyond-kaggle=>competition writeups]]
[[cite:s24e01-competitions-beyond-kaggle-leaderboard=>Competitions Beyond the Kaggle Leaderboard]].
For role-specific versions, see [[machine learning portfolio projects]] and
[[open source portfolio evidence]].

A polished article with no technical choices is weak evidence. A plain README
can be stronger when it names the problem, shows the run path, and explains
tradeoffs.

Executive-facing technical writing has a different structure. Ben Taylor
recommends putting the recommendation first, then keeping the evidence and appendix ready
for questions. That makes the written artifact useful for decision makers while
still preserving the technical backing for reviewers
[[cite:public-speaking-for-data-scientists@39:55=>Executive presentations]].

Tool education needs the same reader context. Learn with Kestra draws on
examples like Docker, Postgres, and Git. A reader often needs the surrounding
setup as much as the main product
[[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]].

## Books and Public Drafts

Machine learning books can use public writing as a staged release process, not
only as a finished artifact. A chapter-by-chapter website makes a book feel
closer to a sequence of articles. It also gives readers a way to react early.
For Interpretable Machine Learning, that feedback helped the project keep
moving instead of becoming a private, unfinished draft
[[cite:interpretable-machine-learning@15:55=>Interpretable Machine Learning]].

Self-publishing shifts deadlines, distribution, and audience trust from the
publisher to the author. The full-time path is strongest when it grows out of
prior writing and book income. Christoph Molnar's path makes the author role a
technical career, not a side note. The book, site, newsletter, and reader
feedback become the work.

It also depends on an existing reader base. Revenue can arrive months later, so
a sudden job quit is risky
[[cite:interpretable-machine-learning@03:45=>Interpretable Machine Learning]]
[[cite:interpretable-machine-learning@17:07=>Interpretable Machine Learning]]
[[cite:interpretable-machine-learning@50:00=>Interpretable Machine Learning]].

Feedback loops scale better when they stay reader-centered and phased. Open
drafts and newsletter-sourced test readers support early review. Small
beta-reader batches let the author incorporate feedback into a new version
before inviting the next group. Conflicting reader comments still require an
editorial decision
[[cite:interpretable-machine-learning@44:51=>Interpretable Machine Learning]].

Book projects can also start from publishing constraints. Traditional publishers
add editorial support and accountability, and they create a more intentional
production path. Self-publishing fits existing work that can become an
"accidental product"
[[cite:solopreneur-developer-and-data-professional@35:44=>Solopreneur Guide]].

A project-first workflow starts with an outline. The author then builds chapter
projects, often in GitHub, and turns those projects and prior documentation
into explanation
[[cite:solopreneur-developer-and-data-professional@38:08=>Solopreneur Guide]].

The marathon analogy frames the work as repeated training. Book writing gets
less intimidating when the author treats the process as discipline and feedback
[[cite:solopreneur-developer-and-data-professional@41:34=>Solopreneur Guide]].

## Documentation and Team Memory

Inside teams, technical writing spans press releases and working-backwards
documents. It also spans design docs, decision logs, rationales, and team
memory. That makes it part of [[software engineering]], not only a public-content
habit
[[cite:technical-writing-for-data-scientists@51:00=>Writing at work]]
[[cite:technical-writing-for-data-scientists@54:00=>Decision logs and team memory]].

Internal writing solves a different problem from blog posts. A design doc helps
reviewers understand the proposed choice before the team commits. A decision log
preserves why the team chose one option over another. A runbook or README helps
someone operate or reproduce the project later. These documents matter in data
work because pipelines, models, dashboards, and metrics often outlive the person
who first built them.

Internal projects can borrow open-source documentation checklists. README
material, guides, API reference, and examples all transfer to internal work
[[cite:open-source-ml-contributions@22:20=>Contribute to Open Source ML]].

For an internal [[machine learning]]
or data platform, the same structure helps a teammate move from "what's this?"
to "how do I use it safely?"
It also helps reviewers separate explanation gaps from code gaps. A missing
guide, unclear API reference, or absent example can block review even when the
implementation works.

## Public Learning and Career Proof

Public writing can make career growth visible without reducing it to personal
branding. Portfolio READMEs, quickstarts, and repo tours turn public learning
into evidence. They also make sharing concrete for a hiring reader judging
clarity, scope, and ownership
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].

Writing can also become business infrastructure. Bartosz Mikulski describes a
blog that began as a place to share programming ideas and later helped attract
clients and support teaching workshops. The useful claim isn't that every blog
becomes a sales funnel. It's that a searchable body of technical explanations
can make expertise easier for clients, students, and collaborators to verify
[[cite:production-ready-ai-engineering@53:10=>Production AI Engineering]].

Technical writing belongs with
[[career growth]] and
[[communication]] because a post
about a pipeline or model evaluation is stronger when it shows the problem. It
should also show the tradeoffs. The same is true for a
[[data-engineering=>data engineering]] system or tool integration that shows the
code path and result. A polished article with no technical choices gives less
evidence than a plain README that lets someone run the project.

Open-source work can become a hiring signal, and video production doubles as
communication practice
[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].
Talks, blogs, meetups, and open-source visibility all link to career growth
[[cite:open-source-ml-contributions=>Contribute to Open Source ML]].

## Tutorials, Demos, and DevRel

Technical writing overlaps with DevRel, open source, and marketing because all
three use public explanation. A useful piece should still help the reader
succeed technically. Technical fluency, writing, and community building are core
[[developer relations]] skills. Writing improves through practice,
collaboration, and editorial feedback
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

A blog post, talk, video, or conference session can work when the format matches
the goal and audience
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

A demo-first practice shows the same boundary because developer advocacy ties to
documentation, demos, and outreach. A flow that starts with bullet points and
demos lets writers turn the material into public teaching
[[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]].

Video strategy needs a defined goal, useful pacing, and complete walkthroughs. A
workflow-notification demo shows how a tutorial can teach a specific product
behavior
[[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]].

## Open-Source Contribution Writing

Open-source writing adds maintainer trust by treating documentation as part of
[[open source]] stewardship. That work includes README material, guides, API
reference, and examples
[[cite:open-source-ml-contributions@22:20=>Contribute to Open Source ML]].

Contribution guides and respectful interaction matter because a clear
reproducible issue is a valuable first contribution. Tests, packaging, CI, and
pre-commit hooks round out the work
[[cite:open-source-ml-contributions=>Contribute to Open Source ML]].

The open-source version of technical writing isn't limited to docs pages. It
includes issue reports and contribution guides. It also includes examples, API
reference, and project tours that let users and maintainers trust the work.
Technical writing
overlaps with
[[open source and developer relations]]
when adoption depends on examples, clear setup, and a contribution path that
respects maintainer time.
