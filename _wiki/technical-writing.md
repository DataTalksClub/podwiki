---
layout: wiki
title: "Technical Writing"
summary: "How DataTalks.Club guests describe technical writing as explanation, documentation, public learning, portfolio proof, and developer education for data and ML work."
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

The strongest writing-specific discussion is
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}).
[Eugene Yan]({{ '/people/eugeneyan/' | relative_url }}) starts from early blog
posts and meetups at 6:00, then frames writing as learning, sharing, and being
useful to future readers at 9:30. At 14:00, he narrows the audience from
"everyone" to a peer, future teammate, or hiring manager. At 16:30, he treats
writing like a product because reader experience determines whether the article
works.

Use this page for technical writing as a
[data science]({{ '/wiki/data-science/' | relative_url }}) and
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) skill. Use
[documentation]({{ '/wiki/documentation/' | relative_url }}) for project docs
and team memory. Use
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) for
adoption and demos. Use
[open source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
for public proof, and [career growth]({{ '/wiki/career-growth/' | relative_url }})
for visibility and seniority signals.

## Reader-Centered Explanation

Technical writing in these episodes is defined less by format than by reader
need. A strong article helps someone solve a problem. It may also help them
understand a tradeoff or decide what to try next. Structure and examples make
the explanation usable rather than merely polished. Code, screenshots, and
diagrams can add the context a reader needs.

[Angelica Lo Duca]({{ '/people/angelicaloduca/' | relative_url }}) makes that
boundary explicit in
[Practical Data Journalism]({{ '/podcasts/data-journalism-python-visualization-storytelling/' | relative_url }}).
At 7:43 and 8:01, she defines data journalism as data-driven news and
general-audience storytelling. At 24:35, she separates technical writing as a
how-to form built around clarity and audience. At 40:47, she structures
articles around the problem, the solution, and the result. She adds code
repositories when the reader needs to reproduce the work.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) applies
the same reader-first standard to tutorials in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
At 43:14, he starts tutorial design with audience and goals. Technical writing
therefore sits beside [communication]({{ '/wiki/communication/' | relative_url }})
and [developer experience]({{ '/wiki/developer-experience/' | relative_url }}).
The writer has to know what the reader is trying to accomplish before deciding
how much setup belongs in the piece. Code, context, and conceptual explanation
depend on that reader.

## Audience, Outline, and Cadence

Eugene gives the clearest reusable writing workflow in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}).
At 20:00, he describes a weekly cadence. At 25:00, he starts with an outline so
ideas can be selected, ordered, and tested before drafting. At 29:00, he talks
about time budget and avoiding endless editing. At 33:00, he discusses idea
sources and topic prioritization, while 37:00 covers titles and article length.

The method matters for technical topics because the audience determines the
level of detail. A
[data scientist]({{ '/wiki/data-scientist-role/' | relative_url }}) may need
dataset assumptions, baselines, evaluation, and code. A platform engineer may
need interfaces, failure modes, and operational notes. A hiring manager may care
more about scope, tradeoffs, ownership, and impact.

Eugene's 14:00 audience chapter is therefore a writing rule and a career rule.
A technical article gives stronger evidence when the reader can see the choice
it supports.

Eugene treats consistency as a craft habit and, at 41:00, argues for starting
despite friction. At 43:30, he compares blogging platforms. His examples include
Medium, Substack, WordPress, and Jekyll on GitHub Pages. At 46:00, he describes
morning writing reps and weekend deep work. At 48:30, he discusses distribution
through Twitter and LinkedIn, which makes writing part of
[career growth]({{ '/wiki/career-growth/' | relative_url }}) without reducing it
to personal branding.

## Technical Writing for Data and ML

Data and ML writing needs enough technical detail for the reader to judge the
work. That usually means naming the dataset, problem, method, and evaluation.
The writer should also show the code path, assumptions, and failure modes. A
reader should be able to tell whether the article is about exploration or a
model. They should also see when it's about a pipeline, production system, or
business decision.

At 56:30 in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
Eugene turns the guidance toward portfolios. He recommends a README and
quickstart, plus a repo tour. Those artifacts should let
another person understand the project without private context. The same guidance
also fits [portfolio projects]({{ '/wiki/portfolio-projects/' | relative_url }}).
It appears again in
[machine learning portfolio projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
and [open source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).

A polished article with no technical choices is weak evidence. A plain README
can be stronger when it names the problem, shows the run path, and explains
tradeoffs.

Tool education has the same requirement. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
[Will Russell]({{ '/people/willrussell/' | relative_url }}) describes Learn with
Kestra at 57:22. His examples include Docker, Postgres, and Git. A reader often
needs the surrounding setup as much as the main product.

## Documentation and Team Memory

Technical writing also lives inside teams. In Eugene's episode, the 51:00
chapter covers writing at work through press releases, working-backwards
documents, and design docs. The 54:00 chapter discusses decision logs,
rationales, and team memory. That makes writing part of
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
not only a public-content habit.

Internal writing solves a different problem from blog posts. A design doc helps
reviewers understand the proposed choice before the team commits. A decision log
preserves why the team chose one option over another. A runbook or README helps
someone operate or reproduce the project later. These documents matter in data
work because pipelines, models, dashboards, and metrics often outlive the person
who first built them.

The open-source documentation checklist from
[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) maps well
to internal projects too. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
the 22:20 chapter names README material and guides. It also names API reference
and examples.
For an internal [machine learning]({{ '/wiki/machine-learning/' | relative_url }})
or data platform, the same structure helps a teammate move from "what's this?"
to "how do I use it safely?"

## Public Learning and Career Proof

Public writing can make career growth visible, but guests don't reduce it to
personal branding. Eugene's 9:30 chapter connects writing to learning and
sharing. The 56:30 chapter covers portfolio READMEs, quickstarts, and repo
tours. A hiring reader can use that material to judge clarity, scope, and
ownership.

Technical writing belongs with
[career growth]({{ '/wiki/career-growth/' | relative_url }}) and
[communication]({{ '/wiki/communication/' | relative_url }}) because a post
about a pipeline or model evaluation is stronger when it shows the problem. It
should also show the tradeoffs. The same is true for a tool integration that
shows the code path and result. A polished article with no technical choices
gives less evidence than a plain README that lets someone run the project.

Vincent makes public proof concrete in two open-source episodes. In
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
the 23:29 chapter discusses open-source work as a hiring signal. At 27:24, he
connects video production with communication practice. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
the 34:00 chapter links talks and blogs to career growth. He also names meetups
and open-source visibility.

## Tutorials, Demos, and DevRel

Technical writing overlaps with DevRel, open source, and marketing because all
three use public explanation. A useful piece should still help the reader
succeed technically. In
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
Hugo names technical fluency, writing, and community building as core
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) skills
at 31:41. At 37:21, he discusses writing improvement through practice,
collaboration, and editorial feedback.

At 46:09 and 48:43, he discusses writing goals and media choices. A blog post,
talk, video, or conference session can all work when the format matches the goal
and audience.

Will's demo-first episode shows the same boundary from practice. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
the 49:14 chapter ties developer advocacy to documentation, demos, and outreach.
At 51:49, he describes a flow that starts with bullet points and demos. Writers
then help turn the material into public teaching.

At 53:40, he explains video strategy through a defined goal and useful pacing.
He also recommends complete walkthroughs. At 54:30, he uses a
workflow-notification demo to show how a tutorial can teach a specific product
behavior.

## Open-Source Contribution Writing

Open-source writing adds maintainer trust. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
Vincent treats documentation as part of
[open source]({{ '/wiki/open-source/' | relative_url }}) stewardship. At 22:20,
he covers README material and guides. He also covers API reference and examples.

At 24:10, he covers contribution guides and respectful interaction. At 25:50, he
treats a clear reproducible issue as a valuable first contribution.
At 27:40, he adds tests and packaging, plus CI and pre-commit hooks.

The open-source version of technical writing isn't limited to docs pages. It
includes issue reports and contribution guides. It also includes examples, API
reference, and project tours that let users and maintainers trust the work.
Technical writing
overlaps with
[open source and developer relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
when adoption depends on examples, clear setup, and a contribution path that
respects maintainer time.
