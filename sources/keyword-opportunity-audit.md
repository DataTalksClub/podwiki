# Keyword and Content Suggestion Audit

This audit records what was extracted from the two provided suggestion files and
how it maps to the current podwiki article set.

Input files:

- `.tmp/ubersuggest_Current_Queries.csv`
- `.tmp/next-actions-done-datatalks.club.xlsx`

## Extraction Result

- Ubersuggest CSV rows extracted: 1000
- Existing article pages checked: 71
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

The CSV is the source for article keywords. We should not create one article per
keyword row. We should group related keyword variants into one article target
when they express the same search intent.

Rows such as `slack`, `download"`, unrelated book/PDF queries, and misspellings
without a DataTalks.Club angle are kept in the raw extraction but excluded from
the article backlog below.

## Existing Coverage

These keyword groups already have article coverage:

| Group | Existing article | Covered keyword variants |
|---|---|---|
| Data engineering courses | `_articles/data-engineering-course.md`, `_articles/data-engineering-courses.md`, `_articles/best-data-engineering-course.md`, `_articles/free-data-engineering-course.md` | data engineering course, data engineering courses, best data engineering course, free data engineering course |
| Data engineering bootcamps | `_articles/data-engineering-bootcamp.md`, `_articles/data-engineer-bootcamp.md` | data engineering bootcamp, data engineer bootcamp |
| Data engineering roadmaps | `_articles/data-engineer-roadmap.md` | data engineer roadmap |
| Data pipeline projects | `_articles/data-engineering-pipeline-project.md`, `_articles/how-to-build-data-pipelines.md` | build data pipelines, data engineering pipeline project |
| Data engineering consulting | `_articles/data-engineering-consulting.md`, `_articles/data-engineering-consultant.md`, `_articles/data-engineer-consulting.md`, `_articles/data-engineer-consultant.md` | data engineering consulting, data engineering consultant, data engineer consulting |
| Freelance data engineering | `_articles/freelance-data-engineer.md`, `_articles/data-engineering-freelance.md` | freelance data engineer, data engineering freelance |
| MLOps core terms | `_articles/mlops.md`, `_articles/what-is-mlops.md`, `_articles/mlops-course.md`, `_articles/mlops-courses.md`, `_articles/mlops-tools.md`, `_articles/mlops-frameworks.md`, `_articles/mlops-architecture.md`, `_articles/mlops-engineer.md`, `_articles/mlops-certification.md` | mlops, what is mlops, mlops course, mlops tools, mlops architecture |
| DataOps core terms | `_articles/dataops.md`, `_articles/dataops-tools.md`, `_articles/dataops-vs-data-engineering.md`, `_articles/mlops-vs-dataops.md` | dataops, data ops, dataops tools, mlops vs dataops |
| Machine learning system design | `_articles/machine-learning-system-design.md`, `_articles/machine-learning-system-design-interview.md`, `_articles/ml-system-design-interview.md`, `_articles/designing-machine-learning-systems.md` | machine learning system design, ml system design interview, designing machine learning systems |
| LLM system design | `_articles/llm-system-design-interview.md` | llm system design interview |
| Machine learning for software engineers | `_articles/machine-learning-for-software-engineers.md`, `_articles/software-engineer-to-machine-learning.md` | machine learning for software engineers, software engineering machine learning |
| Machine learning startups | `_articles/machine-learning-for-startups.md` | machine learning for startups |
| Data scientist interview | `_articles/data-scientist-interview.md` | data scientist interview |
| Data product roles | `_articles/data-product-manager.md`, `_articles/data-product-manager-role.md`, `_articles/product-analyst.md` | data product manager, data product management, product analyst |
| Airflow | `_articles/airflow.md`, `_articles/apache-airflow.md`, `_articles/airflow-docker-compose.md` | airflow, apache airflow, airflow docker compose |
| Data Engineering Zoomcamp | `_articles/data-engineering-zoomcamp.md` | data engineering zoomcamp, data-engineering-zoomcamp, dataengineering zoomcamp, data engineer zoomcamp, data engineering zoom camp |
| MLOps Zoomcamp | `_articles/mlops-zoomcamp.md` | mlops zoomcamp, mlops-zoomcamp, mlops zoom camp, datatalks.club mlops zoomcamp |
| Machine Learning Zoomcamp | `_articles/machine-learning-zoomcamp.md` | machine learning zoomcamp, ml zoomcamp, machine learning zoomcamp reddit |
| LLM Zoomcamp | `_articles/llm-zoomcamp.md` | llm zoomcamp, llm zoomcamp data talks club, datatalksclub llm zoomcamp |
| Data Science for Managers | `_articles/data-science-for-managers.md` | data science for managers |

## Article Backlog From CSV

These groups are plausible article targets from the CSV that are not yet covered
well enough by an existing article. They still need podcast grounding before
publication.

| Priority | Article target | Keyword variants from CSV | Why it may be worth creating |
|---:|---|---|---|
| 1 | Data Roles | data roles | Can become a role-navigation article linking role wiki pages and podcast evidence. |
| 2 | Data Analysis | data analysis | High volume, but broad. Needs a DataTalks-specific angle, probably analytics workflows and analyst role boundaries. |
| 3 | Hire Data Engineers | hire data engineers | Commercial-intent article grounded in hiring, team-building, and data engineering role episodes. |
| 4 | Data Science Headhunter / Recruiter | data science headhunter, data scientist headhunter | Possible hiring-market article if enough podcast evidence exists. |
| 5 | AI Tools for Personal Productivity | ai tools for personal productivity, ai for personal productivity | Possible article if grounded in AI tooling and productivity episodes; avoid generic tool-list content. |
| 6 | Machine Learning Newsletter | machine learning newsletter, machine learnings newsletter | Possible DataTalks/community article, but lower priority unless it maps to a real site asset. |
| 7 | What Is Open Source | what is open source | Could reuse the open-source wiki, but only create an article if the keyword is strategically useful. |
| 8 | Tech Startups | tech startups | Broad; probably lower priority than machine-learning-for-startups, which already exists. |
| 9 | Delta Lake | delta lake | Wiki exists, but no article. Create only if podcast evidence is strong enough. |

## Not Recommended From This CSV

These rows are present but should not drive podwiki articles unless there is a
separate site strategy:

- Generic product/navigation terms: `slack`, `slack careers`, `slack online`,
  `google calendar slack`
- Book/PDF/free-download queries: `ace the data science interview pdf`,
  `build a large language model from scratch`, `grokking machine learning`,
  `natural language processing with transformers`
- Unclear or unrelated terms: `download"`, `scale"`, `rfm analysis`,
  `rfm segmentation`, `faang`

## Completed From This Audit

The first article batch from this audit has been created:

1. `_articles/data-engineering-zoomcamp.md`
2. `_articles/mlops-zoomcamp.md`
3. `_articles/machine-learning-zoomcamp.md`
4. `_articles/llm-zoomcamp.md`
5. `_articles/data-science-for-managers.md`

## Next Content Step

Replace the local gaps workbook with the populated 689-row export, then group
those gap suggestions separately from the Ubersuggest keyword backlog. Until
that file is available locally, continue with the remaining CSV backlog in the
table above.
