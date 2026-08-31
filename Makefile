.PHONY: help stats audit reindex test serve validate format lint

PYTHON = python3
CLI = c64-kb-agent

help:
	@echo "C64-KB-Agent Development Makefile"
	@echo "=================================="
	@echo "  make stats     - Recalculate KB metrics and update METRICS.md"
	@echo "  make audit     - Run schema validation and engine linter audit"
	@echo "  make reindex   - Rebuild SQLite FTS5 search index"
	@echo "  make test      - Run full pytest test suite"
	@echo "  make serve     - Start REST API server on port 8000"
	@echo "  make validate  - Validate document and wiki schemas"
	@echo "  make format    - Run ruff code formatter"
	@echo "  make lint      - Run ruff and mypy linters"

stats:
	$(PYTHON) scripts/wiki_stats.py

audit: validate
	$(PYTHON) -m c64_kb_agent.engine.cli lint

reindex:
	$(CLI) rebuild-index

test:
	$(PYTHON) -m pytest

serve:
	$(CLI) serve --port 8000

validate:
	$(CLI) validate

format:
	ruff format .

lint:
	ruff check .
	mypy c64_kb_agent
