---
layout: wiki
title: "Contributing"
summary: "Podcast-backed guidance on useful contribution paths: reproducible issues, docs fixes, examples, tests, pull requests, mentoring, and community participation."
related:
  - Open Source and Developer Relations
  - Open Source Portfolio Evidence
  - Community
  - Documentation
  - Practices
---

## Definition and Scope

Contributing means doing useful work that improves a project or community for
other people. In DataTalks.Club podcast discussions, it's code and more than
code. It also includes documentation, examples, teaching, and community support.

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) gives
the most direct starting point in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
Around 25:50 he treats a clear, reproducible issue as a real contribution.
Around 27:40 he connects first code pull requests to tests, CI, packaging, and
pre-commit. That makes contribution a practical part of
[open source]({{ '/wiki/open-source/' | relative_url }}) and
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
not a separate prestige activity.

## Common Definition

A useful contribution reduces work for maintainers or helps users succeed. In
Vincent's
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }})
episode, the path starts with using the tool and noticing friction. The next
step is a small scoped improvement. The work can be a README change or API
example. It can also be a contribution note or narrow pull request.

Around 22:20 he names README material, guides, and examples as part of the
work. Around 24:10 he links contribution guides with polite
interaction.

The same definition appears from the maintainer side in
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}).
Vincent discusses contributor growth around 16:43 and maintainer handoff around
18:11. Around 23:29, open-source work becomes a hiring signal. The common
thread is maintainability. A change that's easy to review and test is more
valuable than a large feature that arrives without context.

## Guest Differences

Guests differ mostly on the best entry point. Vincent emphasizes maintainer
fit: start small and reproduce the problem before asking maintainers to review
something large.

In
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}),
[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) emphasizes
structured onboarding. Around 6:30 and 10:31 she describes Hugging Face
contribution sprints, good-first issues, and confidence building. Around 25:09
she includes documentation and non-code contributions.

[Will Russell]({{ '/people/willrussell/' | relative_url }}) puts more weight
on programs and mentorship. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
he connects hackathons to Git, teamwork, and projects around 11:46. Around
35:43 and 39:02 he talks about mentorship, pull request quality, Git skills,
and onboarding into large repositories. Around 41:16 he adds environment setup
and maintainer collaboration, which makes contribution partly a
[developer relations]({{ '/wiki/developer-relations/' | relative_url }})
problem.

[Sara EL-ATEIF]({{ '/people/saraelateif/' | relative_url }}) broadens the idea
beyond repository work. In
[Open Source and Volunteering]({{ '/podcasts/open-source-and-volunteering-in-ai-for-data-ml-career-growth/' | relative_url }}),
she frames volunteering as a way to build AI projects with community impact.
Around 23:44 she compares collaboration models. Around 48:42 she discusses
pitching relevant skills for volunteer projects. Around 51:21 she connects
volunteering to practical experience, referrals, and soft skills.

## Open-Source Contribution Paths

For open-source projects, the guests favor contribution paths that are small
enough to review and concrete enough to verify:

- Reproducible issues: include versions, environment, input, expected behavior,
  actual behavior, and a minimal reproduction. Vincent recommends this first in
  [Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }})
  around 25:50.
- Documentation fixes: improve a README, quickstart, guide, or error message.
  Vincent names documentation assets around 22:20. Around 25:09, Merve includes
  documentation as a valid first contribution in
  [Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
- Small code pull requests: fix one bug or add one narrow behavior with tests.
  Vincent links this to CI and packaging around 27:40. Will adds PR quality and
  Git skills around 39:02 in
  [Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}).
- Examples and demos: publish a notebook, app, video, or tutorial that helps a
  user do the first useful task. Merve discusses Hugging Face Spaces and
  Streamlit or Gradio demos around 17:37 and 51:12, which connects
  contribution work to
  [machine learning portfolio projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).
- Maintainer support: triage issues, improve templates, clarify contribution
  guides, or reduce CI friction. Vincent's maintainer handoff discussion around
  18:11 in
  [Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }})
  shows why this work matters for project sustainability.

## Community Contribution

Community contribution is the non-repository side of the same idea. It helps
other people learn, ship, or stay engaged. This comes up in
[DataTalks.Club Behind the Scenes]({{ '/podcasts/datatalksclub-building-scaling-data-community/' | relative_url }}).

The episode covers these community formats around 24:38 and 55:07:

- Open Source Spotlight
- Minis
- Book of the Week
- live coding
- office hours

Around 42:49, community participation becomes career advice about joining
communities, answering questions, and finding mentors.

This makes [community building]({{ '/wiki/community-building/' | relative_url }})
a contribution path, not only a background activity. Answering questions in
Slack and mentoring learners can create practical proof. So can reviewing
projects, joining Project of the Week, or organizing office hours. The proof
works like a small pull request when the work is visible and useful.

Sara's volunteer project discussion around 51:21 in
[Open Source and Volunteering]({{ '/podcasts/open-source-and-volunteering-in-ai-for-data-ml-career-growth/' | relative_url }})
adds another version. Group projects can build referrals and collaboration
evidence when contributors take clear roles.

## Documentation and Teaching

Documentation and teaching count because they lower the cost of adoption.
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
defines DevRel through education, documentation, and a "wisdom layer" around
18:03 in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
Around 25:17 he connects developer collaboration to feedback loops,
documentation, and dogfooding. Around 43:14 he talks about audience, goals, and
outlines for tutorials.

[Elle O'Brien]({{ '/people/elleobrien/' | relative_url }}) makes the same link
from a data science tool perspective in
[DevRel for Data Science]({{ '/podcasts/devrel-data-science-open-source-tools/' | relative_url }}).
Around 12:20 she describes product work and docs as part of the DevRel scope.
The same segment covers PRs, videos, and hiring. Around 52:06 and 54:46, she connects teaching and
curriculum design with reusable videos and open educational resources. These
are contribution formats when they help users understand a tool, reproduce a
workflow, or avoid common mistakes.

## Career Proof

Contribution becomes career proof when another person can look at the work and
see judgment. Merve's Hugging Face episode connects open-source experience to
hiring around 23:26 and 30:21. GitHub activity can show that a candidate can
work with large codebases, PR workflows, tests, and project conventions.
Vincent makes a similar point around 23:29 in
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
where open-source work demonstrates quality.

The proof is stronger when it's specific:

- one issue with a clean reproduction
- one merged pull request with tests
- one documentation improvement that unblocks users
- one demo that shows how a tool solves a real problem

Use
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
for this hiring focus. Connect contribution work to
[job search]({{ '/wiki/job-search/' | relative_url }}),
[career growth]({{ '/wiki/career-growth/' | relative_url }}), and
[data engineering portfolio projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
when the work needs to prove employability.

## Related Pages

Use these pages for the topics that sit next to contribution work.

- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Community]({{ '/wiki/community/' | relative_url }})
- [Community Building]({{ '/wiki/community-building/' | relative_url }})
- [Documentation]({{ '/wiki/documentation/' | relative_url }})
- [Practices]({{ '/wiki/practices/' | relative_url }})
- [Career Growth]({{ '/wiki/career-growth/' | relative_url }})
