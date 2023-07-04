import pytest


@pytest.mark.check
def test_check_name(user):
    assert user.name == "Andrii"


@pytest.mark.check
def test_check_second_name(user):
    assert user.second_name == "Szyc"


# def test_change_name():
#     user = User()
#     user.create()

#     assert user.name == 'Andrii'
#     user.remove()

# def test_change_second_name():
#     user = User()
#     user.create()

#     assert user.second_name == 'Szyc'
#     user.remove()
