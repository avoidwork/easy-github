"""
title: Easy GitHub
author: Jason Mulligan <jason.mulligan@avoidwork.com>
author_url: https://github.com/avoidwork
funding_url: https://github.com/avoidwork/easy-github
version: 1.1.1
"""

import requests
import json

BASE_URL = "https://api.github.com"
TOKEN = None


class Tools:
    def __init__(self) -> None:
        self.citation = True
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
        url = f"{BASE_URL}/users/{stripped_username}/repos"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        params = {
            "page": 1,
            "per_page": per_page,
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        if not isinstance(data, list):
            return f"Failed to fetch repositories for {stripped_username}."
        if not data:
            return f"No repositories found for {stripped_username}."
        repo_list = [
            {
                "name": repo.get("name"),
                "url": repo.get("html_url"),
                "description": repo.get("description"),
                "stars": repo.get("stargazers_count"),
            }
            for repo in data
            if repo.get("stargazers_count", 0) >= stars
        ]
        repo_list.sort(key=lambda x: x["stars"], reverse=True)
        if len(repo_list) > top:
            repo_list = repo_list[:top]
        result = f"""Show a list of the top {len(repo_list)} results:

{json.dumps(repo_list)}
"""
        return result

    def get_user(self, username: str) -> str:
        """
        Get details for a GitHub user.
        :param username: The GitHub username to get details for.
        :return: User details as a JSON string.
        """
        url = f"{BASE_URL}/users/{username}"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            return f"Failed to fetch user {username}."
        result = f"""Show the details of the user {username} with this data:

{json.dumps(resp.json())}
"""
        return result

    def get_repo(self, owner: str, repo: str) -> str:
        """
        Get details for a specific repository.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :return: Repository details as a JSON string.
        """
        url = f"{BASE_URL}/repos/{owner}/{repo}"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            return f"Failed to fetch repository {owner}/{repo}."
        result = f"""Show the details of the repository {owner}/{repo} with this data:

{json.dumps(resp.json())}
"""
        return result

    def list_issues(
        self, owner: str, repo: str, state: str = "open", per_page: int = 100
    ) -> str:
        """
        List issues for a repository.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param state: The state of the issues (open, closed, all).
        :param per_page: Number of issues per page.
        :return: List of issues as a JSON string.
        """
        url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        params = {
            "state": state,
            "per_page": per_page,
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            return f"Failed to fetch issues for {owner}/{repo}."
        data = resp.json()
        result = f"""Show the issues of the repository {owner}/{repo} with this data:

{json.dumps(data)}
"""
        return result

    def create_issue(self, owner: str, repo: str, title: str, body: str = "") -> str:
        """
        Create an issue in a repository. Requires authentication.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param title: The title of the issue.
        :param body: The body of the issue.
        :return: The created issue as a JSON string or an error message.
        """
        url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        if not TOKEN:
            return "Authentication token required to create an issue."
        headers["Authorization"] = f"Bearer {TOKEN}"
        payload = {
            "title": title,
            "body": body,
        }
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code not in (200, 201):
            return f"Failed to create issue: {resp.text}"
        result = f"""Show the created issue with this data:

{json.dumps(resp.json())}
"""
        return result

    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        top: int = 10,
        per_page: int = 30,
    ) -> str:
        """
        List pull requests for a repository.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param state: The state of the pull requests (open, closed, all).
        :param top: The number of repositories to return.
        :param per_page: Number of pull requests per page.
        :return: List of pull requests as a JSON string.
        """
        url = f"{BASE_URL}/repos/{owner}/{repo}/pulls"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        params = {
            "state": state,
            "per_page": per_page,
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            return f"Failed to fetch pull requests for {owner}/{repo}."
        data = resp.json()
        if len(data) > top:
            data = data[:top]
        result = f"""Show the pull requests of the repository {owner}/{repo} with this data:

{json.dumps(data)}
"""
        return result

    def search_github(
        self,
        search_type: str,
        query: str,
        top: int = 10,
        per_page: int = 200,
        params: dict = None,
    ) -> str:
        """
        Perform a search on GitHub.
        :param search_type: The type of search (repositories, issues, code, users, topics, etc.).
        :param query: The search query string.
        :param top: The number of results to return.
        :param per_page: The number of repositories in the API request.
        :param params: Optional extra parameters for the search (dict).
        :return: Search results as a JSON string or error message.
        """
        allowed_types = ["repositories", "issues", "code", "users", "topics", "commits"]
        if search_type not in allowed_types:
            return f"search_type must be one of: {', '.join(allowed_types)}."
        url = f"{BASE_URL}/search/{search_type}"
        headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        all_params = {
            "q": query,
            "per_page": per_page,
        }
        if params:
            all_params.update(params)
        resp = requests.get(url, headers=headers, params=all_params)
        if resp.status_code != 200:
            return f"Failed to search {search_type}: {resp.text}"
        data = resp.json().get("items", [])
        items = [
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "url": repo.get("html_url"),
                "stars": repo.get("stargazers_count"),
            }
            for repo in data
        ]
        items.sort(key=lambda x: x["stars"], reverse=True)
        if len(items) > top:
            items = items[:top]
        result = f"""Show the top {len(items)} results of the {search_type} search for query '{query}' with this data:

{json.dumps(items)}
"""
        return result
