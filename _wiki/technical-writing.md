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

Technical writing explains technical work so another person can use it. A good
technical write-up helps someone understand and evaluate the work. It also
helps them reproduce or extend it.

In DataTalks.Club episodes, people use writing in blog posts and tutorials.
They use it in READMEs and design docs. They also use it in decision logs, demo
scripts, conference proposals, and teaching material.

The strongest writing-specific episode is
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
where [Eugene Yan]({{ '/people/eugeneyan/' | relative_url }}) describes writing
as a way to learn and share. He also frames it as help for future readers.

At 9:30, he talks about writing motivations. At 14:00, he shifts from writing
for everyone to writing for a specific reader. That reader may be a peer,
future teammate, or hiring manager. At 16:30, he treats writing like a product
because the reader's experience matters.

Read this page for writing as a data and ML skill. Use
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) for
tool adoption, demos, and community feedback. Use
[open source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
for public project proof, and [career growth]({{ '/wiki/career-growth/' | relative_url }})
for promotion, visibility, and seniority signals.

## Common Definition

Podcast guests define technical writing through the reader's job. A technical
article should help someone solve a problem, understand a tradeoff, or decide
what to try next. It isn't only polished explanation. The writer also needs
structure and examples. Code, screenshots, diagrams, and context help another
person follow the work.

Eugene gives the clearest writing routine in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
the 20:00 chapter covers a weekly writing cadence. The 25:00 chapter covers an
outline-first method. The 29:00 chapter discusses time budget and avoiding
endless editing. This advice connects directly to
[data science]({{ '/wiki/data-science/' | relative_url }}) and
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) because
technical readers need problem setup and method. They also need the result and
the limitation, not only a generic story about tools.

[Angelica Lo Duca]({{ '/people/angelicaloduca/' | relative_url }}) makes the
same boundary explicit in
[Practical Data Journalism]({{ '/podcasts/data-journalism-python-visualization-storytelling/' | relative_url }}).
At 24:35, she defines technical writing through how-to guides and clarity. She
also puts audience focus at the center. At 40:47, she describes an article
structure based on problem, solution, and result. She adds code repositories
when the reader needs to reproduce the work.

## Guest Differences

Guests agree that writing should help a reader, but each guest puts the work in
a different context.

Eugene focuses on individual writing practice and career use. In the 6:00
chapter of
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
he starts from early blog posts and meetups. At 41:00, he argues for starting
despite friction. At 48:30, he discusses distribution through Twitter and
LinkedIn. He also treats consistency as part of the practice.

His version of technical writing is partly a learning practice and partly a
public record of judgment.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) places
writing inside [developer relations]({{ '/wiki/developer-relations/' | relative_url }}).
In
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
the 31:41 chapter names technical fluency, writing, and community building as
core DevRel skills. At 37:21, he discusses writing improvement through practice,
collaboration, and editorial feedback. At 43:14, he puts audience and goals at
the center of tutorial design. He also uses structural outlines before drafting.

[Will Russell]({{ '/people/willrussell/' | relative_url }}) pushes writing
toward demos and video. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
the 49:14 chapter ties developer advocacy to documentation, demos, and outreach.
At 51:49, he describes a content flow that starts with bullet points and demos,
then uses collaboration with writers. At 53:40, he explains video strategy
through a defined goal and useful pacing. He also recommends complete
walkthroughs.

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) brings in
open-source stewardship. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
the 22:20 chapter covers a documentation checklist with README and guides. It
also includes API reference and examples. At 25:50, he treats a clear
reproducible issue as a valuable first contribution.

His version of writing sits inside
[open source]({{ '/wiki/open-source/' | relative_url }}) because clear writing
helps make a project usable.

## Technical Writing for Data and ML

Data and ML writing needs enough technical detail for the reader to judge the
work. That usually means naming the dataset, problem, method, and evaluation.
The writer should also show the code path, assumptions, and failure modes. A
reader should be able to tell whether the article is about exploration or a
model. They should also see when it's about a pipeline, production system, or
business decision.

Eugene's 14:00 discussion of audience targeting matters because a data scientist
and a platform engineer need different levels of setup. A hiring manager may
need the decision and impact. A future teammate may need tradeoffs, interfaces,
and operational notes. A writer can fail by giving a manager too much
implementation detail. They can also fail by giving an engineer too little
reproducibility.

Angelica's distinction between data journalism and technical writing keeps the
definition precise. In
[Practical Data Journalism]({{ '/podcasts/data-journalism-python-visualization-storytelling/' | relative_url }}),
the 7:43 and 8:01 chapters define data journalism through data-driven news and
general-audience storytelling. At 24:35, she separates technical writing as a
how-to form. Technical writing can still use narrative, but the reader expects a
usable explanation of how to solve the problem.

DevRel episodes make the same requirement visible. Hugo's 43:14 chapter asks
the writer to choose the audience and goal before drafting a tutorial. Will's
57:22 chapter on Learn with Kestra shows why data and ML writing often has to
teach surrounding tools. Docker, Postgres, and Git may matter as much as the
main product.

## Documentation and Team Memory

Technical writing also lives inside teams. In Eugene's episode, the 51:00
chapter covers writing at work through press releases, working-backwards
documents, and design docs. The 54:00 chapter discusses decision logs,
rationales, and team memory. That makes writing part of
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
not only a public-content habit.

Internal writing solves a different problem from blog posts. A design doc helps
reviewers understand the proposed choice before the team commits. A decision
log preserves why the team chose one option over another. A runbook or README
helps someone operate or reproduce the project later. These documents matter in
data work because pipelines, models, dashboards, and metrics often outlive the
person who first built them.

Vincent's open-source documentation checklist maps well to internal projects
too. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
the 22:20 chapter names README and guides. It also names API reference and
examples. For an internal ML or data platform, the same structure helps a
teammate move from "what's this?" to "how do I use it safely?"

## Public Learning and Career Proof

Public writing can make career growth visible, but guests don't reduce it to
personal branding. Eugene's 9:30 chapter connects writing to learning and
sharing. The 56:30 chapter covers portfolio READMEs, quick starts, and repo
tours. A hiring reader can use that material to judge clarity, scope, and
ownership.

This is why technical writing belongs with
[career growth]({{ '/wiki/career-growth/' | relative_url }}) and
[communication]({{ '/wiki/communication/' | relative_url }}). A post about a
pipeline or model evaluation is stronger when it shows the problem and
tradeoffs. The same is true for a tool integration that shows the code path and
result. A polished article with no technical choices gives less evidence than a
plain README that lets someone run the project.

Vincent makes public proof concrete in two open-source episodes. In
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
the 23:29 chapter discusses open-source work as a hiring signal. At 27:24, he
connects video production with communication practice. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
the 34:00 chapter links talks and blogs to career growth. He also names meetups
and open-source visibility.

## Open Source and DevRel Boundaries

Technical writing overlaps with DevRel, open source, and marketing because all
three use public explanation. A useful piece should still help the reader
succeed technically. In
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
Hugo discusses writing goals at 46:09 and media choices at 48:43. A blog post,
talk, video, or conference session can all work when the format matches the
goal and audience.

Will's demo-first episode shows the same boundary from practice because, at
49:14, documentation and demos sit next to outreach. At 54:30, he uses a specific
workflow notification demo, and at 57:22, his tutorial series teaches the
surrounding developer tools needed to use Kestra. Writing succeeds when the
reader or viewer can do the work afterward.

Open-source writing adds maintainer trust. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
Vincent treats clear issues and contribution guides as part of contribution
quality at 24:10 and 25:50. At 27:40, he adds tests and packaging. He also adds
CI and pre-commit hooks.
That connects technical writing to
[open source and developer relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
because adoption depends on docs, examples, and a respectful contribution path.

## Related Pages

These pages cover the adjacent roles, proof points, and technical contexts.

- [Developer Relations]({{ '/wiki/developer-relations/' | relative_url }})
- [Career Growth]({{ '/wiki/career-growth/' | relative_url }})
- [Communication]({{ '/wiki/communication/' | relative_url }})
- [Open Source]({{ '/wiki/open-source/' | relative_url }})
- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
