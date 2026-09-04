---
published: false
---

# Events Node Registry

This directory contains source-derived node records for DataTalks.Club
webinars, workshops, and conferences. The collection is not published as local
public pages; event links resolve to the recording (`source_url`, usually the
YouTube watch URL) or the registration page. Podcast-type event rows are not
duplicated here — they are covered by the podcast archive registry in
`_podcast_summaries/`.

## Source Policy

- The source of truth is `../datatalksclub.github.io/_data/events.yaml`.
- Regenerate records with `python scripts/sync_event_pages.py` (run by
  `make sources`). Do not hand-edit generated fields.
- Record filenames are `<date>-<title-slug>.md`; the graph node id is
  `event:<filename-slug>`. The YouTube `video_id` frontmatter maps recording
  links and `[[event:<video-id>=>Label]]` chips back to the node.
- Do not copy full transcripts into these records. Concept extraction results
  go into `topics:` (wiki page titles or slugs) and a compact `summary`.
- Once a record has podcast/workshop-grounded notes, set
  `summary_status: done`; sync preserves `summary` and `topics` for those
  records.

## Record Format

```yaml
---
layout: event
title: "Event Title"
event_type: workshop
date: 2026-09-08 17:00:00
speakers: ["person-slug"]
summary: "Workshop, on 2026-09-08, with Speaker Name."
source_url: "https://www.youtube.com/watch?v=<video-id>"
video_id: "<video-id>"
registration_url: "https://luma.com/..."
recording_status: recorded
topics: ["wiki topic title"]
summary_status: pending
---
```
