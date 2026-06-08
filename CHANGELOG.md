# CHANGELOG

## [2026-06-08] - SSE Transport Transition

This update migrates the 8 custom Python-based Model Context Protocol (MCP) servers from the local `stdio` stream transport to standalone **SSE (Server-Sent Events)** HTTP services. This permits concurrent client connections, asynchronous debugging, and decoupling of server lifecycles from single IDE process frames.

### Added
*   **Root `Makefile`**: Exposes targets for booting all MCP servers concurrently (`make run-all`, the default target) as well as booting individual servers (e.g. `make run-pyright`).
    *   **`make setup`**: Added a target to initialize `.venv` folders and synchronize Python dependencies (`uv sync`) for all 8 servers in a single run.
*   **Orchestration Script (`run_servers.py`)**: A cross-platform runner script that concurrently spins up all 8 Python servers via background subprocesses.
    *   **Unified Logging**: Prefixes all stdout and stderr streams with the server's name (e.g., `[bandit]`, `[pyright]`) for unified console reading.
    *   **Ctrl+C Clean Exit**: Intercepts `SIGINT` (KeyboardInterrupt) to terminate child servers gracefully, preventing port lockouts and orphan processes.
    *   **Automatic Exit Monitoring**: Detects if any subprocess exits unexpectedly and automatically shuts down other child processes.

### Changed
*   **FastMCP Server Configurations (`main.py` entry points)**:
    *   Resolved `TypeError: FastMCP.run() got an unexpected keyword argument 'host'` by defining `host="localhost"` and `port=300X` inside the `FastMCP(...)` class instantiation block, rather than the `mcp.run(...)` runner method.
    *   Updated the runner blocks across all 8 servers to use `mcp.run(transport="sse")`.
    *   Allocated unique SSE listener ports across the projects:
        *   `mcp-server-bandit`: Port `3001`
        *   `mcp-server-black-formatter`: Port `3002`
        *   `mcp-server-directry-management`: Port `3003`
        *   `mcp-server-pyright`: Port `3004`
        *   `mcp-server-pytest`: Port `3005`
        *   `mcp-server-radon`: Port `3006`
        *   `mcp-server-ruff`: Port `3007`
        *   `mcp-server-secret-scan`: Port `3008`
*   **Root `README.md`**: Appended a new documentation section detailing Make orchestration, SSE ports, and the required client settings setup.
*   **Project READMEs**: Rewrote the Features, Prerequisites, Usage, and Configuration sections across all 8 subproject `README.md` files to document SSE transport, execution instructions, and the required JSON settings block.
*   **`pyproject.toml` files**: Replaced placeholders (`"Add your description here"`) with descriptive details outlining each server's specific utility and integrations across all 8 Python server configurations and the root ADK.

### Client Configuration Update (`mcp_config.json`)
To consume the newly migrated SSE servers, configurations in `mcp_config.json` were transitioned to use `"serverURL"` (required by the IDE schema) pointing to the `/sse` route:

```json
{
  "mcpServers": {
    "directory-management": {
      "serverURL": "http://localhost:3003/sse"
    },
    "black-formatter": {
      "serverURL": "http://localhost:3002/sse"
    },
    "pyright": {
      "serverURL": "http://localhost:3004/sse"
    },
    "bandit": {
      "serverURL": "http://localhost:3001/sse"
    },
    "pytest": {
      "serverURL": "http://localhost:3005/sse"
    },
    "ruff": {
      "serverURL": "http://localhost:3007/sse"
    },
    "radon": {
      "serverURL": "http://localhost:3006/sse"
    },
    "secret-scan": {
      "serverURL": "http://localhost:3008/sse"
    }
  }
}
```
