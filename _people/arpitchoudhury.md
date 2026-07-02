---
layout: "person"
title: "Arpit Choudhury"
summary: "Arpit Choudhury's DataTalks.Club podcast discussions, organized for topic exploration."
source_url: "https://datatalks.club/people/arpitchoudhury.html"
podcast_episodes: ["data-led-growth-event-tracking-and-reverse-etl"]
curated: "true"
twitter: "icanautomate"
linkedin: "icanautomate"
web: "https://dataled.academy/"
expertise: ["data-led growth", "event tracking", "tracking plans", "reverse ETL", "product analytics", "data activation"]
---

## Background

Arpit Choudhury is the founder of Data-led Academy. In his DataTalks.Club
conversation, he describes the academy as a place where product and growth
people can learn how to work with data. The audience also includes operations
and marketing teams that don't have a deep engineering background.

Before Data-led Academy, Arpit worked on integrations for SMBs. He joined
Integromat early to build its community and later led growth there. That
background shapes his view of data work. For him, data is useful only when
teams know where it came from and can question its accuracy. They also need to
use it in the tools where they make customer decisions
([data-led growth episode](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Data-Led Growth

Arpit distinguishes data-led work from simply following dashboards. A
data-led professional understands the source and structure of the data. They
question its accuracy and combine the evidence with experience instead of
treating data as an automatic instruction. In growth work, that matters because
teams can't personalize acquisition, activation, or retention paths if product
behavior is trapped in a warehouse or dashboard
([10:45-13:34](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

That framing connects growth work to
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}) and
[experimentation]({{ '/wiki/experimentation/' | relative_url }}). Arpit's
examples include A/B tests and lifecycle email. He also discusses SMS
campaigns, in-app experiences, and personalized onboarding. The shared
requirement is access to trusted product data inside the tools used by
marketing and growth teams, as well as product and operations teams. SQL
workflows alone aren't enough
([7:21-9:46](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Tracking Plans And Product Events

Arpit treats the tracking plan as the starting point for useful event data. A
tracking plan should name each event, describe its properties, and record data
types. It should also record whether the event is client-side or server-side.

He uses the sign-up event to show why this matters. A client-side click can
fire before the account exists. A server-side event can represent the completed
signup
([13:34-28:52](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

His practical advice is to avoid tracking everything at the beginning. For a
SaaS product, he recommends starting with the events needed to understand the
customer journey from acquisition to activation. Examples include email
verified, project created, and user invited. He also mentions task created,
client added, and invoice created. The event list should be small enough for
engineers to implement, test, and own
([23:27-27:00](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

Arpit also links documentation to data quality. If teams don't document event
meaning, ownership, and capture logic, new analysts or growth people can't tell
whether a spike is real. They also need consistent casing.

The spike might come from duplicate, malformed, or fake events. He mentions
spreadsheets and Miro for this work. He also names purpose-built
[tools]({{ '/wiki/tools/' | relative_url }}) such as AVO, Iteratively, and
TrackPlan for collaborative tracking plans
([16:01-22:50](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Collection To Activation

Arpit's growth stack follows a sequence. Teams collect product events, store
them, analyze them, and activate them. Product analytics tools such as Mixpanel
or Amplitude can make funnels easier than BI for event data. He still argues
that teams should store raw event data in a warehouse so they can reuse it
later. That puts product analytics beside warehouse modeling,
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
and downstream activation
([28:52-37:25](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

Activation is the step Arpit emphasizes most. Teams should act on data, not
only look at it. Product events can help support teams understand what a user
already tried.

Sales teams can prioritize active accounts, and marketing or engagement tools
can avoid irrelevant messages. In his examples, the same product data can drive
support context and CRM prioritization. It can also drive lifecycle emails,
in-app onboarding, and product personalization
([30:03-33:41](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Reverse ETL And Tool Choices

Arpit places [reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) inside a
warehouse-centered growth stack. Once a team has clean warehouse data, reverse
ETL or operational analytics tools can move selected customer and account data
into business tools. Arpit names sales and marketing systems plus advertising,
support, and product analytics tools. He also names Census, Hightouch, and
Grouparoo in this category
([37:25](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

He contrasts that path with customer data platforms. They can bundle
collection, segmentation, and audience creation for marketers and growth teams.
They also support activation, but Arpit's selection advice is still
conservative.

Teams should list the questions they need to answer. Then they should work
backward to the needed data flow. From there, they can decide whether to buy a
tool, use an open-source option, or build a smaller internal solution. Cost and
maintenance matter, along with security, compliance, and the team's ability to
operate the tool
([38:20-46:13](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

## Self-Service And Data Products

Arpit's version of data democratization isn't just broad access to dashboards.
He argues that teams need data literacy and documentation, plus self-service
tools that let them answer questions without overwhelming data teams. That
requires clean data and documented sources. Business teams also need enough
training to use product analytics tools, BI tools, or simple SQL responsibly
([46:13-53:33](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).

This makes his discussion relevant to
[data products]({{ '/wiki/data-products/' | relative_url }}) because the useful
output isn't only a dataset or dashboard. It's a reliable data-backed workflow
that customer-facing and product teams can use. He also connects data-led work
to product-led growth. A product-led company needs data for activation events,
personalized onboarding, and messages that don't ask people to do things they
already did
([52:07-56:08](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html)).
