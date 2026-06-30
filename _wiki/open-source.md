---
layout: wiki
title: "Open Source"
summary: "How DataTalks.Club podcast guests discuss open source across ML and data: contribution work, career proof, community, governance, licensing, DevRel, startup distribution, and open-core business models."
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
---

Open source in the DataTalks.Club archive isn't only a license choice. Guests
describe it as public work on data and ML tools. They use it to recruit
contributors, earn trust from developers and create a path from individual
learning to startup distribution. The topic sits close to
[contributing]({{ '/wiki/contributing/' | relative_url }}) and
[documentation]({{ '/wiki/documentation/' | relative_url }}). It also connects
to [developer relations]({{ '/wiki/developer-relations/' | relative_url }}),
[developer experience]({{ '/wiki/developer-experience/' | relative_url }}),
and [community building]({{ '/wiki/community-building/' | relative_url }}).

The archive also treats open source as a business and governance problem. A
public repository can help users try a tool before they talk to sales. The
company still has to decide which work belongs in the open project, which work
belongs in a paid product and who reviews contributions. It also has to decide
how licensing protects the project.
[Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
covers the adoption and feedback work around public technical projects.

## Open Source in the Archive

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) gives the
most practical definition in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
Around 9:30, he frames open source as pragmatic sharing: he builds small tools
because he needs them. Other people can then find and reuse them. His examples
include `whatlies`, `clumper`, and
[scikit-lego]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
They show open source as useful byproduct work rather than a grand strategy from
the first commit.

[Will McGugan]({{ '/people/willmcgugan/' | relative_url }}) gives a similar
builder-centered version in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}).
PyFilesystem, Rich, and Textual began from concrete needs. They also gave him
room for learning and creative freedom. Around 57:20, he advises new
open-source authors to solve their own problem first. That keeps the archive's
definition grounded: open source starts with useful software, not with a GitHub
badge.

For ML and data tools, usefulness also depends on ecosystem fit. In
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
Vincent explains why not every useful idea should enter core scikit-learn. Around
14:01, he names plugins such as UMAP and scikit-lego as a healthier path. A
method can follow scikit-learn conventions without adding maintenance burden to
the main project. That connects open source to
[machine learning tools]({{ '/wiki/machine-learning-tools/' | relative_url }}).

The public API matters as much as publishing code, and compatibility norms,
tests, and release expectations matter too.

## Contribution Work and Career Proof

Guests treat open-source work as credible career proof when someone can look at
the work and the conversation around it. Vincent's contribution advice is
deliberately small. Around 22:20 in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
he names README material and guides as part of the project surface. API
reference and examples belong there too. Around 25:50, he treats a reproducible
issue as a valid first contribution.

Around 27:40, he connects code pull requests to tests, CI, packaging and
pre-commit hooks.

[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) gives the Hugging Face
version in
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
She describes contribution sprints, dataset scripts, good-first issues, and
forum support. She also includes non-code contributions.

Around 23:26 and 30:21, she says hiring managers can use GitHub work to see
whether someone has worked with large codebases and pull requests. Tests and
maintainer feedback matter in the same evaluation. That makes open source
especially useful for [job search]({{ '/wiki/job-search/' | relative_url }})
when the contribution proves maintainable work rather than only interest.

Will McGugan adds the founder and hiring view. Around 44:38 in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}),
he says open-source work gives a hiring manager a visible body of work. He also
notes that good developers can exist without public contributions. The archive
therefore treats open source as a strong signal, not a universal requirement.
For the detailed portfolio question, use
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).

## Community, Onboarding, and Maintainer Load

Open-source communities in the archive work best when they help contributors
reduce maintainer burden. Vincent's advice around contribution guides, polite
issue interaction and tests isn't only etiquette. CI and smaller repositories
matter too
([Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
24:10-29:30). It protects volunteer time.

In his later scikit-learn discussion, he returns to the same concern through
maintainer transition. He also discusses volunteer motivation and CI cost control
([Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}),
18:11 / 21:51 / 31:42).

[Will Russell]({{ '/people/willrussell/' | relative_url }}) shows how structured
programs can help new contributors without dumping work on maintainers. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
he describes hackathons, the MLH Fellowship, and Git practice. He also covers
environment setup and mentorship for large repositories. Around 35:43, 39:02,
and 41:16, contributors need project context and setup help. They also need
small scopes and review expectations before they can make useful pull requests.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) connects
this community work to product feedback in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
Around 18:03 and 25:17, he describes DevRel through education and
documentation. Dogfooding and feedback from developers using the tool belong in
that same role.

In an open-source project, tutorials and demos aren't side work. Slack or forum
conversations and docs issues also show where the software confuses real users.

## Governance and Project Boundaries

Open-source governance appears most clearly in the scikit-learn and Metaflow
episodes. Hugo discusses company support for projects such as Dask and Metaflow
around 10:47 in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
He distinguishes company involvement from project ownership, which matters when
a company wants community trust without taking over the project.

Vincent discusses :probabl., scikit-learn, and company naming in
[Open Source ML Tools]({{ '/podcasts/open-source-ml-tools-strategy-and-business-models/' | relative_url }}).
Around 8:33, he explains why the company name should stay separate from the
open-source project. Around 10:28, he discusses scikit-learn governance,
NumFOCUS, and the project's history. Around 14:01, he argues for plugins when
new ideas don't belong in core scikit-learn.

Maintainers use governance to decide what the project can support. They also use
it to decide what should live nearby and how contributors can participate without
turning a mature library into a dumping ground.

The archive also links governance to technical operations. Vincent's CI cost
example around 31:42 shows that open-source maintainers still pay attention to
infrastructure cost and reliability. Merve's Hugging Face discussion around
33:23 treats pull-request rejection and tests as normal parts of contribution.
Design discussion belongs there too.

Public code doesn't remove review, but it makes the review norms visible.

## Licensing, Open Core, and Startup Distribution

Several founders use open source because data and ML buyers need trust before
they adopt infrastructure. [Elena Samuylova]({{ '/people/elenasamuylova/' | relative_url }})
explains this for Evidently in
[How to Build a Successful ML Startup]({{ '/podcasts/building-mlops-startup/' | relative_url }}).
Around 48:11 and 49:29, she describes open core, cloud, and licensing concerns.
Engineers and data scientists can try small pieces of a model monitoring tool.
The company can later sell hosting, scaling, security, or support.

Around 51:48 and 56:17, she connects that model to bottom-up adoption and
on-premise use when teams don't want to send data away.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) gives the identity
resolution version in
[Building an Open-Source ML-Powered Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
Around 24:14, she says open source was both a way to give back and a way for
Zingg to reach more companies. Those companies wouldn't buy an expensive closed
product before trying it. Around 27:00, she discusses AGPL as a licensing choice
to reduce the risk of another company rehosting the product as SaaS. Around
31:10, she still treats discoverability and growth as major reasons to open
source.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) makes the same
tradeoff visible for data connectors in
[ETL vs ELT and Data Lake vs Warehouse]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Around 43:45, she explains Airbyte's open-source plus cloud model and the need
for a broad connector community. Around 48:26 and 49:32, she discusses
competition and license choices, including the Elasticsearch example and
Airbyte's MIT license at the time of the episode. Open source helps with
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) adoption. The
company still has to decide how cloud competitors, support needs, and license
changes affect the business.

[Bela Wiertz]({{ '/people/belawiertz/' | relative_url }}) adds the investor
view in
[Early-Stage Investing in Open Source Developer Tools]({{ '/podcasts/investing-in-open-source-developer-tools/' | relative_url }}).
Around 13:42 and 16:40, he treats open source as go-to-market through community
trust and bottom-up developer adoption. Around 39:01, he warns that GitHub stars
need interpretation. Active engagement and problem validity matter more than
vanity metrics.

Team strength and a commercialization plan matter too. Around 49:28 and 51:09,
he discusses open-core licensing and hosted services.

Enterprise licenses and support belong in that model too.

## Open Source as Product Strategy

The founder episodes show that open source works best when it matches the
product's adoption path. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
positions DLT as a developer-focused library in
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
workarounds become part of sales. Education and DevRel do too, because developer
teams need trust before adopting a labeling and weak-supervision tool.

Will McGugan's Textualize path adds the solo-maintainer-to-company version.
Around 28:08 and 31:40 in
[From Developer to Startup Founder]({{ '/podcasts/open-source-turned-into-career-and-startup-creation/' | relative_url }}),
he describes fundraising and building in public after Rich and Textual gained
attention. Around 38:32, the business model is web hosting for terminal apps
with a generous free tier. Around 49:37, GitHub Discussions, Discord, and
contribution channels become part of the product's community surface.

## Developer Relations and Distribution

Open-source distribution often turns into DevRel work, but the archive keeps
the two topics distinct. DevRel helps developers understand, try, and trust a
tool. Open source supplies the public software, project norms, and contribution
surface.

Hugo's Metaflow discussion places tutorials and docs in one role. Dogfooding and
developer feedback sit there too
([DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}),
18:03 / 25:17 / 36:27). [Elle O'Brien]({{ '/people/elleobrien/' | relative_url }})
adds the data-science version in
[DevRel for Data Science]({{ '/podcasts/devrel-data-science-open-source-tools/' | relative_url }}),
where product work, CML, and documentation sit in one role. Pull requests,
videos, community management, and support sit there too.

For a broad open-source page, the important point is narrower. DevRel becomes
valuable when it makes the open project easier to try and maintain. Good demos
and docs should reduce confusion.

Workshops and community support should produce better feedback. If a company
only uses the repository as a marketing asset, it misses the governance and
contribution work. It also misses the maintainer work that the rest of the
archive keeps foregrounding.
