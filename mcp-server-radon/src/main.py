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


@mcp.tool(name="health", description="Check the health and version of the Radon MCP server.")
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


@mcp.tool(name="get_complexity_report", description="Analyze Python modules/packages and compute Cyclomatic Complexity (CC).")
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


@mcp.tool(name="get_maintainability_index", description="Analyze Python modules/packages and compute the Maintainability Index (MI).")
def get_maintainability_index(path: str) -> str:
    """Analyze the given Python modules/packages and compute the Maintainability Index (MI).

    Args:
        path (str): The file or directory path to analyze.

    Returns:
        str: Maintainability Index report.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        # Run radon mi on path with show flag to show actual MI value
        result = subprocess.run(
            [sys.executable, "-m", "radon", "mi", path, "-s"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running Maintainability Index check on '{path}': {str(e)}"


@mcp.tool(name="get_raw_metrics", description="Analyze Python modules/packages and compute raw metrics (LOC, LLOC, SLOC, etc.).")
def get_raw_metrics(path: str) -> str:
    """Analyze the given Python modules/packages and compute raw metrics (LOC, LLOC, SLOC, etc.).

    Args:
        path (str): The file or directory path to analyze.

    Returns:
        str: Raw metrics report.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        # Run radon raw on path
        result = subprocess.run(
            [sys.executable, "-m", "radon", "raw", path],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running raw metrics check on '{path}': {str(e)}"


@mcp.tool(name="get_halstead_metrics", description="Analyze Python modules/packages and compute Halstead metrics.")
def get_halstead_metrics(path: str) -> str:
    """Analyze the given Python modules/packages and compute Halstead metrics.

    Args:
        path (str): The file or directory path to analyze.

    Returns:
        str: Halstead metrics report.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    try:
        # Run radon hal on path
        result = subprocess.run(
            [sys.executable, "-m", "radon", "hal", path],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running Halstead metrics check on '{path}': {str(e)}"


@mcp.tool(name="get_complexity_of_code", description="Analyze a raw Python code snippet and compute Cyclomatic Complexity (CC).")
def get_complexity_of_code(code: str) -> str:
    """Analyze a raw Python code snippet and compute Cyclomatic Complexity (CC).

    Args:
        code (str): The Python code snippet to analyze.

    Returns:
        str: Cyclomatic Complexity report.
    """
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_file_name = temp_file.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "radon", "cc", temp_file_name, "-s", "-a"],
                capture_output=True,
                text=True,
                check=False,
            )
            output = result.stdout or result.stderr or ""
            return output.replace(temp_file_name, "snippet.py")
        finally:
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
    except Exception as e:
        return f"Error running Cyclomatic Complexity check on code snippet: {str(e)}"


@mcp.tool(name="get_maintainability_of_code", description="Analyze a raw Python code snippet and compute the Maintainability Index (MI).")
def get_maintainability_of_code(code: str) -> str:
    """Analyze a raw Python code snippet and compute the Maintainability Index (MI).

    Args:
        code (str): The Python code snippet to analyze.

    Returns:
        str: Maintainability Index report.
    """
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_file_name = temp_file.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "radon", "mi", temp_file_name, "-s"],
                capture_output=True,
                text=True,
                check=False,
            )
            output = result.stdout or result.stderr or ""
            return output.replace(temp_file_name, "snippet.py")
        finally:
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
    except Exception as e:
        return f"Error running Maintainability Index check on code snippet: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
