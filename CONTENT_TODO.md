# Podwiki Content TODO

This backlog captures page categories that should become repeatable content
families. Use it when planning new wiki pages, guides, comparisons, roadmaps,
how-tos, podcast summaries, or people-page expansion.

## Category Rules

Follow these rules when adding any page from this backlog.

- Keep `_wiki/` pages as archive-backed reference pages with inline episode
  references, tradeoffs, and related pages.
- Put keyword-targeted editorial pages in `_guides/`, `_comparisons/`,
  `_roadmaps/`, or `_how_tos/`. If the page is only the bare concept, put it in
  `_wiki/`. Public URLs are `/guides/`, `/comparisons/`, `/roadmaps/`, and
  `/how-tos/`.
- Keep `_podcast_summaries/` compact enough for agents to decide whether they
  need the source episode.
- Link podcast evidence to local podcast pages such as
  `{{ '/podcasts/<source-file-slug>/' | relative_url }}`. Those local pages
  link to the canonical DataTalks.Club episode. Do not link public-page evidence
  to the generic podcast archive page.
- Run `make check` after adding pages so graph and search stay current.

## Current Rewrite Requirements

These notes capture the current cleanup direction and should not be lost.

- Redo wiki pages to follow one structure: opening definition, link map, common
  definition, where guests differ, concrete topic sections with inline podcast
  references, and related pages.
- Remove public meta sections from wiki and editorial pages. Do not use
  `Contents`, `Search Intent`, `Archive Evidence`, `Episode Evidence`, `Guest
  Descriptions`, `Recurring Archive Themes`, `Maintenance Notes`, or `Agent
  Maintenance Notes` as reader-facing headings.
- Ground each substantive section in actual podcast discussions. Put the
  podcast reference next to the claim it supports, like a citation, instead of
  collecting evidence in a separate appendix.
- Make every page link-heavy: visible links to specific podcast interviews,
  related wiki pages, people pages, category pages, local podcast pages, and the
  grounding evidence behind substantive claims.
- Use local podcast links such as
  `{{ '/podcasts/<source-file-slug>/' | relative_url }}` whenever the source
  episode slug is known. The local podcast page links to the original
  DataTalks.Club episode.
- Make related links visually obvious in CSS. Related pages should look like
  links, not muted tags.
- Keep the graph-driven "See Also in the Graph" section on wiki, editorial,
  podcast summary, and people pages. It is rendered from `graph/graph.json` by
  `assets/page-graph.js`, so Markdown links remain the source of truth.
- Keep `/podcasts/` as a list view closer to the original DataTalks.Club
  podcast structure. The pages in `_podcast_summaries/` are the internal
  citation targets for wiki and editorial pages.
- Treat Markdown pages as the source for the graph. Do not maintain
  `graph/graph.json` separately; regenerate it from the collections.
  Internally, graph nodes may still call guides, comparisons, roadmaps, and
  how-tos article/content nodes; do not expose that as a public category.
- Keep `make sources` as the first step for broad podcast work. It syncs local
  podcast pages, people pages, chapter summaries, and the source index used by
  subagents.
- Use `sources/podcast-topic-inventory.md` as the durable topic map from the
  five-agent archive pass. Extend it when a new archive-wide discovery pass finds
  a recurring grounded topic.
- For broad topic discovery, keep five subagents running on non-overlapping
  podcast batches and collect grounded topic reports before writing pages.
- Keep MLOps and DataOps as separate concept pages. Use `_wiki/mlops.md` for
  model lifecycle operations, `_wiki/dataops.md` for data delivery operations,
  and `_comparisons/mlops-vs-dataops.md` for the comparison.
- Keep pages centered on one topic, role, transition, comparison, roadmap, or
  project type. Split mixed pages instead of broadening them.
- Name concept pages by the concept, not by "What is ..." phrasing. Use
  `Open Source`, `MLOps`, or `DataOps` as page names; keep "what is" only as a
  keyword variant in frontmatter or audit notes.

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
- `_wiki/machine-learning-engineer-role.md`
- `_guides/analytics-engineer.md`
- `_guides/data-product-manager-role.md`

Candidate pages:

- ML platform engineer
- Analytics engineer
- Data product manager
- Developer advocate / DevRel engineer
- MLOps engineer
- Data architect
- Data team lead / head of data

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

- `_wiki/career-transitions-in-data.md`
- `_guides/software-engineer-to-machine-learning.md`

Candidate pages:

- Software engineer to machine learning
- Data analyst to data engineer
- Data analyst to analytics engineer
- Marketing to analytics engineering
- QA engineer to ML or data engineering
- Academic researcher to data science
- Product designer to data product manager
- Data scientist to ML engineer
- DevOps engineer to data engineering
- Consultant or freelancer to data product founder

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

- `_guides/data-scientist-interview.md`
- `_wiki/open-source-and-developer-relations.md`
- `_wiki/data-engineering-portfolio-projects.md`
- `_wiki/machine-learning-portfolio-projects.md`
- `_wiki/analytics-engineering-portfolio-projects.md`
- `_wiki/rag-portfolio-projects.md`
- `_wiki/open-source-portfolio-evidence.md`

Candidate pages:

- End-to-end data pipeline project
- Production ML project checklist
- Search or RAG project checklist
- Dashboard and metric-layer project checklist

Source hints:

- `data-science-interview-and-cv-guide.md`
- `get-data-scientist-job.md`
- `open-source-ml-contributions.md`
- `developer-personal-brand-learn-in-public.md`
- `building-scalable-and-reliable-machine-learning-systems.md`
- `modern-search-systems-vector-databases-llms-semantic-retrieval.md`

## Roadmaps

Create roadmap pages that explain learning sequence, project sequence, role
milestones, and when to stop studying and build. These should be archive-backed,
not generic course lists.

Existing pages:

- `_wiki/machine-learning-system-design.md`
- `_wiki/mlops-and-dataops.md`
- `_wiki/llm-production-patterns.md`
- `_wiki/search-rag-and-knowledge-systems.md`
- `_wiki/dataops-platforms.md`

Candidate pages:

- Data engineering roadmap
- Analytics engineering roadmap
- Machine learning engineer roadmap
- AI engineer roadmap
- MLOps roadmap
- Data scientist interview roadmap
- Data product manager roadmap
- Open-source contributor roadmap
- LLM / RAG production roadmap

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

- `_comparisons/dataops-vs-data-engineering.md`
- `_comparisons/delta-lake-vs-apache-iceberg.md`
- `_comparisons/etl-vs-elt.md`
- `_comparisons/product-owner-vs-product-manager.md`
- `_wiki/batch-vs-streaming.md` owns the canonical batch vs streaming decision.
- `_wiki/data-warehouse-vs-data-lakehouse.md` owns the canonical warehouse vs
  lakehouse decision.
- `_wiki/data-mesh-vs-centralized-data-platform.md` owns the canonical data mesh
  vs centralized platform decision unless a separate editorial comparison is
  needed.
- `_wiki/vector-database-vs-search-engine.md` owns the canonical vector database
  vs search engine decision unless a separate editorial comparison is needed.
- `_wiki/knowledge-graph-vs-vector-search.md` owns the canonical knowledge graph
  vs vector search decision unless a separate editorial comparison is needed.

Candidate pages:

- Data engineer vs data scientist
- Data analyst vs analytics engineer
- Machine learning engineer vs data scientist. Create
  `_comparisons/machine-learning-engineer-vs-data-scientist.md` with
  `_wiki/machine-learning-engineer-role.md`, `_wiki/data-scientist-role.md`,
  `data-team-roles.md`, `data-science-interview-and-cv-guide.md`, and
  `machine-learning-engineering-production-best-practices.md` as primary
  grounding.
- Data product manager vs product manager
- Data product owner vs data product manager. Create
  `_comparisons/data-product-owner-vs-data-product-manager.md` as a focused
  spin-out from `_comparisons/product-owner-vs-product-manager.md`,
  `_wiki/data-product-management.md`, and
  `building-data-products-product-owner-vs-product-manager.md`.
- MLOps vs DevOps
- DataOps vs MLOps
- RAG vs fine-tuning

Source hints:

- `big-data-engineer-vs-data-scientist.md`
- `analytics-engineer-skills-tools.md`
- `building-data-products-product-owner-vs-product-manager.md`
- `data-engineering-tools-modern-data-stack.md`
- `data-mesh-architecture-decentralized-data-products.md`
- `production-ml-search-vector-search-embeddings-hybrid-search.md`

## Next Batch

Start with this batch when expanding the content set.

- Resolve the 689-row content gaps export. The local file
  `.tmp/next-actions-done-datatalks.club.xlsx` currently has the expected tabs
  but only header rows, so replace it with the populated export before creating
  gap-driven pages.
- Add transition pages for marketing to analytics engineering, QA to ML/data
  engineering, and academic researcher to data science.
- Add portfolio project pages for data engineering, ML engineering, analytics
  engineering, and RAG.
- Add roadmap pages for data engineering, AI engineering, MLOps, and analytics
  engineering.
- Add comparison pages for data analyst vs analytics engineer and RAG vs
  fine-tuning first. These have the strongest current mix of podcast evidence,
  existing wiki support, and keyword fit.
- Keep batch vs streaming and data warehouse vs data lakehouse as wiki-owned
  decision pages unless a new keyword brief requires a very short editorial
  page that points back to the canonical wiki page.
- Viable audited follow-ups: data engineer vs data scientist as a short
  decision page, MLOps vs DevOps as a short decision page, and data analyst to
  analytics engineer as an analyst-specific roadmap page.
- Keep `dataops platforms` on `_wiki/dataops-platforms.md`. It links to
  DataOps, DataOps tools, platform engineering, and data engineering platforms.
- Improve `_wiki/open-source.md` before creating any Open Source editorial
  page. The keyword is a bare concept, so the wiki page should own it.
- Treat Delta Lake as a wiki concept. The editorial comparison now lives in
  `_comparisons/delta-lake-vs-apache-iceberg.md`; keep bare Delta Lake updates
  on `_wiki/delta-lake.md`.
- Create `_guides/ab-testing-podcast.md` as a listening guide, not a generic
  explainer. Strong sources include `ab-testing-and-product-experimentation.md`,
  `causal-inference-for-machine-learning.md`,
  `ml-engineering-kpis-and-metrics-strategy.md`, and
  `data-led-growth-event-tracking-and-reverse-etl.md`.
- Do not create a generic machine learning newsletter guide from the podcast
  archive alone. The evidence supports a community-content or owned-channel
  guide later, not a standalone "best newsletters" page.
