"""MCP Server for pytest"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description: Test runner and coverage reporting using pytest and pytest-cov
#
# **************************************************************************************************


import os
import sys
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pytest", host="localhost", port=3005)


@mcp.tool(
    name="health", description="Check the health and version of the pytest MCP server."
)
def health() -> str:
    """Check the health and version of the pytest MCP server.

    Returns:
        str: Health status and version of pytest.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            return f"pytest MCP server is healthy. {version}"
        else:
            return f"pytest MCP server health check failed: {result.stderr or result.stdout}"
    except Exception as e:
        return f"pytest MCP server is unhealthy: {str(e)}"


@mcp.tool(
    name="run_tests", description="Run pytest on the specified file or directory path."
)
def run_tests(path: str) -> str:
    """Run pytest on the given path.

    Args:
        path (str): The path to the directory containing the test files.

    Returns:
        str: The output of the pytest command.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", path],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running pytest on '{path}': {str(e)}"


@mcp.tool(
    name="run_tests_with_coverage",
    description="Run pytest with code coverage analysis using pytest-cov.",
)
def run_tests_with_coverage(path: str) -> str:
    """Run pytest with code coverage analysis on the given path.

    Args:
        path (str): The path to the directory containing the test files.

    Returns:
        str: The output of the pytest command with coverage statistics.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--cov", path, path],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running pytest with coverage on '{path}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse")
