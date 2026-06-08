# Black Formatter MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that formats Python files using the [Black](https://github.com/psf/black) code formatter.

## Features

- **SSE Transport**: Runs over HTTP using Server-Sent Events (SSE) on port `3002`, permitting background orchestration and concurrent access.
- **Tools**:
  - `format_file`: Formats a Python file in place.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-black-formatter

# Install dependencies using uv
uv sync
```

## Configuration & Usage

This server is configured to run over **SSE (Server-Sent Events) Transport**.

### Running the Server

Start the server using `uv`:

```bash
uv run --project c:/GitHub/MCP/mcp-server-black-formatter c:/GitHub/MCP/mcp-server-black-formatter/src/main.py
```
This starts the SSE server at `http://localhost:3002`.

### Configuration

Add the following to your client's settings (e.g. `mcp_config.json`):

```json
{
  "mcpServers": {
    "black-formatter": {
      "serverURL": "http://localhost:3002/sse"
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-black-formatter/src/main.py) is configured for SSE:

```python
mcp = FastMCP("black-formatter", host="localhost", port=3002)

if __name__ == "__main__":
    mcp.run(transport="sse")
```

---

## Available Tools

### `format_file`

Format a Python file using Black.

- **Arguments**:
  - `file_path` (string): Absolute path to the Python file.
- **Returns**: A string message confirming the file has been formatted successfully.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
