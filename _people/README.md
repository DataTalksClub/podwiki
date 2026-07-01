---
published: false
---

# People Exploration Pages

This directory contains LLM-curated exploration pages for DataTalks.Club podcast
guests and contributors.

## Source Policy

- The source person record lives in `../datatalksclub.github.io/_people/<person_id>.md`.
- Podcast participation comes from `../datatalksclub.github.io/_podcast/<episode_slug>.md` frontmatter.
- Do not copy full transcripts into these pages.
- Use podcast frontmatter and transcript snippets only for compact synthesis and source-grounded links.
- Public podcast links should point to local podcast pages, such as
  `{{ '/podcasts/<episode_slug>/' | relative_url }}`. Local podcast pages link
  to the original DataTalks.Club episode.

## Page Format

Each page uses this frontmatter:

```yaml
---
layout: person
title: "Full Name"
source_person: "../datatalksclub.github.io/_people/<id>.md"
person_id: id
summary: "one sentence"
expertise: ["concept name"]
podcast_episodes: ["episode-slug"]
---
```

People pages are primarily about podcast content, not biographies. Include just
enough background to explain why the guest's claims matter, then focus on what
they argued, explained, contrasted, or demonstrated in the archive.

Use these body sections:

- `## Podcast Context`: short bio/context tied to the podcast appearance.
- `## Podcast Contributions`: episode-level contribution summary with links to
  local podcast summary pages when useful.
- `## Reusable Claims and Examples`: claims, distinctions, examples, or
  decision rules future agents can reuse.
- `## Concepts Connected`: concept links using `/wiki/<slug>/` paths when the
  topic exists.
- `## Source Links`: local source person and podcast files for verification.

## Maintenance Notes

- Keep pages concise enough for agent lookup, but synthesize why the person's
  podcast contribution matters across the archive.
- Prefer durable concepts over keyword stuffing.
- If a page becomes a major synthesis artifact, link it from the relevant topic or insight page in a separate wiki-maintenance pass.
