"""MCP Server"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 03-May-2025
#  📖 Description: TODO
#
# **************************************************************************************************

import datetime
import zoneinfo
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("clock")


@mcp.tool()
def health() -> str:
    """Tool to check the health of the Clock MCP server

    Returns:
        str: Message indicating the health of the Clock MCP server
    """
    return "Clock MCP server is healthy."


@mcp.tool()
async def get_current_date_time_iso_format():
    """Get the current date and time in ISO format"""
    return datetime.datetime.now().isoformat()


@mcp.tool()
async def get_current_date_time_in_time_zone(time_zone: str):
    """Get the current date and time in a specific time zone"""
    return datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=time_zone)).isoformat()


if __name__ == "__main__":
    mcp.run(transport="stdio")
