.PHONY: help index lambda-package build serve clean check

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

index: ## Build the zerosearch artifact used by Lambda
	python scripts/build_search_index.py

lambda-package: index ## Prepare the minimal SAM CodeUri directory
	python scripts/prepare_lambda_package.py

build: ## Build the static site
	uvx rustkyll build

serve: ## Serve the static site locally
	uvx rustkyll serve --no-watch

check: lambda-package build ## Build search index/package and static HTML

clean: ## Remove generated build artifacts
	rm -rf _site .rustkyll-manifest.json artifacts lambda_package
