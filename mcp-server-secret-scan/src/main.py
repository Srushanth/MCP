"""MCP Server for Secrets & Credentials Scanning"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 05-June-2026
#  📖 Description: Scans files, directories, and code snippets for secrets and credentials.
#
# **************************************************************************************************

import importlib.metadata
import os
import tempfile
from typing import Any, Dict, List, Optional
from detect_secrets import SecretsCollection
from detect_secrets.settings import default_settings
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("secret-scan")


@mcp.tool(
    name="health",
    description="Check the health and version of the Secrets Scanner MCP server.",
)
def health() -> str:
    """Tool to check the health and version of the Secrets Scanner MCP server.

    Returns:
        str: Message indicating the health and version of the server.
    """
    version = get_detect_secrets_version()
    return f"Secrets Scanner MCP server is healthy. detect-secrets version: {version}"


def get_detect_secrets_version() -> str:
    """Helper to get detect-secrets package version."""
    try:
        return importlib.metadata.version("detect-secrets")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


if __name__ == "__main__":
    mcp.run(transport="stdio")
