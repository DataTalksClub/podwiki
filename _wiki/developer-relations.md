---
layout: wiki
title: "Developer Relations"
summary: "How guests frame DevRel as technical education, demos, docs, community feedback, open-source work, and adoption for data and ML tools."
related:
  - Open Source and Developer Relations
  - Developer Experience
  - Community Building
  - Documentation
  - Technical Writing
---

Developer relations, or DevRel, helps developers understand and trust a
technical product. It also helps them use the product well enough to give useful
feedback. In DataTalks.Club episodes, DevRel sits between
[[developer experience]],
[[documentation]], and
[[technical writing]]. It also
connects [[open source]], product
feedback, and [[community building]].

DevRel centers on education, documentation, and a "wisdom layer" around tools.
Guests connect DevRel to dogfooding, developer collaboration, and documentation
feedback. They also treat it as a way to route user friction back to the team
building the product
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

DevRel is the role and operating practice. [[Open Source and Developer Relations]]
covers the version where the product is an open-source project. That version
depends on maintainers, governance, contribution paths, or open-source business
models. [[Community Building]] and [[Community]] cover member participation,
moderation, events, and peer-to-peer support.

Hugo Bowne-Anderson's freelance path keeps DevRel connected to consulting,
advising, and teaching rather than treating it as a separate communications
track. In his framing, DevRel remains technical product enablement. It helps
people build and ship with AI while feeding practical adoption lessons back into
the work
([[cite:practical-llm-engineering-and-rag@3:57=>Freelance DevRel Path]]).

## Developer Adoption Model

Across the DevRel episodes, guests converge on the same operating model. DevRel
people learn the tool deeply and turn that knowledge into reproducible
examples. They help developers get their first useful result, then bring
confusing parts back to product and engineering.

One DevRel role at Iterative spans product work and CML. It also covers
documentation, pull requests, videos, and hiring. Daily work includes content
creation, community management, and support
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].
DevRel turns the community-facing role into a product signal channel. It sees
where users get confused before roadmap discussions surface those problems
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

DevRel is more than awareness work because it's technical adoption work. A
DevRel person needs enough
[[software engineering]] and
product fluency to build credible examples. They also need enough writing skill
to explain those examples and enough community judgment to notice repeated user
friction.

## DevRel Centers of Gravity

Guests agree on the bridge role, but they place DevRel in different centers of
gravity. Some put it close to product and engineering. Others put it closer to
education, community, or open-source engineering.

One view places DevRel close to engineering and product. It covers reporting
lines and technical alignment, then names technical fluency, writing, and
community building as core skills. Practitioners lose credibility when they stop
dogfooding the product
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

Another view emphasizes solo prioritization and public exposure while balancing
release support with evergreen content
([[cite:devrel-data-science-open-source-tools@15:02=>DevRel for Data Science]]).
It also confronts online abuse and burnout. It covers anonymity, moderation, and
peer solidarity
([[cite:devrel-data-science-open-source-tools@17:54=>DevRel community safety]],
[[cite:devrel-data-science-open-source-tools@28:55=>DevRel burnout risk]]).
In that account, DevRel has emotional and safety costs that don't show up in a
pure [[developer experience]] definition.

At :probabl, [[person:vincentwarmerdam=>Vincent Warmerdam]] combines DevRel
with core development responsibilities. Combining those responsibilities puts
DevRel closer to open-source engineering, with interactive scikit-learn content
and videos tied to the product work
([[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]]).

A more demo-first version describes developer advocacy at Kestra through
documentation, demos, and outreach. The advocate starts with bullet points,
then moves into building demos and collaborating with writers. That role also
has to balance technical depth with community work
([[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]]).

## Education, Tutorials, and Documentation

DevRel people turn internal product knowledge into public learning paths, placing
education and documentation at the center of the job. Tutorials should start from
audience and goals, not from the feature a team wants to announce
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

In the data-science DevRel discussion, teaching includes applied data science
and reproducibility. The guest links teaching with DevRel through curriculum
design and reusable video content
([[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]]).
DevRel depends on the same audience-aware practice used in
[[technical writing]] and
[[documentation]]. It goes beyond
publishing docs because developers still need to succeed with the tool in a real
context.

On the writing side, guests discuss choosing readers, peers, and future
teammates. They also treat technical documentation as decision logs, rationales,
and team memory
([[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]]).
DevRel uses the same writing muscles but points them toward external developer
adoption.

## Demos as Developer Experience

DevRel teams use demos to show the first useful path through a tool. A demo is
weak when it only sells the feature. It helps when it reduces setup uncertainty,
shows the tool in context, and exposes the tradeoffs a real user will hit. That
places demo work close to [[developer experience]].

In the Kestra discussion, demo videos need a clear goal and a useful pace. The
guest argues for full walkthroughs and uses an "after execution" notification
as a concrete feature demo
[[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]].

A "Learn with Kestra" series uses adjacent tools like Docker and Postgres. It
also brings Git into the learning path. Developer adoption often depends on the
surrounding work, not only the main product
([[cite:practical-devrel-demofirst-education-and-open-source=>Developer Advocacy Through Community Impact]]).

In Adrian Brudaru's data-tool startup version, the team used `dlt` workshops as
a product feedback loop because teaching showed where users got stuck.
Checkpoints, live support, and CodeSpaces made that friction visible enough to
improve the developer path
([[cite:from-data-freelancer-to-startup-open-source-products@36:00=>Workshop validation]],
[[cite:from-data-freelancer-to-startup-open-source-products@37:28=>Workshop design]]).

In the ML infrastructure discussion, a Metaflow sandbox demo connects teaching
reproducibility with dogfooding and simplified workflows
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).
Those examples belong with
[[Metaflow]],
[[MLOps]], and
[[machine learning tools]]
because each demo also tests the tool's developer experience.

## Community Channels and Open-Source Trust

DevRel often runs through public communities, but it isn't the same job as
general community management. Community work moves from founder-led activity to
peer-to-peer participation. It also depends on sprints, autonomy, and
many-to-many engagement
([[cite:mlops-community-building-and-meetups=>MLOps Community Playbook]]).

DevRel can use those habits, but its product responsibility is narrower. DevRel
helps developers adopt the tool and routes technical feedback back to the
builders
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

Open-source DevRel has an extra constraint because the project community must
keep its own credibility. Airbyte's open-source-plus-cloud model raises questions
of competition and licensing risk
([[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT & Data Lake vs Warehouse]]).

The scikit-learn discussion adds governance pressure through project history
and maintainer transition
([[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]]).
DevRel work in that setting has to respect governance and maintainers while
supporting contribution paths and long-term trust.

Together, these discussions link DevRel closely to
[[open source and developer relations]],
[[contributing]], and
[[open-source-portfolio-evidence=>open-source portfolio evidence]].
Docs fixes and examples can be real technical contributions when they remove
adoption friction. The same is true for reproducible issues, workshops, and demo
repos.

## Adoption Metrics and Product Feedback

DevRel teams get more from metrics when they track developer progress, not only
audience size. Community signals and analytics can become a serious analysis
function, while growth tactics still need sustainable strategy
([[cite:devrel-data-science-open-source-tools@26:01=>DevRel community metrics]]).
Content goals separate awareness, support, and open-source strategy
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).

They can track successful first runs, activated users, and repeated usage. Docs
issues and unanswered support questions also matter when they change the tool.
The same is true for contribution flow, event follow-up, and product feedback
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].
Vanity metrics can still help with distribution, but they don't prove adoption
by themselves.

A tutorial view, a conference talk, or a social post matters more when it leads
to a working project or a clearer issue. A better doc page or a product fix
matters too.

Community teams measure a different center of gravity. They track membership
milestones, survey and feedback cadence, and member connections
([[cite:mlops-community-building-and-meetups=>MLOps Community Playbook]]).
Those metrics measure community health. DevRel can borrow them but still needs
product-facing signals that tell engineering where developers get stuck.

## Boundaries with Marketing and Community Work

DevRel and marketing both care about reaching developers through SEO and content
strategy
([[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]).
Audience targeting sits in the same overlap.
DevRel has to protect credibility. Practitioners should be able to reproduce the
demo, look at the code, and connect what they learned to real work.

The evangelism side covers AI evangelism, positioning, and messaging strategy,
recommending one to three clear takeaways and calls to action
([[cite:public-speaking-for-data-scientists=>Public Speaking for Data Scientists]]).
DevRel can use that skill, but it doesn't replace the technical feedback loop.

DevRel teams should treat conference work as part of that overlap when it
creates useful developer education rather than only awareness. Ben Taylor
recommends proposing talks with
novelty and enough ambition to stretch the speaker. Speakers can then build a
speaker resume from smaller venues toward keynotes
([[cite:public-speaking-for-data-scientists@50:20=>Conference proposals]],
[[cite:public-speaking-for-data-scientists@53:48=>Speaker resume]]).
Use [[data-ai-conference-building=>data and AI conference building]] for full
event work around speaker selection, sponsor fit, pricing, and networking.
A technical event stays credible for practitioners when organizers handle those
choices carefully
([[cite:s23e09-starting-data-conference-data-makers-fest-story=>Data Makers Fest]]).

Swyx draws the same boundary: reusable talks support communication practice and
technical-judgment distribution. DevRel still has to connect the talk back to
docs, demos, support, and product feedback
([[cite:developer-personal-brand-learn-in-public@59:04=>Reusable talks]]).

A good talk can drive awareness, while a good DevRel program also improves docs,
examples, and onboarding. It should also improve support and product decisions.

DevRel also overlaps with [[community]],
so the ownership boundary matters here too. Community work creates belonging,
moderation, and member-to-member connection. Events and shared identity belong
on the community side. DevRel uses those channels to teach, listen, test
examples, and support adoption.

When a company turns every community interaction into a campaign, it weakens
trust. When DevRel disconnects from product and engineering, it becomes only
broadcasting.

## Related Pages

DevRel also depends on related practices that cover maintainers, docs, technical
users, and community channels.

- [[Open Source and Developer Relations]]
  connects DevRel to maintainers, governance, contribution paths, and
  open-source business models.
- [[Developer Experience]]
  covers adoption friction, onboarding, and usability for technical users.
- [[Documentation]] and
  [[Technical Writing]] cover the
  writing practices behind tutorials, guides, and decision records.
- [[Community Building]] and
  [[Community]] cover membership,
  moderation, events, and peer-to-peer participation.
- [[Open Source]] and
  [[Contributing]] cover project
  stewardship and contribution paths.
