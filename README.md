# MCP: Model Context Protocol Repository

This repository contains implementations, integrations, and examples demonstrating the use of the Model Context Protocol (MCP) for building intelligent and modular AI applications.

## Overview

The repository is structured to facilitate easy understanding and usage of MCP with various toolkits, particularly emphasizing integration with Google's Agent Development Kit (ADK) and custom MCP servers.

## Repository Structure

```text
└── 📁MCP
    ├── 📁.vscode
    │   └── settings.json
    ├── 📁ADK
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── agent.py
    │   └── uv.lock
    ├── 📁Daily_Status_Update
    ├── 📁MCP_Server
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Clock Server)
    │   └── uv.lock
    ├── 📁mcp-server-black-formatter
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Black Formatter Server)
    │   └── uv.lock
    ├── 📁mcp-server-directry-management
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Directory Management Server)
    │   └── uv.lock
    └── 📁mcp-server-ruff
        ├── pyproject.toml
        ├── README.md
        ├── 📁src
        │   └── main.py (Ruff Server)
        └── uv.lock
```

## Available Projects

### 1. Agent Development Kit (ADK)
Contains the integration of agents utilizing Google's ADK to coordinate with MCP servers.

### 2. Directory Management Server (`mcp-server-directry-management`)
A Python-based FastMCP server offering comprehensive filesystem tools including directory listing, file read/write, file copying/moving, path metadata inspection, and search. Supports `health` checks.

### 3. Clock Server (`MCP_Server`)
A simple Python-based FastMCP server providing timezone-aware date and time capabilities. Supports `health` checks.

### 4. Black Formatter Server (`mcp-server-black-formatter`)
A Python-based FastMCP server providing a tool to format Python files using the Black code formatter. Supports `health` checks.

### 5. Ruff Server (`mcp-server-ruff`)
A Python-based FastMCP server providing high-performance code quality tools powered by Ruff. Supports `health` checks.
* `health`: Check server health status.
* `list_rules`: Lists all rules available in Ruff check.
* `lint_file`: Analyzes a file and reports style/syntax violations (over 900 built-in rules).
* `format_file`: Reformats a file to match PEP 8 guidelines.
* `auto_fix_file`: Automatically fixes safe linting and style issues in a file.
* `auto_fix_code`: Automatically fixes safe linting/style issues in python code passed directly.
* `modernize_syntax`: Upgrades older Python syntax to modern standards.

## Future Code Quality Servers (Roadmap)

Here is a checklist of ideas for future MCP servers to enhance code quality and developer workflows:

- [x] **`mcp-server-ruff`** (Linter, Formatter & Modernizer)
  - [x] `lint_file`: Analyzes a file and lists style/syntax violations (over 900 built-in rules).
  - [x] `format_file`: Formats code to match PEP 8 guidelines (drop-in Black replacement).
  - [x] `auto_fix_file`: Automatically fixes safe linting and style issues.
  - [x] `modernize_syntax`: Upgrades older Python code patterns to modern syntax (e.g. converting old string formatting to f-strings).
- [ ] **`mcp-server-pyright` / `mcp-server-mypy`** (Type Checker)
  - [ ] `check_types_in_file`: Verifies type annotations and safety on a file.
  - [ ] `check_types_in_project`: Analyzes the whole project for type errors.
- [ ] **`mcp-server-bandit`** (Security & Vulnerability Scanner)
  - [ ] `scan_vulnerabilities`: Identifies common security issues in Python code.
  - [ ] `check_dependencies`: Inspects `pyproject.toml` or `uv.lock` for known dependency vulnerabilities.
- [ ] **`mcp-server-radon`** (Code Complexity Analyzer)
  - [ ] `get_complexity_report`: Rates function and class complexity using Cyclomatic Complexity.
  - [ ] `get_maintainability_index`: Calculates the maintainability score of python files.
- [ ] **`mcp-server-pytest`** (Test Runner & Coverage)
  - [ ] `run_tests`: Runs unit tests for a directory or file.
  - [ ] `run_tests_with_coverage`: Runs tests and returns statement coverage statistics.
