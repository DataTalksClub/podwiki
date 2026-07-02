# Podcast/Book Mining — shared agent instructions

You mine ideas from DataTalks.Club podcast episodes / books and map them to the
podwiki so we can enrich the knowledge graph and fill real content gaps —
**without re-creating duplication or main-site cannibalization.** READ-ONLY:
your only writes are your one report file. No edits to repo files, no git, no
builds (one optional `python scripts/find_duplicates.py` is allowed).

First read `/home/alexey/git/podwiki/AGENTS.md` and `CONTENT_GUIDE.md`.

## Sources per item
- **Podcast** `<slug>`: read `_podcast_summaries/<slug>.md` (compact summary);
  dip into raw transcript `../datatalksclub.github.io/_podcast/<slug>.md` only
  for specific evidence/timestamps.
- **Book** `<slug>`: read `_books/<slug>.md`; dip into raw
  `../datatalksclub.github.io/_books/<slug>.md` (author Q&A archive) for
  specific author claims.

## Per item, do this
1. Extract **8-15 concrete ideas/concepts** the item actually discusses — real
   topics, arguments, tradeoffs, techniques, or role/career points. Not generic
   buzzwords.
2. For each idea, find existing wiki coverage: `grep -ril "<term>" _wiki` and
   grep the search corpus `search/search-corpus.json`. Identify the page(s) that
   already cover it.
3. Classify each idea into ONE action (prefer the first two; NEW PAGE is rare):
   - **CONNECTION** — a graph edge to add: this item should be cited on wiki page
     X, or page X and page Y should link. Give source → target + one-line reason.
   - **ENRICH** — wiki page X should incorporate this specific evidence
     (guest/author, ~timestamp or Q&A, the claim). Give page + the evidence.
   - **NEW PAGE** (rare) — a genuine gap: NOT covered by any existing wiki page
     AND NOT a query a main-site datatalks.club article owns. Give title + angle
     + why it's a real gap. If unsure, mark **BORDERLINE** and explain — do not
     assert a new page you can't justify.

## Guardrails (these matter — we just removed dozens of duplicate/cannibalizing pages)
- Default to CONNECTION/ENRICH. A NEW PAGE must survive: "is this already a wiki
  page?" and "does a main-site blog article own this query?" If either is yes →
  it's an ENRICH/CONNECTION on the existing page, not a new page.
- Everything stays grounded in the actual episode/book. No invented advice.
- Prefer connecting to existing hubs over inventing near-duplicate topics
  (e.g. don't propose "LLM eval" if `llm-evaluation-workflows` exists — connect).

## Output
Write ONE markdown file (path given in your launch prompt). For each item:
a heading with the slug, then a compact table:
`idea | coverage found (page or "none") | action (CONNECTION/ENRICH/NEW PAGE/BORDERLINE) | target page | specifics`.
End with a 2-line tally: counts of CONNECTION / ENRICH / NEW PAGE / BORDERLINE.

Return a short summary: item count, total ideas, action tally, and the 3-5
highest-value connections or gaps you found.
