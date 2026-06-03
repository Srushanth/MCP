"""MCP Server"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-June-2026
#  📖 Description: TODO
#
# **************************************************************************************************

import os
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("directory-management")


@mcp.tool()
def list_files(directory_path: str) -> List[str]:
    """Tool to list files in a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        List[str]: List of files in the directory
    """
    return os.listdir(path=directory_path)


if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=2000)
