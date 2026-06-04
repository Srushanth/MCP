"""MCP Server for Pyright"""

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

mcp = FastMCP("Pyright")


@mcp.tool()
def check_types_in_file(file_path: str) -> str:
    """Check types in a file using pyright.
    Args:
        file_path (str): The path to the file to check.

    Returns:
        str: The results of the type check.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pyright", file_path],
            capture_output=True,
            text=True,
            check=False,
        )
        output = result.stdout or result.stderr or ""
        if result.returncode == 0:
            return f"Type checking passed:\n{output}"
        else:
            return f"Type checking failed:\n{output}"
    except Exception as e:
        return f"Error running pyright on '{file_path}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
