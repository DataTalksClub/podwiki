# Events Source

DataTalks.Club runs four recurring event formats: webinars (Tuesdays, technical,
with slides), live podcasts (Fridays; the recording becomes a podcast episode),
hands-on workshops, and conferences.

## Source of Truth

`../datatalksclub.github.io/_data/events.yaml` — one YAML row per event with
`time`, `title`, `speakers` (main-site person slugs), `type`
(podcast/webinar/workshop/conference), `link` (registration, usually Lu.ma),
and `youtube` (recording URL when it exists). The file is sorted newest first.

## What We Extract

`python scripts/sync_event_pages.py` (run by `make sources`) writes one node
record per **webinar, workshop, and conference** row into `_events/`.
Podcast-type rows are skipped: those recordings are published as podcast
episodes and are already covered by the `_podcast` archive and
`_podcast_summaries`.

Record facts:

- filename: `<YYYY-MM-DD>-<title-slug>.md`; graph node id `event:<filename-slug>`
- `source_url`: the YouTube recording, else the registration link, else
  `https://datatalks.club/events.html`
- `video_id`: the 11-character YouTube id, used by `[[event:<video-id>=>Label]]`
  chips (rendered to `https://youtu.be/<video-id>`, `?t=<seconds>s` when a time
  is present) and by `build_graph.py` to map recording URLs in any body back to
  the event node
- `speakers`: person slugs; every slug must exist in the people registry
  (event speakers are synced into `_people/` by `sync_people_pages.py`)
- `topics` + `summary`: filled by the concept-extraction pass from the recording
  transcript; `summary_status` flips from `pending` to `done` and sync preserves
  both fields afterwards. Sync also preserves non-empty `topics` on `pending`
  records, so title-derived topic edges on transcript-blocked recordings (set
  manually) survive re-syncs until a real transcript pass replaces them

The full fetched data snapshot used for the initial concept pass lives in
`.tmp/events/` (not committed).

## Recordings Missing from the Source File

Some past rows in `events.yaml` carry no `youtube` link even though the
recording exists on the DataTalks.Club channel. When a recording is found
elsewhere (channel playlists, web search, the events page), stamp its
`video_id`, `source_url`, and `recording_status: recorded` into the record;
sync preserves those fields for source rows without a youtube link, so they
are registry data the source file lacks. Upstream `events.yaml` PRs that add
the missing links are still welcome — the source file stays the long-term
source of truth.
