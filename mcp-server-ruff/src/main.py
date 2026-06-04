"""MCP Server for Ruff"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description:
#
# **************************************************************************************************

import sys
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ruff")


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
