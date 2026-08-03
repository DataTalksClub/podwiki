# Podwiki

An LLM-maintained exploration wiki for the DataTalks.Club podcast archive.

This project applies Andrej Karpathy's LLM wiki pattern to the podcast content in
`../datatalksclub.github.io/_podcast`: raw episode files stay in the website
repo, while this repo holds exploration pages that help agents and readers
understand, connect, and reuse the podcast archive. Public podcast links should
point to canonical `https://datatalks.club/podcast/<slug>.html` pages on the
main website.

## Why

The podcast archive already has episode pages, timestamped clips, topics, and
full transcripts. The missing layer is a persistent topic-oriented wiki:

- episode discovery by theme, not only by publication order
- insight hub drafts for topics like LLMs, MLOps, career transitions, and open source
- cross-links between episodes, guests, clips, and recurring ideas
- a workflow where LLM analysis is filed back into Markdown instead of disappearing
  into chat history

This maps directly to DataTalksClub issue #111: taxonomy, clip categorization, and
thematic "Insight Hub" pages.

## Layout

- `sources/` documents where raw source material lives. The raw Markdown files are
  not copied here.
- `CONTENT_TODO.md` keeps the durable backlog for roles, transitions, portfolio
  projects, roadmaps, and comparison pages.
- `_podcast_summaries/` contains source-derived agent records. Full transcripts
  and public podcast pages stay in the website repo.
- `_people/` contains source-derived person node records that resolve to the
  main website.
- `_wiki/` contains all public content. Some pages use `tags:` such as `guide`,
  `comparison`, `roadmap`, `transition`, or `how-to`.
- `search/` contains the browser fallback corpus copied into the static site.
- `graph/graph.json` contains generated static graph data used by `/graph/`.
- `artifacts/search/` contains build artifacts for the Zerosearch Lambda.
- `sources/podcast-archive-summary.md` contains the generated agent-first map
  of all synced episodes, people, chapter summaries, and topic candidates.
- `search_lambda/` contains the AWS Lambda handler for exploration-page search.
- `scripts/` contains deterministic helpers for search packaging and checking the
  static site.
- `AGENTS.md` tells Codex or another LLM agent how to maintain the wiki.

## Static Site

Build with Rustkyll:

```bash
make build
```

The Makefile runs Rustkyll through
`uvx --no-config --from rustkyll==0.5.0 rustkyll`. The GitHub Pages workflow uses
the same make target, so local and deployed builds use the same Rustkyll version.
The `--no-config` flag matters because a global uv `exclude-newer` setting can
hide fresh Rustkyll releases and silently run an older binary without WASM
extension support.

Serve locally:

```bash
make serve
```

The search page is available at `/search/`. Set `search_api_url` in
`_config.yml` to the deployed Lambda Function URL to use server-side Zerosearch.
When `search_api_url` is empty, the page falls back to a simple client-side search
over `/search/search-corpus.json` for local development. Search indexes the
exploration collections, not full podcast transcripts.

The graph page is available at `/graph/`. It visualizes topics, tagged wiki
pages, source-derived episode records, people, and source-episode relationships
from `graph/graph.json`. Clicking a node opens a side panel with canonical page
links, search links, related nodes, and a copyable graph URL such as
`/graph/#topic%3Allms`.

Rebuild graph data after content changes:

```bash
make graph
```

Check generated internal links after a build:

```bash
python scripts/check_links.py
```

The GitHub Pages workflow runs the same link check on each push to `main` with
the deployed `/podwiki` base URL.

## Search Lambda

Build the packed Zerosearch artifact:

```bash
make index
```

This creates `artifacts/search/search-index.zsx`. To prepare the minimal SAM
package directory, run:

```bash
make lambda-package
```

The Lambda in
`search_lambda/podwiki_search/handler.py` loads that file and exposes:

- `GET /health`
- `GET /?q=<query>`
- `GET /?q=<query>&level=wiki`
- `GET /?q=<query>&level=guide`
- `GET /?q=<query>&level=comparison`
- `GET /?q=<query>&level=roadmap`
- `GET /?q=<query>&level=how_to`
- `GET /?q=<query>&level=podcast_summary`
- `GET /?q=<query>&level=person`
- `GET /?q=<query>&level=section`

The SAM template is `template.yaml`. The GitHub Actions workflow in
`.github/workflows/deploy-search.yml` rebuilds the corpus and `.zsx` artifact,
then deploys on push to `main`. It expects these repository secrets:

- `AWS_DEPLOY_ROLE_ARN`
- `AWS_REGION`

Optional repository variable:

- `CORS_ORIGIN`

## Adding New Episodes

1. Add or update the source episode Markdown in
   `../datatalksclub.github.io/_podcast`.
2. Run `make sources` to regenerate `_podcast_summaries/`, `_people/`,
   `_books/`, `artifacts/podcast/source-index.json`, and
   `sources/podcast-archive-summary.md`.
3. Run `make index`, then `make episode-status` to find episodes that still need
   review. Prepare one with `make episode-plan EPISODE=<slug>`.
4. Decompose useful transcript material into atomic claims, concepts, opinions,
   recommendations, examples, and tradeoffs. Use the worksheet's Podwiki search
   matches to extend relevant `_wiki/` pages or create a focused page only when
   no suitable page exists.
5. Link the evidence in synthesized prose with canonical citation chips. If a
   complete review produces no useful wiki change, record `reviewed_no_change`
   with a reason in `sources/episode-integration-decisions.json`.
6. Run `make check` in this repo. This refreshes graph data, search corpus, the
   Lambda package, static HTML, and generated internal-link checks.
7. Push this repo to rebuild and deploy the search Lambda through GitHub Actions.

See `docs/episode-integration.md` for the complete evidence and page-creation
rules.

## Recommended Workflow

1. Ask the LLM to synthesize one wiki page at a time using existing exploration
   pages plus source transcript excerpts from `../datatalksclub.github.io`.
2. File durable public synthesis into `_wiki/<topic>.md`; use `tags:` for
   keyword-driven editorial pages.
3. Cross-link editorial pages to relevant wiki pages, canonical podcast episode
   URLs, and the podcast evidence that grounds each claim.
4. Refresh compact `_podcast_summaries/` and `_people/` records as reusable
   agent context, not as public mirrors.
5. Periodically ask the LLM to lint for stale summaries, missing cross-links, weak
   taxonomy assignments, and orphan pages.
