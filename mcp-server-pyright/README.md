# Pyright MCP Server

A Model Context Protocol (MCP) server built with Python and [FastMCP](https://github.com/modelcontextprotocol/python-sdk) that provides Python type checking, type stub generation, and type completeness verification using the high-performance Microsoft [Pyright](https://github.com/microsoft/pyright) static type checker.

## Features

- **STDIO Transport**: Runs via standard input/output, which is compatible with most MCP hosts and clients (e.g., Gemini IDE, Claude Desktop).
- **Tools**:
  - `health`: Checks the health and version of the Pyright MCP server.
  - `check_types_in_file`: Runs Pyright check on a specific file to identify type issues.
  - `check_types_in_project`: Runs Pyright type checking project-wide or for a specified directory. Safely respects existing custom configurations (`pyproject.toml` or `pyrightconfig.json`), falling back to a temporary configuration that ignores virtual environments and common directories if none is found.
  - `create_type_stubs`: Generates type stub files (`.pyi`) for third-party libraries.
  - `verify_type_completeness`: Verifies the type completeness of a `py.typed` package.
  - `check_types_in_code`: Runs type checking on a raw Python code snippet directly passed as a string.

## Prerequisites

- **Python**: `>= 3.13`
- **Node.js / npm** (required by Pyright internally)
- **uv** (recommended package manager) or **pip**

## Installation

Clone the repository and install the dependencies:

```bash
# Navigate to the project directory
cd mcp-server-pyright

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
    "pyright": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "c:/GitHub/MCP/mcp-server-pyright",
        "c:/GitHub/MCP/mcp-server-pyright/src/main.py"
      ]
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-pyright/src/main.py) is configured for STDIO:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Available Tools

### `health`
Check the health status of the Pyright MCP server.
- **Returns**: A string indicating whether the server is healthy and the installed Pyright version.

### `check_types_in_file`
Check type errors in a single Python file using Pyright.
- **Arguments**:
  - `file_path` (string): Absolute path to the Python file to be checked.
- **Returns**: Pyright type checking results.

### `check_types_in_project`
Check types project-wide or for a specified directory. If `pyrightconfig.json` or `pyproject.toml` is found in the project root, it uses them; otherwise, it creates a clean temporary configuration that ignores virtual environments and common directories.
- **Arguments**:
  - `project_path` (string, optional): Path to the project directory to check. Defaults to `"."`.
- **Returns**: Project-wide type checking results.

### `create_type_stubs`
Generate type stub files (`.pyi`) for a third-party package using Pyright.
- **Arguments**:
  - `package_name` (string): The name of the package to generate stubs for.
  - `project_path` (string, optional): The path to the project directory. Defaults to `"."`.
- **Returns**: Results of the stub generation.

### `verify_type_completeness`
Verify the type completeness of a `py.typed` package.
- **Arguments**:
  - `package_name` (string): The name of the package to verify.
  - `project_path` (string, optional): The path to the project directory. Defaults to `"."`.
- **Returns**: Type completeness report.

### `check_types_in_code`
Check types in a raw Python code snippet directly passed as a string.
- **Arguments**:
  - `code` (string): Python code snippet to check.
- **Returns**: The type checking results for the snippet.

---

🚀 Created by Srushanth Baride  
✉️ Email: Srushanth.Baride@gmail.com
