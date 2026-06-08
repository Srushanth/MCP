"""MCP Server for Directory Management"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-June-2026
#  📖 Description: Provides a set of tools to perform operations on files and directories.
#                  The tools include:
#                      - list_dir
#                      - list_files
#                      - list_folders
#                      - read_file_contents
#                      - write_file_contents
#                      - create_directory
#                      - move_or_rename
#                      - copy_file_or_folder
#                      - get_path_metadata
#                      - path_exists
#                      - search_files
#
# **************************************************************************************************

import os
import shutil
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("directory-management", host="localhost", port=3003)


@mcp.tool(
    name="health",
    description="Check the health of the Directory Management MCP server.",
)
def health() -> str:
    """Tool to check the health of the Directory Management MCP server

    Returns:
        str: Message indicating the health of the Directory Management MCP server
    """
    return "Directory Management MCP server is healthy."


@mcp.tool(name="list_dir", description="List all files and folders in a directory.")
def list_dir(directory_path: str) -> List[str]:
    """Tool to list files in a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        List[str]: List of files in the directory
    """
    list_of_items = os.listdir(path=directory_path)
    return list_of_items


@mcp.tool(name="list_files", description="List only files in a directory.")
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


@mcp.tool(
    name="list_files_by_extension",
    description="List files in a directory that have a specific file extension.",
)
def list_files_by_extension(directory_path: str, extension: str) -> List[str]:
    """Tool to list files with a specific extension in a directory

    Args:
        directory_path (str): Path to the directory
        extension (str): Extension of the files to list

    Returns:
        List[str]: List of files with the specific extension in the directory
    """
    list_of_files = list_files(directory_path=directory_path)
    return [file for file in list_of_files if file.endswith(extension)]


@mcp.tool(
    name="list_folders", description="List only folders/subdirectories in a directory."
)
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


@mcp.tool(name="read_file_contents", description="Read the contents of a text file.")
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


@mcp.tool(
    name="write_file_contents",
    description="Write content to a file, with optional overwrite permission.",
)
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


@mcp.tool(
    name="create_directory",
    description="Create a new directory and any necessary intermediate parent directories.",
)
def create_directory(directory_path: str) -> str:
    """Tool to create a directory

    Args:
        directory_path (str): Path to the directory

    Returns:
        str: Message indicating the directory has been created
    """
    os.makedirs(path=directory_path, exist_ok=True)
    return f"Directory '{directory_path}' has been created successfully."


@mcp.tool(name="move_or_rename", description="Move or rename a file or directory.")
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


@mcp.tool(
    name="copy_file_or_folder",
    description="Copy a file or directory folder recursively to a destination path.",
)
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


@mcp.tool(
    name="get_path_metadata",
    description="Get metadata properties (size, times, owner, etc.) for a file or directory.",
)
def get_path_metadata(path: str) -> dict:
    """Tool to get the metadata of a file or directory

    Args:
        path (str): Path to the file or directory

    Returns:
        dict: Metadata of the file or directory
    """
    metadata = os.stat(path=path)
    return metadata


@mcp.tool(
    name="path_exists", description="Check whether a file or directory path exists."
)
def path_exists(path: str) -> bool:
    """Tool to check if a path exists

    Args:
        path (str): Path to the file or directory

    Returns:
        bool: True if the path exists, False otherwise
    """
    return os.path.exists(path=path)


@mcp.tool(
    name="search_files",
    description="Search for files in a directory matching a query string in their filename.",
)
def search_files(directory_path: str, query: str) -> List[str]:
    """Tool to search for files in a directory

    Args:
        directory_path (str): Path to the directory
        query (str): Query to search for

    Returns:
        List[str]: List of files that match the query
    """
    list_of_files = list_files(directory_path=directory_path)
    return [file for file in list_of_files if query.lower() in file.lower()]


if __name__ == "__main__":
    mcp.run(transport="sse")
