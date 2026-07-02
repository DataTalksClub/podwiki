.PHONY: help sources graph index lambda-package build serve links wiki-links duplicates content-audit keyword-gap clean check

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

sources: ## Sync source-derived podcast and people pages for graph/search
	python scripts/sync_podcast_pages.py
	python scripts/sync_people_pages.py
	python scripts/sync_book_pages.py
	python scripts/extract_podcast_sources.py
	python scripts/build_podcast_archive_summary.py

graph: sources ## Build the static graph data used by the site
	python scripts/build_graph.py

index: graph ## Build the zerosearch artifact used by Lambda
	python scripts/build_search_index.py

lambda-package: index ## Prepare the minimal SAM CodeUri directory
	python scripts/prepare_lambda_package.py

build: graph ## Build the static site
	uvx rustkyll build

serve: graph ## Serve the static site locally
	uvx rustkyll serve --no-watch

wiki-links: ## Fast source-level wiki link check (no build)
	python scripts/check_wiki_links.py

duplicates: ## Report near-duplicate wiki pages and main-site cannibalization
	python scripts/find_duplicates.py

links: build ## Check generated internal links
	python scripts/check_links.py

content-audit: ## Report wiki/article pages that need citation and link cleanup
	python scripts/audit_content_quality.py

check: lambda-package links ## Build search index/package, static HTML, and link check

clean: ## Remove generated build artifacts
	rm -rf _site .rustkyll-manifest.json artifacts lambda_package

keyword-gap: ## Cluster an Ubersuggest CSV and find groundable, non-overlapping gaps
	python scripts/keyword_gap.py $(CSV)
