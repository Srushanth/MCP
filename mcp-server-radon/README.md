# Radon MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides code quality and complexity analysis using [Radon](https://github.com/rubik/radon) (Cyclomatic Complexity, Maintainability Index, Halstead metrics, and raw line metrics).

## Features

- **SSE Transport**: Runs over HTTP using Server-Sent Events (SSE) on port `3006`, permitting background orchestration and concurrent access.
- **Tools**:
  - `health`: Checks the health and version of the Radon MCP server.
  - `get_complexity_report`: Computes Cyclomatic Complexity (CC) for files or directories.
  - `get_maintainability_index`: Computes Maintainability Index (MI) for files or directories.
  - `get_raw_metrics`: Computes raw metrics (LOC, LLOC, SLOC, comments, blanks) for files or directories.
  - `get_halstead_metrics`: Computes Halstead metrics for files or directories.
  - `get_complexity_of_code`: Computes Cyclomatic Complexity for a raw code snippet.
  - `get_maintainability_of_code`: Computes Maintainability Index for a raw code snippet.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-radon

# Install dependencies using uv
uv sync
```

## Configuration & Usage

This server is configured to run over **SSE (Server-Sent Events) Transport**.

### Running the Server

Start the server using `uv`:

```bash
uv run --project c:/GitHub/MCP/mcp-server-radon c:/GitHub/MCP/mcp-server-radon/src/main.py
```
This starts the SSE server at `http://localhost:3006`.

### Configuration

Add the following to your client's settings (e.g. `mcp_config.json`):

```json
{
  "mcpServers": {
    "radon": {
      "serverURL": "http://localhost:3006/sse"
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-radon/src/main.py) is configured for SSE:

```python
mcp = FastMCP("radon", host="localhost", port=3006)

if __name__ == "__main__":
    mcp.run(transport="sse")
```

---

## Available Tools

### `health`
Check the health status of the Radon MCP server.
- **Returns**: A string indicating whether the server is healthy and the installed Radon version.

### `get_complexity_report`
Analyze Python files/directories and compute Cyclomatic Complexity (CC).
- **Arguments**:
  - `path` (string): Path to the Python file or directory.
- **Returns**: A string report indicating CC grades (A to F) and line numbers.

### `get_maintainability_index`
Analyze Python files/directories and compute the Maintainability Index (MI) score (A to C).
- **Arguments**:
  - `path` (string): Path to the Python file or directory.
- **Returns**: A string report indicating the MI score.

### `get_raw_metrics`
Compute raw metrics (Lines of Code, Logical Lines of Code, Source Lines of Code, comments, multi-line strings, blanks).
- **Arguments**:
  - `path` (string): Path to the Python file or directory.
- **Returns**: A string report of raw counts.

### `get_halstead_metrics`
Compute Halstead metrics (distinct operands/operators, total volume, difficulty, effort).
- **Arguments**:
  - `path` (string): Path to the Python file or directory.
- **Returns**: A string report of Halstead metrics.

### `get_complexity_of_code`
Compute Cyclomatic Complexity (CC) on a raw code snippet.
- **Arguments**:
  - `code` (string): Python code snippet.
- **Returns**: Complexity analysis report.

### `get_maintainability_of_code`
Compute Maintainability Index (MI) on a raw code snippet.
- **Arguments**:
  - `code` (string): Python code snippet.
- **Returns**: Maintainability analysis report.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
