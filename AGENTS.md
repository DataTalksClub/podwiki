# Podwiki Agent Instructions

You maintain a persistent LLM wiki for DataTalks.Club podcast knowledge.

## Core Principle

Treat `../datatalksclub.github.io/_podcast` as source truth. Do not modify those
files from this repo unless the user explicitly asks to prepare a website PR.

The wiki is a compounding artifact. When you answer a meaningful research question,
categorize an episode, or synthesize a theme, file the useful result back into
`_wiki/`, `_podcast_summaries/`, or `_people/` so future sessions do not
rediscover the same knowledge from scratch.

All topic content lives in the single `_wiki/` collection, typed by `tags:`
(comparison, guide, roadmap, transition, how-to; untagged = bare concept hub).
There are no `_guides/`, `_comparisons/`, `_roadmaps/`, or `_how_tos/`
collections and no redirect pages. See `CONTENT_GUIDE.md` for the tag model, the
no-redirects rule, and the deduplication/link-check maintenance process.

## Layers

- `sources/`: documentation about raw sources and source paths.
- `CONTENT_TODO.md`: durable backlog for content families such as roles,
  transitions, portfolio projects, roadmaps, and X vs Y pages.
- `_podcast_summaries/`: compact episode summaries for agents. Do not copy full
  transcripts here; link to the original source episode.
- `_people/`: guest/contributor exploration pages.
- `_wiki/`: the single content collection — human/LLM-authored archive-derived
  pages, typed by `tags:` (comparison, guide, roadmap, transition, how-to;
  untagged = concept hub). Do not overwrite with generated stubs.
- `search/` and `artifacts/search/`: generated exploration-page search corpora
  and packed Zerosearch artifacts.
- `graph/graph.json`: generated podcast graph data for the static visualization.
  Do not hand-edit it; run `python scripts/build_graph.py` or `make graph`.

## Page Ownership

Do not create public full episode, topic, guest, or transcript-copy pages in this
repo. The canonical podcast archive is `https://datatalks.club/podcast.html`, with
source files in `../datatalksclub.github.io/_podcast`.

Every public page must be grounded, linked, and focused:

- Grounded: every substantive section cites actual podcast discussions. Do not
  add generic advice unless a podcast discussion or an existing podcast-grounded
  page supports it.
- Linked: make the page link-heavy. Add visible links to related wiki pages,
  people pages, local podcast pages, and grounding evidence in the body, not
  only in generated graph data.
- Focused: center the page on one topic, role, transition, comparison, roadmap,
  or project type. Split mixed pages instead of padding them.

Use inline references in the relevant section, like Wikipedia citations. Do not
publish separate `Archive Evidence`, `Guest Descriptions`, `Maintenance Notes`,
`Episode Evidence`, `Recurring Archive Themes`, `Contents`, or `Search Intent`
sections in reader-facing pages.

When the source episode is known, link public content pages to the local
podcast page: `{{ '/podcasts/<source-file-slug>/' | relative_url }}`. That
local page links to the original
`https://datatalks.club/podcast/<source-file-slug>.html` episode. Use
`https://datatalks.club/podcast.html` only as a temporary fallback when the
specific episode slug is unknown.

People pages should be mostly about the person's podcast contributions: what
they argued, explained, contrasted, or demonstrated in the archive. Keep a short
bio only when it helps interpret the content.

Curated pages should omit `generated: true`. Do not overwrite curated synthesis
casually. If source evidence changes, update the relevant exploration page with a
compact note and links back to the source podcast repo.

Stub wiki pages are allowed when a topic link already exists and the full
writeup is not ready. Mark them with `stub: true`, link them to an existing hub,
and replace them with podcast-backed synthesis when the topic becomes important.

## Ingest Workflow

1. Read `CONTENT_GUIDE.md`.
2. For broad topic work, read `sources/podcast-topic-inventory.md` after running
   `make sources`.
3. Inspect existing pages in `_wiki/`, `_podcast_summaries/`, and `_people/`.
4. Open raw source episode files in `../datatalksclub.github.io/_podcast` only
   when you need evidence, clips, guests, or transcript context.
5. Update the target exploration page with synthesized takeaways, not just lists
   of links.
6. Add cross-links to related wiki pages, category pages, people pages, local
   podcast pages, and grounding evidence.
7. Add podcast evidence links in the body. Use local
   `/podcasts/<source-file-slug>/` links when the source episode is known.
8. For source-derived podcast and people pages, run `make sources`.
9. For graph/search changes, run `make graph` and
   `python scripts/build_search_index.py`, or simply run `make check`.

For broad podcast-topic work, first extract all episodes, all people, compact
chapter summaries, and topic candidates with `make sources`. Read
`sources/podcast-archive-summary.md` or `.tmp/podcast-archive-summary.md` before
opening full source episodes. Then keep five subagents running on
non-overlapping episode batches. Subagents should produce grounded topic reports
with local podcast links and guest links before writing wiki or editorial pages.

## Insight Hub Target

Insight pages should follow the shape requested in DataTalksClub issue #111:

- title and 1-2 paragraph introduction
- H2/H3 subtopic sections
- brief synthesized takeaways based on transcript evidence
- relevant podcast cards or episode links
- related topics section

Prefer evidence-backed synthesis over generic advice. If the source transcripts do
not support a claim, mark it as a hypothesis or leave it out. Keep guest names,
podcast links, and evidence inside the relevant topic sections instead of adding
visible meta sections such as contents, guest experts, archive evidence, or
maintenance notes.

## Wiki vs Editorial Content

Use `CONTENT_GUIDE.md`.

Wiki pages are comprehensive reference pages based on the full podcast archive.
They should include evidence links, timestamped examples, tradeoffs, and related
wiki pages. Podcast summaries are a separate agent index and should stay compact.

Editorial pages are SEO-informed pages created only after the user supplies
target keywords. They live in `_wiki/` with a type `tag:` (guide, comparison,
roadmap, transition, or how-to) and are served under `/wiki/<slug>/` like every
other page. Bare concepts are untagged wiki pages.

## Taxonomy Guidelines

Use existing `_wiki/` pages as the current working vocabulary. When you find a
recurring theme that does not fit, add it deliberately:

- define the major topic
- add at least three subtopics
- list example episodes or clips
- note the change in `wiki/log.md`

Avoid topic proliferation. Merge near-duplicates such as `LLM`, `LLMs`, and
`large language models` unless the distinction matters for the user.

## Query Workflow

When answering a user question about podcast content:

1. Search `_wiki/`, `_podcast_summaries/`, and `_people/` with `rg`.
2. Read the most relevant exploration pages.
3. Open raw episode files for direct transcript verification when quoting or making
   fine-grained claims.
4. Answer with source links to local files and timestamps where possible.
5. If the answer creates reusable synthesis, ask whether to file it, or file it
   directly when the user asked for wiki maintenance.

## Static Site and Search

Use `make check` before finishing structural changes. It builds the exploration
search index/package and the Rustkyll site.

The public search UI lives at `search.md` and `assets/search.js`. It calls
`site.search_api_url` when configured. Keep the browser fallback working for
local development, but treat the Lambda-backed Zerosearch path as the production
search implementation. Search indexes exploration pages only, not full podcast
transcripts.

The graph UI lives at `graph.md` and `assets/graph.js`. It should remain static:
use `graph/graph.json`, avoid external runtime dependencies, and keep node links
stable through graph URL hashes. `graph/graph.json` is generated from collection
frontmatter and internal links by `scripts/build_graph.py`; do not maintain it
as separate editorial content. Run `make sources` to sync source-derived
podcast and people pages before graph generation. The source documents are
`_wiki/`, `_people/`, and `_podcast_summaries/`. Episode nodes
should link to local podcast pages, which then link to the original
DataTalks.Club podcast pages. The graph may still treat tagged wiki pages
internally as article/content nodes; that is an implementation detail.

Run `python scripts/check_links.py` after a static build to validate generated
internal links. GitHub Pages runs the same checker with the deployed base path.

## Lint Workflow

Periodically check for:

- wiki pages with too many episode mentions and no synthesis
- episodes with missing or overly broad topics
- orphan editorial/wiki pages with no incoming links
- stale claims contradicted by newer episodes
- guest pages with no useful topic links
- high-value transcript clips that should become hub examples

Record durable fixes directly in the relevant collection page.
