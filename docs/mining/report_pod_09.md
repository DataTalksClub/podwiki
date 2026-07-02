# Podcast Mining Report — pod_09 (17 episodes)

Read-only mining. Coverage checked via `grep -ril <slug> _wiki` (wiki uses
`[[podcast:<slug>]]` link syntax) and the wiki page list. Actions prefer
CONNECTION/ENRICH; NEW PAGE reserved for genuine gaps.

Legend: CONN = graph edge to add; ENR = add specific evidence to existing page;
BORD = borderline new page.

---

## analytics-to-data-science-with-kaggle-portfolio (Andrada Olteanu, S3E2)
Already cited on: machine-learning-portfolio-projects, portfolio-projects, data-scientist-cv-and-portfolio, data-science-careers.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Kaggle notebooks as public portfolio | ml-portfolio-projects, portfolio-projects | ENR | machine-learning-portfolio-projects | Olteanu ~9:43/32:14 Kaggle+GitHub as hiring artifact |
| Analyst→DS path (~1yr self-paced pivot) | data-science-careers | CONN | career-transitions-in-data | Udemy+Kaggle+YouTube pivot, 52:54 |
| Transferable analyst skills (validation, EDA, domain) | data-analyst pages | CONN | data-analyst-careers | 36:41 bridge into DS |
| Learn-by-reproducing notebooks method | none | ENR | machine-learning-portfolio-projects | 45:16 decompose/reimplement/debug |
| Algo coding tests vs practical ML | data-scientist-interview | CONN | data-scientist-interview | 26:07 screen mismatch |
| Mentorship via Kaggle → hiring | none | ENR | machine-learning-portfolio-projects | 18:09 portfolio as networking |
| Master's vs independent study | academic-researcher-to-data-science | CONN | data-science-careers | 49:27 tradeoff |
| LinkedIn/Twitter project showcase | data-scientist-cv-and-portfolio | ENR | data-scientist-cv-and-portfolio | 1:01:00 |

## building-and-scaling-data-science-practice-industrial-ai-mlops (Andrey Shtylenko, Honeywell, S11E5)
Cited on: computer-vision, data-teams, data-engineering-and-data-science.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Crawl→Walk→Run maturity model | data-strategy; mlops-adoption-at-scale (not cited) | ENR | mlops-adoption-at-scale | 24:26 org maturity staging |
| Single E2E POC to prove value | production-ml-project-checklist | CONN | mlops-adoption-at-scale | 32:00 adoption wedge |
| Centralized vs embedded vs hub-and-spoke | data-teams (cited) | ENR | data-teams | 43:39-48:13 topology tradeoffs |
| Reporting line CTO/CIO/CMO/CEO | chief-data-officer-role | CONN | chief-data-officer-role | 19:06 |
| Shared services (exp tracking, annotation, procurement) | experiment-tracking, annotation-quality-workflows | CONN | data-teams | 50:14 |
| Industrial AI adoption barriers | industrial-ml-applications | CONN | industrial-ml-applications | 13:46 sensorization precondition |
| Internal SWE→DS pivot & timing | software-engineer-to-machine-learning | CONN | software-engineer-to-machine-learning | 52:39/55:07 |
| Expand scope for org impact | career-growth | ENR | career-growth | 59:44 |

## building-open-source-nlp-tool (Johannes Hotter, S13E9)
Cited on: nlp, embeddings, open-source-and-developer-relations, open-source.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Weak supervision / labeling functions (Refinery) | annotation-quality-workflows (NOT cited) | CONN | annotation-quality-workflows | 6:33/19:48 heuristics-as-ensemble |
| ChatGPT/LLM as labeling heuristic | annotation-quality-workflows | CONN | annotation-quality-workflows | 13:22 GPT+active learning+crowd |
| Bricks heuristic recipe library | none | ENR | annotation-quality-workflows | 18:33 |
| Open-core model (distribution vs revenue) | open-source | ENR | open-source | 28:11/31:47 |
| Developer-focused GTM via DevRel/trust | developer-relations | CONN | developer-relations | 40:21 |
| Consultancy→product pivot (Kern) | consultant-or-freelancer-to-data-product-founder | CONN | consultant-or-freelancer-to-data-product-founder | 20:22 |
| PDF/document NLP niche | nlp | ENR | nlp | 52:40 |
| Fundraising for OSS ML (2.7M) | founder | CONN | founder | 57:02 |

## data-engineering-leadership-and-modern-data-platforms (Rahul Jain, S7E7)
Well-connected (13 pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| ETL→ELT + data lake + lineage at scale | elt (cited) | ENR | elt | 30:50 |
| IC vs people-mgmt time split for DE managers | data-engineering-manager-role (cited) | ENR | data-engineering-manager-role | 8:54 |
| Non-negotiable vs stretch expectations | leadership (cited) | ENR | data-engineering-manager-role | 23:15 |
| DE success metrics (culture, consumers, quality) | data-quality-and-observability | CONN | data-observability-for-data-engineering | 25:04 |
| Data reconciliation source↔target | dataops-checks-for-data-pipelines | CONN | dataops-checks-for-data-pipelines | 28:04 |
| GDPR dynamic masking + RBAC | data-governance | CONN | data-governance | 29:01 |
| Interview buzzword filtering | hire-data-engineers | CONN | hire-data-engineers | 49:35 |
| Fundamentals (DBMS/SQL) over tools | data-engineer-roadmap | CONN | data-engineer-roadmap | 54:34 |

## data-science-and-analytics-for-nonprofits-tech-for-good (Parvathy Krishnan, S13E2)
Only cited on: data-strategy (already covers maturity mapping well, lines 237-243).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Data maturity across people/process/tech | data-strategy (cited) | — | data-strategy | already integrated |
| Discovery workshops before tools | data-strategy | ENR | data-strategy | 6:20 |
| Descriptive→diagnostic→predictive→optimization | data-strategy | ENR | data-strategy | 22:26 analytics ladder |
| Analytics translator / academy tiers | data-translator-role | CONN | data-translator-role | 17:53 |
| Optimization use cases (Nairobi waste, COVID labs) | none | ENR | data-strategy | 9:29/50:06 |
| Nonprofit vs private maturity gap | data-strategy | ENR | data-strategy | 12:33 |
| Small core + extended research network | data-teams | CONN | data-teams | 54:07 |
| Low-resource stack (KoboToolbox, PostgreSQL) | data-engineering-tools | CONN | data-strategy | 44:18 |
| AI for social good motivation | data-science-careers | BORD | (analytics-for-social-good) | resolve as ENR on data-strategy |

## data-team-roles (Alexey Grigorev, S1E1)
Very well-connected (22 role pages). Foundational role-taxonomy source.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| PM keeps team close to user | data-product-manager (cited) | ENR | data-product-manager | 3:38/6:13 |
| DE-before / DS-after boundary | data-engineer-vs-data-scientist (cited) | ENR | data-engineer-vs-data-scientist | 30:01 |
| MLE skills overlap engineers | machine-learning-engineer-role (cited) | ENR | machine-learning-engineer-role | 17:04/20:54 |
| Roles depend on team size | data-teams (cited) | ENR | data-teams | 34:35 |
| Shared metric ownership for ML product | data-teams | CONN | data-product-management | 24:55 |
| Web eng vs ML eng nature of work | machine-learning-for-software-engineers | CONN | machine-learning-engineer-role | 38:52 |

## devrel-open-source-machine-learning (Hugo Bowne-Anderson, S14E6)
Very well-connected (16 pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| DevRel "wisdom layer" definition | developer-relations (cited) | ENR | developer-relations | 18:03 |
| OSS governance (company-backed Dask/Metaflow) | open-source, metaflow (cited) | ENR | open-source | 10:47 |
| DevRel org models / reporting | developer-relations | ENR | developer-relations | 22:52 |
| Dogfooding to teach reproducibility | reproducibility (cited) | CONN | reproducibility | 36:27 |
| Content strategy (awareness/support/OSS + media ROI) | technical-writing (cited) | ENR | technical-writing | 43:14/48:43 |
| AI-assisted drafting (Whisper/ChatGPT) | ai-tools-for-personal-productivity | CONN | technical-writing | 40:17 |
| DevRel↔marketing (SEO/content) | developer-relations | ENR | developer-relations | 27:17 |
| Education→DevRel path | open-source-contributor-roadmap | CONN | developer-relations | 14:34 |

## from-game-ai-to-modern-ai-agents (Micheal Lanham, S21E7)
Very well-connected (14 pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Evolutionary algorithms for prompt engineering | evolutionary-algorithms, prompt-engineering (cited) | ENR | prompt-engineering | 14:09 |
| Minimal agent workflow + task decomposition | agent-engineering (cited) | ENR | agent-engineering | 20:57 |
| Flow vs orchestration (pipelines vs manager agents) | multi-agent-systems (cited) | ENR | multi-agent-systems | 23:48 |
| Agent tooling (OpenAI Agent SDK + MCP) | agent-engineering | CONN | agent-engineering | 31:31 |
| Sequential-thinking servers / scratchpads | context-engineering | CONN | context-engineering | 33:25 |
| Local models / small specialized LLMs | llm-deployment (cited) | ENR | llm-deployment | 45:40/48:40 |
| Eval/monitoring pipelines (Arize Phoenix) | llm-evaluation-workflows, agent-ops | CONN | agent-ops | 57:39 |
| GenAI procedural game content | generative-ai (cited) | ENR | generative-ai | 38:57 |

## from-startup-engineering-to-freelance-data-science (Antonis Stellas, S14E5)
Under-connected: only startups, machine-learning-tools. Freelance hubs miss it.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Upwork playbook (profile/proposals/pricing) | data-freelancing-strategy (NOT cited) | CONN | data-freelancing-strategy | 30:33-40:39 |
| Learning from proposal rejection / specializing | freelance-data-and-ml-careers (NOT cited) | CONN | freelance-data-and-ml-careers | 37:09 |
| Freelancer admin (registration/invoicing) | data-freelancing-strategy | ENR | data-freelancing-strategy | 45:18 |
| Model monitoring: drift + Evidently AI | model-monitoring | CONN | model-monitoring | 21:00 |
| Lean build-measure-learn for ML | lean-mlops-for-startups | CONN | lean-mlops-for-startups | 17:39 |
| Startup "many hats" skill growth | startups (cited) | ENR | startups | 11:56 |
| OSS contribution as portfolio (Evidently/Hacktoberfest) | open-source-portfolio-evidence | CONN | open-source-portfolio-evidence | 28:43 |
| MLOps project (MLflow/Prefect/Grafana) | mlops-tools | CONN | machine-learning-portfolio-projects | 25:12 |

## how-to-grow-your-ml-engineering-career (Krzysztof Szafanek, S12E7)
Cited on: ml-platform-engineer-role, machine-learning-for-software-engineers, career-growth, machine-learning-engineer-role.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| ML platform work (zflow) | ml-platform-engineer-role (cited) | ENR | ml-platform-engineer-role | 13:25 |
| LLMs for coding/architecture sparring + caveats | ai-coding-tools | CONN | ai-coding-tools | 22:01 |
| Transferable skills + Lindy effect | machine-learning-for-software-engineers (cited) | ENR | machine-learning-for-software-engineers | 29:00 |
| T-shaped depth+breadth strategy | career-growth (cited) | ENR | career-growth | 35:23 |
| Debugging as career strength | none | ENR | machine-learning-for-software-engineers | 37:37 |
| Engineer→consultant transition | ml-platform-engineer-role | CONN | career-growth | 17:48 |
| Generalists vs specialists in ML market | hiring, job-descriptions | CONN | machine-learning-engineer-role | 50:22/54:23 |
| Prompt engineering practical tips | prompt-engineering | CONN | prompt-engineering | 26:46 |

## knowledge-graphs-and-llms-for-automotive-rnd (Anahita Pakiman, S18E2)
Very well-connected (9 KG/RAG pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| KG+LLM grounding to reduce hallucination | graph-rag-vs-vector-rag (cited) | ENR | graph-rag-vs-vector-rag | 33:43/42:42 |
| Graph vs tabular (clustering, load-path) | knowledge-graph-vs-vector-search (cited) | ENR | knowledge-graph-vs-vector-search | 20:32 |
| KG semantics vs chunk+embedding+vector DB | retrieval-augmented-generation | ENR | retrieval-augmented-generation | 38:10 |
| Cypher/prompt-template KG retrieval | graph-rag-vs-vector-rag | CONN | graph-rag-vs-vector-rag | 39:56 |
| Graph ML measures (SimRank, PageRank on papers) | none specific | ENR | knowledge-graph-vs-vector-search | 28:00/47:10 |
| FEA vs ML numerical vs data-driven | industrial-ml-applications | CONN | industrial-ml-applications | 8:05 |
| RAG vs transfer learning/fine-tuning | rag-vs-fine-tuning (cited) | ENR | rag-vs-fine-tuning | 40:23 |
| Streamlit limits for graph app | none | CONN | rag-portfolio-projects | 55:36 |

## mentoring-in-tech-how-to-find-and-become-a-mentor (Rahul Jain, S1E5)
Under-connected: career-development, career-growth. No dedicated mentoring page.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Mentoring types (one-off vs long-term) | career-development (cited) | ENR | career-development | 6:10/22:30 |
| Cold outreach best practices | community-building, career-development | ENR | career-development | 16:30 |
| Preparing sessions (goals/agenda) | career-development | ENR | career-development | 19:40 |
| Avoid "advice monster" / listening | leadership, teaching | CONN | leadership | 30:40 |
| Coaching vs managing; external mentors | data-science-for-managers | CONN | data-science-for-managers | 39:50 |
| Paid mentorship (accountability/pricing) | teaching | CONN | teaching | 45:10 |
| Imposter syndrome / tech-vs-mgmt choice | career-transitions-in-data | CONN | career-growth | 36:40 |
| Mentoring-in-tech as its own topic | teaching/community/career (partial) | BORD | (mentoring) | no hub; ENR career-development unless keywords given |

## modern-data-pipelines-orchestration-ingestion-modeling (Santona Tuli, S14E7)
Very well-connected (22 pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| MLOps vs DataOps | mlops-vs-dataops (cited) | ENR | mlops-vs-dataops | 18:44 |
| Upsolver vs dbt (authoring vs execution) | dbt (cited) | ENR | dbt | 10:48 |
| Ingestion pre-proc (dedup/ordering/PII) | dataops-checks-for-data-pipelines (cited) | ENR | dataops-checks-for-data-pipelines | 37:10 |
| Staging/lakehouse; managed ingestion hides stage | data-warehouse-vs-data-lakehouse (cited) | ENR | data-warehouse-vs-data-lakehouse | 32:57 |
| Build vs buy | modern-data-stack (cited) | ENR | modern-data-stack | 29:16 |
| Persona-driven pipeline design | data-pipelines (cited) | ENR | data-pipelines | 52:54 |
| ML vs analytics pipeline | mlops-architecture (cited) | ENR | mlops-architecture | 13:25 |
| Generalist value / closing gaps | data-engineer-roadmap (cited) | ENR | data-engineer-roadmap | 55:56 |

## practical-generative-ai-consulting-from-expertise-to-impact (Verena Weber, S16E5)
Under-connected: solopreneur, nlp, consultant-or-freelancer-to-data-product-founder.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Model-in-the-loop annotation study (time/consistency) | annotation-quality-workflows (NOT cited) | CONN | annotation-quality-workflows | 23:11/25:20 |
| GenAI consulting pitch deck / rates | ml-consulting-proposals (NOT cited) | CONN | ml-consulting-proposals | 39:03 |
| Finding clients (network/events/LinkedIn) | data-freelancing-strategy (NOT cited) | CONN | data-freelancing-strategy | 41:59/51:42 |
| GenAI workshops + use-case discovery | generative-ai, ml-consulting-proposals | CONN | ml-consulting-proposals | 32:07 |
| Research role without PhD | applied-research | CONN | applied-research | 6:56 |
| Business impact over publication counts | applied-research | ENR | applied-research | 16:26 |
| Self-employment realities | solopreneur (cited) | ENR | data-freelancing-strategy | 37:55 |
| Eval to stabilize high-traffic utterances | model-monitoring | CONN | model-monitoring | 27:47 |

## research-to-production-ml-systems-roadmap (Mihail Eric, S5E5)
Well-connected (9 pages).

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| DS 1.0 → 2.0 (production DS) | notebook-to-production-workflow (cited) | ENR | notebook-to-production-workflow | 20:25 |
| Researchers learn eng rigor/reproducibility | reproducibility (cited) | ENR | reproducibility | 23:32 |
| Engineers learn uncertainty/experimental rigor | applied-research (cited) | ENR | applied-research | 28:50 |
| Embedded teams vs over-the-wall handoffs | data-teams | CONN | data-teams | 34:20 |
| Full-stack data scientist | notebook-to-production-ai-systems (cited) | ENR | notebook-to-production-ai-systems | 40:33 |
| Researchers build E2E & deploy | academic-researcher-to-data-science (cited) | ENR | academic-researcher-to-data-science | 44:36 |
| Code reviews fast-track eng skills | reproducibility | CONN | software-engineer-to-machine-learning | 46:57 |
| Engineers read papers/reproduce | applied-research | ENR | applied-research | 47:51 |

## s23e07-understanding-ai-engineer-role (Nasser Qadri, S23E7)
Cited on: ai, ai-engineering-roadmap, llm-deployment, agent-ops, llm-evaluation-workflows, ai-engineering, model-optimization, ai-engineer-role.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Statistical rigor for GenAI eval | llm-evaluation-workflows (cited) | ENR | llm-evaluation-workflows | 7:45 |
| Research mindset vs eng speed | ai-engineer-role | CONN | ai-engineer-role | 12:13 |
| AI roles big tech vs startups | ai-engineer-role (cited) | ENR | ai-engineer-role | 20:27 |
| Beyond API calls: SWE rigor for agents | agent-engineering | CONN | agent-engineering | 42:05 |
| Orchestration & Agent Ops | agent-ops (cited) | ENR | agent-ops | 45:50 |
| Depth vs breadth in framework selection | ai-tooling | CONN | ai-tooling | 51:30 |
| Latency + traditional ML with LLMs | llm-production-patterns | CONN | llm-production-patterns | 56:10 |
| When to distill / fine-tune | model-optimization (cited) | ENR | model-optimization | 1:01:20 |

## theme-park-crowd-modeling-to-tesla-full-stack-data-engineering (Abouzar Abbaspour, S21E9)
Cited on: recommendation-systems, data-engineering-and-data-science, industrial-ml-applications.

| idea | coverage | action | target | specifics |
|---|---|---|---|---|
| Crowd modeling (queue prediction, capacity) | industrial-ml-applications (cited) | ENR | industrial-ml-applications | 7:36 |
| Next-best-action visitor routing recommender | recommendation-systems (cited) | ENR | recommendation-systems | 12:59 |
| Rec validation via employee swiping + A/B | a-b-testing | CONN | a-b-testing | 24:03 |
| Real-time streaming for live experiments | streaming, batch-vs-streaming | CONN | streaming | 26:01 |
| Full-stack data work (apps/instrumentation) | data-engineering-and-data-science (cited) | ENR | data-engineering-and-data-science | 34:21 |
| On-prem inference hw (Pi/Jetson Orin/Mac Mini) | ai-infrastructure | CONN | ai-infrastructure | 46:06 |
| LLM-assisted dev gains + risks (Tesla) | ai-coding-tools | CONN | ai-coding-tools | 41:43 |
| App-adoption incentives to bootstrap data | data-product-adoption | CONN | data-product-adoption | 14:50 |

---

## Tally
Across 17 episodes, ~130 ideas mapped.
- CONNECTION: ~58
- ENRICH: ~66
- NEW PAGE: 0
- BORDERLINE: 2 (mentoring hub; analytics-for-social-good)

No confident NEW PAGE — the wiki already has hubs for every substantive topic
these episodes raise. Both borderlines resolve to ENRICH on existing pages
unless the user supplies target keywords for a guide/how-to.

## Highest-value edges
1. Weak-supervision + model-in-the-loop annotation → annotation-quality-workflows (Hotter Refinery/Bricks + ChatGPT-as-labeler; Weber model-in-the-loop study). Page cites neither.
2. Freelance/consulting episodes orphaned from freelance hubs: from-startup-engineering-to-freelance-data-science and practical-generative-ai-consulting not cited on data-freelancing-strategy, freelance-data-and-ml-careers, or ml-consulting-proposals.
3. Industrial maturity model → mlops-adoption-at-scale (Shtylenko crawl→walk→run + single-E2E-POC + hub-and-spoke); episode not cited there.
4. Theme-park recommender validation → a-b-testing / data-product-adoption (employee-swiping offline validation + app-adoption incentives).
5. data-team-roles (S1E1) is a foundational role-taxonomy anchor already linked from 22 role pages; keep citing for role-boundary definitions.
