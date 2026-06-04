"""MCP Server for pytest"""

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


mcp = FastMCP("pytest")

if __name__ == "__main__":
    mcp.run(transport="stdio")
