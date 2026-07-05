---
published: false
---

# People Node Registry

This directory contains source-derived node records for DataTalks.Club podcast
guests and contributors. The collection is not published as local public pages;
public links should resolve to canonical `https://datatalks.club/people/<slug>.html`
URLs.

## Source Policy

Use these source rules for every people record:

- The source person record lives in `../datatalksclub.github.io/_people/<person_id>.md`.
- Podcast participation comes from `../datatalksclub.github.io/_podcast/<episode_slug>.md` frontmatter.
- Don't copy full transcripts into these records.
- Use podcast frontmatter and transcript snippets only for compact synthesis and
  source-grounded links.
- Public podcast links should use canonical DataTalks.Club episode pages, such
  as `https://datatalks.club/podcast/<episode_slug>.html`.

## Record Format

Each record uses this frontmatter:

```yaml
---
layout: person
title: "Full Name"
summary: "Full Name's DataTalks.Club person index record."
source_url: "https://datatalks.club/people/<slug>.html"
podcast_episodes: ["episode-slug"]
github: "optional"
twitter: "optional"
linkedin: "optional"
web: "optional"
---
```

People records are primarily about podcast content, not biographies. Include just
enough background to explain why the guest's claims matter. Then focus on what
they argued, explained, contrasted, or demonstrated in the podcast source files.

Keep the body compact. These records exist so graph/search can connect guests,
episodes, and wiki topics; durable public synthesis belongs in `_wiki/`.
