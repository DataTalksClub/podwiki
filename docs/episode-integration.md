# Episode Integration Process

This process turns one canonical podcast episode into grounded improvements to
the public wiki. It uses only Podwiki, its sibling podcast source directory, and
the search index already shipped by this repository.

The process has three durable outcomes:

- source-derived metadata stays in `_podcast_summaries/`;
- useful synthesis is integrated into `_wiki/`;
- a reviewed episode that warrants no public change is recorded in
  `sources/episode-integration-decisions.json`.

Temporary decomposition and planning notes belong in
`.tmp/episode-integration/`. They are working material, not reader-facing pages.

## 1. Sync and identify the queue

Start from the canonical source files and refresh the local source and search
layers:

```bash
make sources
make index
make episode-status
```

`make episode-status` classifies each source episode:

- `needs_sync`: the canonical source exists but its local summary is missing;
- `needs_review`: the summary exists, but no wiki page cites the episode and no
  no-change decision has been recorded;
- `integrated`: at least one `_wiki/` page cites or links the canonical episode;
- `reviewed_no_change`: the episode was reviewed and deliberately produced no
  wiki edit.

The report also lists stale local summaries whose canonical source slug no
longer exists. Use `ARGS` to narrow the report, for example:

```bash
make episode-status ARGS="--season 24"
make episode-status ARGS="--status needs_review --limit 10"
```

This status is a triage signal. A citation proves that an episode has entered
the wiki, but it does not prove that every valuable statement has been mined.
Older integrated episodes can still be revisited for a focused topic pass.

## 2. Prepare one episode

Create a temporary worksheet:

```bash
make episode-plan EPISODE=s24e04-from-genai-pilots-to-production
```

The worksheet contains the source location, canonical URL, chapter navigation,
and search-ranked matches from existing wiki pages, wiki sections, and related
episode summaries. It is written to
`.tmp/episode-integration/<episode-slug>.md`.

The same production search index can be queried directly during review:

```bash
make search QUERY="LLM production guardrails" ARGS="--document-type section"
make search QUERY="RAG fine-tuning" ARGS="--level podcast_summary"
```

Search is candidate generation, not an editorial decision. Open the strongest
matching pages and confirm that their scope actually fits the evidence.

## 3. Decompose the transcript

Read the relevant transcript ranges in the canonical source file. Convert only
useful material into atomic evidence blocks in the worksheet. Each block must
contain one statement and preserve:

- a stable local evidence ID;
- statement kind: factual claim, definition, opinion, recommendation,
  experience/example, tradeoff, prediction, or open question;
- speaker and timestamp;
- a faithful paraphrase or short supporting excerpt;
- whether the wording is source evidence or an agent inference;
- confidence, ambiguity, or contradiction;
- concepts and entities needed for search;
- candidate target page and proposed integration action.

A guest's factual-sounding statement remains a claim attributed to that guest
unless it is independently supported. Do not turn opinions, predictions, or
agent synthesis into unattributed facts while editing wiki prose.

Do not decompose every transcript line. Keep material that adds at least one of
the following: a definition, mechanism, decision criterion, tradeoff, failure
mode, concrete example, disagreement, or useful connection between concepts.

## 4. Resolve concepts against the wiki

For every retained evidence block, search the concept and its likely synonyms.
Inspect page and section results, then assign one action:

- `support_existing`: add evidence for an existing explanation;
- `extend_existing`: add a missing distinction, mechanism, tradeoff, or example;
- `revise_conflict`: qualify existing prose when newer evidence disagrees;
- `cross_link`: connect two existing pages without adding a new substantive claim;
- `create_page`: create a focused concept page after passing the new-page gate;
- `no_change`: the wiki already covers the point or the evidence is too weak.

Related episode-summary results are useful for finding corroboration and older
views. Open the canonical source transcript when exact wording, context, or a
disagreement matters.

## 5. Integrate as synthesis

Group compatible evidence into the relevant section of an existing `_wiki/`
page. Rewrite it as coherent reference prose rather than appending isolated
facts or episode-by-episode notes.

Place citations after complete sentences:

```markdown
Production guardrails need multiple defensive layers because a single prompt
filter does not cover every attack path. [[cite:s24e04-from-genai-pilots-to-production=>From GenAI Pilots to Production]]
```

Use timestamped citations when an exact clip materially helps verification.
Add natural links to related wiki concepts and the canonical episode. Do not add
public evidence inventories, transcript copies, or maintenance sections.

## 6. Apply the new-page gate

Create a new `_wiki/` page only when all of these are true:

- search found no page with the same practical scope;
- the concept matters beyond this single episode;
- the page can support at least three meaningful subtopics;
- podcast evidence can ground the substantive sections;
- the page can link to an existing hub and related pages;
- the taxonomy name avoids near-duplicate terms.

If the concept changes the working taxonomy, add it deliberately and record the
change in `docs/taxonomy-log.md`. Otherwise extend the nearest existing page.

## 7. Close the review

When the episode changed the wiki, its canonical citation or link makes the
status report classify it as `integrated`.

When a complete review warrants no wiki change, add a decision like this:

```json
{
  "schema_version": 1,
  "episodes": {
    "episode-slug": {
      "status": "reviewed_no_change",
      "reviewed": "2026-08-03",
      "reason": "Existing pages already cover the useful claims with stronger evidence."
    }
  }
}
```

Keep the reason specific enough that a later reviewer can decide whether newer
wiki content or a new research question justifies reopening the episode.

## 8. Validate and commit

Validate the editorial change and generated site layers:

```bash
make wiki-links
make check
make episode-status ARGS="--season 24"
```

Commit coherent milestones separately: source sync, wiki synthesis, and
generated graph/search artifacts. This keeps source-derived churn separate from
editorial decisions and makes individual episode integrations reviewable.
