# Bandit MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides security linting, vulnerability analysis, and dependency security audits using [Bandit](https://github.com/PyCQA/bandit) and [pip-audit](https://github.com/pypa/pip-audit).

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
- **Tools**:
  - `health`: Checks the health and version of the Bandit MCP server.
  - `scan_vulnerabilities_in_file`: Scans a single Python file for security issues.
  - `scan_vulnerabilities_in_project`: Recursively scans an entire project directory for security issues with optional severity and confidence filtering.
  - `scan_vulnerabilities_in_code`: Analyzes a raw Python code snippet for vulnerabilities.
  - `check_dependencies_vulnerabilities`: Inspects python projects (e.g. `pyproject.toml`, lockfiles, or requirements text files) for known vulnerable dependency packages using `pip-audit`.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-bandit

# Install dependencies using uv
uv sync
```

## Configuration & Usage

### STDIO Transport (Default & Recommended)

In this mode, the MCP host/client spawns the server process directly and communicates via standard input/output.

#### Configuration:

Add the following configuration to your client's settings file (e.g., `mcp_config.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "bandit": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "c:/GitHub/MCP/mcp-server-bandit",
        "c:/GitHub/MCP/mcp-server-bandit/src/main.py"
      ]
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-bandit/src/main.py) is configured for STDIO:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Available Tools

### `health`
Check the health status of the Bandit MCP server.
- **Returns**: A string indicating whether the server is healthy and the installed Bandit version.

### `scan_vulnerabilities_in_file`
Scan a single Python file and report common security issues (e.g., hardcoded passwords, shell injections, weak cryptography).
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A dictionary containing stdout and stderr results.

### `scan_vulnerabilities_in_project`
Scan all Python files in a directory recursively using Bandit, returning structured JSON results.
- **Arguments**:
  - `project_path` (string, optional): Path to the project directory. Defaults to `"."`.
  - `severity_level` (string, optional): Report only issues of this level or higher (`all`, `low`, `medium`, `high`). Defaults to `"all"`.
  - `confidence_level` (string, optional): Report only issues of this level or higher (`all`, `low`, `medium`, `high`). Defaults to `"all"`.
- **Returns**: A dictionary representing the Bandit JSON report of security issues.

### `scan_vulnerabilities_in_code`
Scan a raw Python code snippet directly passed as a string.
- **Arguments**:
  - `code` (string): Python code snippet to check.
- **Returns**: A dictionary containing scan stdout, stderr, and exit code.

### `check_dependencies_vulnerabilities`
Check for security vulnerabilities in a dependency file (e.g., `requirements.txt`) or a local project (e.g. directory containing `pyproject.toml` or lockfiles) using `pip-audit`.
- **Arguments**:
  - `dependency_file` (string): The path to the dependency file or project directory.
- **Returns**: A dictionary with dependency vulnerability scan results.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
