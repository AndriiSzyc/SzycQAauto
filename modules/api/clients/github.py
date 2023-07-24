import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # Individual tasks

    def search_emoji(self):
        r = requests.get("https://api.github.com/emoji")
        body = r.json()

        return body

    def interact_with_commits(self, owner_name, repo_name):
        r = requests.get(
            f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
        )
        body = r.json()

        return body
