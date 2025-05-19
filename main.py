"""
title: Easy GitHub
author: Jason Mulligan <jason.mulligan@avoidwork.com>
author_url: https://github.com/avoidwork
funding_url: https://github.com/avoidwork/easy-github
version: 1.0.0
"""

import requests
import json


class Tools:
    def __init__(self) -> None:
        self.citation = True
        self.base_url = "https://api.github.com"
        self.token = None
        pass

    def list_repos(
        self, username: str, top: int = 10, stars: int = 0, per_page: int = 200
    ) -> str:
        """
        List public repositories for a user ordered by stars.
        :param username: The GitHub username to get repositories for.
        :param top: The number of repositories to return.
        :param stars: The number of stars a repository must have to be included.
        :param per_page: The number of repositories in the API request.
        :return: List of the username's repositories sorted by stargazers.
        """
        stripped_username = username.strip().strip('"').strip("'")
        url = f"{self.base_url}/users/{stripped_username}/repos"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        params = {
            "page": 1,
            "per_page": per_page,
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        if not isinstance(data, list):
            return f"Failed to fetch repositories for {stripped_username}."
        if not data:
            return f"No repositories found for {stripped_username}."
        repo_list = [
            {
                "name": repo.get('name'),
                "url": repo.get("html_url"),
                "stars": repo.get("stargazers_count"),
            }
            for repo in data
            if repo.get("stargazers_count", 0) >= stars
        ]
        repo_list.sort(key=lambda x: x["stars"], reverse=True)
        if len(repo_list) > top:
            repo_list = repo_list[:top]
        result = f"""
Show a list of the top {len(repo_list)} results:

{json.dumps(repo_list)}
"""
        return result
