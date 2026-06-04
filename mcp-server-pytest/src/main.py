"""MCP Server for pytest"""

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


from mcp.server.fastmcp import FastMCP


mcp = FastMCP("pytest")


@mcp.tool()
def run_pytest(path: str) -> str:
    """Run pytest on the given path.

    Args:
        path (str): The path to the directory containing the test files.

    Returns:
        str: The output of the pytest command.
    """
    try:
        result = subprocess.run(
            ["pytest", path],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout or result.stderr or "No results returned."
    except Exception as e:
        return f"Error running pytest on '{path}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
