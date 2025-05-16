"""Daily Status Update - Main Module"""

# -*- coding: utf-8 -*-
# **************************************************************************************************
#
#  🚀 Created by Srushanth Baride
#  🖥️ Author: Srushanth Baride
#  ✉️ Email: Srushanth.Baride@gmail.com
#  📅 Date: 16-May-2025
#  📖 Description: TODO
#
# **************************************************************************************************

import os
from datetime import datetime
import requests


def fetch_git_commits_for_today():
    """_summary_

    Raises:
        RuntimeError: _description_
    """

    def get_env_var(var_name, display_name=None):
        value = os.getenv(var_name)
        print(f"{display_name or var_name}: {value}")
        if not value:
            raise RuntimeError(f"Please set {var_name} environment variable.")
        return value

    github_token = get_env_var("GITHUB_TOKEN", "Token")
    github_username = get_env_var("GITHUB_USERNAME", "GitHub Username")

    # GitHub Search Commits endpoint requires this custom Accept header
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.cloak-preview",
    }

    print("Headers:", headers)

    today_date_str = datetime.now().strftime("%Y-%m-%d")

    print("Today's Date:", today_date_str)

    query = f"author:{github_username} author-date:{today_date_str}"
    params = {"q": query, "per_page": 100}
    url = "https://api.github.com/search/commits"

    commits = []
    while url:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        for item in data.get("items", []):
            commit = item["commit"]
            commits.append(
                {
                    "repo": item["repository"]["full_name"],
                    "sha": item["sha"],
                    "message": commit["message"].split("\n", 1)[0],
                    "date": commit["author"]["date"],
                }
            )

        # handle pagination: GitHub returns a Link header if there’s a next page
        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                next_url = part[part.find("<") + 1 : part.find(">")]
        url = next_url
        # after the first page, clear params so we don’t resend them in the `next` URL
        params = {}

    print(f"Total commits found: {len(commits)}")
    print("Commits:")
    for commit in commits:
        print(f"Repo: {commit['repo']}")
        print(f"SHA: {commit['sha']}")
        print(f"Message: {commit['message']}")
        print(f"Date: {commit['date']}")
        print("-" * 40)
    print("Done!")


if __name__ == "__main__":
    fetch_git_commits_for_today()
