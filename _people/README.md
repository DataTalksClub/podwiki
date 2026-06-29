---
published: false
---

# People Exploration Pages

This directory contains LLM-curated exploration pages for DataTalks.Club podcast guests and contributors.

## Source Policy

- The source person record lives in `../datatalksclub.github.io/_people/<person_id>.md`.
- Podcast participation comes from `../datatalksclub.github.io/_podcast/<episode_slug>.md` frontmatter.
- Do not copy full transcripts into these pages.
- Use podcast frontmatter and transcript snippets only for compact synthesis and source-grounded links.
- Public podcast links should point to `https://datatalks.club/podcast.html`.

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

Body sections:

- `## Background`: short source-grounded bio.
- `## Podcast Contributions`: episode-level contribution summary with links to podcast summaries when useful and to the canonical DataTalks.Club podcast index for source episodes.
- `## Concepts Connected`: concept links using `/wiki/<slug>/` paths when the topic exists.
- `## Source Links`: local source person and podcast files for verification.

## Maintenance Notes

- Keep pages concise enough for agent lookup, but synthesize why the person matters across the archive.
- Prefer durable concepts over keyword stuffing.
- If a page becomes a major synthesis artifact, link it from the relevant topic or insight page in a separate wiki-maintenance pass.
