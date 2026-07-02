# Podcast Mining Report — pod_10 (17 episodes)

Read-only mining pass. Sources: `_podcast_summaries/<slug>.md` chapter summaries;
coverage checked against `_wiki/` (273 pages) and `search/search-corpus.json`.
Target pages are existing `_wiki/` slugs unless marked NEW PAGE/BORDERLINE.

---

## applied-llm-research-and-career-growth-in-practice
Guest: Lavanya Gupta (s20e07) — LLM benchmarking at a financial institution.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Long-context LLM performance drops ~32k–64k | long-context-llm-evaluation | ENRICH | long-context-llm-evaluation | Empirical droparound 32k–64k (12:36); EMNLP paper "Long Context LLMs on Financial Concepts" (15:28) |
| Chunking/retrieval/summarization for large docs vs raw long context | retrieval-augmented-generation, context-engineering | CONNECTION | long-context-llm-evaluation → retrieval-augmented-generation | RAG fallback when context window degrades (14:54) |
| Publishing research from corporate/industry teams (arXiv, endorsement) | applied-research | ENRICH | applied-research | Manager support, community sharing, arXiv endorsement path (17:28–22:10) |
| Streamlit for rapid demos + feedback loops | notebook-to-production-ai-systems, ai-product-feedback-loops | CONNECTION | notebook-to-production-ai-systems | Prototyping tool for stakeholder feedback (30:14) |
| Building + licensing a high-impact Kaggle dataset | competitions-beyond-kaggle, portfolio-projects | ENRICH | competitions-beyond-kaggle | Dataset creation (not just competing) as career asset (33:24) |
| Portfolio: community visibility vs job-targeted projects | data-scientist-cv-and-portfolio | CONNECTION | data-scientist-cv-and-portfolio | Two portfolio strategies contrasted (51:28) |
| Career pivot from non-CS backgrounds into data | career-transitions-in-data | CONNECTION | career-transitions-in-data | Non-CS entry + cold outreach/rapport (45:24, 48:28) |
| Interview prep: LeetCode + conceptual mastery + mock interviews | data-scientist-interview | ENRICH | data-scientist-interview | Named guest prep breakdown (54:33) |
| Women in Data Science / open mentoring | community-building | CONNECTION | community-building | WiDS + open mentoring (37:32) |

## building-and-scaling-data-team
Guest: Tammy Liang (s5e06) — Chief of Data, e-commerce.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Hiring order: analyst → engineer → senior early | hiring, team-building, hire-data-engineers | ENRICH | team-building | "Rethinking hiring order: senior hires early" lesson (15:04, 23:11, 26:26) |
| First-hire qualities: business alignment + leadership mindset | team-building, data-team-lead-role | CONNECTION | team-building | First-hire profile (33:09) |
| dbt tests + regular dashboard checks for accuracy | data-quality-and-observability, dbt | ENRICH | data-quality-and-observability | dbt tests + monitoring cadence; rebuilding trust via playbook (35:38, 40:09) |
| Driving adoption via workshops/Q&A/data culture | data-product-adoption | ENRICH | data-product-adoption | Adoption workshops overcoming spreadsheet culture (10:06, 49:00) |
| Building a data warehouse to enable forecasting | data-warehouse | CONNECTION | data-warehouse | Warehouse as forecasting enabler (17:11) |
| Modern stack: Stitch, GCP, dbt, Data Studio, Notion | modern-data-stack | CONNECTION | modern-data-stack | Concrete small-team stack (22:32) |
| Offline attribution (surveys, TV/banner measurement) | metrics, experimentation | CONNECTION | metrics | Measuring untrackable channels via surveys/sampling (45:39) |
| Product mindset for data products + delegation leadership | data-product-management, leadership | CONNECTION | data-product-management | Product mindset + business alignment (47:08, 50:52) |

## building-production-ml-platform-and-mlops-team
Guest: Simon Stiebellehner (s14e08) — ML platform lead, fintech.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| MLOps = people + processes + technology | mlops | CONNECTION | mlops | Named guest definition (4:42) |
| Core platform skills: cloud, Kubernetes, Terraform | ml-platform-engineer-role, machine-learning-infrastructure | ENRICH | ml-platform-engineer-role | Platform skill set + specialist/generalist balance (8:11, 13:50) |
| Build-vs-buy + platform triggers (standardization across teams) | ml-platforms, mlops-architecture | ENRICH | ml-platforms | When to build; single-team SaaS value first (16:52, 17:14, 20:04) |
| Experiment tracking as low-hanging fruit | experiment-tracking | CONNECTION | experiment-tracking | Reproducibility/collaboration entry point (29:41) |
| Model registry for downstream consumption | model-registry | CONNECTION | model-registry | Persisting models (30:32) |
| Batch inference vs online serving patterns | batch-vs-streaming, llm-deployment | CONNECTION | batch-vs-streaming | Deployment pattern choice (31:15) |
| Thin abstraction layers over cloud (developer experience) | developer-experience, platform-engineering | ENRICH | developer-experience | Thin abstractions over cloud providers (38:40) |
| GDPR/regulatory constraints on logging + dataset storage | data-governance, privacy-engineering-for-ml | ENRICH | data-governance | Fintech compliance shaping metadata/lineage/logging (39:54, 45:50) |
| Business-first: models before heavy platform investment | lean-mlops-for-startups, mlops-adoption-at-scale | CONNECTION | lean-mlops-for-startups | Parallelize minimal platform pieces alongside use (47:08, 49:19) |
| Unified prediction API schemas for monitoring | model-monitoring, machine-learning-system-design | CONNECTION | model-monitoring | API/logging schema for monitoring+analytics (54:15) |

## data-engineering-tools-modern-data-stack
Guest: Natalie Kwong (s5e02, Airbyte) — decoding DE acronyms.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| ETL vs ELT (traditional vs warehouse-native) | etl-vs-elt, etl, elt | ENRICH | etl-vs-elt | CAC use case + analyst-autonomy argument for ELT (6:37, 7:57) |
| Analytics engineer emergence via dbt + SQL | analytics-engineering | CONNECTION | analytics-engineering | Empowering analysts with dbt (12:39) |
| Data marts vs warehouses (layers/consumption) | data-warehouse | CONNECTION | data-warehouse | Mart vs warehouse purpose/layers (15:30) |
| Data lakes + preventing data swamps via governance | data-lake, data-governance | ENRICH | data-lake | Swamp prevention; lake vs warehouse convergence (19:50, 21:22, 24:24) |
| CDC: row-level change capture | cdc | CONNECTION | cdc | CDC + schema/slowly-changing evolution (45:59, 48:58) |
| Reverse ETL (warehouse tables back to sources) | reverse-etl, data-activation | CONNECTION | reverse-etl | Operational reverse flows (35:42) |
| Airflow orchestration + Airbyte E-L + dbt integration | apache-airflow, orchestration, dbt | CONNECTION | modern-data-stack | Best-of-breed stack components (30:59, 33:45) |
| Low-code/no-code evolves DE roles, not replaces | data-engineer-role | CONNECTION | data-engineer-role | Tools reshape, don't eliminate DE (39:06) |
| Open-source strategy + licensing risk (Elasticsearch) | open-source | ENRICH | open-source | MIT/cloud model + relicensing risk (43:45, 48:26, 49:32) |

## data-science-career-abc-framework
Guest: Danny Ma (s2e07) — ABC (Analyst/Builder/Consultant) framework.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| ABC framework: Analyst / Builder / Consultant profiles | career-development (brief mention only) | ENRICH | data-roles | Full three-profile model (11:29–48:49); only glanced at in career-development today — worth grounding on data-roles |
| Type A analyst: exploration, viz, storytelling | data-analyst-role, data-analysis | CONNECTION | data-analyst-role | Type A skillset (13:17, 18:20) |
| Type B builder: ML eng, MLOps, production, tech debt | machine-learning-engineer-role | CONNECTION | machine-learning-engineer-role | Production mindset + systemic risk (25:53, 28:26) |
| Type C consultant/leader: stakeholder persuasion | data-science-for-managers, leadership | CONNECTION | data-science-for-managers | Hands-on → people management (42:38, 48:49) |
| A→B transition tools: Git, Docker, cloud | data-scientist-to-machine-learning-engineer | ENRICH | data-scientist-to-machine-learning-engineer | Core transition toolset + practice outside work (33:12, 36:46) |
| Learn-by-building: projects first, theory when needed | portfolio-projects | CONNECTION | portfolio-projects | Build-first learning strategy (20:01) |
| DS roadmap: SQL → viz → ML → deep learning | data-science-careers | CONNECTION | data-science-careers | Sequenced roadmap (1:19:05) |
| Bootcamps: benefits, limits, realistic expectations | data-science-careers | ENRICH | data-science-careers | Bootcamp expectations + apprenticeship model (1:12:26) |
| Lean DS team: tech lead + data lead roles | team-building | CONNECTION | team-building | Lean team composition (54:48) |

## data-translator-role-and-data-strategy
Guest: Lior Barak (s3e04) — author, "Data is Like a Plate of Hummus".

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data strategist as translator business↔tech | data-translator-role | ENRICH | data-translator-role | Named guest role definition + product-minded translator profile (4:08, 13:15) |
| Proactive alerts to maintain data trust | data-trust-and-strategy, communication | ENRICH | data-trust-and-strategy | Proactive alerting; confidence intervals + QA dashboards (7:46, 10:48) |
| Data-led growth (recruitment, marketing, ops) | data-led-growth | CONNECTION | data-led-growth | Using data across functions (17:33) |
| Lean delivery: MVPs, iteration, OKRs; prototype-first | data-product-adoption, data-strategy | ENRICH | data-strategy | "Embrace imperfect code"; hummus quick-prototype vs crafted product (23:54, 26:17, 34:52) |
| Handover strategy for productionization | notebook-to-production-workflow | CONNECTION | notebook-to-production-workflow | Creating ownership for productionizing prototypes (29:19) |
| Explaining effort to non-technical stakeholders | communication, business-skills-for-data-professionals | CONNECTION | communication | Plain-language effort framing (36:33) |
| Breaking silos via co-working/lunches; remote triggers | data-teams, communication | CONNECTION | data-teams | Cross-team empathy tactics (39:44, 42:55) |
| Book "Data is Like a Plate of Hummus" (stable ground before models) | data-strategy | CONNECTION | data-strategy | Book grounds strategy-foundations claim (51:36, 53:20); link to main-site book page, don't duplicate |

## fairness-in-ai-ml-engineering
Guest: Tamara Atanasoska (s19e09) — Fairlearn/scikit-learn/skops maintainer.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Group fairness + Fairlearn (visualization, mitigation) | responsible-ai-and-governance, machine-learning-tools | ENRICH | responsible-ai-and-governance | Fairlearn tooling; credit-scoring gender-disparity study (14:52, 21:31) |
| Metric tradeoffs: FP vs FN, demographic parity | responsible-ai-and-governance | ENRICH | responsible-ai-and-governance | Who owns the fairness tradeoff (28:52, 31:33) |
| Sensitive group selection is domain-specific, not automatable | responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance | Human judgment limits (24:04, 26:21) |
| Human-in-the-loop essential for fair systems | annotation-quality-workflows, responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance | HITL + cross-functional moderation (35:23, 37:13) |
| Interpretability: inspection pkg, partial dependence | interpretability | ENRICH | interpretability | Probable/`inspection` tooling + partial dependence (42:54) |
| skops secure model persistence vs pickle vulnerabilities | security, scikit-learn | ENRICH | security | Pickle deserialization risk; skops + HuggingFace persistence (46:20, 47:16) |
| Open-source contribution path (good-first-issues, sprints) | open-source-ml-contributions | CONNECTION | open-source-ml-contributions | Contributing to Fairlearn; OSS → role at Probable (39:18, 52:10) |
| Cross-library estimator-API compatibility | scikit-learn | CONNECTION | scikit-learn | Fairlearn/sklearn estimator API interop (44:54) |

## from-iot-data-engineering-to-leading-data-architect
Guest: Loic Magnien (s15e08) — civil-eng IoT → data architect.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data architect role: seniority, end-to-end ownership, modeling | data-architect-role | ENRICH | data-architect-role | Named guest scope; hands-on vs stakeholder balance over time (22:47, 37:10) |
| Medallion lakehouse layering (bronze/silver/gold) | data-warehouse-vs-data-lakehouse, delta-lake | ENRICH | data-warehouse-vs-data-lakehouse | Bronze/silver/gold + data-quality expectations (29:56) |
| Dimensional modeling (facts, dims, metrics) + stakeholder discovery | data-warehouse | CONNECTION | data-warehouse | Core model for multiple consumers (32:58, 36:00) |
| IoT/sensor pipelines: loggers → ingestion → reporting | data-pipelines | CONNECTION | data-pipelines | End-to-end IoT pipeline; structural health monitoring (9:21, 3:24) |
| Domain expertise (civil eng) aiding data diagnosis | data-architect-role | CONNECTION | data-architect-role | Domain knowledge for data diagnosis (11:27) |
| Career path: data manager → engineer → architect/lead | career-transitions-in-data | CONNECTION | career-transitions-in-data | Automation → DE → architect progression (1:45, 7:21) |
| Reusable ingestion/transform/datamart templates | data-engineering-platforms, data-pipelines | ENRICH | data-engineering-platforms | Reusable components vs project-specific tradeoff (57:12, 59:34) |
| Technology scouting + agile POC delivery | modern-data-engineering-trends | CONNECTION | data-architect-role | Draft specs → POC pipelines → iterate (50:45, 53:28) |

## generative-ai-chatbots-in-production-security
Guest: Maria Sukhareva (s19e06) — Principal Key Expert in AI, Siemens.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Large-scale chatbot hacking exercise + findings | ai-red-teaming, prompt-injection-and-chatbot-risk-management | ENRICH | ai-red-teaming | Bot-safety challenge; concrete red-team findings (9:28) |
| Data exfiltration via prompt overloading + KB retrieval | prompt-injection-and-chatbot-risk-management | ENRICH | prompt-injection-and-chatbot-risk-management | Exfiltration technique + layered defenses (13:20, 16:15) |
| Non-LLM classifiers as robust alternative to manipulable models | prompt-injection-and-chatbot-risk-management, security | CONNECTION | prompt-injection-and-chatbot-risk-management | Deterministic classifiers vs generative for safety (17:00) |
| Chatbot failures: hallucinations, legal/financial exposure | llm-production-patterns, generative-ai | ENRICH | llm-production-patterns | Real incidents; trust/adoption risk (11:38, 18:01) |
| Chatbot adoption: usability, verbosity, ROI | data-product-adoption, generative-ai | CONNECTION | llm-production-patterns | Verbosity/ROI as adoption blockers (20:39) |
| Human-in-the-loop hybrid review to improve accuracy | annotation-quality-workflows | CONNECTION | llm-production-patterns | Hybrid review; AI-as-assistant/autopilot analogy (25:34, 27:13) |
| Controlled machine translation with ChatGPT prompts | prompt-engineering, nlp | CONNECTION | prompt-engineering | Prompt-customized MT with quality control (29:53, 32:28) |
| Democratization of GenAI → new "AI experts" via prompting | prompt-engineering, ai-engineering | CONNECTION | ai-engineering | Prompting lowers barrier, reshapes expertise (5:42) |

## how-to-stand-out-in-data-science
Guest: Marijn Markus (s8e02) — sociology → DS.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Diverse/non-CS backgrounds as competitive advantage | data-science-careers, career-transitions-in-data | ENRICH | data-science-careers | Sociology/qualitative methods as differentiator (4:02, 11:16) |
| Hiring pitfall: keyword-driven recruitment + role mismatch | job-descriptions, hiring | ENRICH | job-descriptions | Keyword-matching recruitment failure mode (6:49) |
| Three pillars: statistics + programming + domain | data-science-careers | CONNECTION | data-science-careers | Core pillars; double down on strengths (7:42, 8:31) |
| Proactive task ownership + stretch assignments | career-growth | CONNECTION | career-growth | High-impact work; "bite off more" (12:05, 28:23) |
| Unique portfolio projects vs only Kaggle | data-scientist-cv-and-portfolio, portfolio-projects | ENRICH | data-scientist-cv-and-portfolio | Coffee-machine/IoT-plant home projects as differentiators (36:21, 37:49) |
| Communicating sensitive/risky insights (XAI) | interpretability, communication | CONNECTION | communication | Risky findings + constructive pushback to seniors (19:12, 23:25) |
| Soft skills / niche expertise as differentiation | data-science-careers | CONNECTION | data-science-careers | Presence + niche as standout factors (53:34) |
| LinkedIn growth + personal branding strategy | learning-in-public-ai-career-switch | ENRICH | learning-in-public-ai-career-switch | Timing/content-mix/hashtags; memes + authenticity (57:30, 1:02:24) |

## last-mile-data-delivery-and-data-product-adoption-modern-data-stack
Guest: Caitlin Moorman (s5e08) — Locally Optimistic.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| The "last mile" of data delivery vs modern-stack plumbing | data-product-adoption, data-products | ENRICH | data-product-adoption | Defining last-mile execution gap (8:48, 13:24) |
| Diagnose poor adoption: treat data as a product + user research | data-product-management, data-product-adoption | ENRICH | data-product-adoption | Product-design mindset, personas, user research (26:21, 32:25) |
| Outcome-first design: start from the decision to enable | data-product-intake-and-prioritization | CONNECTION | data-product-intake-and-prioritization | Start projects from target decision (34:00, 38:15) |
| Simplifying A/B-test stats for decision-makers | a-b-testing, experimentation | CONNECTION | a-b-testing | Communicating experiment results simply (28:42) |
| Pareto/80-20 high-leverage analytics work | data-product-intake-and-prioritization | CONNECTION | data-product-intake-and-prioritization | High-leverage question selection, start with financials (16:45, 47:30) |
| Low-fidelity prototyping (sketches/whiteboards) for data | data-product-management | CONNECTION | data-product-adoption | Low-fi prototyping + rapid feedback (39:32) |
| Cultural barriers: incentives + trust/discoverability | data-product-adoption, data-trust-and-strategy | CONNECTION | data-product-adoption | Incentives/behavior + trust/interpretability (20:02, 24:13) |
| Measuring hard-to-track work (proxies, time studies) | metrics, kpis | CONNECTION | metrics | Proxies + time studies for untrackable impact (42:18) |
| Linear vs circular (exploratory) project management | data-science-project-management | CONNECTION | data-science-project-management | Managing uncertainty in exploratory work (58:11) |

## mentoring-in-tech-how-to-find-and-become-a-mentor
Guest: Rahul Jain (s1e05) — mining eng → DE leadership.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Mentoring in tech (find/become a mentor) — whole-episode topic | none (scattered mentions, no hub) | BORDERLINE→NEW PAGE | Mentoring in Tech | No dedicated wiki page; grounded by full episode + cross-guest mentions (Lavanya WiDS, Supreet/DataBuzz, Danny Ma mentors). Strongest gap in this batch |
| Finding a mentor: networks, cold outreach, platforms | job-search, community | CONNECTION | community-building | Cold-outreach best practices: specificity, background, follow-up (12:50, 16:30) |
| Coaching vs managing; when to use external mentors | leadership, data-science-for-managers | CONNECTION | leadership | Coaching vs managing distinction (39:50) |
| Benefits of being a mentor (pattern recognition, growth) | career-growth | CONNECTION | career-growth | Listening/pattern-recognition growth for mentor (25:10) |
| "Advice Monster" / empathy + listening skills | communication | CONNECTION | communication | Avoiding advice-giving reflex (30:40) |
| Imposter syndrome + tech-vs-management choice (mentee) | career-development, career-growth | CONNECTION | career-development | Common mentee challenges (36:40) |
| Paid mentorship: accountability, pricing, boundaries | freelance-data-and-ml-careers | CONNECTION | career-development | When to charge / professional coaching (42:30, 45:10) |
| Blended technical + leadership career paths | data-engineering-manager-role, leadership | CONNECTION | leadership | Balancing IC work + leadership (33:30) |

## modern-search-systems-vector-databases-llms-semantic-retrieval
Guest: Atita Arora (s17e02) — Qdrant, search consultant.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Vector databases (Qdrant, plug-and-play vector search) | vector-databases | ENRICH | vector-databases | Named guest overview; vectors-in-existing-search vs standalone DB (17:01, 20:27) |
| Evolution of search: NLP, personalization, learning-to-rank, LLMs | search, search-relevance | ENRICH | search | Full arc Solr/Lucene → LTR → LLM (4:42, 23:00) |
| RAG reduces hallucinations (retrieve → augment → generate) | retrieval-augmented-generation | CONNECTION | retrieval-augmented-generation | RAG concept + prompt design/citations (30:38, 42:49) |
| Chunking/overlap/embedding-model ingest strategy | retrieval-augmented-generation, embeddings | CONNECTION | retrieval-augmented-generation | Ingest: chunking, overlap, vectorization (38:24) |
| RAG evaluation: multi-level metrics, offline + HITL | rag-evaluation-workflow | ENRICH | rag-evaluation-workflow | Multi-level metrics; "Human-in-the-Loop" reading (48:09, 50:52) |
| Building a chatbot from podcast transcripts + Whisper | rag-portfolio-projects, search-and-rag-project-checklist | CONNECTION | rag-portfolio-projects | Concrete transcript-RAG build (35:49) |
| Vector DBs for session-based recs + re-ranking | recommendation-systems, machine-learning-personalization | CONNECTION | machine-learning-personalization | Session-based vs collaborative filtering (52:07, 54:54) |
| Langchain orchestration in RAG pipelines | llm-tools, retrieval-augmented-generation | CONNECTION | llm-tools | Langchain role (41:32) |
| Learning resources: Intro to IR, Relevant Search | information-retrieval, search-relevance | CONNECTION | information-retrieval | Canonical reading list (57:50) |

## practical-llm-engineering-and-rag
Guest: Hugo Bowne-Anderson (s22e04) — Vanishing Gradients, freelance/DevRel.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Generator-Evaluator pattern (automated output QC) | llm-production-patterns, llm-evaluation-workflows | ENRICH | llm-evaluation-workflows | Generator-evaluator / LLM-as-judge for QC (13:56) |
| Eval sets: gold tests, size, cost, representativeness | llm-evaluation-workflows | ENRICH | llm-evaluation-workflows | Eval sets + failure analysis/error categorization (23:00, 26:43) |
| Chunking strategies + "context rot" | context-engineering, retrieval-augmented-generation | ENRICH | context-engineering | Fixed/sliding-window chunking, context rot (48:20) |
| When to move from RAG to agents / tool calls | agent-engineering, rag-vs-fine-tuning | ENRICH | agent-engineering | RAG-first, add tooling later; 4-step agent framework (50:19, 56:21) |
| Vibe coding + monitoring (logging, traces, debuggable MVPs) | ai-coding-tools, llmops | CONNECTION | llmops | Observability for LLM apps (27:38) |
| Dev assistants: Copilot, Cursor, IDE agents, Slack agents | ai-coding-tools | ENRICH | ai-coding-tools | Embedded/proactive agents in workflows (31:56, 33:14) |
| Agent memory: retrieval-based vs multi-turn conversation | context-engineering, agent-engineering | CONNECTION | agent-engineering | Memory design distinction (57:41) |
| Driving AI adoption via loss aversion + experimentation time | ai-product-feedback-loops, generative-ai | CONNECTION | ai-engineering | Loss aversion + dedicated experimentation time (8:24) |
| Consulting/advisory + DevRel freelance path | freelance-data-and-ml-careers, developer-relations | CONNECTION | freelance-data-and-ml-careers | Consulting vs advisory distinction (7:11) |
| Everyday LLM use: summaries, translation, CSV; prompting | prompt-engineering | CONNECTION | prompt-engineering | Role prompts, structured output (9:28, 11:11) |

## responsible-explainable-ai-bias-detection
Guest: Supreet Kaur (s10e09) — Morgan Stanley, DataBuzz founder.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Explainable vs Responsible AI (post-mortem tools vs governance mindset) | responsible-ai-and-governance, interpretability | ENRICH | responsible-ai-and-governance | Named distinction: XAI tooling vs governance mindset (8:20) |
| Local interpretability: LIME, SHAP, surrogate models | interpretability | ENRICH | interpretability | LIME/SHAP/surrogate + What-If, Skater, AIX360 (19:03, 23:24) |
| Data-level fairness checks (skewness, missingness, coverage) | responsible-ai-and-governance, data-quality-and-observability | CONNECTION | responsible-ai-and-governance | EDA for bias detection (11:36, 12:48) |
| PII handling: masking, use-case justification | privacy-engineering-for-ml, data-governance | ENRICH | privacy-engineering-for-ml | Age/gender masking + feature-necessity decisioning (14:39, 17:20) |
| Drift + feedback loops (demographics, KS tests) | model-monitoring | ENRICH | model-monitoring | KS tests, overfitting, demographic drift (37:31) |
| Accuracy vs interpretability tradeoff | interpretability | CONNECTION | interpretability | Managing model-complexity tradeoff (32:29) |
| Cross-functional governance (SMEs, compliance, leadership) | responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance | Ethics vs profitability + governance roles (24:22, 27:38) |
| AutoML risks: democratization without oversight | responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance | AutoML democratization risk (50:17) |
| Hiring-tool historical-bias case + remediation | cv-screening, responsible-ai-and-governance | CONNECTION | cv-screening | Biased hiring model remediation lessons (44:07) |

## s23e09-starting-data-conference-data-makers-fest-story
Guest: Leonid Kholkine (s23e09) — Data Makers Fest.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Conference operations (scheduling, venue, sponsorship) | data-ai-conference-building (already cites episode) | ENRICH | data-ai-conference-building | Add specifics: automated timetable optimization (36:52), sponsorship/student tickets (45:47) |
| Professional growth through community organizing | community-building, career-growth | CONNECTION | community-building | Organizing → network + growth |
| Data Lead Club + executive networking retreats | community-building | CONNECTION | community-building | Executive peer format (10:18) |
| Curating quality CFP proposals in the AI era | data-ai-conference-building | CONNECTION | data-ai-conference-building | AI-era proposal curation (41:22) |
| Forward Deployed Engineer role + methodology | none (only this summary in corpus) | BORDERLINE | ai-engineer-role / data-roles | FDE defined (54:44); one brief mention — connect to a role hub, don't create standalone page yet |
| AI observability / R&D | agent-ops, model-monitoring | CONNECTION | agent-ops | AI observability work (14:03) |
| ML research in sports physiology | sensor-ml-personal-baselines | CONNECTION | sensor-ml-personal-baselines | Sports-physiology ML (6:13) |

## trends-in-modern-data-engineering
Guest: Adrian Brudaru (s20e03) — dltHub co-founder.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| dlt as Python-based ingestion standard | data-engineering-tools, modern-data-engineering-trends | ENRICH | modern-data-engineering-trends | dlt ingestion standard + DLT Plus + reusable-data-product marketplace (4:03, 59:42) |
| Apache Iceberg: table format, vendor lock-in reduction | apache-iceberg | ENRICH | apache-iceberg | Parquet storage, catalog role, lock-in reduction (18:17, 21:27) |
| DuckDB: embeddable local OLAP + cheap pipelines | duckdb | ENRICH | duckdb | DuckDB + GitHub Actions headless pipelines (25:58, 27:40) |
| Table format comparison: Delta vs Hudi vs Iceberg | delta-lake-vs-apache-iceberg | ENRICH | delta-lake-vs-apache-iceberg | Delta/Hudi/Iceberg differences (49:42) |
| dbt influence + alternatives (SQLMesh) | dbt | CONNECTION | dbt | SQLMesh as dbt alternative (31:29) |
| Orchestration options 2025: Airflow/Prefect/Dagster/GH Actions | orchestration | ENRICH | orchestration | 2025 orchestration landscape (35:37) |
| Streaming: micro-batching, Kafka, SQS, Flink | streaming, batch-vs-streaming | CONNECTION | streaming | Streaming architecture options (51:19) |
| AI engineering convergence: DEs building AI agents | ai-engineering, modern-data-engineering-trends | CONNECTION | modern-data-engineering-trends | DE→AI-agent convergence + code-gen commoditization (38:02, 56:15) |
| Modern-stack critique + "postmodern" OSS alternatives | modern-data-stack, modern-data-engineering-trends | CONNECTION | modern-data-stack | Critique + vendor caution (14:32, 44:42) |
| Beginner DE roadmap + senior-backend transition | data-engineer-roadmap, devops-to-data-engineering | CONNECTION | data-engineer-roadmap | SQL/Python/requirements roadmap; senior backend → DE (41:06, 45:56) |

---

## Tally
- Items mined: 17 episodes
- Total ideas: ~145
- CONNECTION: ~78 | ENRICH: ~63 | NEW PAGE: 0 | BORDERLINE: 2
  (Mentoring in Tech — BORDERLINE leaning NEW; Forward Deployed Engineer — BORDERLINE leaning CONNECTION)
