# Secrets & Credentials Scanner MCP Server

A Model Context Protocol (MCP) server providing security tools to scan files, directories, and raw code snippets for exposed credentials, API keys, passwords, and private keys. 

Powered by Yelp's standard `detect-secrets` package as its heuristic analysis engine.

## Features & Tools

### 1. `health`
Checks the server health status and lists the active `detect-secrets` package version.
*   **Parameters:** None
*   **Returns:** A status string.

### 2. `scan_file`
Scans a single file on disk. If potential secrets are found, it queries the file to include the corresponding source code lines as context.
*   **Parameters:**
    *   `file_path` (string, required): Absolute path to the file.
*   **Returns:** A JSON summary containing the count of secrets found and a list of findings (type, line number, hashed secret, and line content).

### 3. `scan_code`
Allows scanning raw code strings or snippets in memory (e.g. text copy-pasted or generated).
*   **Parameters:**
    *   `code` (string, required): Raw text/code snippet contents to scan.
*   **Returns:** A JSON summary of any found secrets matching the line boundaries of the string.

### 4. `scan_directory`
Recursively crawls a workspace or directory to identify credentials.
*   **Parameters:**
    *   `directory_path` (string, required): Absolute path to the directory.
    *   `exclude_patterns` (array of strings, optional): Additional substrings to filter out file paths (e.g. `["tests", "fixtures"]`).
*   **Returns:** A grouped JSON object mapping each relative file path to its findings.
*   **Smart Exclusions:** Automatically skips binary files, build artifacts, and dependency directories:
    *   `.git`, `.venv`, `venv`, `node_modules`, `__pycache__`
    *   `.mypy_cache`, `.ruff_cache`, `.vscode`, `.idea`, `build`, `dist`

---

## Configuration & Usage

This server is configured to run over **SSE (Server-Sent Events) Transport**.

### Running the Server

Start the server using `uv`:

```bash
uv run --project c:/GitHub/MCP/mcp-server-secret-scan c:/GitHub/MCP/mcp-server-secret-scan/src/main.py
```
This starts the SSE server at `http://localhost:3008`.

### Configuration

Add the following to your client's settings (e.g. `mcp_config.json`):

```json
{
  "mcpServers": {
    "secret-scan": {
      "serverURL": "http://localhost:3008/sse"
    }
  }
}
```

Make sure the entry point in [src/main.py](file:///c:/GitHub/MCP/mcp-server-secret-scan/src/main.py) is configured for SSE:

```python
mcp = FastMCP("secret-scan", host="localhost", port=3008)

if __name__ == "__main__":
    mcp.run(transport="sse")
```

---

## Local Development & Debugging

### Running via MCP Inspector
To run and test the server interactively using the official Model Context Protocol Inspector:

```bash
npx @modelcontextprotocol/inspector uv --directory C:/GitHub/MCP/mcp-server-secret-scan run src/main.py
```

### Installation
Dependencies are managed via `uv`. You can install them by running:

```bash
cd mcp-server-secret-scan
uv sync
```
