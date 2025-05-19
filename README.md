# Easy GitHub

A GitHub tool for your LLM.

## Overview

`main.py` provides a Python interface to interact with the GitHub API, allowing you to fetch and display a user's public repositories, sorted by star count. The main functionality is encapsulated in the `Tools` class.

## Example LLM Prompts

Here are some example prompts you can use with your LLM to interact with Easy GitHub:

### List Repositories (`list_repos`)
- `Show me the top 5 repositories for the GitHub user "octocat".`
- `List the top 10 repositories for user "torvalds" with at least 1000 stars.`
- `Get the most popular repositories for "microsoft" on GitHub.`
- `Give me the URLs of the top 3 repositories for "facebook" with more than 5000 stars.`
- `What are the most starred repositories for the user "avoidwork"?`

### List Issues (`list_issues`)
- `Show me all open issues for the repository "octocat/Hello-World".`
- `List closed issues for "avoidwork/easy-github".`

### Create Issue (`create_issue`)
- `Create an issue in "avoidwork/easy-github" titled "Bug: login fails" with the body "Steps to reproduce: ...".`
- `Open a new issue called "Feature request: dark mode" in the repo "octocat/Hello-World".`

### Get Repository Details (`get_repo`)
- `Show details for the repository "torvalds/linux".`
- `Get information about the repo "avoidwork/easy-github".`

### Get User Details (`get_user`)
- `Get details for the GitHub user "octocat".`
- `Show information about the user "avoidwork".`

### Search GitHub (`search_github`)
- `Search for repositories about "machine learning" with at least 500 stars.`
- `Find users related to "openai" on GitHub.`
- `Show me issues mentioning "bug" in the repo "octocat/Hello-World".`

### List Pull Requests (`list_pull_requests`)
- `List open pull requests for "octocat/Hello-World".`
- `Show closed pull requests in the repo "avoidwork/easy-github".`

## About

- Author: Jason Mulligan <jason.mulligan@avoidwork.com>
- GitHub: https://github.com/avoidwork
- Funding: https://github.com/avoidwork/easy-github
- Version: 1.0.0
