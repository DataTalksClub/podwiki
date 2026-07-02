# Deduplication & SEO-Focus Review

Record of the duplication review run with `scripts/find_duplicates.py` (local
zerosearch index) plus five parallel review agents. See `CONTENT_GUIDE.md`
("Maintenance: Deduplication and SEO Focus") for how to re-run it.

## Merges executed

- **`rag` → `retrieval-augmented-generation`** — `rag.md` was a full parallel
  page covering the same guests, episodes, and timestamps as the canonical RAG
  page (a doorway duplicate). Grafted its one unique link
  (`knowledge-graph-vs-vector-search`) into the canonical page and merged.
- **`dataops-operating-model` → `dataops`** — orphan (0 inbound links) that
  re-expanded `dataops`'s delivery/testing/observability sections from the same
  Bergh episode. Ported its unique "four gates" release framing into `dataops`.
- **`startup` → `startups`** — singular/plural doorway pair covering the same
  guests, episodes, and timestamps (Samuylova, Paolino, Kruszelnicki, Brudaru,
  Radojkovic, Goyal, Wiertz). Kept the plural (better-linked hub) and ported the
  two unique guest sections from the singular page — Maria Bruckert's *Building
  Digital Health Startups* and Liesbeth Dingemans's *AI Product Design* — into a
  new "Product Strategy in High-Risk Domains" section, then removed the leftover
  singular/plural doorway framing.

## Verified and kept (NOT duplicates)

Structural review showed distinct scope + independent inbound links; merging
would lose long-tail coverage:

- **`governance` vs `data-governance`** — hub/spoke, not duplicate. `governance`
  is the cross-domain umbrella (adds ML release controls, Responsible AI review,
  LLM/agent controls); `data-governance` is the deep data-specific page. They
  already cross-link.
- **`experimentation` / `causal-inference` / `experimentation-and-causal-inference`**
  — the combined page is a well-linked (20 inbound) bridge with a "choosing the
  evidence standard" synthesis the two focused pages lack. Distinct query intents.
- **Role/roadmap/comparison families** (e.g. `data-product-manager` vs
  `-roadmap` vs `-vs-product-manager`; ML-engineer role/roadmap/transition) —
  intentionally separate intents under the tag model, not duplication.

Second pass (2026-07) re-evaluated the highest-overlap pairs the reports surface
and confirmed these are distinct-intent, not duplicates:

- **`data-activation` vs `reverse-etl`** (48% vocab) — broad activation concept
  vs the specific warehouse-to-tool sync mechanism. Both explicitly carve out
  scope ("reverse ETL is narrower than data activation") and cross-link; distinct
  head terms.
- **`event-tracking` vs `tracking-plans`** (46% vocab) — the instrumentation
  practice vs the instrumentation spec/artifact. Both are established, separately
  searched terms drawing on the same Arpit/Natalie/Jakob episodes.
- **`solopreneur` vs `solopreneur-data-scientist`** — untagged concept hub vs a
  `guide`-tagged career page with its own anchor guest (Marianna Diachuk) and a
  90-day solo-DS plan. Concept-vs-guide, distinct intent.
- **`notebook-to-production-ai-systems` vs `notebook-to-production-workflow`** —
  concept hub vs a `how-to`-tagged procedural sequence. The guide explicitly
  keeps concept vs how-to separate. (The how-to is under-linked — a linking gap
  to fix, not a merge.)
- **`data-analyst-careers` vs `data-analyst-role`** — entry routes / portfolio /
  hiring signals vs responsibilities and adjacent-role boundaries. Role-vs-career
  split; both well-linked. Skill-stack overlap could be trimmed to a cross-link
  later, but that is editorial polish, not a merge.
- **`mlops-adoption-at-scale` vs `ml-platforms`** — organizational
  change-management, tech-translator/evangelist roles, regulated-finance rollout
  (Nemanja's *MLOps in Finance*), and DataOps day-two habits (Bergh) versus the
  platform-as-internal-product page. Distinct guests and angle; the 1-inbound is
  a linking gap, not duplication.
- **`rag-portfolio-projects` vs `search-and-rag-project-checklist`** — a catalog
  of RAG project *types* (source-cited assistant, search-first, evaluation,
  agentic, graph, career-transition, production) versus a single-project
  build-and-review *checklist* (corpus/chunking, retrieval baselines, citations,
  traces, review checklist). Same evidence base and mutual cross-links, but a
  real ideation-vs-execution split; kept both under the conservative rule.

## Cross-site (vs datatalksclub.github.io) outcome

Most `find_duplicates.py --cross-site` hits were shared vocabulary with branded
Zoomcamp/course pages, which target course-signup queries and are NOT
cannibalization. Genuine article collisions were resolved by adding one canonical
link to the main article (and, for `airflow-docker-compose`, trimming a generic
install sequence the main how-to owns). Pages touched: `dataops`,
`dataops-vs-data-engineering`, `mlops`, `mlops-vs-devops`, `data-roles`,
`data-engineering-courses`, `llm-tools`, `ai-tools-for-personal-productivity`,
`agent-ops`, `airflow-docker-compose`.

## Optional consolidations for owner decision

These overlap in citations but currently serve distinct query intents. Judgment
calls — consolidate only if you want fewer, broader pages:

- **`mlops-adoption-at-scale`** (1 inbound, near-orphan) overlaps `ml-platforms`
  on platform-team/adoption content. Either fold the adoption slice into
  `ml-platforms` (using `scripts/merge_wiki_page.py`) or add inbound links so it
  is not an orphan. Its distinct angle is organizational change-management at
  scale and regulated constraints.
- **`dataops-platforms` vs `dataops-tools`** — "platform as operating layer" vs
  "what your stack should cover". Both well-linked; distinct head terms. Keep
  unless you want a single DataOps-infrastructure page.
- **`data-analyst-careers` vs `data-analyst-role`** — career/entry-route vs
  role/responsibilities. The "Skill Stack" sections overlap; consider trimming
  one to a cross-link rather than merging.
- **Hiring family** (`hiring`, `data-science-recruiter`, `cv-screening`,
  `salary-negotiation`) — reuse the same recruiter-funnel passages. Distinct by
  query; consider centralizing shared prose in `hiring` with the others
  cross-linking.

To act on any of these, move the unique content into the canonical page, then
run `python scripts/merge_wiki_page.py <source-slug> <target-slug>` and
`python scripts/check_wiki_links.py`.
