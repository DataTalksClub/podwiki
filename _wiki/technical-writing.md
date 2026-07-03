---
layout: wiki
title: "Technical Writing"
summary: "How DataTalks.Club guests connect technical writing with documentation, public learning, portfolios, and developer education."
related:
  - Developer Relations
  - Career Growth
  - Communication
  - Open Source and Developer Relations
  - Open Source Portfolio Evidence
  - Data Science
  - Machine Learning
---

## Definition and Scope

Technical writing explains technical work so another person can use it,
evaluate it, reproduce it, or extend it. In the DataTalks.Club podcast, writing
appears in public posts and tutorials. It also appears in READMEs, design docs,
and decision logs. Demo scripts, conference proposals, and teaching material use
the same skill.

Across those forms, the writer serves a concrete reader. The reader may need to
understand the work or run the project. They may also need to review a decision
or continue independently.

The strongest writing-specific discussion starts from early blog posts and
meetups and frames writing as learning, sharing, and being useful to future
readers. It narrows the audience from "everyone" to a peer, future teammate, or
hiring manager. It also treats writing like a product because reader experience
determines whether an article works
([[person:eugeneyan|Eugene Yan]],
[[podcast:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]]).

Use this page for technical writing as a
[[data science]] and
[[machine learning]] skill. Use
[[documentation]] for project docs
and team memory. Use
[[developer relations]] for
adoption and demos. Use
[[open source portfolio evidence]]
for public proof, and [[career growth]]
for visibility and seniority signals.

## Reader-Centered Explanation

Technical writing in these episodes is defined less by format than by reader
need. A strong article helps someone solve a problem. It may also help them
understand a tradeoff or decide what to try next. Structure and examples make
the explanation usable rather than merely polished. Code, screenshots, and
diagrams can add the context a reader needs.

Data journalism is data-driven news and general-audience storytelling, while
technical writing is a how-to form built around clarity and audience. A how-to
article is structured around the problem, solution, and result. It adds code
repositories when the reader needs to reproduce the work
([[person:angelicaloduca|Angelica Lo Duca]],
[[podcast:data-journalism-python-visualization-storytelling=>Practical Data Journalism]]).

The same reader-first standard applies to tutorials: tutorial design starts
with audience and goals
([[person:hugobowneanderson|Hugo Bowne-Anderson]],
[[podcast:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).
Technical writing therefore sits beside [[communication]]
and [[developer experience]].
The writer has to know what the reader is trying to accomplish before deciding
how much setup belongs in the piece. Code, context, and conceptual explanation
depend on that reader.

## Audience, Outline, and Cadence

The clearest reusable writing workflow uses a weekly cadence and starts with an
outline so ideas can be selected, ordered, and tested before drafting. It sets
a time budget to avoid endless editing and covers idea sources, topic
prioritization, titles, and article length
([[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]).

The method matters for technical topics because the audience determines the
level of detail. A
[[data-scientist-role=>data scientist]] may need
dataset assumptions, baselines, evaluation, and code. A platform engineer may
need interfaces, failure modes, and operational notes. A hiring manager may care
more about scope, tradeoffs, ownership, and impact.

Choosing the audience is therefore both a writing rule and a career rule. A
technical article gives stronger evidence when the reader can see the choice it
supports.

Consistency is a craft habit, and starting despite friction matters. Blogging
platforms include Medium, Substack, WordPress, and Jekyll on GitHub Pages. A
routine can mix morning writing reps with weekend deep work. Distribution
through Twitter and LinkedIn makes writing part of
[[career growth]] without reducing it
to personal branding
([[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]).

Using AI to draft can lower the cost of turning rough notes into a post, but it
doesn't remove the writer's voice problem. The bounded uses are sentence
rewrites, structure from dumped notes, and drafts from bullet points. The author
still edits the result back into their style. For free drafting, a plain editor
can be better than autocomplete when the writer needs imperfect but intentional
text
[[cite:production-ready-ai-engineering|AI-assisted writing|56:17]].

## Technical Writing for Data and ML

Data and ML writing needs enough technical detail for the reader to judge the
work. That usually means naming the dataset, problem, method, and evaluation.
The writer should also show the code path, assumptions, and failure modes. A
reader should be able to tell whether the article is about exploration or a
model. They should also see when it's about a pipeline, production system, or
business decision.

For portfolios, the guidance recommends a README, a quickstart, and a repo tour.
Together they help another person understand the project without private context
([[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]).
The same guidance fits [[portfolio projects]],
and appears again in
[[machine learning portfolio projects]]
and [[open source portfolio evidence]].

A polished article with no technical choices is weak evidence. A plain README
can be stronger when it names the problem, shows the run path, and explains
tradeoffs.

Tool education has the same requirement. Learn with Kestra draws on examples
like Docker, Postgres, and Git. A reader often needs the surrounding setup as
much as the main product
([[person:willrussell|Will Russell]],
[[podcast:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]]).

## Books and Public Drafts

Machine learning books can use public writing as a staged release process, not
only as a finished artifact. A chapter-by-chapter website makes a book feel
closer to a sequence of articles. It also gives readers a way to react early.
For Interpretable Machine Learning, that feedback helped the project keep
moving instead of becoming a private, unfinished draft
[[cite:interpretable-machine-learning|Interpretable ML writing workflow|15:55]].

Self-publishing shifts deadlines, distribution, and audience trust from the
publisher to the author. The full-time path is strongest when it grows out of
prior writing and book income. It also depends on an existing reader base.
Revenue can arrive months later, so a sudden job quit is risky
[[cite:interpretable-machine-learning|Full-time technical author path|3:45]]
[[cite:interpretable-machine-learning|Self-publishing tradeoffs|17:07]]
[[cite:interpretable-machine-learning|Full-time author economics|50:00]].

Feedback loops scale better when they stay reader-centered and phased. Open
drafts and newsletter-sourced test readers support early review. Small
beta-reader batches let the author incorporate feedback into a new version
before inviting the next group. Conflicting reader comments still require an
editorial decision
[[cite:interpretable-machine-learning|Beta-reader feedback loops|44:51]].

Book projects can also start from publishing constraints. Traditional publishers
add editorial support and accountability, and they create a more intentional
production path. Self-publishing fits existing work that can become an
"accidental product"
[[cite:solopreneur-developer-and-data-professional|Publishing options|35:44]].

A project-first workflow starts with an outline. The author then builds chapter
projects, often in GitHub, and turns those projects and prior documentation
into explanation
[[cite:solopreneur-developer-and-data-professional|Book workflow|38:08]].

The marathon analogy frames the work as repeated training. Book writing gets
less intimidating when the author treats the process as discipline and feedback
[[cite:solopreneur-developer-and-data-professional|Book discipline|41:34]].

## Documentation and Team Memory

Inside teams, technical writing spans press releases and working-backwards
documents. It also spans design docs, decision logs, rationales, and team
memory. That makes it part of [[software engineering]], not only a public-content
habit
([[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]).

Internal writing solves a different problem from blog posts. A design doc helps
reviewers understand the proposed choice before the team commits. A decision log
preserves why the team chose one option over another. A runbook or README helps
someone operate or reproduce the project later. These documents matter in data
work because pipelines, models, dashboards, and metrics often outlive the person
who first built them.

An open-source documentation checklist maps well to internal projects too,
naming README material and guides. It also covers API reference and examples
([[person:vincentwarmerdam|Vincent Warmerdam]],
[[podcast:open-source-ml-contributions=>Contribute to Open Source ML]]).
For an internal [[machine learning]]
or data platform, the same structure helps a teammate move from "what's this?"
to "how do I use it safely?"

## Public Learning and Career Proof

Public writing can make career growth visible without reducing it to personal
branding. Portfolio READMEs, quickstarts, and repo tours turn public learning
into evidence. They also make sharing concrete for a hiring reader judging
clarity, scope, and ownership
([[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]).

Technical writing belongs with
[[career growth]] and
[[communication]] because a post
about a pipeline or model evaluation is stronger when it shows the problem. It
should also show the tradeoffs. The same is true for a tool integration that
shows the code path and result. A polished article with no technical choices
gives less evidence than a plain README that lets someone run the project.

Public proof is concrete across two open-source episodes. Open-source work is a
hiring signal, and video production doubles as communication practice
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]).
Talks, blogs, meetups, and open-source visibility all link to career growth
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

## Tutorials, Demos, and DevRel

Technical writing overlaps with DevRel, open source, and marketing because all
three use public explanation. A useful piece should still help the reader
succeed technically. Technical fluency, writing, and community building are core
[[developer relations]] skills. Writing improves through practice,
collaboration, and editorial feedback
([[person:hugobowneanderson|Hugo Bowne-Anderson]],
[[podcast:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

Writing goals and media choices come next. A blog post, talk, video, or
conference session can work when the format matches the goal and audience
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).

A demo-first practice shows the same boundary because developer advocacy ties to
documentation, demos, and outreach. A flow that starts with bullet points and
demos lets writers turn the material into public teaching
([[person:willrussell|Will Russell]],
[[podcast:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]]).

Video strategy needs a defined goal, useful pacing, and complete walkthroughs. A
workflow-notification demo shows how a tutorial can teach a specific product
behavior
([[podcast:practical-devrel-demofirst-education-and-open-source|Developer Advocacy Through Community Impact]]).

## Open-Source Contribution Writing

Open-source writing adds maintainer trust by treating documentation as part of
[[open source]] stewardship. That work includes README material, guides, API
reference, and examples
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

Contribution guides and respectful interaction matter because a clear
reproducible issue is a valuable first contribution. Tests, packaging, CI, and
pre-commit hooks round out the work
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

The open-source version of technical writing isn't limited to docs pages. It
includes issue reports and contribution guides. It also includes examples, API
reference, and project tours that let users and maintainers trust the work.
Technical writing
overlaps with
[[open source and developer relations]]
when adoption depends on examples, clear setup, and a contribution path that
respects maintainer time.
