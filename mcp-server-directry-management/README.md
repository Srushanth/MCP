# Directory Management MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides tools for directory and file listing.

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
- **Tools**:
  - `list_dir`: List all files and folders in a directory.
  - `list_files`: List only the files in a directory.
  - `list_folders`: List only the subfolders in a directory.
  - `read_file_contents`: Read the full text contents of a file.
  - `write_file_contents`: Write text contents to a file.
  - `create_directory`: Create a directory (including parent directories recursively).
  - `move_or_rename`: Move or rename a file or directory.
  - `copy_file_or_folder`: Copy a file or recursively copy a directory.
  - `get_path_metadata`: Retrieve path stat metadata.
  - `path_exists`: Verify if a file/directory path exists.
  - `search_files`: Search for files inside a directory by name matching.

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
        "c:/GitHub/MCP/mcp-server-directry-management/src/main.py"
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

### `list_dir`
List the contents of a directory path.
- **Arguments**:
  - `directory_path` (string): Absolute path to the directory.
- **Returns**: A list of file and folder names.

### `list_files`
List only the files in a directory.
- **Arguments**:
  - `directory_path` (string): Absolute path to the directory.
- **Returns**: A list of filenames.

### `list_folders`
List only the folders/subdirectories in a directory.
- **Arguments**:
  - `directory_path` (string): Absolute path to the directory.
- **Returns**: A list of folder names.

### `read_file_contents`
Read the text content of a file.
- **Arguments**:
  - `file_path` (string): Path to the file.
- **Returns**: The contents of the file.

### `write_file_contents`
Write text content to a file.
- **Arguments**:
  - `file_path` (string): Path to the file.
  - `contents` (string): Content to write.
  - `overwrite` (boolean, optional): Whether to overwrite if the file exists (default: `false`).
- **Returns**: Status message.

### `create_directory`
Create a directory recursively.
- **Arguments**:
  - `directory_path` (string): Path to the directory.
- **Returns**: Status message.

### `move_or_rename`
Move or rename a file or directory.
- **Arguments**:
  - `source_path` (string): Current path.
  - `destination_path` (string): Target path.
- **Returns**: Status message.

### `copy_file_or_folder`
Copy a file or directory tree.
- **Arguments**:
  - `source_path` (string): Source path.
  - `destination_path` (string): Destination path.
- **Returns**: Status message.

### `get_path_metadata`
Get OS stat metadata of a file or directory.
- **Arguments**:
  - `path` (string): Path to the file or directory.
- **Returns**: Dictionary containing file/directory statistics.

### `path_exists`
Check if a path exists on the filesystem.
- **Arguments**:
  - `path` (string): Path to verify.
- **Returns**: `true` if it exists, `false` otherwise.

### `search_files`
Search files in a directory by substring match.
- **Arguments**:
  - `directory_path` (string): Path to search.
  - `query` (string): Query substring to look for.
- **Returns**: List of matching filenames.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
