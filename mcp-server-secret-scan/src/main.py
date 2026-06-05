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


if __name__ == "__main__":
    mcp.run(transport="stdio")
