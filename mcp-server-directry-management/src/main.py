"""MCP Server for Directory Management"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-June-2026
#  📖 Description: MCP Server providing tools to list directory contents, files, and folders
#
# **************************************************************************************************

import os
import shutil
from typing import List
from typing import Optional
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


@mcp.tool()
def read_file_contents(file_path: str) -> str:
    """Tool to read the contents of a file

    Args:
        file_path (str): Path to the file

    Returns:
        str: Contents of the file
    """
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        contents = f.read()
        return contents


@mcp.tool()
def write_file_contents(file_path: str, contents: str, overwrite: bool = False) -> str:
    """Tool to write the contents of a file

    Args:
        file_path (str): Path to the file
        contents (str): Contents to be written to the file
        overwrite (bool, optional): Whether to overwrite the file if it exists. Defaults to False.

    Returns:
        str: Message indicating the file has been written
    """
    if os.path.exists(path=file_path) and not overwrite:
        return f"File '{file_path}' already exists. Use overwrite=True to overwrite the file."
    with open(file=file_path, mode="w", encoding="utf-8") as f:
        f.write(contents)
        return f"File '{file_path}' has been written successfully."


@mcp.tool()
def create_directory(directory_path: str) -> str:
    """Tool to create a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        str: Message indicating the directory has been created
    """
    os.makedirs(path=directory_path, exist_ok=True)
    return f"Directory '{directory_path}' has been created successfully."


@mcp.tool()
def move_or_rename(source_path: str, destination_path: str) -> str:
    """Tool to move or rename a file or directory

    Args:
        source_path (str): Path to the file or directory
        destination_path (str): Path to the file or directory

    Returns:
        str: Message indicating the file or directory has been moved or renamed
    """
    os.rename(src=source_path, dst=destination_path)
    return f"File or directory '{source_path}' has been moved or renamed to '{destination_path}'."


@mcp.tool()
def copy_file_or_folder(source_path: str, destination_path: str) -> str:
    """Tool to copy a file or directory

    Args:
        source_path (str): Path to the file or directory
        destination_path (str): Path to the file or directory

    Returns:
        str: Message indicating the file or directory has been copied
    """
    if os.path.isdir(path=source_path):
        shutil.copytree(src=source_path, dst=destination_path)
        return f"Directory '{source_path}' has been copied to '{destination_path}'."
    else:
        shutil.copy2(src=source_path, dst=destination_path)
        return f"File '{source_path}' has been copied to '{destination_path}'."


@mcp.tool()
def get_path_metadata(path: str) -> dict:
    """Tool to get the metadata of a file or directory

    Args:
        path (str): Path to the file or directory

    Returns:
        dict: Metadata of the file or directory
    """
    metadata = os.stat(path=path)
    return metadata


if __name__ == "__main__":
    mcp.run(transport="stdio")
