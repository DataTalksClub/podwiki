# Podwiki

An LLM-maintained exploration wiki for the DataTalks.Club podcast archive.

This project applies Andrej Karpathy's LLM wiki pattern to the podcast content in
`../datatalksclub.github.io/_podcast`: raw episode files stay in the website
repo, while this repo holds exploration pages that help agents and readers
understand, connect, and reuse the podcast archive. Public podcast links should
point to `https://datatalks.club/podcast.html`.

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
- `_podcast_summaries/` contains agent-friendly episode summaries that link back
  to the original podcast archive. Full transcripts stay in the website repo.
- `_people/` contains guest/contributor exploration pages.
- `_wiki/` contains comprehensive archive-derived wiki articles.
- `_articles/` contains keyword-driven SEO/editorial articles.
- `search/` contains the browser fallback corpus copied into the static site.
- `graph/graph.json` contains generated static graph data used by `/graph.html`.
- `artifacts/search/` contains build artifacts for the Zerosearch Lambda.
- `search_lambda/` contains the AWS Lambda handler for exploration-page search.
- `scripts/` contains deterministic helpers for search packaging and checking the
  static site.
- `AGENTS.md` tells Codex or another LLM agent how to maintain the wiki.

## Static Site

Build with Rustkyll:

```bash
make build
```

Serve locally:

```bash
make serve
```

The search page is available at `/search.html`. Set `search_api_url` in
`_config.yml` to the deployed Lambda Function URL to use server-side Zerosearch.
When `search_api_url` is empty, the page falls back to a simple client-side search
over `/search/search-corpus.json` for local development. Search indexes the
exploration collections, not full podcast transcripts.

The graph page is available at `/graph.html`. It visualizes topics, articles,
episode summaries, people, and source-episode relationships from
`graph/graph.json`. Clicking a node opens a side panel with canonical page links,
search links, related nodes, and a copyable graph URL such as
`/graph.html#topic%3Allms`.

Rebuild graph data after content changes:

```bash
make graph
```

Check generated internal links after a build:

```bash
python scripts/check_links.py
```

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
- `GET /?q=<query>&level=article`
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
2. Add or update a compact page in `_podcast_summaries/` if the episode should be
   discoverable here.
3. Link the new summary from relevant `_wiki/`, `_articles/`, and `_people/`
   pages when it adds evidence.
4. Run `make check` in this repo. This refreshes graph data, search corpus, the
   Lambda package, static HTML, and generated internal-link checks.
5. Push this repo to rebuild and deploy the search Lambda through GitHub Actions.

## Recommended Workflow

1. Ask the LLM to synthesize one wiki page at a time using existing exploration
   pages plus source transcript excerpts from `../datatalksclub.github.io`.
2. File durable public synthesis into `_wiki/<topic>.md`; use `_articles/` for
   keyword-driven editorial pages.
3. Add compact `_podcast_summaries/` and `_people/` pages as reusable agent
   context, not as podcast mirrors.
4. Periodically ask the LLM to lint for stale summaries, missing cross-links, weak
   taxonomy assignments, and orphan pages.
