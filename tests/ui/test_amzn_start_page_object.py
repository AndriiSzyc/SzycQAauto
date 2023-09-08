import pytest


@pytest.mark.ui_amzn
def test_check_incorrect_username_page_object(ui_for_amzn):
    ui_for_amzn.try_login("myemail@mistakeinemail.com")
    ui_for_amzn.implicitly_wait(2)

    assert ui_for_amzn.check_title("Amazon Sign-In")


@pytest.mark.ui_amzn
def test_empty_cart(ui_for_amzn):
    ui_for_amzn.go_cart()

    assert ui_for_amzn.check_text_empty_cart("Your Amazon Cart is empty")


@pytest.mark.ui_amzn
def test_search_amzn(ui_for_amzn):
    ui_for_amzn.search_amzn("half life")

    assert ui_for_amzn.check_title("Amazon.com : half life")
