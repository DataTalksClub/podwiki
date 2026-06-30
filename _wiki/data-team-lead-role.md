---
layout: wiki
title: "Data Team Lead Role"
summary: "Podcast-backed definition of the data team lead and head of data role: hiring order, team design, stakeholder adoption, quality standards, trust repair, and leadership boundaries."
related:
  - Data Teams
  - Leadership
  - Team Building
  - Data Strategy
  - Data Engineering Platforms
  - Data Product Management
  - Data Quality and Observability
  - Data Scientist Role
  - Data Engineer Role
---

A data team lead turns data work into an operating system for the organization.
The role isn't just senior analysis or senior engineering. In the
DataTalks.Club interviews, it covers hiring order and delivery priorities. It
also covers quality standards and stakeholder adoption. Team model choices
belong there too.

[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) gives the most
concrete early-team version. As Chief of Data, she starts with business health
monitoring and dashboards. She then grows the team toward warehouse work,
forecasting, and governance repairs. dbt tests and adoption workshops follow
([building data team episode at 4:07-50:52]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Lisa Cohen]({{ '/people/lisacohen/' | relative_url }}) gives the org-design
version. Her discussion compares centralized, decentralized, and hybrid data
science teams. She then ties structure to OKRs, cross-functional rituals,
staffing, and experimentation. Product partnership sits in the same structure
([data science org design episode at 6:27-55:48]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).

## Common Definition

The common definition is ownership of the team system around data work. A data
team lead decides what the team should do first and which roles are needed.
They also decide how the team works with business partners and what quality bar
makes data trusted. That makes the role a close neighbor of
[Data Teams]({{ '/wiki/data-teams/' | relative_url }}),
[Leadership]({{ '/wiki/leadership/' | relative_url }}), and
[Team Building]({{ '/wiki/team-building/' | relative_url }}).

Tammy's episode shows the operating sequence. The team first makes business
health visible, then streamlines reporting and builds trust with other teams.
As the company needs more, the work moves into predictive projects, warehouse
foundations, and demand forecasting
([building data team episode at 7:22-29:20]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

The same role has to choose people, not only projects. Tammy describes hiring
an analyst first, then a data engineer. Later she revisits that order and says
senior hires can matter earlier because early decisions create long-lived
patterns
([building data team episode at 15:04-26:26]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Marco De Sa]({{ '/people/marcodesa/' | relative_url }}) gives the executive
version in his chief data officer discussion. That role works backward from
business goals into strategy, KPIs, and accountability. Org design, governance,
and data culture belong there too
([CDO episode at 6:08-34:43]({{ '/podcasts/chief-data-officer-data-strategy-and-org-design/' | relative_url }})).
A head of data may be more operating-level than a CDO, but both roles turn
company goals into a data operating model.

## Guest Differences

Guests differ on the reporting model. Cohen separates centralized teams from
embedded teams because each model protects a different thing. Central teams
protect craft standards and career support. Teams embed data people to gain
domain context and faster product decisions. Hybrid models try to keep both
benefits
([data science org design episode at 6:27-30:52]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).

Tammy's episode puts less emphasis on reporting lines and more emphasis on
business trust. Her team has to overcome spreadsheet habits and data accuracy
issues. Dashboard skepticism has to be handled before more advanced work can
land
([building data team episode at 8:51-12:00 and 35:38-41:42]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Katie Bauer]({{ '/people/katiebauer/' | relative_url }}) adds a manager's
view from B2B SaaS. Her episode connects data science management to matrix
work, mentorship, documentation, and stakeholder expectations. Career systems
belong in the same management work
([data science team management episode]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).
That version makes people development more explicit than the early-team buildout.

[Barbara Sobkowiak]({{ '/people/barbarasobkowiak/' | relative_url }}) separates
manager and expert paths. Her discussion says a manager needs strategy, team
development, stakeholder work, and prioritization. Impact judgment also matters,
while a deep expert role can remain separate in larger organizations
([manager vs expert episode at 4:58-50:12]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }})).
Startups soften that boundary because one senior generalist may need to cover
both management and expert judgment.

## Quality, Trust, and Adoption

The team lead owns the conditions that let people trust the team's work.
Tammy's trust-repair discussion covers data accuracy, governance, and errors.
Playbooks and dbt tests matter too. Regular dashboard checks matter too. She connects timely
insights to operational visibility and campaign monitoring
([building data team episode at 35:38-41:42]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

That work links directly to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).
A team lead can't treat adoption as something that happens after delivery.
Tammy describes workshops and Q&A sessions as part of leadership. Delegation,
ownership, and team empowerment belong there too
([building data team episode at 47:08-56:19]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) gives the
last-mile version of the same point. Analytics outputs need discoverability,
interpretability, trust, and a place in the actual decision workflow
([last-mile data delivery episode]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).
The data team lead has to make those adoption loops part of delivery.

## Planning and Role Boundaries

The role boundary changes as the team grows. In an early company, the lead may
write SQL, repair dashboards, and interview stakeholders. They may also manage
vendor choices.

Tammy's stack discussion includes Stitch, GCP, and dbt, while Data Studio and a
Notion wiki also appear. That stack supports reporting and forecasting while
the team is still small
([building data team episode at 22:32]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

At larger scale, Cohen's version moves toward org design through OKRs and
cross-functional ceremonies. Dependency management and staffing ratios sit in
the same planning layer. Product partnership belongs in that layer as well
([data science org design episode at 18:43-47:20]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).
That makes the lead responsible for how data scientists and engineers work with
product managers. Designers and analysts belong in that operating model too.

[Tereza Iofciu]({{ '/people/terezaiofciu/' | relative_url }}) adds the
leadership-transition view. Moving from IC to lead changes the work from direct
execution to feedback culture, visibility, and product mindset. KPIs and
influence without authority matter too. Stakeholder framing and empathy matter
as well
([data leadership coaching episode at 6:17-50:23]({{ '/podcasts/data-leadership-coaching/' | relative_url }})).

The boundary with a
[data architect]({{ '/wiki/data-architect-role/' | relative_url }}) is that the
architect owns durable system structure. The data team lead owns the people,
priorities, and operating habits that make the architecture useful. In small
teams, one person may hold both responsibilities.

## Related Pages

These pages cover adjacent roles, operating concerns, and team systems.

- [Data Teams]({{ '/wiki/data-teams/' | relative_url }})
- [Leadership]({{ '/wiki/leadership/' | relative_url }})
- [Team Building]({{ '/wiki/team-building/' | relative_url }})
- [Data Strategy]({{ '/wiki/data-strategy/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
