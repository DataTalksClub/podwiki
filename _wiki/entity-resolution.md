---
layout: wiki
title: "Entity Resolution"
summary: "How DataTalks.Club podcast discussions explain entity resolution, identity resolution, matching, record linkage, and the data product tradeoffs behind trusted customer, supplier, fraud, and public-data views."
related:
  - Customer Data Platforms
  - Data Products
  - Modern Data Stack
  - Data Engineering Tools
  - Data Quality and Observability
  - Data Governance
  - Open Source
  - Startups
---

Entity resolution decides whether different records refer to the same
real-world thing. The thing may be a customer, supplier, product, or patient.
It may also be a donor, account, address, or location.

In DataTalks.Club
podcast discussions, entity resolution sits between [data
engineering]({{ '/wiki/data-engineering/' | relative_url }}) and [data
products]({{ '/wiki/data-products/' | relative_url }}). It also touches
[[machine learning]] and [data
governance]({{ '/wiki/data-governance/' | relative_url }}). The warehouse may
hold the records, but a business still has to decide which rows describe the
same outside reality.

Identity resolution decides whether several warehouse records refer to the same
real-world customer. When teams broaden that into entity resolution, the same
matching problem applies to employees, addresses, and locations
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

It can also apply to products or events. The same logic covers suppliers,
healthcare providers, patients, and donors.

Teams often meet the practical problem after they centralize data. Once the
warehouse, lake, or lakehouse contains records from online stores and offline
channels, ordinary joins often stop being enough. Surveys and ticketing systems
add more variations. Sales tools, procurement tools, and billing systems add
their own versions too. Entity resolution therefore belongs with the [modern
data stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[[customer data platforms]],
and [[data engineering tools]].

## Terminology and Boundaries

Teams link records that refer to the same real-world entity. They then decide
how the business should consume that linked view
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

The technical linking problem is separate from the downstream action. Duplicate
detection is part of the work, but deduplication is only one way to consume the
result. A team may merge or purge duplicate records. It may also keep the linked
records because a customer 360 or supplier 360 needs the full history
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

The broader task includes record linkage, entity matching, and entity
disambiguation. Customer systems often say identity resolution. Classic data
integration often says record linkage, and NLP-adjacent work may say entity
disambiguation
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

The boundary with [customer data
platforms]({{ '/wiki/customer-data-platforms/' | relative_url }}) is practical
rather than absolute. CDPs bundle customer tracking, segmentation, and
activation
([[cite:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth]]).
CDPs and master data management systems may include identity-resolution
features. A dedicated entity-resolution tool can go deeper on large-scale
matching, probabilistic models, and non-customer entities
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

## Entity and Identity Resolution

Identity resolution is the customer- or person-centered version of entity
resolution. A customer may appear five times in a warehouse because records
arrived from offline channels and online stores. Surveys, ticketing systems, and
other interactions add more versions
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
If the company counts those rows as five customers, it distorts lifetime value
and personalization. It can also distort anti-money-laundering and
know-your-customer workflows.

Beyond people, entity resolution applies to suppliers and vendors, products and
B2B accounts. Locations, patients, donors, and healthcare providers fit the same
frame
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

Those examples matter because they turn the topic from a marketing-data problem
into a broader [[data-products|data product]]
problem. A trusted supplier view, product catalog, or donor-recipient graph can
be as important as a trusted customer profile.

Deduplication is too narrow when it creates one clean row. Entity resolution may
preserve multiple rows and add a resolved identity or cluster. Downstream
systems can then keep context instead of flattening it away. In customer 360 and
supplier 360, linked records complete the story instead of disappearing into one
canonical record
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

## Matching, Blocking, and Scale

Entity resolution becomes expensive when the system doesn't know which records
to compare. An all-pairs comparison grows too fast. A few million records can
become impractical, so useful tools avoid all-pairs comparison without missing
likely matches
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

Zingg combines model training with blocking and distributed execution. After
users label selected pairs as matches or non-matches, the tool refines the model
and runs it at larger scale. The model learns how to create comparison buckets.
The system then compares plausible candidates instead of every record against
every other record
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

This is where entity resolution differs from a fuzzy join in an ETL tool. Exact
joins are fine when the identifier is trusted and consistent. When identifiers
vary across systems, teams still need to decide thresholds and candidate
generation. They also need to handle transitive matches and scale
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

When fields such as names, addresses, emails and KYC identifiers vary, teams get
a graph of records that belong together. They can consume that linked output as
a table or graph
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

## Modern Data Stack Fit

Entity resolution often appears after teams have already solved ingestion and
storage. Modern data stack practices make extraction and transformation more
standard. They also make warehouses and lakes more standard places to load data
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
Once data arrives in one place, teams start asking whether the people and
products inside that data are real duplicates. They ask the same question about
suppliers and accounts.

This places entity resolution downstream of many [data engineering
tools]({{ '/wiki/data-engineering-tools/' | relative_url }}) and upstream of
many decisions. A resolved identity may feed [data
activation]({{ '/wiki/data-activation/' | relative_url }}), product analytics,
support workflows, and sales routing. It may also feed fraud checks,
compliance analysis, or ML features. It isn't only a cleanup task because the
linked entity can become an
operational data product.

The integration surface matters because entity resolution has to run inside
the tools teams already use. Zingg uses Spark distribution and a Snowflake-native
implementation, plus a Python interface and integrations with Databricks
notebooks and dbt
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
Those choices put entity resolution inside existing data pipelines rather than
beside them as a separate manual cleanup project. That makes it a practical fit
for [[how to build data pipelines]]
when identity work becomes part of production pipeline design.

## Open Source Product Strategy

Entity resolution is also a product and
[[open-source=>open-source]] strategy. Zingg came
from repeated consulting problems, then took about 18 months to reach a public
release
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
The open-source choice was partly personal, but it was also a distribution
decision.

CDPs and master data management systems can be expensive and can include weaker
forms of identity resolution. Open source made it possible for more companies
to try a dedicated tool. Open source also helped Zingg discover more use cases
than direct sales alone would have found
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

Zingg used AGPL, under which companies can use it internally or build solutions
around it.
A provider can't simply repackage it as a closed SaaS without satisfying the
license
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
Entity-resolution tooling therefore belongs in
broader [[open-source-portfolio-evidence|open-source portfolio evidence]]
and [[startups]] discussions.

Code and community affect whether teams adopt a technical tool as a product.
Integrations, license, and market validation matter too.

## Customer, Supplier, Fraud, and Public-Data Use Cases

Customer and supplier 360 are the simplest use cases. Customer records, lifetime
value, and personalization explain why a company needs to know which records
belong together. The same logic applies when procurement and sales systems
describe the same external party in different ways. Support, billing, and
marketing systems add more versions
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

Fraud and compliance are higher-stakes versions of the same problem. People can
create multiple accounts with slightly different names and addresses, and use
different KYC identifiers. If the system treats them as separate people, teams
misread the flow of money
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

Fraud and AML systems get a clearer graph to analyze when the identity layer
resolves those accounts. The topic overlaps with [data quality and
observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
because matching errors can affect investigations, compliance work, and
customer actions.

Graph outputs also matter here. Zingg does pairwise matching, then uses graph
algorithms to find the network of records that belong together. Fraud systems
can lay transaction data over that resolved identity graph for downstream
analysis
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).

A public-data example shows the non-enterprise side. The North Carolina campaign
data included donor and recipient records in different forms across historical
and online records
([[podcast:building-open-source-data-product-for-identity-resolution|Building an Open-Source Identity Resolution Tool]]).
Once the project resolved those entities, voters and analysts could more easily
analyze spending and affiliations. The same mechanism that supports customer
analytics can support public-interest data when the entities are donors or
recipients rather than customers or orders.

Sabina Firtala's domestic risk-assessment project adds a higher-stakes public
and social-service example. The project drew on case-management data plus
public records and surveys. Those sources had to be cleaned and linked before
the team could engineer features for a risk score
([[cite:building-domestic-risk-assessment-tool|Building a Domestic Risk Assessment Tool]]).

In that setting, entity resolution isn't just a matching convenience. Linkage
choices and unresolved uncertainty affect which people, events, services, and
risk signals appear connected. Privacy, governance, and bias checks have to
come before scoring or decision support.

## Related Topics

These pages cover the adjacent stack, governance, and product questions.

- [[Customer Data Platforms]] covers the customer-profile and activation layer that often uses identity resolution.
- [[Data Products]] covers the broader way of turning a trusted entity view into reusable business data.
- [[Modern Data Stack]] and [[Data Engineering Tools]] cover the warehouses, pipelines, and integrations that entity-resolution tools plug into.
- [[Data Quality and Observability]] covers reliability questions around identity errors, while [[Data Governance]] covers ownership.
- [[Open Source]], [[Open Source Portfolio Evidence]], and [[Startups]] cover the product and distribution side of Zingg's open-source route.
- [[How to Build Data Pipelines]] and [[Data Observability for Data Engineering]] cover adjacent implementation and reliability work.
