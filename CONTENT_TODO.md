# Podwiki Content TODO

This backlog captures page categories that should become repeatable content
families. Use it when planning new wiki pages, guides, comparisons, roadmaps,
how-tos, or podcast summaries.

## Category Rules

Follow these rules when adding any page from this backlog.

- Keep `_wiki/` pages as podcast-grounded reference pages with inline episode
  references, tradeoffs, and related pages.
- Put keyword-targeted editorial pages in `_wiki/` with a type tag such as
  `guide`, `comparison`, `roadmap`, `transition`, or `how-to`. If the page is
  only the bare concept, keep it untagged. Public URLs are `/wiki/<slug>/`.
- Keep `_podcast_summaries/` compact enough for agents to decide whether they
  need the source episode.
- Link podcast evidence to canonical episode pages such as
  `https://datatalks.club/podcast/<source-file-slug>.html`. Do not link
  public-page evidence to the generic podcast archive page.
- Run `make check` after adding pages so graph and search stay current.
- For edited public pages, run the content audit with
  `--strict-scaffold-headings --paths <files...>` so old template headings do
  not reappear on new work.

## Current Rewrite Requirements

These notes capture the current cleanup direction and should not be lost.

- Rewrite wiki pages to use compact citation markers for routine evidence:
  `[[cite:<podcast-slug>=>Episode Label]]`. Use a timestamp only when a precise
  clip helps verification:
  `[[cite:<podcast-slug>@MM:SS=>Episode Label]]`. Use two-digit `MM:SS` only;
  do not use `M:SS` or `H:MM:SS`. For clips after one hour, convert to total
  minutes, for example `1:03:12` becomes `63:12`. Keep visible
  `[[podcast:...]]` chips for navigation lists or sentences where the episode is
  itself the object being discussed. Avoid `|` inside citation, podcast, person,
  book, and wiki chips because Markdown can render adjacent pipe chips as
  accidental tables.
- Redo wiki pages to follow one structure: opening definition, topic-specific
  sections, concrete differences in how guests apply the topic, inline podcast
  references, and related pages. Do not expose scaffolding headings such as
  `Common Definition`, `Guest Differences`, or `Guest Tradeoffs`; use headings
  that describe the actual subject.
- Remove public meta sections from wiki and editorial pages. Do not use
  `Contents`, `Search Intent`, `Archive Evidence`, `Episode Evidence`, `Guest
  Descriptions`, `Recurring Archive Themes`, `Maintenance Notes`, or `Agent
  Maintenance Notes` as reader-facing headings. Do not use generic guest
  scaffolding such as `Common Definition`, `Guest Differences`, `Guest
  Tradeoffs`, `Guest Disagreements`, or `Guest Emphasis`. Do not add visible
  `Link Map` sections; spread those links through the article body and
  `Related Pages`.
- Ground each substantive section in actual podcast discussions. Put the
  podcast reference next to the claim it supports, like a citation, instead of
  collecting evidence in a separate appendix.
- Make every page link-heavy: visible links to specific podcast interviews,
  related wiki pages, category pages, and the grounding evidence behind
  substantive claims. Person links are optional and should point to the
  canonical main-site profile when they help the reader.
- Use canonical podcast links such as
  `https://datatalks.club/podcast/<source-file-slug>.html` whenever the source
  episode slug is known.
- Make related links visually obvious in CSS. Related pages should look like
  links, not muted tags.
- Keep the graph-driven "See Also in the Graph" section on wiki, editorial,
  and podcast summary pages. It is rendered from `graph/graph.json` by
  `assets/page-graph.js`, so Markdown links remain the source of truth.
- `_podcast_summaries/` are source-derived agent records, not public podcast
  pages. Public links should point to the main DataTalks.Club episode pages.
- Treat Markdown pages as the source for the graph. Do not maintain
  `graph/graph.json` separately; regenerate it from the collections.
  Internally, graph nodes may still call guides, comparisons, roadmaps, and
  how-tos article/content nodes; do not expose that as a public category.
- Keep `make sources` as the first step for broad podcast work. It syncs
  source-derived podcast/person registries, chapter summaries, and the source
  index used by subagents.
- Use `sources/podcast-topic-inventory.md` as the durable topic map from the
  five-agent archive pass. Extend it when a new archive-wide discovery pass finds
  a recurring grounded topic.
- For broad topic discovery, keep five subagents running on non-overlapping
  podcast batches and collect grounded topic reports before writing pages.
- Keep MLOps and DataOps as separate concept pages. Use `_wiki/mlops.md` for
  model lifecycle operations, `_wiki/dataops.md` for data delivery operations,
  and `_wiki/mlops-vs-dataops.md` for the comparison.
- Keep pages centered on one topic, role, transition, comparison, roadmap, or
  project type. Split mixed pages instead of broadening them.
- Name concept pages by the concept, not by "What is ..." phrasing. Use
  `Open Source`, `MLOps`, or `DataOps` as page names; keep "what is" only as a
  keyword variant in frontmatter or audit notes.
- Keep stub pages temporary. A stub may exist only to satisfy an existing link,
  must use `stub: true`, must point to an existing hub page, and should be
  replaced with podcast-grounded synthesis when the topic becomes important.

## Link and Graph Enrichment Backlog

The 2026-07-06 five-agent page-quality pass found no new grounded keyword gaps
from the Ubersuggest CSV. The current work should enrich existing canonical
pages, not create duplicate keyword pages.

Completed from this batch:

- `_wiki/delta-lake-vs-apache-iceberg.md`: enriched with lakehouse,
  governance, staging, DataOps checks, and catalog context.
- `_wiki/llm-deployment.md`: enriched with production ownership, latency, cost,
  evaluation gates, agent services, infrastructure ownership, and feedback
  evidence.
- `_wiki/evaluation.md`: enriched as a routing hub for LLM evaluation, RAG
  evaluation, production search evaluation, search relevance, agent evaluation,
  experiment checks, and human review.
- `_wiki/data-product-manager.md`: strengthen the role guide with discovery,
  roadmap ownership, adoption, platform PM work, and product-boundary evidence
  from `product-designer-to-data-product-manager`,
  `building-and-scaling-ai-data-products-with-mlops`,
  `last-mile-data-delivery-and-data-product-adoption-modern-data-stack`,
  and `ml-product-manager-and-mlops-platform-strategy`.
- `_wiki/machine-learning-engineer-roadmap.md`: strengthen production
  ownership, system design, platform habits, reproducibility, and monitoring
  from `machine-learning-engineering-production-best-practices`,
  `building-scalable-and-reliable-machine-learning-systems`,
  `building-production-ml-platform-and-mlops-team`, and
  `human-centered-mlops-and-model-monitoring`.
- `_wiki/llm-rag-production-roadmap.md`: strengthen RAG, search evaluation,
  agents, security, cost, deployment, and infrastructure stages from
  `practical-llm-engineering-and-rag`,
  `building-agentic-ai-engineering-tooling-retrieval-evaluation`,
  `production-ready-ai-engineering`, `generative-ai-chatbots-in-production-security`,
  and `ai-infrastructure-hybrid-cloud-on-prem-distributed-training`.
- `_wiki/graph-data-science.md`: separate graph analytics, knowledge graphs,
  graph retrieval, and vector retrieval using
  `knowledge-graphs-and-llms-for-automotive-rnd`,
  `bioinformatics-worflows-tools-and-data-science`,
  `modern-search-systems-vector-databases-llms-semantic-retrieval`, and
  adjacent vector/search pages.

The five-page enrichment batch is complete. Future batches should start from
the content-quality audit, keyword gaps, or graph-link audit rather than
rewriting these same pages again.

The 2026-07-06 DataOps/MLOps borderline SEO cluster was tightened so it stays
distinct from the main-site DataOps definition pages:

- `_wiki/dataops-tools.md`: focused on tool-category decisions across version
  control, CI/CD, orchestration, tests, observability, lineage, deployment, and
  recovery.
- `_wiki/dataops-platforms.md`: focused on shared platform surfaces, release
  services, self-service guardrails, observability, governance, access,
  ownership, and adoption; removed the untagged `keyword:` field to avoid
  head-term cannibalization.
- `_wiki/dataops-engineer-role.md`: focused on role accountability,
  support/onboarding, release/recovery, incident handoffs, and nearby-role
  boundaries.
- `_wiki/dataops-checks-for-data-pipelines.md`: focused on concrete pipeline
  checks, runtime placement, blocking behavior, responders, CI/CD gates,
  observability, lineage, and recovery.
- `_wiki/mlops-vs-dataops.md`: focused on model lifecycle versus data delivery
  ownership, monitoring boundaries, platform boundaries, and incident handoffs.

The `docs/mining/report_pod_03.md` high-value missing-edge batch was integrated
on 2026-07-05:

- healthcare, biohacking, and domestic-risk evidence now strengthens
  personalization, career-development, team-lead, privacy, responsible-AI,
  entity-resolution, monitoring, adoption, and portfolio pages
- cloud-governance, leadership-coaching, data-science leadership, and B2B SaaS
  team-management evidence now strengthens governance, self-service, team,
  leadership, manager, KPI, hiring, analytics-engineering, and software
  engineering pages
- DataTalks.Club community, staff-AI, radio-astronomy, and hiring evidence now
  strengthens community, teaching, staff-AI, academic-transition,
  data-scientist-role, job-search, scientific tooling, notebook-to-production,
  AI infrastructure, and end-to-end pipeline pages
- human-centered MLOps, decision optimization, finance MLOps, production ML
  pipelines, and AI-engineering evidence now strengthens business ML,
  monitoring, optimization, finance, MLOps, infrastructure, pipelines, LLMOps,
  AI-engineering, RAG, agent, and portfolio pages
- Vincent Warmerdam and Nadia Nahar evidence now strengthens open-source,
  contributor-roadmap, scikit-learn, documentation, OSS portfolio, career,
  software-engineering, MLOps architecture, model-registry, reproducibility, and
  responsible-AI pages

The `docs/mining/report_pod_05.md` high-value missing-edge batch was integrated
on 2026-07-05:

- Will McGugan's open-source-to-startup episode now strengthens founder,
  startups, open-source, DevRel, entrepreneurship, freelance, and OSS portfolio
  evidence pages
- Liesbeth Dingemans, Ranjitha Kulkarni, Alexey Grigorev, Bartosz Mikulski, and
  Aditya Gautam evidence now strengthens AI product, agent engineering, RAG,
  LLM evaluation, AI engineering, prompt-cost, data-quality, and CRISP-DM pages
- Eleni Stamatelou and Daynan Crull evidence now strengthens healthcare ML,
  interpretability, sensor ML, model monitoring, computer vision,
  infrastructure, industrial ML, astroinformatics, annotation, and
  reproducibility pages
- DataTalks.Club scaling, MLOps community-building, Barbara Sobkowiak, Noah
  Gift, Isabella Bicalho, Santiago Valdarrama, and Christoph Molnar evidence now
  strengthens community, manager, KPI, transition, freelancing, open-source,
  bioinformatics, ML engineering, technical-writing, and solopreneur pages

The `docs/mining/report_pod_07.md` high-value missing-edge batch was integrated
on 2026-07-05:

- Marcello La Rocca's algorithms/data-structures episode now strengthens
  information retrieval, vector databases, embeddings, ML-for-SWE, software
  engineering, interview, and competition pages
- Pauline Clavelloux's indie-hacking episode now strengthens the solopreneur
  data-scientist page with a more specific UnrealMe prototype citation
- Elena Samuylova's MLOps startup episode and Loris Marini's SaaS
  business-skills episode now strengthen founder and ML-for-business pages
- Sarah Mestiri's job-search episode now strengthens portfolio-project advice
  around courses versus applied proof
- Theofilos Papapanagiotou, CJ Jenkins, Ben Taylor, and Johanna Bayer evidence
  now strengthens monitoring, notebook-to-production, CV, community,
  communication, and open-source contributor pages
- Two stale `.md.md` podcast-summary redirect records were removed, and the
  matching `source_episode` metadata now points to the canonical source files

The `docs/mining/report_pod_08.md` high-value missing-edge items were integrated
on 2026-07-05:

- Boyan Angelov's data-strategy episode now strengthens `_wiki/data-strategy.md`
- Alexander Guschin's Kaggle Grandmaster episode now strengthens
  `_wiki/competitions-beyond-kaggle.md`
- Vin Vashishta's ML monetization discussion now strengthens
  `_wiki/ml-product-manager-role.md`
- Misra Turp's career-search and portfolio advice now strengthens
  `_wiki/job-search.md` and `_wiki/data-scientist-cv-and-portfolio.md`
- Angela Ramirez's fraud-detection feature and graph examples now strengthen
  `_wiki/feature-stores.md` and `_wiki/knowledge-graph-vs-vector-search.md`

The 2026-07-05 graph audit found no current graph edges dropped because of
missing node ids. When Markdown sources change, regenerate `graph/graph.json`
with `make graph` or `make check`; do not hand-edit it.

Follow-up graph-link maintenance on 2026-07-05 retargeted two stale source
chips that the graph builder had been dropping before node filtering:
`juanluiscano` now points to `juanmanuelperafan`, and the broken
`gpt-3-podcast` citation now points to the existing GPT-3 book node while the
Sandra Kublik podcast citation remains in the page.

The second `docs/mining/report_pod_08.md` enrichment batch was integrated on
2026-07-05:

- Agita Jaunzeme's DevOps-to-data-engineering path now strengthens transition,
  career-fit, open-source DevRel, and DE-vs-DS comparison pages
- Jack Blandin's applied-ML leadership episode now strengthens ML business,
  startup, system-design, business-skill, and communication pages
- Jose Maria Sanchez Salas's remote IoT data-engineering episode now strengthens
  platform, data-product, data-engineering, technical-writing, and roadmap pages
- Elle O'Brien and Will Russell's DevRel/open-source episodes now strengthen
  developer-relations, developer-experience, community-building,
  learning-in-public, and open-source contribution pages
- Barr Moses and Boyan Angelov evidence now strengthens observability,
  governance, DataOps, intake, translator, CDO, and AI productivity pages

The third `docs/mining/report_pod_08.md` enrichment batch was integrated on
2026-07-05:

- Victoria Perez Mola's analytics-engineering episode now strengthens dbt,
  analytics-engineering, AE-vs-analyst, DataOps checks, analytics roadmap, and
  data-observability pages
- Sonal Goyal's identity-resolution episode now strengthens entity-resolution,
  open-source, OSS founder, startup, and customer-data-platform pages
- Jeff Katz's data-engineering career episode now strengthens DE roadmap,
  warehouse, job-search, analyst-to-DE, and teaching pages
- Danny Leybzon's MLOps monitoring episode now strengthens MLOps engineer,
  MLOps tools, model monitoring, lean MLOps, responsible AI, and career pages
- Slawomir Tulski's 2026 data-engineering episode and Eugene Yan's technical
  writing episode now strengthen DE role, DE trends, FinOps, modern stack,
  batch-vs-streaming, technical writing, documentation, portfolio, and
  community pages

The `docs/mining/report_pod_09.md` high-value graph edges were integrated on
2026-07-04:

- weak-supervision and model-in-the-loop annotation evidence from Hotter's
  Refinery/Bricks discussion and Weber's Alexa NLU work now strengthens
  `_wiki/annotation-quality-workflows.md`
- freelance and consulting evidence from
  `from-startup-engineering-to-freelance-data-science` and
  `practical-generative-ai-consulting` now strengthens the freelance,
  consulting proposal, and consulting-to-product-founder pages
- Shtylenko's industrial maturity model now strengthens MLOps adoption,
  data-team, CDO, and industrial ML pages
- theme-park recommender validation now strengthens A/B testing,
  data-product adoption, recommendation systems, streaming, and AI
  infrastructure pages
- the Kaggle portfolio and mentoring-in-tech edges now strengthen career,
  portfolio, interview, and leadership pages

`docs/mining/report_pod_10.md` was the last broad missing-edge audit source and
is now fully integrated. Future missing-edge work should start from a fresh
mining report or a new graph/link audit, not by reopening `report_pod_10.md`.
These are page-enrichment tasks, not new-page requests. Keep using
`data-team-roles` as foundational role-taxonomy evidence when tightening
role-boundary pages.

The first `docs/mining/report_pod_10.md` enrichment batch was integrated on
2026-07-04:

- applied LLM research, long-context evaluation, RAG fallback, industry
  publishing, Kaggle dataset work, portfolio strategy, career transitions, and
  interview prep now strengthen the relevant LLM, research, portfolio, and
  career pages
- data-team scaling and last-mile delivery now strengthen team-building, data
  quality, adoption, product-management, intake, metrics, team, and project
  management pages
- production ML platform evidence now strengthens MLOps, platform engineering,
  platform architecture, experiment tracking, model registry, serving,
  developer experience, governance, lean MLOps, and monitoring pages
- modern-data-stack evidence now strengthens ETL/ELT, analytics engineering,
  warehouse, lake, CDC, reverse ETL, modern stack, data-engineer role, and open
  source pages
- fairness, responsible-AI, privacy, monitoring, security, contribution, and
  scikit-learn evidence now strengthens the responsible-AI cluster

The second `docs/mining/report_pod_10.md` enrichment batch was integrated on
2026-07-05:

- data-science ABC roles, standout career advice, and mentoring-in-tech
  evidence now strengthen role, career, portfolio, team, and mentoring pages
- data-translator strategy evidence now strengthens translator, trust,
  data-led growth, strategy, production handoff, communication, business-skill,
  and data-team pages
- IoT/data-architect and modern-data-engineering evidence now strengthens data
  architecture, lakehouse, warehouse, pipeline, platform, trend, table-format,
  DuckDB, dbt, orchestration, streaming, roadmap, and DevOps-to-DE pages
- production chatbot security evidence now strengthens red-team, prompt
  injection, security, LLM production, adoption, annotation, prompt engineering,
  NLP, and AI engineering pages
- search/RAG, practical LLM engineering, and conference-building evidence now
  strengthens search, retrieval, evaluation, RAG projects, LLM tooling, context,
  agents, LLMOps, AI coding, feedback, freelance/DevRel, conference,
  community, AI-engineer role, AgentOps, and sensor-ML pages

The residual `docs/mining/report_pod_10.md` enrichment pass was integrated on
2026-07-05:

- mentoring-in-tech, career-development, career-growth, and communication pages
  now cite more precise community, mentoring, and stakeholder-communication
  clips
- data-engineering-tools and modern-data-stack pages now cover dlt as
  library-first ingestion and reusable data-product packaging
- data-trust-and-strategy now includes dashboard-quality repair, dbt checks, and
  operational-input consistency from the scaling-data-team episode
- responsible-AI, privacy-engineering-for-ML, and model-monitoring pages now
  include regulated ML platform logging, metadata, lineage, and artifact
  storage tradeoffs
- job-description and machine-learning-engineer-role pages now cover forward
  deployed engineering as an adjacent client-facing boundary without creating a
  standalone role page

All mined `report_pod_10.md` sections have now been integrated as enrichment.
For the next broad podcast-mining pass, create or use the next numbered mining
report and keep the same no-new-page default unless a keyword brief or repeated
archive evidence justifies a new hub.

The 2026-07-05 keyword-backed enrichment follow-up strengthened existing pages
instead of creating duplicate content:

- MLOps framework and architecture intent now strengthens
  `_wiki/mlops-architecture.md` and `_wiki/mlops-engineer.md`
- DataOps platform and data-pipeline-training intent now strengthens
  `_wiki/dataops-platforms.md` and `_wiki/how-to-build-data-pipelines.md`
- data-engineer recruiter, manager-job-description, and analyst-take-home
  intent now strengthens `_wiki/hire-data-engineers.md`,
  `_wiki/data-engineering-manager-role.md`, and
  `_wiki/data-analyst-careers.md`
- data-engineering certification and no-experience roadmap intent now
  strengthens `_wiki/data-engineering-certification.md` and
  `_wiki/how-to-become-a-data-engineer-with-no-experience.md`
- product-analyst-projects, analytics-engineering-roadmap, and
  data-team-building intent now strengthens `_wiki/product-analyst.md`,
  `_wiki/analytics-engineering-roadmap.md`, and `_wiki/team-building.md`

## Roles

Create role pages that explain the work, the boundary with nearby roles, and the
skills that show up in the archive. Each page should name the episodes that
support the claims.

When a role page links to people, use them as sources for what they said in the
podcast archive. Keep biographies secondary.

Existing pages:

- `_wiki/analytics-engineering.md`
- `_wiki/ai-engineer-role.md`
- `_wiki/data-analyst-role.md`
- `_wiki/data-engineer-role.md`
- `_wiki/data-product-management.md`
- `_wiki/data-scientist-role.md`
- `_wiki/data-team-lead-role.md`
- `_wiki/data-architect-role.md`
- `_wiki/machine-learning-engineer-role.md`
- `_wiki/ml-platform-engineer-role.md`
- `_wiki/mlops-engineer.md`
- `_wiki/chief-data-officer-role.md`
- `_wiki/dataops-engineer-role.md`
- `_wiki/analytics-engineering.md` owns the Analytics Engineer role vocabulary.
- `_wiki/data-roles.md`
- `_wiki/data-product-manager.md`
- `_wiki/data-scientist-role.md`
- `_wiki/product-analyst.md`
- `_wiki/developer-relations.md` owns the Developer Advocate / DevRel Engineer
  role vocabulary unless a future keyword brief needs a separate role page.

Candidate pages:

- Improve existing analytics engineer and data product manager pages as new
  interviews add evidence. Do not create duplicate role pages for the same
  keyword family.

Source hints:

- `data-engineering-career-path-and-skills.md`
- `big-data-engineer-vs-data-scientist.md`
- `analytics-engineer-skills-tools.md`
- `s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.md`
- `devrel-open-source-machine-learning.md`
- `building-production-ml-platform-and-mlops-team.md`

## Career Transitions

Create reusable pages for common moves from one background into another data or
AI role.

Each page should cover the same core pieces:

- transferable skills
- missing skills
- portfolio evidence
- first job targets
- relevant guest examples

Existing pages:

- `_wiki/solopreneur.md`
- `_wiki/career-transitions-in-data.md`
- `_wiki/how-to-build-data-pipelines.md` owns the procedural pipeline
  build page. Keep `_wiki/end-to-end-data-pipeline-project.md` as the canonical
  portfolio-ready pipeline blueprint.
- `_wiki/data-engineer-roadmap.md` owns the main data engineer roadmap.
- `_wiki/software-engineer-to-machine-learning.md` owns the transition page.
  `_wiki/machine-learning-for-software-engineers.md` owns the software
  engineer audience guide.
- `_wiki/data-scientist-to-data-engineer.md`
- `_wiki/data-analyst-to-data-engineer.md`
- `_wiki/academic-researcher-to-data-science.md`
- `_wiki/devops-to-data-engineering.md`
- `_wiki/marketing-to-analytics-engineering.md`
- `_wiki/product-designer-to-data-product-manager.md`
- `_wiki/qa-to-ml-and-data-engineering.md`
- `_wiki/data-scientist-to-machine-learning-engineer.md`
- `_wiki/software-engineer-to-machine-learning.md`
- `_wiki/data-analyst-to-analytics-engineer.md`
- `_wiki/consultant-or-freelancer-to-data-product-founder.md`
- `_wiki/project-manager-to-data-science.md`

Candidate pages:

- Improve existing transition pages as new episodes add evidence.

Source hints:

- `from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`
- `how-to-transition-into-ml-and-data-engineering-from-qa.md`
- `postdoc-to-data-science-lead-career-transition.md`
- `from-software-engineering-data-science-to-data-engineering-leadership.md`
- `product-designer-to-data-product-manager.md`
- `becoming-data-freelancer.md`

## Portfolio Projects

Create pages that help learners choose projects that prove real skills, not
only tutorial completion. These pages should connect project ideas to
episode-backed expectations around hiring, open source, production readiness,
and role-specific portfolios.

Existing pages:

- `_wiki/portfolio-projects.md`
- `_wiki/data-scientist-interview.md`
- `_wiki/open-source-and-developer-relations.md`
- `_wiki/data-engineering-portfolio-projects.md`
- `_wiki/machine-learning-portfolio-projects.md`
- `_wiki/analytics-engineering-portfolio-projects.md`
- `_wiki/rag-portfolio-projects.md`
- `_wiki/open-source-portfolio-evidence.md`
- `_wiki/end-to-end-data-pipeline-project.md`
- `_wiki/production-ml-project-checklist.md`
- `_wiki/search-and-rag-project-checklist.md`
- `_wiki/dashboard-and-metric-layer-project-checklist.md`
- `_wiki/volunteer-data-engineering-projects.md`

Candidate pages:

- Improve the published project-checklist pages as new interviews add evidence.

Source hints:

- `data-science-interview-and-cv-guide.md`
- `get-data-scientist-job.md`
- `open-source-ml-contributions.md`
- `developer-personal-brand-learn-in-public.md`
- `building-scalable-and-reliable-machine-learning-systems.md`
- `modern-search-systems-vector-databases-llms-semantic-retrieval.md`

## How-Tos

Create how-to pages for procedural workflows where readers need an operating
sequence rather than a concept definition. Each page should show when to use the
workflow, the steps, the tradeoffs, and the podcast evidence behind the
recommendation.

Existing how-to pages:

- `_wiki/how-to-build-data-pipelines.md`
- `_wiki/dataops-checks-for-data-pipelines.md`
- `_wiki/notebook-to-production-workflow.md`
- `_wiki/rag-evaluation-workflow.md`

Supporting concept pages:

- `_wiki/apache-airflow.md`
- `_wiki/orchestration.md`

Candidate pages:

- Add new how-tos only when the keyword or podcast evidence asks for a concrete
  procedure. Keep bare concepts in `_wiki/`.

Source hints:

- `modern-data-pipelines-orchestration-ingestion-modeling.md`
- `dataops-automation-and-reliable-data-pipelines.md`
- `data-engineering-career-path-and-skills.md`
- `s24e03-from-notebook-to-production-building-end-to-end-ai-systems.md`

## Roadmaps

Create roadmap pages that explain learning sequence, project sequence, role
milestones, and when to stop studying and build. These should be
podcast-grounded, not generic course lists.

Existing roadmap-tagged pages:

- `_wiki/data-engineer-roadmap.md`
- `_wiki/how-to-become-a-data-engineer-with-no-experience.md`
- `_wiki/analytics-engineering-roadmap.md`
- `_wiki/ai-engineering-roadmap.md`
- `_wiki/mlops-roadmap.md`
- `_wiki/data-scientist-interview-roadmap.md`
- `_wiki/machine-learning-engineer-roadmap.md`
- `_wiki/data-product-manager-roadmap.md`
- `_wiki/open-source-contributor-roadmap.md`
- `_wiki/llm-rag-production-roadmap.md`
- `_wiki/data-analyst-to-analytics-engineer.md`
- `_wiki/data-analyst-to-data-engineer.md`
- `_wiki/data-scientist-to-data-engineer.md`
- `_wiki/lean-mlops-for-startups.md`

Supporting pages:

- `_wiki/machine-learning-system-design.md`
- `_wiki/llm-production-patterns.md`
- `_wiki/search-and-rag-project-checklist.md`
- `_wiki/dataops-platforms.md`

Candidate pages:

- Improve existing roadmap pages as new episodes add evidence.

Source hints:

- `data-engineering-career-path-and-skills.md`
- `how-to-grow-your-ml-engineering-career.md`
- `s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.md`
- `machine-learning-system-design-interview.md`
- `mlops-at-scale-reproducibility-adoption.md`

## X vs Y

Create comparison pages for high-intent queries where readers need concrete
comparison outcomes:

- a decision
- a role boundary
- an architecture tradeoff
- a vocabulary clarification

Existing pages:

- `_wiki/data-engineer-vs-data-scientist.md`
- `_wiki/data-analyst-vs-analytics-engineer.md`
- `_wiki/data-product-manager-vs-product-manager.md`
- `_wiki/data-product-owner-vs-data-product-manager.md`
- `_wiki/dataops-vs-data-engineering.md`
- `_wiki/data-warehouse-vs-data-lakehouse.md`
- `_wiki/batch-vs-streaming.md`
- `_wiki/data-mesh-vs-centralized-data-platform.md`
- `_wiki/delta-lake-vs-apache-iceberg.md`
- `_wiki/etl-vs-elt.md`
- `_wiki/graph-rag-vs-vector-rag.md`
- `_wiki/knowledge-graph-vs-vector-search.md`
- `_wiki/machine-learning-engineer-vs-data-scientist.md`
- `_wiki/mlops-vs-dataops.md`
- `_wiki/mlops-vs-devops.md`
- `_wiki/product-analyst-vs-data-analyst.md`
- `_wiki/product-owner-vs-product-manager.md`
- `_wiki/rag-vs-fine-tuning.md`
- `_wiki/vector-database-vs-search-engine.md`

Candidate pages:

- Improve existing comparison pages as new interviews add evidence.
- Remaining real comparison pages were normalized into tagged `_wiki/` pages
  on 2026-07-01. There are no redirect pages; incoming links should point
  directly to the canonical `_wiki/<slug>.md` file.
- No known `X vs Y` migration candidates remain in `_wiki/`.
- Keep `_wiki/data-engineer-vs-data-scientist.md` as the canonical
  comparison page. Put role and concept material in `_wiki/data-engineer-role.md`
  and `_wiki/data-scientist-role.md`, not in a duplicate wiki comparison page.

Source hints:

- `big-data-engineer-vs-data-scientist.md`
- `analytics-engineer-skills-tools.md`
- `building-data-products-product-owner-vs-product-manager.md`
- `data-engineering-tools-modern-data-stack.md`
- `data-mesh-architecture-decentralized-data-products.md`
- `production-ml-search-vector-search-embeddings-hybrid-search.md`

## Next Batch

- The 2026-07-05 source-coverage audit confirmed that podcast and people
  registries are synced: 202 source episodes, 202 `_podcast_summaries/`
  records, 438 source people, and 438 `_people/` records, with no slug diffs.
  The first summary-quality batch is complete: the 15 episode summaries whose
  source-index prose summary is empty now have compact `Agent Summary` guidance
  with why-it-matters, useful-for, and probably-skip-if bullets, and the
  placeholder `Transcript checkpoint` chapter labels were removed from
  `data-team-roles`, `crisp-dm`, and `s22e07-reinventing-career-in-tech`.
  `scripts/audit_podcast_summaries.py` now checks these invariants.
- The 2026-07-04 five-agent enrichment pass has been handled through the three
  `report_pod_10.md` batches above. Future work should use a fresh mining
  report or new source evidence rather than reopening the same pending list.
- The remaining 2026-07-04 keyword candidates were handled on 2026-07-05:
  `_wiki/apache-airflow.md` was tightened for Docker/local workflow intent while
  keeping the main-site Docker Compose article canonical; existing
  `_wiki/machine-learning-vs-software-engineering.md` was enriched as the
  comparison page; `_wiki/project-manager-to-data-science.md` was created as a
  transition page; and `_wiki/volunteer-data-engineering-projects.md` was
  created as a narrow guide for reviewed volunteer/nonprofit/open-source data
  engineering portfolio evidence.
- The 2026-07-03 recent-topic gap audit verified and quality-audited the v1
  recent-topic gap pages: `_wiki/context-engineering.md`,
  `_wiki/ai-coding-tools.md`, `_wiki/llmops.md`, `_wiki/agent-ops.md`,
  `_wiki/model-optimization.md`, `_wiki/autonomous-driving-ai.md`, and
  `_wiki/multimodal-llms.md`. Do not recreate these pages from the stale
  `.tmp/topic-gap-analysis.md` report. Future work should add narrower subpages
  only when a new keyword or recurring podcast theme supports them.
- The 2026-07-05 recent-topic v2 gap audit verified and tightened the wider
  gap pages: `_wiki/ai-for-social-good.md`, `_wiki/graph-data-science.md`,
  `_wiki/synthetic-data.md`, `_wiki/text-to-sql.md`, and
  `_wiki/simulation-and-digital-twins.md`. The lower-priority NLP and
  leadership items are already handled as sections in `_wiki/nlp.md` and
  `_wiki/leadership.md`. Do not recreate those pages from the stale
  `.tmp/topic-gap-analysis-v2.md` report.
- Resolve the 689-row content gaps export. The local file
  `.tmp/next-actions-done-datatalks.club.xlsx` currently has the expected tabs
  but only header rows, so replace it with the populated export before creating
  gap-driven pages.
- The 2026-07-01 five-agent audit reconfirmed that the local workbook has only
  header rows. Keep using the CSV-backed audit until the populated workbook is
  available.
- The strongest CSV-backed content candidates from the earlier audit are now
  covered by `_wiki/machine-learning-for-business.md`,
  `_wiki/data-science-project-management.md`, and
  `_wiki/algorithmic-trading.md`. Future work should extend those pages only
  when new podcast evidence or a distinct keyword cluster appears; do not create
  pages for book/PDF/download, Slack, or generic navigation queries.
- The 2026-07-01 five-agent keyword-gap batch strengthened
  `_wiki/data-engineer-roadmap.md`,
  `_wiki/freelance.md`,
  `_wiki/data-science-for-managers.md`, and
  `_wiki/ai-powered-business-intelligence.md`, and improved
  `_wiki/machine-learning-for-startups.md`. Future work should extend these
  pages with new episode evidence instead of creating duplicates.
- The 2026-07-01 follow-up keyword-gap batch added
  `_wiki/data-engineering-and-data-science.md`,
  `_wiki/data-engineering-manager-role.md`,
  `_wiki/machine-learning-personalization.md`, and
  `_wiki/search-relevance.md`, and improved
  `_wiki/machine-learning-for-software-engineers.md`. Future work should
  extend these pages rather than adding duplicate pages for the same keyword
  families.
- The 2026-07-01 keyword-alias improvement batch strengthened
  `_wiki/data-engineer-roadmap.md`,
  `_wiki/freelance.md`,
  `_wiki/data-science-recruiter.md`,
  `_wiki/machine-learning-for-software-engineers.md`, and
  `_wiki/dataops.md` for existing Ubersuggest variants. Future work should
  extend these pages instead of creating duplicate pages for those variants.
- The 2026-07-01 six-page quality batch strengthened
  `_wiki/machine-learning-for-business.md`,
  `_wiki/data-science-project-management.md`,
  `_wiki/algorithmic-trading.md`,
  `_wiki/notebook-to-production-ai-systems.md`,
  `_wiki/dataops-checks-for-data-pipelines.md`, and
  `_wiki/rag-evaluation-workflow.md`. Future work should add fresh podcast
  evidence or narrow subpages only when a new keyword cluster has distinct
  intent.
- Keep improving `_wiki/` when a keyword cluster asks for a concrete
  operating sequence. The notebook-to-production, DataOps checks, and RAG
  evaluation workflows were strengthened on 2026-07-01; future how-tos should
  cover distinct procedures or add new podcast evidence to those canonical
  pages.
- The 2026-07-05 five-agent keyword audit found no new standalone page targets
  from the current local files. Its existing-page enrichment targets were
  strengthened in the 2026-07-05 keyword-backed follow-up above. Residual
  variants such as `mlops frameworks`, `data ops platform`,
  `data pipeline training`, `data engineer recruiter`, analyst take-home
  assignments, manager job descriptions, and product analyst projects should
  continue to strengthen those canonical pages, not create duplicates.
- A 2026-07-05 `scripts/keyword_gap.py` rerun on
  `.tmp/ubersuggest_Current_Queries.csv` found 0 grounded new-page clusters.
  Treat the current CSV as a maintenance/enrichment source until a new keyword
  file or populated 689-row workbook appears.
- The same 2026-07-05 graph audit found no dropped graph links and no dangling
  endpoints. The earlier seven zero-inbound wiki nodes were resolved through
  adjacent hub links; the generated graph now reports no zero-inbound public
  wiki/content nodes.
- Do not prioritize people-page cleanup. People documents are node records for
  canonical main-site profiles, not public content targets. When a
  guest contribution matters, add it to the relevant wiki, guide, comparison,
  roadmap, transition, or how-to page with an inline podcast citation.
- Improve the published transition pages for marketing to analytics
  engineering, QA to ML/data engineering, academic researcher to data science,
  product designer to data product manager, and data scientist to machine
  learning engineer as the source archive grows.
  These five pages were realigned to the current grounded wiki structure on
  2026-07-01; future work should add new episode evidence rather than rewrite
  the same structure again.
- Keep portfolio project coverage connected through `_wiki/portfolio-projects.md`.
  Existing pages cover data engineering, analytics engineering, machine
  learning, RAG, open-source evidence, and project checklists. Improve those
  pages as new podcast evidence appears instead of creating duplicate portfolio
  pages.
  The hub and five role-specific portfolio pages were realigned to the current
  grounded wiki structure on 2026-07-01.
- Improve roadmap pages for data engineering, AI engineering, MLOps, analytics
  engineering, machine learning engineering, data product management, open
  source contribution, and LLM/RAG production as the archive grows.
- Improve the existing comparison pages for data analyst vs analytics engineer
  and RAG vs fine-tuning when new podcast evidence appears.
- Continue improving real `X vs Y` decision pages in `_wiki/` as new
  podcast evidence appears.
- Improve `_wiki/data-analyst-to-analytics-engineer.md` as new evidence
  appears.
- The 2026-07-05 analytics-engineering transition cleanup made
  `_wiki/data-analyst-to-analytics-engineer.md` transition-only, retitled it
  and `_wiki/data-analyst-vs-analytics-engineer.md` with the full "Data
  Analyst" label, shortened duplicated roadmap/comparison material, aligned
  related links with the body, and timestamped Nikola's blurred
  analyst/analytics-engineer role evidence plus Juan Pablo's
  BI/analytics-engineering evidence.
- The 2026-07-05 data-engineering transition link cleanup added `DevOps to
  Data Engineering` and `Career Transitions in Data` to the data-engineer
  roadmap graph, added missing transition links to
  `career-transitions-in-data`, `devops-to-data-engineering`,
  `qa-to-ml-and-data-engineering`, and
  `how-to-become-a-data-engineer-with-no-experience`, and retitled
  `_wiki/data-scientist-to-data-engineer.md` from "Data Eng" to "Data
  Engineer" while keeping it transition-focused.
- The 2026-07-05 community boundary cleanup trimmed conference operations from
  `_wiki/community.md`, kept organizer execution on `_wiki/community-building.md`,
  and kept venue, CFP, sponsor, timetable, and networking details on
  `_wiki/data-ai-conference-building.md` with precise Data Makers Fest anchors.
- The 2026-07-05 weak-node graph cleanup added grounded body links for
  `_wiki/llm-deployment.md` from RAG/LLM production pages,
  `_wiki/entity-resolution.md` from data-engineering portfolio/tool pages,
  `_wiki/model-monitoring-vs-data-observability.md` from MLOps comparison and
  roadmap pages, and `_wiki/sensor-ml-personal-baselines.md` from
  nontraditional AI paths. The RFM link from Data Analyst vs Analytics Engineer
  was added in the analytics transition cleanup.
- The second 2026-07-05 weak-node graph cleanup linked data architect from
  `_wiki/data-freelancing-strategy.md`, data roles from
  `_wiki/analytics-engineering.md`, data engineering/data science from
  `_wiki/data-engineer-vs-data-scientist.md`, data product manager roadmap from
  `_wiki/data-product-owner-vs-data-product-manager.md`, reinforcement learning
  and evolutionary algorithms from `_wiki/ai.md`, synthetic data from
  `_wiki/llm-evaluation-workflows.md`, and volunteer data projects from
  `_wiki/career-transitions-in-data.md`.
- The same audit still reports 17 nodes below 8 inbound links. The nodes from
  the second cleanup moved from 6 to 7 inbound links, so the next graph pass
  should add one more grounded body link to each of those pages and then address
  the remaining 7-inbound nodes from `scripts/audit_graph.py --min-inbound 8`.
- The third 2026-07-05 weak-node graph cleanup added grounded links for the LLM
  and RAG production roadmap, AI-powered BI, AI product feedback loops,
  AI tools workflow guide, Scikit-Learn, and machine learning for startups.
  The graph audit dropped from 17 to 12 weak nodes afterward. AI-powered BI
  still needs a grounded link from a page that does not already link to it.
- The fourth 2026-07-05 weak-node graph cleanup added grounded body links for
  the remaining 12 weak nodes. `python scripts/audit_graph.py --min-inbound 8`
  now reports 0 weak wiki nodes below 8 inbound links.
- The 2026-07-05 strict graph-depth follow-up used
  `python scripts/audit_graph.py --min-inbound 12` and strengthened five
  high-value keyword/editorial pages: `_wiki/how-to-build-data-pipelines.md`,
  `_wiki/data-observability-for-data-engineering.md`,
  `_wiki/machine-learning-system-design-interview.md`,
  `_wiki/llm-system-design-interview.md`, and `_wiki/hire-data-engineers.md`.
  All five now have at least 12 inbound links. The strict audit still reports
  68 wiki/content nodes below 12 inbound links, so future graph-depth work
  should continue from that audit rather than reopening the older min-8 list.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/ai-coding-tools.md`, `_wiki/annotation-quality-workflows.md`,
  `_wiki/apache-iceberg.md`, `_wiki/competitions-beyond-kaggle.md`, and
  `_wiki/data-engineer-to-data-scientist.md`. All five now have at least 12
  inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  63 wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/data-product-manager-roadmap.md`,
  `_wiki/data-product-manager-vs-product-manager.md`,
  `_wiki/data-science-project-management.md`,
  `_wiki/data-scientist-cv-and-portfolio.md`, and
  `_wiki/data-translator-role.md`. All five now have at least 12 inbound links.
  `python scripts/audit_graph.py --min-inbound 12` now reports 58 wiki/content
  nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/dataops-vs-data-engineering.md`, `_wiki/delta-lake.md`,
  `_wiki/delta-lake-vs-apache-iceberg.md`,
  `_wiki/evolutionary-algorithms.md`, and
  `_wiki/freelance-data-and-ml-careers.md`. All five now have at least 12
  inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  53 wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/game-ai-to-llm-agents.md`, `_wiki/llm-cost-optimization.md`,
  `_wiki/llm-deployment.md`, `_wiki/llm-rag-production-roadmap.md`, and
  `_wiki/llm-tools.md`. All five now have at least 12 inbound links.
  `python scripts/audit_graph.py --min-inbound 12` now reports 48 wiki/content
  nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/machine-learning-engineer-roadmap.md`,
  `_wiki/machine-learning-for-software-engineers.md`,
  `_wiki/machine-learning-personalization.md`,
  `_wiki/machine-learning-vs-software-engineering.md`, and
  `_wiki/manufacturing-predictive-maintenance-yield-analytics.md`. All five now
  have at least 12 inbound links. `python scripts/audit_graph.py --min-inbound
  12` now reports 43 wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/marketing-to-analytics-engineering.md`,
  `_wiki/ml-consulting-proposals.md`, `_wiki/mlops-adoption-at-scale.md`,
  `_wiki/mlops-vs-devops.md`, and
  `_wiki/model-monitoring-vs-data-observability.md`. All five now have at least
  12 inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  38 wiki/content nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/model-optimization.md`, `_wiki/modern-data-engineering-trends.md`,
  `_wiki/notebook-to-production-workflow.md`,
  `_wiki/open-source-ml-contributions.md`, and
  `_wiki/product-analyst-vs-data-analyst.md`. All five now have at least 12
  inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  33 wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/product-owner-vs-product-manager.md`,
  `_wiki/project-manager-to-data-science.md`,
  `_wiki/prompt-injection-and-chatbot-risk-management.md`,
  `_wiki/rag-evaluation-workflow.md`, and `_wiki/salary-negotiation.md`. All
  five now have at least 12 inbound links. `python scripts/audit_graph.py
  --min-inbound 12` now reports 28 wiki/content nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/sensor-ml-personal-baselines.md`,
  `_wiki/software-engineer-to-machine-learning.md`,
  `_wiki/volunteer-data-engineering-projects.md`, `_wiki/a-a-testing.md`, and
  `_wiki/ai-engineering-portfolio-projects.md`. All five now have at least 12
  inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  23 wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/applied-research.md`,
  `_wiki/astroinformatics-scientific-data-pipelines.md`,
  `_wiki/camera-first-vs-lidar-autonomous-driving.md`,
  `_wiki/context-engineering.md`, and
  `_wiki/data-engineering-and-data-science.md`. All five now have at least 12
  inbound links. `python scripts/audit_graph.py --min-inbound 12` now reports
  18 wiki/content nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/data-engineering-certification.md`,
  `_wiki/data-product-owner-vs-data-product-manager.md`,
  `_wiki/data-roles.md`, `_wiki/data-science-for-managers.md`, and
  `_wiki/lean-mlops-for-startups.md`. All five now have at least 12 inbound
  links. `python scripts/audit_graph.py --min-inbound 12` now reports 13
  wiki/content nodes below 12 inbound links.
- The following 2026-07-05 strict graph-depth batch strengthened
  `_wiki/learning-in-public-ai-career-switch.md`,
  `_wiki/machine-learning-engineer-vs-data-scientist.md`,
  `_wiki/machine-learning-for-business.md`,
  `_wiki/machine-learning-for-startups.md`, and `_wiki/metaflow.md`. All five
  now have at least 12 inbound links. `python scripts/audit_graph.py
  --min-inbound 12` now reports 8 wiki/content nodes below 12 inbound links.
- The next 2026-07-05 strict graph-depth batch strengthened
  `_wiki/ml-platform-engineer-role.md`,
  `_wiki/ml-system-design-documents.md`,
  `_wiki/nontraditional-paths-to-ai-engineering.md`,
  `_wiki/product-analyst.md`, and
  `_wiki/product-designer-to-data-product-manager.md`. All five now have at
  least 12 inbound links. `python scripts/audit_graph.py --min-inbound 12` now
  reports 3 wiki/content nodes below 12 inbound links.
- The final 2026-07-05 strict graph-depth batch strengthened
  `_wiki/rfm-analysis.md`, `_wiki/scikit-learn.md`, and
  `_wiki/staff-ai-engineer.md`. All three now have at least 12 inbound links.
  `python scripts/audit_graph.py --min-inbound 12` now reports 0 wiki/content
  nodes below 12 inbound links.
- The 2026-07-06 graph-depth drift cleanup found three pages back below the
  strict 12-inbound threshold after later corpus changes:
  `_wiki/ai-engineering-portfolio-projects.md`,
  `_wiki/product-designer-to-data-product-manager.md`, and
  `_wiki/product-owner-vs-product-manager.md`. Grounded body links from
  `_wiki/career-transitions-in-data.md` and
  `_wiki/data-product-intake-and-prioritization.md` restored the strict audit:
  `python scripts/audit_graph.py --min-inbound 12` now reports 0 weak wiki
  nodes.
- The 2026-07-06 read-only quality audit backlog is complete. It differentiated
  `_wiki/graph-rag-vs-vector-rag.md` from neighboring search/RAG pages;
  broadened or narrowed `_wiki/project-manager-to-data-science.md`,
  `_wiki/game-ai-to-llm-agents.md`,
  `_wiki/camera-first-vs-lidar-autonomous-driving.md`, and
  `_wiki/data-ai-conference-building.md`; tightened `_wiki/apache-iceberg.md`
  and `_wiki/delta-lake.md` around concept-vs-comparison routing; added
  body crosslinks to `_wiki/text-to-sql.md`; and improved
  `_wiki/volunteer-data-engineering-projects.md` links and wording.
- The 2026-07-06 Ubersuggest audit still found no grounded new standalone page
  clusters, but it did find alias/enrichment work for existing pages: add
  `data ops platform` wording to `_wiki/dataops-platforms.md`; make
  `mlops frameworks`, `mlops tool`, and `mlops tools` explicit on
  `_wiki/mlops-tools.md`; strengthen head-term and "what is" intent on
  `_wiki/data-product-management.md`; tighten course/certification/training
  intent on `_wiki/data-product-manager-roadmap.md`; add consultancy variants
  to `_wiki/freelance.md`; clarify data-engineer recruiter intent through
  `_wiki/hire-data-engineers.md` and `_wiki/data-science-recruiter.md`; and
  make analyst take-home assignment coverage easier to find from
  `_wiki/data-analyst-careers.md`.
- The 2026-07-06 Ubersuggest alias/enrichment batch above is complete. The
  affected pages now route spaced DataOps aliases, MLOps tool/framework
  variants, data product management definition/course/certification/training
  variants, consultancy variants, data-engineer recruiter intent, and analyst
  take-home assignment intent without creating duplicate pages.
- The 2026-07-06 stricter body-link exploration audit found hub-to-guide and
  body-link gaps even though the generated graph passes min-12 inbound:
  strengthen body links into `_wiki/career-development.md`,
  `_wiki/data-analysis.md`, and `_wiki/graph-data-science.md`; add return links
  from `_wiki/data-engineering.md`, `_wiki/machine-learning.md`, and
  `_wiki/data-science.md` to their high-value tagged pages; and improve
  exploration links on `_wiki/text-to-sql.md` and
  `_wiki/model-monitoring-vs-data-observability.md`.
- The first 2026-07-06 body-link batch added return links from
  `_wiki/data-engineering.md`, `_wiki/machine-learning.md`, and
  `_wiki/data-science.md` to their high-value tagged pages.
- The second 2026-07-06 body-link batch is complete. It added inbound body links
  for career development, data analysis, and graph data science from adjacent
  role, career, RAG, ML, and simulation pages. It also added outgoing
  exploration links on `_wiki/text-to-sql.md` and
  `_wiki/model-monitoring-vs-data-observability.md`.
- Keep `dataops platforms` on `_wiki/dataops-platforms.md`. It links to
  DataOps, DataOps tools, platform engineering, and data engineering platforms.
- Improve `_wiki/open-source.md` before creating any Open Source editorial
  page. The keyword is a bare concept, so the wiki page should own it.
  The canonical page was strengthened with contribution, DevRel, data/ML tool,
  portfolio, licensing, and founder evidence. Future open-source work should
  extend that page or the linked contributor roadmap, not create a duplicate
  "what is open source" guide.
- Keep `data engineering open source projects` covered by `_wiki/open-source.md`,
  `_wiki/open-source-portfolio-evidence.md`,
  `_wiki/data-engineering-portfolio-projects.md`, and
  `_wiki/open-source-contributor-roadmap.md` unless a future brief asks for
  a narrower project guide.
- Keep `open source entity resolution` covered by `_wiki/entity-resolution.md`
  and linked supporting pages such as Open Source, Data Engineering Tools, and
  portfolio pages. Extend the entity-resolution wiki page when more interviews
  add matching, identity, or customer-360 evidence.
- Treat Delta Lake as a wiki concept. The editorial comparison now lives in
  `_wiki/delta-lake-vs-apache-iceberg.md`; keep bare Delta Lake updates
  on `_wiki/delta-lake.md`.
- Keep A/B testing as wiki coverage, not a separate guide or content category.
  Current canonical coverage lives in `_wiki/a-b-testing.md`,
  `_wiki/experimentation-and-causal-inference.md`, `_wiki/experimentation.md`,
  and `_wiki/power-analysis.md`. Editorial pages such as Product Analyst should
  link back to those wiki pages instead of owning the topic.
- Do not create a generic machine learning newsletter guide from the podcast
  archive alone. The evidence supports a community-content or owned-channel
  guide later, not a standalone "best newsletters" page.
- The latest 2026-07-06 Ubersuggest rerun still has 0 grounded new-page
  clusters. Current counts: 207 covered by podwiki, 310 main-site owned, 123
  branded/navigation, 204 book-intent, 18 noise, and 138 ungrounded gaps. Keep
  using the CSV for canonical-page maintenance, not new duplicate pages.
- The 2026-07-06 five-agent graph-depth pass strengthened inbound body links
  and page boundaries for AI coding tools, AI finance decision support, Python
  stock analysis, annotation quality workflows, and Delta/Iceberg table-format
  pages. The stricter exploration audit improved from 125 to 121 nodes below
  16 inbound links while the official min-12 graph gate stayed clean. Future
  min-16 work should continue from the remaining weak-node list rather than
  revisiting those clusters.
- The next 2026-07-06 graph-depth pass used two five-agent batches to strengthen
  applied research, astroinformatics scientific pipelines, camera-first versus
  LiDAR autonomous driving, services-to-product-founder, data-analyst-to-
  analytics-engineer, data roles, ML consulting proposals, and adjacent pipeline
  and optimization pages. `python scripts/audit_graph.py --min-inbound 16`
  improved from 121 to 119 weak nodes, and
  `python scripts/audit_graph.py --min-inbound 12` still reports 0 weak wiki
  nodes. Continue future min-16 work from the remaining weak-node list.
- The following 2026-07-06 five-agent graph-depth batch strengthened role and
  career-transition clusters: data engineer to data scientist, data engineering
  manager, data science for managers, data scientist interview prep, and data
  scientist to machine learning engineer. It also tightened
  `_wiki/mlops-architecture.md` after the duplicate audit showed temporary
  overlap with MLOps and the MLOps roadmap. `python scripts/audit_graph.py
  --min-inbound 16` improved from 119 to 117 weak nodes, the official
  `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The next 2026-07-06 five-agent graph-depth batch strengthened DataOps
  engineer, DataOps tools, Delta Lake, DuckDB, and industrial ML application
  clusters with grounded body links from CI/CD, testing, lakehouse, pipeline,
  freelancing, and industrial AI pages. `python scripts/audit_graph.py
  --min-inbound 16` improved from 117 to 116 weak nodes, the official
  `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The following 2026-07-06 five-agent graph-depth batch strengthened data roles,
  how to build data pipelines, KPIs, lean MLOps for startups, and public
  learning for AI careers with grounded body links from role, transition,
  project, tooling, monitoring, orchestration, portfolio, freelancing, and
  technical-writing pages. `python scripts/audit_graph.py --min-inbound 16`
  improved from 116 to 115 weak nodes, the official `--min-inbound 12` gate
  stayed clean, and `python scripts/find_duplicates.py --overlap --min-pct 35`
  returned 0 pairs.
- The next 2026-07-06 graph-depth pass used two five-agent batches to strengthen
  LLM/RAG production roadmap, LLM system design interview, LLM tools, ML
  engineer roadmap, and ML personalization clusters. The pass added grounded
  in-body links from LLM, evaluation, agent, AI tooling, data-role, MLOps,
  recommendation, search, vector, customer-data, and industrial ML pages. It
  also tightened the LLM evaluation versus RAG evaluation boundary after the
  overlap audit found a temporary 35.0% vocabulary collision.
  `python scripts/audit_graph.py --min-inbound 16` improved from 115 to 111
  weak nodes, the official `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The following 2026-07-06 five-agent graph-depth batch strengthened ML system
  design interview, machine learning versus software engineering, fab
  maintenance and yield ML, marketer to analytics engineer, and Metaflow
  clusters. The pass added grounded body links from interview, recruiter,
  portfolio, recommendation, ML engineering, design-document, industrial data
  team, CDO, sensor baseline, data strategy, experimentation, causal
  inference, MLOps, platform, registry, and production checklist pages.
  `python scripts/audit_graph.py --min-inbound 16` improved from 111 to 106
  weak nodes, all five targets reached at least 16 inbound links, the official
  `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The next 2026-07-06 graph-depth pass used a five-agent batch plus two focused
  follow-up workers to strengthen ML consulting proposals, ML platform engineer
  role, ML system design documents, MLOps vs DevOps practices, and model
  optimization. The pass added grounded body links from consulting, startup,
  salary, platform, registry, experiment-tracking, MLOps, design-document,
  technical-writing, computer-vision, LLM, infrastructure, and software-to-ML
  transition pages. `python scripts/audit_graph.py --min-inbound 16` improved
  from 106 to 101 weak nodes, all five target clusters reached at least 16
  inbound links, the official `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The following 2026-07-06 five-agent graph-depth batch strengthened
  multi-agent systems, nontraditional AI engineering, notebook-to-production
  workflow, open-source ML contributions, and product analyst vs data analyst.
  The pass added grounded body links from agent, LLM, evaluation, tooling,
  career-transition, bootcamp, research, portfolio, notebook handoff,
  open-source, product-metrics, A/B testing, KPI, and data-team pages.
  `python scripts/audit_graph.py --min-inbound 16` improved from 101 to 96 weak
  nodes, all five targets reached at least 16 inbound links, the official
  `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The next 2026-07-06 five-agent graph-depth batch strengthened product
  designer to data product manager, product owner vs product manager, project
  manager to data science, salary negotiation, and scikit-learn. The pass added
  grounded body links from discovery, data-team, founder, communication,
  governance, data-mesh, personalization, project-management, compensation,
  freelance-pricing, DevRel, QA-to-ML, and machine-learning-tool pages.
  `python scripts/audit_graph.py --min-inbound 16` improved from 96 to 91 weak
  nodes, all five targets reached at least 16 inbound links, the official
  `--min-inbound 12` gate stayed clean, and
  `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs.
- The following 2026-07-08 five-agent graph-depth batch strengthened sensor ML
  personal baselines, staff AI engineer, synthetic data, teaching, and
  text-to-SQL. The pass added grounded body links from baseline/project,
  senior-IC, architecture, generated-data, test-data, mentoring, education,
  semantic-layer, BI-assistant, and LLM-tool pages. `python
  scripts/audit_graph.py --min-inbound 16` improved from 91 to 86 weak nodes,
  all five targets reached at least 16 inbound links, the official
  `--min-inbound 12` gate stayed clean, and `python
  scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs. `python
  scripts/build_graph.py` produced 1071 nodes and 12820 links.
- The next 2026-07-08 graph-depth pass used two five-agent waves to strengthen
  A/A testing, researcher-to-data-science, AI engineering portfolios, AI finance
  decision support, and AI-powered business intelligence. The first wave
  improved prose and citations but reused several already-connected source
  pages, so the follow-up wave targeted fresh source pages for unique graph
  depth. The pass added grounded body links from experimentation, research,
  scientific-data, agent, RAG, context-engineering, decision-support, KPI,
  analytics, activation, and BI roadmap pages. `python scripts/audit_graph.py
  --min-inbound 16` improved from 86 to 81 weak nodes, all five targets reached
  at least 16 inbound links, the official `--min-inbound 12` gate stayed clean,
  and `python scripts/find_duplicates.py --overlap --min-pct 35` returned 0
  pairs. `python scripts/build_graph.py` produced 1071 nodes and 12840 links.
  The Ubersuggest rerun still found 0 grounded new-page gaps.
- The following 2026-07-08 five-agent graph-depth batch strengthened AI tools
  for personal productivity, autonomous driving AI, causal inference, CDC, and
  the chief data officer role. The pass added grounded body links from learning
  workflows, career-development, developer-experience, industrial ML,
  safety/governance, product-analysis, data-pipeline, ETL, DataOps-tooling,
  architecture, engineering-management, and adoption pages. `python
  scripts/audit_graph.py --min-inbound 16` improved from 81 to 76 weak nodes,
  all five targets reached at least 16 inbound links, the official
  `--min-inbound 12` gate stayed clean, and `python
  scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs. `python
  scripts/build_graph.py` produced 1071 nodes and 12856 links. The Ubersuggest
  rerun still found 0 grounded new-page gaps and produced no report diff.
- The next 2026-07-08 five-agent graph-depth batch strengthened competitions
  beyond Kaggle, customer data platforms, data and AI conference building, data
  architect role, and data engineering plus data science. The pass added
  grounded body links from applied-research, portfolio, customer-activation,
  analytics-engineering, data-product, DevRel, technical-writing,
  developer-experience, contract, mesh, lakehouse, trend, transition, MLOps, and
  manager pages. `python scripts/audit_graph.py --min-inbound 16` improved from
  76 to 71 weak nodes, all five targets reached at least 16 inbound links, the
  official `--min-inbound 12` gate stayed clean, and `python
  scripts/find_duplicates.py --overlap --min-pct 35` returned 0 pairs. `python
  scripts/build_graph.py` produced 1071 nodes and 12873 links. The Ubersuggest
  rerun still found 0 grounded new-page gaps and produced no report diff.
- The following 2026-07-08 graph-depth pass used two five-agent waves to
  strengthen data engineering certification, data mesh vs centralized data
  platform, data product manager vs product manager, data product owner vs data
  product manager, and data science project management. The first wave improved
  body links but did not move all targets above the stricter min-16 threshold,
  so the second wave used fresh source pages for unique graph edges. The pass
  added grounded body links from Airflow, orchestration, ETL, data contracts,
  modern data stack, data quality, product intake, data architect, product
  analyst, metrics, data teams, evaluation, ML system design, and design-doc
  pages. `python scripts/audit_graph.py --min-inbound 16` improved from 71 to
  67 weak nodes, the official `--min-inbound 12` gate stayed clean, and
  `python scripts/build_graph.py` produced 1071 nodes and 12890 links.
  `python scripts/find_duplicates.py --overlap --min-pct 35` now reports one
  borderline vocabulary-overlap pair:
  `_wiki/machine-learning-system-design-interview.md` and
  `_wiki/machine-learning-system-design.md` at 35.2% token overlap with only
  0.3% verbatim shingle overlap. Keep them separate unless the interview guide
  starts ranking against the reference concept page; their intents remain
  interview preparation versus production reference.
- The next 2026-07-08 graph-depth pass used two five-agent waves to strengthen
  data scientist CV and portfolio, data translator role, DataOps vs data
  engineering, founder, game AI to LLM agents, LLM deployment, machine learning
  engineer vs data scientist, and ML for software engineers. The pass added
  grounded body links from data scientist role, competitions, applied research,
  product analytics, analytics engineering, data analysis, Airflow,
  orchestration, data quality, startup/MLOps, AI BI, context engineering,
  multi-agent systems, LLM production, agent engineering, prompt engineering,
  MLOps roles, platform roles, developer experience, notebook-to-production,
  and production ML checklist pages. `python scripts/audit_graph.py
  --min-inbound 16` improved from 67 to 60 weak nodes, the official
  `--min-inbound 12` gate stayed clean, and `python scripts/build_graph.py`
  produced 1071 nodes and 12916 links. `python scripts/find_duplicates.py
  --overlap --min-pct 35` reports two vocabulary-overlap pairs with low
  verbatim overlap: Airflow vs Orchestration at 35.4% token and 0.4% verbatim,
  plus the existing ML system design interview vs reference page at 35.2% token
  and 0.3% verbatim. Keep both pairs separate for now because the intents are
  concrete tool page vs generic control-plane concept, and interview prep vs
  production reference.
- The following 2026-07-08 five-agent graph-depth pass strengthened machine
  learning for startups, machine learning tools, MLOps adoption at scale, model
  monitoring vs data observability, and modern data engineering trends. The pass
  added grounded body links from product-manager roadmap, product analytics,
  model optimization, ML system design, design docs, MLOps engineer, MLOps
  tools, production ML checklist, LLM production, data contracts, data mesh, and
  data product management pages. `python scripts/audit_graph.py --min-inbound
  16` improved from 60 to 56 weak nodes, the official `--min-inbound 12` gate
  stayed clean, and `python scripts/build_graph.py` produced 1071 nodes and
  12933 links. `python scripts/find_duplicates.py --overlap --min-pct 35`
  still reports only the two known vocabulary-overlap pairs: Airflow vs
  Orchestration and ML system design interview vs ML system design.
- The next 2026-07-08 five-agent graph-depth pass strengthened open source
  contributor roadmap, practices, product analyst, prompt injection and chatbot
  risk management, and reinforcement learning. The pass added grounded body
  links from technical writing, developer relations, data engineering
  certification, software engineering, CI/CD, DataOps tools, data-led growth,
  data analysis, KPIs, generative AI, privacy engineering, LLM system design
  interview, causal inference, experimentation and causal inference, and
  recommendation systems pages. `python scripts/audit_graph.py --min-inbound
  16` improved from 56 to 51 weak nodes, the official `--min-inbound 12` gate
  stayed clean, and `python scripts/build_graph.py` produced 1071 nodes and
  12948 links. `python scripts/find_duplicates.py --overlap --min-pct 35`
  still reports only the two known vocabulary-overlap pairs: Airflow vs
  Orchestration and ML system design interview vs ML system design.
- The following 2026-07-08 five-agent graph-depth pass strengthened RFM
  analysis, software engineer to machine learning, volunteer data engineering
  projects, community, and data freelancing strategy. The pass added grounded
  body links from data warehouse, data analyst role, power analysis, machine
  learning engineer roadmap, machine learning portfolio projects,
  notebook-to-production AI systems, job search, AI for social good, data
  analyst careers, data engineering certification, machine learning tools,
  developer experience, documentation, nontraditional AI engineering,
  solopreneur, and data science careers pages. `python
  scripts/audit_graph.py --min-inbound 16` improved from 51 to 46 weak nodes,
  the official `--min-inbound 12` gate stayed clean, and `python
  scripts/build_graph.py` produced 1071 nodes and 12963 links. `python
  scripts/find_duplicates.py --overlap --min-pct 35` still reports only the two
  known vocabulary-overlap pairs: Airflow vs Orchestration and ML system design
  interview vs ML system design.
