import pytest
from tests.api.test_fixture import User
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage

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
def db():
    db = Database()
    yield db


@pytest.fixture
def ui_fix():
    paje_object = SignInPage()
    paje_object.go_to()
    yield paje_object

    paje_object.close()
