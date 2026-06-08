# Pytest MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides test running and code coverage statistics using [pytest](https://docs.pytest.org/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov).

## Features

- **SSE Transport**: Runs over HTTP using Server-Sent Events (SSE) on port `3005`, permitting background orchestration and concurrent access.
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

This server is configured to run over **SSE (Server-Sent Events) Transport**.

### Running the Server

Start the server using `uv`:

```bash
uv run --project c:/GitHub/MCP/mcp-server-pytest c:/GitHub/MCP/mcp-server-pytest/src/main.py
```
This starts the SSE server at `http://localhost:3005`.

### Configuration

Add the following to your client's settings (e.g. `mcp_config.json`):

```json
{
  "mcpServers": {
    "pytest": {
      "serverURL": "http://localhost:3005/sse"
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-pytest/src/main.py) is configured for SSE:

```python
mcp = FastMCP("pytest", host="localhost", port=3005, streamable_http_path="/sse")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
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
