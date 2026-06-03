# Directory Management MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides tools for directory and file listing.

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
- **Tools**:
  - `list_files`: List files and folders within a given directory path.

## Prerequisites

- **Python**: `>= 3.13`
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-directry-management

# Install dependencies using uv
uv sync
```

## Configuration & Usage

### 1. STDIO Transport (Default & Recommended)

In this mode, the MCP host/client spawns the server process directly and communicates via standard input/output.

#### Configuration:

Add the following configuration to your client's settings file (e.g., `mcp_config.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "directory-management": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "c:/GitHub/MCP/mcp-server-directry-management",
        "src/main.py"
      ]
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-directry-management/src/main.py) is configured for STDIO:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

### 2. SSE Transport (Alternative)

If you want to run this server over HTTP using Server-Sent Events (SSE):

1. Update the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-directry-management/src/main.py):
   ```python
   if __name__ == "__main__":
       mcp.run(transport="sse")
   ```
2. Start the HTTP server:
   ```bash
   uv run src/main.py
   ```
   This will spin up the server at `http://localhost:8000`.
3. Configure the client using the SSE `url`:
   ```json
   {
     "mcpServers": {
       "directory-management": {
         "url": "http://localhost:8000/sse"
       }
     }
   }
   ```

---

## Available Tools

### `list_files`

List the contents of a directory path.

- **Arguments**:
  - `directory_path` (string): Absolute path to the directory.
- **Returns**: A list of strings containing file and folder names.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
