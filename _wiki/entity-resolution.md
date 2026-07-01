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

Entity resolution is the work of deciding whether different records refer to
the same real-world thing. The thing may be a customer, supplier, product, or
patient. It may also be a donor, account, address, or location. In
DataTalks.Club discussions, the topic sits between
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) and [data
products]({{ '/wiki/data-products/' | relative_url }}). It also connects to
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) and [data
governance]({{ '/wiki/data-governance/' | relative_url }}).

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) gives the clearest
definition in
[Building an Open-Source Identity Resolution Tool]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
At [5:47]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she defines identity resolution as deciding whether several warehouse records
refer to the same real-world customer. At
[7:20]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she broadens that into entity resolution. The same idea can apply to employees
and addresses. It can also apply to locations, events, products, and suppliers.

Teams often meet the practical problem after they centralize data. Once the
warehouse, lake, or lakehouse contains records from online stores and offline
channels, ordinary joins often stop being enough. Surveys and ticketing systems
add more variations. Sales tools, procurement tools, and billing systems add
their own versions too. That's why entity resolution connects
to the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[customer data platforms]({{ '/wiki/customer-data-platforms/' | relative_url }}),
and [data engineering tools]({{ '/wiki/data-engineering-tools/' | relative_url }}).

## Common Definition

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) uses a direct
definition in the identity-resolution episode. Teams link records that refer to
the same real-world entity, then decide how the business should consume that
linked view.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) separates the
technical linking problem from the downstream action. At
[8:02]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}) in the
[identity-resolution episode]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she says duplicate detection is part of the work, but deduplication is only one
way to consume the result. A team may merge or purge duplicate records. It may
also keep the linked records because a customer 360 or supplier 360 needs the
full history.

She places record linkage and entity matching near the same problem family. She
also includes entity disambiguation. At
[13:38]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she describes those terms as flavors of the same broader task. Customer systems
often say identity resolution. Classic data integration often says record
linkage, while NLP-adjacent work may say entity disambiguation.

## Guest Disagreements

Guests usually agree on the goal, but they draw the boundary in different
places.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) uses identity
resolution when the entity is a person or customer. She uses the same label for
a citizen or healthcare provider. Entity resolution is the broader class of
things a company must reconcile
([7:20]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

The same episode approaches that class of problems through duplicate detection
in classifieds. Around
[9:08]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
the example asks whether two listings are duplicates. Sonal responds at
[11:09]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
by moving from classifieds to customer data and products. She also names
patients, donors, and suppliers.

Guests and episode threads also differ on where the capability should live. In
the [data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) frames
[customer data platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
as bundled systems for tracking and segmenting customer data.
Those systems can also activate customer data.
[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) says at
[24:32]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
that CDPs and master data management systems can contain some identity-resolution
capability. A dedicated tool can go deeper on
large-scale matching, probabilistic models, and non-customer entities.

The matching method has the same split. At
[41:29]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
and [44:48]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}) in the
[Zingg episode]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal says deterministic joins work when trusted identifiers are consistently
populated. When real-world records vary across sources, teams need fuzzier
matching methods and a way to control scale.

## Entity And Identity Resolution

Identity resolution is the customer- or person-centered version of entity
resolution. Sonal's first example is a customer who appears five times in a
warehouse because records arrived from offline channels and online stores.
Surveys, ticketing systems, and other interactions add more versions
([5:47]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).
If the company counts those rows as five customers, it distorts lifetime value
and personalization. It can also distort anti-money-laundering and
know-your-customer workflows.

Entity resolution generalizes the same question beyond people. At
[7:20]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
and [11:09]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) first names suppliers
and vendors. She then adds products and B2B accounts. Locations, patients,
donors, and healthcare providers appear in the same discussion.

Those examples matter because they turn the topic from a marketing-data problem
into a broader [data product]({{ '/wiki/data-products/' | relative_url }})
problem. A trusted supplier view, product catalog, or donor-recipient graph can
be as important as a trusted customer profile.

That distinction also explains why deduplication is too narrow. Deduplication
may create one clean row, while entity resolution may preserve multiple rows
and add a resolved identity or cluster. Downstream systems can then keep
context.
At [8:02]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal uses customer 360 and supplier 360 as examples where the linked records
complete the story instead of disappearing into one canonical record.

## Matching, Blocking, and Scale

Entity resolution becomes expensive when the system doesn't know which records
to compare. [Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) describes
the scaling problem at
[14:35]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}):
an all-pairs comparison grows too fast. A few million records can become
impractical. Useful tools avoid all-pairs comparison without missing likely
matches.

Zingg combines model training with blocking and distributed execution. At
[18:35]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal explains that users label selected pairs as matches or non-matches. The
tool then refines the model and runs it at larger scale. At
[14:35]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she says the model learns how to create comparison buckets. The system then
compares plausible candidates instead of every record against every other record.

This is where entity resolution differs from a fuzzy join in an ETL tool. At
[41:29]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal says exact joins are fine when the identifier is trusted and consistent.
But teams still need to decide thresholds and candidate generation when
identifiers vary across systems. They also need to handle transitive matches and
scale.

Names, addresses, emails, and KYC fields can all vary. At
[49:39]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal also describes the output as a graph of records that belong together.
Teams can consume that output as a table or graph.

## Modern Data Stack Fit

Entity resolution often appears after teams have already solved ingestion and
storage. At 4:51 in the
[identity-resolution episode]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal says modern data stack practices make extraction and transformation more
standard. They also make warehouses and lakes more standard places to load
data. Once data arrives in one place, teams start asking whether the people and
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
the tools teams already use. At
[18:35]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
and [20:46]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal describes Zingg using Spark distribution and building a Snowflake-native
implementation. She also describes a Python interface plus integrations with
Databricks notebooks and dbt. Those choices put entity resolution inside
existing data pipelines rather than beside them as a separate manual cleanup
project. That makes it a practical fit for
[how to build data pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }})
when identity work becomes part of production pipeline design.

## Open Source and Product Strategy

Sonal's episode also treats entity resolution as a product and
[open-source]({{ '/wiki/open-source/' | relative_url }}) strategy. Zingg came
from repeated consulting problems, then took about 18 months to reach a public
release
([23:00]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).
The open-source choice was partly personal, but it was also a distribution
decision.

At [24:32]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal says CDPs and master data management systems can be expensive and can
include weaker forms of identity resolution. Open source made it possible for
more companies to try a dedicated tool. At
[25:25]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
and [31:10]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she also says open source helped Zingg discover more use cases than direct sales
alone would have found.

Around [27:00-31:10]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal explains why Zingg used AGPL. Companies can use it internally or build
solutions around it, but a provider can't simply repackage it as a closed SaaS
without satisfying the license. That connects entity-resolution tooling to the
broader [open-source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and [startups]({{ '/wiki/startups/' | relative_url }}) discussions.

Code and community affect whether teams adopt a technical tool as a product.
Integrations, license, and market validation matter too.

## Customer, Supplier, Fraud, and Public-Data Use Cases

Customer and supplier 360 are the simplest use cases. At
[5:47]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
and [8:02]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal uses customer records, lifetime value, and personalization to explain why
a company needs to know which records belong together. She also names customer
360 and supplier 360. The same logic applies when procurement and sales systems
describe the same external party in different ways. Support, billing, and
marketing systems can add more versions
([39:11]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})).

Fraud and compliance are higher-stakes versions of the same problem. At
[46:08]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal explains that people can create multiple accounts with slightly different
names and addresses. They may also use different KYC identifiers. If the system
treats them as separate people, teams misread the flow of money.

Fraud and AML systems get a clearer graph to analyze when the identity layer
resolves those accounts. This connects entity resolution to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
because mistakes can affect investigations, compliance work, and customer
actions.

The fraud discussion also shows why graph outputs matter. At
[49:39]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
Sonal says Zingg does pairwise matching, then uses graph algorithms to find the
network of records that belong together. Fraud systems can lay transaction data
over that resolved identity graph and run downstream processing.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }})'s public-data example
shows the non-enterprise side. At
[52:23]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}),
she describes North Carolina campaign donor and recipient data where donors and
recipients appeared in different forms across historical and online records.
Once the project resolved those entities, voters and analysts could more easily
analyze spending and affiliations. The same mechanism that supports customer
analytics can support public-interest data when the entities are donors or
recipients rather than customers or orders.

## Related Pages

These pages cover the stack, product, and governance topics around entity
resolution.

- [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Open Source]({{ '/wiki/open-source/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Startups]({{ '/wiki/startups/' | relative_url }})
- [How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }})
- [Data Observability for Data Engineering]({{ '/guides/data-observability-for-data-engineering/' | relative_url }})
