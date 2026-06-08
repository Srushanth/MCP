# Ruff MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides linting, formatting, auto-fixing, and syntax modernization tools using the high-performance [Ruff](https://github.com/astral-sh/ruff) linter and formatter.

## Features

- **SSE Transport**: Runs over HTTP using Server-Sent Events (SSE) on port `3007`, permitting background orchestration and concurrent access.
- **Tools**:
  - `health`: Checks the health of the Ruff MCP server.
  - `list_rules`: Lists all available rules in Ruff.
  - `lint_file`: Runs ruff check on a file to analyze syntax/style violations.
  - `format_file`: Runs ruff format on a file to ensure PEP 8 guidelines compliance.
  - `auto_fix_file`: Runs ruff check with auto-fixing on a file.
  - `auto_fix_code`: Runs ruff check with auto-fixing on Python code passed directly as a string.
  - `modernize_syntax`: Runs ruff check with modernization rule fixes.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-ruff

# Install dependencies using uv
uv sync
```

## Configuration & Usage

This server is configured to run over **SSE (Server-Sent Events) Transport**.

### Running the Server

Start the server using `uv`:

```bash
uv run --project c:/GitHub/MCP/mcp-server-ruff c:/GitHub/MCP/mcp-server-ruff/src/main.py
```
This starts the SSE server at `http://localhost:3007`.

### Configuration

Add the following to your client's settings (e.g. `mcp_config.json`):

```json
{
  "mcpServers": {
    "ruff": {
      "serverURL": "http://localhost:3007/sse"
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-ruff/src/main.py) is configured for SSE:

```python
mcp = FastMCP("ruff", host="localhost", port=3007, streamable_http_path="/sse")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

---

## Available Tools

### `health`
Check the health status of the Ruff MCP server.
- **Returns**: A string message indicating whether the server is healthy.

### `list_rules`
List all rules available in Ruff check.
- **Returns**: A string listing all supported rules.

### `lint_file`
Analyze a Python file and report style/syntax violations (over 900 built-in rules).
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A string with lint violations or a message confirming no issues were found.

### `format_file`
Reformat a Python file in place to match PEP 8 guidelines.
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A string message confirming successful reformatting.

### `auto_fix_file`
Automatically resolve safe linting/formatting issues in a file in-place.
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A string message confirming auto-fix execution.

### `auto_fix_code`
Automatically resolve safe issues in Python code passed directly as a string.
- **Arguments**:
  - `code` (string): Python code snippet to fix.
- **Returns**: The fixed Python code or error details.

### `modernize_syntax`
Upgrade Python syntax using Ruff's modernization rules (e.g., converting old-style formats to f-strings).
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A string message confirming syntax modernization.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
