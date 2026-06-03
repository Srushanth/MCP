# Black Formatter MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that formats Python files using the [Black](https://github.com/psf/black) code formatter.

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
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

### STDIO Transport (Default & Recommended)

In this mode, the MCP host/client spawns the server process directly and communicates via standard input/output.

#### Configuration:

Add the following configuration to your client's settings file (e.g., `mcp_config.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "black-formatter": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "c:/GitHub/MCP/mcp-server-black-formatter",
        "c:/GitHub/MCP/mcp-server-black-formatter/src/main.py"
      ]
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-black-formatter/src/main.py) is configured for STDIO:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
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
