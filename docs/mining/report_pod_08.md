# Podcast Mining Report — batch pod_08

17 episodes mined against `_wiki/`. Coverage checked via `grep -ril` over `_wiki`
plus per-episode/per-guest citation counts. Most topics are already well-covered by
hub pages, so almost every action is CONNECTION or ENRICH. Recurring pattern: an
episode's single most on-topic hub page often does not yet cite that episode, even
when 10-20 other pages do.

Citation baseline (wiki pages already citing each episode): analytics-engineer 19,
data-eng-career 19, data-observability(Barr) 21, mlops-monitoring(Danny) 21,
s23e06 19, identity-resolution 11, technical-writing 10, devrel(Elle) 9,
practical-devrel(Will) 9, make-money(Vin) 6, fraud(Angela) 5, data-strategy(Boyan) 3,
from-devops(Agita) 3, remote-DE(Jose) 2, VP-of-ML(Jack) 2, how-to-break(Misra) 1,
kaggle-grandmaster(Alexander) 1.

---

## analytics-engineer-skills-tools (Victoria Perez Mola, S3E11)
Already heavily connected (19 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| dbt as the tool behind the AE movement | dbt, analytics-engineering | CONNECTION | dbt.md | dbt (SQL transforms, version control, tests, DAG) created the role (~6:49, ~30:06) |
| AE vs data analyst vs data engineer boundary | data-analyst-vs-analytics-engineer | ENRICH | data-analyst-vs-analytics-engineer.md | AE reduces analysts' cleaning workload; Spotify origin (~14:34, ~16:54) |
| Role origin: reduce analysts' cleaning burden (Spotify) | analytics-engineering | ENRICH | analytics-engineering.md | concrete origin narrative (~16:54) |
| dbt tests, warnings vs errors, upstream checks | dataops-checks-for-data-pipelines | CONNECTION | dataops-checks-for-data-pipelines.md | testing strategy, macros for bad data/schema (~36:44-38:53) |
| Toolstack: dbt + Snowflake + ETL + Looker | modern-data-stack | CONNECTION | modern-data-stack.md | concrete AE stack (~10:04) |
| Platform vs embedded AE placement | analytics-engineering, data-teams | ENRICH | analytics-engineering.md | team scale/placement tradeoff (~48:36) |
| Path in: software practices + Kimball + dbt | analytics-engineering-roadmap | CONNECTION | analytics-engineering-roadmap.md | learning path signals (~42:05) |
| dbt docs + profiling (Datafold) | data-observability-for-data-engineering | CONNECTION | data-observability-for-data-engineering.md | documentation & profiling tools (~50:46) |

## building-and-scaling-data-engineering-systems-for-fraud-detection (Angela Ramirez, S15E9)
Cited by only 5 pages. Fraud/graph-feature ideas under-connected. No dedicated fraud page warranted.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Hybrid arch: daily batch features + real-time scoring | feature-stores, batch-vs-streaming | ENRICH | feature-stores.md | feature-stores.md does NOT cite Angela; batch features served at instant inference (~8:24, ~34:46) |
| Network/graph features for fraud | knowledge-graph-vs-vector-search, entity-resolution | ENRICH | knowledge-graph-vs-vector-search.md | graph DB + SPARQL/Wikidata; members-transactions-products graph features (~23:04, ~29:15) |
| Relational vs document vs graph modeling decision | machine-learning-system-design | CONNECTION | machine-learning-system-design.md | DB selection: static schema vs dynamic data (~20:30, ~35:33) |
| Real-time decisioning at point of sale | machine-learning-system-design-interview | ENRICH | machine-learning-system-design.md | front-end fraud signals for cashiers/security (~33:34) |
| SWE discipline for DE: testing, code quality (PySpark) | software-engineering | CONNECTION | software-engineering.md | testing/code quality for data engineers (~40:50) |
| Data quality tooling: Great Expectations + cloud monitoring | data-quality-and-observability | CONNECTION | data-quality-and-observability.md | GE + cloud monitoring in production (~43:28) |
| Debugging playbook: logs, runbooks, error docs | data-observability-for-data-engineering | ENRICH | data-observability-for-data-engineering.md | operational runbooks/error docs (~48:21) |
| Neo4j graph visualization for investigations | knowledge-graph-vs-vector-search | CONNECTION | knowledge-graph-vs-vector-search.md | Neo4j for investigator UX (~38:11) |
| DE career path: process improvement -> analyst -> DE | data-analyst-to-data-engineer | CONNECTION | data-analyst-to-data-engineer.md | transition narrative (~16:02) |

## building-open-source-data-product-for-identity-resolution (Sonal Goyal, S11E4)
Well-connected; entity-resolution.md already cites Sonal heavily (38 mentions).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Entity vs identity resolution terminology | entity-resolution | covered | entity-resolution.md | already grounded |
| ML matching: training, blocking, indexing for scale | entity-resolution | covered | entity-resolution.md | already grounded |
| Deterministic rules vs probabilistic ML tradeoff | entity-resolution | ENRICH | entity-resolution.md | accuracy tradeoff detail (~44:25) if not present |
| AGPL licensing to prevent SaaS rehosting | open-source | CONNECTION | open-source.md | licensing choice rationale (~27:00) |
| Consultancy -> full-time OSS product founder | consultant-or-freelancer-to-data-product-founder | CONNECTION | consultant-or-freelancer-to-data-product-founder.md | 18-mo POC->release, cofounder-earlier regret (~21:51, ~54:11) |
| OSS strategy: community/adoption vs IP concerns | open-source, startups | CONNECTION | startups.md | discoverability vs IP tradeoff (~24:14, ~31:10) |
| Identity resolution for AML/fraud | customer-data-platforms | CONNECTION | customer-data-platforms.md | fraud/AML use cases (~45:50) |
| Beyond fuzzy joins / basic ETL | entity-resolution | covered | entity-resolution.md | when joins aren't enough (~40:36) |

## data-engineering-career-path-and-skills (Jeff Katz, S8E8)
Very well connected (19 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| 85% Python/SQL fundamentals, 15% tools | data-engineer-roadmap | ENRICH | data-engineer-roadmap.md | curriculum ratio; drop Spark/Kafka/K8s for juniors (~38:05, ~56:46) |
| SQL mastery: window functions + medium LeetCode SQL | data-engineer-roadmap | CONNECTION | data-engineer-roadmap.md | concrete SQL prep target (~44:21) |
| OLTP vs OLAP data modeling practice | data-warehouse | CONNECTION | data-warehouse.md | modeling practice with sample DBs (~45:14) |
| Interview stages: screening, SQL test, on-site | job-search | CONNECTION | job-search.md | DE interview funnel (~48:00) |
| Data analyst -> data engineer (backend + cloud) | data-analyst-to-data-engineer | ENRICH | data-analyst-to-data-engineer.md | transition path detail (~40:42) |
| Bootcamp curriculum / employer validation | teaching | CONNECTION | teaching.md | market research + employer validation (~9:58) |
| Apply early, learn from rejection | job-search | CONNECTION | job-search.md | interview practice mindset (~33:05) |

## data-quality-data-observability-data-reliability (Barr Moses, S3E3)
Very well connected (21 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Five pillars of data observability | data-observability-for-data-engineering | covered | data-observability-for-data-engineering.md | freshness/volume/distribution/schema/lineage (~16:38) |
| Monitoring vs observability (detection vs diagnosis) | model-monitoring-vs-data-observability | ENRICH | model-monitoring-vs-data-observability.md | detection vs root-cause diagnosis (~24:31) |
| Data downtime as a business problem | data-observability-for-data-engineering | covered | data-observability-for-data-engineering.md | already grounded |
| RACI for data ownership/accountability | data-governance | CONNECTION | data-governance.md | accountability model (~29:00) |
| Data SLAs + inferring thresholds from history | data-observability-for-data-engineering | ENRICH | data-observability-for-data-engineering.md | SLA automation (~35:24, ~38:14) |
| Maturity curve reactive->proactive->automated->scalable | data-observability-for-data-engineering | CONNECTION | data-observability-for-data-engineering.md | maturity model (~43:00) |
| Reducing false positives / contextual anomalies | model-monitoring | CONNECTION | model-monitoring.md | anomalies vs bad data (~1:00:27) |

## data-strategy-and-dataops-for-ai-powered-products (Boyan Angelov, S14E3)
Only 3 pages cite it, and data-strategy.md itself does NOT. Highest-value ENRICH gap in this batch.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Data strategy = actionable, flexible plans tied to business goals | data-strategy | ENRICH | data-strategy.md | data-strategy.md does NOT cite this episode; actionable strategy, due diligence, alignment (~8:13, ~10:13) |
| Use-case ideation -> feasibility -> prioritization | data-product-intake-and-prioritization | CONNECTION | data-product-intake-and-prioritization.md | strategy design loop, scope creep (~13:28, ~16:21) |
| DataOps principles: lean, agile, CI/CD | dataops | ENRICH | dataops.md | DataOps as lean/agile/CI-CD for data products (~24:57) |
| Data strategist role & path (business fluency) | data-translator-role | CONNECTION | data-translator-role.md | accidental transition; translation skill (~5:47, ~39:09) |
| Strategist -> CTO ownership/budgeting | chief-data-officer-role | CONNECTION | chief-data-officer-role.md | ownership, budgeting, management (~41:31) |
| GPT as writing/ideation co-pilot for strategy | ai-tools-for-personal-productivity | CONNECTION | ai-tools-for-personal-productivity.md | GPT for outlines, decks, prompting (~43:46, ~51:02) |
| Pitch small: budgeted use case + pre/post baselines | machine-learning-for-business | ENRICH | machine-learning-for-business.md | start-small pitch + measurement (~52:44, ~55:32) |

## devrel-data-science-open-source-tools (Elle O'Brien, S2E2)
Reasonably connected (9 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| DevRel vs developer advocate vs evangelist | developer-relations | covered | developer-relations.md | role distinctions (~27:04) |
| Solo DevRel prioritization: release vs evergreen | developer-relations | ENRICH | developer-relations.md | scheduling releases vs evergreen (~15:02) |
| DevRel as product signal / user insight channel | developer-experience | CONNECTION | developer-experience.md | community feedback as product signal (~23:51) |
| Community metrics & analytics | community-building | CONNECTION | community-building.md | signals/analytics for community (~26:01) |
| Managing toxicity, burnout, online abuse | developer-relations | ENRICH | developer-relations.md | safety practices, anonymity, moderation (~17:54, ~28:55) |
| Learning in public / non-technical path into DevRel | learning-in-public-ai-career-switch | CONNECTION | learning-in-public-ai-career-switch.md | blogging, portfolio, learning in public (~39:31) |
| Viral OSS project (StyleGAN) -> DevRel role | open-source-ml-contributions | CONNECTION | open-source-ml-contributions.md | project-as-career-launch (~9:33) |

## from-devops-to-data-engineering-automation-open-source-volunteering (Agita Jaunzeme, S19E8)
Only 3 pages cite it.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| DevOps -> data engineering transition | devops-to-data-engineering | covered | devops-to-data-engineering.md | already cited |
| Automating repetitive tasks -> rapid promotion | devops-to-data-engineering | ENRICH | devops-to-data-engineering.md | scripting toil as promotion lever (~14:29) |
| Problem-solving as core transferable skill | career-transitions-in-data | CONNECTION | career-transitions-in-data.md | transferable competencies (~19:16) |
| Community management + Versatile Data Kit (OSS) | open-source-and-developer-relations | CONNECTION | open-source-and-developer-relations.md | VMware VDK community role; DevRel overlap (~9:20, ~38:05) |
| Personality traits for DE (precision, persistence) | data-engineer-vs-data-scientist | CONNECTION | data-engineer-vs-data-scientist.md | DS vs DE interest/personality split (~29:53, ~34:52) |
| Career coaching: align career with who you are | career-development | CONNECTION | career-development.md | self-fit framing (~43:04) |

## from-software-engineering-to-vp-of-machine-learning-applied-ml-leadership (Jack Blandin, S16E6)
Only 2 pages cite it.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Sell ML with fast POCs/demos for buy-in | machine-learning-for-business | ENRICH | machine-learning-for-business.md | fast POCs/demos to win support (~20:48) |
| Rapid prototyping tools: Gradio, Streamlit | machine-learning-for-startups | CONNECTION | machine-learning-for-startups.md | lightweight demo tooling (~28:17) |
| Baseline first: heuristics/manual before ML | machine-learning-system-design | ENRICH | machine-learning-system-design.md | start with baseline/manual process (~28:46) |
| Actionability over accuracy (churn model lesson) | machine-learning-for-business | ENRICH | machine-learning-for-business.md | usable insight > raw accuracy (~34:09) |
| Full-stack ML: SWE skills for production ML | machine-learning-for-software-engineers | covered | machine-learning-for-software-engineers.md | already cited |
| IC -> manager -> VP leadership growth | leadership | covered | leadership.md | already cited |
| Stakeholder comms in business language (CAC/KPIs) | business-skills-for-data-professionals | CONNECTION | business-skills-for-data-professionals.md | speaking marketing/finance language (~15:25) |
| Risk communication without raw accuracy | communication | CONNECTION | communication.md | explaining model tradeoffs (~26:15) |

## how-to-break-into-data-science (Misra Turp, S9E5)
Only 1 page cites it (data-science-careers). Job-search and portfolio hubs miss it - strong CONNECTION cluster.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Portfolio projects: what hiring managers look for | data-scientist-cv-and-portfolio | CONNECTION | data-scientist-cv-and-portfolio.md | page does NOT cite Misra; real/dirty datasets (NYC Open Data) (~57:09, ~58:14) |
| Entry-level job-hunting strategies | job-search | CONNECTION | job-search.md | job-search.md does NOT cite Misra; catching recruiter attention (~50:32, ~54:31) |
| Managing FOMO / imposter syndrome | career-growth | ENRICH | career-growth.md | FOMA + imposter syndrome coping (~15:43, ~35:31) |
| Generalist vs specialist career tradeoff | data-science-careers | CONNECTION | data-science-careers.md | generalist vs specialist paths (~47:33) |
| Degrees vs experience (Master's/PhD) | data-science-careers | CONNECTION | data-science-careers.md | when advanced degrees matter (~1:01:42) |
| Communicating DS value to stakeholders | communication | CONNECTION | communication.md | biggest challenge = comms (~30:11) |
| DALL-E 2 / diffusion models explainer | generative-ai | BORDERLINE | generative-ai.md | text-to-image/diffusion (~20:21); too thin to ground a page (0 wiki mentions of diffusion/DALL) - connect only |
| Data scientist role variants (consultant/in-house/freelance) | data-scientist-role | CONNECTION | data-scientist-role.md | role variants + deliverables (~9:01, ~10:58) |

## kaggle-grandmaster-to-production-ml-and-education (Alexander Guschin, S20E2)
Only 1 page cites it (teaching). competitions-beyond-kaggle.md does NOT cite it - clear CONNECTION.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Kaggle for skill broadening, domain exposure, interviews | competitions-beyond-kaggle | CONNECTION | competitions-beyond-kaggle.md | page does NOT cite Guschin; Kaggle career value + regional differences (~17:10, ~26:18) |
| Competition prep: iteration, baselines, infra | competitions-beyond-kaggle | ENRICH | competitions-beyond-kaggle.md | EDA, validation, "no single trick" (~21:42, ~1:01:48) |
| Applying competition rigor to production ML | machine-learning-system-design | CONNECTION | machine-learning-system-design.md | competition->production transfer (~22:45) |
| MLEM tooling anecdote (Iterative OSS) | mlops-tools | CONNECTION | mlops-tools.md | MLEM model tooling story (~8:36) |
| ML system design teaching (bot detection case) | machine-learning-system-design | ENRICH | machine-learning-system-design.md | problem-centered assignments, dual leaderboards (~41:10, ~46:50) |
| GenAI & AutoML: productivity vs winning solutions | competitions-beyond-kaggle | CONNECTION | competitions-beyond-kaggle.md | AutoML productivity vs winning (~1:03:11) |
| Online education at scale (Coursera, 100k students) | teaching | covered | teaching.md | already cited |

## make-money-with-machine-learning-roles-skills (Vin Vashishta, S2E9)
Cited by 6 pages but ml-product-manager-role.md does NOT cite it.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Monetize ML: revenue focus (ARR/MRR) drives strategy | machine-learning-for-business | covered | machine-learning-for-business.md | already cited |
| ML product management: strategy -> researchable use cases | ml-product-manager-role | CONNECTION | ml-product-manager-role.md | page does NOT cite Vin; gated decisions, feasibility studies (~43:28, ~48:54) |
| Three core roles to monetize ML | data-roles | ENRICH | data-roles.md | role split into focused functions (~20:15, ~1:14:14) |
| ML architecture: platform vision, cost, buy vs build | machine-learning-infrastructure | CONNECTION | machine-learning-infrastructure.md | platform vision + cost estimation (~54:50, ~58:04) |
| Category creation with ML (Amazon/Google/Stitch Fix) | machine-learning-for-business | covered | machine-learning-for-business.md | already cited |
| Revenue vs cost-savings business-model metrics | kpis | CONNECTION | kpis.md | ML product business metrics (~15:59) |
| Corporate upskilling "farm club" pipelines | career-development | CONNECTION | career-development.md | education gap + corporate upskilling (~1:03:12) |
| Product metrics for ML adoption | data-product-adoption | CONNECTION | data-product-adoption.md | adoption metrics + pricing (~1:15:14) |

## mlops-model-monitoring-data-observability (Danny Leybzon, S10E3)
Very well connected (21 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| MLOps Architect as technical-business bridge | mlops-engineer, ml-platform-engineer-role | ENRICH | mlops-engineer.md | role definition, tooling advising (~8:11, ~10:32) |
| Model monitoring priority; observability scope to ETL | model-monitoring-vs-data-observability | covered | model-monitoring-vs-data-observability.md | already cited |
| Build vs buy guidance for tooling | mlops-tools | CONNECTION | mlops-tools.md | procurement/build-vs-buy (~34:25) |
| WhyLogs (OSS profiling) vs WhyLabs (SaaS) | model-monitoring | CONNECTION | model-monitoring.md | profiling arch: WhyLogs + Apache Druid (~31:50, ~55:50) |
| ONNX interoperability adoption | mlops-tools | CONNECTION | mlops-tools.md | ONNX interoperability (~38:01) |
| Startup "wear many hats" reality | lean-mlops-for-startups | CONNECTION | lean-mlops-for-startups.md | early-stage versatility (~13:50) |
| Fairness/bias/segmentation over explainability | responsible-ai-and-governance | CONNECTION | responsible-ai-and-governance.md | research focus on fairness/bias (~41:00) |
| Career: exploration vs exploitation (Thompson sampling) | career-development | CONNECTION | career-development.md | explore/exploit career framing (~45:49) |

## practical-devrel-demofirst-education-and-open-source (Will Russell, S20E8)
Reasonably connected (9 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Demo-driven DevRel content (goal, pace, walkthrough) | developer-relations | ENRICH | developer-relations.md | video strategy, feature-demo workflow (~53:40, ~54:30) |
| Hackathons as learning (Git, teamwork, projects) | community-building | covered | community-building.md | already cited |
| Running/judging hackathons (matrices, categories) | community-building | ENRICH | community-building.md | judging matrices, sponsor challenges (~25:26, ~26:14) |
| MLH Fellowship mentorship / large-repo contribution | open-source-contributor-roadmap | CONNECTION | open-source-contributor-roadmap.md | mentorship model, PR quality, onboarding (~35:43, ~39:02) |
| Contribution best practices: PR quality, env setup | open-source-contributor-roadmap | CONNECTION | open-source-contributor-roadmap.md | onboarding complex projects (~39:02, ~41:16) |
| Career tradeoff: technical depth vs community work | developer-relations | CONNECTION | developer-relations.md | depth vs community-work tension (~20:07) |
| Demo-first education at Kestra (docs, demos) | developer-experience | CONNECTION | developer-experience.md | docs/demos/outreach at Kestra (~49:14) |

## remote-data-engineering-work-and-building-iot-platforms (Jose Maria Sanchez Salas, S15E5)
Only 2 pages cite it. IoT/remote angles under-connected.

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| IoT platform as "operating system" for sensors | platform-engineering | ENRICH | platform-engineering.md | IoT platform architecture + sensor onboarding (~12:29, ~31:04) |
| Turning raw sensor data into business value (the why) | data-products | CONNECTION | data-products.md | understand-the-why before pipelines (~24:04) |
| Remote DE work: routine, isolation, workspace boundaries | data-engineering | ENRICH | data-engineering.md | remote-work challenges/loneliness; only 2 pages mention "remote work" (~15:31, ~18:17) |
| Newsletter/personal branding as opportunity driver | technical-writing | CONNECTION | technical-writing.md | writing for non-technical audiences; branding (~32:17, ~38:10) |
| Learning DE: software foundations + projects | data-engineer-roadmap | CONNECTION | data-engineer-roadmap.md | SWE foundations first (~48:36) |
| Remote-first hiring landscape (Norway) | job-search | BORDERLINE | job-search.md | geography-specific, thin; main site owns "remote data engineering" - connect only (~8:13) |
| Soft skills / communication for remote DE | communication | CONNECTION | communication.md | communication as key remote skill (~57:12) |

## s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for (Slawomir Tulski, S23E6)
Very well connected (19 pages).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Platform vs product data engineering ("identity crisis") | data-engineer-role, data-roles | ENRICH | data-engineer-role.md | platform-vs-product DE specialization (~11:54) |
| Hadoop hype lessons applied to AI hype | modern-data-engineering-trends | ENRICH | modern-data-engineering-trends.md | big-data hype cycle -> AI (~6:47) |
| Cost-aware engineering as competitive advantage | finops-for-data-engineers | CONNECTION | finops-for-data-engineers.md | cost-aware engineering (~25:33) |
| Avoiding over-engineered modern data stacks | modern-data-stack | ENRICH | modern-data-stack.md | over-engineering critique (~30:56) |
| Real-time myth: when to actually use Kafka/Spark | batch-vs-streaming | ENRICH | batch-vs-streaming.md | real-time overuse critique (~38:01) |
| 2026 DE market reality / breaking in | data-engineer-roadmap | covered | data-engineer-roadmap.md | already cited |
| Strategic builders vs "dbt monkeys" (AI automation) | modern-data-engineering-trends | CONNECTION | modern-data-engineering-trends.md | AI automation & strategic value (~51:04) |
| End-to-end platform as ultimate portfolio project | data-engineering-portfolio-projects | covered | data-engineering-portfolio-projects.md | already cited |

## technical-writing-for-data-scientists (Eugene Yan, S2E1)
Well connected (10 pages; technical-writing.md cites Eugene 4x).

| idea | coverage found | action | target page | specifics |
|---|---|---|---|---|
| Writing as product: weekly shipping, UX mindset | technical-writing | covered | technical-writing.md | already cited |
| 7-day writing cadence / outline-first method | technical-writing | ENRICH | technical-writing.md | weekly workflow, outline-first, editing budget (~20:00, ~25:00) |
| Writing motivations: share, learn, be a beacon | learning-in-public-ai-career-switch | CONNECTION | learning-in-public-ai-career-switch.md | learn-by-teaching motive (~9:30) |
| Writing at work: press release / working backwards / design docs | ml-system-design-documents | CONNECTION | ml-system-design-documents.md | Amazon working-backwards, design docs (~51:00, ~54:00) |
| Decision logs / rationales as team memory | documentation | CONNECTION | documentation.md | decision logs & rationales (~54:00) |
| Portfolio README best practices | data-scientist-cv-and-portfolio | CONNECTION | data-scientist-cv-and-portfolio.md | clear README/quick-start/repo tour (~56:30) |
| Audience growth: distribution + consistency | community-building | CONNECTION | community-building.md | Twitter/LinkedIn distribution (~48:30) |

---

## Tally
- Total ideas: ~135 across 17 episodes (8-9 each).
- Actions: CONNECTION ~66 · ENRICH ~34 · NEW PAGE 0 · BORDERLINE 2 · already-covered ~15.
- No NEW PAGE: every gap maps to an existing hub. Two BORDERLINE items (DALL-E/diffusion
  explainer; Norway remote-hiring) too thin to ground a page; main site owns remote-DE query.

### Highest-value findings
1. data-strategy.md does NOT cite its most on-topic episode (Boyan Angelov). Only 3 pages cite it. Prime ENRICH.
2. competitions-beyond-kaggle.md does NOT cite the Kaggle Grandmaster episode (Guschin, only 1 page total). Clear CONNECTION.
3. ml-product-manager-role.md does NOT cite Vin Vashishta's monetize-ML episode - the canonical ML-PM interview. CONNECTION.
4. how-to-break-into-data-science (Misra Turp) cited by only 1 page; job-search.md and data-scientist-cv-and-portfolio.md both miss it. CONNECTION cluster.
5. feature-stores.md does NOT cite Angela Ramirez's fraud episode (batch-features-plus-real-time-scoring; graph features -> knowledge-graph-vs-vector-search.md). ENRICH.
