---
layout: wiki
title: "Open Source"
summary: "How DataTalks.Club podcast guests discuss open source across ML and data tools, contribution work, governance, licensing, developer relations, and startup distribution."
related:
  - Open Source and Developer Relations
  - Open Source Portfolio Evidence
  - Contributing
  - Developer Relations
  - Documentation
  - Developer Experience
  - Community Building
  - Founder
  - Machine Learning Tools
  - Data Engineering Tools
  - Startup
  - Entrepreneurship
  - Tools
---

Open source appears in the DataTalks.Club podcast as a way to build public
software for data and ML, including developer tools. Guests describe it as an
engineering habit, a contribution surface, a trust mechanism, and a business
model.

The common thread is public usefulness, so the code and docs must help real
users. Examples, issues, and community conversations should do the same.

The topic sits next to
[contributing]({{ '/wiki/contributing/' | relative_url }}) and
[documentation]({{ '/wiki/documentation/' | relative_url }}). It also connects
to [developer experience]({{ '/wiki/developer-experience/' | relative_url }}),
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}), and
[community building]({{ '/wiki/community-building/' | relative_url }}).

For tool adoption, it overlaps with
[machine learning tools]({{ '/wiki/machine-learning-tools/' | relative_url }})
and
[data engineering tools]({{ '/wiki/data-engineering-tools/' | relative_url }}).
For company paths, see [startup]({{ '/wiki/startup/' | relative_url }}) and
[entrepreneurship]({{ '/wiki/entrepreneurship/' | relative_url }}).

## Common Definition

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) gives the
most practical definition in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
Around 14:22 and 15:39, he frames open source as useful public work that starts
from a concrete problem. He builds small tools such as `whatlies`, `clumper`,
and scikit-lego because he needs them, then lets other people reuse them.

[Will McGugan]({{ '/people/willmcgugan/' | relative_url }}) gives a similar
builder-centered definition in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}).
PyFilesystem, Rich, and Textual grew out of his own needs and experiments.
Around 57:20, he advises new authors to solve their own problem first. That
keeps open source attached to useful software rather than GitHub visibility.

For data and ML tools, usefulness also depends on ecosystem fit. In
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
Vincent explains why not every useful idea should enter core scikit-learn.
Around 14:01, he names plugins such as UMAP and scikit-lego as a healthier path.
A method can follow scikit-learn conventions without adding maintenance burden
to the main project.

## Guest Differences

Guests agree that open source should be useful, but they disagree on emphasis.
Vincent focuses on small libraries, maintainability, and project boundaries.
[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) focuses on public
contribution work and portfolio evidence through Hugging Face in
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) focuses
on education, feedback, and company support around projects such as Metaflow in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).

Founders and investors add a different lens.
[Elena Samuylova]({{ '/people/elenasamuylova/' | relative_url }}) uses Evidently
to explain open core, cloud, and on-prem adoption in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}).
[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) uses Zingg to explain
why open source can be both giving back and distribution in
[Building an Open-Source ML-Powered Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
[Bela Wiertz]({{ '/people/belawiertz/' | relative_url }}) treats open source as
developer-tool go-to-market in
[Early-Stage Investing in Open Source Developer Tools]({{ '/podcasts/investing-in-open-source-developer-tools/' | relative_url }}).

The disagreements aren't contradictions because they describe different parts of
the same system. Public engineering work, community maintenance, company
incentives, and developer adoption all matter.

## Contribution Work and Career Proof

Open-source work becomes career evidence when the work and the surrounding
conversation are visible. Vincent's contribution advice is deliberately small.
Around 22:20 in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
he treats README material and guides as part of the project surface. API
reference and examples belong there too.

Around 25:50, he treats a reproducible issue as a valid first contribution.
Around 27:40 and 28:40, he connects pull requests to tests and CI. Packaging and
pre-commit hooks matter too.

Merve gives the Hugging Face version in
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
She describes contribution sprints and dataset scripts. Good-first issues,
forum support, and non-code contributions belong in the same contribution
surface. Around 23:26 and 30:21, she says hiring managers can use GitHub work as
a work sample. They can see large-codebase experience, pull requests, tests, and
maintainer feedback.

Will adds the founder and hiring view. Around 44:38 in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}),
he says open-source work gives a hiring manager a visible body of work. He also
notes that good developers can exist without public contributions. The project
therefore treats open source as a strong signal, not a universal requirement.
For the focused career page, see
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and [job search]({{ '/wiki/job-search/' | relative_url }}).

## Community, Onboarding, and Maintainer Load

Open-source communities work best when they help contributors while protecting
maintainer time. Vincent's advice around contribution guides and polite issue
interaction isn't only etiquette. Smaller repositories, tests, and CI matter too
([Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
24:10-29:30). These habits help maintainers review work without turning every issue into
a support queue.

In the later scikit-learn conversation, Vincent returns to the same concern
through maintainer transition and volunteer motivation. He also talks about CI
cost control
([Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
18:11 / 21:51 / 31:42). Public code still needs operating discipline.

[Will Russell]({{ '/people/willrussell/' | relative_url }}) shows how structured
programs can make the first contribution less confusing. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
he describes hackathons, the MLH Fellowship, and Git practice. He also covers
environment setup and mentorship for large repositories. Around 35:43, 39:02,
and 41:16, contributors need project context and setup help. Small scopes and
review expectations help them make useful pull requests.

Hugo connects this community work to product feedback in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
Around 18:03 and 25:17, he describes DevRel through education and
documentation. Around 36:27, he adds dogfooding and feedback from developers
using the tool. In an open-source project, tutorials and demos aren't side work.
Docs issues, Slack, and forum conversations show where the software is hard to
understand.

## Governance and Project Boundaries

Open-source governance decides what the project can support and what should live
nearby. Hugo discusses company support for Dask and Metaflow around 10:47 in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
He distinguishes company involvement from project ownership, which matters when
a company wants community trust without taking over the project.

Vincent discusses :probabl., scikit-learn, and company naming in
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}).
Around 8:33, he explains why the company name should stay separate from the
open-source project. Around 10:28, he discusses scikit-learn governance,
NumFOCUS, and project history. Around 14:01, he argues for plugins when new
ideas don't belong in core scikit-learn.

Governance also includes technical operations. Vincent's CI cost example around
31:42 shows that maintainers still pay attention to infrastructure cost and
reliability. Merve's Hugging Face discussion around 33:23 treats pull-request
rejection, tests, and design discussion as normal parts of contribution. Public
code doesn't remove review. It makes review norms visible.

## Licensing, Open Core, and Monetization

Several founders use open source because data and ML buyers need trust before
they adopt infrastructure. Elena explains this for Evidently in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}).
Around 48:11 and 49:29, she describes open core, cloud, and licensing concerns.
Engineers and data scientists can try a model-monitoring tool before the company
sells hosting, scaling, security, or support. Around 51:48 and 56:17, she
connects the model to bottom-up adoption and on-prem use when teams don't want
to send data away.

Sonal gives the identity-resolution version in
[Building an Open-Source ML-Powered Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
Around 24:14, she says open source was both a way to give back and a way for
Zingg to reach more companies. Around 27:00, she discusses AGPL as a licensing
choice to reduce the risk of another company rehosting the product as SaaS.
Around 31:10, she still treats discoverability and growth as major reasons to
open source the product.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) shows the same
tradeoff for data connectors in
[ETL vs ELT and Data Lake vs Warehouse]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Around 43:45, she explains Airbyte's open-source plus cloud model. A broad
connector community is part of that model.

Around 48:26 and 49:32, she discusses competition and license choices. She uses
the Elasticsearch example and Airbyte's MIT license at the time of the episode.
Open source can help with
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) adoption.

The company still has to decide how cloud competitors, support needs, and
license choices affect the business.

## Open Source as Distribution

Bela adds the investor view in
[Early-Stage Investing in Open Source Developer Tools]({{ '/podcasts/investing-in-open-source-developer-tools/' | relative_url }}).
Around 13:42 and 16:40, he treats open source as go-to-market through community
trust and bottom-up developer adoption. Around 39:01, he warns that GitHub stars
need interpretation. Active engagement and problem validity matter more than
vanity metrics. Around 49:28 and 51:09, he discusses open-core licensing and
hosted services.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) shows the
library-to-startup path for DLT in
[From Data Freelancer to Startup]({{ '/podcasts/from-data-freelancer-to-startup-open-source-products/' | relative_url }}).
Around 36:00, his team uses workshops as product feedback. Around 41:23, he
treats documentation as a productive asset. Around 47:56 and 50:53, he explains
bottom-up go-to-market through personas, ecosystem partnerships, and demos.
Around 55:10, DLT's roadmap includes a paid complement to the open-source
library.

[Johannes Hötter]({{ '/people/johanneshotter/' | relative_url }}) gives a
similar story for open-source NLP tooling in
[Build Open-Source NLP Tools]({{ '/podcasts/building-open-source-nlp-tool/' | relative_url }}).
Around 26:22 and 28:11, he discusses why Kern chose open source and how the team
weighed distribution against revenue. Around 31:47, he describes open core,
multi-user SaaS, and services. Around 36:00 and 40:21, Discord support and
workarounds become part of sales because developer teams need trust before
adopting a labeling and weak-supervision tool.

Will's Textualize path adds the solo-maintainer-to-company version. Around
28:08 and 31:40 in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}),
he describes fundraising and building in public after Rich and Textual gained
attention. Around 38:32, the business model is web hosting for terminal apps
with a generous free tier. Around 49:37, GitHub Discussions, Discord, and
contribution channels become part of the product's community surface.

## Developer Relations and Feedback Loops

Open-source distribution often turns into
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) work,
but the two topics are related rather than identical. DevRel helps developers
understand, try, and trust a tool. Open source supplies the public software,
project norms, and contribution surface.

Hugo's Metaflow discussion places tutorials and docs in one role. Dogfooding and
developer feedback sit there too
([DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
18:03 / 25:17 / 36:27). [Elle O'Brien]({{ '/people/elleobrien/' | relative_url }})
adds the data-science version in
[DevRel for Data Science]({{ '/podcasts/devrel-data-science-open-source-tools/' | relative_url }}),
where product work, CML, and documentation sit with pull requests. Videos,
community management, and support sit there too.

For open-source projects, DevRel becomes valuable when it makes the project
easier to try or maintain. Demos and docs should reduce confusion, while
workshops and community support should produce better feedback. If a company
only uses the repository as a marketing asset, it misses the maintainer work
described throughout this page.

## Related Pages

[Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
focuses on adoption, education, feedback, and public technical communities.
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
focuses on using public contributions as career proof.
[Contributing]({{ '/wiki/contributing/' | relative_url }}) covers first
contributions and pull-request habits.
[Documentation]({{ '/wiki/documentation/' | relative_url }}) covers docs as a
product surface.
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) and
[Tools]({{ '/wiki/tools/' | relative_url }}) cover the surrounding product
interfaces.
