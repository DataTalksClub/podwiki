---
layout: wiki
title: "Data Engineering Tools"
summary: "A podcast-grounded map of data engineering tools across ingestion, storage, transformation, orchestration, quality, and platform operations."
related:
  - Data Engineering
  - Modern Data Stack
  - Data Engineering Platforms
  - DataOps
  - Tools
---

## Definition

Data engineering tools are the systems teams use to move, store, transform,
and schedule data. Teams also use them to test, observe, and publish data. In
the podcast archive, these tools matter because they make recurring data work
operable. They don't replace the design work around ownership, contracts,
naming, and recovery.

## Common Tool Groups

[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
frames the modern stack as a chain of ingestion, storage, transformation, and
orchestration choices. The episode connects Airbyte-style ingestion with
warehouse or lake storage. It also connects dbt-style transformations,
orchestration, and reverse data flows.

[Scale Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
adds the platform lesson because Mehdi OUAZZA discusses Airflow, conventions,
playbooks, and Kafka. He also discusses schemas and data contracts as platform
parts that many teams can use repeatedly.

## Guest Differences

Guests differ on how much platform a team needs. Early or small workflows can
start with simpler schedulers and managed services. Larger teams need shared
orchestration, deployment paths, observability, and reusable templates. Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
for platform design and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for
the operating practices behind the tools.

## Related Pages

These pages cover the adjacent tool and operating model topics:

- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Tools]({{ '/wiki/tools/' | relative_url }})
