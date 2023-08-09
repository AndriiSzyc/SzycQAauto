import requests
import os


class GitToken:
    @classmethod
    def get_token(cls):
        return os.environ.get("GIT_TOKEN")


class GitHub:
    HEADERS = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + GitToken.get_token(),
        "X-GitHub-Api-Versio": "2022-11-28",
    }

    def get_user(self, username):
        r = requests.get(
            f"https://api.github.com/users/{username}", headers=GitHub.HEADERS
        )
        body = r.json()

        return body

    def search_repo(self, reponame):
        r = requests.get(
            "https://api.github.com/search/repositories",
            headers=GitHub.HEADERS,
            params={"q": reponame},
        )
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis", headers=GitHub.HEADERS)
        body = r.json()

        return body

    def list_commits(self, owner_name, repo_name, params=None):
        r = requests.get(
            f"https://api.github.com/repos/{owner_name}/{repo_name}/commits",
            headers=GitHub.HEADERS,
            params=params,
        )
        body = r.json()

        return body
