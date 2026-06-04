"""MCP Server for Ruff"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description: Lint, format, and auto-fix Python code using Ruff
#
# **************************************************************************************************

import sys
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ruff")


@mcp.tool()
def health() -> str:
    """Tool to check the health of the Ruff MCP server

    Returns:
        str: Message indicating the health of the Ruff MCP server
    """
    return "Ruff MCP server is healthy."


@mcp.tool()
def list_rules() -> str:
    """Tool to list all available rules in Ruff

    Returns:
        str: Message indicating the rules available in Ruff
    """
    try:
        # Run ruff check on the file
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "check", "--list-rules"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return f"Rules available: {result.stdout}"
        else:
            output = result.stderr or result.stdout
            return f"Error listing rules: {output}"
    except Exception as e:
        return f"Error listing rules: {str(e)}"


@mcp.tool()
def lint_file(file_path: str) -> str:
    """Tool to lint a file using Ruff

    Args:
        file_path (str): Path to the file to be linted

    Returns:
        str: Message indicating the file has been linted
    """
    try:
        # Run ruff check on the file
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "check", file_path],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return f"File '{file_path}' has been linted. No issues found."
        else:
            # Ruff prints lint errors to stdout by default
            output = result.stdout or result.stderr
            return f"File '{file_path}' has been linted. Issues found:\n{output}"
    except Exception as e:
        return f"Error running lint on '{file_path}': {str(e)}"


@mcp.tool()
def format_file(file_path: str) -> str:
    """Tool to format a python file using the Ruff formatter

    Args:
        file_path (str): Path to the file to be formatted

    Returns:
        str: Message indicating the file has been formatted successfully
    """
    try:
        # Run ruff format on the file
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "format", file_path],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return f"File '{file_path}' has been formatted successfully."
        else:
            output = result.stderr or result.stdout
            return f"Error formatting file '{file_path}':\n{output}"
    except Exception as e:
        return f"Error running formatter on '{file_path}': {str(e)}"


@mcp.tool()
def auto_fix_file(file_path: str) -> str:
    """Tool to auto fix a python file using the Ruff auto-fixer

    Args:
        file_path (str): Path to the file to be auto-fixed

    Returns:
        str: Message indicating the file has been auto-fixed successfully
    """
    try:
        # Run ruff check on the file
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "check", file_path, "--fix"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return f"File '{file_path}' has been auto-fixed successfully."
        else:
            output = result.stderr or result.stdout
            return f"Error auto-fixing file '{file_path}':\n{output}"
    except Exception as e:
        return f"Error running auto-fix on '{file_path}': {str(e)}"


@mcp.tool()
def auto_fix_code(code: str) -> str:
    """Tool to auto fix python code using the Ruff auto-fixer

    Args:
        code (str): The python code to be fixed

    Returns:
        str: The fixed python code
    """
    try:
        # Run ruff check on the code
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "check", "--fix", "--code", code],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return "Code has been fixed successfully."
        else:
            output = result.stderr or result.stdout
            return f"Error fixing code:\n{output}"
    except Exception as e:
        return f"Error running auto-fix on code: {str(e)}"


@mcp.tool()
def modernize_syntax(file_path: str) -> str:
    """Tool to modernize syntax of a python file using the Ruff modernize-syntax rule

    Args:
        file_path (str): Path to the file to be modernized

    Returns:
        str: Message indicating the file has been modernized successfully
    """
    try:
        # Run ruff check on the file
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "ruff",
                "check",
                file_path,
                "--fix",
                "--rule",
                "RUF001",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return f"File '{file_path}' has been modernized successfully."
        else:
            output = result.stderr or result.stdout
            return f"Error modernizing file '{file_path}':\n{output}"
    except Exception as e:
        return f"Error running modernize on '{file_path}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
