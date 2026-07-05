# Keyword and Content Suggestion Audit

This audit records what was extracted from the two provided suggestion files and
how it maps to the current podwiki editorial content set.

Input files:

- `.tmp/ubersuggest_Current_Queries.csv`
- `.tmp/next-actions-done-datatalks.club.xlsx`

## Extraction Result

- Ubersuggest CSV rows extracted: 1000
- Existing tagged wiki/editorial pages checked: 79
  (`_wiki/` pages with `guide`, `comparison`, `roadmap`, `transition`, or
  `how-to` tags)
- Existing wiki pages checked: 281
- Excel workbook tabs checked in the local file:
  `Quick-wins`, `Competitor Gaps`, `Code Fix`
- Excel rows beyond headers in the local file: 0
- Expected rows in the intended gaps export: 689

The workbook was checked through the raw `.xlsx` XML. The local file at
`.tmp/next-actions-done-datatalks.club.xlsx` is 17,859 bytes and has these
sheet dimensions:

- `Quick-wins`: `A1:C1`
- `Competitor Gaps`: `A1:B1`
- `Code Fix`: `A1:A1`

So the checked local Excel file currently contains only headers, not content
rows. The 689 expected rows are not present in the checked workbook. This does
not mean there are no gap suggestions; it means the local `.tmp` workbook should
be replaced with the populated export or added next to it before we create
content from the gap source.

## CSV Use

The CSV is the source for editorial keywords. We should not create one page per
keyword row. We should group related keyword variants into one content target
when they express the same search intent.

Editorial targets live in `_wiki/` with a type tag such as `guide`,
`comparison`, `roadmap`, `transition`, or `how-to`. Public URLs are
`/wiki/<slug>/`. Before publication, each page should cross-link relevant wiki
pages, canonical podcast evidence, and the podcast discussions that ground its
claims.

The normalized keyword artifacts in `artifacts/keywords/` are historical
analysis artifacts. If regenerated, they should map editorial coverage to
`_wiki/` files and type tags, not retired `_articles/` or split editorial
collections.

Rows such as `slack`, `download"`, unrelated book/PDF queries, and misspellings
without a DataTalks.Club angle are kept in the raw extraction but excluded from
the editorial backlog below.

## Existing Coverage

These keyword groups already have editorial coverage:

| Group | Existing content | Covered keyword variants |
|---|---|---|
| Data engineering courses | `_wiki/data-engineer-roadmap.md` | data engineering course, data engineering courses, best data engineering course, free data engineering course |
| Data engineering bootcamps | `_wiki/data-engineer-roadmap.md` | data engineering bootcamp, data engineer bootcamp |
| Data engineering roadmaps | `_wiki/data-engineer-roadmap.md` | data engineer roadmap |
| Data pipeline projects | `_wiki/end-to-end-data-pipeline-project.md`, `_wiki/how-to-build-data-pipelines.md` | build data pipelines, data engineering pipeline project |
| Data engineering consulting | `_wiki/freelance.md` | data engineering consulting, data engineering consultant, data engineer consulting, data engineer consultant |
| Freelance data engineering | `_wiki/freelance.md` | freelance data engineer, data engineering freelance |
| Portfolio projects | `_wiki/portfolio-projects.md`, `_wiki/data-engineering-portfolio-projects.md`, `_wiki/machine-learning-portfolio-projects.md`, `_wiki/analytics-engineering-portfolio-projects.md`, `_wiki/rag-portfolio-projects.md`, `_wiki/open-source-portfolio-evidence.md`, `_wiki/volunteer-data-engineering-projects.md` | portfolio projects, data engineering portfolio projects, machine learning portfolio projects, analytics engineering portfolio projects, rag portfolio projects, volunteer data engineering projects, open source data engineering portfolio, nonprofit data engineering projects, data engineering volunteer work |
| MLOps core terms | `_wiki/mlops.md`, `_wiki/mlops-roadmap.md`, `_wiki/mlops-tools.md`, `_wiki/mlops-architecture.md`, `_wiki/mlops-engineer.md` | mlops, what is mlops, mlops course, mlops tools, mlops architecture |
| DataOps core terms | `_wiki/dataops.md`, `_wiki/dataops-tools.md`, `_wiki/mlops-vs-dataops.md`, `_wiki/dataops-vs-data-engineering.md` | dataops, data ops, dataops tools, mlops vs dataops, dataops vs data engineering |
| Machine learning system design | `_wiki/machine-learning-system-design.md`, `_wiki/machine-learning-system-design-interview.md` | machine learning system design, ml system design interview, designing machine learning systems |
| LLM system design | `_wiki/llm-system-design-interview.md` | llm system design interview |
| Business Intelligence | `_wiki/business-intelligence.md` | ai powered business intelligence, business intelligence |
| Machine learning for software engineers | `_wiki/machine-learning-for-software-engineers.md`, `_wiki/software-engineer-to-machine-learning.md`, `_wiki/machine-learning-vs-software-engineering.md` | machine learning for software engineers, software engineering machine learning, machine learning vs software engineering, software engineering vs machine learning, machine learning and software engineering, software engineer vs machine learning engineer |
| Machine learning startups | `_wiki/machine-learning-for-startups.md` | machine learning for startups |
| Data scientist interview | `_wiki/data-scientist-interview.md` | data scientist interview |
| Data science project management and PM transitions | `_wiki/data-science-project-management.md`, `_wiki/project-manager-to-data-science.md` | data science project management, project management for data science, data science project manager, project manager to data science, project manager to data scientist, project management to data science |
| Data product roles | `_wiki/data-product-manager.md`, `_wiki/data-product-management.md`, `_wiki/product-analyst.md` | data product manager, data product management, product analyst |
| Product owner vs product manager | `_wiki/product-owner-vs-product-manager.md`, `_wiki/data-product-owner-vs-data-product-manager.md` | data product owner, data science product owner, data product owner vs data product manager |
| Data engineering management | `_wiki/data-engineering-manager-role.md`, `_wiki/leadership.md` | data engineering manager, data engineer manager, data engineering manager job description, data engineering manager roles and responsibilities |
| Airflow | `_wiki/apache-airflow.md`, `_wiki/orchestration.md` | airflow, apache airflow, airflow docker compose, airflow lite, airflow standalone docker, install airflow docker compose, lightweight airflow |
| Data Engineering Zoomcamp | main DataTalks.Club course page | data engineering zoomcamp, data-engineering-zoomcamp, dataengineering zoomcamp, data engineer zoomcamp, data engineering zoom camp |
| MLOps Zoomcamp | main DataTalks.Club course page | mlops zoomcamp, mlops-zoomcamp, mlops zoom camp, datatalks.club mlops zoomcamp |
| Machine Learning Zoomcamp | main DataTalks.Club course page | machine learning zoomcamp, ml zoomcamp, machine learning zoomcamp reddit |
| LLM Zoomcamp | main DataTalks.Club course page | llm zoomcamp, llm zoomcamp data talks club, datatalksclub llm zoomcamp |
| Data Science for Managers | `_wiki/leadership.md` | data science for managers |
| Data Roles | `_wiki/data-roles.md` | data roles |
| Data Analysis | `_wiki/data-analysis.md` | data analysis |
| Hire Data Engineers | `_wiki/hire-data-engineers.md` | hire data engineers |
| Data Science Recruiter | `_wiki/data-science-recruiter.md` | data science headhunter, data scientist headhunter |
| AI Tools for Personal Productivity | `_wiki/ai-tools-for-personal-productivity.md` | ai tools for personal productivity, ai for personal productivity |
| Delta Lake vs Apache Iceberg | `_wiki/delta-lake-vs-apache-iceberg.md` | delta lake, delta lake vs apache iceberg, apache iceberg vs delta lake |
| ETL vs ELT | `_wiki/etl-vs-elt.md` | etl vs elt, elt vs etl, etl and elt |
| DataOps Platforms | `_wiki/dataops-platforms.md` | dataops platforms |
| DataOps Engineer Role | `_wiki/dataops-engineer-role.md`, `_wiki/dataops-vs-data-engineering.md`, `_wiki/mlops-vs-dataops.md` | data ops engineer, dataops engineer, dataops engineer vs data engineer |
| Chief Data Officer Role | `_wiki/chief-data-officer-role.md`, `_wiki/leadership.md`, `_wiki/data-team-lead-role.md` | chief data officer skills, chief data officer interview questions |
| A/B Testing | `_wiki/a-b-testing.md`, `_wiki/experimentation-and-causal-inference.md`, `_wiki/experimentation.md`, `_wiki/power-analysis.md` | a/b testing podcast, ab testing, product experimentation |
| Recommendation Systems | `_wiki/recommendation-systems.md`, `_wiki/search.md`, `_wiki/vector-databases.md`, `_wiki/machine-learning-system-design.md` | machine learning personalization, personalization machine, practical recommender systems |
| Entity Resolution | `_wiki/entity-resolution.md`, `_wiki/open-source.md`, `_wiki/open-source-portfolio-evidence.md` | open source entity resolution, entity resolution use cases, identity resolution vs entity resolution, zingg entity resolution |
| RFM Analysis | `_wiki/rfm-analysis.md`, `_wiki/product-analytics.md`, `_wiki/analytics-engineering.md` | rfm analysis, rfm segmentation, rfm analysis for customer segmentation |
| Open Source | `_wiki/open-source.md`, `_wiki/open-source-portfolio-evidence.md`, `_wiki/open-source-contributor-roadmap.md` | what is open source, data engineering open source projects |
| Tech Startups | `_wiki/startups.md`, `_wiki/founder.md`, `_wiki/entrepreneurship.md`, `_wiki/machine-learning-for-startups.md` | tech startups, machine learning startup, machine learning for startups, startup machine learning, ml startups |

## Conditional CSV Items

These groups are visible in the CSV but are not recommended as podwiki pages
unless DataTalks.Club wants owned-channel content grounded in real newsletter or
community assets. They are not active editorial backlog.

| Priority | Content target | Keyword variants from CSV | Recommendation |
|---:|---|---|---|
| 3 | Machine Learning Newsletter | machine learning newsletter, machine learnings newsletter | Conditional only: not recommended for podwiki unless DataTalks.Club wants owned-channel content grounded in real newsletter/community assets. |
| 3 | DTC Newsletter | dtc newsletter | Conditional only: not recommended for podwiki unless DataTalks.Club wants owned-channel content grounded in real newsletter/community assets. |

## Not Recommended From This CSV

These rows are present but should not drive podwiki content unless there is a
separate site strategy:

- Generic product/navigation terms: `slack`, `slack careers`, `slack online`,
  `google calendar slack`
- Book/PDF/free-download queries: `ace the data science interview pdf`,
  `build a large language model from scratch`, `grokking machine learning`,
  `natural language processing with transformers`
- Unclear or unrelated terms: `download"`, `scale"`, `faang`
- Owned-channel terms without a current podwiki archive angle:
  `machine-learning-newsletter`, `machine learning newsletter`,
  `machine learnings newsletter`, `dtc newsletter`. Reconsider only if
  DataTalks.Club wants a newsletter/community landing page with real owned
  assets and links.

## Completed From This Audit

The first content batches from this audit created the following durable podwiki
coverage. The four branded Zoomcamp guide pages were later removed because the
main DataTalks.Club site owns those course queries.

1. `_wiki/leadership.md`
2. `_wiki/data-roles.md`
3. `_wiki/data-analysis.md`
4. `_wiki/hire-data-engineers.md`
5. `_wiki/data-science-recruiter.md`
6. `_wiki/ai-tools-for-personal-productivity.md`
7. `_wiki/product-owner-vs-product-manager.md`
8. `_wiki/data-product-owner-vs-data-product-manager.md`
9. `_wiki/delta-lake-vs-apache-iceberg.md`
10. `_wiki/etl-vs-elt.md`
11. `_wiki/dataops-platforms.md`
12. `_wiki/open-source.md`
13. `_wiki/startups.md`
14. `_wiki/founder.md`
15. `_wiki/entrepreneurship.md`
16. `_wiki/machine-learning-for-startups.md`
18. `_wiki/apache-airflow.md`
19. `_wiki/recommendation-systems.md`
20. `_wiki/entity-resolution.md`
21. `_wiki/rfm-analysis.md`
22. `_wiki/chief-data-officer-role.md`
23. `_wiki/dataops-engineer-role.md`
24. `_wiki/machine-learning-vs-software-engineering.md`
25. `_wiki/project-manager-to-data-science.md`
26. `_wiki/volunteer-data-engineering-projects.md`

`_wiki/apache-airflow.md` was also enriched on 2026-07-05 for Airflow
Docker/local workflow intent while keeping the main DataTalks.Club Docker
Compose article canonical for setup instructions.

The duplicate data engineering course, courses, bootcamp, and training guide
variants were later removed. Their useful guidance belongs in
`_wiki/data-engineer-roadmap.md`, with roadmap-specific intents still covered
by `_wiki/data-engineer-roadmap.md` and
`_wiki/how-to-become-a-data-engineer-with-no-experience.md`.

The duplicate MLOps course, courses, certification, machine learning bootcamp,
and machine learning engineer certification guide variants were later removed.
Their useful guidance belongs in `_wiki/mlops-roadmap.md`.

The freelance and consulting keyword variants were consolidated into
`_wiki/freelance.md`; do not recreate separate guide pages for those variants.
The data-engineering-manager and data-engineer-manager keyword variants were
consolidated into `_wiki/leadership.md`; do not recreate separate guide pages
for those variants.
A/B testing should remain wiki concept coverage through `_wiki/a-b-testing.md`
and the experimentation wiki cluster, not guide or category content.
AI-powered business intelligence was moved into `_wiki/business-intelligence.md`
so the AI material supports a durable wiki topic rather than a standalone
keyword guide.

## Current Content Step

Replace the local gaps workbook with the populated 689-row export, then group
those gap suggestions separately from the Ubersuggest keyword backlog. Until
that file is available locally, do not use the headers-only workbook as a source
for content decisions.

The 2026-07-01 follow-up audit confirmed that the local workbook still contains
only headers. The strongest CSV-backed candidates from the current CSV have now
been published and tightened:

1. `machine learning business`, `machine learning for small business`, and
   related variants are covered by `_wiki/machine-learning-for-business.md`,
   grounded in data products, ML strategy, startup, adoption, metrics, and
   production ML episodes.
2. `data science project management`, `project management for data science`,
   `data science project manager`, and related variants are covered by
   `_wiki/data-science-project-management.md`, grounded in stakeholder planning,
   scope, KPIs, delivery, and analytics/ML project evidence.
3. `data science stock market`, `data analytics stock market`, `python stock
   analysis`, and related variants are covered by `_wiki/algorithmic-trading.md`,
   grounded in the algorithmic-trading episode and the Machine Learning for
   Algorithmic Trading book reference. The page is educational and explicitly
   not trading advice.

Improve existing pages rather than creating new ones for data events,
podcast-discovery queries, and Relevant Search. Keep ignoring book/PDF,
free-download, Slack, DataQuest, and generic navigation rows. Tavily appears in
the local archive only as an affiliation mention, not as a substantive podcast
discussion of the tool, so it should remain excluded until stronger source
evidence exists.

The newsletter cluster (`machine-learning-newsletter` / `dtc-newsletter`)
remains conditional and is not recommended for podwiki unless it becomes
community-content or owned-channel content with real DataTalks.Club asset links.
The broad Tech Startups keyword belongs to the startup wiki cluster rather than
a separate generic guide.

The 2026-07-05 five-agent follow-up confirmed that the Excel workbook still
contains only headers. The remaining 2026-07-04 CSV-backed candidates have now
been handled: `_wiki/apache-airflow.md` was tightened for Docker/local workflow
intent; `_wiki/machine-learning-vs-software-engineering.md` covers the ML vs
software engineering comparison intent; `_wiki/project-manager-to-data-science.md`
covers the PM-to-data-science transition intent; and
`_wiki/volunteer-data-engineering-projects.md` covers volunteer, nonprofit, and
open-source data engineering portfolio intent.

`_wiki/data-ai-conference-building.md` was tightened for `data analytics events`
and `data events` intent without creating a duplicate page.

The 2026-07-06 `scripts/keyword_gap.py` rerun against the current
`.tmp/ubersuggest_Current_Queries.csv` found 0 `GAP_GROUNDED` clusters:
127 keywords were already covered by podwiki, 318 belonged to the main website,
113 were branded/navigation, 204 were book-download/book-intent queries, and
220 were ungrounded gaps. This means the current CSV supports maintenance of
canonical pages rather than new page creation.

Residual CSV intent is now maintenance for canonical pages, not a new-page
queue. Enrich the relevant existing page when new evidence appears: use the
newer pages above for their covered intents; MLOps architecture and engineer
role pages for framework, architect, and diagram queries; DataOps platforms and
pipeline how-to pages for platform/software and pipeline-training variants; and
hiring, no-experience, analyst-career, certification, data-engineering-manager,
and product-analyst pages for career and role variants. Do not create duplicate
pages for those terms.
