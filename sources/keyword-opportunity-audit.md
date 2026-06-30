# Keyword and Content Suggestion Audit

This audit records what was extracted from the two provided suggestion files and
how it maps to the current podwiki editorial content set.

Input files:

- `.tmp/ubersuggest_Current_Queries.csv`
- `.tmp/next-actions-done-datatalks.club.xlsx`

## Extraction Result

- Ubersuggest CSV rows extracted: 1000
- Existing editorial pages checked: 76
- Existing wiki pages checked: 168
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
rows. This does not mean there are no gap suggestions. The expected source has
689 rows, so the local `.tmp` workbook should be replaced with the populated
export or added next to it before we create content from the gap source.

## CSV Use

The CSV is the source for editorial keywords. We should not create one page per
keyword row. We should group related keyword variants into one content target
when they express the same search intent.

Editorial targets live in `_guides/`, `_comparisons/`, `_roadmaps/`, or
`_how_tos/`, with public URLs under `/guides/`, `/comparisons/`, `/roadmaps/`,
and `/how-tos/`. Before publication, each page should cross-link relevant wiki
pages, people pages, local podcast pages, and the podcast evidence that grounds
its claims.

Rows such as `slack`, `download"`, unrelated book/PDF queries, and misspellings
without a DataTalks.Club angle are kept in the raw extraction but excluded from
the editorial backlog below.

## Existing Coverage

These keyword groups already have editorial coverage:

| Group | Existing content | Covered keyword variants |
|---|---|---|
| Data engineering courses | `_guides/data-engineering-course.md`, `_guides/data-engineering-courses.md`, `_guides/best-data-engineering-course.md`, `_guides/free-data-engineering-course.md` | data engineering course, data engineering courses, best data engineering course, free data engineering course |
| Data engineering bootcamps | `_guides/data-engineering-bootcamp.md`, `_guides/data-engineer-bootcamp.md` | data engineering bootcamp, data engineer bootcamp |
| Data engineering roadmaps | `_roadmaps/data-engineer-roadmap.md` | data engineer roadmap |
| Data pipeline projects | `_guides/data-engineering-pipeline-project.md`, `_how_tos/how-to-build-data-pipelines.md` | build data pipelines, data engineering pipeline project |
| Data engineering consulting | `_guides/data-engineering-consulting.md`, `_guides/data-engineering-consultant.md`, `_guides/data-engineer-consulting.md`, `_guides/data-engineer-consultant.md` | data engineering consulting, data engineering consultant, data engineer consulting |
| Freelance data engineering | `_guides/freelance-data-engineer.md`, `_guides/data-engineering-freelance.md` | freelance data engineer, data engineering freelance |
| MLOps core terms | `_wiki/mlops.md`, `_guides/mlops-course.md`, `_guides/mlops-courses.md`, `_wiki/mlops-tools.md`, `_guides/mlops-frameworks.md`, `_guides/mlops-architecture.md`, `_wiki/mlops-engineer.md`, `_guides/mlops-certification.md` | mlops, what is mlops, mlops course, mlops tools, mlops architecture |
| DataOps core terms | `_wiki/dataops.md`, `_guides/dataops-tools.md`, `_comparisons/dataops-vs-data-engineering.md`, `_comparisons/mlops-vs-dataops.md` | dataops, data ops, dataops tools, mlops vs dataops |
| Machine learning system design | `_wiki/machine-learning-system-design.md`, `_guides/machine-learning-system-design-interview.md`, `_guides/ml-system-design-interview.md`, `_guides/designing-machine-learning-systems.md` | machine learning system design, ml system design interview, designing machine learning systems |
| LLM system design | `_guides/llm-system-design-interview.md` | llm system design interview |
| Machine learning for software engineers | `_guides/machine-learning-for-software-engineers.md`, `_wiki/software-engineer-to-machine-learning.md` | machine learning for software engineers, software engineering machine learning |
| Machine learning startups | `_guides/machine-learning-for-startups.md` | machine learning for startups |
| Data scientist interview | `_guides/data-scientist-interview.md` | data scientist interview |
| Data product roles | `_guides/data-product-manager.md`, `_guides/data-product-manager-role.md`, `_guides/product-analyst.md` | data product manager, data product management, product analyst |
| Product owner vs product manager | `_comparisons/product-owner-vs-product-manager.md` | data product owner, data science product owner |
| Airflow | `_guides/airflow.md`, `_guides/apache-airflow.md`, `_how_tos/airflow-docker-compose.md` | airflow, apache airflow, airflow docker compose |
| Data Engineering Zoomcamp | `_guides/data-engineering-zoomcamp.md` | data engineering zoomcamp, data-engineering-zoomcamp, dataengineering zoomcamp, data engineer zoomcamp, data engineering zoom camp |
| MLOps Zoomcamp | `_guides/mlops-zoomcamp.md` | mlops zoomcamp, mlops-zoomcamp, mlops zoom camp, datatalks.club mlops zoomcamp |
| Machine Learning Zoomcamp | `_guides/machine-learning-zoomcamp.md` | machine learning zoomcamp, ml zoomcamp, machine learning zoomcamp reddit |
| LLM Zoomcamp | `_guides/llm-zoomcamp.md` | llm zoomcamp, llm zoomcamp data talks club, datatalksclub llm zoomcamp |
| Data Science for Managers | `_guides/data-science-for-managers.md` | data science for managers |
| Data Roles | `_guides/data-roles.md` | data roles |
| Data Analysis | `_guides/data-analysis.md` | data analysis |
| Hire Data Engineers | `_guides/hire-data-engineers.md` | hire data engineers |
| Data Science Recruiter | `_guides/data-science-recruiter.md` | data science headhunter, data scientist headhunter |
| AI Tools for Personal Productivity | `_guides/ai-tools-for-personal-productivity.md` | ai tools for personal productivity, ai for personal productivity |
| Delta Lake vs Apache Iceberg | `_comparisons/delta-lake-vs-apache-iceberg.md` | delta lake, delta lake vs apache iceberg, apache iceberg vs delta lake |

## Editorial Backlog From CSV

These groups are plausible content targets from the CSV that are not yet covered
well enough by existing pages. They still need podcast grounding before
publication.

| Priority | Content target | Keyword variants from CSV | Why it may be worth creating |
|---:|---|---|---|
| 1 | DataOps Platforms | dataops platforms | Adjacent pages exist, but the platform angle may need its own grounded hub. |
| 2 | Open Source | what is open source | Improve the open-source wiki first; only create a guide if the keyword is strategically useful. |
| 3 | A/B Testing Podcast | a/b testing podcast | Good fit as a curated listening guide through experimentation episodes, not as a generic explainer. |
| 4 | Machine Learning Newsletter | machine learning newsletter, machine learnings newsletter | Do not create a generic newsletter guide. Keep for a possible community-content or owned-channel guide only. |
| 5 | Tech Startups | tech startups | Broad; probably lower priority than machine-learning-for-startups, which already exists. |

## Not Recommended From This CSV

These rows are present but should not drive podwiki content unless there is a
separate site strategy:

- Generic product/navigation terms: `slack`, `slack careers`, `slack online`,
  `google calendar slack`
- Book/PDF/free-download queries: `ace the data science interview pdf`,
  `build a large language model from scratch`, `grokking machine learning`,
  `natural language processing with transformers`
- Unclear or unrelated terms: `download"`, `scale"`, `rfm analysis`,
  `rfm segmentation`, `faang`

## Completed From This Audit

The first content batches from this audit have been created:

1. `_guides/data-engineering-zoomcamp.md`
2. `_guides/mlops-zoomcamp.md`
3. `_guides/machine-learning-zoomcamp.md`
4. `_guides/llm-zoomcamp.md`
5. `_guides/data-science-for-managers.md`
6. `_guides/data-roles.md`
7. `_guides/data-analysis.md`
8. `_guides/hire-data-engineers.md`
9. `_guides/data-science-recruiter.md`
10. `_guides/ai-tools-for-personal-productivity.md`
11. `_comparisons/product-owner-vs-product-manager.md`
12. `_comparisons/delta-lake-vs-apache-iceberg.md`

## Next Content Step

Replace the local gaps workbook with the populated 689-row export, then group
those gap suggestions separately from the Ubersuggest keyword backlog. Until
that file is available locally, continue with the remaining CSV backlog in the
table above.

The next strongest comparison pages from the current backlog are ETL vs ELT,
data analyst vs analytics engineer, and RAG vs fine-tuning. The next strongest
non-comparison page is DataOps Platforms. Machine Learning Newsletter should
stay out of scope unless it becomes a community-content or owned-channel guide
with real DataTalks.Club asset links.
