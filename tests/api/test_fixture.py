import pytest


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Andrii"
        self.second_name = "Szyc"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.mark.change
def test_remove_name(user):
    """check that the username can be deleted"""
    user.name = ""
    assert user.name == ""


@pytest.mark.check
def test_name(user):
    """check that the name is Andrii"""
    assert user.name == "Andrii"


@pytest.mark.check
def test_second_name(user):
    """checks that the surname is Szyc"""
    assert user.second_name == "Szyc"
