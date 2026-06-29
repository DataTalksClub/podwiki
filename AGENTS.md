# Podwiki Agent Instructions

You maintain a persistent LLM wiki for DataTalks.Club podcast knowledge.

## Core Principle

Treat `../datatalksclub.github.io/_podcast` as source truth. Do not modify those
files from this repo unless the user explicitly asks to prepare a website PR.

The wiki is a compounding artifact. When you answer a meaningful research question,
categorize an episode, or synthesize a theme, file the useful result back into
`_wiki/`, `_articles/`, `_podcast_summaries/`, or `_people/` so future sessions do
not rediscover the same knowledge from scratch.

## Layers

- `sources/`: documentation about raw sources and source paths.
- `_podcast_summaries/`: compact episode summaries for agents. Do not copy full
  transcripts here; link to the original source episode.
- `_people/`: guest/contributor exploration pages.
- `_wiki/`: human/LLM-authored archive-derived wiki pages. Do not overwrite
  with generated stubs.
- `_articles/`: keyword-driven editorial articles. Do not create these until
  the user provides target keywords.
- `search/` and `artifacts/search/`: generated exploration-page search corpora
  and packed Zerosearch artifacts.
- `graph/graph.json`: generated podcast graph data for the static visualization.

## Page Ownership

Do not create public full episode, topic, guest, or transcript-copy pages in this
repo. The canonical podcast archive is `https://datatalks.club/podcast.html`, with
source files in `../datatalksclub.github.io/_podcast`.

Curated pages should omit `generated: true`. Do not overwrite curated synthesis
casually. If source evidence changes, update the relevant exploration page with a
compact note and links back to the source podcast repo.

## Ingest Workflow

1. Read `CONTENT_GUIDE.md`.
2. Inspect existing pages in `_wiki/`, `_articles/`, `_podcast_summaries/`, and
   `_people/`.
3. Open raw source episode files in `../datatalksclub.github.io/_podcast` only
   when you need evidence, clips, guests, or transcript context.
4. Update the target exploration page with synthesized takeaways, not just lists
   of links.
5. Add cross-links to related wiki pages, articles, people, and podcast summaries.
6. For search changes, run `python scripts/build_search_index.py`.

## Insight Hub Target

Insight pages should follow the shape requested in DataTalksClub issue #111:

- title and 1-2 paragraph introduction
- table of contents
- H2/H3 subtopic sections
- brief synthesized takeaways based on transcript evidence
- relevant podcast cards or episode links
- guest experts section
- related topics section

Prefer evidence-backed synthesis over generic advice. If the source transcripts do
not support a claim, mark it as a hypothesis or leave it out.

## Wiki vs Articles

Use `CONTENT_GUIDE.md`.

Wiki pages are comprehensive reference pages based on the full podcast archive.
They should include evidence links, timestamped examples, tradeoffs, and related
wiki pages. Podcast summaries are a separate agent index and should stay compact.

Articles are SEO pages created only after the user supplies target keywords.
They should link back to wiki pages but are not the same deliverable.

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

1. Search `_wiki/`, `_articles/`, `_podcast_summaries/`, and `_people/` with `rg`.
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
stable through graph URL hashes. Episode nodes should link to local podcast
summaries when available and otherwise to `https://datatalks.club/podcast.html`.

## Lint Workflow

Periodically check for:

- wiki pages with too many episode mentions and no synthesis
- episodes with missing or overly broad topics
- orphan articles/wiki pages with no incoming links
- stale claims contradicted by newer episodes
- guest pages with no useful topic links
- high-value transcript clips that should become hub examples

Record durable fixes directly in the relevant collection page.
