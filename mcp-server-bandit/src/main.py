"""MCP Server for Bandit"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description:
#   - Security and vulnerability scanner for Python using Bandit
#   - Checks for security vulnerabilities in a Python file
#   - Checks for security vulnerabilities in a dependency file
#   - Checks for security vulnerabilities in a project/directory
#   - Checks for security vulnerabilities in a raw Python code snippet
#
# **************************************************************************************************


import os
import sys
import json
import tempfile
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bandit")


@mcp.tool(name="health", description="Check the health of the Bandit MCP server.")
def health() -> str:
    """Check the health of the Bandit MCP server.

    Returns:
        str: Message indicating the health of the Bandit MCP server.
    """
    try:
        # Run bandit --version
        result = subprocess.run(
            ["bandit", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            version = result.stdout.strip().split("\n")[0]
            return f"Bandit MCP server is healthy. {version}"
        else:
            return f"Bandit MCP server health check failed: {result.stderr or result.stdout}"
    except Exception as e:
        return f"Bandit MCP server is unhealthy: {str(e)}"


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
        dependency_file (str): The path to the dependency file (e.g. requirements.txt or pyproject.toml) or directory to scan.

    Returns:
        dict: Dictionary containing the audit results or error details.
    """
    if not os.path.exists(dependency_file):
        return {"error": f"Path '{dependency_file}' does not exist."}

    cmd = [sys.executable, "-m", "pip_audit", "-f", "json"]

    if os.path.isfile(dependency_file) and dependency_file.endswith(".txt"):
        cmd.extend(["-r", dependency_file])
    else:
        # If it's a directory or a file like pyproject.toml, pass the directory path
        if os.path.isfile(dependency_file):
            cmd.append(os.path.dirname(os.path.abspath(dependency_file)))
        else:
            cmd.append(dependency_file)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

        # Parse stdout as json if possible
        try:
            if result.stdout.strip():
                stdout = result.stdout
                start = stdout.find("{")
                end = stdout.rfind("}")
                if start != -1 and end != -1:
                    json_str = stdout[start : end + 1]
                    audit_data = json.loads(json_str)
                    return {"vulnerabilities": audit_data, "stderr": result.stderr}

            return {
                "output": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
            }
        except Exception as json_err:
            return {
                "error": f"Failed to parse pip-audit JSON output: {str(json_err)}",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
            }

    except Exception as e:
        return {"error": f"Error running pip-audit: {str(e)}"}


@mcp.tool()
def scan_vulnerabilities_in_project(
    project_path: str = ".",
    severity_level: str = "all",
    confidence_level: str = "all",
) -> dict:
    """Scan all Python files in a project/directory recursively using Bandit.

    Args:
        project_path (str): Path to the project directory. Defaults to ".".
        severity_level (str): Report only issues of this level or higher (all, low, medium, high). Defaults to "all".
        confidence_level (str): Report only issues of this level or higher (all, low, medium, high). Defaults to "all".

    Returns:
        dict: Scan results including issues found or error messages.
    """
    if not os.path.isdir(project_path):
        return {"error": f"Path '{project_path}' is not a valid directory."}

    cmd = [sys.executable, "-m", "bandit", "-r", project_path, "-f", "json"]

    if severity_level in ["low", "medium", "high"]:
        cmd.extend(["--severity-level", severity_level])
    if confidence_level in ["low", "medium", "high"]:
        cmd.extend(["--confidence-level", confidence_level])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

        try:
            if result.stdout.strip():
                return json.loads(result.stdout)
            return {
                "output": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
            }
        except Exception as json_err:
            return {
                "error": f"Failed to parse Bandit JSON output: {str(json_err)}",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
            }
    except Exception as e:
        return {"error": f"Error running Bandit on project: {str(e)}"}


@mcp.tool()
def scan_vulnerabilities_in_code(code: str) -> dict:
    """Scan a raw Python code snippet for security vulnerabilities using Bandit.

    Args:
        code (str): The Python code snippet to scan.

    Returns:
        dict: Scan results containing stdout and stderr.
    """
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_file_name = temp_file.name

        try:
            result = subprocess.run(
                ["bandit", temp_file_name],
                capture_output=True,
                text=True,
                check=False,
            )
            # Remove reference to the temp file path in the output for cleaner display
            stdout = result.stdout or ""
            stderr = result.stderr or ""
            stdout = stdout.replace(temp_file_name, "snippet.py")
            stderr = stderr.replace(temp_file_name, "snippet.py")

            return {"stdout": stdout, "stderr": stderr, "exit_code": result.returncode}
        finally:
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
    except Exception as e:
        return {"error": f"Error running Bandit on code snippet: {str(e)}"}


if __name__ == "__main__":
    mcp.run(transport="stdio")
