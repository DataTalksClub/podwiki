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
