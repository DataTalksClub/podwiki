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
feedback. In data and ML tooling, DevRel sits between product work and developer
communities. It also draws on [[developer experience]], [[documentation]], and
[[technical writing]].

DevRel handles the developer-facing function and feedback loop, while
[[Community Building]] covers membership and moderation, events, and peer-to-peer
support.
[[Open Source and Developer Relations]] covers the version where maintainers,
governance, contribution paths, or open-source business models govern the work.

## Adoption Feedback Loop

The recurring DevRel model is practical adoption feedback. DevRel people learn
the tool deeply and build reproducible examples. They help developers get their
first useful result, then bring confusing parts back to product and engineering.

Guests connect DevRel to a "wisdom layer" around tools, dogfooding, and
developer collaboration. They also connect it to documentation feedback and
product decisions
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
One DevRel role at Iterative spans product work and CML. It also covers
documentation, pull requests, videos, and hiring. Daily work includes content
creation, community management, and support
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

DevRel is more than awareness work because it's technical adoption work. A
DevRel person needs enough [[software engineering]] and product fluency to build
credible examples. They also need enough writing skill to explain those examples
and enough community judgment to notice repeated user friction.

Hugo Bowne-Anderson's freelance path keeps DevRel connected to consulting,
advising, and teaching rather than treating it as a separate communications
track. In his framing, DevRel helps people build and ship with AI while feeding
practical adoption lessons back into the work
[[cite:practical-llm-engineering-and-rag@3:57=>Freelance DevRel Path]].

## Centers of Gravity

Guests agree on the bridge role, but they place DevRel in different centers of
gravity. Some put it close to product and engineering. Others put it closer to
education, community, or open-source engineering.

One view places DevRel close to engineering and product. It covers reporting
lines and technical alignment, then names technical fluency, writing, and
community building as core skills. Practitioners lose credibility when they stop
dogfooding the product
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

Another view emphasizes solo prioritization and public exposure while balancing
release support with evergreen content
[[cite:devrel-data-science-open-source-tools@15:02=>DevRel for Data Science]].
It also confronts online abuse and burnout through anonymity, moderation, and
peer solidarity
[[cite:devrel-data-science-open-source-tools@17:54=>DevRel community safety]]
[[cite:devrel-data-science-open-source-tools@28:55=>DevRel burnout risk]].
In that account, DevRel has emotional and safety costs that don't show up in a
pure [[developer experience]] definition.

At :probabl, [[person:vincentwarmerdam=>Vincent Warmerdam]] combines DevRel with
core development responsibilities. Combining those responsibilities puts DevRel
closer to open-source engineering, with interactive scikit-learn content and
videos tied to product work
[[cite:open-source-ml-tools-strategy-and-business-models=>Open Source ML Tools]].

## Education, Tutorials, and Documentation

DevRel people turn internal product knowledge into public learning paths.
Tutorials should start from audience and goals, not from the feature a team wants
to announce
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

In the data-science DevRel discussion, teaching includes applied data science and
reproducibility. The guest links teaching with DevRel through curriculum design
and reusable video content
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].
DevRel depends on the same audience-aware practice used in [[technical writing]]
and [[documentation]], but it points that writing toward external developer
adoption.

Technical writing discussions add an adjacent skill because writers choose
readers, peers, and future teammates. They also use docs as decision logs,
rationales, and team memory
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].
DevRel uses those muscles when tutorials, docs, and examples help developers
make a product work in context.

## Demos as Developer Experience

DevRel teams use demos to show the first useful path through a tool. Weak demos
only sell the feature. Useful demos reduce setup uncertainty. They show the tool
in context and expose the tradeoffs a real user will hit. Demo work sits close
to [[developer experience]].

The Kestra guest emphasizes clear demo goals and useful pace
[[cite:practical-devrel-demofirst-education-and-open-source=>Kestra DevRel]].
Full walkthroughs and an "after execution" notification show the same
demo-first approach.
A "Learn with Kestra" series uses adjacent tools like Docker and Postgres. It
also brings Git into the learning path because developer adoption often depends
on the surrounding work rather than only the main product
[[cite:practical-devrel-demofirst-education-and-open-source=>Kestra DevRel]].

In Adrian Brudaru's data-tool startup version, the team used `dlt` workshops as
a product feedback channel. Teaching showed where users got stuck. Checkpoints,
live support, and CodeSpaces made that friction visible enough to improve the
developer path
[[cite:from-data-freelancer-to-startup-open-source-products@36:00=>Workshop validation]]
[[cite:from-data-freelancer-to-startup-open-source-products@37:28=>Workshop design]].

In the ML infrastructure discussion, a Metaflow sandbox demo connects teaching
reproducibility with dogfooding and simplified workflows
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Those examples also connect to [[Metaflow]], [[MLOps]], and
[[machine learning tools]] because each demo tests the tool's developer
experience.

## Community Channels Without Community Ownership

DevRel often uses public communities, but it isn't the same job as general
community management. Community work creates belonging, moderation, and
member-to-member connection. Events and shared identity belong on the community
side. DevRel uses those channels to teach, listen, test examples, and support
adoption.

The MLOps community discussion describes a move from founder-led activity to
peer-to-peer participation through sprints, autonomy, and many-to-many
engagement
[[cite:mlops-community-building-and-meetups=>MLOps Community Playbook]].
DevRel can use those habits, but its product responsibility is narrower. DevRel
helps developers adopt the tool and routes technical feedback back to builders
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

When a company turns every community interaction into a campaign, it weakens
trust. When DevRel disconnects from product and engineering, it becomes only
broadcasting.

## Metrics and Product Signals

DevRel teams get more from metrics when they track developer progress, not only
audience size. Community signals and analytics can become a serious analysis
function, while growth tactics still need sustainable strategy
[[cite:devrel-data-science-open-source-tools@26:01=>DevRel community metrics]].
Content goals separate awareness, support, and open-source strategy
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

Useful signals include successful first runs and activated users. DevRel teams
can also track repeated usage and docs issues. They can track unanswered support
questions and contribution flow. Event follow-up and product feedback also matter
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

Vanity metrics can help distribution, but they don't prove adoption by
themselves. A tutorial view or conference talk matters more when it leads to a
working project. A social post matters more when it leads to a clearer issue,
better docs page, or product fix.

Community teams measure a different center of gravity. They track membership
milestones, survey cadence, feedback cadence, and member connections
[[cite:mlops-community-building-and-meetups=>MLOps Community Playbook]].
DevRel can borrow those signals, but it still needs product-facing signals that
tell engineering where developers get stuck.

## Boundaries with Marketing and Events

DevRel and marketing both care about reaching developers through SEO and content
strategy
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
DevRel has to protect credibility. Practitioners should be able to reproduce the
demo, look at the code, and connect what they learned to real work.

The evangelism side covers AI evangelism, positioning, and messaging strategy,
including clear takeaways and calls to action
[[cite:public-speaking-for-data-scientists=>Public Speaking for Data Scientists]].
DevRel can use that skill, but it doesn't replace technical feedback from
developers who try the tool.

DevRel teams should treat conference work as useful developer education, not
only awareness. Ben Taylor recommends proposing talks with novelty and enough
ambition to stretch the speaker. Speakers can then build a speaker resume from
smaller venues toward keynotes
[[cite:public-speaking-for-data-scientists@50:20=>Conference proposals]]
[[cite:public-speaking-for-data-scientists@53:48=>Speaker resume]].
[[data-ai-conference-building=>Data and AI conference building]] covers full
event work around speaker selection, sponsor fit, pricing, and networking.

Swyx draws the same boundary: reusable talks support communication practice and
technical-judgment distribution. DevRel still has to connect the talk back to
docs, demos, support, and product feedback
[[cite:developer-personal-brand-learn-in-public@59:04=>Reusable talks]].

## Related Pages

These pages cover the practices DevRel depends on.

- [[Open Source and Developer Relations]] for maintainers, governance,
  contribution paths, and open-source business models.
- [[Developer Experience]] for adoption friction, onboarding, and usability for
  technical users.
- [[Documentation]] and [[Technical Writing]] for tutorials, guides, and
  decision records.
- [[Community Building]] and [[Community]] for membership, moderation, events,
  and peer-to-peer participation.
- [[Open Source]] and [[Contributing]] for project stewardship and contribution
  paths.
