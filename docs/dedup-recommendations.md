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

Third pass (2026-07-05) used five parallel cleanup batches to sharpen page
ownership without merging distinct intents. The edited clusters were search and
vector retrieval, Delta Lake and Apache Iceberg, Airflow and orchestration, RAG
project pages, and MLOps/DataOps role-roadmap-platform pages. The pass replaced
duplicated generic explanations with links to the owning concept pages, removed
reader-facing routing phrases, and kept inline podcast citations. At the same
thresholds used for the previous pass, overlap findings moved from 40 to 39 and
internal near-duplicate findings moved from 75 to 73.

The remaining high-scoring pairs are mostly expected concept/comparison or
concept/tool neighbors. Treat them as candidates for boundary edits first, not
automatic merges:

- **`apache-airflow` vs `orchestration`** — tool page versus general
  control-plane concept.
- **`delta-lake-vs-apache-iceberg` vs `delta-lake` / `apache-iceberg`** —
  comparison page versus format-specific concept hubs.
- **`vector-database-vs-search-engine` vs `vector-databases` /
  `vector-search-vs-keyword-search`** — infrastructure boundary versus storage
  concept and retrieval-method comparison.
- **`mlops-architecture` vs `mlops-engineer` / `mlops-roadmap`** — system
  component map versus role accountability and learning sequence.
- **`rag-evaluation-workflow` vs `rag-portfolio-projects`** — evaluation
  procedure versus portfolio proof.

Fourth pass (2026-07-05) tightened another five duplicate-report clusters:
machine-learning infrastructure versus ML platforms, machine-learning system
design versus the interview guide, ETL versus ELT and the comparison, event
tracking versus tracking plans, and analyst-role comparisons. The system-design
interview, ETL/ELT, and tracking-plan pairs dropped out of the current duplicate
tails after the pass. The remaining ML infrastructure versus ML platforms hit is
still a distinct-intent pair: infrastructure owns workload components and
constraints, while platforms own the shared internal product surface.

Fifth pass (2026-07-05) tightened data-engineering tools versus modern data
stack, data-product-manager versus owner comparison, data-scientist interview
prep versus roadmap, embeddings versus vector-search comparison, and open-source
concept versus contributor roadmap. The pass kept these as distinct intents:
tool selection versus architecture composition, role hub versus title-boundary
comparison, round expectations versus preparation sequence, representation
concept versus retrieval-method comparison, and concept/community hub versus
staged contribution path.

Sixth pass (2026-07-05) tightened AI red teaming versus chatbot risk, portfolio
hub versus role-specific portfolio pages, analyst-to-analytics-engineer
transition versus role comparison, information retrieval versus vector-search
infrastructure, and DataOps engineer versus platform pages. The pass preserved
separate intents by moving generic overlap into cross-links: adversarial testing
process versus chatbot control design, general portfolio evidence versus
role-specific proof, career sequence versus responsibility comparison, retrieval
modeling versus infrastructure ownership, and staffing accountability versus
shared platform packaging.

Seventh pass (2026-07-05) used five parallel workers on the highest remaining
overlap clusters: Airflow versus orchestration, RAG portfolio versus project
checklist versus RAG concept, MLOps architecture versus engineer/roadmap/tools,
DataOps concept versus comparison/platform pages, and vector/search pages. The
pass kept each page family distinct by pushing implementation detail to tool or
checklist pages, moving broad concept framing back to hubs, and using cross-links
instead of repeated definitions. At the same thresholds, content-overlap findings
fell from 38 to 36 while internal near-duplicate findings stayed at 70.

Eighth pass (2026-07-05) tightened another five high-overlap families: Delta
Lake and Apache Iceberg concept pages versus their comparison, autonomous
driving hub versus camera-first/LiDAR comparison, graph/vector retrieval pages,
product-analyst role and comparison boundaries, and community/DevRel pages. The
pass kept concept pages on durable topic ownership and comparisons on decision
criteria. At the same thresholds, content-overlap findings fell from 36 to 33
and internal near-duplicate findings fell from 70 to 69.

Ninth pass (2026-07-05) used five parallel workers on vector/search, DataOps,
MLOps, data-engineering transition/roadmap/portfolio, and
experimentation/evaluation families. The pass pushed generic procedure and
checklist material back to owning pages, tightened role/roadmap/comparison
boundaries, and kept citations in the relevant body sections. At the same
thresholds, content-overlap findings fell from 33 to 26 while internal
near-duplicate findings stayed at 69.

Tenth pass (2026-07-05) used five parallel workers on the highest remaining
content-overlap pairs: Airflow versus orchestration, analyst-to-data-engineer
transition versus the data engineer roadmap, DataOps versus DataOps platforms,
data mesh concept versus mesh/central-platform comparison, and AI engineering
concept versus roadmap. The pass kept each page pair separate by making concept
pages own definitions and durable boundaries while comparison, roadmap, and
transition pages own decisions, sequence, or career reframing. At the same
thresholds, content-overlap findings fell from 12 to 7.

Eleventh pass (2026-07-05) used five parallel workers on the remaining
content-overlap pairs: data-scientist-to-machine-learning-engineer versus the
machine-learning-engineer role, founder versus startups, MLOps architecture
versus roadmap, RAG portfolio projects versus the project checklist,
machine-learning system design versus interview prep, AI infrastructure versus
machine-learning infrastructure, and graph RAG versus knowledge-graph/vector
search. A follow-up stylint pass split the prose into the same file groups. The
pass kept transition, role, concept, roadmap, comparison, checklist, and
portfolio intents distinct. At the same thresholds, content-overlap findings
fell from 7 to 0.

Twelfth pass (2026-07-05) used five parallel auditors on the remaining high
internal near-duplicate clusters after content-overlap fell to zero. No content
edits were needed. The auditors confirmed these are monitored adjacency
clusters, not merge candidates: Delta Lake/Apache Iceberg concept pages versus
their comparison; search, information-retrieval, relevance, vector-search, and
vector-database pages; Graph RAG/vector-search pages; product-analyst role
versus comparison; evolutionary-algorithms versus game-AI-to-LLM-agents; and
developer-relations versus open-source DevRel. Keep watching these with
`find_duplicates.py`, but treat `--overlap --min-pct 35` as the action trigger
unless a manual page read shows same-intent duplication.

Search/vector spot check (2026-07-06): no public wiki edits were made. The
current unstemmed `python scripts/find_duplicates.py --overlap --min-pct 35`
report has five pairs, none in the search/vector/RAG retrieval family. The
search/vector pages still rank highly in the BM25 near-duplicate report - for
example vector databases versus vector search, graph RAG versus graph/vector
search, information retrieval versus search, and production search evaluation
versus search relevance - but those remain expected adjacency clusters. Keep
using the unstemmed overlap command above as the action trigger for this family;
BM25-only hits should prompt a page read, not an automatic merge.

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
