"""MCP Server for Pyright"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 04-June-2026
#  📖 Description: Static type checking, type stub generation, and package verification using Pyright
#
# **************************************************************************************************


import os
import sys
import json
import tempfile
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Pyright", host="localhost", port=3004)


@mcp.tool(
    name="health", description="Check the health and version of the Pyright MCP server."
)
def health() -> str:
    """Check the health and version of the Pyright MCP server.

    Returns:
        str: Message indicating health status and Pyright version.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pyright", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            return f"Pyright MCP server is healthy. Pyright version: {version}"
        else:
            return f"Pyright MCP server health check failed: {result.stderr or result.stdout}"
    except Exception as e:
        return f"Pyright MCP server is unhealthy: {str(e)}"


@mcp.tool(
    name="check_types_in_file",
    description="Check types in a specific Python file using Pyright.",
)
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


@mcp.tool(
    name="check_types_in_project",
    description="Check types project-wide or in a specified directory using Pyright.",
)
def check_types_in_project(project_path: str = ".") -> str:
    """Check types in the specified project directory using pyright.

    Args:
        project_path (str): The path to the project directory to check. Defaults to ".".

    Returns:
        str: The results of the type check.
    """
    if not os.path.isdir(project_path):
        return f"Error: '{project_path}' is not a valid directory."

    # Check if a pyrightconfig.json or pyproject.toml already exists in the project
    has_config = False
    for filename in ["pyrightconfig.json", "pyproject.toml"]:
        if os.path.exists(os.path.join(project_path, filename)):
            has_config = True
            break

    temp_config_path = os.path.join(project_path, "pyrightconfig.temp.json")

    try:
        cmd = [sys.executable, "-m", "pyright"]

        if has_config:
            cmd.append(project_path)
        else:
            # Create a temporary config to enable recursive checking while ignoring virtual environments
            config_data = {
                "reportMissingImports": True,
                "reportMissingTypeStubs": False,
                "reportUnknownMemberType": False,
                "reportUnknownParameterType": False,
                "reportUnknownVariableType": False,
                "reportUnusedImport": False,
                "reportUnusedClass": False,
                "reportUnusedFunction": False,
                "reportUnusedVariable": False,
                "strict": True,
                "ignore": [
                    "**/__pycache__/**",
                    ".venv/**",
                    ".env/**",
                    "venv/**",
                    "ENV/**",
                    "env/**",
                    ".env.local/**",
                ],
                "exclude": ["**/*.pyi", "**/node_modules/**"],
            }
            with open(temp_config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4)

            cmd.extend(["-p", temp_config_path])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout or result.stderr or ""
        if result.returncode == 0:
            return f"Project-wide type checking passed:\n{output}"
        else:
            return f"Project-wide type checking failed:\n{output}"

    except Exception as e:
        return f"Error running pyright on project '{project_path}': {str(e)}"
    finally:
        if not has_config and os.path.exists(temp_config_path):
            try:
                os.remove(temp_config_path)
            except Exception:
                pass


@mcp.tool(
    name="create_type_stubs",
    description="Generate type stub files (.pyi) for a third-party package using Pyright.",
)
def create_type_stubs(package_name: str, project_path: str = ".") -> str:
    """Generate type stub files (.pyi) for a third-party package using pyright.

    Args:
        package_name (str): The name of the package/import to generate stubs for.
        project_path (str): The path to the project directory. Defaults to ".".

    Returns:
        str: The results of the stub generation.
    """
    if not os.path.isdir(project_path):
        return f"Error: '{project_path}' is not a valid directory."

    try:
        # Pyright creates stubs relative to the current working directory, or a specified project.
        result = subprocess.run(
            [sys.executable, "-m", "pyright", "--createstub", package_name],
            capture_output=True,
            text=True,
            check=False,
            cwd=project_path,
        )
        output = result.stdout or result.stderr or ""
        if result.returncode == 0:
            return f"Successfully created type stubs for package '{package_name}':\n{output}"
        else:
            return (
                f"Failed to create type stubs for package '{package_name}':\n{output}"
            )
    except Exception as e:
        return f"Error creating type stubs: {str(e)}"


@mcp.tool(
    name="verify_type_completeness",
    description="Verify the type completeness of a py.typed package.",
)
def verify_type_completeness(package_name: str, project_path: str = ".") -> str:
    """Verify the type completeness of a py.typed package.

    Args:
        package_name (str): The name of the package to verify.
        project_path (str): The path to the project directory. Defaults to ".".

    Returns:
        str: The type completeness report.
    """
    if not os.path.isdir(project_path):
        return f"Error: '{project_path}' is not a valid directory."

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pyright", "--verifytypes", package_name],
            capture_output=True,
            text=True,
            check=False,
            cwd=project_path,
        )
        output = result.stdout or result.stderr or ""
        if result.returncode == 0:
            return (
                f"Type completeness verification passed for '{package_name}':\n{output}"
            )
        else:
            return f"Type completeness verification failed/incomplete for '{package_name}':\n{output}"
    except Exception as e:
        return f"Error verifying type completeness: {str(e)}"


@mcp.tool(
    name="check_types_in_code",
    description="Check types in a raw Python code snippet using Pyright.",
)
def check_types_in_code(code: str) -> str:
    """Check types in a raw Python code snippet using pyright.

    Args:
        code (str): The Python code to check.

    Returns:
        str: The results of the type check.
    """
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_file_name = temp_file.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "pyright", temp_file_name],
                capture_output=True,
                text=True,
                check=False,
            )
            # Remove reference to the temp file path in the output for cleaner display
            output = result.stdout or result.stderr or ""
            output = output.replace(temp_file_name, "snippet.py")

            if result.returncode == 0:
                return f"Type checking passed for code snippet:\n{output}"
            else:
                return f"Type checking failed for code snippet:\n{output}"
        finally:
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
    except Exception as e:
        return f"Error running type check on code snippet: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse")
