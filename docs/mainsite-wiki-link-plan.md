# Main-site → Podwiki reciprocal linking plan

Goal: link main-site blog posts (`datatalksclub.github.io/_posts/*.md`, published at
`datatalks.club/blog/<slug>.html`) to the deeper podwiki topic hubs
(`podwiki/_wiki/<slug>.md`, published at `datatalks.club/podwiki/wiki/<slug>/`).
This passes link equity from the (currently orphaned) blog into the wiki and gives
readers a podcast-grounded "go deeper" path.

Scope reviewed: 54 posts, 273 wiki hubs. Read-only scouting; no files were edited.

Target-URL convention for anchors: `/podwiki/wiki/<slug>/`.

Podcast-derived definition used: author = `angelicaloduca` (wrote FROM podcast episodes),
OR the post embeds/links a specific DataTalks.Club podcast episode, OR the post is itself
an interview/podcast writeup.

---

## (A) LINK PLAN

Ranked by link value: podcast-derived + exact-topic hub first, then strong topical, then moderate.
"Podcast-derived?" column: Y = angelicaloduca or embeds a specific episode; ~ = has a
podcast/Spotify tie but is primarily an authored/how-to piece; N = not podcast-related.

| # | Post file | Post title (short) | Podcast-derived? | Target wiki hub slug(s) | Suggested anchor text | Placement note |
|---|-----------|--------------------|------------------|-------------------------|-----------------------|----------------|
| 1 | 2022-12-23-dataops-similarities-and-differences-with-data-engineering-and-data-science.md | DataOps vs DE vs DS | Y (angelicaloduca) | `dataops-vs-data-engineering` (primary), `mlops-vs-dataops` | "how DataOps and data engineering split day-to-day ownership" | Inline near the "DataOps and Data Engineering" section + a "Go deeper" line at the end |
| 2 | 2022-06-11-what-dataops-exactly.md | What is DataOps exactly? | Y (angelicaloduca; Storytime for DataOps, Christopher Bergh) | `dataops` (primary), `dataops-tools` | "the full DataOps topic hub" / for the tools section: "DataOps tool categories" | "Go deeper" line after intro; inline link on "DataOps tools" section |
| 3 | 2022-05-15-devops-and-mlops-same-thing.md | DevOps vs MLOps | Y (angelicaloduca; The Rise of MLOps, Papapanagiotou + Grigorev) | `mlops-vs-devops` (primary), `mlops` | "which DevOps practices actually transfer to ML" | Inline at first "MLOps vs DevOps" comparison + "Go deeper" at end |
| 4 | 2020-12-14-data-roles.md | Data Team Roles — Alexey Grigorev (OLX) | Y (podcast episode; anchor.fm) | `data-roles` (primary), `data-teams` | "the data roles topic hub" | "Go deeper" line under the episode embed |
| 5 | 2022-07-12-building-data-science-team.md | Build a Data Science Team from Scratch | Y (angelicaloduca; Dat Tran) | `team-building` (primary), `hiring`, `data-teams` | "building and hiring data teams" | Inline at "who to hire first" + "Go deeper" at end |
| 6 | 2022-07-16-data-science-manager-vs-data-science-expert.md | DS Manager vs Expert | Y (angelicaloduca; Barbara Sobkowiak) | `data-science-for-managers` (primary), `leadership`, `data-team-lead-role` | "how managers scope and support data science work" | Inline near "when to hire a manager or an expert" |
| 7 | 2020-11-29-segmentation.md | Customer Segmentation with RFM+ and K-Means | N (authored how-to; embeds video) | `rfm-analysis` (primary), `machine-learning` | "the RFM analysis topic hub" | Inline at first mention of "RFM analysis" in the intro |
| 8 | 2021-02-01-landing-product-analyst-job.md | How I Landed a Product Analyst Job | ~ (Spotify link) | `product-analyst` (primary), `data-analyst-careers` | "what the product analyst role actually involves" | Inline at first mention of "product analyst" |
| 9 | 2022-09-17-how-to-setup-lightweight-local-version-for-airflow.md | Lightweight Local Airflow | N (embeds video) | `apache-airflow` (primary), `orchestration` | "how teams use Apache Airflow in production" | "Go deeper" line after intro |
| 10 | 2025-04-11-how-do-professionals-use-llm-tools-and-frameworks.md | How Professionals Use LLM Tools | ~ (community survey) | `llm-tools` (primary), `ai-tooling` | "choosing an LLM tool stack for real products" | Inline in intro / conclusion |
| 11 | 2025-04-15-how-do-data-professionals-use-data-engineering-tools-and-practices.md | How Professionals Use DE Tools | ~ (survey) | `data-engineering-tools` (primary), `modern-data-stack` | "the data engineering tools topic hub" | Inline in intro / conclusion |
| 12 | 2025-04-28-how-do-data-professionals-use-ml-and-mlops-tools-and-practices.md | How Professionals Use MLOps Tools | ~ (survey) | `mlops-tools` (primary), `mlops` | "MLOps tool categories and stack selection" | Inline in intro / conclusion |
| 13 | 2025-04-10-ai-tools-for-personal-productivity.md | AI Tools for Personal Productivity | ~ (survey) | `ai-tools-for-personal-productivity` (primary; exact match) | "how data professionals wire AI into daily work" | Inline in intro / conclusion |
| 14 | 2022-07-23-starting-career-as-data-scientist.md | Starting a Career as a Data Scientist | Y (angelicaloduca; ABC of DS, Danny Ma) | `data-science-careers` (primary), `data-scientist-role`, `data-roles` | "the data science careers hub" | "Go deeper" line after intro |
| 15 | 2022-07-15-what-open-source-can-do-for-your-data-career.md | What Open Source Can Do for Your Data Career | ~ (podcast ref; by Mehdi Ouazza) | `open-source` (primary), `open-source-portfolio-evidence` | "how open source becomes portfolio proof" | Inline at first mention of contributing |
| 16 | 2023-01-04-guidelines-to-get-data-engineer-job-against-odds.md | Get a Data Engineer Job Against the Odds | N | `how-to-become-a-data-engineer-with-no-experience` (primary), `job-search`, `data-analyst-to-data-engineer` | "becoming a data engineer with no experience" | Inline in intro |
| 17 | 2022-09-01-hiring-process-for-data-professionals.md | The Hiring Process for Data Professionals | N | `hiring` (primary), `job-search` | "how data hiring pipelines actually screen" | "Go deeper" line after intro |
| 18 | 2022-09-02-data-engineers-arent-plumbers.md | Data Engineers Aren't Plumbers | N | `data-engineer-role` (primary), `data-engineering` | "what data engineers really own" | Inline in intro |
| 19 | 2020-12-25-data-narrative.md | Data Storytelling | N (embeds video) | `communication` (primary), `technical-writing` | "communication as a core data skill" | "Go deeper" line at end |
| 20 | 2020-12-17-simplifying-concepts.md | Simplify Technical Concepts | N (embeds video) | `communication` (primary), `technical-writing` | "explaining technical concepts to stakeholders" | "Go deeper" line at end |
| 21 | 2022-07-31-essentials-of-public-speaking-for-career-in-data-science.md | Public Speaking for a DS Career | Y (angelicaloduca; Ben Taylor) | `communication` (primary), `career-development` | "communication and public proof in data careers" | "Go deeper" line after intro |
| 22 | 2020-12-07-practical-guide-better-code.md | Python CI/CD with GitHub Actions | N | `ci-cd` (primary), `testing` | "CI/CD for data, ML, and AI systems" | Inline at first mention of CI/CD |
| 23 | 2022-05-02-mlops-10-minutes.md | MLOps in 10 Minutes | ~ (by Alexey Grigorev) | `mlops` (primary), `mlops-architecture` | "the MLOps topic hub" | "Go deeper" line after intro |
| 24 | 2026-01-25-benefits-of-learning-in-public.md | Benefits of Learning in Public | Y (episode/podcast refs) | `learning-in-public-ai-career-switch` (primary), `career-development` | "how learning in public builds a career" | Inline at first mention of learning in public |
| 25 | 2025-02-26-building-ai-agent-that-thrives-in-real-world.md | Building an AI Agent That Thrives | N (Arize partner post) | `agent-engineering` (primary), `agent-ops` | "engineering AI agents for production" | Inline at first mention of "agent" |
| 26 | 2025-12-25-open-source-free-ai-agent-evaluation-tools.md | Open Source AI Agent Evaluation Tools | N | `llm-evaluation-workflows` (primary), `agent-ops`, `evaluation` | "evaluating agent and LLM systems" | Inline in intro |
| 27 | 2023-11-18-prepare-for-better-structured-data-extraction.md | Better Structured Data Extraction | N (Arize; LLM monitoring) | `llm-evaluation-workflows` (primary), `model-monitoring` | "LLM evaluation and monitoring in production" | Inline near the monitoring discussion |
| 28 | 2022-05-20-starting-career-in-data-science-at-45.md | Starting a DS Career at 45 | Y (interview format) | `career-transitions-in-data` (primary), `nontraditional-paths-to-ai-engineering` | "career transitions into data" | "Go deeper" line at end |
| 29 | 2023-02-21-summary-of-kitchenware-competition.md | Kaggle Kitchenware Competition | Y (angelicaloduca) | `competitions-beyond-kaggle` (primary), `computer-vision` | "using competitions as portfolio evidence" | "Go deeper" line at end |
| 30 | 2020-12-23-slack-communities.md | Best Data Science Slack Communities | N (by Alexey/Valeriia) | `community` (primary), `community-building` | "how communities support data learning" | Inline in intro |
| 31 | 2025-08-11-how-to-build-blood-cell-classifier-for-cancer-prediction-case-study-from-ml-zoomcamp.md | Blood Cell Classifier Case Study | ~ (zoomcamp case study) | `computer-vision` (primary), `healthcare-ml-validation-and-adoption`, `machine-learning-portfolio-projects` | "healthcare ML validation and adoption" | "Go deeper" line at end |
| 32 | 2025-08-05-how-to-build-waste-classifier-case-study-from-ml-zoomcamp.md | Waste Classifier Case Study | ~ (zoomcamp case study) | `computer-vision` (primary), `machine-learning-portfolio-projects`, `production-ml-project-checklist` | "computer vision project work" | "Go deeper" line at end |
| 33 | 2025-09-23-ai-dev-tools-zoomcamp-2025-...automation.md | AI Dev Tools Zoomcamp | ~ (podcast/yt refs) | `ai-coding-tools` (primary), `ai-tooling` | "how practitioners use AI coding assistants" | Inline in intro |
| 34 | 2021-01-01-ml-deployment-lambda.md | Deploy ML on AWS Lambda | N | `mlops` (primary), `machine-learning-engineer-role` | "putting ML models into production" | "Go deeper" line at end |
| 35 | 2022-09-29-do-you-know-golden-rules-while-working-with-data.md | Golden Rules Working With Data | N | `data-quality-and-observability` (primary), `dataops` | "data quality and observability practices" | Inline at end |
| 36 | 2022-10-02-naming-variables-in-machine-learning.md | Naming Variables in ML | N | `software-engineering` (primary), `reproducibility` | "software engineering discipline for ML" | "Go deeper" line at end |

Notes:
- Course/landing posts (ML/DE/MLOps/LLM Zoomcamp pages, free-courses lists) intentionally get
  at most a roadmap-hub "learn the field" link, not listed above individually — they are
  promotional and already internally linked. If desired, the strongest single addition would be
  linking each Zoomcamp page to its matching roadmap hub (`machine-learning-engineer-roadmap`,
  `data-engineer-roadmap`, `mlops-roadmap`, `ai-engineering-roadmap`).

### No good wiki match (deliberately skipped)
- 2020-12-17-ner-reformers.md — narrow NER/Reformer tutorial; only `nlp` is a loose fit, adds little depth.
- 2022-09-22-regularization-in-regression.md — no regression/regularization hub; `machine-learning` too generic.
- 2022-10-21-important-sql-fact-that-everyone-should-know.md — no SQL hub; would be a forced `data-engineering` link.
- 2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker.md — infra how-to; no matching hub.
- 2022-08-22-interview-with-ken-wu.md, 2022-09-29-interview-with-valerii-chetvertakov.md — ML Zoomcamp internship interviews; no topical hub adds depth.
- 2023-12-11-8-newsletters-...md, 2025-08-16-free-machine-learning-courses.md, 2025-12-10-free-data-engineering-courses.md, 2024-04-11-guide-to-free-online-courses-...md — curated link lists; no topic hub is a natural target.
- 2023-08-17/2023-11-18/2024-03-07/2024-11-11 Zoomcamp landing pages, 2024-10-21 winning solutions, 2025-05-16 community demographics, 2025-08-05/2025-08-11 "key lessons"/"building discipline" course reflections — promotional/course pages; optional roadmap-hub link only (see Notes).

---

## (B) ENRICHMENT CANDIDATES

Podcast-derived (mostly angelicaloduca "freely inspired by episode X") articles whose target
wiki hub already cites the SAME guest/episode — so the hub holds concrete quotes, timestamps,
and cross-guest context the thin blog article could absorb in a later content pass.
Verified: the listed guests appear as `[[person:...]]` citations inside the named hub.

| # | Post file | Wiki hub with the evidence | Podcast evidence that could be added |
|---|-----------|----------------------------|--------------------------------------|
| 1 | 2022-06-11-what-dataops-exactly.md | `dataops`, `dataops-vs-data-engineering` | Both hubs cite Christopher Bergh (the article's actual source, "Storytime for DataOps"), plus Lars Albertsson, Tomasz Hinc, Barr Moses, Mehdi Ouazza — timestamped DataOps definitions and tool discussion beyond the single episode. |
| 2 | 2022-12-23-dataops-similarities-and-differences-...md | `dataops-vs-data-engineering`, `mlops-vs-dataops` | Hub is explicitly grounded in Tomasz Hinc, Christopher Bergh, and Lars Albertsson interviews — the exact ownership-split framing this article gropes toward, with episode citations. |
| 3 | 2022-05-15-devops-and-mlops-same-thing.md | `mlops-vs-devops`, `mlops` | Hub cites Theofilos Papapanagiotou (the article's source, "The Rise of MLOps") plus Maria Vechtomova, Santiago Valdarrama, Nadia Nahar — concrete "which DevOps practices transfer / which risks they miss" evidence. |
| 4 | 2022-07-12-building-data-science-team.md | `team-building`, `data-science-for-managers` | Both hubs cite Dat Tran (the article's source, "Building a Data Science Team") plus Katie Bauer, Lisa Cohen, Rahul Jain — hiring-order and specialist-vs-generalist evidence from multiple guests. |
| 5 | 2022-07-16-data-science-manager-vs-data-science-expert.md | `data-science-for-managers`, `leadership` | Hub cites Barbara Sobkowiak (the article's source) alongside Dat Tran, Alicja Notowska, Ben Wilson — richer manager-vs-expert and when-to-hire evidence. |
| 6 | 2020-12-14-data-roles.md | `data-roles`, `data-teams` | Alexey's own OLX episode grounds the post; the hub adds Dat Tran, Ben Wilson, Greg Coquillo, Jeff Katz and others defining each role, so the article could cite cross-guest agreement/disagreement. |
| 7 | 2022-07-31-essentials-of-public-speaking-...md | `communication` | Hub does NOT cite Ben Taylor (the source guest), but covers public speaking / evangelism via other guests (Eugene Yan, Nick Singh, etc.) — still a source of concrete communication stories to fold in. Lower-confidence enrichment. |
| 8 | 2022-07-23-starting-career-as-data-scientist.md | `data-science-careers`, `data-scientist-role` | Hub does NOT cite Danny Ma (the source guest); enrichment is weaker, but the hub's Type A/B/C-style role framing from other guests could still be layered in. Lower-confidence. |
| 9 | 2020-11-29-segmentation.md (not angelica, but strong) | `rfm-analysis` | Hub cites Jakob Graff, Juan Orduz, Arpit Choudhury, Nikola Maksimovic on RFM in product/analytics context — episodes this authored how-to could reference to ground its RFM framing. |
| 10 | 2021-02-01-landing-product-analyst-job.md | `product-analyst` | Hub cites Jakob Graff, Arpit Choudhury, Juan Manuel Perafan on the product analyst role — real-episode role evidence to strengthen this personal-story post. |

Highest-confidence enrichment (source guest is cited in the target hub): rows 1–6.
Lower-confidence (topical hub, source guest not in hub): rows 7–10.

---

## Summary of counts
- Posts proposed for a wiki link: 36 of 54.
- Of those, podcast-derived (Y) or podcast-tied (~): 8 clearly podcast-derived (Y) + ~10 podcast/survey-tied (~).
- Deliberately skipped (no good match): ~18 (narrow tutorials + course/list landing pages).
- Enrichment candidates: 10 (6 high-confidence where the source guest is cited in the hub, 4 lower-confidence).
