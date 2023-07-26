import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


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


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def sqlite_table_connection():
    table_connection = Database()
    yield table_connection
