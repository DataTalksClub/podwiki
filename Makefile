.PHONY: help graph index lambda-package build serve links clean check

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

graph: ## Build the static graph data used by the site
	python scripts/build_graph.py

index: graph ## Build the zerosearch artifact used by Lambda
	python scripts/build_search_index.py

lambda-package: index ## Prepare the minimal SAM CodeUri directory
	python scripts/prepare_lambda_package.py

build: graph ## Build the static site
	uvx rustkyll build

serve: graph ## Serve the static site locally
	uvx rustkyll serve --no-watch

links: build ## Check generated internal links
	python scripts/check_links.py

check: lambda-package links ## Build search index/package, static HTML, and link check

clean: ## Remove generated build artifacts
	rm -rf _site .rustkyll-manifest.json artifacts lambda_package
