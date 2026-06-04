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
    ├── 📁mcp-server-bandit
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Bandit Server)
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
    ├── 📁mcp-server-pyright
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Pyright Server)
    │   └── uv.lock
    ├── 📁mcp-server-pytest
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Pytest Server)
    │   └── uv.lock
    ├── 📁mcp-server-radon
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Radon Server)
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
- **Entry point**: [agent.py](file:///c:/GitHub/MCP/ADK/src/agent.py)

### 2. Directory Management Server (`mcp-server-directry-management`)
A Python-based FastMCP server offering comprehensive filesystem tools including directory listing, file read/write, file copying/moving, path metadata inspection, and search. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-directry-management/src/main.py)
- **Tools**:
  * `health`: Check Directory Management server health status.
  * `list_dir`: List all files and folders in a directory.
  * `list_files`: List all files matching specific extensions in a directory.
  * `list_folders`: List all sub-folders in a directory.
  * `read_file_contents`: Retrieve the text content of a file.
  * `write_file_contents`: Create or overwrite a file with specific contents.
  * `create_directory`: Create a new directory and any necessary parent directories.
  * `move_or_rename`: Move or rename files and folders.
  * `copy_file_or_folder`: Copy files or directories recursively.
  * `get_path_metadata`: Inspect detailed file/folder attributes (size, permissions, creation time).
  * `path_exists`: Verify if a file or directory exists.
  * `search_files`: Search for files matching patterns within a directory structure.

### 3. Bandit Server (`mcp-server-bandit`)
A Python-based FastMCP server providing security and vulnerability scanning for Python code and project dependencies. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-bandit/src/main.py)
- **Tools**:
  * `health`: Check Bandit server health status and version.
  * `scan_vulnerabilities_in_file`: Scan a single Python file for security vulnerabilities using Bandit.
  * `check_dependencies_vulnerabilities`: Check for security vulnerabilities in project dependencies using pip-audit.
  * `scan_vulnerabilities_in_project`: Scan a project directory recursively for security vulnerabilities using Bandit.
  * `scan_vulnerabilities_in_code`: Scan a raw Python code snippet for security vulnerabilities using Bandit.

### 4. Black Formatter Server (`mcp-server-black-formatter`)
A Python-based FastMCP server providing a tool to format Python files using the Black code formatter. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-black-formatter/src/main.py)
- **Tools**:
  * `health`: Check Black Formatter server health status.
  * `format_file`: Reformats a file to match PEP 8 guidelines.

### 5. Ruff Server (`mcp-server-ruff`)
A Python-based FastMCP server providing high-performance code quality tools powered by Ruff. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-ruff/src/main.py)
- **Tools**:
  * `health`: Check Ruff server health status.
  * `list_rules`: Lists all rules available in Ruff check.
  * `lint_file`: Analyzes a file and reports style/syntax violations (over 900 built-in rules).
  * `format_file`: Reformats a file to match PEP 8 guidelines.
  * `auto_fix_file`: Automatically fixes safe linting and style issues in a file.
  * `auto_fix_code`: Automatically fixes safe linting/style issues in python code passed directly.
  * `modernize_syntax`: Upgrades older Python syntax to modern standards.

### 6. Pyright Server (`mcp-server-pyright`)
A Python-based FastMCP server providing static type checking and type analysis powered by Pyright. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-pyright/src/main.py)
- **Tools**:
  * `health`: Check Pyright server health status and version.
  * `check_types_in_file`: Verifies type annotations and safety on a file.
  * `check_types_in_project`: Analyzes the whole project for type errors.
  * `create_type_stubs`: Generates type stub files (`.pyi`) for third-party libraries.
  * `verify_type_completeness`: Verifies the type completeness of a `py.typed` package.
  * `check_types_in_code`: Analyzes type errors in a raw Python code snippet.

### 7. Pytest Server (`mcp-server-pytest`)
A Python-based FastMCP server providing test runner capabilities and code coverage analysis. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-pytest/src/main.py)
- **Tools**:
  * `health`: Check Pytest server health status and version.
  * `run_tests`: Runs unit tests inside a directory or file using pytest.
  * `run_tests_with_coverage`: Runs unit tests with code coverage analysis using pytest and pytest-cov.

### 8. Radon Server (`mcp-server-radon`)
A Python-based FastMCP server providing code complexity and quality metrics powered by Radon. Supports `health` checks.
- **Entry point**: [main.py](file:///c:/GitHub/MCP/mcp-server-radon/src/main.py)
- **Tools**:
  * `health`: Check Radon server health status and version.
  * `get_complexity_report`: Rates function and class complexity using Cyclomatic Complexity.
  * `get_maintainability_index`: Calculates the maintainability score of Python files.
  * `get_raw_metrics`: Computes raw metrics (LOC, LLOC, SLOC, comments, blanks).
  * `get_halstead_metrics`: Computes Halstead metrics (operands, operators, volume, difficulty, effort).
  * `get_complexity_of_code`: Calculates Cyclomatic Complexity for a raw code snippet.
  * `get_maintainability_of_code`: Calculates the maintainability score of a raw code snippet.
