---
title: "Analytics Engineering — Data Engineering Zoomcamp Module 4"
summary: "Module overview and materials for Analytics Engineering."
related_course:
  - dez-module-04
---

[Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) › [Module 4: Analytics Engineering](/course-wiki/dez-module-04/) › Analytics Engineering

## Notes

# Module 4: Analytics Engineering

Goal: Transforming the data loaded in DWH into Analytical Views developing a dbt project.

### Prerequisites

The prerequisites depend on which setup path you choose:

**For Cloud Setup (BigQuery):**

- Completed Module 3: Data Warehouse with:
  - A GCP project with BigQuery enabled
  - Service account with BigQuery permissions
  - NYC taxi data loaded into BigQuery (yellow and green taxi data for 2019-2020)

**For Local Setup (DuckDB):**

- No prerequisites! The local setup guide will walk you through downloading and loading the data.

> [!NOTE]
> This module focuses on **yellow and green taxi data** (2019-2020). While Module 3 may have included FHV data, it is not used in this dbt project.

## Setting up your environment

Choose your setup path:

### 🏠 Local Setup

- **Stack**: DuckDB + dbt Core
- **Cost**: Free
- → Get Started

### ☁️ Cloud Setup

- **Stack**: BigQuery + dbt Cloud
- **Cost**: Free tier available (dbt Cloud Developer), BigQuery costs vary
- **Requires**: Completed Module 3 with BigQuery data
- → Get Started

## Content

### Introduction to Analytics Engineering

### Introduction to data modeling

### What is dbt?

### Differences between dbt Core and dbt Cloud

### Project Setup

| Alternative A  | Alternative B   |
|-----------------------------|--------------------------------|
| BigQuery + dbt Platform | DuckDB + dbt core |
|  |  |

### dbt Course

| dbt Project Structure | dbt Sources | dbt Models | Seeds and Macros |
|-----------------------|-------------|------------|------------------|
|  |  |  |  |

| dbt Tests | Documentation | dbt Packages | dbt Commands |
|-----------|---------------|----------------------|---------------|
|  |  |  |  |

## Troubleshooting

- DuckDB Troubleshooting Guide — If you're getting OOM errors during `dbt build` with DuckDB

## Extra resources

> [!NOTE]
> If you find the videos above overwhelming, we recommend completing the [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) course and then rewatching the module. It provides a solid foundation for all the key concepts you need in this module.

## SQL refresher

The homework for this module focuses heavily on window functions and CTEs. If you need a refresher on these topics, you can refer to these notes.

* SQL refresher

## Homework

* 2026 Homework

# Community notes

<details>
<summary>Did you take notes? You can share them here</summary>

* [Slides used in previous years](https://docs.google.co

## Key concepts

- [Analytics Engineering](/course-wiki/analytics-engineering/)

## Related notes

- [dez-m01-deployment-with-a-variables-file](/course-wiki/dez-m01-deployment-with-a-variables-file/)
- [dez-m01-introduction-terraform-concepts-and-overview-a-p](/course-wiki/dez-m01-introduction-terraform-concepts-and-overview-a-p/)
- [dez-m01-introduction-to-gcp-google-cloud-platform](/course-wiki/dez-m01-introduction-to-gcp-google-cloud-platform/)
- [dez-m01-sql-refresher](/course-wiki/dez-m01-sql-refresher/)
- [dez-m01-terraform-basics-simple-one-file-terraform-deplo](/course-wiki/dez-m01-terraform-basics-simple-one-file-terraform-deplo/)
- [dez-m01-workshop](/course-wiki/dez-m01-workshop/)

## Sources

- [Video](https://www.youtube.com/watch?v=HxMIsPrIyGQ)
- [Lesson file](https://github.com/data-engineering-zoomcamp/blob/main/04-analytics-engineering/README.md)
