# Easy GitHub

A GitHub tool for your LLM.

## Overview

`main.py` provides a Python interface to interact with the GitHub API, allowing you to fetch and display a user's public repositories, sorted by star count. The main functionality is encapsulated in the `Tools` class.

## Usage

1. **Install dependencies:**
   Ensure you have `requests` installed:
   ```bash
   pip install requests
   ```

2. **Using main.py in your code:**
   ```python
   from main import Tools

   tools = Tools()
   username = "octocat"  # Replace with the GitHub username you want to query
   top_repos = tools.list_repos(username, top=5)
   print(top_repos)
   ```

   - `username`: GitHub username to fetch repositories for
   - `top`: Number of top repositories to display (default: 10)
   - `per_page`: Number of repositories to fetch per API request (default: 200)

3. **Sample Output:**
   The output will be a JSON-formatted list of repositories, sorted by star count, for the specified user.

## Example LLM Prompts

Here are some example prompts you can use with your LLM to interact with Easy GitHub:

- `Show me the top 5 repositories for the GitHub user "octocat".`
- `List the top 10 repositories for user "torvalds" with at least 1000 stars.`
- `Get the most popular repositories for "microsoft" on GitHub.`
- `Give me the URLs of the top 3 repositories for "facebook" with more than 5000 stars.`
- `What are the most starred repositories for the user "avoidwork"?`

These prompts leverage the `list_repos` method, allowing you to specify the username, number of repositories, and minimum star count as parameters.

## About

- Author: Jason Mulligan <jason.mulligan@avoidwork.com>
- GitHub: https://github.com/avoidwork
- Funding: https://github.com/avoidwork/easy-github
- Version: 1.0.0
