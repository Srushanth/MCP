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


if __name__ == "__main__":
    mcp.run(transport="stdio")
