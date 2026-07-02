# Podcast mining report — batch pod_03

17 podcast episodes mined. Sources: `_podcast_summaries/<slug>.md` chapter maps
(cross-checked against `_wiki/` via `grep -ril` and `search/search-corpus.json`).
Most episodes are already cited in several wiki pages, so most rows are edges/
evidence to add, not new pages.

---

## ai-in-healthcare-and-digital-therapeutics (Stefan Gudmundsson, S8E4)
Already cited on 6 pages (machine-learning-personalization, healthcare-ml-validation-and-adoption, a-b-testing, recommendation-systems, model-monitoring-vs-data-observability, ai-powered-business-intelligence).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| A/B testing as foundation for personalization | a-b-testing (cites) | ENRICH | a-b-testing | 39:57 segmentation/iteration; 43:00 experimentation platform |
| Agenda-driven recommender systems in a health app | recommendation-systems (cites), machine-learning-personalization | ENRICH | machine-learning-personalization | 35:39 goal-driven personalization |
| Clinical trials vs app experiments (scale, cost, bias) | healthcare-ml-validation-and-adoption (cites) | ENRICH | healthcare-ml-validation-and-adoption | 45:29 trials vs in-app; 49:25 speed over perfection |
| GDPR/HIPAA, de-identification, empathy | privacy-engineering-for-ml | CONNECTION | privacy-engineering-for-ml | 31:41 health-data privacy example |
| Behavioral design, low in-app time | machine-learning-personalization | ENRICH | machine-learning-personalization | 15:04 minimize in-app time; 25:43 charity vs leaderboards |
| Remote monitoring & wearables (activity, HRV) | sensor-ml-personal-baselines | CONNECTION | sensor-ml-personal-baselines | 29:33 wearable signals |
| Safeguards for safe experimentation (medical risk) | responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance | 51:55 high-stakes experimentation safeguards |
| Building AI/data teams (King, H&M, Sidekick) | data-team-lead-role | CONNECTION | data-team-lead-role | 2:08 team building across domains |
| AI for mental health monitoring | healthcare-ml-validation-and-adoption | ENRICH | healthcare-ml-validation-and-adoption | 55:53 mental-health signals |

## biohacking-productivity-for-data-scientists-and-ml-engineers (Ruslan Shchuchkin, S13E3)
Only on career-development.md. circadian/dopamine keywords absent elsewhere in _wiki.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Behavioral vs chemical biohacking | career-development (cites) | ENRICH | career-development | 6:56 |
| Circadian light: morning sun, cortisol/melatonin, daylight lamps | none | CONNECTION | career-development | 18:41, 26:14 |
| Dopamine/motivation; dopamine resets, voluntary discomfort | none | ENRICH | career-development | 9:31, 43:25 |
| Sleep planning (90-min cycles, alarm timing) | none | ENRICH | career-development | 27:50 |
| Habit tracking (steps/exercise/hydration), Notion dashboards | none | CONNECTION | sensor-ml-personal-baselines | 38:07, 48:21 personal self-tracking |
| Procrastination/perfectionism; prioritize five goals | none | ENRICH | career-development | 4:51, 53:45, 55:21 |
| Failed experiments (fasting, cold showers); n=1 caveats | none | ENRICH | career-development | 41:16, 45:47 |
| "Biohacking for data scientists" as own topic | career-development only | BORDERLINE | (career-development) | single-episode niche, off-domain; keep folded, don't make a page |

## building-domestic-risk-assessment-tool (Sabina Firtala, S18E7)
UNDER-CONNECTED: only on responsible-ai-and-governance.md. Rich end-to-end social-impact ML project.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Risk-scoring model architecture | responsible-ai-and-governance (cites) | ENRICH | responsible-ai-and-governance | 18:00 architecture; 21:40 validation |
| Data cleaning/linking/feature engineering from mixed sources | entity-resolution, end-to-end-data-pipeline-project | CONNECTION | entity-resolution | 10:45 sources; 14:20 record linking |
| Privacy & legal compliance in high-stakes scoring | privacy-engineering-for-ml | CONNECTION | privacy-engineering-for-ml | 25:15, 29:00 |
| Deploy into frontline workflows + decision-support UI | notebook-to-production-workflow, data-products | CONNECTION | notebook-to-production-workflow | 32:10, 35:50 |
| Drift detection & alerts for deployed risk model | model-monitoring | CONNECTION | model-monitoring | 42:20 |
| Bias assessment / fairness in scoring | responsible-ai-and-governance (cites) | ENRICH | responsible-ai-and-governance | 21:40 |
| Stakeholder trust, training, adoption | data-product-adoption | CONNECTION | data-product-adoption | 39:05 |
| End-to-end social-impact ML as portfolio pattern | machine-learning-portfolio-projects | CONNECTION | machine-learning-portfolio-projects | full arc template |
| NGO/agency collaboration, funding, sustainability | none | ENRICH | responsible-ai-and-governance | 52:10, 55:00 non-profit ML context |

## cloud-data-governance (Jessi Ashdown & Uri Gilad, S3E10)
Well cited (7 pages). data-governance.md is the hub.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Governance = people+processes+tools, beyond security/PII | data-governance (cites) | ENRICH | data-governance | 6:40, 14:04 |
| Cloud + regulation (GDPR, Cambridge Analytica) drove adoption | data-governance | ENRICH | data-governance | 8:57 |
| Data classification & taxonomy | data-governance | ENRICH | data-governance | 24:14, 15:33 |
| Data catalog: tools vs spreadsheets; metadata/lineage/glossary | data-engineering, model-registry | CONNECTION | data-engineering | 27:48, 54:37 |
| Data stewards/producers/decision-makers | data-teams, data-governance | ENRICH | data-governance | 33:03 |
| Policies as enablement / guardrails; shopping-cart access | self-service-data-platforms | CONNECTION | self-service-data-platforms | 42:04, 47:02 |
| Enforcement: catalog interface vs storage control plane | data-governance | ENRICH | data-governance | 45:04 |
| Measuring governance ROI | data-governance, data-trust-and-strategy | ENRICH | data-governance | 50:19 |
| Minimum Viable Governance | data-governance | ENRICH | data-governance | 53:21, 19:40 |
| Tools: Dataplex, Collibra | data-governance | CONNECTION | data-governance | 47:35 |

## data-leadership-coaching (Tereza Iofciu, S18E1)

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| IC → lead transition challenges | data-team-lead-role, leadership | CONNECTION | data-team-lead-role | 6:17, 9:15 |
| Feedback culture / psychological safety | team-building, leadership | ENRICH | team-building | 19:43, 20:18 |
| Making data work visible (foundation, product mindset, KPIs) | data-science-for-managers, kpis | CONNECTION | data-science-for-managers | 24:32 |
| Influencing without authority; stakeholder framing | leadership, communication | ENRICH | leadership | 46:00, 49:20 |
| Span of control ("pizza" metaphor) | data-team-lead-role | ENRICH | data-team-lead-role | 12:38 |
| Self-promotion vs bragging; personal retrospectives | career-growth, data-scientist-cv-and-portfolio | CONNECTION | career-growth | 36:14, 38:33 two-year rule |
| Coaching vs mentoring vs advice (blended) | leadership | ENRICH | leadership | 34:38 |
| Inclusive leadership | leadership, team-building | ENRICH | team-building | 54:24 |

## data-science-leadership-hiring-mlops (Mariano Semelman, S6E9)
Well cited (5 pages). Head of DS at OLX.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Product-first mindset: user impact over modeling | machine-learning-for-business | ENRICH | machine-learning-for-business | 29:29, 36:50 |
| Start simple/fail fast; Rules of ML | notebook-to-production-workflow | CONNECTION | notebook-to-production-workflow | 33:36, 30:06 |
| CRISP-DM + deployment realities | data-science-project-management (has CRISP-DM) | ENRICH | data-science-project-management | 36:12 |
| Search/recsys, RTB/campaign optimization | recommendation-systems, algorithmic-trading | CONNECTION | recommendation-systems | 19:57, 21:19 |
| 30-60-90 onboarding plan for new managers | staff-ai-engineer, data-team-lead-role | CONNECTION | data-team-lead-role | 12:52, 15:16 |
| Diagnosing model issues (overfit, data, features) | machine-learning | ENRICH | machine-learning | 26:16 |
| Feedback technique: ask permission, care, options | team-building | ENRICH | team-building | 44:17 |
| Hiring, probation, remediation plans | hiring, data-teams | CONNECTION | hiring | 55:48 |
| Manager who still codes; delegation | data-team-lead-role | ENRICH | data-team-lead-role | 52:37, 54:58 |

## datatalksclub-building-scaling-data-community (Eugene Yan & Alexey Grigorev, S7E1)

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Scaling a data community to ~9k | community-building | ENRICH | community-building | 10:05, 16:54 |
| Event formats (OSS Spotlight, Minis, Book of the Week) | community-building, open-source-and-developer-relations | ENRICH | community-building | 24:38 |
| Content automation (Zapier, Eventbrite) | community-building | ENRICH | community-building | 20:22 |
| Monetization/sponsorship (TopCoder, Toloka) | community-building, data-ai-conference-building | CONNECTION | community-building | 31:37 |
| ML Zoomcamp/Bookcamp: project-based end-to-end learning | teaching, machine-learning-portfolio-projects | CONNECTION | teaching | 38:22, 39:06 |
| Tool-evaluation: avoid churn, follow lasting trends | machine-learning-tools, modern-data-engineering-trends | CONNECTION | machine-learning-tools | 45:40 |
| Just-in-time learning by projects/notes | learning-in-public-ai-career-switch | CONNECTION | learning-in-public-ai-career-switch | 50:31 |
| Public deadlines/accountability/batching | career-development | ENRICH | career-development | 48:56 |
| Principal DS role: internal consulting/architecture/mentoring | data-scientist-role, data-science-careers | CONNECTION | data-scientist-role | 6:27 |

## from-academia-to-staff-ai-engineer-interviews-and-career-growth (Tatiana Gabruseva, S12E9)
Well cited (5 pages). staff-ai-engineer.md hub.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Staff AI engineer archetypes | staff-ai-engineer (cites) | ENRICH | staff-ai-engineer | 11:04 |
| Skipping mid-level: staff role from academia | academic-researcher-to-data-science | CONNECTION | academic-researcher-to-data-science | 19:08 |
| Translating research/grants to industry impact | academic-researcher-to-data-science (cites) | ENRICH | academic-researcher-to-data-science | 21:26, 25:30 |
| Coding interview strategy (LeetCode plan) | data-scientist-interview-roadmap | CONNECTION | data-scientist-interview-roadmap | 34:40 |
| ML design interview: decomposition + mocks | machine-learning-system-design-interview | CONNECTION | machine-learning-system-design-interview | 39:44, 43:36 |
| Referrals/networking; reframing rejections | job-search, career-growth | CONNECTION | job-search | 29:41, 32:08 |
| Onboarding shock + mentorship | staff-ai-engineer | ENRICH | staff-ai-engineer | 3:24, 17:45 |
| Staff in MLOps/ETL/pipelines; code-review load | mlops-engineer, staff-ai-engineer | ENRICH | staff-ai-engineer | 51:10, 52:19 |
| Recommended staff-engineering books | staff-ai-engineer | ENRICH | staff-ai-engineer | 59:45 |

## from-radio-astronomy-to-machine-learning-and-data-engineering (Daniel Egbo, S21E5)
Cited on 4 pages. astroinformatics-scientific-data-pipelines.md hub.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| MEERKAT/SKA data workflow; point-source detection | astroinformatics-scientific-data-pipelines (cites) | ENRICH | astroinformatics-scientific-data-pipelines | 10:39, 6:19 |
| Multi-wavelength cross-matching; positional uncertainty | entity-resolution, astroinformatics | CONNECTION | entity-resolution | 11:50, 13:35 as a matching problem |
| Physics-based verification with domain priors | astroinformatics | ENRICH | astroinformatics-scientific-data-pipelines | 15:30 |
| Curated datasets as ML foundation | astroinformatics | ENRICH | astroinformatics-scientific-data-pipelines | 17:54 |
| Python astronomy tooling at scale (Astropy/NumPy/SciPy) | machine-learning-tools | CONNECTION | astroinformatics-scientific-data-pipelines | 24:33 |
| ML Zoomcamp → reusable/production code | teaching, notebook-to-production-workflow | CONNECTION | notebook-to-production-workflow | 26:58 |
| Edge deployment on Intel hardware | notebook-to-production-ai-systems, ai-infrastructure | CONNECTION | ai-infrastructure | 31:26 |
| End-to-end pipeline: MySQL→MinIO→Spark→warehouse; Kestra/Airflow | end-to-end-data-pipeline-project, batch-vs-streaming, apache-airflow | CONNECTION | end-to-end-data-pipeline-project | 42:48, 45:15, 44:08 |
| Domain expert → ML/DE transition | career-transitions-in-data, academic-researcher-to-data-science | CONNECTION | academic-researcher-to-data-science | 57:59 |

## hiring-and-managing-data-science-teams-in-b2b-saas (Katie Bauer, S11E2)
Well cited (12 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data scientist as broad/varied role | data-scientist-role (cites) | ENRICH | data-scientist-role | 7:08, 6:22 |
| Craft quality: maintainability/docs/peer review for analytics | analytics-engineering, software-engineering | CONNECTION | analytics-engineering | 11:58 |
| Career framework: junior/senior/"terminal" level | career-growth, data-science-careers | CONNECTION | career-growth | 15:12, 18:50 |
| IC vs management pendulum | data-team-lead-role | ENRICH | data-team-lead-role | 25:54 |
| Hiring juniors: build vs buy, succession | hiring, data-teams | ENRICH | hiring | 40:12 |
| Evaluating DS manager candidates | hiring, data-team-lead-role | CONNECTION | hiring | 44:39, 47:21 |
| Entry-level standing out: outreach, prep | data-scientist-interview, job-search | CONNECTION | job-search | 50:21 |
| Onboarding first month: proactive comms, async help | staff-ai-engineer, team-building | CONNECTION | team-building | 52:43, 54:11 |
| Head-of-data challenges: prioritization, data literacy | data-strategy, data-science-for-managers | CONNECTION | data-science-for-managers | 56:20 |

## human-centered-mlops-and-model-monitoring (Lina Weichbrodt, S4E6)
Heavily cited (18 pages). model-monitoring.md cites her.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Project intake checklist: business case, KPIs, alternatives | model-monitoring/machine-learning-for-business | ENRICH | machine-learning-for-business | 4:50, 9:43 quantify alternatives |
| ML incident response: post-mortems, Five Whys, ML recovery | model-monitoring (cites); no dedicated page | ENRICH | model-monitoring | 24:34, 27:14, 32:11, 39:26 |
| Live test sets + small A/B tests for detection | model-monitoring, a-b-testing | ENRICH | model-monitoring | 29:23 |
| Data monitoring: input distribution, unit changes, feature drift | model-monitoring, data-quality-and-observability | ENRICH | model-monitoring | 46:28 |
| Explainability vs debugging — when to use XAI | interpretability | CONNECTION | interpretability | 44:11, 37:12 credit-scoring surprise |
| Observability: log features, feature stores, reproducibility | feature-stores, reproducibility | CONNECTION | feature-stores | 49:28 |
| Stakeholder buy-in: fears → mitigations/metrics | leadership, machine-learning-for-business | CONNECTION | machine-learning-for-business | 18:29 |
| Demos vs reporting to build belief | data-product-adoption | CONNECTION | data-product-adoption | 22:36 |
| Standalone "ML incident response/post-mortems" page? | scattered | BORDERLINE | (model-monitoring) | distinct how-to intent but thin/one-episode; fold in unless more episodes support |

## machine-learning-decision-optimization (Dan Becker, S2E6)
Cited only on reinforcement-learning/evolutionary-algorithms/deep-learning (via guest), NOT on business/finance pages. Prescriptive/decision-optimization near-absent in _wiki (only data-strategy mentions "prescriptive"; no OR-Tools/Gurobi anywhere).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Gap: ML predictions vs real-world decisions | machine-learning-for-business (adjacent) | ENRICH | machine-learning-for-business | 3:00 core argument |
| Prescriptive analytics in ML pipelines | none dedicated | ENRICH | machine-learning-for-business | 6:00 |
| Formulating optimization: objectives + constraints | none | ENRICH | machine-learning-for-business | 9:00, 35:00 |
| Robust/stochastic optimization under uncertainty | none | CONNECTION | machine-learning-for-business | 12:00, 51:30 |
| Aligning loss with business objectives | machine-learning-for-business, metrics | ENRICH | machine-learning-for-business | 18:45 |
| Solvers: OR-Tools, Gurobi, Pyomo | none (no wiki mention) | CONNECTION | machine-learning-tools | 22:00 |
| Supply chain, pricing/bidding/revenue use cases | ai-for-finance-decision-support, algorithmic-trading | CONNECTION | ai-for-finance-decision-support | 28:30, 32:00 |
| Skillset blend: DS + OR + SWE | data-roles, machine-learning-engineer-role | CONNECTION | machine-learning-for-business | 46:30 |
| Dedicated decision-optimization/prescriptive-analytics page | no wiki page; heavy in search corpus | BORDERLINE | (new: decision-optimization) | real topic gap but grounded mainly by one episode (+RTB in Semelman); prefer ENRICH now, promote only if ≥3 episodes support |

## mlops-and-ml-engineering-in-finance (Nemanja Radojkovic, S17E5)
Well cited (11 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Finance use cases: compliance, AML, fraud, doc automation | ai-for-finance-decision-support, mlops | ENRICH | ai-for-finance-decision-support | 10:35 |
| Regulated/legacy constraints; approvals | mlops-adoption-at-scale, responsible-ai-and-governance | CONNECTION | mlops-adoption-at-scale | 18:52, 22:25 |
| Integrating ML into corporate DevOps | mlops-vs-devops, ci-cd | CONNECTION | mlops-vs-devops | 23:39 |
| On-prem infra: Hadoop, OpenShift | machine-learning-infrastructure, ai-infrastructure | CONNECTION | machine-learning-infrastructure | 27:51 |
| "MLOps on a shoestring" — minimal viable MLOps | lean-mlops-for-startups | ENRICH | lean-mlops-for-startups | 31:02, 31:57, 35:57 S3 as interim registry |
| Team structure: many DS per ML engineer | data-teams, mlops-engineer | CONNECTION | mlops-engineer | 41:14 |
| Internal libraries + FastAPI for reuse | ml-platforms, platform-engineering | CONNECTION | ml-platforms | 43:39 |
| Skills for ML engineers (Python/Linux/networking/cloud) | machine-learning-engineer-roadmap, mlops-roadmap | ENRICH | machine-learning-engineer-roadmap | 45:04 |
| Agile limits for ML; prototyping | data-science-project-management | CONNECTION | data-science-project-management | 38:48 |

## open-source-ml-contributions (Vincent Warmerdam, S2E3)
Heavily cited (16 pages). open-source-ml-contributions.md wiki page exists.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Pragmatic OSS definition + reciprocity | open-source, open-source-ml-contributions | ENRICH | open-source | 9:30 |
| Common mistake: publishing to PyPI prematurely | open-source-contributor-roadmap | ENRICH | open-source-contributor-roadmap | 11:45 |
| scikit-lego: scikit-learn-compatible components | scikit-learn | CONNECTION | scikit-learn | 17:15 |
| Design: low-maintenance APIs, ecosystem compat | open-source, software-engineering | ENRICH | open-source | 19:00 |
| Documentation checklist (README/guides/API/examples) | documentation, technical-writing | CONNECTION | documentation | 22:20 |
| First contributions: reproducible issues, small fixes, PR prep | open-source-contributor-roadmap, contributing | ENRICH | open-source-contributor-roadmap | 25:50, 27:40 |
| Large vs small repos strategy | open-source-contributor-roadmap | ENRICH | open-source-contributor-roadmap | 29:30 |
| OSS for career visibility | open-source-portfolio-evidence, career-growth | CONNECTION | open-source-portfolio-evidence | 34:00 |
| Employer OSS strategy (hiring/branding/legal) | open-source-and-developer-relations | CONNECTION | open-source-and-developer-relations | 32:40 |

## production-ml-pipelines-with-aws-and-kafka (Andreas Kretz, S4E2)
Well cited (10 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data pipeline anatomy (ingest→buffer→process→store→viz) | data-pipelines, how-to-build-data-pipelines | ENRICH | data-pipelines | 13:25 |
| Ingestion via message queues (Kafka, Kinesis) | streaming, batch-vs-streaming | CONNECTION | streaming | 15:11 |
| Streaming vs batch modes | batch-vs-streaming | ENRICH | batch-vs-streaming | 16:51 |
| Operational risk of too many tools | modern-data-stack, data-engineering-tools | CONNECTION | data-engineering-tools | 12:03 |
| Productionizing notebooks (Docker training, model on S3) | notebook-to-production-workflow | CONNECTION | notebook-to-production-workflow | 34:16 |
| Inference: live API vs precomputed | machine-learning-system-design | CONNECTION | machine-learning-system-design | 31:33 |
| Scheduling: Airflow vs CloudWatch/Lambda vs simple | orchestration, apache-airflow | CONNECTION | orchestration | 35:46, 41:06 |
| Model serving: SageMaker + cost tradeoffs | ai-infrastructure-cost-and-ownership | CONNECTION | ai-infrastructure-cost-and-ownership | 37:53 |
| Start simple, iterate to Airflow/K8s | how-to-build-data-pipelines, lean-mlops-for-startups | ENRICH | how-to-build-data-pipelines | 41:06 |
| $0 POC to convince stakeholders + ROI | machine-learning-for-business | CONNECTION | machine-learning-for-business | 58:56 |
| E-commerce pipeline as portfolio project | data-engineering-portfolio-projects | CONNECTION | data-engineering-portfolio-projects | 54:52 |

## s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products (Paul Iusztin, S23E1)
Most cited episode in batch (23 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data science vs AI engineering distinction | ai-engineering (cites), machine-learning-engineer-vs-data-scientist | ENRICH | ai-engineering | 15:13 |
| Full-stack AI engineer skill stack | ai-engineer-role, ai-engineering-roadmap | ENRICH | ai-engineering-roadmap | 22:29 |
| RAG & knowledge management mastery | retrieval-augmented-generation, search-rag-and-knowledge-systems | CONNECTION | retrieval-augmented-generation | 29:12 |
| Generalist edge: learning with AI | nontraditional-paths-to-ai-engineering | CONNECTION | nontraditional-paths-to-ai-engineering | 32:17 |
| Technical pillars for shipping AI products | ai-engineering, llm-production-patterns | ENRICH | llm-production-patterns | 42:28 |
| LLMOps in the stack | llmops | CONNECTION | llmops | 22:29/42:28 |
| Agents in the stack | agent-engineering | CONNECTION | agent-engineering | agents in full-stack AI eng |
| Portfolio "second brain" | ai-engineering-portfolio-projects (cites), context-engineering | ENRICH | ai-engineering-portfolio-projects | 54:05 |
| LLM Engineer's Handbook | ai-engineering-roadmap, staff-ai-engineer | CONNECTION | ai-engineering-roadmap | 58:01 |

## software-engineering-for-machine-learning (Nadia Nahar, S13E5)
Well cited (16 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Hidden technical debt in ML systems | machine-learning-for-software-engineers, software-engineering, mlops | ENRICH | machine-learning-for-software-engineers | 10:12 |
| ML vs traditional software | machine-learning-for-software-engineers, software-engineer-to-machine-learning | ENRICH | machine-learning-for-software-engineers | 7:42 |
| Communication/alignment: shared vocabulary | team-building, data-science-project-management | CONNECTION | team-building | 13:52 |
| Empirical study: ~300 OSS ML products; what is an ML product | open-source-portfolio-evidence, machine-learning-portfolio-projects | CONNECTION | machine-learning-portfolio-projects | 15:17, 21:54 |
| Failure modes (discontinuation, unmet reqs, poor data) | machine-learning-for-business, notebook-to-production-ai-systems | CONNECTION | machine-learning-for-business | 29:42 |
| Process gap: CRISP-DM/Agile mismatch; integrated ML+SW | data-science-project-management, software-engineering | ENRICH | data-science-project-management | 34:22, 56:55 |
| Team structures / integration patterns | data-teams, mlops-architecture | CONNECTION | data-teams | 36:28 |
| Documentation: Model Cards, Datasheets, factsheets | model-registry, documentation, reproducibility | CONNECTION | model-registry | 42:47 |
| Responsible AI: explainability, product-centric fairness | responsible-ai-and-governance, interpretability | CONNECTION | responsible-ai-and-governance | 47:16, 54:16 |

---

## Tally
- CONNECTION: 62
- ENRICH: 68
- NEW PAGE: 0
- BORDERLINE: 3 (biohacking-as-own-topic -> keep in career-development; ML-incident-response/post-mortems -> fold into model-monitoring; decision-optimization/prescriptive-analytics -> ENRICH machine-learning-for-business unless >=3 episodes justify a hub)
