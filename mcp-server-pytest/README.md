# Pytest MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides test running and code coverage statistics using [pytest](https://docs.pytest.org/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov).

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
- **Tools**:
  - `health`: Checks the health and version of the pytest MCP server.
  - `run_tests`: Runs unit tests in a specified directory or file.
  - `run_tests_with_coverage`: Runs unit tests in a specified directory or file with code coverage reports.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-pytest

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
    "pytest": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "c:/GitHub/MCP/mcp-server-pytest",
        "c:/GitHub/MCP/mcp-server-pytest/src/main.py"
      ]
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-pytest/src/main.py) is configured for STDIO:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Available Tools

### `health`
Check the health status of the pytest MCP server.
- **Returns**: A string indicating whether the server is healthy and the installed pytest version.

### `run_tests`
Run tests inside a specified path using pytest.
- **Arguments**:
  - `path` (string): Path to the test file or directory containing test files.
- **Returns**: A string with the pytest output report.

### `run_tests_with_coverage`
Run tests inside a specified path using pytest and return coverage details.
- **Arguments**:
  - `path` (string): Path to the test file or directory containing test files.
- **Returns**: A string with test results and coverage percentages.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
