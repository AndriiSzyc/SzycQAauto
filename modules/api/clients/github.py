import requests
import os


class GitHub:
    HEADERS = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + os.environ.get("GIT_TOKEN"),
        "X-GitHub-Api-Versio": "2022-11-28",
    }

    def get_user(self, username):
        r = requests.get(
            f"https://api.github.com/users/{username}", headers=self.HEADERS
        )
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            headers=self.HEADERS,
            params={"q": name},
        )
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis", headers=self.HEADERS)
        body = r.json()

        return body

    def list_commits(self, owner_name, repo_name):
        r = requests.get(
            f"https://api.github.com/repos/{owner_name}/{repo_name}/commits",
            headers=self.HEADERS,
        )
        body = r.json()

        return body
