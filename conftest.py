import pytest
from tests.api.test_fixture import User
from modules.api.clients.github import GitHub
from modules.common.database import Database

"""In this file defines the fixture functions 
to make them available to make them accessible across multiple test files."""


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
