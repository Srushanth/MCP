# Makefile to orchestrate and run MCP servers

.PHONY: run-all run-bandit run-black-formatter run-directory-management run-pyright run-pytest run-radon run-ruff run-secret-scan setup

# Default target
run-all:
	python run_servers.py

setup:
	@echo "Creating virtual environments and syncing dependencies for all servers..."
	uv sync --project mcp-server-bandit
	uv sync --project mcp-server-black-formatter
	uv sync --project mcp-server-directry-management
	uv sync --project mcp-server-pyright
	uv sync --project mcp-server-pytest
	uv sync --project mcp-server-radon
	uv sync --project mcp-server-ruff
	uv sync --project mcp-server-secret-scan
	@echo "All environments initialized and synced successfully!"

run-bandit:
	uv run --project mcp-server-bandit mcp-server-bandit/src/main.py

run-black-formatter:
	uv run --project mcp-server-black-formatter mcp-server-black-formatter/src/main.py

run-directory-management:
	uv run --project mcp-server-directry-management mcp-server-directry-management/src/main.py

run-pyright:
	uv run --project mcp-server-pyright mcp-server-pyright/src/main.py

run-pytest:
	uv run --project mcp-server-pytest mcp-server-pytest/src/main.py

run-radon:
	uv run --project mcp-server-radon mcp-server-radon/src/main.py

run-ruff:
	uv run --project mcp-server-ruff mcp-server-ruff/src/main.py

run-secret-scan:
	uv run --project mcp-server-secret-scan mcp-server-secret-scan/src/main.py
