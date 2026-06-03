# MCP: Model Context Protocol Repository

This repository contains implementations, integrations, and examples demonstrating the use of the Model Context Protocol (MCP) for building intelligent and modular AI applications.

## Overview

The repository is structured to facilitate easy understanding and usage of MCP with various toolkits, particularly emphasizing integration with Google's Agent Development Kit (ADK) and custom MCP servers.

## Repository Structure

```text
└── 📁MCP
    ├── 📁.vscode
    │   └── settings.json
    ├── 📁ADK
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── agent.py
    │   └── uv.lock
    ├── 📁Daily_Status_Update
    ├── 📁MCP_Server
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Clock Server)
    │   └── uv.lock
    ├── 📁mcp-server-black-formatter
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── 📁src
    │   │   └── main.py (Black Formatter Server)
    │   └── uv.lock
    └── 📁mcp-server-directry-management
        ├── pyproject.toml
        ├── README.md
        ├── 📁src
        │   └── main.py (Directory Management Server)
        └── uv.lock
```

## Available Projects

### 1. Agent Development Kit (ADK)
Contains the integration of agents utilizing Google's ADK to coordinate with MCP servers.

### 2. Directory Management Server (`mcp-server-directry-management`)
A Python-based FastMCP server offering comprehensive filesystem tools including directory listing, file read/write, file copying/moving, path metadata inspection, and search.

### 3. Clock Server (`MCP_Server`)
A simple Python-based FastMCP server providing timezone-aware date and time capabilities.

### 4. Black Formatter Server (`mcp-server-black-formatter`)
A Python-based FastMCP server providing a tool to format Python files using the Black code formatter.


