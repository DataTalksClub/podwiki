---
name: podcast-episode-integration
description: Mine public DataTalks.Club podcast episodes into grounded Podwiki synthesis, mapping concepts to existing pages or justified tagged guides/how-tos with canonical citations and source validation. Use only in this repository; ignore underscore-prefixed source drafts.
---

# Podcast Episode Integration

Use this skill when a new or previously unmined DataTalks.Club episode should
be turned into reusable Podwiki knowledge. The detailed local playbooks are the
canonical procedure—read them before editing:

- `AGENTS.md` for repository ownership and source boundaries.
- `CONTENT_GUIDE.md` for page shape, tags, links, and
  citation prose.
- `docs/episode-integration.md` for the
  end-to-end episode workflow and action vocabulary.
- `docs/mining/methodology.md` for batch
  mining reports and the duplicate/cannibalization guardrails.

## Source and queue

The sibling `../datatalksclub.github.io/_podcast/` directory is source truth and
is read-only from this repository. Only public episode files are eligible:
ignore `README.md`, templates, and every source filename beginning with `_`.
Never create a summary, person appearance, citation, graph node, or search entry
for an excluded source file.

Refresh the local source layers before triage:

```bash
make sources
make index
make episode-status
```

Read `sources/podcast-archive-summary.md`, then inspect the relevant
`_podcast_summaries/<slug>.md`. For transcript-level evidence, open the matching
public source file only when exact wording, a timestamp, or a disagreement
matters. `make episode-plan EPISODE=<slug>` prepares the worksheet and ranked
matches against existing pages.

## Mine and map concepts

Keep atomic evidence blocks: one claim, definition, mechanism, tradeoff,
failure mode, example, prediction, or open question per block. Preserve speaker,
timestamp, statement kind, faithful paraphrase, confidence, and whether a
conclusion is source evidence or agent inference. Search both `_wiki/` and
`search/search-corpus.json`; search hits suggest candidates but do not decide
scope.

Assign each retained block one action:

- `support_existing` — add evidence to an existing explanation;
- `extend_existing` — add a missing distinction, mechanism, tradeoff, or example;
- `revise_conflict` — qualify prose when newer evidence disagrees;
- `cross_link` — connect existing pages without inventing a new claim;
- `create_page` — create a focused page only after the new-page gate;
- `no_change` — coverage is sufficient or evidence is too weak.

Prefer `support_existing`, `extend_existing`, and `cross_link`. Create a new
`_wiki/` page only when no page has the same practical scope, the concept matters
beyond one episode, at least three meaningful subtopics can be grounded, the
page can link to an existing hub, and no main-site DataTalks.Club article owns
the query. A procedural concept may be a how-to, but use the single `_wiki/`
collection with `tags: ["how-to"]`; do not create a separate `_how_tos/`
collection or a keyword-only page. Record deliberate taxonomy additions in
`docs/taxonomy-log.md`.

For a batch, follow the mining methodology: extract 8–15 concrete ideas per
item, write one report in `.tmp/episode-integration/`, and mark each idea
`CONNECTION`, `ENRICH`, `NEW PAGE`, or `BORDERLINE` before public edits. Keep
reports grounded in the actual episode and default uncertain gaps to
`BORDERLINE`, not a new page.

## Write grounded prose

Group compatible evidence into coherent reference prose instead of appending
episode recaps. Put a compact citation after the complete sentence:
`[[cite:<podcast-slug>=>Episode Label]]`. Use a timestamp only when it improves
verification: `[[cite:<podcast-slug>@MM:SS=>Episode Label]]`, with total minutes
and two-digit minutes. Link the canonical episode URL, related wiki concepts,
and an existing hub in the relevant section. Do not copy transcripts or add
visible evidence/maintenance sections.

When a person's name is retained because attribution adds value, use
`[[person:<slug>=>Full Name]]`, matching the canonical title in
`_people/<slug>.md`. `=>` is canonical; never use `|`. Keep punctuation outside
the chip, for example `[[person:<slug>=>Full Name]]'s`. If attribution is not
useful, omit the name and cite the episode instead. Do not expand people pages.

## Close and validate

If the episode changed a page, its canonical citation or link should make
`episode-status` report `integrated`. If review found no useful public change,
record a specific `reviewed_no_change` decision in
`sources/episode-integration-decisions.json`.

Run the relevant checks before handing off:

```bash
make wiki-links
make check
make episode-status ARGS="--status needs_review"
```

Regenerate graph/search through `make graph` and
`python scripts/build_search_index.py`; never hand-edit generated artifacts.
