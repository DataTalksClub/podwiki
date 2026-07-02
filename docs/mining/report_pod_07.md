# Podcast Mining Report — batch pod_07

17 podcast episodes mined. Coverage checked via `grep -ril` over `_wiki/` and by
scanning existing `[[podcast:<slug>]]` / `[[person:<slug>]]` citations. Every
episode is already cited somewhere, so the work is filling gaps on
under-connected episodes and enriching hubs with specific evidence. Link format
in the wiki is `[[podcast:<slug>|ts|label]]` and `[[person:<slug>|Name]]`.

Two episodes are badly under-connected and hold the most value:
`algorithms-data-structures-for-engineers` (only cited in `evolutionary-algorithms`)
and `from-software-engineering-to-leading-data-science-teams` (only cited in
`recommendation-systems`).

---

## algorithms-data-structures-for-engineers (Marcello La Rocca, S5E1)
Currently cited only in `evolutionary-algorithms.md`. Rich, badly under-connected.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Bloom filters: memory-efficient probabilistic containment w/ false positives; crawlers, routing tables, adtech device IDs | none (no page mentions "bloom filter") | CONNECTION | information-retrieval.md | La Rocca explains mechanism + adtech returning-user targeting at 30:09, 34:43, 35:59 |
| Approximate nearest-neighbor: KD-tree limits in high dimensions, R-trees / SS-trees | vector-databases, vector-search-vs-keyword-search, information-retrieval discuss ANN | ENRICH | vector-databases.md | Add La Rocca data-structure grounding for why exact NN fails in high dim (39:10, 42:44); no page cites this episode |
| Vector similarity, embeddings, recommender systems, Faiss | embeddings.md, recommendation-systems.md exist | CONNECTION | embeddings.md | Ties ANN -> embeddings -> Faiss -> recsys at 44:46 |
| Profiling to spot algorithmic wins; wrong list-vs-set for containment | machine-learning-for-software-engineers, software-engineering | ENRICH | machine-learning-for-software-engineers.md | Concrete performance-pitfall example at 19:14, 20:14 |
| Frameworks vs internals: when to trust libraries vs inspect | software-engineering.md | CONNECTION | software-engineering.md | 47:47 abstraction-vs-implementation (also 12:17) |
| Tech interviews over-weight algorithms; LeetCode/contests | data-scientist-interview.md, machine-learning-engineer-roadmap.md | CONNECTION | data-scientist-interview.md | 52:55, 58:53 |
| Learning philosophy: applications over formal proofs; practice via competitions | competitions-beyond-kaggle.md | CONNECTION | competitions-beyond-kaggle.md | 5:19, 15:57 |
| Python vs C++ / Cython for performance | software-engineering, data-engineering-tools | CONNECTION | machine-learning-for-software-engineers.md | 1:00:39 |

## building-and-scaling-ai-data-products-with-mlops (Greg Coquillo, S7E3)
Well covered (11 data-product pages). Only residual gaps.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Operational metrics: pipeline failures, SLAs, data-quality as success metrics | data-quality-and-observability, kpis | CONNECTION | data-quality-and-observability.md | 53:27 |
| Identify unscalable manual processes -> MLOps prioritization | lean-mlops-for-startups, mlops | CONNECTION | lean-mlops-for-startups.md | 39:01 |
| SMART goals / success metrics for internal data platforms | kpis.md, metrics.md | CONNECTION | kpis.md | 51:11 |
| Five Whys, working backwards, hypothesis testing | data-product-management, ml-product-manager-role (cite) | already covered | data-product-management.md | 20:28, 23:20, 31:45 |
| 3-year roadmap by impact/effort/cost; Excel template | data-product-manager-roadmap (cites) | already covered | data-product-manager-roadmap.md | 41:44, 47:18 |

## building-mlops-startup (Elena Samuylova / Evidently, S4E4)
Cited in 9 startup/founder/ML pages but NOT in `model-monitoring.md` — clearest fit.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Evidently origin: validating model monitoring as a business | model-monitoring.md exists, does not cite episode | CONNECTION | model-monitoring.md | 43:59 founder of OSS monitoring tool; strong missing edge |
| Open-core / cloud / licensing risk | open-source.md (cites) | already covered | open-source.md | 48:11, 49:29 |
| Bottom-up adoption: engineers first, enterprise later | open-source-and-developer-relations, developer-relations | CONNECTION | open-source-and-developer-relations.md | 51:48 |
| On-prem deployments so clients keep data | ai-infrastructure-cost-and-ownership, governance | CONNECTION | ai-infrastructure-cost-and-ownership.md | 56:17 |
| Vertical solution vs infrastructure/MLOps market choice | machine-learning-for-startups (cites) | already covered | machine-learning-for-startups.md | 21:34 |
| Productizing services: manual delivery -> scalable SaaS | founder, machine-learning-for-startups | CONNECTION | founder.md | 39:25 |

## data-consulting-business-pricing-and-client-acquisition (Aleksander Kruszelnicki, S13E4)
Cited in 8 pages (consulting/freelance/solopreneur).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Value-based pricing / benchmarking; day-rate vs project pricing | ml-consulting-proposals.md has value-based pricing but does not cite episode | CONNECTION | ml-consulting-proposals.md | 45:19, 52:38 |
| Customer validation & user interviews before building | data-product-management, machine-learning-for-startups | CONNECTION | machine-learning-for-startups.md | 9:08, 12:53, 15:55 |
| Lesson from a failed product: premature build, market-size misjudgment | founder, machine-learning-for-startups | CONNECTION | founder.md | 18:01 |
| Network-first client acquisition; positioning/messaging | data-freelancing-strategy (cites), freelance | already covered | data-freelancing-strategy.md | 27:59, 37:03 |
| Consulting over product to capture data-modeling value | data-engineering-consulting (cites) | already covered | data-engineering-consulting.md | 21:39, 22:42 |

## data-professionals-business-skills-in-saas (Loris Marini, S12E2)
Cited in 6 pages.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Semantic alignment: defining "customer" & core metrics across functions | metrics.md, business-skills-for-data-professionals (cites) | CONNECTION | metrics.md | 12:19, 18:00 |
| Lead indicators, stickiness/churn, causal thinking | causal-inference, experimentation-and-causal-inference | CONNECTION | causal-inference.md | 15:46 |
| Stakeholder CRM; stakeholder mapping | data-science-project-management (cites), communication | already covered | data-science-project-management.md | 27:55, 35:20 |
| Conversation-first: description & diagnostics before ML | machine-learning-for-business | CONNECTION | machine-learning-for-business.md | 53:08 |
| RL applied to practical marketing-automation problems | reinforcement-learning.md (cites) | already covered | reinforcement-learning.md | 8:30 |
| Presenting online: podcasting, pauses, audio practice | communication (cites) | already covered | communication.md | 56:13 |

## data-scientist-and-indie-hacker-bootstrapping-side-projects (Pauline Clavelloux, S12E5)
Cited in 4 pages but NOT `solopreneur-data-scientist.md`, the best fit.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Indie hacking = bootstrapping products without funding (Cryptopy, UnrealMe) | solopreneur-data-scientist.md exists, does not cite episode | CONNECTION | solopreneur-data-scientist.md | 7:23 strong missing edge on the solopreneur hub |
| Day-job + side-projects time allocation & routine | portfolio-projects, machine-learning-portfolio-projects | CONNECTION | machine-learning-portfolio-projects.md | 8:58 |
| UnrealMe: DreamBooth, API fine-tuning vs self-hosted GPUs | generative-ai.md | CONNECTION | generative-ai.md | 23:33, 25:48 |
| Skills gained from side projects: GCP, data eng, web dev, marketing | portfolio-projects, career-growth | CONNECTION | portfolio-projects.md | 35:47 |
| Idea validation: competitor scan, skills check, build criteria | machine-learning-for-startups (cites) | already covered | machine-learning-for-startups.md | 48:54 |
| Pieter Levels "many projects"; Twitter personal branding | solopreneur, learning-in-public-ai-career-switch | CONNECTION | solopreneur.md | 50:35, 54:35 |

## developer-personal-brand-learn-in-public (swyx, S3E7)
Foundational learn-in-public episode; cited in 6 pages.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Personal marketing framework: brand, domain, value, skills, channel | learning-in-public-ai-career-switch, career-growth (cite) | already covered | learning-in-public-ai-career-switch.md | 10:26 |
| Owned platforms: mailing list/newsletter/personal site | technical-writing.md | CONNECTION | technical-writing.md | 25:54 |
| Hiring portfolio: unsolicited redesigns, product clones, case studies | data-scientist-cv-and-portfolio, portfolio-projects | CONNECTION | data-scientist-cv-and-portfolio.md | 38:30 |
| Brag document / signature initiative for internal promotion | career-growth (cites) | already covered | career-growth.md | 51:10, 54:16 |
| "Pick up what they put down" engagement tactic | learning-in-public pages | already covered | learning-in-public-ai-career-switch.md | 30:27 |
| Reusable talks / public speaking as a skill | communication, developer-relations | CONNECTION | communication.md | 59:04 |
| Niche selection & validation via meetups/community signals | career-growth | already covered | career-growth.md | 21:12, 22:32 |

## from-data-freelancer-to-startup-open-source-products (Adrian Brudaru / dlt, S17E1)
Adrian already one of the most-cited guests (44 pages). Residual gaps only.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Workshop/teaching as a product feedback loop (checkpoints, CodeSpaces) | teaching.md, developer-relations | CONNECTION | developer-relations.md | 36:00, 37:28 |
| Documentation as a productive asset for a dev-tool company | documentation.md | CONNECTION | documentation.md | 41:23 |
| dlt: declarative JSON->relational; anti-pattern of dumping JSON in warehouses | data-engineering-tools, elt (cite) | already covered | data-engineering-tools.md | 17:51, 19:38 |
| PMF signals: core adoption + "removal test" | machine-learning-for-startups, founder | already covered | founder.md | 44:00 |
| Library-first vs Airbyte/Fivetran positioning | etl-vs-elt, data-engineering-tools | CONNECTION | etl-vs-elt.md | 58:11 |
| Freelance -> subcontracting -> agency tradeoffs & misalignment | data-freelancing-strategy (cites), freelance | already covered | data-freelancing-strategy.md | 5:20, 8:46, 10:51 |

## from-software-engineering-to-leading-data-science-teams (Sadat Anwar, S12E1)
Only cited in `recommendation-systems.md`. Second-biggest gap in the batch.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| SWE -> engineering manager -> data-science manager transition | data-team-lead-role, career-transitions-in-data, leadership | CONNECTION | data-team-lead-role.md | 25:11, 43:33, 52:52 — absent from all three |
| Brag list: documenting leadership evidence for interviews | career-growth (covers brag doc via swyx) | CONNECTION | career-growth.md | 33:46 second grounding source |
| Search engineering at OLX: Solr autoscaling, decoupling search from monolith | search-relevance, information-retrieval | CONNECTION | search-relevance.md | 6:31, 8:42, 10:37 real production-search war story |
| Transition pain: dopamine loss, dropping hands-on coding | leadership, data-team-lead-role | CONNECTION | data-team-lead-role.md | 36:16 |
| Safety nets for ML experimentation: feature flags, backups, monitoring | experimentation.md, mlops | CONNECTION | experimentation.md | 21:58 |
| People-management skills: conflict resolution, hiring, business metrics | leadership.md | CONNECTION | leadership.md | 30:25 |
| Measuring managerial impact: influence, business value, team-health metrics | data-team-lead-role, leadership | CONNECTION | data-team-lead-role.md | 57:34 |
| "Act before you think" — 20% time (word2vec, recsys) | recommendation-systems (cites word2vec) | already covered | recommendation-systems.md | 18:58, 20:47 |

## hiring-for-data-science-jobs-interview-questions-skills (Olga Ivina, S9E9)
Cited in 3 pages. NOTE: summary frontmatter has a doubled `.md.md` source_episode extension — flag for maintenance.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Inclusive job posts: wording that avoids discouraging candidates | job-descriptions.md, hiring (cites) | CONNECTION | job-descriptions.md | 47:06, 53:53 |
| AutoML limits & human-in-the-loop | no dedicated AutoML page | CONNECTION | machine-learning-for-business.md | 37:44 |
| Evaluating employment gaps / long CV breaks | hiring.md (cites), job-search | CONNECTION | job-search.md | 56:31 |
| Conformal prediction (PhD: air-pollution modeling) | conformal on interpretability, responsible-ai, machine-learning | BORDERLINE | interpretability.md | 6:25 real practitioner but tangential to a hiring episode |
| Hiring criteria: technical excellence + growth mindset + humility | hiring, data-scientist-interview (cite) | already covered | data-scientist-interview.md | 14:49, 18:03 |
| IC vs management trade-offs | career-growth, career-development | CONNECTION | career-growth.md | 42:09 |

## job-search-strategy-in-tech-projects-skills-cv-networking (Sarah Mestiri, S17E6)
Cited in 6 pages; job-search well covered.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Four-pillar framework: goals, networking, CV, strategy | job-search.md (cites) | already covered | job-search.md | 10:59 |
| Courses vs projects — validate skills through practical work | portfolio-projects, machine-learning-portfolio-projects | CONNECTION | portfolio-projects.md | 26:28 |
| Informational interviews: outreach, key questions | job-search, career-growth (cite) | already covered | career-growth.md | 32:17, 36:10 |
| Weak ties / referrals; top-5 target-company list | job-search (cites) | already covered | job-search.md | 31:40, 29:35 |
| Strength/interest assessments (Gallup, HIGH5, MyNextMove) | career-development (cites) | already covered | career-development.md | 49:18 |
| Age & career change: emphasize results and transferable skills | career-transitions-in-data | CONNECTION | career-transitions-in-data.md | 53:30 |

## machine-learning-system-design-interview (Valerii Babushkin, S7E5)
Cited in 16 pages — near-saturated. No new actions warranted.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Fraud detection: loss functions, class imbalance, real-time | machine-learning-system-design, ml-system-design-documents (cite) | already covered | machine-learning-system-design.md | 13:58, 16:43 |
| Features matter more than model architecture | machine-learning-system-design-interview (cites) | already covered | machine-learning-system-design-interview.md | 47:52 |
| Metrics, baselines, A/B testing in end-to-end pipeline | a-b-testing, experimentation-and-causal-inference (cite) | already covered | a-b-testing.md | 24:28, 57:23 |
| When to avoid ML / proxy metrics & business alignment | machine-learning-for-business (cites) | already covered | machine-learning-for-business.md | 40:11, 52:25 |
| New-grad expectations: coding focus, limited system design | machine-learning-engineer-roadmap (cites) | already covered | machine-learning-engineer-roadmap.md | 54:07 |

## mlops-kubeflow-model-monitoring (Theofilos Papapanagiotou, S2E4)
Cited in 7 MLOps pages but NOT `model-monitoring.md` despite heavy monitoring content.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Monitoring drift/fairness as retraining triggers; monitoring as source of new training data | model-monitoring.md exists, does not cite episode | CONNECTION | model-monitoring.md | 11:17, 33:27 clear missing edge |
| MLOps maturity models (Google/Microsoft): manual -> pipeline -> automated retraining | mlops-roadmap, mlops-adoption-at-scale | CONNECTION | mlops-roadmap.md | 23:47, 27:01, 30:08 |
| Katib for hyperparameter search / AutoML in Kubeflow | no hyperparameter page cites it; model-optimization exists | CONNECTION | model-optimization.md | 40:12 |
| Edge & mobile deployment: offline models, edge Kubernetes | machine-learning-infrastructure, ml-platforms | CONNECTION | machine-learning-infrastructure.md | 51:44 |
| MLOps as continuation of / divergence from DataOps | mlops-vs-dataops.md | CONNECTION | mlops-vs-dataops.md | 50:35 |
| Feast feature store in Kubeflow ecosystem | feature-stores.md (already cites) | already covered | feature-stores.md | 37:06 |
| Data/model versioning: MLMD, metadata, traceability | model-registry.md (cites) | already covered | model-registry.md | 46:58 |

## postdoc-to-data-science-lead-career-transition (CJ Jenkins, S6E6)
Cited in 3 pages.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Bridging deployment gap: Docker + Python for a stats/R researcher | software-engineer-to-machine-learning, notebook-to-production-workflow | CONNECTION | notebook-to-production-workflow.md | 6:10 |
| Resume: 14 CV iterations, skills-first rewrite, ATS, LinkedIn keywords | data-scientist-cv-and-portfolio.md | CONNECTION | data-scientist-cv-and-portfolio.md | 17:14, 20:40 |
| Hiring signals: smartness, ambition, receptiveness to feedback | hiring, data-scientist-interview | CONNECTION | data-scientist-interview.md | 8:41, 10:42 |
| Psychological safety: team rituals, sharing failures, trust | community.md (only psych-safety page) | CONNECTION | community.md | 51:05 |
| Clean code, LeetCode, pair programming, code reviews for juniors | machine-learning-for-software-engineers | CONNECTION | machine-learning-for-software-engineers.md | 36:43, 37:39 |
| One-year transition plan / Coursera sprint; GLMs foundation | academic-researcher-to-data-science (cites) | already covered | academic-researcher-to-data-science.md | 15:36, 4:45 |
| Research vs industry: publications vs portfolios | academia (cites) | already covered | academia.md | 40:02 |

## public-speaking-for-data-scientists (Ben Taylor, S2E10)
Only cited in 2 pages. No dedicated public-speaking page.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Scaling talks: repeatable keynotes; earning stages meetup->conference | communication, developer-relations (cites) | CONNECTION | communication.md | 9:37, 47:38 |
| Storytelling: hero-story intros, Pixar structure, attention hooks | communication.md (storytelling covered) | ENRICH | communication.md | 24:17, 34:12, 19:54 |
| Executive presentations: recommendations first, appendix ready | communication, technical-writing | CONNECTION | technical-writing.md | 39:55 |
| Translating data/metrics into narrative | metrics, communication | CONNECTION | communication.md | 30:57 |
| Q&A strategy: handle tough questions, admit unknowns | communication | ENRICH | communication.md | 52:13 |
| Conference proposals: novelty, "scare yourself"; speaker resume | developer-relations, career-growth | CONNECTION | developer-relations.md | 50:20, 53:48 |
| Starter talk topics: business problems over hype | machine-learning-for-business | CONNECTION | machine-learning-for-business.md | 56:37 |
| Dedicated "public speaking for data scientists" hub page | communication.md + developer-relations.md + main-site episode own the intent | BORDERLINE | communication.md | Ben Taylor + swyx + Loris Marini could ground a page, but risks cannibalizing communication.md; prefer enrich unless a keyword list justifies a `guide` |

## s23e05-inside-ai-engineer-role-tools-skills-and-career-path (Ruslan Shchuchkin, S23E5)
Cited in 8 AI-engineering pages; well covered.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| AI engineer as "universal soldier" across the stack | ai-engineer-role.md (cites) | already covered | ai-engineer-role.md | 19:40 |
| Maximizing "luck surface area" via public output | learning-in-public-ai-career-switch (cites), career-growth | CONNECTION | learning-in-public-ai-career-switch.md | 15:26 |
| Vibe coding & side hustles; Branch GPT side project | ai-coding-tools, ai-engineering-portfolio-projects (cite) | already covered | ai-coding-tools.md | 38:49, 7:51 |
| Skills over degrees in hiring | nontraditional-paths-to-ai-engineering (cites), hiring | already covered | nontraditional-paths-to-ai-engineering.md | 57:39 |
| Using AI to learn instead of just generating code | ai-tools-for-personal-productivity | CONNECTION | ai-tools-for-personal-productivity.md | 1:03:12 |
| Launching a lean local AI community/meetup | community-building.md | CONNECTION | community-building.md | 33:21 |
| Future & longevity of the data-science role | data-science-careers.md | CONNECTION | data-science-careers.md | 52:28 |

## teaching-reproducible-research-and-open-science-coding-practices-for-academia (Johanna Bayer, S12E4)
Cited in 6 pages.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Software as a research output: DOIs, publishing code, toolboxes | reproducibility, open-source-ml-contributions | CONNECTION | open-source-ml-contributions.md | 16:36, 36:05 |
| Core coding practices to teach: packaging, environments, formatting, tests, cookiecutter | reproducibility.md, testing.md | CONNECTION | reproducibility.md | 27:38, 38:50 |
| Sensitive-data reality: "data upon request", de-identification, controlled access | data-governance, privacy-engineering-for-ml | CONNECTION | privacy-engineering-for-ml.md | 37:01, 42:22 |
| Guided onboarding to open source: small repos, first PRs, Turing Way | open-source-contributor-roadmap.md | CONNECTION | open-source-contributor-roadmap.md | 10:52 |
| MLflow experiment tracking in research | experiment-tracking.md (cites) | already covered | experiment-tracking.md | 22:12, 39:27 |
| Research Software Engineer (RSE) role & academic RSE career | academia, applied-research (cite) | already covered | academia.md | 12:10, 14:10 |
| Culture change in labs: grassroots hackathons, Brainhack | community-building.md (cites) | already covered | community-building.md | 17:10, 28:18 |
| Carpentries / Turing Way structured beginner curriculum | teaching.md (cites) | already covered | teaching.md | 7:39, 55:12 |

---

## Tally
- CONNECTION: 63
- ENRICH: 4
- NEW PAGE: 0
- BORDERLINE: 2
(Remaining ~55 rows are "already covered" — recorded so future runs don't re-propose them.)
