import pytest
import requests
import random


# User is able to search for an existing user
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


# User is able to search non-existent user
@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("butenkosergii")

    assert user["message"] == "Not Found"


# User is able to search for an existing repo
@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo("become-qa-auto")

    assert repo["total_count"] == 43
    assert "become-qa-auto" in repo["items"][0]["name"]


# User is able to search for non existing repo
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert repo["total_count"] == 0


# User is able to search for the repo with name that consists from 1 character
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo("s")

    assert repo["total_count"] != 0


# Tests API to list and view all the available emojis to use on GitHub
@pytest.mark.api
def test_all_emojis_can_be_found(github_api):
    emoji = github_api.get_emojis()
    random_emoji = random.choice(list(emoji))

    assert "message" not in emoji.keys()
    assert emoji[random_emoji].startswith("https://github")
    assert isinstance(random_emoji, str)
    assert len(emoji) == 1877


@pytest.mark.api
def test_can_be_found_special_emoji(github_api):
    emoji = github_api.get_emojis()

    assert "zombie" in emoji
    assert requests.get(emoji["zombie"]).status_code == 200


@pytest.mark.api
def test_cannot_be_found_emoji(github_api):
    emoji = github_api.get_emojis()

    assert "andrii" not in emoji


# Tests API to interact with commits


@pytest.mark.api
def test_commits_can_be_found(github_api):
    commits = github_api.list_commits("sergii-butenko-gl", "become-qa-auto-aug2020")

    assert isinstance(commits, list)
    assert commits[0]["commit"]["author"]["name"] == "Sergii Butenko"


@pytest.mark.api
def test_commits_cannot_be_found(github_api):
    commits = github_api.list_commits("butenkosergii", "become-qa-auto")

    assert isinstance(commits, dict)
    assert commits["message"] == "Not Found"


@pytest.mark.api
def test_chek_message_commit(github_api):
    commit = github_api.list_commits("AndriiSzyc", "SzycQAauto")
    assert commit[0]["commit"]["message"] != "null"


@pytest.mark.api
def test_chek_reponame_commit(github_api):
    commit = github_api.list_commits("AndriiSzyc", "SzycQAauto")
    assert "SzycQAauto" and "AndriiSzyc" in commit[0]["commit"]["tree"]["url"]


@pytest.mark.api
def test_parents(github_api):
    commit = github_api.list_commits("AndriiSzyc", "SzycQAauto")
    assert commit[-1]["parents"] == []
