---
title: "Analytics Engineering — Data Engineering Zoomcamp Module 4"
summary: "Module overview and materials for Analytics Engineering."
related_course:
  - dez-module-04
---

[Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) › [Module 4: Analytics Engineering](/course-wiki/dez-module-04/) › Analytics Engineering

## Notes

# Module 4: Analytics Engineering

Goal: Transforming the data loaded in DWH into Analytical Views developing a [dbt project](taxi_rides_ny/README.md).

### Prerequisites

The prerequisites depend on which setup path you choose:

**For Cloud Setup (BigQuery):**

- Completed [Module 3: Data Warehouse](../03-data-warehouse/) with:
  - A GCP project with BigQuery enabled
  - Service account with BigQuery permissions
  - NYC taxi data loaded into BigQuery (yellow and green taxi data for 2019-2020)

**For Local Setup (DuckDB):**

- No prerequisites! The local setup guide will walk you through downloading and loading the data.

> [!NOTE]
> This module focuses on **yellow and green taxi data** (2019-2020). While Module 3 may have included FHV data, it is not used in this dbt project.

## Setting up your environment

Choose your setup path:

### 🏠 [Local Setup](setup/local_setup.md)

- **Stack**: DuckDB + dbt Core
- **Cost**: Free
- [→ Get Started](setup/local_setup.md)

### ☁️ [Cloud Setup](setup/cloud_setup.md)

- **Stack**: BigQuery + dbt Cloud
- **Cost**: Free tier available (dbt Cloud Developer), BigQuery costs vary
- **Requires**: Completed Module 3 with BigQuery data
- [→ Get Started](setup/cloud_setup.md)

## Content

### Introduction to Analytics Engineering

[](https://www.youtube.com/watch?v=HxMIsPrIyGQ)

### Introduction to data modeling

[](https://www.youtube.com/watch?v=uF76d5EmdtU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=40)

### What is dbt?

[](https://www.youtube.com/watch?v=gsKuETFJr54&list=PLaNLNpjZpzwgneiI-Gl8df8GCsPYp_6Bs&index=5)

### Differences between dbt Core and dbt Cloud

[](https://www.youtube.com/watch?v=auzcdLRyEIk)

### Project Setup

| Alternative A  | Alternative B   |
|-----------------------------|--------------------------------|
| BigQuery + dbt Platform | DuckDB + dbt core |
| [](https://www.youtube.com/watch?v=GFbwlrt6f54) | [](https://www.youtube.com/watch?v=GoFAbJYfvlw) |

### dbt Course

| dbt Project Structure | dbt Sources | dbt Models | Seeds and Macros |
|-----------------------|-------------|------------|------------------|
| [](https://www.youtube.com/watch?v=2dYDS4OQbT0) | [](https://www.youtube.com/watch?v=7CrrXazV_8k) | [](https://www.youtube.com/watch?v=JQYz-8sl1aQ) | [](https://www.youtube.com/watch?v=lT4fmTDEqVk) |

| dbt Tests | Documentation | dbt Packages | dbt Commands |
|-----------|---------------|----------------------|---------------|
| [](https://www.youtube.com/watch?v=bvZ-rJm7uMU) | [](https:

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
