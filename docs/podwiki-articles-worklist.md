# Retired articles worklist — per-page decisions

Status note: this worklist was written before the category split in commit
`473dd0e`. Article retirement is complete: the public `_articles/` collection
and `/articles/` URLs are no longer the active editorial surface. Surviving
editorial content now lives under `_guides/`, `_comparisons/`, `_roadmaps/`, and
`_how_tos/`, with public URLs under `/guides/`, `/comparisons/`, `/roadmaps/`,
and `/how-tos/`.

This file is now a historical/current decision record for the 71 retired
article pages. Its purpose is to preserve why the Ubersuggest keyword swarm was
dissolved, where useful material landed, and which migrated editorial pages
should keep being maintained as guides, comparisons, roadmaps, or how-tos.

See `SEO_INTEGRATION.md` for the why. _Generated 2026-06-30._

## Decision legend

| Code | Meaning | Action |
|---|---|---|
| **DELETE-BRANDED** | DTC owns this as a real course/product on the main site | 301 → main-site page; remove article |
| **MERGE→wiki** | An existing (or 1 new) wiki topic covers this concept | Fold useful content into the topic; 301 article → `/podwiki/wiki/<topic>/` |
| **CONSOLIDATE** | One of several keyword variants for a single intent | Pick the one canonical target; 301 all variants → it |
| **KEEP-NEW** | Additive format the main site & wiki lack | Build the consolidated page; 301 variants → it |

**Redirects were optional for the retirement.** A 301 preserves a URL's earned
index presence, backlinks, and live references. The article pages were new,
unindexed, and orphaned when the cleanup happened, so most were deleted or
merged without per-page redirects. Add a 301 only if an old article URL was
shared externally and still matters. Old URL form: `/podwiki/articles/<slug>/`.

---

## A. DELETE-BRANDED (5) — main site owns these

Status: the four Zoomcamp guide pages and the `data-engineering-podcast` guide
were removed from podwiki on 2026-07-01. The main DataTalks.Club site owns
those course and podcast archive pages. Keep podcast evidence about course
usage inside role, roadmap, portfolio, and transition pages, and link to the
official course or podcast pages there when useful.

| Slug | Keyword | 301 target |
|---|---|---|
| data-engineering-zoomcamp | data engineering zoomcamp | main DE Zoomcamp course page |
| machine-learning-zoomcamp | machine learning zoomcamp | main ML Zoomcamp course page |
| mlops-zoomcamp | mlops zoomcamp | main MLOps Zoomcamp course page |
| llm-zoomcamp | llm zoomcamp | main LLM Zoomcamp course page |
| data-engineering-podcast | data engineering podcast | `/podcast/` |

## B. CONSOLIDATE — keyword swarms → one page each (26)

### B1 → wiki `data-engineering-roadmap` ("how to learn / become a DE")
Status: the duplicate guide pages for data engineering course, courses,
bootcamp, and training variants were removed from podwiki on 2026-07-01. Useful
selection guidance belongs in `_wiki/data-engineering-roadmap.md`. Keep the
roadmap-category pages `_roadmaps/data-engineer-roadmap.md` and
`_roadmaps/how-to-become-a-data-engineer-with-no-experience.md` for their
specific roadmap intents.

best-data-engineering-course · free-data-engineering-course · data-engineer-course ·
data-engineer-courses · data-engineering-course · data-engineering-courses ·
data-engineer-bootcamp · data-engineering-bootcamp · data-engineering-training ·
data-engineer-training · how-to-become-a-data-engineer-with-no-experience ·
data-engineer-roadmap  → 301 all to `/podwiki/wiki/data-engineer-roadmap/` (which links to the DE Zoomcamp)

### B2 → wiki `mlops-roadmap` (learn MLOps/ML + certifications)
Status: the duplicate MLOps course, courses, certification, machine learning
bootcamp, and machine learning engineer certification guide pages were removed
from podwiki on 2026-07-01. Useful course and certification selection guidance
belongs in `_wiki/mlops-roadmap.md`.

mlops-course · mlops-courses · mlops-certification · machine-learning-bootcamp ·
machine-learning-engineer-certification  → 301 to `/podwiki/wiki/mlops-roadmap/`

### B3 → wiki `freelance` (consulting/freelance DE)
Status: the duplicate freelance and consulting guide variants were consolidated
into `_wiki/freelance.md` on 2026-07-01. Keep consulting/freelance career
guidance in the wiki concept page rather than separate keyword guide pages.

data-engineer-consultant · data-engineer-consulting · data-engineering-consultant ·
data-engineering-consulting · data-engineering-freelance · freelance-data-engineer
 → 301 to `/podwiki/wiki/freelance/`

### B4 → KEEP-NEW interview-prep pages (see §D)
Status: `ml-system-design-interview` was folded into
`_guides/machine-learning-system-design-interview.md` on 2026-07-01. Keep
`_guides/llm-system-design-interview.md` as a separate guide because the query
has distinct LLM/RAG/agent/evaluation intent.

machine-learning-system-design-interview · ml-system-design-interview → canonical
ML interview guide. llm-system-design-interview → canonical LLM interview guide.

## C. MERGE→wiki — 1:1 into an existing topic (39)

Status: exact guide/wiki slug collisions were merged into the wiki layer and
the duplicate guide files were removed on 2026-06-30. Rows marked **keep** are
the surviving editorial pages now maintained in the split collections. The
Airflow/apache-airflow concept pages were consolidated into
`_wiki/orchestration.md` on 2026-07-01, while `airflow-docker-compose` now has a
standalone procedural how-to in `_how_tos/airflow-docker-compose.md`. The
analytics-engineer guide variant was consolidated into
`_wiki/analytics-engineering.md` on 2026-07-01. The
data-engineering-manager/data-engineer-manager cluster was consolidated into
`_wiki/leadership.md` on 2026-07-01.

| Slug | → wiki topic | Note |
|---|---|---|
| airflow | orchestration | **done: consolidated into `_wiki/orchestration.md`** |
| apache-airflow | orchestration | **done: consolidated into `_wiki/orchestration.md`; dup of airflow** |
| airflow-docker-compose | orchestration | **done: standalone procedural how-to in `_how_tos/airflow-docker-compose.md`; concept context remains in `_wiki/orchestration.md`** |
| analytics-engineer | analytics-engineering | **done: consolidated into `_wiki/analytics-engineering.md`** |
| data-engineering-and-data-science | data-engineer-vs-data-scientist | **done: consolidated into `_comparisons/data-engineer-vs-data-scientist.md`** |
| data-engineering-certification | data-engineering-certification | **done: slug collision merged** |
| data-engineering-manager | leadership | **done: consolidated into `_wiki/leadership.md`** |
| data-engineer-manager | leadership | **done: consolidated into `_wiki/leadership.md`; dup of data-engineering-manager** |
| data-engineering | data-engineering | **done: slug collision removed** |
| data-engineering-pipeline-project | data-engineering-portfolio-projects | **done: folded into `_wiki/end-to-end-data-pipeline-project.md`; old guide removed** |
| data-engineering-tools | data-engineering-tools | **done: slug collision merged** |
| data-observability-for-data-engineering | data-observability | **keep: practical guide for the data-engineering-specific observability query** |
| dataops | dataops | **done: slug collision removed** |
| dataops-tools | dataops | **keep: guide for practical DataOps stack/tool selection** |
| dataops-vs-data-engineering | dataops | **done: comparison lives in `_comparisons/dataops-vs-data-engineering.md`; concept context remains in `_wiki/dataops.md`** |
| data-product-manager | data-product-management | **keep: short role guide linked to canonical wiki page** |
| data-product-manager-role | data-product-management | **done: duplicate removed; links retargeted to `_guides/data-product-manager.md`** |
| data-science-for-managers | leadership | **done: consolidated into `_wiki/leadership.md`** |
| data-scientist-interview | data-scientist-interview-roadmap | **keep: keyword guide; roadmap remains `_wiki/data-scientist-interview-roadmap.md`** |
| data-scientist | data-scientist-role | **keep: keyword guide linked to canonical role page** |
| data-scientist-to-data-engineer | career-transition | **done: moved to `_roadmaps/data-scientist-to-data-engineer.md`** |
| designing-machine-learning-systems | machine-learning-system-design | **done: book-title guide folded into `_wiki/machine-learning-system-design.md`** |
| fundamentals-of-data-engineering | data-engineering | **done: book-title guide folded into `_wiki/data-engineering.md`, `_wiki/data-pipelines.md`, and `_wiki/data-engineering-roadmap.md`** |
| how-to-build-data-pipelines | data-pipelines | **keep: procedural how-to in `_how_tos`** |
| interpretable-machine-learning | interpretability | **done: guide folded into `_wiki/interpretability.md`** |
| llm-tools | llms | **keep: guide for practical LLM stack selection; crosslink to LLMs and AI Tooling** |
| machine-learning-for-software-engineers | software-engineer-to-machine-learning | **keep: practical software-engineer-to-ML keyword guide linked to canonical wiki page** |
| machine-learning-for-startups | startups | **keep: practical startup ML guide linked to startup and ML wiki topics** |
| machine-learning-system-design | machine-learning-system-design | **done: slug collision removed** |
| mlops-architecture | mlops | **keep: architecture guide; linked from MLOps** |
| mlops-engineer | mlops-engineer | **done: slug collision merged** |
| mlops-frameworks | mlops-tools | **keep: guide for framework/convention selection by failure mode** |
| mlops | mlops | **done: slug collision removed** |
| mlops-tools | mlops-tools | **done: slug collision merged** |
| mlops-vs-dataops | mlops-vs-dataops | **done: comparison lives in `_comparisons/mlops-vs-dataops.md`; removed combined wiki bridge** |
| product-analyst | product-analytics | **keep: role/job-description guide** |
| software-engineer-to-machine-learning | software-engineer-to-machine-learning | **done: slug collision removed** |
| solopreneur-data-scientist | entrepreneurship | **keep: practical data/AI career guide** |
| MLOps definition keyword variant | mlops | **done: handled by the MLOps wiki page; keep "what is mlops" only as a keyword variant** |

## D. KEEP-NEW — additive pages to build (2)

| New page | Absorbs | Why it's additive |
|---|---|---|
| **ML system-design interview prep** | B4 (`machine-learning-system-design-interview`, `ml-system-design-interview`) | **done: canonical guide is `_guides/machine-learning-system-design-interview.md`; short variant removed** |
| **LLM system-design interview prep** | B4 (`llm-system-design-interview`) | **keep: distinct guide for RAG, agents, evaluation, safety, latency, and operations** |
| **Business Intelligence** | ai-powered-business-intelligence | **done: moved into `_wiki/business-intelligence.md` with AI-powered BI as one section** |

---

## Outcome

- 71 articles → **0 standalone keyword pages.**
- The public `_articles/` collection is retired.
- Surviving content: existing wiki topics (enriched), split editorial pages in
  `_guides/`, `_comparisons/`, `_roadmaps/`, and `_how_tos/`, canonical ML and
  LLM interview-prep guides, and the `business-intelligence` wiki topic.

## Archived execution order

1. Enrich each §C wiki topic with the article's useful content, then delete the article.
2. Enrich the 2 roadmap topics + `freelance` (§B); delete the variant articles.
3. Build the 2 KEEP-NEW pages (§D); delete their source articles.
4. Delete §A articles (link the branded ones to the main course page from wherever they're referenced).
5. Fix any internal links that pointed at deleted articles.
6. Remove emptied `_articles/`, update `articles.md`, sitemap, and nav.
7. Resubmit sitemaps in Search Console.

Steps 1-6 are complete. Search Console sitemap resubmission remains an external
operations task. Redirects were only needed where noted above, not wholesale for
the brand-new, unindexed article URLs.
