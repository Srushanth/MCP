"""Agent"""

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
from google.adk.agents import Agent  # type: ignore


def get_current_date_time_iso_format():
    """Get the current date and time in ISO format"""
    return datetime.datetime.now().isoformat()


def get_current_date_time_in_time_zone(time_zone: str):
    """Get the current date and time in a specific time zone"""
    return datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=time_zone)).isoformat()


root_agent = Agent(
    name="clock_agent",
    model="gemini-3.1-pro-preview",
    description="Agent to get the current time",
    instruction="Get the current time",
    tools=[get_current_date_time_iso_format, get_current_date_time_in_time_zone],
)
