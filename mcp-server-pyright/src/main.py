"""MCP Server for Pyright"""

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
import os
import sys
import json
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Pyright")


@mcp.tool()
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


@mcp.tool()
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


if __name__ == "__main__":
    mcp.run(transport="stdio")
