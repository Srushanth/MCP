"""MCP Server for Bandit"""

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

mcp = FastMCP("bandit")


@mcp.tool(description="Scans for security vulnerabilities in a Python file")
def scan_vulnerabilities_in_file(file_path: str) -> dict:
    """Scans for security vulnerabilities in a Python file.

    Args:
        file_path (str): The path to the Python file to scan.

    Returns:
        dict: Dictionary containing the stdout and stderr of the Bandit scan.
    """
    try:
        result = subprocess.run(
            ["bandit", file_path],
            capture_output=True,
            text=True,
            check=True,
        )
        return {"stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"stdout": e.stdout, "stderr": e.stderr}


@mcp.tool()
def check_dependencies_vulnerabilities(dependency_file: str) -> dict:
    """Check for security vulnerabilities in a dependency file.

    Args:
        dependency_file (str): The path to the dependency file to scan.

    Returns:
        dict: Dictionary containing the stdout and stderr of the Bandit scan.
    """
    try:
        result = subprocess.run(
            ["bandit", "-r", dependency_file],
            capture_output=True,
            text=True,
            check=True,
        )
        return {"stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"stdout": e.stdout, "stderr": e.stderr}


if __name__ == "__main__":
    mcp.run(transport="stdio")
