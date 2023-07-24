import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("butenkosergii")

    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo("become-qa-auto")

    assert repo["total_count"] == 42
    assert "become-qa-auto" in repo["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert repo["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo("s")

    assert repo["total_count"] != 0


# Individual tasks


@pytest.mark.api
def test_all_emojis_can_be_found(github_api):
    emoji = github_api.search_emoji()
    assert "messege" not in emoji


@pytest.mark.api
def test_can_be_found_special_emoji(github_api):
    emoji = github_api.search_emoji()
    assert "zombie" in emoji


@pytest.mark.api
def test_cannot_be_found_emoji(github_api):
    emoji = github_api.search_emoji()
    assert "andrii" not in emoji


@pytest.mark.api
def test_not_finde_commits(github_api):
    commit = github_api.interact_with_commits("butenkosergii", "become-qa-auto")
    assert commit["message"] == "Not Found"


@pytest.mark.api
def test_finde_email_commit(github_api):
    commit = github_api.interact_with_commits("AndriiSzyc", "SzycQAauto")
    assert commit[0]["commit"]["committer"]["email"] == "andrewszyc@ukr.net"


@pytest.mark.api
def test_chek_message_commit(github_api):
    commit = github_api.interact_with_commits("AndriiSzyc", "SzycQAauto")
    assert commit[0]["commit"]["message"] != "null"


@pytest.mark.api
def test_chek_reponame_commit(github_api):
    commit = github_api.interact_with_commits("AndriiSzyc", "SzycQAauto")
    assert "SzycQAauto" and "AndriiSzyc" in commit[0]["commit"]["tree"]["url"]
