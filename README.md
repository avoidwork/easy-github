# Easy GitHub

A GitHub tool for your LLM.

## Overview

`main.py` provides a Python interface to interact with the GitHub API, allowing you to fetch and display a user's public repositories, sorted by star count. The main functionality is encapsulated in the `Tools` class.

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
