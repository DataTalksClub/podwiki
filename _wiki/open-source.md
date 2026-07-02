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
  - Technical Writing
  - Developer Experience
  - Community Building
  - Job Search
  - Founder
  - Machine Learning Tools
  - Data Engineering Tools
  - Data Engineering Portfolio Projects
  - Startups
  - Entrepreneurship
  - Solopreneur
  - Tools
---

Open source means public software that other people can use, discuss, and
improve. DataTalks.Club guests usually discuss it through data and ML tools.
[[podcast:open-source-ml-contributions|Vincent Warmerdam's contribution episode]]
covers scikit-learn ecosystem libraries, and
[[podcast:hugging-face-contributions-and-nlp-portfolio|Merve Noyan's NLP portfolio episode]]
covers Hugging Face work.
[[podcast:data-engineering-tools-modern-data-stack|Natalie Kwong's modern data stack episode]]
covers Airbyte,
[[podcast:from-data-freelancer-to-startup-open-source-products|Adrian Brudaru's founder episode]]
covers DLT, and
[[podcast:building-mlops-startup|Elena Samuylova's MLOps startup episode]]
covers Evidently.
Other episodes cover terminal UI tools, reproducibility tools, and open-source
NLP tooling.

The podcast discussions treat open source as practical rather than ideological.
Public code isn't enough because useful projects also need docs and examples.
They also need issue handling, tests, releases, and community norms.

Those pieces connect open source to
[[contributing]] and
[[documentation]]. They also connect
it to [[developer experience]],
[[developer relations]], and
[[community building]].

Open source also creates public evidence. A contribution can support
[[job search]], a
[[data-engineering-portfolio-projects|data engineering portfolio]],
or [[machine learning portfolio projects]].
For the step-by-step path, use the
[[Open Source Contributor Roadmap]].
For hiring evidence, use
[[Open Source Portfolio Evidence]].
For open-source adoption work, use
[[Open Source and Developer Relations]].

## Reusable Project Work

A practical definition frames open source through pragmatism and reciprocity,
with small tools that started from concrete needs, such as `whatlies`, `clumper`,
`memo`, and scikit-lego
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

The important point isn't that every idea becomes a famous package. The author
solves a real problem first, then makes the solution reusable. In those examples,
open source is about
[[contributing]],
[[documentation]], and the
[[Open Source Contributor Roadmap]]
more than repository publishing alone.

A similar builder-centered definition comes from PyFilesystem, Rich, and Textual,
which grew out of their author's own needs and experiments. New authors should
solve their own problem first, which keeps open source attached to useful
software rather than GitHub visibility
([[podcast:open-source-turned-into-career-and-startup-creation|From Developer to Startup Founder]]).

For data and ML tools, usefulness also depends on ecosystem fit. Not every useful
idea should enter core scikit-learn; plugins such as UMAP and scikit-lego are a
healthier path, since a method can follow scikit-learn conventions without adding
maintenance burden to the main project. That links open source to
[[machine learning tools]]
and [[software engineering]],
not only to public repositories
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]).

## Contribution, Adoption, and Company Lenses

Open source should be useful, but different lenses focus on different parts of
the system.

One lens centers small libraries, maintainability, and project boundaries:
scikit-learn governance, plugin strategy, maintainer transition, volunteer
motivation, and CI costs
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]).
It treats open source as an operating system for shared software, not only a
publishing format. That view sits close to
[[machine learning tools]],
[[tools]], and project
[governance](#governance-and-project-boundaries).

Another lens centers public contribution work and portfolio evidence through
Hugging Face: contribution sprints and good-first issues make the first step less
ambiguous, and Spaces with Streamlit or Gradio demos turn model work into
something other people can look at. This links directly to
[[Open Source Portfolio Evidence]]
and [[machine learning portfolio projects]]
([[podcast:hugging-face-contributions-and-nlp-portfolio|Contribute to Hugging Face and Build an NLP Portfolio]]).

A third lens centers education, feedback, and company support around projects
such as Metaflow: DevRel as education and documentation around tools, plus
collaboration, dogfooding, and developer feedback. That puts those examples next
to
[[developer relations]],
[[documentation]], and
[[Open Source and Developer Relations]]
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).

Founders and investors add a different lens. Evidently illustrates open core,
cloud, and on-prem adoption, in a sequence that starts before the repository with
customer discovery, product validation, and founder work around content and
community
([[podcast:building-mlops-startup|How to Build a Successful ML Startup]]). Use
[[startups|startup]] and
[[founder]] for that operating lens.

Zingg shows why open source can be both giving back and distribution. It took
about 18 months before public release, with hindsight connecting cofounder
search, earlier open source, use-case validation, and distribution channels
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source ML-Powered Identity Resolution Tool]]).

An investor lens treats open source as developer-tool go-to-market, warning that
GitHub stars need interpretation and that active users, engagement, and problem
validity matter more than vanity metrics
([[podcast:investing-in-open-source-developer-tools|Early-Stage Investing in Open Source Developer Tools]]).
For startup distribution, that lens pairs open source with
[[startups|startup]] work and
[[open-source-portfolio-evidence|open-source portfolio evidence]]
rather than vanity metrics.

These lenses aren't contradictions because they describe different parts of the
same system. Public engineering work, community maintenance, company incentives,
and developer adoption all matter.

## Data and ML Tool Ecosystems

Teams adopt each type of data or ML tool through a different route. A library
exposes APIs and examples. A connector exposes source coverage and
configuration. A model hub exposes models, datasets, demos, and community
support.

scikit-learn shows the library route: scikit-lego demonstrates
ecosystem-compatible components and low-maintenance APIs
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]), while
:probabl. stays separate from scikit-learn and governance sits with the project
and NumFOCUS, keeping company support separate from project ownership
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]]).

Hugging Face shows a platform route: dataset scripts and Hub features appear next
to Spaces, with community tabs and forum support nearby. That turns open source
into an ecosystem of models and datasets where demos and community support matter
as much as code, and connects open source to
[[NLP]],
[[model-registry|model registries]], and
[[developer experience]]
([[podcast:hugging-face-contributions-and-nlp-portfolio|Contribute to Hugging Face and Build an NLP Portfolio]]).

Airbyte gives the data engineering connector route. Its open-source strategy
depends on the long tail of connector needs, while custom connectors and
enterprise features sit closer to the cloud offering, and cloud competition and
license choices shape the model. The same discussion links Airbyte to ELT, dbt,
CDC, and the modern data stack
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Data Lake vs Warehouse]]).

This is why open source sits next to
[[data engineering tools]],
[[modern data stack]],
[[ELT]], and
[[CDC]].

Zingg gives the data product route. The product handles entity and identity
resolution, while the open-source decision affects adoption, licensing,
integrations, and growth. For complex matching systems, public software also
helps buyers evaluate the logic before they commit to a tool, which matters when
the product touches customer identity, fraud, or data quality
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source ML-Powered Identity Resolution Tool]]).

The topic connects open source to
[[data products]],
[[data engineering]], and
[[machine learning]].

DLT gives the programmable library route. The library turns JSON into relational
data and evolves through user feedback; workshops validate the product, docs
become a productive asset, and ecosystem demos support bottom-up adoption. This
route differs from a connector platform because the library helps Python users
build pipelines directly
([[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]]).

## Contribution Work and Career Proof

Open-source work becomes career evidence when reviewers can see the work and
the surrounding conversation. A public repository alone is weak evidence. A
useful issue or pull request shows what problem the contributor understood. So
can a demo, guide, test, or discussion.

The review trail matters too because it shows how the project responded. Useful
contribution advice is deliberately small: README material, guides, API
reference, and examples are part of the project surface; a reproducible issue is
a valid first contribution; and pull requests connect to tests, CI, packaging,
and pre-commit hooks. Those details connect the page to
[[software engineering]],
[[ci-cd|CI/CD]], and
[[testing]]
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

The Hugging Face version spans contribution sprints, dataset scripts, and CI
learning, with good-first issues, forum support, and non-code contributions in
the same contribution surface. Hiring managers can use GitHub work as a work
sample, seeing large-codebase experience, pull requests, tests, and maintainer
feedback. PR rejection becomes design alignment: open a discussion, understand
the project direction, and add tests that prove compatibility
([[podcast:hugging-face-contributions-and-nlp-portfolio|Contribute to Hugging Face and Build an NLP Portfolio]]).

The data-engineering hiring bar expects Python and SQL depth, code structure, and
tests, and values open-source contributions because review pressure makes the
work closer to professional practice
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep]]).

The interview framing requires a project walkthrough that shows ownership and
leads with impact, and candidates should defend the technical claims they put in
front of interviewers. An open-source link still needs a clear explanation of the
problem and setup, plus quality controls, maintainer interaction, and the result
([[podcast:data-interview-behavioral-and-portfolio-prep-guide|Ace Data Interviews]]).

The learn-in-public mechanism includes progress and corrections, with
collaborative docs, cheat sheets, demos, and brag documents making the work
easier for others to understand
([[podcast:developer-personal-brand-learn-in-public|Learn in Public]]).

On the founder and hiring view, open-source work gives a hiring manager a visible
body of work, though good developers can exist without public contributions. Open
source is therefore a strong signal, not a universal requirement
([[podcast:open-source-turned-into-career-and-startup-creation|From Developer to Startup Founder]]).

For the focused career page, see
[[Open Source Portfolio Evidence]]
and [[job search]]. For portfolio
framing, use
[[data engineering portfolio projects]]
and
[[machine learning portfolio projects]].
For an ordered learning path, use the
[[Open Source Contributor Roadmap]].

## Community, Onboarding, and Maintainer Load

Open-source communities work best when they help contributors while protecting
maintainer time. Vincent's advice around contribution guides and polite issue
interaction isn't only etiquette. Smaller repositories matter, and tests and CI
matter too
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]],
24:10-29:30). These habits help maintainers review work without turning every
issue into a support queue.

In the later scikit-learn conversation, Vincent returns to the same concern
through maintainer transition and volunteer motivation. He also talks about CI
cost control
([[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]],
18:11 / 21:51 / 31:42). Public code still needs operating discipline.

[[person:willrussell|Will Russell]] shows how structured
programs can make the first contribution less confusing. In
[[podcast:practical-devrel-demofirst-education-and-open-source|Developer Advocacy Through Community Impact]],
he describes hackathons, the MLH Fellowship, and Git practice. He also covers
environment setup and mentorship for large repositories. Around 35:43, 39:02,
and 41:16, contributors need project context and setup help. Small scopes and
review expectations help them make useful pull requests.

At 41:16-44:12, setup becomes part of the contribution barrier. Large projects
may require local services, memory, or hardware before a beginner can make a
useful change. Some projects need GPUs, Colab, or VMs.

Hugo connects this community work to product feedback in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
Around 18:03 and 25:17, he describes DevRel through education and
documentation. Around 36:27, he adds dogfooding and feedback from developers
using the tool. In an open-source project, tutorials and demos aren't side work.
Docs issues, Slack, and forum conversations show where the software is hard to
understand.

## Governance and Project Boundaries

Open-source governance decides what the project can support and what should live
nearby. Hugo discusses company support for Dask and Metaflow at 10:47 in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
He distinguishes company involvement from project ownership, which matters when
a company wants community trust without taking over the project.

Vincent discusses :probabl., scikit-learn, and company naming in
[[podcast:open-source-ml-tools-strategy-and-business-models|Open Source ML Tools]].
Around 8:33, he explains why the company name should stay separate from the
open-source project. Around 10:28, he discusses scikit-learn governance,
NumFOCUS, and project history. Around 14:01, he argues for plugins when new
ideas don't belong in core scikit-learn.

Governance also includes technical operations. Vincent's CI cost example at
31:42 shows that maintainers still pay attention to infrastructure cost and
reliability. Maintainers may need custom GitHub Actions runners or caching. They
may also need cheaper compute.

Merve's
[[podcast:hugging-face-contributions-and-nlp-portfolio|33:23|Hugging Face discussion]]
treats pull-request rejection, tests, and design discussion as normal parts of
contribution. Public code doesn't remove review. It makes review norms visible.

## Licensing, Open Core, and Monetization

Several founders use open source because data and ML buyers need trust before
they adopt infrastructure. That doesn't replace customer discovery. Elena
explains this for Evidently in
[[podcast:building-mlops-startup|How to Build a Successful ML Startup]].

At 42:15 and 43:59, the Evidently story starts with interviews and validation
around model monitoring. At 48:11 and 49:29, she describes open core, cloud, and
licensing concerns. Engineers and data scientists can try a
[[model-monitoring|model-monitoring]] tool before
the company sells hosting, scaling, security, or support.

At 51:48 and 56:17, she connects the model to bottom-up adoption and on-prem
use when teams don't want to send data away.

Sonal gives the identity-resolution version in
[[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source ML-Powered Identity Resolution Tool]].
At 23:00, Zingg took about 18 months before public release. At 24:14, she says
open source was both a way to give back and a way for Zingg to reach more
companies. At 27:00, she discusses AGPL as a licensing choice to reduce the
risk of another company rehosting the product as SaaS. At 31:10, she still
treats discoverability and growth as major reasons to open source the product.

[[person:nataliekwong|Natalie Kwong]] shows the same
tradeoff for data connectors in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Data Lake vs Warehouse]].
At 43:45, she explains why Airbyte is open source. A broad connector community
helps cover sources that a closed team may not prioritize. At 46:52, the cloud
and enterprise offering sits around that project. At 48:26 and 49:32, she
discusses competition and license choices.

She uses the Elasticsearch example and Airbyte's MIT license at the time of the
episode. Open source can help with
[[data engineering]] adoption.

The company still has to decide how cloud competitors, support needs, and
license choices affect the business. Those tradeoffs separate open source as a
technical practice from
[[startups|startup]],
[[founder]], and
[[entrepreneurship]] topics.

## Open Source as Distribution

Bela adds the investor view in
[[podcast:investing-in-open-source-developer-tools|Early-Stage Investing in Open Source Developer Tools]].
At 13:42 and 16:40, he treats open source as go-to-market through community
trust and bottom-up developer adoption. At 32:31 and 36:27, it still needs a
team, market need, and problem validity. At 39:01, he warns that GitHub stars
need interpretation. Active engagement matters more than vanity metrics.

At 49:28 and 51:09, he discusses open-core licensing and hosted services. At
54:47, support-only revenue looks less attractive because it scales with
headcount.

[[person:adrianbrudaru|Adrian Brudaru]] shows the
library-to-startup path for DLT in
[[podcast:from-data-freelancer-to-startup-open-source-products|From Data Freelancer to Startup]].
Around 36:00, his team uses workshops as product feedback. Around 41:23, he
treats documentation as a productive asset. Around 47:56 and 50:53, he explains
bottom-up go-to-market through personas, ecosystem partnerships, and demos.
Around 55:10, DLT's roadmap includes a paid complement to the open-source
library.

This route came from freelancing, savings, consulting, and design partners.
Product validation mattered too, so it's a services-to-product route rather than
only an open-source launch.

[[person:johanneshotter|Johannes Hötter]] gives a
similar story for open-source NLP tooling in
[[podcast:building-open-source-nlp-tool|Build Open-Source NLP Tools]].
Around 26:22 and 28:11, he discusses why Kern chose open source and how the team
weighed distribution against revenue. Around 31:47, he describes open core,
multi-user SaaS, and services. Around 36:00 and 40:21, Discord support and
workarounds become part of sales because developer teams need trust before
adopting a labeling and weak-supervision tool.

At 56:03 and 57:02, open source builds trust and sends a signal to investors.
It isn't the whole business model.

Will's Textualize path adds the solo-maintainer-to-company version. Around
28:08 and 31:40 in
[[podcast:open-source-turned-into-career-and-startup-creation|From Developer to Startup Founder]],
he describes fundraising and building in public after Rich and Textual gained
attention. This attention wasn't a scripted fundraising funnel. At 38:32 and
40:28, the planned model is web hosting and add-on features for terminal apps
with a generous free tier. At 49:37, GitHub Discussions, Discord, and
contribution channels become part of the product's community surface.

## Developer Relations and Feedback Loops

Open-source distribution often turns into
[[developer relations]] work,
but the two topics are related rather than identical. DevRel helps developers
understand, try, and trust a tool. Open source supplies the public software,
project norms, contribution surface, and governance constraints.

Hugo's Metaflow discussion places tutorials and docs in one role. Dogfooding and
developer feedback sit there too
([[podcast:devrel-open-source-machine-learning|18:03-36:27]]).
At 43:14 and 54:31, GitHub portfolios and talks become career signals. Meetups
and audience-centered tutorials support adoption too.

[[person:elleobrien|Elle O'Brien]] adds the data-science
version in
[[podcast:devrel-data-science-open-source-tools|DevRel for Data Science]].
Her path starts with a visible StyleGAN project at 9:33, then moves into DVC
and CML. Documentation, pull requests, and videos come next. Community support
and product signal appear in the same work
([[podcast:devrel-data-science-open-source-tools|12:20-23:51]]).

For the full adoption, education, and feedback-loop treatment, use
[[Open Source and Developer Relations]].

## Limits

These episodes also put limits around the signal. Open source doesn't prove
that a tool has product-market fit. It doesn't prove that a contributor can do
every part of a paid role. It also doesn't remove the need for governance,
support, security, or licensing decisions. Teams still need commercial
strategy.

Bela's investor discussion makes this explicit. At 32:31 and 36:27 in
[[podcast:investing-in-open-source-developer-tools|Early-Stage Investing in Open Source Developer Tools]],
he looks for the team, market need, and problem validity behind the repository.
At 39:01, he warns against reading GitHub stars without engagement context. At
49:28 and 51:09, he still needs a commercialization model.

Will McGugan gives the career version in
[[podcast:open-source-turned-into-career-and-startup-creation|From Developer to Startup Founder]].
Open-source work can give a recruiter a body of work at 44:38, but he also says
good developers can exist without public contributions. Treat open source as
reviewable evidence, not as the only evidence.

## Related Pages

These pages cover adjacent contribution, adoption, tool, and company paths.

- Adoption and feedback:
  [[Open Source and Developer Relations]],
  [[Developer Relations]],
  [[Developer Experience]],
  and [[Community Building]].
- Contribution and career evidence:
  [[Open Source Contributor Roadmap]]
  and
  [[Open Source Portfolio Evidence]].
  [[Contributing]],
  [[Documentation]], and
  [[Technical Writing]] cover
  the working habits behind that evidence.
  [[Data Engineering Portfolio Projects]]
  and
  [[Machine Learning Portfolio Projects]]
  cover the project framing around open-source work samples.
- Data and ML tools:
  [[Data Engineering Tools]],
  [[Machine Learning Tools]],
  [[Tools]], and
  [[scikit-learn|Scikit-Learn]].
- Company paths:
  [[startups|Startup]],
  [[Founder]],
  [[Entrepreneurship]], and
  [[Solopreneur]].
