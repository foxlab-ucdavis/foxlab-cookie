.PHONY: install
install: ## Install the virtual environment and dependencies.
	@echo "📦 Creating virtual environment"
	@python3 -m venv .venv && \
	echo "Installing requirements.txt in .venv" && \
	. .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

.PHONY: update
update: ## Update the dependencies.
	@echo "📦 Updating dependencies"
	@. .venv/bin/activate && \
	pip install --upgrade pip && \
	echo "-e .[all] \n" > requirements.txt && \
	pip freeze >> requirements.txt
	@echo "Dependencies updated!"

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help