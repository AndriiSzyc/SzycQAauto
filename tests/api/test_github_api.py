import pytest
import requests
import random


@pytest.mark.api
def test_user_exists(github_api):
    # User is able to search for an existing user
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    # User is able to search non-existent user
    user = github_api.get_user("butenkosergii")

    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    # User is able to search for an existing repo
    repo = github_api.search_repo("become-qa-auto")

    assert repo["total_count"] == 43
    assert "become-qa-auto" in repo["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    # User is able to search for non existing repo
    repo = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert repo["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    # User is able to search for the repo with name that consists from 1 character
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

    assert "message" not in emoji


# Tests API to interact with commits

@pytest.mark.api
def test_commits_can_be_found(github_api):
    commits = github_api.list_commits("AndriiSzyc", "SzycQAauto")

    assert isinstance(commits, list)
    assert commits[0]["commit"]["author"]["name"] == "Andrii Shyts"


@pytest.mark.api
def test_commits_cannot_be_found(github_api):
    commits = github_api.list_commits("butenkosergii", "become-qa-auto")

    assert isinstance(commits, dict)
    assert commits["message"] == "Not Found"


# Positive tests to query parameters to interact with commits

@pytest.mark.api
def test_chek_SHA_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc",
        "IT_test_drive",
        {"sha": "fc13642796f72ec77b7820e476f3739d3f9f263f"},
    )

    assert len(commits) == 4
    assert commits[0]["parents"][0]["sha"] == commits[1]["sha"]


@pytest.mark.api
def test_chek_PATH_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "SzycQAauto", {"path": "config/config.py"}
    )

    assert len(commits) == 1
    assert commits[0]["commit"]["author"]["name"] == "Andrii Shyts"


@pytest.mark.api
def test_chek_AUTHOR_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "IT_test_drive", {"author": "andrewszyc@ukr.net"}
    )

    assert len(commits) == 1
    assert commits[0]["commit"]["author"]["name"] == "andrii"
    assert commits[0]["commit"]["author"]["email"] == "andrewszyc@ukr.net"


@pytest.mark.api
def test_chek_COMMITER_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "IT_test_drive", {"committer": "AndriiSzyc"}
    )

    assert len(commits) == 4
    assert commits[-1]["commit"]["committer"]["name"] == "andrii"
    assert commits[-1]["commit"]["committer"]["email"] == "andrewszyc@ukr.net"


@pytest.mark.api
def test_chek_SINCE_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "IT_test_drive", {"since": "2023-03-25T08:37:53Z"}
    )

    assert len(commits) == 6
    assert commits[-1]["commit"]["author"]["date"] == "2023-03-25T08:37:53Z"
    assert commits[-1]["commit"]["message"] == "add docker"


@pytest.mark.api
def test_chek_UNTIL_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "SzycQAauto", {"until": "2023-07-04T10:14:43Z"}
    )

    assert len(commits) == 13
    assert commits[0]["commit"]["author"]["date"] == "2023-07-04T10:14:43Z"
    assert commits[0]["commit"]["message"] == "Create empty project"


@pytest.mark.api
def test_chek_PER_PAGE_params(github_api):
    commits = github_api.list_commits("AndriiSzyc", "SzycQAauto", {"per_page": 2})

    assert len(commits) == 2


@pytest.mark.api
def test_chek_PAGE_params(github_api):
    commits = github_api.list_commits(
        "AndriiSzyc", "SzycQAauto", {"per_page": 10, "page": 2}
    )

    assert len(commits) == 10
