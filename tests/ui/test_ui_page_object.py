from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Creating page object
    sign_in_page = SignInPage()

    # Enter 'https://github.com/login' page
    sign_in_page.go_to()

    # Try to log in to GitHub system
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Check that name of page is what we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close Browser
    sign_in_page.close()


@pytest.mark.ui
def test_get_create_account_page(ui_fix):
    ui_fix.get_create_acc_page()
    ui_fix.implicitly_wait(2)

    assert ui_fix.check_title("Join GitHub · GitHub")
