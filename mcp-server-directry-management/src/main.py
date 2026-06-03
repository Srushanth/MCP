"""MCP Server"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-June-2026
#  📖 Description: MCP Server to list files in a directory
#
# **************************************************************************************************

import os
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("directory-management")


@mcp.tool()
def list_dir(directory_path: str) -> List[str]:
    """Tool to list files in a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        List[str]: List of files in the directory
    """
    list_of_items = os.listdir(path=directory_path)
    return list_of_items


@mcp.tool()
def list_files(directory_path: str) -> List[str]:
    """Tool to list files in a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        List[str]: List of files in the directory
    """
    list_of_items = os.listdir(path=directory_path)
    list_of_files = [
        item
        for item in list_of_items
        if os.path.isfile(os.path.join(directory_path, item))
    ]
    return list_of_files


@mcp.tool()
def list_folders(directory_path: str) -> List[str]:
    """Tool to list folders in a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        List[str]: List of folders in the directory
    """
    list_of_items = os.listdir(path=directory_path)
    list_of_folders = [
        item
        for item in list_of_items
        if os.path.isdir(os.path.join(directory_path, item))
    ]
    return list_of_folders


if __name__ == "__main__":
    mcp.run(transport="stdio")
