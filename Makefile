RUSTKYLL_PYPI_VERSION ?= 0.5.0
RUSTKYLL ?= uvx --no-config --from rustkyll==$(RUSTKYLL_PYPI_VERSION) rustkyll
STEMMER ?= porter
GRAPH_MIN_INBOUND ?= 6
GRAPH_MAINTENANCE_MIN_INBOUND ?= 16
BASEURL ?=

.PHONY: help sources graph graph-audit graph-maintenance-audit graph-explorer-check index lambda-package build serve links wiki-links chip-syntax podcast-summary-audit episode-status episode-plan search duplicates content-audit keyword-gap keyword-artifacts clean check ci-site ci-lambda-package

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

sources: ## Sync source-derived registries and archive indexes for graph/search
	python scripts/sync_podcast_pages.py
	python scripts/sync_people_pages.py
	python scripts/sync_book_pages.py
	python scripts/rewrite_to_canonical.py
	python scripts/stamp_wiki_dates.py
	python scripts/extract_podcast_sources.py
	python scripts/build_podcast_archive_summary.py
	python scripts/check_source_records.py

graph: sources ## Build the static graph data used by the site
	python scripts/build_graph.py

graph-audit: ## Enforce the minimum inbound-link graph gate
	python scripts/audit_graph.py --min-inbound $(GRAPH_MIN_INBOUND) --fail

graph-maintenance-audit: ## Optional non-failing report for graph enrichment ideas
	python scripts/audit_graph.py --min-inbound $(GRAPH_MAINTENANCE_MIN_INBOUND)

graph-explorer-check: ## Check landing/full graph parity and navigation contracts
	python scripts/check_graph_explorer.py

index: graph ## Build the zerosearch artifact used by Lambda
	python scripts/build_search_index.py --stemmer $(STEMMER)

lambda-package: index ## Prepare the minimal SAM CodeUri directory
	python scripts/prepare_lambda_package.py

build: ## Build the static site (uses committed graph/search data; run 'make graph' after source/content changes)
	$(RUSTKYLL) build $(if $(BASEURL),--baseurl "$(BASEURL)")
	@if [ -n "$(BASEURL)" ]; then \
		python scripts/fix_absolute_urls.py --baseurl "$(BASEURL)"; \
	fi
	python scripts/prune_sitemap.py $(if $(BASEURL),--baseurl "$(BASEURL)")

serve: ## Serve the static site locally (uses committed graph/search data; run 'make graph' after source/content changes)
	$(RUSTKYLL) serve --no-watch

wiki-links: ## Fast source-level wiki link check (no build)
	python scripts/check_wiki_links.py

chip-syntax: ## Check touched Markdown files for legacy pipe chip aliases (PATHS="file1 file2")
	@if [ -z "$(PATHS)" ]; then \
		echo 'usage: make chip-syntax PATHS="_wiki/example.md ..."'; \
		exit 2; \
	fi
	python scripts/check_chip_syntax.py $(PATHS)

podcast-summary-audit: ## Check source-derived podcast summaries for agent usability
	python scripts/audit_podcast_summaries.py

episode-status: ## List source episodes that still need sync or wiki review
	python scripts/episode_integration_status.py $(ARGS)

episode-plan: ## Prepare a source/search worksheet (EPISODE=<slug>)
	@test -n "$(EPISODE)" || (echo 'usage: make episode-plan EPISODE=<slug>'; exit 2)
	python scripts/prepare_episode_integration.py "$(EPISODE)" $(ARGS)

search: ## Query the local Podwiki search index (QUERY="terms")
	@test -n "$(QUERY)" || (echo 'usage: make search QUERY="terms"'; exit 2)
	python scripts/search_podwiki.py "$(QUERY)" $(ARGS)

duplicates: ## Report highest-signal near-duplicates and main-site cannibalization
	python scripts/find_duplicates.py --top-k 3 --limit 25

links: build ## Check generated internal links
	python scripts/check_html_chips.py
	python scripts/check_links.py $(if $(BASEURL),--baseurl "$(BASEURL)")

content-audit: ## Report wiki/article pages that need citation and link cleanup
	python scripts/audit_content_quality.py --strict-scaffold-headings --strict-source-scaffolding

seo-audit: ## Report on-page SEO issues (title/description length, duplicate H1)
	python scripts/audit_seo.py

check: graph-explorer-check lambda-package graph-audit podcast-summary-audit content-audit seo-audit links ## Build search index/package, static HTML, graph audit, and link check

ci-site: content-audit seo-audit ## CI build/check path for GitHub Pages (expects checked-in source-derived records)
	python scripts/check_source_records.py
	python scripts/build_graph.py
	python scripts/audit_graph.py --min-inbound $(GRAPH_MIN_INBOUND) --fail
	python scripts/build_search_index.py --stemmer $(STEMMER)
	$(RUSTKYLL) build $(if $(BASEURL),--baseurl "$(BASEURL)")
	@if [ -n "$(BASEURL)" ]; then \
		python scripts/fix_absolute_urls.py --baseurl "$(BASEURL)"; \
	fi
	python scripts/prune_sitemap.py $(if $(BASEURL),--baseurl "$(BASEURL)")
	python scripts/check_html_chips.py
	python scripts/check_links.py $(if $(BASEURL),--baseurl "$(BASEURL)")

ci-lambda-package: ## CI build path for Lambda search package
	python scripts/check_source_records.py
	python scripts/build_search_index.py --stemmer $(STEMMER)
	python scripts/prepare_lambda_package.py

clean: ## Remove generated build artifacts
	rm -rf _site .rustkyll-manifest.json artifacts lambda_package

keyword-gap: ## Cluster an Ubersuggest CSV and find groundable, non-overlapping gaps
	python scripts/keyword_gap.py $(CSV)

keyword-artifacts: ## Refresh machine-readable keyword and suggestion artifacts
	python scripts/build_keyword_artifacts.py
