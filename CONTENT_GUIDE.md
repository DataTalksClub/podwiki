# Content Guide

This project has several different content products.

## Page Quality Gate

Every public page must pass three checks before it is committed:

- Grounded: every substantive section must cite actual DataTalks.Club podcast
  discussions. Link evidence through the local `/podcasts/<slug>/` page when the
  source episode is known; that page links to the original DataTalks.Club
  episode.
- Linked: every page must visibly link to related wiki pages, people pages,
  local podcast pages, and podcast evidence. Tagged pages (guide, comparison,
  roadmap, transition, how-to) should use `related_wiki` frontmatter and body
  links; untagged concept pages should use `related` frontmatter and body links.
- Focused: every page centers one topic, role, transition, comparison, roadmap,
  or project type. Split mixed pages instead of writing a broad generic essay.

Do not publish maintenance notes, agent instructions, evidence appendixes, guest
description appendixes, or SEO scaffolding such as `Search Intent` sections.
Use inline references in the relevant section, like Wikipedia citations.
Avoid reader-facing scaffold phrases such as "the archive says" or
"podcast-grounded." Name the guest, episode, or podcast discussions that support
the claim instead.

When the source episode is known, public content pages should link to the local
podcast page: `{{ '/podcasts/<source-file-slug>/' | relative_url }}`. The local
podcast page links to the original
`https://datatalks.club/podcast/<source-file-slug>.html` episode. Use
`https://datatalks.club/podcast.html` only when the specific episode slug is not
known yet.

## Wiki Pages

Wiki pages live in `_wiki/` and are archive-derived reference pages. They should
answer: "What has the DataTalks.Club podcast collectively taught about this topic?"

Required structure:

1. Opening definition: 1-3 short paragraphs that define the topic and link to
   the most important related wiki pages.
2. Common definition: what the podcast archive converges on, with inline
   episode links.
3. Guest disagreements: boundary differences, tradeoffs, or places where guests
   focus on different parts of the topic, with
   inline episode links.
4. Topic sections: concrete subtopics with podcast references inside the
   section where the claim appears.
5. Related pages: a short final list when the body needs a navigational close.

Do not publish a separate link map or evidence appendix. Put links where they
help the claim: related wiki pages in definitions, people links where a guest's
argument appears, and local podcast links next to the discussion they support.
Do not use reader-facing headings with "Archive" in the name. Use
`Common Definition`, `Guest Disagreements`, and concrete topic headings instead.

Use these reader-facing headings where they fit:

```markdown
## Common Definition
## Guest Disagreements
## <Concrete Topic Section>
## Related Pages
```

Do not use these headings in public pages:

```markdown
## Contents
## Link Map
## Search Intent
## Archive Evidence
## Episode Evidence
## Guest Descriptions
## Recurring Archive Themes
## Maintenance Notes
## Agent Maintenance Notes
```

Wiki pages should not target arbitrary SEO keywords. They should be comprehensive
knowledge pages built from the podcast archive.

## Stub Pages

Stub wiki pages are allowed only when a topic link already exists and the page
prevents a broken reader path. Mark them with `stub: true` in frontmatter, link
to at least one existing hub page, and keep the body short. Replace the stub with
podcast-grounded synthesis when the topic becomes important enough to cover.

## Podcast Summaries

Podcast summaries live in `_podcast_summaries/`. They are not replacement podcast
pages and must not copy full transcripts. Their job is to help future agents decide
whether to open the original source episode in `../datatalksclub.github.io`.
They are also the internal citation targets for all wiki pages.

Required structure:

- why the episode matters
- chapter-level summary from clips or transcript sections
- key concepts
- useful-for / probably-skip-if guidance for agents
- source pointers back to `https://datatalks.club/podcast.html` and source files

Generate or refresh these local podcast pages with
`python scripts/sync_podcast_pages.py`. The source of truth is still
`../datatalksclub.github.io/_podcast`.

Before topic writeups, run `make sources`. This extracts podcast episodes,
people, chapter summaries, topic candidates, `artifacts/podcast/source-index.json`,
and `sources/podcast-archive-summary.md`. Agents should read the archive
summary and local `/podcasts/<slug>/` pages as their first pass before opening a
full episode transcript.

For large topic discovery work, keep five subagents running in parallel. Split
the source episodes into non-overlapping batches. Each subagent should return
candidate topics, local podcast links, guest links, and chapter evidence before
any wiki or editorial page is written.

## Graph Source

The graph is derived from Markdown documents, not maintained as editorial
content. All wiki pages (concept hubs and tagged guide/comparison/roadmap/
transition/how-to pages), people pages, and local podcast pages are the source.
`graph/graph.json` is generated by `python scripts/build_graph.py` and should not
be hand-edited. Run `make sources` before `make graph` when podcast or people
source files changed. The graph may model tagged wiki pages internally as
article/content nodes; that is an implementation detail.

## People Pages

People pages live in `_people/`. They collect guest/contributor information from
`../datatalksclub.github.io/_people` and podcast participation. They should link
people to wiki pages (concepts and tagged guide/comparison/roadmap/transition/
how-to pages) and local podcast summaries where relevant.
Use the original people profile for short background, but make the page mostly
about what the person argued, explained, contrasted, or demonstrated in podcast
discussions.

## One Collection, Typed by Tags

There is a single content collection: `_wiki/`, served at `/wiki/<slug>/`. There
are no separate `_guides/`, `_comparisons/`, `_roadmaps/`, or `_how_tos/`
collections and no `/guides/`, `/comparisons/`, `/roadmaps/`, or `/how-tos/`
URLs. Everything that used to live in those collections is now a wiki page with a
`tags:` entry that records its editorial type:

- `comparison` — X vs Y pages and role or architecture tradeoffs.
- `guide` — practical, keyword-driven synthesized pages.
- `roadmap` — learning paths and "how to get into" pages.
- `transition` — role-to-role career-change pages.
- `how-to` — procedural build, setup, or operations pages.

A bare concept page has no type tag — it is just a wiki topic hub. The wiki owns
the concept; a tagged page owns a question, comparison, path, or procedure about
it. For example, `A/B Testing` is the untagged concept page
`_wiki/a-b-testing.md`, while a `guide`-tagged product page links to it when it
uses experiments as evidence. An `X vs Y` page is a `comparison`-tagged wiki page
that links back to both underlying concept hubs.

Tagged pages use `layout: article` (which shows the type label and a related-wiki
panel) and derive their label from the tag; untagged concept pages use the
default `wiki` layout. The `/special-pages/` hub and its nav dropdown filter
`site.wiki` by tag, so a new tagged page appears there automatically.

Do not create `guide`/`comparison`/`roadmap`/`how-to` pages until a target
keyword list is provided. Required structure once keywords exist:

- exact target keyword in frontmatter
- one topic-centered opening that states what the page helps the reader do
- content outline matched to the keyword without a public `Search Intent` section
- podcast-backed examples and expert quotes or paraphrases
- visible links to relevant wiki pages, people pages, local podcast pages, and
  grounding evidence

Tagged pages still follow the wiki evidence rule: cite specific podcast
interviews inline when making claims.

## No Redirects

The site has no redirect pages. Do not add `layout: redirect` or `redirect_to:`
frontmatter, and do not keep stub pages that only forward to another URL. Every
page is a real page at its `/wiki/<slug>/` URL.

When you merge or rename a page, do not leave a redirect behind. Instead:

1. Pick the canonical target page.
2. Move any unique, podcast-grounded content into it.
3. Rewrite every incoming link to the canonical URL — both body `/wiki/<slug>/`
   links and `related` / `related_wiki` frontmatter titles (those are slugified
   to `/wiki/<title>/`, so the title must slugify to the target's filename).
4. Delete the old page.
5. Prove there are no dead links (see Maintenance below).

## Maintenance: Deduplication and SEO Focus

The goal is focused pages: one page per topic and search intent, so pages do not
cannibalize each other or the main DataTalks.Club site. Run these checks
periodically and after any merge, rename, or bulk content change.

Detect duplication with the local Zerosearch index (no Lambda, no network):

```
make duplicates        # python scripts/find_duplicates.py
```

- Internal report: near-duplicate wiki pages that compete for the same query.
  Highest-signal cues are near-identical slugs/titles and high content overlap.
  Merge true same-intent duplicates into one page and rewrite links (see No
  Redirects). Keep pages that share a topic but serve a different intent (a
  `roadmap` vs a `comparison` vs the concept hub) and cross-link them instead.
- Cross-site report: wiki pages that overlap articles in
  `../datatalksclub.github.io/_posts`. The main site owns its branded and
  article terms (course/zoomcamp names, "what is X" posts it already ranks for).
  Where a wiki page duplicates such an article, trim the generic overlap, keep
  only the podcast-archive synthesis that the article does not have, and link out
  to the main article rather than restating it. Do not modify the main-site repo
  from here; propose those changes as a separate website PR.

Prove there are no dead links after edits:

```
make wiki-links        # fast, source-level: scripts/check_wiki_links.py
make links             # authoritative: builds the site, then scripts/check_links.py
```

`make wiki-links` validates every `/wiki/` body link and `related`/`related_wiki`
title against real pages without a build. `make links` builds the static site and
checks all rendered links (nav, generated people/podcast pages, anchors). Run
`make wiki-links` before committing and `make links` before finishing structural
changes. Rebuild search after content changes: `python scripts/build_search_index.py`.

## Evidence Rules

- Every content section should include actual podcast references when it makes a
  claim about the topic.
- Prefer transcript clips and timestamped episode links over generic claims.
- Do not cite a guest as supporting a claim unless the transcript evidence is
  present in the episode page.
- If pages disagree, preserve the disagreement instead of smoothing it away.
- Avoid shallow topic labels. A page must explain the actual mechanism,
  workflow, tradeoff, or pattern discussed in the archive.
