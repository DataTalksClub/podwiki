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

Thirteenth pass (2026-07-06) used five parallel workers on the current
unstemmed content-overlap tail: data product management versus the data product
manager guide, data science versus data scientist role, and the DataOps
discipline/engineer/platform trio. The pass kept concept, role, and platform
intents separate; removed reader-facing related-page tails from edited role
pages; added body links to preserve graph depth; and added a practice-specific
artifact/interface section to data product management. At `--overlap --min-pct
35`, content-overlap findings fell from 5 to 0.

Fourteenth pass (2026-07-06) used five parallel workers on stricter graph-depth
and monitored adjacency clusters: AI coding tools, AI finance decision support,
Python stock analysis, annotation quality workflows, and Delta/Iceberg table
formats. The pass added grounded body links from distinct source pages, removed
several generic related-page tails, shortened long citation labels, and kept
comparison pages separate from concept pages. At `--overlap --min-pct 35`,
content-overlap findings remained 0. The stricter `audit_graph.py
--min-inbound 16` weak-node count improved from 125 to 121 while the official
min-12 gate remained clean.

Fifteenth pass (2026-07-06) used two five-agent graph-depth batches on weak
clusters around applied research, astroinformatics scientific pipelines,
camera-first versus LiDAR autonomous driving, services-to-product-founder,
data-analyst-to-analytics-engineer, data roles, ML consulting proposals, and
nearby pipeline/optimization pages. The pass added grounded body links, removed
generic related-page tails where links already lived in prose, and kept public
pages free of reader-facing scaffolding sections. At `--overlap --min-pct 35`,
content-overlap findings remained 0. The stricter `audit_graph.py
--min-inbound 16` weak-node count improved from 121 to 119 while the official
min-12 gate remained clean.

Sixteenth pass (2026-07-06) used five parallel workers on role and career
clusters: data engineer to data scientist, data engineering manager, data
science for managers, data scientist interview prep, and data scientist to
machine learning engineer. The pass added grounded body links from neighboring
role, portfolio, management, MLOps, and transition pages. A follow-up edit
tightened `_wiki/mlops-architecture.md` so it stays a component/interface map
rather than restating the MLOps concept or roadmap. At `--overlap --min-pct 35`,
content-overlap findings remained 0. The stricter `audit_graph.py
--min-inbound 16` weak-node count improved from 119 to 117 while the official
min-12 gate remained clean.

Seventeenth pass (2026-07-06) used five parallel workers on DataOps engineer,
DataOps tools, Delta Lake, DuckDB, and industrial ML application clusters. The
pass added grounded body links from CI/CD, testing, observability, lakehouse,
pipeline, freelancing, and industrial AI organization pages. At `--overlap
--min-pct 35`, content-overlap findings remained 0. The stricter
`audit_graph.py --min-inbound 16` weak-node count improved from 117 to 116 while
the official min-12 gate remained clean.

Eighteenth pass (2026-07-06) used five parallel workers on data roles, how to
build data pipelines, KPIs, lean MLOps for startups, and public learning for AI
careers. The pass added grounded body links from role, transition, project,
tooling, monitoring, orchestration, portfolio, freelancing, and
technical-writing pages, then removed reader-facing scaffold language that the
strict content audit flagged. At `--overlap --min-pct 35`, content-overlap
findings remained 0. The stricter `audit_graph.py --min-inbound 16` weak-node
count improved from 116 to 115 while the official min-12 gate remained clean.

Nineteenth pass (2026-07-06) used two five-agent batches on LLM/RAG production
roadmap, LLM system design interview, LLM tools, ML engineer roadmap, and ML
personalization clusters. The pass added grounded body links from LLM,
evaluation, agent, AI tooling, data-role, MLOps, recommendation, search, vector,
customer-data, and industrial ML pages. The first duplicate scan found a
temporary 35.0% vocabulary collision between LLM evaluation workflows and the
RAG evaluation workflow, so the LLM page was tightened to delegate RAG-specific
mechanics instead of repeating them. At `--overlap --min-pct 35`,
content-overlap findings returned to 0. The stricter `audit_graph.py
--min-inbound 16` weak-node count improved from 115 to 111 while the official
min-12 gate remained clean.

Twentieth pass (2026-07-06) used five parallel workers on ML system design
interview, machine learning versus software engineering, fab maintenance and
yield ML, marketer to analytics engineer, and Metaflow clusters. The pass added
grounded body links from interview, recruiter, portfolio, recommendation, ML
engineering, design-document, industrial data team, CDO, sensor baseline, data
strategy, experimentation, causal inference, MLOps, platform, registry, and
production checklist pages. At `--overlap --min-pct 35`, content-overlap
findings remained 0. The stricter `audit_graph.py --min-inbound 16` weak-node
count improved from 111 to 106 while the official min-12 gate remained clean.

Twenty-first pass (2026-07-06) used five parallel workers on ML consulting
proposals, ML platform engineer role, ML system design documents, MLOps vs
DevOps practices, and model optimization clusters, then used two focused
follow-up workers where repeated links inside already-connected pages did not
increase unique graph depth. The pass added grounded body links from consulting,
startup, salary, platform, registry, experiment-tracking, MLOps,
design-document, technical-writing, computer-vision, LLM, infrastructure, and
software-to-ML transition pages. At `--overlap --min-pct 35`, content-overlap
findings remained 0. The stricter `audit_graph.py --min-inbound 16` weak-node
count improved from 106 to 101 while the official min-12 gate remained clean.

Twenty-second pass (2026-07-06) used five parallel workers on multi-agent
systems, nontraditional AI engineering, notebook-to-production workflow,
open-source ML contributions, and product analyst vs data analyst clusters. The
pass added grounded body links from agent, LLM, evaluation, tooling,
career-transition, bootcamp, research, portfolio, notebook handoff,
open-source, product-metrics, A/B testing, KPI, and data-team pages. At
`--overlap --min-pct 35`, content-overlap findings remained 0. The stricter
`audit_graph.py --min-inbound 16` weak-node count improved from 101 to 96 while
the official min-12 gate remained clean.

Twenty-third pass (2026-07-06) used five parallel workers on product designer to
data product manager, product owner vs product manager, project manager to data
science, salary negotiation, and scikit-learn clusters. The pass added grounded
body links from discovery, data-team, founder, communication, governance,
data-mesh, personalization, project-management, compensation, freelance-pricing,
DevRel, QA-to-ML, and machine-learning-tool pages. At `--overlap --min-pct 35`,
content-overlap findings remained 0. The stricter `audit_graph.py
--min-inbound 16` weak-node count improved from 96 to 91 while the official
min-12 gate remained clean.

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
