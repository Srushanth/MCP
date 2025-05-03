# ADK: Agent Development Kit Integration with MCP

This module demonstrates the integration of Google's Agent Development Kit (ADK) with the Model Context Protocol (MCP), enabling the development of intelligent agents capable of interacting seamlessly with external tools and services.

## Overview

* **ADK Integration**: Google's Agent Development Kit is utilized for agent development.
* **MCP Communication**: Implements MCP, allowing agents to communicate effectively with external tools.
* **Modular Design**: Easily extensible architecture for integrating additional tools and functionalities.

## Prerequisites

* Python 3.13
* [Google ADK](https://github.com/google/adk-python)
* [MCP Server](https://github.com/google/adk-docs/blob/main/docs/tools/mcp-tools.md)
* [uv Package Manager](https://github.com/astral-sh/uv)

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Srushanth/MCP.git
    cd MCP/ADK
    ```

2. **Set Up Environment with `uv`**:

    ```bash
    uv sync
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    uv pip install -r requirements.txt
    ```

## Usage

1. **Start the Agent**:

    ```bash
    adk web
    ```

The agent will now connect to the MCP server and handle incoming requests.

## Project Structure

```text
└── 📁ADK
    └── 📁src
        └── __init__.py
        └── agent.py
    └── __init__.py
    └── .python-version
    └── pyproject.toml
    └── README.md
    └── uv.lock
```

## References

* [Google ADK Documentation](https://google.github.io/adk-docs/)
* [MCP Tools Documentation](https://google.github.io/adk-docs/tools/mcp-tools/)
