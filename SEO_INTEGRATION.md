# Podwiki ↔ Main site: SEO integration analysis & plan

How `DataTalksClub/podwiki` (served at `datatalks.club/podwiki/`) should be
integrated with the main site (`datatalksclub.github.io`, served at
`datatalks.club/`) for maximum SEO benefit.

_Last updated: 2026-07-01._

Status note: this analysis was written before the category split in commit
`473dd0e`. The public `_articles/` collection and `/articles/` URLs have now
been retired. Editorial content lives under `_guides/`, `_comparisons/`,
`_roadmaps/`, and `_how_tos/`, with public URLs under `/guides/`,
`/comparisons/`, `/roadmaps/`, and `/how-tos/`. Keep the notes below as
historical SEO rationale and as a consolidation checklist for the migrated
editorial surface.

---

## 1. Topology — already correct, do not change

| | Repo | Served at | Mechanism |
|---|---|---|---|
| Main | `datatalksclub.github.io` | `datatalks.club/` | org Pages site (owns the CNAME) |
| Wiki | `DataTalksClub/podwiki` | `datatalks.club/podwiki/` | project Pages site, `--baseurl /podwiki` injected at build |

Subdirectory (`/podwiki/`) is the SEO-optimal choice — link equity and domain
authority stay consolidated on one host. A subdomain would split them. **Keep it.**

## 2. URL structure — fine, no action

Wiki/editorial/podcast/people URLs are ~3 segments deep
(`/podwiki/wiki/rag/`, `/podwiki/guides/data-roles/`,
`/podwiki/comparisons/mlops-vs-dataops/`). **URL/folder depth is not a ranking
factor** — click depth and internal linking are. Slugs are descriptive,
lowercase, hyphenated, with consistent trailing-slash pretty permalinks. Only
rule: **keep slugs stable once indexed.**

## 3. The real problems

### 3a. Structural duplication of the main site's entities (HIGH)

Podwiki mirrors the two biggest collections of the main site almost 1:1:

| Entity | Main | Podwiki | Shared slugs |
|---|---|---|---|
| People | 438 (`/people/x.html`) | 439 (`/podwiki/people/x/`) | **437** |
| Podcast episodes | 203 (`/podcast/x.html`) | 203 (`/podwiki/podcasts/x/`) | **200** |

Two pages per person/episode on one domain = duplicate-content / signal-splitting
risk. Podwiki's *unique* value is **wiki topics, exploration search, and the
graph** — not re-publishing people and episode pages.

### 3b. The retired article set was an Ubersuggest keyword-page swarm (HIGH)

The retired set had 71 article pages generated from `artifacts/keywords/*`
(Ubersuggest), with `keyword:` / `search_intent:` front matter. This was useful
for discovering demand but risky as a public URL surface:

- **Cannibalize the main site** on branded terms — the retired articles included
  `data-engineering-zoomcamp`, `mlops-zoomcamp`, `machine-learning-zoomcamp`,
  `llm-zoomcamp`, competing with the main site's own course pages.
- **Cannibalize podwiki's own wiki** — 9 article slugs were identical to wiki
  slugs: `data-engineering`, `dataops`, `mlops`, `mlops-tools`, `mlops-engineer`,
  `machine-learning-system-design`, `data-engineering-tools`,
  `data-engineering-certification`, `software-engineer-to-machine-learning`.
- **Doorway/thin-content clusters** — many singular/plural/synonym variants for
  one intent, e.g. `data-engineer-course` · `data-engineer-courses` ·
  `data-engineering-course` · `data-engineering-courses` ·
  `best-data-engineering-course` · `free-data-engineering-course` ·
  `data-engineering-training` · `data-engineer-training`. Google's spam /
  helpful-content systems flag these swarms and can penalize the **whole
  subdirectory**, not just those URLs.

### 3c. Discoverability gaps (MEDIUM)

- **Sitemap not advertised.** Only the root `robots.txt` (the *main* repo's) is
  read by crawlers; a project page can't override it. It lists only
  `datatalks.club/sitemap.xml`. The podwiki sitemap at
  `datatalks.club/podwiki/sitemap.xml` is invisible.
- **Crawl orphan.** No link to `/podwiki/` exists anywhere in the main site
  (grepped header/footer/index/config). Only reachable via sitemap → no internal
  link equity.
- **Absolute URLs may miss the `/podwiki` prefix.** Local build emits sitemap
  `<loc>https://datatalks.club/wiki/...</loc>` *without* `/podwiki/`. CI builds
  with `--baseurl /podwiki` (fixes `href`s) but auto-generated absolute URLs
  (sitemap `<loc>`, feed `<link>`) come from `site.url` and must be verified.
- **No canonical / OG tags** in any podwiki layout (`_layouts/*.html`).

## 4. Recommendation — what podwiki should be

Podwiki's defensible, non-duplicative surface = **Topics (wiki) + Exploration
search + Graph**. Everything else should either defer to the main site or be
consolidated into topics.

1. **People & podcast episodes → defer to the main site.** These are the main
   site's canonical entities. Either (a) `rel=canonical` each podwiki person/
   episode page to its main-site equivalent, or (b) drop standalone podwiki
   people/episode pages and surface that data only inside topic hubs + search.
   Recommended: keep podcast *summaries* only if they add clear, distinct value
   and canonical-link to the main episode page; canonicalize people to main.
2. **Keep the article replacement split — see §5.** The keyword swarm has been
   collapsed into topics and a small number of genuinely additive editorial
   formats.
3. **One canonical owner per query.** Branded/course terms (zoomcamps) →
   main site always wins. Concept terms → podwiki wiki topic wins. Comparison
   and decision queries → `_comparisons/` wins. Never two live competitors for
   the same query.

## 5. What replaced `articles/`

The keyword-page model was the liability. The completed collection split moved
the useful parts into additive formats that the main blog and wiki do not
already cover:

- **Fold into Topics (wiki).** An "article" on a concept *is* a topic hub.
  Merge the 9 article==wiki collisions and any concept articles into the wiki;
  one strong page per concept beats two thin ones.
- **Learning paths / roadmaps.** Curated sequences (e.g. "become a data
  engineer") that link OUT to topics + episodes. Additive, not a keyword clone.
- **Q&A / "ask the archive".** Question-shaped pages backed by exploration
  search — a format the main site lacks entirely.
- **Comparison / "vs" pages** (e.g. `mlops-vs-dataops`) — keep these in
  `_comparisons/` where the comparison is real and link to both topic hubs;
  drop the rest.

Net: 71 keyword articles → 0 standalone keyword pages. Surviving editorial
content now lives as focused guides, comparisons, roadmaps, and how-tos; the
rest was absorbed into wiki topics or removed. Each remaining editorial page
must target a query no main-site or wiki page already owns.

## 6. Action checklist

- [x] Main repo `robots.txt`: add `Sitemap: https://datatalks.club/podwiki/sitemap.xml`
- [x] Main repo: add nav/footer link to `/podwiki/`; podwiki links back
- [x] Verify CI sitemap `<loc>` includes `/podwiki/`; if not, set `baseurl: "/podwiki"` in `_config.yml`
- [x] Add self-referencing canonical + OG tags to podwiki `_layouts/default.html`
- [x] Canonicalize podwiki people → main `/people/`; podcast summaries → main `/podcast/`
- [x] Add explicit `canonical_url` support and canonicalize the podcast guide
  to the main podcast page
- [x] Remove branded Zoomcamp guide pages from podwiki so the main site owns
  those course queries
- [x] Retire the public `_articles/` collection and split surviving editorial
  content into `_guides/`, `_comparisons/`, `_roadmaps/`, and `_how_tos/`
- [x] Consolidate the article keyword swarm into topics + editorial formats (§5)
- [x] Remove podwiki articles that duplicate wiki slugs or target branded/course terms
  - [x] Remove exact guide/wiki slug collisions and move useful guide material
    into the wiki layer
  - [x] Remove branded Zoomcamp guide pages
  - [x] Remove duplicate data engineering course, courses, bootcamp, and
    training guide variants
  - [x] Remove duplicate MLOps course, certification, and machine learning
    bootcamp guide variants
  - [x] Consolidate freelance and consulting guide variants into
    `_wiki/freelance.md`
  - [x] Consolidate Airflow and Apache Airflow variants into
    `_wiki/orchestration.md`; keep Airflow Docker Compose as an additive
    `_how_tos/airflow-docker-compose.md` procedural page
  - [x] Consolidate analytics-engineer into
    `_wiki/analytics-engineering.md`
  - [x] Consolidate data-engineering-manager and data-engineer-manager into
    `_wiki/leadership.md`
  - [x] Consolidate data-science-for-managers into `_wiki/leadership.md`
  - [x] Keep A/B testing as wiki concept coverage, not guide/category content
- [ ] Resubmit both sitemaps in Google Search Console
