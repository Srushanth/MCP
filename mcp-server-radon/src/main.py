"""MCP Server for Radon"""

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

mcp = FastMCP("radon")


@mcp.tool()
def get_complexity_report(
    path: str = Field(..., description="Path to the file")
) -> str:
    """
    Radon analyses Python source code and returns metrics for code-quality
    assessment. It can be used as a package, module, or command-line tool.


    Args:
        path (str, optional): _description_. Defaults to Field(..., description="Path to the file").

    Returns:
        str: _description_
    """
    return radon.cli.main_for_function(
        radon.cli.CLI,
        [
            "cc",
            path,
            "-a",
            "-s",
            "--no-doc",
            "--no-multiline",
            "--no-blank",
            "--no-skip-over-tests",
        ],
    )


@mcp.tool()
def get_maintainability_index(
    path: str = Field(..., description="Path to the file")
) -> str:
    """
    Radon analyses Python source code and returns metrics for code-quality
    assessment. It can be used as a package, module, or command-line tool.

    Args:
        path (str, optional): Path to the file. Defaults to Field(..., description="Path to the file").

    Returns:
        str: Maintainability Index of the file
    """
    return radon.cli.main_for_function(
        radon.cli.CLI,
        [
            "mi",
            path,
            "-a",
            "-s",
            "--no-doc",
            "--no-multiline",
            "--no-blank",
            "--no-skip-over-tests",
        ],
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
