"""MCP Server for Secrets & Credentials Scanning"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 05-June-2026
#  📖 Description: Scans files, directories, and code snippets for secrets and credentials.
#
# **************************************************************************************************

import importlib.metadata
import os
import tempfile
from typing import Any, Dict, List, Optional
from detect_secrets import SecretsCollection
from detect_secrets.settings import default_settings
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("secret-scan")


@mcp.tool(
    name="health",
    description="Check the health and version of the Secrets Scanner MCP server.",
)
def health() -> str:
    """Tool to check the health and version of the Secrets Scanner MCP server.

    Returns:
        str: Message indicating the health and version of the server.
    """
    version = get_detect_secrets_version()
    return f"Secrets Scanner MCP server is healthy. detect-secrets version: {version}"


def get_detect_secrets_version() -> str:
    """Helper to get detect-secrets package version."""
    try:
        return importlib.metadata.version("detect-secrets")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def is_binary_file(file_path: str) -> bool:
    """Check if a file is binary by attempting to read a small UTF-8 chunk."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read(1024)
        return False
    except (UnicodeDecodeError, PermissionError):
        return True


def read_line_from_file(file_path: str, line_number: int) -> str:
    """Helper to read a specific line from a file (1-indexed)."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for idx, line in enumerate(f, start=1):
                if idx == line_number:
                    return line.strip()
    except Exception as e:
        return f"<Error reading line: {str(e)}>"
    return ""


@mcp.tool(
    name="scan_file",
    description="Scan a single file for secrets, credentials, and API keys.",
)
def scan_file(file_path: str) -> Dict[str, Any]:
    """Scan a single file for credentials.

    Args:
        file_path (str): Absolute path to the file to scan.

    Returns:
        dict: A dictionary containing the list of found secrets or an error message.
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}", "secrets": []}

    if not os.path.isfile(file_path):
        return {"error": f"Path is not a file: {file_path}", "secrets": []}

    if is_binary_file(file_path):
        return {
            "error": f"File is binary and cannot be scanned: {file_path}",
            "secrets": [],
        }

    secrets = SecretsCollection()
    try:
        with default_settings():
            secrets.scan_file(file_path)
    except Exception as e:
        return {"error": f"Error scanning file: {str(e)}", "secrets": []}

    findings = []
    json_results = secrets.json()

    # The JSON output format from detect-secrets maps filenames to lists of potential secrets.
    for filename, secret_list in json_results.items():
        for secret in secret_list:
            line_no = secret.get("line_number", 0)
            line_content = (
                read_line_from_file(file_path, line_no) if line_no > 0 else ""
            )
            findings.append(
                {
                    "type": secret.get("type", "Unknown Secret"),
                    "line_number": line_no,
                    "hashed_secret": secret.get("hashed_secret"),
                    "line_content": line_content,
                    "is_verified": secret.get("is_verified", False),
                }
            )

    return {
        "file_path": file_path,
        "secrets_found_count": len(findings),
        "secrets": findings,
    }


@mcp.tool(
    name="scan_code",
    description="Scan a raw code snippet or string for secrets, credentials, and API keys.",
)
def scan_code(code: str) -> Dict[str, Any]:
    """Scan a raw code snippet for credentials.

    Args:
        code (str): The raw code snippet or string to scan.

    Returns:
        dict: A dictionary containing the list of found secrets or an error message.
    """
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        secrets = SecretsCollection()
        with default_settings():
            secrets.scan_file(temp_file_path)

        findings = []
        json_results = secrets.json()
        code_lines = code.splitlines()

        for filename, secret_list in json_results.items():
            for secret in secret_list:
                line_no = secret.get("line_number", 0)
                line_content = ""
                if 0 < line_no <= len(code_lines):
                    line_content = code_lines[line_no - 1].strip()

                findings.append(
                    {
                        "type": secret.get("type", "Unknown Secret"),
                        "line_number": line_no,
                        "hashed_secret": secret.get("hashed_secret"),
                        "line_content": line_content,
                        "is_verified": secret.get("is_verified", False),
                    }
                )

        return {"secrets_found_count": len(findings), "secrets": findings}
    except Exception as e:
        return {"error": f"Error scanning code snippet: {str(e)}", "secrets": []}
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


@mcp.tool(
    name="scan_directory",
    description="Recursively scan a directory for secrets, credentials, and API keys.",
)
def scan_directory(
    directory_path: str, exclude_patterns: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Recursively scan a directory for secrets, ignoring binary and metadata folders.

    Args:
        directory_path (str): Absolute path to the directory to scan.
        exclude_patterns (list, optional): Additional substrings to exclude in file paths.

    Returns:
        dict: Scanned directory summary and list of found secrets grouped by file.
    """
    if not os.path.exists(directory_path):
        return {
            "error": f"Directory not found: {directory_path}",
            "files_scanned_count": 0,
            "results": {},
        }

    if not os.path.isdir(directory_path):
        return {
            "error": f"Path is not a directory: {directory_path}",
            "files_scanned_count": 0,
            "results": {},
        }

    # Standard directories and files to ignore
    default_ignores = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".mypy_cache",
        ".ruff_cache",
        ".vscode",
        ".idea",
        "build",
        "dist",
    }

    scanned_files_count = 0
    results = {}

    for root, dirs, files in os.walk(directory_path):
        # In-place modify dirs list to skip ignored directories recursively
        dirs[:] = [d for d in dirs if d not in default_ignores]

        for file in files:
            file_path = os.path.join(root, file)

            # Check exclusions
            should_exclude = False
            if exclude_patterns:
                for pattern in exclude_patterns:
                    if pattern in file_path:
                        should_exclude = True
                        break
            if should_exclude:
                continue

            if is_binary_file(file_path):
                continue

            scanned_files_count += 1

            # Run scan_file internal logic
            secrets = SecretsCollection()
            try:
                with default_settings():
                    secrets.scan_file(file_path)
            except Exception:
                # Skip files that cause errors during parsing
                continue

            json_results = secrets.json()
            findings = []

            for filename, secret_list in json_results.items():
                for secret in secret_list:
                    line_no = secret.get("line_number", 0)
                    line_content = (
                        read_line_from_file(file_path, line_no) if line_no > 0 else ""
                    )
                    findings.append(
                        {
                            "type": secret.get("type", "Unknown Secret"),
                            "line_number": line_no,
                            "hashed_secret": secret.get("hashed_secret"),
                            "line_content": line_content,
                            "is_verified": secret.get("is_verified", False),
                        }
                    )

            if findings:
                # Use relative path as key for readability
                rel_path = os.path.relpath(file_path, directory_path)
                results[rel_path] = findings

    return {
        "directory_path": directory_path,
        "files_scanned_count": scanned_files_count,
        "total_secrets_found": sum(len(f) for f in results.values()),
        "results": results,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
