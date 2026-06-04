"""MCP Server for Radon"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description: Code complexity and maintainability analysis using Radon
#
# **************************************************************************************************
import os
import sys
import tempfile
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("radon")


@mcp.tool()
def health() -> str:
    """Check the health and version of the Radon MCP server.

    Returns:
        str: Health status and version of Radon.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "radon", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            return f"Radon MCP server is healthy. Radon version: {version}"
        else:
            return f"Radon MCP server health check failed: {result.stderr or result.stdout}"
    except Exception as e:
        return f"Radon MCP server is unhealthy: {str(e)}"


@mcp.tool()
def get_complexity_report(path: str) -> str:
    """Analyze the given Python modules/packages and compute Cyclomatic Complexity (CC).

    Args:
        path (str): The file or directory path to analyze.

    Returns:
        str: Cyclomatic Complexity report.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        # Run radon cc on path with show-complexity and average flags
        result = subprocess.run(
            [sys.executable, "-m", "radon", "cc", path, "-s", "-a"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running Cyclomatic Complexity check on '{path}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
