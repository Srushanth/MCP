"""MCP Server for Black Formatter"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-June-2026
#  📖 Description: Formats python files using the black formatter
#
# **************************************************************************************************

import black
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("black-formatter")


@mcp.tool(name="health", description="Check the health of the Black Formatter MCP server.")
def health() -> str:
    """Tool to check the health of the Black Formatter MCP server

    Returns:
        str: Message indicating the health of the Black Formatter MCP server
    """
    return "Black Formatter MCP server is healthy."


@mcp.tool(name="format_file", description="Format a Python file in-place using the Black formatter.")
def format_file(file_path: str) -> str:
    """Tool to format a python file using the black formatter

    Args:
        file_path (str): Path to the file to be formatted

    Returns:
        str: Message indicating the file has been formatted successfully
    """
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        contents = f.read()
    formatted_contents = black.format_str(src_contents=contents, mode=black.FileMode())
    with open(file=file_path, mode="w", encoding="utf-8") as f:
        f.write(formatted_contents)
    return f"File '{file_path}' has been formatted successfully."


if __name__ == "__main__":
    mcp.run(transport="stdio")
